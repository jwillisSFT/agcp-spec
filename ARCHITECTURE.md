# AGCP Architecture Overview

## Purpose

This document provides a high-level overview of the Artificial Intelligence Governance Control Plane (AGCP) architecture and explains how the specification artifacts within this repository relate to one another.

Normative behavior is established first by the published **AGCP Runtime Governance Conformance Requirements (CRs)** and then by the **AGCP Core Specification**. Applicable normative Companion Specifications may add profile-specific obligations only where expressly adopted. The Architecture Reference Model (ARM) governs architectural terminology and concept meaning without independently creating conformance obligations. Normative Statements, the RTM, tests, assessments, and reference artifacts support extraction, traceability, verification, and implementation and do not supersede the normative sources. This document is informative and introduces no additional normative requirements.

---

# Architecture Overview

AGCP is a deterministic runtime governance architecture that evaluates and authorizes governance-significant actions immediately prior to execution.

Rather than governing model behavior or training, AGCP governs **action execution** at the runtime execution boundary (the **Commit Boundary**), ensuring that every governed action satisfies deterministic governance requirements before execution is permitted.

The architecture is implementation independent and may be applied to autonomous agents, orchestration platforms, enterprise applications, APIs, robotic systems, cyber-physical systems, and other autonomous or programmatic execution environments.

---

# Runtime Governance Pipeline

At a high level, governed execution proceeds through the following stages:

```
Proposal
    │
    ▼
Proposal Qualification
    │
    ▼
Governance Decision Function
    │
    ▼
Execution Authorization / Eligible Nonterminal State
    │
    ├── Continuation Integrity, where applicable while nonterminal
    │
    ▼
Governance Realization and Commit Boundary
    │
    ▼
Governed Execution
```

Governance Evidence is a cross-cutting supporting service generated during applicable governance-significant processing; it is not a final sequential stage. Continuation Integrity applies only before commitment while the Proposal remains nonterminal. Separately defined post-commit operational controls are distinct from Continuation Integrity.

Each governance stage and supporting service is governed by the applicable CRs and the AGCP Core Specification, together with any expressly adopted normative Companion Specification obligations.

---

# Architectural Principles

The AGCP architecture is founded on several core principles:

* deterministic governance decisions
* implementation independence
* explicit governance authority
* separation of reasoning from execution governance
* non-bypassable execution authorization
* immutable governance evidence
* tenant and domain isolation
* governance configuration integrity
* auditable governance lifecycle

These principles are further explained in the Architecture Reference Model (ARM).

---

# Specification Ecosystem

The AGCP specification is organized into complementary artifacts.

| Artifact                               | Purpose                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Runtime Governance Conformance Requirements (CRs) | Highest-precedence controlled normative capability requirements                                   |
| AGCP Core Specification                | Normative runtime behavior                                                                         |
| Applicable normative Companion Specifications | Profile-specific normative obligations when expressly adopted                               |
| Architecture Reference Model (ARM)     | Authoritative architectural vocabulary and conceptual reference; non-normative                     |
| Normative Statements                   | Extracted atomic Core obligations used for stable identification and traceability                  |
| Requirements Traceability Matrix (RTM) | Authoritative traceability across architecture, normative sources, implementation, and verification artifacts |
| Implementation Profiles                | Applied conformance scope below adopted normative Companion Specifications                         |
| Conformance Test Suite                 | Verification artifact below the normative sources                                                  |
| Reference Implementations              | Lowest-precedence illustrative implementation artifacts                                            |

---

# Repository Organization

The repository is organized into the following current directories:

```text
spec/
    Runtime Governance Requirements
    Core Specification
    Architecture Reference Model
    Normative Statements
    Requirements Traceability Matrix and traceability process documents
    Normative Companion Specifications

lifecycle/
    Governance lifecycle, progression, and implementation guidance

schemas/
    Active JSON Schemas, examples, and Schema Catalog

api/
    OpenAPI contract and interface catalog

registries/
    Controlled registry documents and registry-entry catalog

conformance/
    Conformance Specification, traceability and automation relationship model, Harness Checks, Test Vectors, mappings, fixtures, and Test Cases

governance/
    Versioning, change history, contribution guidance, and release-validation records

implementer/
    Controlled Implementation Profile format specification and schema
    Implementation Profile authoring template
    Controlled and informational profiles
    Profile catalog and package manifest

reference/
    Reference implementation pseudocode and supporting material

diagrams/
    Canonical architecture diagrams

research/
    Historical and explanatory publications
```

