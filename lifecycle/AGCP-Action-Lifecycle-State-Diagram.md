# AGCP Formal Action Lifecycle State Transition Specification

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  

---

# 1. State Set and Visibility

## 1.1 Lifecycle States (Normative)

An action SHALL exist in exactly one of the following states at any given time:

- SUBMITTED (transient)
- REJECTED (terminal)
- PENDING_HITL
- AUTHORIZED
- EXECUTED (terminal)

No additional lifecycle states SHALL be introduced within the same **MAJOR** version.

---

## 1.2 External Observability (Normative)

`SUBMITTED` is transient and **MUST NOT** be externally observable via retrieval endpoints.

**Implementer Guidance**

`POST /actions/submit` SHOULD return the post-decision state:

- AUTHORIZED
- PENDING_HITL
- REJECTED

rather than exposing an intermediate in-progress state.

If internal workflow statuses are used, they MUST NOT be returned by canonical retrieval endpoints.

---

# 2. Deterministic Evaluation Pipeline

## 2.1 Mandatory Ordering (Normative)

On submission, the implementation **MUST** enforce the following ordering:

1. Schema validation *(outside PEC)*
2. Provenance verification *(outside PEC)*
3. Tenant state validation *(outside PEC)*
4. Policy resolution *(outside PEC)*
5. Constraint evaluation
6. Invariant evaluation
7. HITL evaluation
8. Decision computation
9. Ledger append *(outside PEC)*

Additional ordering rules:

- Constraint evaluation **MUST precede** invariant evaluation.
- HITL evaluation **MUST occur after** invariant evaluation.

---

# 3. Formal Transition Diagram

## 3.1 Permitted Transitions Only (Normative)

The following transitions are permitted:

```
SUBMITTED -> REJECTED
SUBMITTED -> PENDING_HITL
SUBMITTED -> AUTHORIZED
PENDING_HITL -> AUTHORIZED
PENDING_HITL -> REJECTED
AUTHORIZED -> EXECUTED
```

No other transitions are permitted.

---

## 3.2 ASCII State Diagram (Normative)

```
             (PEC decision = REJECT)

          +---------------------------+

          |                           v

     +---------+                 +----------+

     |SUBMITTED| --------------> | REJECTED |

     +---------+                 +----------+

          |

          | (PEC decision = PENDING_HITL)

          v

   +-------------+      (valid quorum)     +------------+

   |PENDING_HITL | ----------------------> | AUTHORIZED |

   +-------------+                         +------------+

          |                                     |

          | (expiration / governance cancel)    | (successful execution commit)

          v                                     v

     +----------+                           +----------+

     | REJECTED |                           | EXECUTED |

     +----------+                           +----------+
```

---

# 4. Transition Rules With Guards and Effects

## 4.1 SUBMITTED (Transient)

**Characteristics**

- Accepted for evaluation
- Validation complete through policy resolution
- PEC evaluation in progress or complete
- Decision not finalized in ledger
- Not externally observable

### SUBMITTED -> REJECTED

**Trigger / Guard**

Decision computed as `REJECT`.

Examples:

- Hard invariant failure
- Constraint failure without valid exception
- Invalid cosign token
- Execution attempt without authorization

---

### SUBMITTED -> PENDING_HITL

**Trigger / Guard**

```
PEC decision = PENDING_HITL
```

---

### SUBMITTED -> AUTHORIZED

**Trigger / Guard**

```
PEC decision = ACCEPT
```

---

## 4.2 PENDING_HITL

Meaning: Human approval required prior to authorization.

**Properties**

- `required_cosign_roles` MUST be defined
- Cosign tokens MAY be accepted
- Execution commit MUST be rejected while pending

---

### PENDING_HITL -> AUTHORIZED

**Trigger**

Valid quorum satisfaction.

**HTTP Alignment**

```
POST /agcp/v1/actions/{action_id}/cosign
```

Upon quorum satisfaction the action transitions to **AUTHORIZED**.

---

### PENDING_HITL -> REJECTED

