/spec/AGCP-Core-v0.9.0.md

# AGCP Core Specification v0.9.0

Status: Normative  
Version: 0.9.0  
Series: AGCP Core  
License/IPR Mode: To be declared upon formal standards submission  

---

## Normative Language

The key words “MUST”, “MUST NOT”, “SHALL”, “SHALL NOT”, “SHOULD”, and “MAY” are to be interpreted as described in RFC 2119 and RFC 8174.

---

## 1. Introduction

The AI Governance Control Plane (AGCP) defines a domain-agnostic, multitenant governance control plane architecture for regulating AI-enabled and automated decision execution.

AGCP standardizes:

- Action submission envelopes  
- Policy evaluation contract (PEC)  
- Constraint and invariant enforcement  
- Human-in-the-loop (HITL) controls  
- Execution authorization gating  
- Multitenant isolation  
- Ledger integrity  
- Deterministic decisioning  
- Conformance validation  

AGCP does not mandate a specific implementation language or runtime.

---

## 2. Terminology

### 2.1 Tenant

A logically isolated governance namespace.

### 2.2 ActionEnvelope

A structured request submitted for governance validation.

### 2.3 Policy Evaluation Contract (PEC)

The required deterministic evaluation interface for constraints, invariants, and HITL logic.

### 2.4 Policy Evaluation Module (PEM)

A tenant-scoped implementation of the PEC.

### 2.5 Constraint

A conditional rule evaluated prior to execution authorization.

### 2.6 Invariant

A systemic rule that MUST hold regardless of policy flexibility.

### 2.7 HITL

Human-in-the-loop approval mechanism requiring cosignatures.

### 2.8 Ledger

An immutable record of governance decisions and execution authorization.

---

## 3. Architectural Model

AGCP enforces a deterministic validation pipeline:

1. Schema validation  
2. Provenance verification  
3. Tenant state verification  
4. Policy resolution  
5. PEC constraint evaluation  
6. PEC invariant evaluation  
7. PEC HITL evaluation  
8. Decision computation  
9. Ledger append  
10. Execution authorization (if applicable)

Evaluation ordering is mandatory and MUST NOT vary.

---

## 4. Multitenant Model

### 4.1 Tenant States

- PROVISIONED  
- ACTIVE  
- SUSPENDED  
- DECOMMISSIONED  

Actions MAY only be submitted and executed when tenant state is ACTIVE.

If tenant state transitions to DECOMMISSIONED:

- No further transitions permitted  
- Ledger remains readable  

---

### 4.2 Isolation Requirements

An implementation MUST ensure:

- No cross-tenant policy resolution  
- No cross-tenant constraint resolution  
- No cross-tenant invariant resolution  
- No cross-tenant exception resolution  
- No cross-tenant ledger access  
- No cross-tenant execution authorization  

Violation MUST result in `TENANT_SCOPE_VIOLATION`.

---

## 5. ActionEnvelope

Each ActionEnvelope MUST include:

- tenant_id  
- action_id  
- idempotency_key  
- timestamp  
- authority context  
- requested operation  
- target surface  
- provenance signature  

Schema details are defined in `/schemas/ActionEnvelope.json`.

---

## 6. Policy Evaluation Contract (PEC)

AGCP requires deterministic evaluation via PEC.

### 6.1 Required Entrypoints

A PEM MUST support:

```

evaluate_constraints(pec_input)
evaluate_invariants(pec_input, constraints_output)
evaluate_hitl(pec_input, constraints_output, invariants_output)
evaluate_decision(...)

```

---

### 6.2 PEC Input

PEC input MUST include:

- tenant_id  
- action_envelope  
- resolved_policies  
- resolved_constraints  
- resolved_invariants  
- resolved_exceptions  
- state_snapshot  
- registries  

PEC input MUST NOT include nondeterministic values (e.g., current system time beyond envelope timestamp).

---

### 6.3 Determinism Requirement

Given identical inputs and registry state, outputs MUST be identical.

Non-deterministic policy modules MUST be rejected with:

```
POLICY_MODULE_NONDETERMINISTIC
```

---

## 7. Constraints

Each Constraint evaluation produces:

- constraint_id  
- type  
- outcome (PASS | FAIL | NOT_APPLICABLE)  
- reason  

Unknown constraint types MUST result in rejection unless explicitly permitted via exception.

