> **Current published baseline:** AGCP v2.1.0 Public Review Controlled Baseline  
> **Synchronized change-set target:** AGCP v2.1.x  
> **Change-set status:** CLOSED FOR DOWNSTREAM IMPLEMENTATION  
> **Controlling published baseline date:** 2026-08-15
>
> The v2.1.x synchronization change set is complete through Trust Model, ARM, Core, Companion/Profile, Normative Statements, DS/interface/API, Formal Test Cases, Test Matrix, test mappings, test-control mappings, Harness Vectors/Checks, aggregate conformance validation, and final RTM synchronization at `RTM-1.47`. The exact publication Semantic Version for this synchronized change set has not been assigned by this closure step; the currently published baseline remains v2.1.0 until a controlled release decision is made.  
> **v2.1.x synchronization notes:** [`RELEASE_NOTES_v2.1.x.md`](RELEASE_NOTES_v2.1.x.md)  
> **Current published release notes:** [`RELEASE_NOTES_v2.1.0.md`](RELEASE_NOTES_v2.1.0.md)

---

## Controlled release version source

The repository root `VERSION` file is the sole maintained AGCP repository release number. Current-release labels used by build and validation tooling are derived from that value. Human-authored historical release records are not rewritten when `VERSION` changes.

The root `VERSION` file continues to identify the currently published repository baseline as `2.1.0`. This v2.1.x synchronization closure does not silently assign a new publication version; release designation is a separate controlled governance action.

## Normative Statement inventory

The synchronized v2.1.x inventory contains **393 permanent Normative Statement identifiers**, of which **390 are current** and **3 are retired/reserved** (`NS-8.6A-01`, `NS-8.6A-03`, and `NS-9.1-01`). The current statements remain Core-derived extraction and traceability artifacts; they do not supersede the CRs, Core, or adopted normative Companion Specifications.

## Specification Status

AGCP v2.1.0 remains the controlled **Public Review Controlled Baseline** dated 2026-08-15. This repository working snapshot also contains the closed v2.1.x synchronization change set used for downstream implementation handoff. That synchronized change set is not a separately published AGCP release until release governance assigns and records a publication version.

The purpose of this review is to evaluate:

- architectural correctness
- determinism guarantees
- lifecycle derivation model
- conformance framework completeness
- multitenant isolation guarantees

Review feedback may result in a later revision, but does not alter this controlled baseline unless the change is incorporated into a versioned release and recorded in `governance/CHANGELOG.md`.

---

## Test and Injection Point Development Status

AGCP test-control, fixture-injection, and Governance Observation Point definitions are under active development. The interfaces, control types, injection semantics, and observation points currently enumerated in this repository represent the test capabilities identified to date; they should not be interpreted as a final or exhaustive inventory.

Additional test or injection points may be identified as the reference implementation, conformance suite, negative testing, and integration testing mature. Some enumerated capabilities may also be only partially implemented in a given reference implementation until the corresponding source-code integration is completed and qualified.

The specification repository defines the intended external semantics and isolation requirements for standardized test controls. The specific internal source-code hooks used to realize those controls are implementation details and may evolve during development.

Conformance claims should therefore be based on the capabilities required by the applicable released conformance profile and Formal Test Cases, together with the objective evidence required by those artifacts, rather than on an assumption that every development-stage test or injection point described in the repository is already implemented.

---

# Purpose

AGCP provides a structural control-plane model for governing automated actions in distributed systems. It addresses technical challenges including:

- Non-deterministic workflow ordering
- Time-of-check/time-of-use (TOCTOU) gaps
- Authorization drift over time
- Mutable lifecycle state corruption
- Cross-tenant integrity risks
- Replay inconsistency under evolving configuration

AGCP is **not a policy language**.  
It is a deterministic governance foundation.

---

# Core Architectural Principles

### 1. Append-Only Ledger Semantics

All governance stage results are recorded as immutable stage entries.

### 2. Per-Action Total Ordering

Strictly increasing sequence values per action identifier define canonical ordering.

### 3. Deterministic Lifecycle Derivation

Lifecycle state is derived exclusively from ordered stage entries — never from independently mutable status fields.

### 4. Execution-Bound Authorization

Execution eligibility must be re-derived at commit time against canonical state.

### 5. Structural Invariant Separation

Control-plane invariants operate independently of tenant-defined policy logic.

### 6. Multitenant Governance Isolation Guarantees

Cross-tenant artifact resolution and ledger access are structurally constrained.

---

# How to Review This Specification

AGCP is released for **public technical review**.

Reviewers do not need to read the entire specification to contribute.  
Feedback is most valuable when focused on:

- determinism of evaluation stages
- policy evaluation ordering
- constraint and invariant semantics
- lifecycle state transitions
- multitenant isolation guarantees
- conformance test coverage

