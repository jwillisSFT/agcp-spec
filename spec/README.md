# AGCP Specification Library

**Artifact Lifecycle:** Current  
**Current Published Repository Release:** AGCP v2.1.0  
**Synchronized Change-Set Target:** AGCP v2.1.x  
**Change-Set Status:** Closed for downstream implementation  
**Controlling Published Baseline:** AGCP v2.1.0 Public Review Controlled Baseline  
**Baseline Date:** 2026-08-15

## Overview

This directory contains the normative and supporting specifications that define the Artificial Intelligence Governance Control Plane (AGCP).

AGCP is a deterministic runtime governance architecture that governs execution at the Commit Boundary. The specification ecosystem separates normative requirements, architectural guidance, implementation specifications, and conformance artifacts into complementary documents.

---

# Specification Precedence

Where interpretation requires resolution among AGCP sources, the following order applies:

1. Published AGCP Runtime Governance Conformance Requirements (CRs)
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile
4. Implementation Profiles
5. AGCP Conformance Test Suite
6. Reference Implementations

The CRs establish controlled normative capability requirements, and the Core defines corresponding normative runtime behavior. The ARM is the authoritative architectural vocabulary and conceptual reference used to interpret ARM-defined concepts, but it does not independently create conformance obligations. Normative Statements are extracted atomic obligations from the Core used for stable identification and traceability. The RTM is the authoritative traceability artifact. Neither the Normative Statements, RTM, tests, assessments, profiles, nor reference implementations supersede a higher-precedence normative source.

---

# Documents

## AGCP Core Specification

Defines the normative execution semantics and constitutional requirements for runtime governance.

The Core Specification defines:

* architectural scope
* governance processing model
* execution authorization
* Commit Boundary semantics
* governance evidence
* lifecycle semantics
* governance invariants
* conformance requirements

The Core Specification is the second-precedence normative source after the published CRs and defines AGCP normative runtime behavior. Applicable adopted normative Companion Specifications may add profile-specific obligations without weakening or contradicting the CRs or Core.

---

## Architecture Reference Model (ARM)

The Architecture Reference Model provides the authoritative architectural vocabulary and conceptual reference supporting interpretation of the CRs and Core Specification. It is non-normative and does not independently create conformance obligations.

The ARM explains:

* architectural concepts
* design rationale
* reference architecture
* implementation considerations
* processing relationships
* governance services
* illustrative examples

The ARM introduces no additional normative requirements.

---

## Normative Statements

The Normative Statements document extracts and enumerates atomic obligations from the Core Specification for stable identification, traceability, testing, and assessment. It does not create an independently superior normative source and does not alter the precedence of the CRs, Core, or applicable adopted normative Companion Specifications.

Each statement:

* has a unique identifier
* traces to the Core Specification
* supports conformance verification
* supports requirements traceability

---

## Companion Specifications

Companion Specifications define implementation-specific aspects of the AGCP ecosystem.

Examples include:

* Protocol specifications
* Schema specifications
* HTTP/API specifications
* Operational profiles
* Security profiles
* Storage contracts
* Registry specifications

Applicable normative Companion Specifications may add profile-specific obligations only where expressly adopted. They remain below the CRs and Core in precedence and SHALL NOT weaken, replace, or contradict either source.

---

# Related Repository Artifacts

Additional repository components include:

| Artifact                               | Purpose                                 |
| -------------------------------------- | --------------------------------------- |
| Runtime Governance Requirements        | Requirements catalog                    |
| Requirements Traceability Matrix (RTM) | End-to-end requirements traceability    |
| Conformance Test Suite                 | Verification of normative behavior      |
| JSON Schemas                           | Machine-readable data definitions       |
| API Specifications                     | HTTP/OpenAPI interfaces                 |
| Registries                             | Controlled vocabularies and identifiers |
| Assessment Frameworks                  | Governance evaluation and assurance     |

---

# Normative and Informative Content

The specification ecosystem distinguishes between normative and informative artifacts.

## Normative Sources

Normative behavior is established by:

1. Published AGCP Runtime Governance Conformance Requirements (CRs)
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile

Implementation Profiles, the Conformance Test Suite, and Reference Implementations occupy the lower precedence positions established by the Core. Normative Statements are extraction and traceability artifacts derived from the Core, not an independently superior normative source.

## Informative

Informative artifacts provide explanation, rationale, examples, and implementation guidance.

These include:

* Architecture Reference Model
* Repository architecture documentation
* Reference material

Informative documents introduce no additional normative requirements.

---

# Repository Versioning

The AGCP repository is versioned through GitHub Releases.

Released versions are archived through Zenodo.

Individual specification documents are maintained without embedded document version numbers. The GitHub Release identifies the authoritative published version of the complete specification ecosystem.

---

# Additional Information

For an overview of the repository architecture, see:

* `../ARCHITECTURE.md`

For repository usage and project information, see:

* `../README.md`



---

# Canonical Companion References

Repository documents shall reference controlled artifacts by canonical title and path. The controlled disposition of retired absent companion labels and noncanonical titles is published in `../governance/AGCP-Normative-Companion-Reference-Dispositions.md` with a machine-readable companion at `../governance/normative-companion-reference-dispositions.json`.

Governance Evidence is represented by DS-020 (`../schemas/governance_evidence.json`) and DS-033 (`../schemas/evidence_qualification_result.json`) under the controlling CR and Core obligations; no separate umbrella evidence specification is implied.

## v2.1.0 Governance Observability and Management Plane

The normative companion set now includes `AGCP-Governance-Observability-and-Management-Specification.md` (IF-003/IF-004) and `AGCP-Conformance-Test-Control-Specification.md` (optional IF-005). These interfaces support operational management, observability, and executable conformance metrology without weakening the governed-action or commit-boundary model.


## v2.1.x Final Traceability Closure

The synchronized specification layer is closed through `RTM-1.47`. The v2.1.x Normative Statement inventory contains 393 permanent identifiers, 390 current statements, and three retired/reserved identifiers. Formal Test Cases remain TC-001 through TC-122. DS/interface/profile/catalog relationships and the conformance support layer are synchronized through the final RTM. Repository-level closure status and validation are recorded in `../governance/AGCP-v2.1.x-REPOSITORY-CLOSURE.md` and `../governance/AGCP-v2.1.x-repository-closure-validation.json`.

## v2.1.x Trust, Governance Realization, and Profile Alignment

The controlled architecture distinguishes the Governance Decision Function / PDP from the Governance Realization Function (GRF). A Governance Decision does not by itself establish commit-bound authority. Execution Authorization is later consumed by the GRF, which re-establishes current commitment-sensitive eligibility, applies the controlling PEP Profile, constructs the Enforcement Context, and presents the exact transition to the PEP. The PEP controls crossing of the enforcement boundary.

`spec/AGCP-Trust-Model.md` is the controlled non-normative architectural trust reference. It is subordinate to the published CRs and Core and does not independently create conformance requirements.

The generic implementer framework includes two subordinate controlled profile types:

- Identity and Authorization Store (IAS) Profile - authoritative identity plus identity-system roles, groups, entitlements, governance permissions, reviewer classes, scopes, delegation/authority attributes, validity, and account state used as governance input; and
- PEP Profile - exact GRF-to-PEP action/target mapping, Enforcement Context requirements, caller authentication, PEP-to-target authority, response mapping, and fail-closed behavior.

Deployment-specific profiles remain separate from the generic specification unless intentionally published.
