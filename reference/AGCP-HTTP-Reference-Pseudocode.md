# AGCP HTTP Interface Deterministic Reference Pseudocode

Version: 0.9.0  
Status: Informational (Reference Implementation Guidance)

This document provides deterministic reference pseudocode for the AGCP HTTP interface.  
Implementations MAY use concurrent execution internally, but MUST produce the same externally observable outcomes defined here.

This document is not normative. The normative requirements are defined in:

- AGCP Core Specification
- AGCP HTTP Interface Specification
- AGCP Conformance Specification
- AGCP Error Mapping Table
- AGCP Provenance Wire Format Specification

---

# 0. Core Data Model Assumptions

## 0.1 Canonical Externally Observable Action States

Externally observable states are:

- REJECTED (terminal)
- PENDING_HITL
- AUTHORIZED
- EXECUTED (terminal)

`SUBMITTED` is transient and MUST NOT be returned by canonical retrieval.

---

## 0.2 Ledger is the Source of Truth

Ledger entries are append-only.

Lifecycle state is derived exclusively from ledger history.

Any cached state MUST be treated as a derived view.

---

## 0.3 Tenant Scoping

All operations are tenant scoped.

Cross-tenant access MUST be rejected.

---

# 1. Types and Constants

## 1.1 Enumerations

### ActionState

```
REJECTED
PENDING_HITL
AUTHORIZED
EXECUTED
```

### PecDecision

```
ACCEPT
REJECT
PENDING_HITL
```

### LedgerStage

```
SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
TENANT_STATE_VALIDATION
POLICY_RESOLUTION
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
DECISION
EXECUTION_AUTHORIZED
EXECUTION_COMMITTED
```

### RejectionCode

```
SCHEMA_VALIDATION_FAILED
PROVENANCE_INVALID
TENANT_STATE_INVALID
TENANT_SCOPE_VIOLATION
POLICY_NOT_FOUND
IDEMPOTENCY_CONFLICT
ACTION_NOT_AUTHORIZED
COSIGN_INVALID
COSIGN_EXPIRED
INTERNAL_ERROR
```

---

## 1.2 Platform vs PEC Stages

### Platform Stages

```
SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
TENANT_STATE_VALIDATION
POLICY_RESOLUTION
Ledger append operations
```

### PEC Engine Stages

```
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
Decision computation
```

The platform records decision results in the ledger.

---

# 2. Storage Interfaces

These interfaces are abstract. Implementations may use databases or other persistent stores.

---

## 2.1 Idempotency Store

Used for action submission.

### IdempotencyRecord

```
tenant_id
idempotency_key
request_fingerprint
action_id
created_at
```

### Interface

```
idempotency_get(tenant_id, idempotency_key)
idempotency_put_if_absent(record)
```

---

## 2.2 Action Registry

### ActionRecord

```
tenant_id
action_id
```

### Interface

```
action_exists(tenant_id, action_id)
action_create_if_absent(tenant_id, action_id)
```

---

## 2.3 Ledger Store

### LedgerEntry

```
tenant_id
action_id
stage
timestamp
data
ref
```

### Interface

```
ledger_append(entry)
ledger_list(tenant_id, action_id)
```

Ledger entries MUST be returned ordered by append sequence.

---

# 3. Deterministic Helper Functions

## 3.1 Canonical Request Fingerprint

```
function canonical_fingerprint(json_obj):

    canonical = canonicalize_json(json_obj)
    return sha256_hex(canonical)
```

Canonicalization MUST:

- recursively sort object keys
- normalize whitespace
- encode UTF-8
- produce stable JSON output

---

## 3.2 Tenant State Check

```
function require_tenant_active(tenant_id):

    state = tenant_get_state(tenant_id)

    if state != "ACTIVE":
        return error_response(403, TENANT_STATE_INVALID)

    return OK
```

---

## 3.3 Tenant Scope Check

```
function require_same_tenant(request_tenant, resource_tenant):

    if request_tenant != resource_tenant:
        return error_response(403, TENANT_SCOPE_VIOLATION)

    return OK
```

---

## 3.4 Derive Lifecycle State From Ledger

Lifecycle state MUST be derived solely from ledger history.

```
function derive_action_view_from_ledger(entries):

    if exists_stage(entries, EXECUTION_COMMITTED):
        return EXECUTED

    if exists_stage(entries, EXECUTION_AUTHORIZED):
        return AUTHORIZED

    decision = latest_decision(entries)

    if decision == REJECT:
        return REJECTED

    if decision == PENDING_HITL:
        return PENDING_HITL

    if decision == ACCEPT:
        return AUTHORIZED

    return SUBMITTED_TRANSIENT
```

`SUBMITTED_TRANSIENT` MUST NOT be returned by canonical retrieval.

---

# 4. Deterministic Evaluation Pipeline

The evaluation pipeline order MUST be fixed.

```
SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
TENANT_STATE_VALIDATION
POLICY_RESOLUTION
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
DECISION
```

This ordering MUST NOT change.

---

# 5. Endpoint Reference Pseudocode

## 5.1 POST /agcp/v1/actions/submit

High-level flow:

```
validate idempotency key

check idempotency store

append SCHEMA_VALIDATION

append PROVENANCE_VERIFICATION

append TENANT_STATE_VALIDATION

append POLICY_RESOLUTION

evaluate PEC constraints

evaluate PEC invariants

evaluate HITL requirements

append DECISION

if ACCEPT
    append EXECUTION_AUTHORIZED
```

Submission MUST enforce idempotency.

A repeated request with the same key and different payload MUST return:

```
409 IDEMPOTENCY_CONFLICT
```

---

## 5.2 GET /agcp/v1/actions/{action_id}

```
verify tenant scope

derive state from ledger

if state == SUBMITTED_TRANSIENT
    return 404

return action view
```

SUBMITTED state MUST NOT be externally observable.

---

## 5.3 POST /agcp/v1/actions/{action_id}/cosign

Cosign is only valid in `PENDING_HITL`.

```
verify tenant scope

verify token signature

verify token binding to tenant and action

verify token expiry

check replay protection
```

If quorum satisfied:

```
append EXECUTION_AUTHORIZED
```

---

## 5.4 POST /agcp/v1/executions/commit

Commit requires `AUTHORIZED` state.

```
verify tenant ACTIVE

verify action state AUTHORIZED

verify ledger_authorization_ref

verify provenance

append EXECUTION_COMMITTED
```

This transition is terminal.

---

# 6. Deterministic HITL Quorum Function

```
function compute_quorum(required_roles, cosigns):

    for role in required_roles:
        if no cosign satisfies role:
            return false

    return true
```

Each required role must be satisfied by at least one valid cosign.

---

# 7. Determinism Requirements

An implementation is deterministic if it satisfies all of the following:

1. Fixed evaluation stage ordering is enforced.
2. State is derived solely from ledger history.
3. `SUBMITTED` state is never externally returned.
4. Submit idempotency is strictly enforced.
5. Cosign is allowed only in `PENDING_HITL`.
6. Commit is allowed only in `AUTHORIZED`.
7. Terminal states reject further transitions.

---

# 8. Relationship to Normative Specifications

This document illustrates reference behavior.

Normative requirements are defined in:

- AGCP Core Specification
- AGCP HTTP Interface Specification
- AGCP Conformance Specification
- AGCP Error Mapping Table
- AGCP Provenance Wire Format Specification

Implementations MUST follow the normative specifications even if internal architecture differs.
