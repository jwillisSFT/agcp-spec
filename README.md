> **Current release:** AGCP v2.0.5  
> **Artifact lifecycle:** CURRENT  
> **Release status:** PUBLIC_REVIEW_CONTROLLED_BASELINE  
> **Controlling published baseline:** AGCP v2.0.5 Public Review Controlled Baseline  
> **Baseline date:** 2026-08-05
>
> This repository snapshot is the controlled AGCP v2.0.5 public-review release. Every change is recorded in `governance/CHANGELOG.md` and synchronized through the controlled catalogs, RTM, validation reports, and repository manifest.  
> **Current release notes:** [`RELEASE_NOTES_v2.0.5.md`](RELEASE_NOTES_v2.0.5.md)  
> **Prior published-baseline notes:** [`RELEASE_NOTES_v2.0.0.md`](RELEASE_NOTES_v2.0.0.md)

---

## Controlled release version source

The repository root `VERSION` file is the sole maintained AGCP repository release number. Current-release labels used by build and validation tooling are derived from that value. Human-authored historical release records are not rewritten when `VERSION` changes.

For this repository snapshot, `VERSION` is `2.0.5`, yielding release tag `v2.0.5` and RTM specification version `v.2.0.5`.

## Normative Statement inventory

The v2.0.5 controlled inventory contains **357 unique Normative Statement identifiers**. The Core has **358 controlled normative source-text occurrences** under the release inventory accounting because the conformance-scope obligation in Core Section 17.2 duplicates the obligation already represented by `NS-2.7-01` from Section 2.7. `NS-17.2-01` is intentionally unassigned. See `RELEASE_NOTES_v2.0.5.md` and `governance/AGCP-normative-statement-inventory-validation.json`.

## Specification Status

AGCP v2.0.5 is issued as the controlled **Public Review Controlled Baseline** dated 2026-08-05. The contents of this repository snapshot are the fixed basis for review, implementation comparison, and conformance evaluation until a later versioned revision is issued.

The purpose of this review is to evaluate:

- architectural correctness
- determinism guarantees
- lifecycle derivation model
- conformance framework completeness
- multitenant isolation guarantees

Review feedback may result in a later revision, but does not alter this controlled baseline unless the change is incorporated into a versioned release and recorded in `governance/CHANGELOG.md`.

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
8. `spec/AGCP-HTTP-Interface-Specification.md` and `api/AGCP-HTTP-Contract.yaml` — interface semantics and executable contract
9. `spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md` — Governance Ledger Event requirements
10. `lifecycle/AGCP Governance Lifecycle Model.md` and `lifecycle/AGCP Normative Governance Progression Table.md` — lifecycle interpretation and progression
12. `conformance/AGCP-Conformance-Traceability-and-Automation-Model.md`, `conformance/AGCP-Conformance.md`, `conformance/AGCP-Test-Matrix.md`, and `conformance/AGCP-Conformance-Test-Vectors.md` — conformance relationships, profiles, mappings, and executable tests

---

## Repository Structure

The following abbreviated tree lists the current controlled paths used for review and implementation. Every named path exists in this release.

```text
.
├── README.md
├── RELEASE_NOTES_v2.0.5.md
├── RELEASE_NOTES_v2.0.4.md
├── RELEASE_NOTES_v2.0.0.md
├── ARCHITECTURE.md
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

### Machine-readable and conformance artifacts

- Active schemas and the Schema Catalog under `schemas/`
- Controlled registries under `registries/`
- The OpenAPI contract and interface catalog under `api/`
- The conformance relationship model, conformance specification, Harness Checks, Test Vectors, mappings, fixtures, and formal Test Cases under `conformance/`

### Supporting artifacts

- Controlled Implementation Profile format artifacts, profiles, catalogs, and package manifest under `implementer/`
- `RELEASE_NOTES_v2.0.5.md` — release notes for the current v2.0.5 Public Review Controlled Baseline
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

This controlled release is AGCP v2.0.5 Public Review Controlled Baseline, baseline date 2026-08-05. Subsequent normative or machine-readable changes SHALL be issued as a later versioned revision and recorded in `governance/CHANGELOG.md`.

---

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

AGCP v2.0.5 is the current Public Review Controlled Baseline. Active catalogs and controlled artifacts use lifecycle `CURRENT`, and the controlled baseline date is `2026-08-05`. The controlled policy and validation are published under `governance/AGCP-Release-Lifecycle-Metadata-Policy.md` and `governance/AGCP-release-lifecycle-metadata-validation.json`.


## v2.0.5 repository-wide integrity gate

The aggregate validator is `governance/validate_repository_integrity.py`; its controlled report is `governance/AGCP-v2.0.5-repository-integrity-validation.json`.

## v2.0.5 repository synchronization

The accumulated correction set is synchronized through `RTM-1.46`, Schema Catalog `1.0.50`, Interface Catalog `1.0.5`, Registry Entry Catalog `1.0.3`, and Implementation Profile Catalog `1.0.3`. The machine-readable repository manifest and controlled validation report are under `governance/`.