### Suggested Review Path

Use repository-relative paths when citing documents. A structured review sequence is:

1. `spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv` — highest-precedence capability requirements
2. `spec/AGCP-Core.docx` — normative runtime behavior
3. `spec/Architecture Reference Model.docx` — architectural concepts and terminology
4. `spec/AGCP Normative Statements.docx` — extracted atomic Core obligations
5. `spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx` — authoritative traceability
6. `spec/AGCP-Policy-Evaluation-Contract.md` — implementation-independent policy-evaluation companion specification
7. `AGCP-Machine-Readable-Governance-Chain.md` — informative end-to-end explanation of how architectural functions and machine-readable DS artifacts relate from authenticated identity through governed execution and durable evidence
8. `spec/AGCP-HTTP-Interface-Specification.md` and `api/AGCP-HTTP-Contract.yaml` — interface semantics and executable contract
9. `spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md` — Governance Ledger Event requirements
10. `lifecycle/AGCP Governance Lifecycle Model.md` and `lifecycle/AGCP Normative Governance Progression Table.md` — lifecycle interpretation and progression
11. `conformance/AGCP-Conformance-Traceability-and-Automation-Model.md`, `conformance/AGCP-Conformance.md`, `conformance/AGCP-Test-Matrix.md`, and `conformance/AGCP-Conformance-Test-Vectors.md` — conformance relationships, profiles, mappings, and executable tests

---

## Repository Structure

The following abbreviated tree lists the current controlled paths used for review and implementation. Every named path exists in this release.

```text
.
├── README.md
├── RELEASE_NOTES_v2.1.x.md
├── RELEASE_NOTES_v2.1.0.md
├── RELEASE_NOTES_v2.0.4.md
├── RELEASE_NOTES_v2.0.0.md
├── ARCHITECTURE.md
├── AGCP-Machine-Readable-Governance-Chain.md
├── LICENSE
├── NOTICE.md
├── .github/
│   ├── CODEOWNERS
│   └── ISSUE_TEMPLATE/spec-review.yml
├── spec/
│   ├── AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv
│   ├── AGCP-Core.docx
│   ├── Architecture Reference Model.docx
│   ├── AGCP Normative Statements.docx
│   ├── AGCP_Requirements_Traceability_Matrix_(RTM).xlsx
│   ├── AGCP Requirements Traceability Framework.docx
│   ├── Requirements Traceability Matrix (RTM) Specification.docx
│   ├── AGCP-Policy-Evaluation-Contract.md
│   ├── AGCP-HTTP-Interface-Specification.md
│   ├── AGCP-Human-Review-Specification.md
│   ├── AGCP-Multitenant-Operational-Specification.md
│   ├── AGCP-Provenance-Wire-Format-Specification.md
│   ├── AGCP-Error-Mapping.md
│   └── ledger/AGCP-Append-Only-Governance-Ledger-Specification.md
├── lifecycle/
├── schemas/
│   ├── catalog/
│   └── examples/
├── registries/
├── conformance/
│   └── tests/
├── api/
│   └── AGCP-HTTP-Contract.yaml
├── governance/
├── implementer/
├── reference/
├── diagrams/
└── research/
```

---

# Repository Contents

This repository contains specification, traceability, conformance, and supporting artifacts; it does not contain a production AGCP implementation.
### Server implementer / Codex starting point

The repository does not contain the production Rust server source. Implementers building the server should begin with `reference/AGCP-v2.1.0-Server-Implementation-Blueprint.md` and `conformance/AGCP-v2.1.0-Executable-Regression-Requirements.json`, then use the normative Core/Companion Specifications and controlled DS/IF contracts as authority. The blueprint translates the known executable regression closures into concrete module boundaries, processing order, atomicity requirements, source-adapter behavior, and pre-conformance regression tests without creating new CRs.


### Authoritative and normative sources

- `spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv`
- `spec/AGCP-Core.docx`
- Applicable adopted companion specifications under `spec/`, including the policy-evaluation, HTTP-interface, provenance, multitenant, error-mapping, and Governance Ledger specifications

### Architectural and traceability artifacts

- `spec/Architecture Reference Model.docx`
- `spec/AGCP Normative Statements.docx`
- `spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx`
- `spec/AGCP Requirements Traceability Framework.docx`
- `spec/Requirements Traceability Matrix (RTM) Specification.docx`

### Formal Test Case synchronization status

The formal conformance procedures are synchronized to the current v2.1.x Core and Normative Statements while preserving the frozen CR-001 through CR-122 / TC-001 through TC-122 one-to-one model. No TC-123 is introduced. Forty-two TCs contain formal traceability/assertion changes and twenty-two additional TCs contain regression/scenario updates. The Test Matrix, test mappings, test-control mappings, Harness Checks, and Harness Test Vectors have now been synchronized and the aggregate conformance-layer validation has passed. Final RTM synchronization is complete at `RTM-1.47`. See `conformance/AGCP-v2.1.x-AGGREGATE-CONFORMANCE-LAYER-VALIDATION.md`.

