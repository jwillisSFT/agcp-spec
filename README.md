> **Controlled repository baseline:** AGCP v2.0.0 Public Review  
> **Baseline date:** 2026-07-30  
> **Baseline composition:** CR-001 through CR-122; RTM-1.45; Schema Catalog 1.0.44; 122 formal Test Cases; 17 Harness Checks; 54 synchronized Harness Test Vectors; and 29 controlled fixtures.  
> This archive is a fixed review baseline. Any later change requires a versioned revision and a corresponding entry in `governance/CHANGELOG.md`.  
> **Release notes:** [`RELEASE_NOTES_v2.0.0.md`](RELEASE_NOTES_v2.0.0.md)  

# AGCP — Governance Control Plane Architecture

**Status:** Public Review — Controlled Baseline  
**Release:** AGCP v2.0.0  
**Baseline date:** 2026-07-30  
**Series:** AGCP Core Specification  

AGCP specifies a deterministic governance control-plane architecture for execution-bound authorization, lifecycle derivation, invariant enforcement, and multitenant isolation in automated systems.

The architecture is designed to eliminate reliance on independently mutable status fields, preserve authoritative ordering for recorded governance events, and require execution-time re-derivation of authorization eligibility from current qualified Canonical State resolved from applicable authoritative governance sources.

---

## Specification Status

AGCP v2.0.0 is issued as the controlled **Public Review** baseline dated 2026-07-30. The contents of this repository snapshot are the fixed basis for review, implementation comparison, and conformance evaluation until a later versioned revision is issued.

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
6. `spec/AGCP-Policy-Evaluation-Contract.md` — policy-evaluation companion specification
7. `spec/AGCP-HTTP-Interface-Specification.md` and `api/AGCP-HTTP-Contract.yaml` — interface semantics and executable contract
8. `spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md` — Governance Ledger Event requirements
9. `lifecycle/AGCP Governance Lifecycle Model.md` and `lifecycle/AGCP Normative Governance Progression Table.md` — lifecycle interpretation and progression
10. `conformance/AGCP-Conformance-Traceability-and-Automation-Model.md`, `conformance/AGCP-Conformance.md`, `conformance/AGCP-Test-Matrix.md`, and `conformance/AGCP-Conformance-Test-Vectors.md` — conformance relationships, profiles, mappings, and executable tests

---

## Repository Structure

The following abbreviated tree lists the current controlled paths used for review and implementation. Every named path exists in this release.

```text
.
├── README.md
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
│   └── ledger/
│       └── AGCP-Append-Only-Governance-Ledger-Specification.md
├── lifecycle/
│   ├── README.md
│   ├── AGCP Governance Lifecycle Model.md
│   ├── AGCP Normative Governance Progression Table.md
│   └── AGCP Governance Progression Implementation Guide.md
├── schemas/
│   ├── README.md
│   ├── SCHEMA-CATALOG.md
│   ├── catalog/
│   │   ├── schema-catalog.json
│   │   ├── schema-catalog.csv
│   │   └── schema-catalog-validation.json
│   ├── proposal_submit_request.json
│   ├── governed_action_proposal.json
│   ├── governance_approval_artifact.json
│   ├── governance_ledger_event.json
│   └── examples/
├── registries/
│   ├── README.md
│   ├── registry-entry-catalog.json
│   ├── registry-entry-catalog.csv
│   ├── constraint-type-registry.json
│   ├── invariant-type-registry.json
│   └── rejection-code-registry.json
├── conformance/
│   ├── README.md
│   ├── AGCP-Conformance-Traceability-and-Automation-Model.md
│   ├── AGCP-Conformance.md
│   ├── Conformance Test Suite.md
│   ├── AGCP-Test-Matrix.md
│   ├── AGCP-Conformance-Harness-Spec.yml
│   ├── AGCP-Conformance-Test-Vectors.md
│   ├── AGCP Harness Check Registry.md
│   ├── harness-checks.json
│   ├── test-mapping.json
│   ├── fixture-mapping.json
│   └── tests/
├── api/
│   ├── AGCP-HTTP-Contract.yaml
│   ├── INTERFACE-CATALOG.md
│   ├── interface-catalog.json
│   └── interface-catalog.csv
├── governance/
│   ├── AGCP-Versioning.md
│   ├── CHANGELOG.md
│   └── CONTRIBUTING.md
├── implementer/
│   └── AGCP-Implementation-Decision-Record-Template.md
├── reference/
│   ├── README.md
│   └── AGCP-HTTP-Reference-Implementation-Pseudocode.md
├── diagrams/
│   └── agcp-control-plane.png
└── research/
    └── README.md
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

- `RELEASE_NOTES_v2.0.0.md` — comparison-based release notes and migration guidance
- Current lifecycle documents under `lifecycle/`
- Versioning and contribution guidance under `governance/`
- Reference pseudocode under `reference/`
- The canonical control-plane diagram under `diagrams/`
- Historical and explanatory publications under `research/`

---

# What This Repository Does Not Contain

- Production implementation code
- Deployment artifacts
- Customer operating profiles
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

This controlled release is AGCP v2.0.0 Public Review, baseline date 2026-07-30. Subsequent changes SHALL be issued as a versioned revision and recorded in `governance/CHANGELOG.md`.

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
