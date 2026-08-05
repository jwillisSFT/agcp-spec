# AGCP Harness Check Registry

**Status:** Informational  
**Applicable release:** AGCP v2.0.0  
**Interface:** IF-001 `/agcp/v2`  
**Canonical machine-readable source:** [`harness-checks.json`](harness-checks.json)  
**Fixture mapping:** [`fixture-mapping.json`](fixture-mapping.json)

> **Relationship model:** Harness Checks are reusable executable capability checks that support portions of Formal Test Cases. They are not independent normative requirements or assessment authorities. See `AGCP-Conformance-Traceability-and-Automation-Model.md`.

## Purpose

Harness Checks are executable realizations of portions of published Formal Test Cases. They do not create an independent normative layer. The controlled traceability relationship is CR ↔ Core-derived NS identifiers ↔ TC. The RTM controls the CR/Core-derived-NS/TC relationships, and `test-mapping.json` extends the TC relationship to Harness Checks and Test Vectors. These traceability relationships do not alter normative precedence. The governing specifications define implementation obligations, and the Formal Test Cases control assessment procedures.

## Registry

| Harness Check ID | Validated capability |
|---|---|
| `CHECK-PROPOSAL-QUALIFICATION` | Proposal Qualification accepts valid proposals and refuses malformed or inadmissible proposals. |
| `CHECK-GOVERNANCE-DECISION` | Governance Decision Function produces deterministic governance outcomes from qualified proposals and authoritative inputs. |
| `CHECK-GOVERNANCE-APPROVAL` | Human adjudication and Governance Approval Artifacts are enforced when required and cannot be bypassed before Commit-Bound Admissibility. |
| `CHECK-EXECUTION-AUTHORIZATION` | Execution Authorization is produced only after required governance prerequisites are satisfied. |
| `CHECK-COMMIT-BOUNDARY` | Commit Boundary processing gates governance-significant execution and validates current governance conditions immediately before commit. |
| `CHECK-GOVERNANCE-EVIDENCE` | Governance Evidence is produced, linked, attributable, integrity-protected, and sufficient for audit and deterministic replay. |
| `CHECK-APPEND-ONLY-GOVERNANCE-LEDGER` | DS-040 Governance Ledger Events preserve immutable, attributable, integrity-linked, and authoritatively ordered governance history. |
| `CHECK-CANONICAL-STATE` | Canonical State is deterministically resolved from applicable qualified authoritative governance sources; incorporated Governance Ledger records use authoritative ledger ordering, and materialized views are reproducible from those sources. |
| `CHECK-IDEMPOTENCY` | Repeated proposal submission with the same idempotency key or replay-protection mechanism does not create conflicting governance state. |
| `CHECK-TENANT-STATE-GATING` | Tenant lifecycle state gates proposal submission, Execution Authorization, and Commit Boundary processing. |
| `CHECK-TENANT-AND-DOMAIN-ISOLATION` | Tenant and Governance Domain isolation prevent unauthorized cross-boundary governance operations. |
| `CHECK-PROVENANCE` | Governance-significant requests and artifacts include valid provenance and reject invalid provenance. |
| `CHECK-REGISTRIES` | Governance processing uses published registries and rejects unknown registered values. |
| `CHECK-QUALIFIED-GOVERNANCE-INPUTS` | Canonical State, Governance Evidence, and authority are independently qualified or re-derived before commitment. |
| `CHECK-LIFECYCLE-AND-CONTINUATION` | Derived Lifecycle State and Continuation Integrity preserve governed nonterminal progression, degradation, re-evaluation, and recovery. |
| `CHECK-GOVERNANCE-COMPILATION-ACTIVATION` | Governance Configuration, deterministic compilation, constitutional validation and constraint preservation, omission analysis, self-protection, atomic controlled activation, prior-version preservation, governed rollback, evidence, and lineage are executable and traceable. |
| `CHECK-HTTP-INTERFACE-CONTRACT` | All ten mandatory IF-001 operations have executable positive coverage and applicable negative, isolation, and idempotency coverage. |

## Synchronization rules

- Schema references use exact current repository paths.
- Fixture references resolve through `fixture-mapping.json` and validate before harness execution.
- Governance Approval Artifact terminology is used exclusively; DS-016 compatibility handling is absent.
- Commit Boundary fixtures use the current DS-018 Enforcement Context representation.
- `/agcp/v2` is the only active HTTP namespace for IF-001.
- Every mandatory IF-001 operation has at least one schema-valid positive vector; applicable negative, isolation, and idempotency behavior is also executable.
- Every `MUST` Harness Check SHALL reference at least one substantive executable vector. `CHECK-GOVERNANCE-COMPILATION-ACTIVATION` is realized by `TV-GCFG-001`, `TV-GCOMP-001`, `TV-GCONST-001`, `TV-GCONST-002`, `TV-GOMIT-001`, `TV-GSELF-001`, `TV-GACT-001`, `TV-GACT-002`, and `TV-GROLL-001`.
- Check identifiers remain stable, but obsolete compatibility behavior is not retained.