### Test Matrix regeneration status

`conformance/AGCP-Test-Matrix.md` has been completely regenerated from the synchronized `TC-001` through `TC-122` Formal Test Case files. The machine-readable/human-readable test mappings, test-control mappings, 21 Harness Checks, and 71 Harness Test Vectors are synchronized and aggregate conformance-layer validation has passed. Final RTM synchronization is complete at `RTM-1.47`.

### Test mapping regeneration status

`conformance/test-mapping.json` has been completely regenerated for all `TC-001` through `TC-122` records, and `conformance/test-control-mapping.json` plus `conformance/AGCP-Test-Control-Mapping.md` have been regenerated against DS-050/DS-046. Harness Test Vector/Check content is synchronized at 21 checks and 71 vectors. Aggregate conformance-layer validation has passed and final RTM synchronization is complete at `RTM-1.47`.

### Machine-readable and conformance artifacts

- Active schemas and the Schema Catalog under `schemas/`
- Controlled registries under `registries/`
- The OpenAPI contract and interface catalog under `api/`
- The conformance relationship model, conformance specification, Harness Checks, Test Vectors, mappings, fixtures, and formal Test Cases under `conformance/`

### Supporting artifacts

- `AGCP-Machine-Readable-Governance-Chain.md` — informative narrative guide connecting authenticated principals, IAS qualification, GDF/PDP decisions, Execution Authorization, GRF processing, PEP enforcement, commitment, execution outcome, lifecycle, evidence, receipts, and ledger events
- Controlled Implementation Profile format artifacts, profiles, catalogs, and package manifest under `implementer/`
- `RELEASE_NOTES_v2.1.x.md` — closure notes for the synchronized v2.1.x change set; publication version intentionally unassigned by this step
- `RELEASE_NOTES_v2.1.0.md` — release notes for the current published v2.1.0 Public Review Controlled Baseline
- `RELEASE_NOTES_v2.0.4.md` — historical release notes for v2.0.4
- `RELEASE_NOTES_v2.0.0.md` — comparison-based release notes and migration guidance for the published baseline
- Current lifecycle documents under `lifecycle/`
- Versioning and contribution guidance under `governance/`
- Reference pseudocode under `reference/`
- The canonical control-plane diagram under `diagrams/`
- Historical and explanatory publications under `research/`

---

# What This Repository Does Not Contain

- Production implementation code
- Deployment artifacts
- Unpublished customer-specific operating profiles or deployment overlays; controlled public Implementation Profiles may be included as lower-precedence specification artifacts
- Cryptographic key material
- Enterprise-specific configurations

This repository defines the **architectural specification only**.

---

# Conformance Model

AGCP defines five cumulative conformance levels.

**L1 — Schema & Envelope Validation**

**L2 — Ordered Governance Mediation**

**L3 — Deterministic Governance**

**L4 — Execution Authorization Control**

**L5 — Multitenant Governance Isolation**

Conformance claims must declare:

- Implementation name
- Version
- Supported AGCP version
- Conformance level
- Cryptographic profile
- Test report reference

---

# Public Review Process

AGCP is released for public technical review.

Feedback categories:

- Normative Defect
- Structural Gap
- Ambiguity
- Conformance Clarification
- Security Concern
- Determinism Concern
- Multitenant Governance Isolation Concern

Please submit issues referencing:

- specification section number
- assertion ID (if applicable)
- proposed resolution language

---

# Determinism & Replay Posture

AGCP requires that identical governance envelopes processed under identical configuration produce identical:

- stage entry sequences
- lifecycle derivations
- decision outcomes

Replay behavior must not depend on timestamp ordering or mutable status fields.

---

# Versioning

AGCP follows semantic versioning.

- **MAJOR** — breaking structural or normative changes  
- **MINOR** — additive normative clarifications  
- **PATCH** — editorial or non-behavioral corrections  

The currently published baseline is AGCP v2.1.0 Public Review Controlled Baseline, baseline date 2026-08-15. The synchronized v2.1.x change set documented here is closed for downstream implementation but is not assigned a new publication Semantic Version by this closure step. Publication SHALL occur only through a later controlled release decision recorded in the release-governance artifacts.

---

## v2.1.x Repository Synchronization Closure

The specification synchronization sequence is complete. The authoritative RTM is `RTM-1.47`; the conformance layer has passed aggregate validation; and the repository closure manifest and validation report are published under `governance/AGCP-v2.1.x-repository-closure-manifest.json` and `governance/AGCP-v2.1.x-repository-closure-validation.json`. The cumulative direct-overlay change package is closed for the next governed layer: generic source implementation.

