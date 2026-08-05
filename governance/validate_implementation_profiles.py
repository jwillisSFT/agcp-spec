#!/usr/bin/env python3
"""Validate AGCP Implementation Profile packages.

This validator is intentionally scoped to profile format version 1.1.0. The
profile schema uses integer numeric fields and ASCII object keys; the
canonicalizer rejects floating-point values and non-ASCII keys so the local
serialization remains equivalent to RFC 8785 JCS for this controlled format.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.tokens import AliasToken, AnchorToken, TagToken


class StrictJSONSafeLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: StrictJSONSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError(f"YAML object key must be a string: {key!r}")
        if key == "<<":
            raise ValueError("YAML merge keys are prohibited")
        if key in mapping:
            raise ValueError(f"Duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictJSONSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping,
)


def reject_prohibited_yaml(text: str) -> None:
    for token in yaml.scan(text):
        if isinstance(token, AnchorToken):
            raise ValueError(f"YAML anchors are prohibited: {token.value}")
        if isinstance(token, AliasToken):
            raise ValueError(f"YAML aliases are prohibited: {token.value}")
        if isinstance(token, TagToken):
            raise ValueError("Explicit YAML tags are prohibited")


def assert_json_compatible(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"Non-finite numeric value at {path}")
        raise ValueError(f"Floating-point values are not permitted by profile format 1.1.0 at {path}")
    if isinstance(value, list):
        for index, item in enumerate(value):
            assert_json_compatible(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"Non-string key at {path}: {key!r}")
            if not key.isascii():
                raise ValueError(f"Non-ASCII object key is outside the controlled JCS subset at {path}: {key!r}")
            assert_json_compatible(item, f"{path}.{key}")
        return
    raise ValueError(f"Non-JSON YAML value at {path}: {type(value).__name__}")


def jcs_subset_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_profile(repo: Path, profile_path: Path, schema_path: Path) -> dict[str, Any]:
    text = profile_path.read_text(encoding="utf-8")
    reject_prohibited_yaml(text)
    profile = yaml.load(text, Loader=StrictJSONSafeLoader)
    assert_json_compatible(profile)

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(profile), key=lambda error: list(error.absolute_path))
    if errors:
        messages = [f"{'.'.join(map(str, e.absolute_path)) or '$'}: {e.message}" for e in errors]
        raise ValueError("Schema validation failed:\n" + "\n".join(messages))

    expected_yaml = f"{profile['profile']['id']}.yaml"
    if profile_path.name != expected_yaml:
        raise ValueError(f"Profile filename mismatch: expected {expected_yaml}, found {profile_path.name}")
    if Path(profile['profile']['uri']).name != profile_path.name:
        raise ValueError("profile.uri does not identify the authoritative YAML filename")

    companion_name = profile['document']['human_readable_rendering']
    companion_path = profile_path.with_name(companion_name)
    if not companion_path.is_file():
        raise ValueError(f"Missing Markdown companion: {companion_path}")
    companion = companion_path.read_text(encoding="utf-8")
    required_strings = [
        profile['profile']['id'],
        profile['profile']['version'],
        profile_path.name,
        schema_path.name,
        profile['document']['digest']['value'],
        profile['baseline']['bundle_sha256'],
    ]
    missing = [item for item in required_strings if item not in companion]
    if missing:
        raise ValueError(f"Markdown companion omits controlled values: {missing}")

    digest_copy = json.loads(json.dumps(profile))
    del digest_copy['document']['digest']['value']
    calculated = hashlib.sha256(jcs_subset_bytes(digest_copy)).hexdigest()
    declared = profile['document']['digest']['value']
    if calculated != declared:
        raise ValueError(f"Profile digest mismatch: declared {declared}, calculated {calculated}")

    lifecycle = profile['profile']['lifecycle_state']
    bundle_uri = profile['baseline']['bundle_uri']
    if lifecycle in {'APPROVED', 'ACTIVE'} and not bundle_uri:
        raise ValueError("APPROVED or ACTIVE profile requires an immutable baseline bundle URI")

    return {
        'profile_id': profile['profile']['id'],
        'profile_version': profile['profile']['version'],
        'status': profile['profile']['status'],
        'lifecycle_state': lifecycle,
        'profile_digest': declared,
        'baseline_bundle': profile['baseline']['bundle_name'],
        'baseline_sha256': profile['baseline']['bundle_sha256'],
        'schema_errors': 0,
    }


def validate_manifest(implementer_dir: Path) -> dict[str, Any]:
    manifest_path = implementer_dir / 'implementation-profile-manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    checked = 0
    for entry in manifest['files']:
        path = implementer_dir / entry['path']
        if not path.is_file():
            raise ValueError(f"Manifest file missing: {entry['path']}")
        actual_hash = sha256(path)
        actual_bytes = path.stat().st_size
        if actual_hash != entry['sha256']:
            raise ValueError(f"Manifest SHA-256 mismatch for {entry['path']}")
        if actual_bytes != entry['bytes']:
            raise ValueError(f"Manifest byte-size mismatch for {entry['path']}")
        checked += 1
    return {'manifest_files_checked': checked, 'manifest_sha256': sha256(manifest_path)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()

    repo = args.repo.resolve()
    implementer = repo / 'implementer'
    schema = implementer / 'AGCP-Implementation-Profile-Schema.json'
    profiles = sorted(implementer.glob('AGCP-*.yaml'))
    if not schema.is_file():
        raise ValueError(f"Missing profile schema: {schema}")
    if not profiles:
        raise ValueError("No authoritative Implementation Profile YAML files found")

    results = [validate_profile(repo, path, schema) for path in profiles]
    manifest_result = validate_manifest(implementer)
    report = {'release_context':{'repository_release_target':'v2.0.1','repository_release_target_status':'UNRELEASED_ACCUMULATED_CORRECTION_SET','controlling_published_baseline':'v2.0.0','controlling_baseline_status':'PUBLIC_REVIEW_CONTROLLED_BASELINE','baseline_date':'2026-07-30','artifact_lifecycle_state':'CURRENT'},
        'validation_type': 'AGCP_IMPLEMENTATION_PROFILE_VALIDATION',
        'status': 'PASS',
        'profiles_validated': len(results),
        'profiles': results,
        **manifest_result,
    }
    payload = json.dumps(report, indent=2) + '\n'
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(payload, encoding='utf-8')
    print(payload, end='')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Implementation Profile validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