---

## 8. Invariants

Each Invariant evaluation produces:

- invariant_id  
- invariant_type  
- enforcement_level (Hard | Soft)  
- outcome  
- reason  

Hard invariant failure MUST result in REJECT.

---

## 9. Human-in-the-Loop (HITL)

HITL evaluation returns:

- required (boolean)  
- required_cosign_roles[]  
- reason  

Cosign tokens MUST:

- Bind to tenant_id  
- Bind to action_id  
- Be signed  
- Be unexpired  
- Be non-reusable  

Invalid tokens MUST result in rejection.

---

## 10. Decision Output

Decision object MUST include:

- decision (ACCEPT | REJECT | PENDING_HITL)  
- rejection_code (if REJECT)  
- failed_constraints[]  
- violated_invariants[]  
- required_cosign_roles[]

---

## 11. Determinism Requirement (Lifecycle)

Given identical:

- ActionEnvelope  
- Tenant state  
- Registry state  
- Policy module version  

Lifecycle state transitions MUST be identical.

Non-deterministic lifecycle behavior invalidates L3 conformance.

---

## 12. Execution Authorization

Execution commit MUST:

- Reference ledger authorization record  
- Verify tenant scope  
- Verify action state AUTHORIZED  
- Append execution result to ledger  

Unauthorized commit attempts MUST result in `ACTION_NOT_AUTHORIZED`.

---

## 13. Ledger Requirements

Ledger MUST:

- Be append-only  
- Be immutable  
- Preserve ordering  
- Be tenant-scoped  

Ledger entries MUST include:

- decision stage  
- constraint results  
- invariant results  
- hitl requirements  
- execution outcome (if applicable)

---

## 14. Security Requirements

### 14.1 Signature Verification

Envelope signatures MUST be verified prior to PEC evaluation.

### 14.2 Replay Protection

Duplicate `idempotency_key` with differing payload MUST be rejected.

### 14.3 Cross-Tenant Protection

All requests MUST be tenant-scoped.

### 14.4 Policy Module Integrity

Policy modules MUST be verifiable and version-controlled.

---

## 15. Conformance Profiles

AGCP defines five conformance levels:

- L1 — Schema & envelope validation  
- L2 — Validation ordering  
- L3 — Determinism & invariant enforcement  
- L4 — HITL & execution gating  
- L5 — Multitenant isolation  

All profiles require passing all mapped assertions.

---

## 16. Versioning

AGCP uses semantic versioning:

```

MAJOR.MINOR.PATCH

```

Breaking changes require MAJOR increment.  
Schemas and registries MUST align with release version.

---

## 17. Registry Governance

Registries define:

- Constraint types  
- Invariant types  
- Rejection codes  

Core namespace entries are managed via formal governance process.  
Vendor extensions MUST use vendor namespace.

---

## 18. Change Control

Changes MUST include:

- Impacted sections  
- Schema impact  
- Registry impact  
- Conformance impact  
- Security impact  
- Compatibility analysis  

---

## 19. Determinism & Ordering

The following ordering MUST be preserved:

1. Schema validation  
2. Provenance verification  
3. Tenant state verification  
4. Policy resolution  
5. Constraint evaluation  
6. Invariant evaluation  
7. HITL evaluation  
8. Decision computation  
9. Ledger append  

Deviation invalidates conformance.

---

## 20. Multitenant Operational Profile

Trust artifacts MAY allow limited cross-tenant operations.

Absent trust artifact, cross-tenant execution MUST be rejected.

Tenant deletion transitions to DECOMMISSIONED and preserves ledger history.

---

## 21. Interoperability Guarantees

Within a MAJOR version:

- Compatible MINOR versions MUST interoperate  
- Registry additions MUST NOT break prior artifacts  
- Conformance behavior MUST remain stable  

---

## 22. Release Requirements

An official release MUST include:

- Core spec  
- HTTP spec  
- PEC spec  
- Security profile  
- Multitenant profile  
- Versioning policy  
- Conformance clause  
- Schema bundle  
- Registry bundle  
- Assertion mapping  

---

## 23. Final Notes

AGCP is:

- Domain-agnostic  
- Vendor-neutral  
- Engine-neutral  
- Deterministic  
- Multitenant  

It defines behavioral guarantees, not implementation internals.
```