---

# Governance Artifacts

The repository contains three categories of artifacts.

## Normative

Normative sources define required behavior in the following order of precedence:

1. Published AGCP Runtime Governance Conformance Requirements (CRs)
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile

Implementation Profiles, the Conformance Test Suite, and Reference Implementations are lower-precedence application and verification artifacts. Normative Statements are extracted atomic obligations from the Core used for identification and traceability; they are not an independently superior normative source.

## Informative

Informative artifacts provide architectural explanation, rationale, implementation guidance, and examples.

Examples include:

* Architecture Reference Model
* Architecture Overview
* Reference documentation

## Machine-readable

Machine-readable artifacts support implementation and conformance.

Examples include:

* JSON Schemas
* OpenAPI definitions
* Registry definitions
* Conformance mappings
* Test manifests

---

# Conformance

Conformance is determined by satisfying the applicable CRs, Core requirements, expressly adopted normative Companion Specification obligations, and implementation-profile requirements in the precedence order established by the Core Specification.

The ARM governs architectural terminology and concept meaning. Core obligations are assigned stable Normative Statement identifiers for extraction and traceability, and the RTM maintains the authoritative mappings among normative sources, implementation artifacts, and conformance tests.

The relationship among Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, and profile-level conformance determinations is governed by `conformance/AGCP-Conformance-Traceability-and-Automation-Model.md`. Harness artifacts automate portions of Formal Test Cases and do not independently establish conformance.

---

# Versioning

Repository releases are managed through GitHub Releases.

Released versions are archived through Zenodo.

The repository may contain work in progress between official releases.

---

# Additional Information

The following documents provide further information:

* AGCP Core Specification
* AGCP Architecture Reference Model
* AGCP Normative Statements
* Runtime Governance Requirements
* Requirements Traceability Matrix
* Conformance Test Suite

## Governance Approval command/record boundary

DS-045 Governance Approval Submission is an untrusted command at IF-001. DS-026 Governance Approval Artifact is an authoritative AGCP-created or AGCP-qualified record. The public contract rejects claimant assertions of server-derived verification, lifecycle, quorum, evidence, replay, digest, and ledger state.

### Algorithm-explicit digest contract

`schemas/common.json#/$defs/content_digest` is the shared algorithm/output-length contract. `conformance/digests/` contains reusable positive and negative vectors, and `governance/validate_content_digest_contract.py` verifies dependent schemas, examples, catalogs, RTM mappings, and test mappings.

## IF-001 Error and Metadata Contract

`schemas/error_response.json`, `schemas/meta_response.json`, `api/AGCP-HTTP-Contract.yaml`, and `registries/rejection-code-registry.json` form the public IF-001 error and metadata contract. Reusable vectors reside under `conformance/http/`; automated validation resides under `governance/`.

## Semantic fixture validation layer

Controlled examples in `schemas/examples/` are structural schema fixtures. The `conformance/semantic-fixtures/` package adds cross-field equality rules and negative mismatch vectors so structurally valid but semantically contradictory objects cannot be accepted as positive conformance evidence. Claimant-assertion negatives remain in the command-versus-record package.

## Normative companion reference integrity

`governance/AGCP-Normative-Companion-Reference-Dispositions.md` and `governance/normative-companion-reference-dispositions.json` control the disposition of absent or noncanonical companion labels. `governance/validate_normative_companion_references.py` scans repository text and Office artifacts, validates canonical replacement paths, and prevents retired labels from reappearing as active normative references.


## Release and lifecycle metadata control

`governance/release-lifecycle-metadata.json` separates repository release target, release-target status, controlling published baseline, publication maturity, specification version, artifact lifecycle, and baseline date. Catalogs, normative specification headers, manifests, metadata examples, validation reports, and release notes are validated against that policy.


## Repository synchronization control

`governance/AGCP-v2.0.1-repository-synchronization-manifest.json` inventories the accumulated public-repository correction set, and `governance/validate_repository_synchronization.py` verifies catalogs, RTM versions and mappings, manifests, vectors, validation reports, indexes, release records, and file hashes before packaging.


## Repository-wide integrity gate