**Trigger**

- HITL expiration
- Governance cancellation

---

## 4.3 AUTHORIZED

**Entry Conditions**

- PEC decision = ACCEPT  
OR
- HITL quorum satisfied

**Properties**

- `ledger_authorization_ref` MUST exist
- Execution commit MAY be accepted
- Idempotency integrity MUST be preserved

---

### AUTHORIZED -> EXECUTED

**Trigger**

Successful execution commit.

**Execution Gating Requirements**

Execution commit MUST verify:

- action state = `AUTHORIZED`
- `ledger_authorization_ref` matches
- tenant state = `ACTIVE`

**HTTP Alignment**

```
POST /agcp/v1/executions/commit
```

If validation fails:

```
ACTION_NOT_AUTHORIZED
```

---

## 4.4 EXECUTED (Terminal)

Meaning:

- Execution commit recorded
- Execution result appended to ledger
- Immutable state
- Further commits rejected

---

## 4.5 REJECTED (Terminal)

Properties:

- `rejection_code` MUST be present
- Execution commit MUST be rejected
- No further transitions permitted

---

# 5. Decision-to-State Mapping and Ledger Stage Alignment

## 5.1 PEC Decision Mapping (Normative)

PEC decision output SHALL map to lifecycle state as follows:

```
REJECT        -> REJECTED
PENDING_HITL  -> PENDING_HITL
ACCEPT        -> AUTHORIZED
```

This mapping **MUST occur prior to ledger append**.

---

## 5.2 Ledger Stage Alignment (Normative)

LedgerEntry.stage values SHALL align to lifecycle transitions.

### Evaluation Stages

```
SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
POLICY_RESOLUTION
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
DECISION
```

### Authorization Stage

```
EXECUTION_AUTHORIZED
```

### Commit Stage

```
EXECUTION_COMMITTED
```

Ledger properties:

- append-only
- tenant-scoped
- immutable

Lifecycle state SHALL be derivable from ledger history.

**Implementer Guidance**

State SHOULD be treated as a **derived view over the ledger stream**, rather than stored mutable state.

---

# 6. Tenant-State Interaction (Execution Gating)

## 6.1 Tenant Constraints (Normative)

Actions may only be submitted and executed when tenant state is:

```
ACTIVE
```

### Tenant State Rules

| Tenant State | Submission | Execution | Ledger Read |
|---------------|------------|-----------|-------------|
| PROVISIONED | REJECT | REJECT | Allowed |
| ACTIVE | Allowed | Allowed | Allowed |
| SUSPENDED | REJECT | REJECT | Allowed |
| DECOMMISSIONED | REJECT | REJECT | Allowed |

Ledger **MUST NOT** be deleted for decommissioned tenants.

---

**Implementer Guidance**

Tenant state SHOULD be treated as an **orthogonal guard** on:

- `submit`
- `executions/commit`

Do **not** introduce extra lifecycle states such as:

```
BLOCKED_BY_TENANT
```

Instead return an appropriate rejection code.

---

# 7. Replay Protection and Idempotency

## 7.1 Idempotency on Submit (Normative)

If the same `idempotency_key` is submitted:

| Condition | Result |
|----------|--------|
| Same payload | Existing lifecycle state returned |
| Different payload | `IDEMPOTENCY_CONFLICT` |

**HTTP Alignment**

```
HTTP 409
IDEMPOTENCY_CONFLICT
```

---

## 7.2 Replay After Terminal States

- Cosign token replay MUST NOT alter state after `EXECUTED`.
- Replay of execution commit MUST be rejected.

---

# 8. Minimal Implementer Checklist

Implementations MUST ensure:

- Mandatory evaluation ordering is enforced
- `SUBMITTED` is never returned by canonical retrieval endpoints
- Only permitted lifecycle transitions are implemented
- Execution commits are gated by:
  - AUTHORIZED state
  - ledger_authorization_ref match
  - tenant ACTIVE state
- Lifecycle state is derivable from the ledger
- Idempotency rules are strictly enforced
