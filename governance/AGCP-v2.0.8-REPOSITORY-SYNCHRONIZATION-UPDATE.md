# AGCP v2.0.8 Repository Synchronization Update

**Date:** 2026-08-14  
**Repository release target:** v2.0.8  
**Version source:** `VERSION`  
**Status:** Public Review Controlled Baseline synchronization  
**Controlling published baseline:** v2.0.8 Public Review Controlled Baseline  
**Baseline date:** 2026-08-14  
**RTM dataset:** RTM-1.46  
**Schema Catalog:** 1.0.50  
**Interface Catalog:** 1.0.5  
**Registry Entry Catalog:** 1.0.3  
**Implementation Profile Catalog:** 1.0.3

## Scope

This record closes the v2.0.8 repository synchronization step and the single-source release-version dependency audit. The root `VERSION` file is the sole maintained current repository release number. Current-release tooling derives release identity through `governance/release_version.py`; `governance/sync_release_version.py` propagates that identity to controlled current-release metadata.

## Dependency audit

The audit distinguishes three classes of release-number occurrence:

1. current-release metadata, which SHALL be generated or synchronized from root `VERSION`;
2. historical release/provenance records, which retain their original historical release identifiers; and
3. semantic fixture/example values that intentionally model a particular AGCP release and are not repository-release authorities.

Executable Python tooling outside `governance/release_version.py` is checked for literal use of the current semantic version. Current conformance-harness release metadata and current normative-companion disposition release identity are included in VERSION-driven synchronization.

## Controlled result

The v2.0.8 release build is complete only when VERSION synchronization is at a fixed point, controlled source hashes are current, the synchronization manifest is generated under the VERSION-derived filename, repository synchronization validation passes, repository-wide integrity validation passes, and the AGCP assessment baseline preflight accepts the resulting repository.
