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

## Management Control Plane test-control operability

- DS-050 wire contract v1.2 requires a finite `expires_at` lease for every non-reset IF-005 control.
- DS-051 wire contract v1.2 adds required per-operation `runtime_binding_status` and applying-principal readback, plus Tenant/Governance Domain and lease context; `EFFECTIVE` now normatively implies `BOUND`.
- DS-047 response v1.1 advertises exact supported variants for target-execution and enforcement-path-fault controls and whether authorized test-control enumeration/recovery is implemented.
- IF-005 adds authorized `GET /agcp/test/v1/controls` enumeration for active-control inventory, client-restart recovery, and verified cleanup.
- The Management Plane harness adds exact-variant discovery, EFFECTIVE/BOUND consistency, finite-expiry, and orphan-control recovery/reset checks.
- These changes do not add new Formal Test Cases or new governance outcome injection mechanisms; they make the existing standardized test and injection points safely operable by a Management Control Plane.
