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
   - [L1 — Interface & Schema Conformance](#31-level-l1--interface--schema-conformance)  
   - [L2 — Governance Pipeline Conformance](#32-level-l2--governance-pipeline-conformance)  
   - [L3 — Deterministic Governance](#33-level-l3--deterministic-governance)  
   - [L4 — Human Review, Execution Authorization & Commit Boundary](#34-level-l4--human-review-execution-authorization--commit-boundary)  
   - [L5 — Multitenant & Governance Domain Isolation](#35-level-l5--multitenant--governance-domain-isolation)  
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
- Human Review validation
- Execution Authorization validation
- Commit Boundary validation
- Multitenant and Governance Domain isolation validation
- Conformance declaration format

This specification complements the AGCP Core Specification and defines how an implementation demonstrates conformance to the normative requirements defined throughout the AGCP specification suite.

Conformance ensures that AGCP implementations:

- Implement deterministic governance behavior
- Produce interoperable externally observable behavior
- Preserve Canonical State integrity
- Derive Canonical State from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation can be deterministically reproduced
- Preserve Governance Evidence
- Preserve ordered Append-Only Governance Ledger integrity
- Enforce governance policy before execution
- Enforce Human Review where required
- Enforce Execution Authorization
- Enforce Commit Boundary requirements
- Preserve multitenant and Governance Domain isolation
- Maintain interoperability within the same AGCP repository release

---

# 2. Conformance Model Overview

AGCP conformance is defined through the combination of:

- Normative specification requirements expressed using RFC 2119 / RFC 8174 terminology
- Assertion identifiers (`AGCP-A-XXXX`)
- Conformance profiles (L1–L5)
- Frozen Requirements → Normative Statement → Test Case traceability
- Required conformance test coverage
- Deterministic replay verification
- Governance Evidence validation
- Append-Only Governance Ledger validation
- Canonical State validation

The authoritative normative hierarchy is:

```

Normative Specification
↓
Normative Statement (NS)
↓
Conformance Requirement (CR)
↓
Test Case (TC)

```

Assertion identifiers (`AGCP-A-XXXX`) provide an implementation-facing conformance abstraction for harness execution, reporting, and certification activities. They are derived from the authoritative normative specifications and SHALL NOT supersede the frozen Requirements → Normative Statement → Test Case traceability model.

A conformant implementation SHALL satisfy every applicable normative requirement for the conformance profile it claims.

Implementations MAY exceed the requirements of a profile, but SHALL NOT claim conformance to a profile unless every mandatory requirement for that profile is satisfied.

Externally observable behavior SHALL take precedence over implementation architecture. Implementations MAY differ internally provided that they produce equivalent externally observable governance behavior and satisfy all applicable normative requirements.
```

# 3. Conformance Profiles

AGCP defines five cumulative conformance profiles.

Each profile includes all requirements of the preceding profiles unless explicitly stated otherwise.

A conformance claim SHALL identify the highest profile satisfied by the implementation.

The conformance profiles are:

| Profile | Scope |
|---------|-------|
| L1 | Interface & Schema Conformance |
| L2 | Governance Pipeline Conformance |
| L3 | Deterministic Governance |
| L4 | Human Review, Execution Authorization & Commit Boundary |
| L5 | Multitenant & Governance Domain Isolation |

Implementations MAY implement functionality beyond a claimed profile. Additional functionality SHALL NOT invalidate a conformance claim provided that all mandatory requirements remain satisfied.

---

## 3.1 Level L1 — Interface & Schema Conformance

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

## 3.2 Level L2 — Governance Pipeline Conformance

L2 verifies correct execution of the normative governance pipeline.

An implementation claiming L2 conformance SHALL:

- Execute Proposal Qualification.
- Evaluate the Governance Decision Function.
- Apply Policy Evaluation Contract (PEC) processing where required.
- Produce deterministic Governance Decision Results.
- Produce Governance Evidence for governance-significant processing.
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
- Derive Canonical State from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered ledger can be deterministically reproduced.
- Support deterministic replay.
- Preserve Governance Evidence sufficient for deterministic replay.
- Preserve ordered governance history.
- Detect non-deterministic governance behavior.

The ordered Append-Only Governance Ledger SHALL be authoritative for Canonical State derivation.

Timestamp ordering SHALL NOT determine Canonical State.

Materialized state views MAY be used for performance provided they remain reproducible from the ordered ledger.

---

## 3.4 Level L4 — Human Review, Execution Authorization & Commit Boundary

L4 verifies governance controls that directly authorize execution.

An implementation claiming L4 conformance SHALL:

- Support Human Review where required by governance policy.
- Validate Human Review artifacts.
- Enforce Human Review completion before execution authorization.
- Produce Execution Authorization artifacts.
- Enforce Commit Boundary processing.
- Prevent execution without valid authorization.
- Record Human Review, Execution Authorization, Commit Boundary processing, and associated Governance Evidence in the Append-Only Governance Ledger.
- Reject attempts to bypass required governance controls.

Execution SHALL occur only after successful completion of the required governance pipeline.

---

## 3.5 Level L5 — Multitenant & Governance Domain Isolation

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

The authoritative source of all AGCP requirements is the normative specification suite.

Assertions SHALL be derived from the authoritative specifications and SHALL NOT introduce new normative requirements.

The authoritative traceability model is:

```
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
        ↓
Derived Assertion(s)
```

Assertions support implementation and certification activities but SHALL NOT supersede the authoritative CR → NS → TC mappings.

If a conflict exists between an assertion and a normative specification, the normative specification SHALL take precedence.

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
| HUMAN_REVIEW | Human Review processing |
| EXECUTION | Execution Authorization and Commit Boundary processing |
| EVIDENCE | Governance Evidence generation and validation |
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
- Human Review artifacts
- Execution Authorization artifacts
- Commit Boundary results
- Governance Evidence
- Append-Only Governance Ledger behavior
- Canonical State reconstruction
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
- Human Review processing
- Execution Authorization
- Commit Boundary processing
- Governance Evidence
- Append-Only Governance Ledger ordering
- Canonical State derivation

Deterministic replay SHALL reproduce the same Canonical State when evaluated using the ordered Append-Only Governance Ledger or a verifiable materialized state deterministically derived from that ledger.

Timestamp ordering SHALL NOT substitute for ledger sequence ordering.

---

## 4.8 Negative Assertions

Negative assertions verify that prohibited behavior does not occur.

Examples include:

- acceptance of malformed requests
- unauthorized execution
- bypass of Human Review
- invalid Execution Authorization
- invalid Commit Boundary processing
- invalid provenance
- cross-tenant access
- cross-domain access
- ledger modification
- Canonical State derivation from reordered ledger history
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

These assertions are derived from the authoritative Normative Statements (NS), Conformance Requirements (CR), and Test Cases (TC).

This specification does not introduce an independent assertion identifier system. The authoritative conformance traceability model remains:

```
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

---

## 5.1 Interface & Schema Conformance

An implementation SHALL:

- Validate requests and responses against the published AGCP JSON Schemas.
- Reject malformed requests using the appropriate rejection codes.
- Produce structured error responses conforming to the published ErrorResponse schema.
- Produce deterministic externally observable interface behavior.

---

## 5.2 Governance Pipeline Conformance

An implementation SHALL:

- Execute Proposal Qualification before Governance Decision evaluation.
- Execute Policy Evaluation Contract (PEC) processing where required.
- Evaluate constraints before invariants.
- Complete invariant evaluation before determining Human Review requirements.
- Complete Execution Authorization before Commit Boundary processing.
- Produce Governance Evidence for governance-significant processing.
- Record governance-significant events in the Append-Only Governance Ledger.

---

## 5.3 Deterministic Governance

An implementation SHALL:

- Produce identical governance outcomes for identical authoritative inputs.
- Produce deterministic Governance Decision Results.
- Reject non-deterministic governance behavior.
- Derive Canonical State from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered ledger can be deterministically reproduced.
- Preserve deterministic replay capability.

---

## 5.4 Human Review

Where Human Review is required by governance policy, an implementation SHALL:

- Validate Human Review artifacts.
- Enforce required approvals.
- Reject expired or invalid review artifacts.
- Prevent Execution Authorization until required Human Review has successfully completed.

---

## 5.5 Execution Authorization & Commit Boundary

An implementation SHALL:

- Prevent execution without valid Execution Authorization.
- Validate Commit Boundary requirements.
- Produce Governance Evidence for Commit Boundary processing.
- Record successful Commit Boundary processing in the Append-Only Governance Ledger.

---

## 5.6 Governance Evidence & Ledger

An implementation SHALL:

- Produce Governance Evidence conforming to the published schema.
- Preserve immutable Governance Evidence.
- Preserve an Append-Only Governance Ledger.
- Preserve deterministic ledger ordering.
- Use ledger sequence, not timestamps, as the authoritative ordering for Canonical State derivation.
- Support deterministic Canonical State reconstruction from the ordered ledger.

---

## 5.7 Multitenant & Governance Domain Isolation

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

The complete normative traceability model is defined by the Requirements Traceability Matrix (RTM), Normative Statements, and Conformance Test Suite.

---

## 6.1 Positive Tests

Positive tests SHALL verify:

- successful Proposal Qualification
- successful Governance Decision evaluation
- successful Human Review processing where required
- successful Execution Authorization
- successful Commit Boundary processing
- successful Governance Evidence generation
- successful Append-Only Governance Ledger recording
- successful Canonical State derivation

---

## 6.2 Negative Tests

Negative tests SHALL verify rejection of:

- malformed requests
- invalid provenance
- invalid tenant state
- governance policy rejection
- failed Human Review
- unauthorized execution
- invalid Commit Boundary processing
- unauthorized cross-tenant access
- unauthorized Governance Domain access
- invalid Governance Evidence
- ledger integrity violations
- invalid Canonical State reconstruction

---

## 6.3 Deterministic Governance Tests (L3+)

Deterministic governance testing SHALL verify that identical authoritative inputs produce identical externally observable governance behavior.

Testing SHALL include:

1. Submission of an identical Proposal using identical authoritative inputs.
2. Recording of the Governance Decision Result, Governance Evidence, Append-Only Governance Ledger entries, and Canonical State.
3. Repetition of the evaluation.
4. Comparison of the externally observable governance results.

Canonical State SHALL be reproducible from the ordered Append-Only Governance Ledger, or from a verifiable materialized state deterministically derived from that ledger.

Timestamp ordering SHALL NOT substitute for ledger sequence ordering.

---

## 6.4 Canonical State Reconstruction Tests (L3+)

Testing SHALL verify:

1. Deterministic reconstruction using the ordered Append-Only Governance Ledger.
2. Deterministic reconstruction using a verifiable materialized state, where implemented.
3. Rejection or non-equivalence of reordered ledger histories.
4. Preservation of Governance Evidence integrity throughout reconstruction.

---

## 6.5 Multitenant Isolation Tests (L5)

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
- Failure of Canonical State reconstruction
- Failure of Governance Evidence validation
- Failure of Append-Only Governance Ledger validation
- Failure of Human Review enforcement
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

- Core Specification
- HTTP Interface Specification
- JSON Schemas
- Security Specification
- Human Review Specification
- Provenance Wire Format Specification
- Append-Only Governance Ledger Specification
- Error Mapping Specification
- Published registries
- Requirements Traceability Matrix (RTM)
- Official Conformance Test Suite

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
- Human Review processing
- Execution Authorization
- Commit Boundary enforcement
- Governance Evidence production
- Append-Only Governance Ledger integrity
- Canonical State derivation
- Deterministic replay
- Tenant isolation
- Governance Domain isolation where applicable

The authoritative conformance traceability model is:

```
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

Conformance SHALL be demonstrated using the official AGCP Requirements Traceability Matrix (RTM) and Conformance Test Suite.

Implementations MAY exceed the minimum requirements defined by this specification, provided all mandatory requirements applicable to the claimed conformance profile are satisfied.
