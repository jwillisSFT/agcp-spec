# AGCP Normative Transition Table
*(Companion to the Action Lifecycle State Diagram)*

---

# Legend

**Event**  
An externally triggered operation (HTTP call) or an internal pipeline step.

**Guard**  
Condition(s) that MUST hold; otherwise the operation MUST be rejected.

**Ledger Stages**  
Required alignment points (stage names) used to derive and justify lifecycle state.

---

# A) Submission Pipeline → Post-Decision States

| Current State | Event | Guard (MUST) | Next State | Ledger Stage Requirements | Canonical HTTP Outcome / rejection_code |
|---|---|---|---|---|---|
| (none) | `POST /agcp/v1/actions/submit` | Perform mandatory ordering: schema, provenance, tenant state, policy resolution, PEC constraints, PEC invariants, PEC HITL, decision computation, ledger append | SUBMITTED is transient only | Ordering MUST NOT vary | Returns decision result (ACCEPT / REJECT / PENDING_HITL) |
| (none) | `POST /agcp/v1/actions/submit` | Same `idempotency_key` reused with differing payload | REJECTED (request rejected; existing action unaffected) | N/A | HTTP 409, `IDEMPOTENCY_CONFLICT` |
| SUBMITTED (transient) | Decision computed | `decision = REJECT` | REJECTED | Decision-to-state mapping MUST occur prior to ledger append | REJECTED is terminal; `rejection_code` MUST be present; execution commit MUST be rejected |
| SUBMITTED (transient) | Decision computed | `decision = PENDING_HITL` | PENDING_HITL | Decision-to-state mapping MUST occur prior to ledger append | Execution commit MUST be rejected while pending; `required_cosign_roles` MUST be defined |
| SUBMITTED (transient) | Decision computed | `decision = ACCEPT` | AUTHORIZED | Decision-to-state mapping MUST occur prior to ledger append | `ledger_authorization_ref` MUST exist; execution commit MAY be accepted |

**Visibility Rule**

`SUBMITTED` is transient and **MUST NOT** be externally observable via retrieval endpoints.

---

# B) HITL Cosign Path

| Current State | Event | Guard (MUST) | Next State | Ledger Stage Requirements | Canonical HTTP Outcome / rejection_code |
|---|---|---|---|---|---|
| PENDING_HITL | `POST /agcp/v1/actions/{action_id}/cosign` | Token valid (tenant-bound, action-bound, signed, unexpired, non-reusable) | No transition OR AUTHORIZED upon quorum | HITL stage precedes authorization stages | If invalid → `COSIGN_INVALID`; if expired → `COSIGN_EXPIRED` |
| PENDING_HITL | Cosign quorum satisfied | Valid quorum satisfaction | AUTHORIZED | Authorization stage aligns to `EXECUTION_AUTHORIZED` | Upon quorum satisfaction, action transitions to AUTHORIZED |
| PENDING_HITL | Expiration or governance cancellation | Expiration/cancel recognized | REJECTED | Transition permitted | REJECTED terminal rules apply |

---

# C) Execution Commit Path

| Current State | Event | Guard (MUST) | Next State | Ledger Stage Requirements | Canonical HTTP Outcome / rejection_code |
|---|---|---|---|---|---|
| AUTHORIZED | `POST /agcp/v1/executions/commit` | Verify action state = AUTHORIZED; ledger reference matches; tenant scope matches | EXECUTED | `EXECUTION_COMMITTED`; execution result appended to ledger | If invalid → `ACTION_NOT_AUTHORIZED` |
| AUTHORIZED | `POST /agcp/v1/executions/commit` | Tenant state = ACTIVE | EXECUTED | Tenant ACTIVE required for execution | Otherwise reject |
| EXECUTED | Replay commit | Any further execution attempt | No transition (terminal) | Further commits MUST be rejected | Replay MUST be rejected |

---

# D) “Only These Transitions Exist” Rule

Permitted transitions are exactly:

```
SUBMITTED -> REJECTED
SUBMITTED -> PENDING_HITL
SUBMITTED -> AUTHORIZED
PENDING_HITL -> AUTHORIZED
PENDING_HITL -> REJECTED
AUTHORIZED -> EXECUTED
```

No other transitions are permitted.

Invalid or inconsistent operations MUST result in:

```
ACTION_NOT_AUTHORIZED
```

or

```
TENANT_STATE_INVALID
```

as appropriate.

---

# E) Ledger Stage Alignment

Ledger stage names SHALL align to lifecycle transitions.

## Evaluation Stages

```
SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
POLICY_RESOLUTION
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
DECISION
```

## Authorization Stage

```
EXECUTION_AUTHORIZED
```

## Commit Stage

```
EXECUTION_COMMITTED
```

Each stage MUST be:

- append-only  
- tenant-scoped  

Lifecycle state SHALL be derivable from ledger history.
