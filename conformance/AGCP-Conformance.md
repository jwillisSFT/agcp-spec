# AGCP Conformance Specification

**Status:** Normative  
**Applies To:** All AGCP-conformant implementations

> **Versioning**
>
> This specification is versioned by the AGCP repository release. All references to specification compatibility refer to the repository release rather than an embedded document version.

---

# Table of Contents

1. [Purpose](#1-purpose)  
2. [Conformance Model Overview](#2-conformance-model-overview)  
3. [Conformance Profiles](#3-conformance-profiles)  
   - [L1 — Schema & Envelope Validation](#31-level-l1--schema--envelope-validation)  
   - [L2 — Ordered Governance Mediation](#32-level-l2--ordered-governance-mediation)  
   - [L3 — Deterministic Governance](#33-level-l3--deterministic-governance)  
   - [L4 — Execution Authorization Control](#34-level-l4--execution-authorization-control)  
   - [L5 — Multitenant Governance Isolation](#35-level-l5--multitenant-governance-isolation)  
4. [Assertion Model](#4-assertion-model)  
5. [Required Assertions](#5-required-assertions-core-set)  
6. [Test Requirements](#6-test-requirements)  
7. [Conformance Claim Format](#7-conformance-claim-format)  
8. [Conformance Failure](#8-conformance-failure)  
9. [Certification Model (Optional)](#9-certification-model-optional)  
10. [Repository Compatibility](#10-repository-compatibility)  
11. [Non-Goals](#11-non-goals)  
12. [Summary](#12-summary)

---

# 1. Purpose

This specification defines the requirements for claiming conformance to the Autonomous Governance Control Plane (AGCP).

It specifies:

- The AGCP conformance model
- Conformance profiles (L1–L5)
- Assertion model
- Conformance test requirements
- Deterministic governance validation
- Governance Evidence validation
- Append-Only Governance Ledger validation
- Canonical State validation
- Governance Approval Artifact validation
- Execution Authorization validation
- applicable pre-commit Continuation Integrity validation
- Governance Realization and Commit-Bound Admissibility validation
- Policy Enforcement Point and Commit Boundary validation
- Multitenant and Governance Domain isolation validation
- Conformance declaration format

This specification complements the AGCP Core Specification and defines how an implementation demonstrates conformance to the normative requirements defined throughout the AGCP specification suite.

Conformance ensures that AGCP implementations:

- Implement deterministic governance behavior
- Produce interoperable externally observable behavior
- Preserve Canonical State integrity
- Resolve Canonical State deterministically from the applicable qualified authoritative governance sources, using authoritative Governance Ledger ordering for incorporated governance events and Derived Lifecycle State
- Preserve Governance Evidence
- Preserve ordered Append-Only Governance Ledger integrity
- Enforce governance policy before execution
- Enforce governed approval and human adjudication where required
- Enforce Execution Authorization
- preserve applicable pre-commit Continuation Integrity for nonterminal Proposals
- enforce Governance Realization and final Commit-Bound Admissibility
- enforce Policy Enforcement Point and Commit Boundary requirements
- Preserve multitenant and Governance Domain isolation
- Maintain interoperability within the same AGCP repository release

---

# 2. Conformance Model Overview

AGCP conformance is defined through the combination of:

- Normative specification requirements expressed using RFC 2119 / RFC 8174 terminology
- Assertion identifiers (`AGCP-A-XXXX`)
- Conformance profiles (L1–L5)
- Frozen CR-to-Core-derived-NS-to-TC traceability maintained by the RTM
- Required conformance test coverage
- Deterministic replay verification
- Governance Evidence validation
- Append-Only Governance Ledger validation
- Canonical State validation

The authoritative normative precedence is:

```text
1. Published AGCP Runtime Governance Conformance Requirements (CRs)
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile
4. Implementation Profiles
5. AGCP Conformance Test Suite
6. Reference Implementations
```

The ARM governs architectural terminology and concept meaning where an ARM-defined concept is used, but it does not independently create conformance obligations. Normative Statements are extracted atomic obligations from the Core used for stable identification and traceability; they are not an independently superior normative source.

Assertion identifiers (`AGCP-A-XXXX`) provide an implementation-facing conformance abstraction for harness execution, reporting, and certification activities. They are derived from the applicable normative sources and SHALL NOT supersede the CR-to-Core-derived-NS-to-TC mappings maintained by the RTM.

The relationship semantics among CRs, NS identifiers, the RTM, Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, and conformance determinations are defined in `AGCP-Conformance-Traceability-and-Automation-Model.md`. Harness artifacts automate portions of Formal Test Cases and do not independently establish conformance.

A conformant implementation SHALL satisfy every applicable normative requirement for the conformance profile it claims.

Implementations MAY exceed the requirements of a profile, but SHALL NOT claim conformance to a profile unless every mandatory requirement for that profile is satisfied.

Externally observable behavior SHALL take precedence over implementation architecture. Implementations MAY differ internally provided that they produce equivalent externally observable governance behavior and satisfy all applicable normative requirements.

# 3. Conformance Profiles

AGCP defines five cumulative conformance profiles.

Each profile includes all requirements of the preceding profiles unless explicitly stated otherwise.

A conformance claim SHALL identify the highest profile satisfied by the implementation.

The conformance profiles are:

| Profile | Scope |
|---------|-------|
| L1 | Schema & Envelope Validation |
| L2 | Ordered Governance Mediation |
| L3 | Deterministic Governance |
| L4 | Execution Authorization Control |
| L5 | Multitenant Governance Isolation |

Implementations MAY implement functionality beyond a claimed profile. Additional functionality SHALL NOT invalidate a conformance claim provided that all mandatory requirements remain satisfied.

---

## 3.1 Level L1 — Schema & Envelope Validation

L1 establishes baseline interoperability.

An implementation claiming L1 conformance SHALL:

- Implement the required AGCP HTTP interface.
- Accept and produce artifacts conforming to the published JSON Schemas.
- Validate request and response payloads against the applicable schemas.
- Reject malformed requests using the defined rejection codes.
- Produce deterministic externally observable interface behavior.
- Support the required Governance Evidence structures.
- Preserve provenance information required by the Provenance Wire Format Specification.

L1 verifies interoperability of the public interface rather than internal implementation architecture.

---

## 3.2 Level L2 — Ordered Governance Mediation

L2 verifies correct execution of the normative governance pipeline.

An implementation claiming L2 conformance SHALL:

- Execute Proposal Qualification.
- Evaluate the Governance Decision Function.
- Apply Policy Evaluation Contract (PEC) processing where required.
- Produce deterministic Governance Decision Results.
- Preserve applicable pre-commit Continuation Integrity while a Proposal remains nonterminal.
- Perform Governance Realization and resolve final Commit-Bound Admissibility before permitting a governed consequence.
- Apply the governance decision through the Policy Enforcement Point at or immediately adjacent to the Commit Boundary.
- Produce Governance Evidence throughout every applicable governance-significant stage as a cross-cutting supporting service.
- Record governance-significant events in the Append-Only Governance Ledger.
- Preserve ordering of governance events.
- Reject proposals that fail mandatory governance requirements.

The governance pipeline SHALL execute deterministically for identical authoritative inputs.

Implementations MAY optimize internal execution provided externally observable behavior remains equivalent.

---

## 3.3 Level L3 — Deterministic Governance

L3 verifies deterministic governance behavior.

An implementation claiming L3 conformance SHALL:

- Produce identical governance outcomes for identical authoritative inputs.
- Resolve Canonical State deterministically from the complete set of applicable qualified authoritative governance sources.
- Interpret incorporated Governance Ledger records using authoritative ledger ordering.
- Support deterministic replay.
- Preserve Governance Evidence sufficient for deterministic replay.
- Preserve ordered governance history.
- Detect non-deterministic governance behavior.

The ordered Append-Only Governance Ledger SHALL be authoritative for recorded governance events, event ordering, and Derived Lifecycle State. It need not originate every governance-relevant fact incorporated into Canonical State.

Timestamp ordering SHALL NOT substitute for authoritative ledger ordering of recorded governance events.

Materialized state views MAY be used for performance provided they remain reproducible from the applicable qualified authoritative governance sources, including ordered Governance Ledger records where applicable.

---

## 3.4 Level L4 — Execution Authorization Control

L4 verifies governance controls that directly authorize execution.

An implementation claiming L4 conformance SHALL:

- Support governed human adjudication and Governance Approval where required by governance policy.
- Validate Governance Approval Artifacts.
- Enforce required governed approval or adjudication completion before Execution Authorization.
- Produce Execution Authorization artifacts.
- Preserve applicable pre-commit Continuation Integrity while an authorized or otherwise eligible Proposal remains nonterminal.
- Perform Governance Realization and resolve current Commit-Bound Admissibility immediately before commitment.
- Enforce the resulting decision through the Policy Enforcement Point at or immediately adjacent to the Commit Boundary.
- Prevent execution without valid authorization, applicable continuation integrity, final admissibility, and enforcement binding.
- Record Governance Approval, Execution Authorization, applicable Continuation Integrity events, Governance Realization and Commit Boundary processing, and associated Governance Evidence in the Append-Only Governance Ledger.
- Reject attempts to bypass required governance controls.

Execution SHALL occur only after successful completion of the required governance pipeline.

---

## 3.5 Level L5 — Multitenant Governance Isolation

L5 verifies isolation across tenants and governance domains.

An implementation claiming L5 conformance SHALL:

- Enforce tenant isolation.
- Enforce Governance Domain isolation where applicable.
- Prevent unauthorized cross-tenant access.
- Prevent unauthorized cross-domain access.
- Preserve tenant-scoped Governance Evidence.
- Preserve tenant-scoped Append-Only Governance Ledger history.
- Preserve tenant-scoped Canonical State derivation.
- Demonstrate deterministic behavior across isolated tenants.
- Pass all required negative isolation tests.

Cross-boundary operations SHALL require explicit authorization consistent with the AGCP Core Specification.

Failure of mandatory isolation requirements invalidates an L5 conformance claim.

# 4. Assertion Model

## 4.1 Purpose

AGCP assertion identifiers provide a stable, implementation-oriented abstraction for conformance verification, automated harness execution, reporting, and certification.

Assertions are intended to facilitate executable conformance testing while preserving traceability to the authoritative normative requirements.

Assertion identifiers are stable across compatible repository releases unless the underlying normative behavior changes incompatibly.

---

## 4.2 Relationship to the Normative Specifications

AGCP normative requirements are established according to the Core-defined precedence order: published CRs, Core Specification, and applicable adopted normative Companion Specifications, followed by the lower-precedence profiles, Test Suite, and reference implementations.

Assertions SHALL be derived from the authoritative specifications and SHALL NOT introduce new normative requirements.

The authoritative traceability model is:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
        |
        v
Derived Assertion(s)
```

Assertions support implementation and certification activities but SHALL NOT supersede the authoritative CR → NS → TC mappings.

If a conflict exists between an assertion and another AGCP source, it SHALL be resolved using the Core-defined precedence order. An assertion, Normative Statement, Test Case, harness check, or vector SHALL NOT weaken or supersede a higher-precedence normative source.

---

## 4.3 Assertion Identifier Format

Assertion identifiers SHALL use the following format:

```
AGCP-A-XXXX
```

where:

- `AGCP` identifies the specification family.
- `A` designates a conformance assertion.
- `XXXX` is a repository-assigned identifier.

Assertion identifiers SHALL remain stable across repository releases unless a breaking normative change requires replacement.

Retired assertions SHALL NOT be reassigned.

---

## 4.4 Assertion Categories

Assertions MAY be grouped into implementation-oriented categories.

Recommended categories include:

| Category | Scope |
|----------|-------|
| INTERFACE | HTTP interface, schemas, media types |
| GOVERNANCE | Proposal Qualification and Governance Decision Function |
| POLICY | Policy Evaluation Contract (PEC) processing |
| GOVERNANCE_APPROVAL | Governance Approval and human-adjudication processing |
| EXECUTION | Execution Authorization, applicable pre-commit Continuation Integrity, Governance Realization, Commit-Bound Admissibility, Policy Enforcement Point, and Commit Boundary processing |
| EVIDENCE | Cross-cutting Governance Evidence generation and validation throughout applicable governance-significant processing |
| LEDGER | Append-Only Governance Ledger behavior |
| CANONICAL_STATE | Canonical State derivation and deterministic replay |
| MULTITENANCY | Tenant and Governance Domain isolation |
| SECURITY | Provenance, integrity, cryptographic validation |
| CONFORMANCE | Reporting, claims, and certification behavior |

Categories exist solely to organize assertions and SHALL NOT affect normative interpretation.

---

## 4.5 Assertion Construction

Each assertion SHOULD evaluate a single externally observable governance behavior whenever practical.

Assertions SHOULD be:

- deterministic
- implementation-independent
- objectively verifiable
- reproducible
- automatable

Assertions SHALL avoid reliance on implementation-specific internal architecture unless explicitly required by a normative specification.

---

## 4.6 Assertion Evaluation

An assertion SHALL evaluate observable behavior rather than implementation details.

Observable behavior MAY include:

- HTTP responses
- governance outcomes
- Proposal Views
- Governance Decision Results
- Governance Approval Artifacts
- Execution Authorization artifacts
- Commit Boundary results
- Governance Evidence
- Append-Only Governance Ledger behavior
- Canonical State resolution and, for replay, reproduction of Canonical State resolution from recorded qualified source versions and applicable ordered Governance Ledger records
- rejection codes
- conformance reports

Internal implementation mechanisms are outside the scope of assertion evaluation unless explicitly required by a normative specification.

---

## 4.7 Deterministic Assertions

Assertions evaluating deterministic governance SHALL verify that identical authoritative inputs produce identical externally observable governance behavior.

Where applicable, deterministic evaluation SHALL verify:

- Proposal Qualification
- Governance Decision Function
- Policy Evaluation Contract processing
- Governance Approval and human-adjudication processing
- Execution Authorization
- applicable pre-commit Continuation Integrity
- Governance Realization and Commit-Bound Admissibility
- Policy Enforcement Point and Commit Boundary processing
- cross-cutting Governance Evidence generation and binding
- Append-Only Governance Ledger ordering
- Canonical State derivation

Deterministic replay SHALL reproduce the same Canonical State when evaluated using the same qualified authoritative source versions, applicable Governance Ledger records in authoritative order, governance configuration, and policy artifacts.

Timestamp ordering SHALL NOT substitute for ledger sequence ordering.

---

## 4.8 Negative Assertions

Negative assertions verify that prohibited behavior does not occur.

Examples include:

- acceptance of malformed requests
- unauthorized execution
- bypass of required Governance Approval or human adjudication
- invalid Execution Authorization
- invalid Commit Boundary processing
- invalid provenance
- cross-tenant access
- cross-domain access
- ledger modification
- acceptance of reordered Governance Ledger history as equivalent for ledger-derived events or Derived Lifecycle State
- acceptance of Governance Evidence with invalid integrity

Negative assertions SHALL verify that implementations reject prohibited behavior using the appropriate rejection codes and externally observable behavior.

---

## 4.9 Assertion Traceability

Every assertion SHALL be traceable to one or more:

- Normative Statements
- Conformance Requirements
- Test Cases

Assertions SHALL NOT exist without authoritative traceability.

Derived traceability SHALL be maintained throughout the repository.

---

## 4.10 Assertion Stability

Assertion identifiers are intended to remain stable across compatible repository releases.

Editorial clarification SHALL NOT require new assertion identifiers.

Breaking normative changes MAY require:

- retirement of an assertion,
- replacement by one or more new assertions, or
- remapping to updated Normative Statements.

Repository release documentation SHOULD identify retired and replacement assertions where applicable.

---

# 5. Required Conformance Assertions

The following conformance assertions define the minimum observable behaviors that every AGCP implementation SHALL satisfy.

These assertions are derived from the applicable CRs and Core behavior through the Core-derived Normative Statement mappings and Test Cases maintained in the RTM.

This specification does not introduce an independent assertion identifier system. The authoritative conformance traceability model remains:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
```

---

## 5.1 Schema & Envelope Validation

An implementation SHALL:

- Validate requests and responses against the published AGCP JSON Schemas.
- Reject malformed requests using the appropriate rejection codes.
- Produce structured error responses conforming to the published ErrorResponse schema.
- Produce deterministic externally observable interface behavior.

---

## 5.2 Ordered Governance Mediation

An implementation SHALL:

- Execute Proposal Qualification before Governance Decision evaluation.
- Execute Policy Evaluation Contract (PEC) processing where required.
- Evaluate constraints before invariants.
- Complete invariant evaluation before determining Governance Approval requirements.
- Complete Execution Authorization before final commit-time processing.
- Preserve applicable pre-commit Continuation Integrity while a Proposal remains nonterminal.
- Perform Governance Realization and resolve final Commit-Bound Admissibility before commitment.
- Apply the decision through the Policy Enforcement Point at or immediately adjacent to the Commit Boundary.
- Produce Governance Evidence throughout governance-significant processing as a cross-cutting supporting service.
- Record governance-significant events in the Append-Only Governance Ledger.

---

## 5.3 Deterministic Governance

An implementation SHALL:

- Produce identical governance outcomes for identical authoritative inputs.
- Produce deterministic Governance Decision Results.
- Reject non-deterministic governance behavior.
- Resolve Canonical State deterministically from the applicable qualified authoritative governance sources and preserve authoritative Governance Ledger ordering for incorporated governance events and Derived Lifecycle State.
- Preserve deterministic replay capability.

---

## 5.4 Governance Approval and Human Adjudication

Where governed approval or human adjudication is required by governance policy, an implementation SHALL:

- Validate Governance Approval Artifacts.
- Enforce required approvals.
- Reject expired or invalid review artifacts.
- Prevent Execution Authorization until required Governance Approval or human adjudication has successfully completed.

---

## 5.5 Execution Authorization, Continuation Integrity & Governance Realization/Commit Boundary

An implementation SHALL:

- Prevent execution without valid Execution Authorization.
- Preserve applicable pre-commit Continuation Integrity for nonterminal Proposals.
- Perform Governance Realization using current qualified governance inputs.
- Validate final Commit-Bound Admissibility, Governance Enforcement Binding, and Policy Enforcement Point requirements.
- Produce Governance Evidence during each applicable stage, including Continuation Integrity, Governance Realization, enforcement, and Commit Boundary processing.
- Record successful commitment and associated governance-significant processing in the Append-Only Governance Ledger.

---

## 5.6 Governance Evidence & Ledger

An implementation SHALL:

- Produce Governance Evidence conforming to the published schema.
- Preserve immutable Governance Evidence.
- Preserve an Append-Only Governance Ledger.
- Preserve deterministic ledger ordering.
- Use ledger sequence, not timestamps or implementation-specific storage order, as the authoritative ordering for recorded governance events and Derived Lifecycle State.
- Support deterministic reproduction of the Canonical State evaluation basis from the applicable qualified authoritative source versions and ordered Governance Ledger records.

---

## 5.7 Multitenant Governance Isolation

An implementation SHALL:

- Enforce tenant isolation.
- Enforce Governance Domain isolation where applicable.
- Reject unauthorized cross-tenant operations.
- Reject unauthorized cross-domain operations.
- Preserve tenant-scoped Governance Evidence.
- Preserve tenant-scoped Append-Only Governance Ledger history.
- Preserve tenant-scoped Canonical State derivation.

---

## 5.8 Registry Conformance

An implementation SHALL:

- Use only published registry values.
- Reject unknown registered constraint types.
- Reject unknown registered invariant types.
- Use published rejection codes.

---

# 6. Test Requirements

Conformance testing SHALL verify externally observable behavior rather than implementation-specific architecture.

The RTM is the authoritative traceability artifact. It maps the applicable CRs, Core-derived Normative Statement identifiers, adopted Companion Specification obligations, implementation artifacts, and Conformance Test Cases without changing normative precedence.

Formal Test Cases remain the authoritative assessment procedures. Harness Checks and Harness Test Vectors MAY provide executable evidence for mapped TC criteria, subject to `AGCP-Conformance-Traceability-and-Automation-Model.md`; a harness result alone does not establish Test Case or profile conformance.

---

## 6.1 Positive Tests

Positive tests SHALL verify:

- successful Proposal Qualification
- successful Governance Decision evaluation
- successful Governance Approval and human-adjudication processing where required
- successful Execution Authorization
- successful applicable pre-commit Continuation Integrity where the Proposal remains nonterminal
- successful Governance Realization and final Commit-Bound Admissibility
- successful Policy Enforcement Point and Commit Boundary processing
- successful cross-cutting Governance Evidence generation and binding
- successful Append-Only Governance Ledger recording
- successful Canonical State derivation

---

## 6.2 Negative Tests

Negative tests SHALL verify rejection of:

- malformed requests
- invalid provenance
- invalid tenant state
- governance policy rejection
- failed Governance Approval or human adjudication
- unauthorized execution
- invalid Commit Boundary processing
- unauthorized cross-tenant access
- unauthorized Governance Domain access
- invalid Governance Evidence
- ledger integrity violations
- invalid Canonical State resolution or invalid replay reproduction from recorded qualified source versions and applicable ordered Governance Ledger records

---

## 6.3 Deterministic Governance Tests (L3+)

Deterministic governance testing SHALL verify that identical authoritative inputs produce identical externally observable governance behavior.

Testing SHALL include:

1. Submission of an identical Proposal using identical authoritative inputs.
2. Recording of the Governance Decision Result, Governance Evidence, Append-Only Governance Ledger entries, and Canonical State.
3. Repetition of the evaluation.
4. Comparison of the externally observable governance results.

Canonical State SHALL be reproducible from the same complete set of qualified authoritative source versions and applicable Governance Ledger records used for the original evaluation.

Timestamp ordering SHALL NOT substitute for ledger sequence ordering.

---

## 6.4 Canonical State Resolution and Replay Reproduction Tests (L3+)

Testing SHALL verify:

1. Deterministic Canonical State resolution using the same complete set of qualified authoritative source versions used for the original evaluation.
2. Authoritative ledger ordering for any incorporated Governance Ledger records and Derived Lifecycle State.
3. Deterministic reproduction of a materialized Canonical State view from the applicable qualified authoritative sources, where such a view is implemented.
4. Rejection or non-equivalence of reordered ledger histories for ledger-derived governance events or Derived Lifecycle State.
5. Preservation of source provenance, source-version references, Governance Evidence integrity, and ledger-ordering evidence throughout resolution and replay.

---

## 6.5 Multitenant Governance Isolation Tests (L5)

Testing SHALL verify:

1. Tenant isolation.
2. Governance Domain isolation where applicable.
3. Cross-tenant artifact protection.
4. Cross-tenant Append-Only Governance Ledger protection.
5. Cross-tenant Canonical State protection.
6. Cross-tenant Commit Boundary protection.

Unauthorized operations SHALL be rejected using the appropriate rejection codes.

---

# 7. Conformance Claim Format

An implementation claiming AGCP conformance SHALL publish a Conformance Declaration.

The declaration SHALL include:

- Implementation name
- Implementation version
- Supported AGCP repository release
- Claimed conformance profile (L1–L5)
- Supported cryptographic profile(s), where applicable
- Reference to the executed conformance test suite
- Date of the conformance claim

The declaration MAY additionally include:

- Organization
- Product identifier
- Deployment profile
- Supported optional capabilities
- Certification information, if applicable

### Example

```
AGCP Conformance Declaration

Implementation: Example Governance Engine
Implementation Version: 2.3.1
Repository Release: 2026.1
Conformance Profile: L4
Cryptographic Profiles:
  - Ed25519
  - ES256

Conformance Test Suite:
  AGCP Official Conformance Suite

Declaration Date:
  YYYY-MM-DD
```

A Conformance Declaration SHALL accurately represent the capabilities demonstrated by the implementation under test.

Implementations SHALL NOT claim support for functionality that has not been successfully demonstrated through the applicable conformance tests.

---

# 8. Conformance Failure

An implementation SHALL NOT claim conformance to a profile if any mandatory requirement for that profile is not satisfied.

Examples include, but are not limited to:

- Failure of any required Conformance Requirement (CR)
- Failure of any required Test Case (TC)
- Failure of deterministic governance verification
- Failure of Canonical State resolution or failure to reproduce that resolution from recorded qualified source versions and applicable ordered Governance Ledger records for replay
- Failure of Governance Evidence validation
- Failure of Append-Only Governance Ledger validation
- Failure of Governance Approval enforcement
- Failure of Execution Authorization validation
- Failure of Commit Boundary validation
- Failure of tenant isolation
- Failure of Governance Domain isolation where applicable

Failure at a higher conformance profile SHALL NOT invalidate a valid claim at a lower profile provided all mandatory requirements of the lower profile remain satisfied.

---

# 9. Certification Model (Optional)

AGCP does not mandate a specific certification process.

Implementations MAY be evaluated using:

- Self-attestation
- Independent third-party validation
- Community validation
- Formal certification authority

Certification methodology is outside the scope of the AGCP Core Specification.

Certification SHALL NOT modify or supersede the normative requirements defined by the AGCP specification suite.

---

# 10. Repository Compatibility

AGCP specifications are versioned by repository release.

Implementations SHALL identify the repository release against which conformance is claimed.

Conformance is evaluated against the complete set of normative artifacts contained within the referenced repository release, including:

- AGCP Runtime Governance Conformance Requirements
- AGCP Core Specification
- Policy Evaluation Contract
- AGCP HTTP Interface Specification
- AGCP Multitenant Operational Specification
- AGCP Human Adjudication and Governance Approval Specification
- AGCP Provenance Wire Format Specification
- Append-Only Governance Ledger Specification
- AGCP Error Mapping
- active JSON Schemas, including DS-020 Governance Evidence and DS-033 Evidence Qualification Result
- published registries
- Requirements Traceability Matrix (RTM)
- Official Conformance Test Suite

Security and Governance Evidence obligations are evaluated through the controlling artifacts that actually exist in the referenced release; no absent umbrella companion is implied.

Repository releases preserve compatibility according to the repository governance process.

---

# 11. Non-Goals

This specification does not:

- Define implementation architecture.
- Mandate a specific programming language.
- Mandate a specific database.
- Mandate a specific ledger implementation technology.
- Mandate a specific policy engine.
- Mandate a specific execution engine.
- Mandate CI/CD tooling.
- Mandate certification authorities.
- Define deployment topology.

Conformance is determined exclusively by externally observable behavior and satisfaction of the published normative requirements.

---

# 12. Summary

AGCP conformance demonstrates that an implementation satisfies the normative requirements defined by the AGCP specification suite.

Conformance verifies:

- Interface interoperability
- Deterministic governance
- Governance pipeline correctness
- Governance Approval and human-adjudication processing
- Execution Authorization
- applicable pre-commit Continuation Integrity
- Governance Realization and final Commit-Bound Admissibility
- Policy Enforcement Point and Commit Boundary enforcement
- cross-cutting Governance Evidence production throughout applicable governance-significant processing
- Append-Only Governance Ledger integrity
- Canonical State derivation
- Deterministic replay
- Tenant isolation
- Governance Domain isolation where applicable

The authoritative conformance traceability model is:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
```

Conformance SHALL be demonstrated using the official AGCP Requirements Traceability Matrix (RTM) and Conformance Test Suite.

Implementations MAY exceed the minimum requirements defined by this specification, provided all mandatory requirements applicable to the claimed conformance profile are satisfied.
