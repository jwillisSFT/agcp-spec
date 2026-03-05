# AGCP Implementer Annex to the Normative Transition Table

**Status:** Non-Normative (except where explicitly restating Core requirements)  
**Version:** 0.9.0  
**Series:** AGCP Core  

This annex provides implementation guidance for the AGCP lifecycle transition model.

It adds:

- Recommended internal guard-failure return codes
- Explicit separation of **Outside PEC vs Inside PEC responsibilities**
- A deterministic **derive lifecycle state from ledger** algorithm

---

# Annex A — Responsibility Boundaries (Outside PEC vs Inside PEC)

The AGCP evaluation model deliberately separates:

- **Outside PEC** — platform responsibility  
- **Inside PEC** — policy evaluation engine responsibility  

This separation **MUST remain stable** for determinism and auditability.

---

## A.1 Outside PEC (Platform-Enforced, Mandatory Ordering)

The following MUST occur **outside PEC** and **in this order**:

1. Schema validation  
2. Provenance verification  
3. Tenant state validation  
4. Policy resolution  
5. Ledger append (after decision mapping)

These are **platform invariants** and **MUST NOT** be delegated to PEC.

---

### Recommended Internal Failure Codes (Platform Layer)

| Step | Failure Condition | Recommended Internal Code | External `rejection_code` |
|-----|-----|-----|-----|
| Schema validation | JSON invalid / schema mismatch | `ERR_SCHEMA_INVALID` | `SCHEMA_VALIDATION_FAILED` |
| Provenance verification | Signature invalid / missing | `ERR_PROVENANCE_INVALID` | `PROVENANCE_INVALID` |
| Tenant state validation | Tenant not ACTIVE | `ERR_TENANT_STATE` | `TENANT_STATE_INVALID` |
| Policy resolution | Unknown policy reference | `ERR_POLICY_RESOLUTION` | `POLICY_NOT_FOUND` |
| Idempotency check | Same key + mismatched payload | `ERR_IDEMPOTENCY` | `IDEMPOTENCY_CONFLICT` |

**Guidance**

Internal codes SHOULD be more granular than registry-level rejection codes.  
External `rejection_code` values MUST conform to the rejection registry.

---

## A.2 Inside PEC (Deterministic Evaluation Engine)

PEC is responsible for:

- Constraint evaluation
- Invariant evaluation
- HITL evaluation
- Decision computation

PEC **MUST NOT**:

- Mutate tenant state
- Perform schema validation
- Append to ledger

---

### Recommended Internal PEC Failure Codes

| PEC Stage | Failure Type | Internal Code | Lifecycle Effect |
|---|---|---|---|
| Constraint | FAIL (no valid exception) | `PEC_CONSTRAINT_FAIL` | REJECT |
| Invariant (Hard) | FAIL | `PEC_HARD_INVARIANT_FAIL` | REJECT (mandatory) |
| Invariant (Soft) | FAIL | `PEC_SOFT_INVARIANT_FAIL` | No automatic REJECT |
| HITL | HITL required | `PEC_HITL_REQUIRED` | PENDING_HITL |
| Decision | ACCEPT | `PEC_ACCEPT` | AUTHORIZED |
| Decision | REJECT | `PEC_REJECT` | REJECTED |

**Critical Rule**

Any **Hard invariant FAIL MUST result in REJECT**.  
No override is permitted.

---

# Annex B — Guard Enforcement Matrix

This matrix clarifies which layer enforces which guard.

| Guard | Enforced Outside PEC | Enforced Inside PEC |
|---|---|---|
| Schema valid | YES | NO |
| Provenance valid | YES | NO |
| Tenant ACTIVE for submit | YES | NO |
| Constraint logic | NO | YES |
| Invariant logic | NO | YES |
| HITL quorum logic | Partially (token validity) | Yes (quorum decision) |
| Authorization reference match on commit | YES | NO |
| Tenant ACTIVE for execution | YES | NO |
| Idempotency integrity | YES | NO |

---

# Annex C — Derived Lifecycle State from Ledger

Lifecycle state **MUST be derivable from ledger history**.

---

## C.1 Stage Precedence Order

The following stage precedence SHALL determine lifecycle state:

```
EXECUTION_COMMITTED
EXECUTION_AUTHORIZED
DECISION
PEC_HITL
PEC_INVARIANTS
PEC_CONSTRAINTS
POLICY_RESOLUTION
PROVENANCE_VERIFICATION
SCHEMA_VALIDATION
```

Higher entries represent later lifecycle stages.

---

## C.2 Deterministic Derivation Algorithm

Given ledger entries ordered by append sequence:

### Step 1
If any entry:

```
stage == EXECUTION_COMMITTED
```

Return:

```
EXECUTED
```

---

### Step 2
If any entry:

```
stage == EXECUTION_AUTHORIZED
```

Return:

```
AUTHORIZED
```

---

### Step 3
Find latest `DECISION` stage.

If:

```
decision == REJECT
```

Return:

```
REJECTED
```

If:

```
decision == ACCEPT
```

Return:

```
AUTHORIZED
```

If:

```
decision == PENDING_HITL
```

Return:

```
PENDING_HITL
```

---

### Step 4
If no `DECISION` stage exists:

```
State = SUBMITTED
```

This state is **transient** and **MUST NOT be externally returned**.

---

### Step 5
If the ledger is empty:

```
Action does not exist
```

---

### Determinism Property

Lifecycle state **MUST be a pure function of ledger history**.

Mutable status fields **MUST NOT** be the source of truth.

Replaying the ledger **MUST yield identical lifecycle state**.

---

# Annex D — Terminal State Safety Rules

## REJECTED

Terminal state.

Properties:

- `rejection_code` MUST be present
- Execution commit MUST return `ACTION_NOT_AUTHORIZED`
- Cosign MUST return `ACTION_NOT_AUTHORIZED`

---

## EXECUTED

Terminal state.

Properties:

- Further execution commits MUST be rejected
- Cosign MUST be rejected
- Replay attempts MUST NOT alter the ledger

---

# Annex E — Invalid Transition Handling

If an operation attempts a **non-permitted transition**:

```
HTTP 409
rejection_code = ACTION_NOT_AUTHORIZED
```

If caused by **tenant state**:

```
HTTP 403
rejection_code = TENANT_STATE_INVALID
```

If caused by **cross-tenant scope**:

```
HTTP 403
rejection_code = TENANT_SCOPE_VIOLATION
```

---

# Annex F — Determinism Guarantees Checklist

An implementation is conformant only if:

- Evaluation ordering never varies
- Decision-to-state mapping occurs before ledger append
- Ledger is append-only
- Lifecycle state is derivable solely from ledger
- `SUBMITTED` is never externally observable
- Only permitted transitions exist
- Idempotency rules are enforced exactly
- Tenant state gating is enforced on submit and commit
