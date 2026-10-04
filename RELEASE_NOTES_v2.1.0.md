# AGCP v2.1.0 Release Notes

**Release:** AGCP v2.1.0  
**Status:** Public Review Controlled Baseline  
**Artifact lifecycle:** CURRENT  
**Baseline date:** 2026-08-14  
**Version source:** root `VERSION` file

## Conformance testability closure

This repository update makes the root `VERSION` file the sole maintained repository release number for current-release synchronization and removes validator dependence on hard-coded catalog-version literals. Protocol/interface revisions and historical provenance identifiers remain independently versioned where they represent different concepts.

The Management Plane artifacts DS-047 through DS-049 and their controlled examples are present and IF-003/IF-004/IF-005 references resolve. DS-050/DS-051 add `TARGET_EXECUTION_FIXTURE` and `ENFORCEMENT_PATH_FAULT_FIXTURE` so the TC-081 asynchronous execution path and TC-120/TC-121 enforcement-integrity negative paths have standardized, discoverable test-control mechanisms without injecting governance outcomes.

Every TC-001 through TC-122 has a dedicated direct harness orchestration vector. TC-073, TC-075, and TC-090 retain genuine external-dependency requirements for alternate transport or independent implementation/deployment comparison.

Validation is read-only in `make validate`; release synchronization writes occur only during an explicit release build or `make sync-version`.

## Normative Statement inventory

The controlled inventory contains **393 permanent Normative Statement identifiers**: **390 current** and **3 retired/reserved** (`NS-8.6A-01`, `NS-8.6A-03`, and `NS-9.1-01`). `NS-17.2-01` remains intentionally unassigned because the duplicated Core obligation is canonically identified as `NS-2.7-01`.
