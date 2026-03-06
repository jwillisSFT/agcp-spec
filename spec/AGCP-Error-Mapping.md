# AGCP Endpoint-Level Error Mapping Table

Version: 0.9.0  
Status: Normative  
Scope: Defines the required mapping between HTTP status codes, rejection codes, and ledger append behavior for AGCP endpoints. This document ensures deterministic and interoperable error handling across implementations.

---

# 1. Conformance Rules

Implementations MUST comply with the following rules.

1. Implementations MUST use the exact HTTP status codes and `rejection_code` values defined in this document.

2. If `ledger_append = YES`, a `DECISION` stage entry MUST be appended to the ledger unless explicitly stated otherwise.

3. If `ledger_append = NO`, no new ledger entry SHALL be created.

4. Cross-tenant handling MUST be consistent across all endpoints. Implementations MUST choose either:

- **Hide profile** (404)
- **Forbid profile** (403)

Once chosen, the strategy MUST be applied uniformly across the system.

---

# 2. POST /agcp/v1/actions/submit

| Failure Path | HTTP Status | rejection_code | ledger_append |
|--------------|------------|----------------|---------------|
| Schema validation failure | 400 | SCHEMA_VALIDATION_FAILED | YES |
| Provenance invalid | 400 | PROVENANCE_INVALID | YES |
| Tenant not ACTIVE | 403 | TENANT_STATE_INVALID | YES |
| Policy not found | 400 | POLICY_NOT_FOUND | YES |
| Constraint failure | 200 | CONSTRAINT_FAIL | YES |
| Hard invariant failure | 200 | INVARIANT_HARD_FAIL | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- Constraint and invariant failures return **HTTP 200** because the request was valid but governance rejected execution.
- A `DECISION` ledger entry MUST record the rejection.

---

# 3. GET /agcp/v1/actions/{action_id}

| Failure Path | HTTP Status | rejection_code | ledger_append |
|--------------|------------|----------------|---------------|
| Action not found (or hidden cross-tenant) | 404 | ACTION_NOT_AUTHORIZED | NO |
| Cross-tenant (forbid profile) | 403 | TENANT_SCOPE_VIOLATION | NO |

Notes:

- Implementations using the hide profile SHOULD always return 404 for cross-tenant access.
- No ledger append occurs for retrieval failures.

---

# 4. POST /agcp/v1/actions/{action_id}/cosign

| Failure Path | HTTP Status | rejection_code | ledger_append |
|--------------|------------|----------------|---------------|
| Invalid signature | 409 | COSIGN_INVALID | NO |
| Expired token | 409 | COSIGN_EXPIRED | NO |
| Replay detected | 409 | COSIGN_INVALID | NO |
| Action not PENDING_HITL | 409 | ACTION_NOT_AUTHORIZED | NO |
| Cross-tenant (hide profile) | 404 | ACTION_NOT_AUTHORIZED | NO |
| Cross-tenant (forbid profile) | 403 | TENANT_SCOPE_VIOLATION | NO |

Notes:

- Cosign failures MUST NOT modify the ledger.
- HITL validation occurs before any ledger modification.

---

# 5. POST /agcp/v1/executions/commit

| Failure Path | HTTP Status | rejection_code | ledger_append |
|--------------|------------|----------------|---------------|
| Tenant not ACTIVE | 403 | TENANT_STATE_INVALID | NO |
| Action not AUTHORIZED | 409 | ACTION_NOT_AUTHORIZED | NO |
| Ledger authorization ref mismatch | 409 | ACTION_NOT_AUTHORIZED | NO |
| Replay commit after EXECUTED | 409 | ACTION_NOT_AUTHORIZED | NO |
| Cross-tenant (hide profile) | 404 | ACTION_NOT_AUTHORIZED | NO |
| Cross-tenant (forbid profile) | 403 | TENANT_SCOPE_VIOLATION | NO |

Notes:

- Commit failures MUST NOT append ledger entries.
- Only successful commits append `EXECUTION_COMMITTED`.

---

# 6. Success Path Notes

Successful operations produce the following behavior.

### Successful ACCEPT decision on submit

```
HTTP 200
state = AUTHORIZED
ledger_append = YES
```

### Successful PENDING_HITL decision

```
HTTP 200
state = PENDING_HITL
ledger_append = YES
```

### Successful commit

```
HTTP 200
state = EXECUTED
ledger_append = YES
stage = EXECUTION_COMMITTED
```

---

# 7. Versioning

Any change to:

- HTTP status codes
- rejection_code values
- ledger append behavior

constitutes a **breaking change**.

Breaking changes MUST require a **MAJOR version increment**.
