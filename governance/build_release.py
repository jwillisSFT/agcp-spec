#!/usr/bin/env python3
"""Run the controlled AGCP release synchronization and validation pipeline."""
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
from release_version import ROOT, SYNC_MANIFEST, SYNC_REPORT, INTEGRITY_REPORT

SEMANTIC_VALIDATORS=[
 ["governance/sync_release_version.py","--write"],
 ["governance/validate_implementation_profiles.py"],
 ["governance/validate_provenance_wire_format.py"],
 ["governance/validate_command_record_separation.py"],
 ["governance/validate_content_digest_contract.py"],
 ["governance/validate_http_error_metadata_contract.py"],
 ["governance/validate_semantic_fixtures.py"],
 ["governance/validate_normative_companion_references.py"],
 ["governance/validate_release_lifecycle_metadata.py"],
 ["governance/validate_normative_statement_inventory.py"],
]

def run(root: Path, argv: list[str]) -> None:
    cmd=[sys.executable,*argv]; print("+"," ".join(cmd),flush=True)
    env=os.environ.copy(); env["PYTHONDONTWRITEBYTECODE"]="1"
    subprocess.run(cmd,cwd=root,env=env,check=True)

def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",default=str(ROOT)); ap.add_argument("--validate-only",action="store_true"); a=ap.parse_args(); root=Path(a.repo).resolve()
    for cmd in SEMANTIC_VALIDATORS: run(root,cmd)
    # Refresh embedded source hashes to a fixed point. Some controlled reports refer
    # to other controlled reports, so one pass can legitimately cause a second pass.
    for _ in range(3):
        run(root,["governance/refresh_source_hashes.py"])
    run(root,["governance/sync_release_version.py","--check"])
    if a.validate_only:
        print(json.dumps({"status":"PASS","mode":"validate-only"},indent=2)); return 0
    run(root,["governance/generate_repository_manifest.py"])
    run(root,["governance/validate_repository_synchronization.py"])
    # Sync report is intentionally excluded from the manifest but is a controlled report for integrity validation.
    run(root,["governance/validate_repository_integrity.py"])
    print(json.dumps({"status":"PASS","mode":"build-release","manifest":SYNC_MANIFEST,"synchronization_report":SYNC_REPORT,"integrity_report":INTEGRITY_REPORT},indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
