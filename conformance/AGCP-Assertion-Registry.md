# AGCP Assertion Registry

Version: 0.9.0  
Status: Normative (Index)  
Canonical Source: `/conformance/assertions.json`

---

# 1. Purpose

This document provides a human-readable index of normative assertions used in the AGCP conformance framework.

Assertions define **testable behavioral guarantees** that implementations must satisfy in order to claim AGCP conformance.

The authoritative machine-readable assertion registry is located at:


/conformance/assertions.json


Assertions are enforced by the conformance harness defined in:


/conformance/AGCP Conformance Harness Spec.yml


Traceability between tests, requirements, and assertions is defined in:


/conformance/test-mapping.json


---

# 2. Assertion Model

AGCP conformance is verified through the following traceability chain:


Specification
↓
Assertion
↓
Requirement
↓
Conformance Test


Assertions represent **normative behavioral invariants** derived from the AGCP specifications.

Implementations claiming AGCP conformance **MUST satisfy all assertions referenced by the conformance test suite.**

---

# 3. Assertion Registry

## Core Behavioral Assertions

| Assertion ID | Description |
|--------------|-------------|
| A-ORDERING | Ledger stage entries MUST be appended in deterministic evaluation order: constraints → invariants → HITL. |
| A-DERIVATION | Returned action state MUST equal the lifecycle state derived from ordered ledger history. |
| A-STATE-NO-SUBMITTED | Canonical API responses MUST NOT expose the SUBMITTED state or any transient submission state. |
| A-COMMIT-GATING | Execution commit MUST only succeed when the action lifecycle state is AUTHORIZED and the ledger_authorization_ref matches the authorization reference recorded in the ledger. |
| A-COSIGN-GATING | Cosign operations MUST only be valid when the action lifecycle state is PENDING_HITL. |
| A-TENANT-ACTIVE-GATING | Operations that require tenant participation MUST reject requests when the tenant state is not ACTIVE. |
| A-IDEMPOTENCY-NO-MUTATION | Idempotent request replays MUST NOT mutate ledger state or append new stage entries. |
| A-TERMINAL-NO-TRANSITION | Terminal lifecycle states MUST reject further transitions or execution attempts. |

---

# 4. Conformance Enforcement

Assertions are enforced through the AGCP Conformance Harness.

Each conformance test references one or more requirements, which in turn map to assertions.

Example traceability:


Test: TV-COM-001
↓
Requirement: REQ-COMMIT-APPENDS-COMMITTED
↓
Assertion: A-COMMIT-GATING


An implementation fails conformance if any assertion is violated.

---

# 5. Assertion Scope

Assertions enforce guarantees across the following AGCP specification domains:

- Core lifecycle semantics
- Deterministic evaluation ordering
- Ledger derivability
- HITL (Human-in-the-Loop) enforcement
- Commit authorization gating
- Tenant isolation and multitenant safety
- Idempotency guarantees
- Terminal state safety

Assertions do not define API syntax or schema structure; those are defined in the HTTP Interface and Schema specifications.

---

# 6. Relationship to Requirements

Requirements represent **testable conditions derived from assertions**.

Requirements are defined in the conformance mapping layer and are associated with specific tests.

Example:


Assertion: A-DERIVATION
Requirement: REQ-STATE-DERIVED-FROM-LEDGER
Tests:
TV-COS-001
TV-COM-001
TV-XTEN-001


---

# 7. Canonical Registry

The authoritative assertion definitions are stored in:


/conformance/assertions.json


The JSON registry includes:

- Assertion identifiers
- Normative statements
- Source specification references
- Endpoint applicability
- Associated test identifiers

The Markdown registry exists solely for **human-readable review and specification documentation.**

---

# 8. Change Control

Assertion identifiers are **stable across specification patch releases**.

Rules:

- Assertion IDs MUST NOT be renumbered once published.
- Deprecated assertions MUST remain in the registry and be marked deprecated.
- New assertions MUST use new identifiers.

This stability ensures long-term traceability for conformance testing.

---

# 9. Conformance Claim

An implementation may claim **AGCP Conformance** only if:

1. All applicable conformance tests pass.
2. No registered assertion is violated.
3. Behavior is consistent with the normative specifications.

---

# 10. Notes for Reviewers

During public review:

- Assertions provide the fastest way to evaluate whether the specification guarantees deterministic behavior.
- Reviewers may propose changes to assertions by referencing the Assertion ID.
- Issues SHOULD reference the assertion identifier and the affected specification section.

Example issue reference:


Assertion: A-ORDERING
Spec: Core Deterministic Evaluation Pipeline
Proposed change: Clarify ordering requirement for constraint evaluation.


---

# 11. Future Extensions

Future versions of AGCP may introduce additional assertion domains including:

- Distributed replay verification
- Ledger consistency validation
- Multi-ledger federation safety
- Deterministic replay conformance tiers

These assertions will be added to the canonical JSON registry while maintaining identifier stability.

---
