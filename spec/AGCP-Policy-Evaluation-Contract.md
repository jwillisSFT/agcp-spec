# AGCP Policy Evaluation Contract (PEC) Specification v0.9.0

Status: Normative  
Version: 0.9.0  
Series: AGCP Core  
Applies To: All AGCP-conformant implementations

---

# 1. Purpose

The Policy Evaluation Contract (PEC) defines the mandatory, deterministic interface by which an AGCP implementation evaluates:

- Constraints
- Invariants
- Human-in-the-loop (HITL) triggers
- Final governance decisions

PEC ensures:

- Deterministic behavior
- Engine neutrality
- Multitenant safety
- Conformance testability
- Policy/runtime decoupling

PEC does not mandate a policy language or runtime engine.

---

# 2. Design Principles

PEC is designed to guarantee:

- Determinism
- Side-effect freedom
- Isolation
- Explicit ordering
- Registry compliance
- Testability via black-box conformance

---

# 3. Terminology

## 3.1 PEC

Policy Evaluation Contract.

## 3.2 PEM

Policy Evaluation Module — a tenant-scoped implementation that satisfies PEC.

## 3.3 PEC Input

Canonical input object passed to the PEM.

## 3.4 PEC Outputs

Structured output objects returned by evaluation functions.

---

# 4. Required Evaluation Model

An AGCP implementation MUST support a tenant-scoped PEM that provides the following logical evaluation stages:

- Constraint evaluation
- Invariant evaluation
- HITL evaluation
- Decision computation

Implementations MAY internally combine these stages, but observable outputs MUST reflect the defined ordering.

---

# 5. Evaluation Ordering (Mandatory)

The following order MUST be enforced:

1. Schema validation (outside PEC)
2. Provenance verification (outside PEC)
3. Tenant state validation (outside PEC)
4. Policy resolution (outside PEC)
5. Constraint evaluation
6. Invariant evaluation
7. HITL evaluation
8. Decision computation
9. Ledger append (outside PEC)

Constraint evaluation MUST precede invariant evaluation.  
HITL evaluation MUST occur after invariant evaluation.

Tenant state validation SHALL occur prior to invocation of the Policy Evaluation Module (PEM).

An implementation MUST verify that the tenant state permits action submission before invoking constraint evaluation, invariant evaluation, or HITL evaluation within PEC.

Tenant state validation is outside the scope of PEC and is part of the governance control plane validation pipeline defined in the Core Specification.

---

# 6. PEC Input Object (Normative)

The PEC input object MUST contain:

- tenant_id (string)
- action_envelope (object)
- resolved_policies (array)
- resolved_constraints (array)
- resolved_invariants (array)
- resolved_exceptions (array)
- state_snapshot (object)
- registries (object)
- request_context (object, optional)

---

## 6.1 Determinism Restrictions

PEC input MUST NOT include:

- Current system time (beyond `action_envelope.timestamp`)
- Random values
- Network-derived values
- Mutable global state
- Environment variables
- Non-repeatable data

If nondeterministic inputs are detected, the implementation MUST reject policy activation with:


POLICY_MODULE_NONDETERMINISTIC


---

# 7. Constraint Evaluation Stage

The PEM MUST evaluate each constraint in `resolved_constraints`.

Each evaluation result MUST include:

- constraint_id
- type
- outcome (`PASS | FAIL | NOT_APPLICABLE`)
- reason

Unknown constraint types MUST result in `FAIL` unless explicitly permitted via an active exception.

Constraint failures MUST be recorded.

---

# 8. Invariant Evaluation Stage

The PEM MUST evaluate each invariant in `resolved_invariants`.

Each evaluation result MUST include:

- invariant_id
- invariant_type
- enforcement_level (`Hard | Soft`)
- outcome (`PASS | FAIL`)
- reason

If any Hard invariant produces `FAIL`, the final decision MUST be `REJECT`.

Soft invariant failures MUST be recorded but MAY allow continuation.

---

# 9. HITL Evaluation Stage

The PEM MUST evaluate HITL requirements.

Output MUST include:

- required (boolean)
- required_cosign_roles (array of strings)
- reason

If `required` is true and quorum not satisfied, final decision MUST be `PENDING_HITL`.

---

# 10. Decision Computation Stage

The final decision output MUST include:

- decision (`ACCEPT | REJECT | PENDING_HITL`)
- rejection_code (string or null)
- failed_constraints (array)
- violated_invariants (array)
- required_cosign_roles (array)

Rules:

- If `REJECT` → `rejection_code` MUST be present.
- If `ACCEPT` or `PENDING_HITL` → `rejection_code` MUST be null.
- Hard invariant violations MUST cause `REJECT`.
- Constraint failures MUST cause `REJECT` unless valid exception applies.

---

# 11. Determinism Requirements

Given identical:

- PEC input
- Registry state
- Policy module version
- Tenant state

The PEM MUST produce identical:

- Constraint outputs
- Invariant outputs
- HITL outputs
- Decision outputs

Determinism is REQUIRED for conformance.

Replay tests MUST succeed under the **L3 profile**.

---

# 12. Policy Module Validation

Before activation, a PEM MUST:

- Pass integrity validation
- Pass determinism validation (static or runtime)
- Produce outputs conforming to the PEC output contract

If output structure invalid → reject with:


POLICY_EVALUATION_OUTPUT_INVALID


If module unavailable → reject with:


POLICY_MODULE_UNAVAILABLE


---

# 13. Multitenant Safety

The PEM MUST operate strictly within the tenant scope.

PEC input MUST contain only tenant-scoped artifacts.

Cross-tenant references MUST be rejected prior to PEC evaluation.

---

# 14. Exception Handling

Resolved exceptions MAY modify constraint evaluation outcomes.

Exceptions MUST:

- Be tenant-scoped
- Be unexpired
- Be recorded in the decision basis

Expired exceptions MUST NOT be considered.

---

# 15. Output Validation

The AGCP implementation MUST validate PEC outputs before computing the final decision.

If required fields are missing → reject with:


POLICY_EVALUATION_OUTPUT_INVALID


---

# 16. Side-Effect Prohibition

The PEM MUST:

- Not perform network calls
- Not mutate external state
- Not write to disk
- Not alter tenant registry state
- Not alter the ledger

All side effects MUST occur **outside PEC** in the governance pipeline.

---

# 17. Performance Constraints

PEC evaluation MUST be bounded.

Infinite loops or unbounded recursion MUST cause module rejection.

---

# 18. Conformance Implications

An implementation claiming **L3 or higher** MUST demonstrate:

- Deterministic replay consistency
- Hard invariant enforcement
- Proper ordering
- Proper rejection code behavior

---

# 19. Non-Goals

PEC does not define:

- Policy language
- Runtime engine
- Bytecode format
- Deployment model
- Performance optimization

PEC defines **behavioral contract only**.

---

# 20. Versioning

Changes to PEC input/output contract require **MAJOR version increment**.

Additions of optional fields require **MINOR version increment**.

Clarifications require **PATCH increment**.

---

# 21. Security Considerations

PEM artifacts SHOULD be:

- Integrity verified
- Version controlled
- Cryptographically signed

Policy modules MUST NOT weaken multitenant isolation guarantees.

---

# 22. Summary

PEC ensures:

- Engine neutrality
- Deterministic governance
- Conformance testability
- Policy-runtime decoupling
- Multitenant safety

All AGCP implementations MUST satisfy this contract to claim **Core conformance**.
