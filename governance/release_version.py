#!/usr/bin/env python3
"""Authoritative AGCP repository release-version helper.

The root VERSION file is the sole maintained repository release number.
All current-release labels and generated report filenames are derived here.
Historical release records are not rewritten by this module.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
SETTINGS_FILE = ROOT / "governance/release-settings.json"

def _read_semver() -> str:
    value = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", value):
        raise ValueError(f"VERSION must contain bare MAJOR.MINOR.PATCH; found {value!r}")
    return value

def _settings() -> dict:
    return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))

SEMVER = _read_semver()
RELEASE_TAG = f"v{SEMVER}"
RTM_SPEC_VERSION = f"v.{SEMVER}"
RELEASE_IDENTIFIER = f"AGCP-{RELEASE_TAG}"
CURRENT_RELEASE_NOTES = f"RELEASE_NOTES_{RELEASE_TAG}.md"
SYNC_UPDATE = f"governance/AGCP-{RELEASE_TAG}-REPOSITORY-SYNCHRONIZATION-UPDATE.md"
SYNC_MANIFEST = f"governance/AGCP-{RELEASE_TAG}-repository-synchronization-manifest.json"
SYNC_REPORT = f"governance/AGCP-{RELEASE_TAG}-repository-synchronization-validation.json"
INTEGRITY_REPORT = f"governance/AGCP-{RELEASE_TAG}-repository-integrity-validation.json"
SETTINGS = _settings()
RELEASE_STATUS = SETTINGS["repository_release_target_status"]
CONTROLLING_BASELINE_STATUS = SETTINGS["controlling_baseline_status"]
BASELINE_DATE = SETTINGS["baseline_date"]
ARTIFACT_LIFECYCLE_STATE = SETTINGS["artifact_lifecycle_state"]

def release_context() -> dict:
    return {
        "repository_release_target": RELEASE_TAG,
        "repository_release_target_status": RELEASE_STATUS,
        "controlling_published_baseline": RELEASE_TAG,
        "controlling_baseline_status": CONTROLLING_BASELINE_STATUS,
        "baseline_date": BASELINE_DATE,
        "artifact_lifecycle_state": ARTIFACT_LIFECYCLE_STATE,
    }

def release_lifecycle_metadata() -> dict:
    return {
      "policy_id": "AGCP-RELEASE-LIFECYCLE-METADATA-1.0",
      "policy_version": "1.1.0",
      "finding": "P2-01",
      "version_source": "VERSION",
      "repository_release_target": RELEASE_TAG,
      "repository_release_target_status": RELEASE_STATUS,
      "controlling_published_baseline": {
        "release_id": RELEASE_IDENTIFIER,
        "specification_version": SEMVER,
        "release_status": CONTROLLING_BASELINE_STATUS,
        "baseline_date": BASELINE_DATE
      },
      "current_artifact_lifecycle_state": ARTIFACT_LIFECYCLE_STATE,
      "current_catalog_publication_status": SETTINGS["catalog_publication_status"],
      "current_repository_specification_version": SEMVER,
      "rules": [
        "The root VERSION file is the sole maintained repository release number; current-release labels are generated or validated from it.",
        f"AGCP {RELEASE_TAG} is the current Public Review Controlled Baseline for this repository release.",
        "Active controlled artifacts use lifecycle CURRENT and publication status CURRENT unless a more specific controlled lifecycle applies.",
        "Working Draft is reserved for artifacts intentionally outside the controlled current repository set.",
        "Implementation Profiles retain their own controlled lifecycle and status values."
      ],
      "validation_report_release_context": release_context()
    }