# Scope

Although AGCP may be applied to AI-enabled systems, the architecture is general and applicable to:

- financial transaction processors
- settlement engines
- regulated execution systems
- infrastructure change governance
- multi-agent automated systems
- workflow and orchestration platforms

---

# Security Disclosures

Security-sensitive concerns or matters not appropriate for public issue tracking may be directed to:


research@agcp.ai


Public technical review comments should be submitted via **GitHub Issues**.

---

AGCP specifies a control-plane architecture intended to improve distributed system reliability, lifecycle determinism, and execution-bound governance correctness.

## Governance Approval submission and authoritative record

IF-001 accepts `schemas/governance_approval_submission.json` (DS-045) as untrusted ingress. `schemas/governance_approval_artifact.json` (DS-026) is created or qualified by AGCP after independent processing and is not accepted as request content.

## AGCP v2.0.4 content-digest correction

The cumulative v2.0.4 correction set binds every DS-001 content-digest algorithm to its exact lowercase-hexadecimal output length. Controlled examples, negative vectors, validation, and CI are published under `schemas/examples/`, `conformance/digests/`, and `governance/`.

### Public IF-001 errors and metadata (v2.0.4)

The cumulative v2.0.4 correction set normalizes public protected-resource failures to `404 RESOURCE_NOT_FOUND`, defines pre-governance throttling as `429 REQUEST_THROTTLED` with required delay-seconds `Retry-After`, defines unavailable processing capacity as `503 CAPACITY_UNAVAILABLE`, and keeps governance quota denial as an authoritative Governance Outcome. DS-003 metadata now binds immutable baseline, profile, schema, generated validator, and active-governance integrity.

### Semantic fixture integrity

The v2.0.4 correction stream validates controlled positive fixtures beyond JSON Schema structure. Fourteen fixtures now use internally consistent Tenant, Governance Domain, Proposal, target, policy, authorization, lifecycle, evidence, and Canonical State bindings. Controlled negative vectors remain separate under `conformance/semantic-fixtures/` and `conformance/command-record/`.

## Normative companion reference integrity (v2.0.4)

The cumulative v2.0.4 correction set retires absent umbrella companion labels and requires references to identify the controlled artifacts that actually exist. The dispositions are published in `governance/AGCP-Normative-Companion-Reference-Dispositions.md` and `governance/normative-companion-reference-dispositions.json`; automated validation is provided by `governance/validate_normative_companion_references.py`.


## Release and lifecycle metadata

AGCP v2.1.0 is the current Public Review Controlled Baseline. Active catalogs and controlled artifacts use lifecycle `CURRENT`, and the controlled baseline date is `2026-08-15`. The controlled policy and validation are published under `governance/AGCP-Release-Lifecycle-Metadata-Policy.md` and `governance/AGCP-release-lifecycle-metadata-validation.json`.


## Published-baseline repository integrity

The v2.1.0 published-baseline aggregate validator remains `governance/validate_repository_integrity.py`, with its historical controlled report under the v2.1.0 release artifacts. The closed v2.1.x synchronization change set is validated separately so historical v2.1.0 release evidence is not silently rewritten.

## v2.1.x repository synchronization closure

The synchronized change set is complete through `RTM-1.47`; the current Schema, Interface, Registry Entry, and Implementation Profile catalogs carry reciprocal RTM synchronization metadata. The closure record, full repository closure manifest, and closure validation report are `governance/AGCP-v2.1.x-REPOSITORY-CLOSURE.md`, `governance/AGCP-v2.1.x-repository-closure-manifest.json`, and `governance/AGCP-v2.1.x-repository-closure-validation.json`.

## v2.1.x Trust, Governance Realization, and Profile Alignment

The controlled architecture distinguishes the Governance Decision Function / PDP from the Governance Realization Function (GRF). A Governance Decision does not by itself establish commit-bound authority. Execution Authorization is later consumed by the GRF, which re-establishes current commitment-sensitive eligibility, applies the controlling PEP Profile, constructs the Enforcement Context, and presents the exact transition to the PEP. The PEP controls crossing of the enforcement boundary.

`spec/AGCP-Trust-Model.md` is the controlled non-normative architectural trust reference. It is subordinate to the published CRs and Core and does not independently create conformance requirements.

The generic implementer framework includes two subordinate controlled profile types:

- Identity and Authorization Store (IAS) Profile - authoritative identity plus identity-system roles, groups, entitlements, governance permissions, reviewer classes, scopes, delegation/authority attributes, validity, and account state used as governance input; and
- PEP Profile - exact GRF-to-PEP action/target mapping, Enforcement Context requirements, caller authentication, PEP-to-target authority, response mapping, and fail-closed behavior.

Deployment-specific profiles remain separate from the generic specification unless intentionally published.
