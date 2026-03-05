# AGCP Conformance Specification v0.9.0

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  
**Applies To:** All AGCP-conformant implementations

---

# Table of Contents

1. [Purpose](#1-purpose)  
2. [Conformance Model Overview](#2-conformance-model-overview)  
3. [Conformance Profiles](#3-conformance-profiles)  
   - [L1 — Schema & Envelope Validation](#31-level-l1--schema--envelope-validation)  
   - [L2 — Ordered Validation Pipeline](#32-level-l2--ordered-validation-pipeline)  
   - [L3 — Deterministic Governance](#33-level-l3--deterministic-governance)  
   - [L4 — HITL & Execution Gating](#34-level-l4--hitl--execution-gating)  
   - [L5 — Multitenant Isolation](#35-level-l5--multitenant-isolation)  
4. [Assertion Model](#4-assertion-model)  
5. [Required Assertions](#5-required-assertions-core-set)  
6. [Test Requirements](#6-test-requirements)  
7. [Conformance Claim Format](#7-conformance-claim-format)  
8. [Conformance Failure](#8-conformance-failure)  
9. [Certification Model (Optional)](#9-certification-model-optional)  
10. [Version Impact](#10-version-impact)  
11. [Non-Goals](#11-non-goals)  
12. [Summary](#12-summary)

---

# 1. Purpose

This specification defines:

- What it means to claim conformance to AGCP
- Conformance levels (L1–L5)
- Assertion model
- Test requirements
- Determinism validation requirements
- Multitenant validation requirements
- Negative test requirements
- Conformance declaration format

Conformance ensures that AGCP implementations:

- Enforce deterministic governance
- Preserve multitenant isolation
- Enforce invariant guarantees
- Maintain security posture
- Remain interoperable within a **MAJOR version**

---

# 2. Conformance Model Overview

AGCP conformance is defined via:

- Normative specification requirements (**MUST / SHALL**)
- Assertion identifiers (`AGCP-A-XXXX`)
- Conformance profiles (L1–L5)
- Required test coverage mapping
- Deterministic replay verification

An implementation **MUST satisfy all assertions in the claimed profile.**

---

# 3. Conformance Profiles

AGCP defines **five cumulative conformance levels.**

Each higher level **includes all lower levels.**

---

## 3.1 Level L1 — Schema & Envelope Validation

An **L1 implementation MUST:**

- Validate all request payloads against JSON schemas
- Enforce required fields
- Reject invalid schema submissions
- Return structured error responses
- Support `/meta` endpoint

**L1 does NOT require:**

- PEC enforcement
- Determinism validation
- HITL
- Execution gating
- Multitenancy

---

## 3.2 Level L2 — Ordered Validation Pipeline

An **L2 implementation MUST enforce validation ordering:**

1. Schema validation
2. Signature verification
3. Tenant state validation
4. Policy resolution
5. Constraint evaluation
6. Invariant evaluation
7. HITL evaluation
8. Decision computation
9. Ledger append

Additional requirements:

- Rejection codes MUST be enforced consistently
- Decisions MUST be recorded in the ledger

**L2 does NOT require deterministic replay validation.**

---

## 3.3 Level L3 — Deterministic Governance

An **L3 implementation MUST:**

- Enforce PEC contract
- Demonstrate deterministic replay
- Enforce Hard invariant rejection
- Validate policy module structure
- Reject nondeterministic policy modules

Replay testing **MUST confirm identical outputs for identical inputs.**

---

## 3.4 Level L4 — HITL & Execution Gating

An **L4 implementation MUST:**

- Enforce HITL quorum logic
- Validate cosign tokens
- Prevent execution without ledger authorization
- Record execution commits in ledger

Unauthorized execution **MUST be rejected.**

---

## 3.5 Level L5 — Multitenant Isolation

An **L5 implementation MUST:**

- Enforce strict tenant namespace isolation
- Reject cross-tenant artifact resolution
- Reject cross-tenant ledger access
- Support cross-tenant trust artifacts (if implemented)
- Pass cross-tenant negative tests
- Demonstrate per-tenant isolation behavior

Failure of any cross-tenant negative test **invalidates an L5 claim.**

---

# 4. Assertion Model

Each normative requirement is mapped to a unique assertion identifier.

Format:


AGCP-A-XXXX


Example:


AGCP-A-0001 — Schema validation MUST reject missing required fields.


Assertions are categorized by domain:

- SCHEMA
- SECURITY
- PEC
- HITL
- EXECUTION
- MULTITENANT
- REGISTRY
- LEDGER
- VERSIONING

---

# 5. Required Assertions (Core Set)

Below is the **minimal normative assertion baseline.**

---

## 5.1 Schema Assertions

**AGCP-A-0001**  
Implementation MUST validate JSON payloads against published schemas.

**AGCP-A-0002**  
Invalid schema MUST return `SCHEMA_INVALID`.

**AGCP-A-0003**  
Structured error response MUST conform to `ErrorResponse` schema.

---

## 5.2 Ordering Assertions

**AGCP-A-0101**  
Schema validation MUST precede signature verification.

**AGCP-A-0102**  
Constraint evaluation MUST precede invariant evaluation.

**AGCP-A-0103**  
Invariant evaluation MUST precede HITL evaluation.

**AGCP-A-0104**  
Decision MUST precede ledger append.

---

## 5.3 PEC Assertions

**AGCP-A-0201**  
PEC input MUST conform to required structure.

**AGCP-A-0202**  
PEC evaluation MUST be deterministic.

**AGCP-A-0203**  
Hard invariant failure MUST produce `REJECT`.

**AGCP-A-0204**  
Policy module output MUST conform to PEC output contract.

**AGCP-A-0205**  
Nondeterministic policy module MUST be rejected.

---

## 5.4 HITL Assertions

**AGCP-A-0301**  
Cosign token MUST bind to `tenant_id` and `action_id`.

**AGCP-A-0302**  
Expired cosign token MUST be rejected.

**AGCP-A-0303**  
Quorum logic MUST enforce `required_cosign_roles`.

---

## 5.5 Execution Assertions

**AGCP-A-0401**  
Execution commit MUST require authorized action state.

**AGCP-A-0402**  
Execution commit MUST validate ledger binding.

**AGCP-A-0403**  
Execution result MUST be appended to ledger.

---

## 5.6 Multitenant Assertions

**AGCP-A-0501**  
Cross-tenant artifact resolution MUST be rejected.

**AGCP-A-0502**  
Cross-tenant ledger access MUST be rejected.

**AGCP-A-0503**  
Cross-tenant execution commit MUST be rejected.

**AGCP-A-0504**  
Tenant state MUST restrict action submission appropriately.

---

## 5.7 Registry Assertions

**AGCP-A-0601**  
Unknown constraint type MUST be rejected.

**AGCP-A-0602**  
Unknown invariant type MUST be rejected.

**AGCP-A-0603**  
Rejection codes MUST exist in rejection registry.

---

# 6. Test Requirements

---

## 6.1 Positive Tests

Must validate:

- Valid action → `ACCEPT`
- Hard invariant failure → `REJECT`
- HITL required → `PENDING_HITL`
- Authorized execution → `COMMITTED`

---

## 6.2 Negative Tests

Must validate:

- Schema invalid payload
- Signature invalid
- Idempotency conflict
- Cross-tenant access attempt
- Invalid cosign token
- Expired cosign token
- Execution without authorization
- Unknown constraint type
- Unknown invariant type

---

## 6.3 Determinism Tests (L3+)

Procedure:

1. Submit `ActionEnvelope`
2. Capture `ValidationResult`
3. Reset environment state
4. Replay the same `ActionEnvelope`
5. Compare outputs

Outputs **MUST be identical.**

---

## 6.4 Cross-Tenant Isolation Tests (L5)

Procedure:

1. Create Tenant A and Tenant B
2. Attempt to reference B policy from A
3. Attempt to read B ledger from A
4. Attempt execution commit across tenants

All **MUST return `TENANT_SCOPE_VIOLATION`.**

---

# 7. Conformance Claim Format

An implementation claiming conformance **MUST publish:**

- Implementation name
- Implementation version
- Supported spec version
- Conformance level (L1–L5)
- Cryptographic profile(s)
- Test report reference
- Date of claim

Example:


AGCP Conformance Declaration
Implementation: ExampleEngine 1.2.0
Spec Version: 0.9
Conformance Level: L4
Crypto Profile: HYBRID
Test Suite Version: 0.9.0
Date: YYYY-MM-DD


---

# 8. Conformance Failure

An implementation **MUST NOT claim a profile level if:**

- Any required assertion fails
- Determinism test fails (L3+)
- Cross-tenant negative test fails (L5)
- Security requirements are not enforced

---

# 9. Certification Model (Optional)

AGCP **MAY support:**

- Self-attestation
- Community validation
- Formal certification authority

Certification processes are **out of scope for AGCP Core.**

---

# 10. Version Impact

Conformance assertions are stable within a **MAJOR version.**

- Changes to assertion semantics require a **MAJOR version increment**
- Additions of new assertions require a **MINOR version increment**

---

# 11. Non-Goals

This document does **not:**

- Define a specific test runner
- Mandate CI/CD tools
- Mandate certification authority
- Mandate runtime architecture

---

# 12. Summary

AGCP conformance ensures:

- Deterministic governance
- Proper evaluation ordering
- Hard invariant enforcement
- HITL integrity
- Execution gating security
- Multitenant isolation
- Registry discipline
- Version stability

An implementation **MUST satisfy all assertions for its claimed level.**
