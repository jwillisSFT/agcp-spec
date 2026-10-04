# AGCP Interface Definition Catalog

> **Version source:** `VERSION`  
> **Current repository release:** `v2.1.0`  
> **Release status:** `PUBLIC_REVIEW_CONTROLLED_BASELINE`  
> **Artifact Lifecycle:** `CURRENT`  
> **Baseline Date:** `2026-08-14`  


Updated 2026-10-04. No IF-006 is introduced. IAS lookup and GRF-to-PEP transport remain Implementation Profile / IAS Profile / PEP Profile controlled rather than standardized public AGCP interfaces.

| ID | Interface | Contract | Notes |
|---|---|---|---|
| IF-001 | AGCP HTTP Interface v2 | 2.1.0 | IF-001 invokes Governance Realization through /commit-boundary/commit. The GRF independently establishes current commit eligibility, selects/applies the PEP Profile, constructs Enforcement Context, and mediates the PEP. Commit Successful is distinct from later asynchronous execution completion. Approval ingress uses server-side IAS qualification; no public IAS or PEP interface is standardized. |
| IF-002 | AGCP Policy Evaluation Contract | 2.1.0 | GDF/PDP deterministic evaluation contract. It may consume DS-053 qualified identity/authorization input but does not perform Governance Realization or PEP enforcement. |
| IF-003 | AGCP Governance Observation Interface v1 | 2.1.0 | Read-only observations distinguish IAS qualification, GDF/PDP, GRF, PEP enforcement, commitment, and post-commit execution outcome. |
| IF-004 | AGCP Governance Management and Actuation Interface v1 | 2.1.0 | Supporting production management surface. Request acceptance is distinct from authoritative realization; status readback is provided and EFFECTIVE requires ordinary authoritative governance mechanisms, evidence, and observation. |
| IF-005 | AGCP Conformance Test Control Interface v1 | 2.1.0 | Optional isolated test-only surface with finite non-reset leases, per-operation BOUND/EFFECTIVE/OBSERVED readback, exact variant discovery, and authorized active-control enumeration for recovery and verified cleanup. TARGET_EXECUTION_FIXTURE and ENFORCEMENT_PATH_FAULT_FIXTURE establish controlled input conditions only and cannot inject GDF/GRF decisions or desired governance outcomes. |
