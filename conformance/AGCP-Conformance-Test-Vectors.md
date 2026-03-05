# AGCP Conformance Test Vectors

Status: Informational (Deterministic Conformance Harness Specification)  
AGCP Version: 0.9.0

## Purpose

This document defines deterministic conformance test vectors for AGCP. Each test defines initial conditions, request, expected HTTP response, and expected ledger delta (append-only).

Deterministic conformance test vectors you can use as a harness spec: each test defines initial conditions, request, expected HTTP response, and expected ledger delta (append-only). These are written to be ledger-first so the harness can verify "state is derivable from ledger" and that no illegal transitions occur.

I'm assuming:
- Ledger entries are appended in order and retrievable by (tenant_id, action_id).
- "Action exists" is true if there is any ledger history for that action_id (or a separate action record). If you don't persist a separate action record, treat "no ledger history" as not found.
- HTTP status codes are those recommended in the OpenAPI draft; if you prefer different ones, keep the rejection_code and ledger effects identical.

# A. Conventions used in test vectors

## A.1 Notation

- tenant_id: "T1"
- action_id: "A1" (or generated)
- idem_key: "K1"
- ledger_authorization_ref: "LAR1"
- Cosign token: "CT1"

## A.2 Ledger entry format

Each ledger entry is represented as:
- stage:
- data:

The harness should allow additional fields (timestamps, refs), but must validate stage ordering effects and required stages.

## A.3 Canonical state assertions

For any point-in-time ledger history, the harness should compute:

derive_state(entries):
- if any EXECUTION_COMMITTED -> EXECUTED
- else if any EXECUTION_AUTHORIZED -> AUTHORIZED
- else if latest DECISION is REJECT -> REJECTED
- else if latest DECISION is PENDING_HITL -> PENDING_HITL
- else if latest DECISION is ACCEPT -> AUTHORIZED
- else -> SUBMITTED_TRANSIENT (must not be returned by GET)

# B. Submit endpoint test vectors

## TV-SUB-001 - Happy path ACCEPT -> AUTHORIZED

**Initial conditions**
- tenant_state(T1) = ACTIVE
- idempotency_store has no record for (T1, K1)
- policy_ref resolves

**Request**
- POST /agcp/v1/actions/submit
- Headers: Idempotency-Key = K1
- Body: { tenant_id: T1, policy_ref: valid, action: valid, provenance: valid }

**Expected response**
- HTTP 200
- state = AUTHORIZED
- decision = ACCEPT
- ledger_authorization_ref present

**Expected ledger delta (append-only)**
- SCHEMA_VALIDATION (ok=true)
- PROVENANCE_VERIFICATION (ok=true)
- TENANT_STATE_VALIDATION (ok=true)
- POLICY_RESOLUTION (ok=true)
- PEC_CONSTRAINTS (PASS)
- PEC_INVARIANTS (hard_fail=false)
- PEC_HITL (requires_hitl=false)
- DECISION (ACCEPT)
- EXECUTION_AUTHORIZED (ledger_authorization_ref)

**Determinism checks**
- stages appear in exact pipeline order
- derived state is AUTHORIZED

## TV-SUB-002 - HITL required -> PENDING_HITL

**Initial conditions**
- tenant_state(T1) = ACTIVE
- policy_ref resolves
- PEC_HITL returns: requires_hitl=true, required_cosign_roles=["RISK_OFFICER"]

**Request**
- POST /agcp/v1/actions/submit
- Headers: Idempotency-Key = K1
- Body: { tenant_id: T1, policy_ref: valid, action: valid, provenance: valid }

**Expected response**
- HTTP 200
- state = PENDING_HITL
- decision = PENDING_HITL
- required_cosign_roles includes "RISK_OFFICER"

**Expected ledger delta (append-only)**
- SCHEMA_VALIDATION (ok=true)
- PROVENANCE_VERIFICATION (ok=true)
- TENANT_STATE_VALIDATION (ok=true)
- POLICY_RESOLUTION (ok=true)
- PEC_CONSTRAINTS (PASS)
- PEC_INVARIANTS (hard_fail=false)
- PEC_HITL (requires_hitl=true)
- DECISION (PENDING_HITL)

**Determinism checks**
- no EXECUTION_AUTHORIZED stage exists
- derived state is PENDING_HITL

## TV-SUB-003 - Hard invariant failure -> REJECT

**Initial conditions**
- tenant_state(T1) = ACTIVE
- PEC_INVARIANTS returns hard_fail=true, rejection_code="INVARIANT_HARD_FAIL"

**Request**
- POST /agcp/v1/actions/submit
- Headers: Idempotency-Key = K1
- Body: { tenant_id: T1, policy_ref: valid, action: valid, provenance: valid }

**Expected response**
- HTTP 200
- state = REJECTED
- decision = REJECT
- rejection_code = INVARIANT_HARD_FAIL

**Expected ledger delta (append-only)**
- SCHEMA_VALIDATION (ok=true)
- PROVENANCE_VERIFICATION (ok=true)
- TENANT_STATE_VALIDATION (ok=true)
- POLICY_RESOLUTION (ok=true)
- PEC_CONSTRAINTS (PASS)
- PEC_INVARIANTS (hard_fail=true)
- DECISION (REJECT)

**Determinism checks**
- hard invariant failure always results in REJECT
- derived state is REJECTED

## TV-SUB-004 - Schema validation failure (reject early)

**Initial conditions**
- tenant_state(T1) = ACTIVE

**Request**
- POST /agcp/v1/actions/submit
- Headers: Idempotency-Key = K1
- Body: malformed / invalid schema

**Expected response**
- HTTP 400
- decision = REJECT
- rejection_code = SCHEMA_VALIDATION_FAILED

**Expected ledger delta (append-only)**
- SCHEMA_VALIDATION (ok=false)
- DECISION (REJECT)

**Determinism checks**
- no subsequent stages executed after schema failure

# C. Get action endpoint test vectors

## TV-GET-001 - Get AUTHORIZED action

**Initial conditions**
- Ledger contains history for (T1, A1) including EXECUTION_AUTHORIZED.

**Request**
- GET /agcp/v1/actions/A1

**Expected response**
- HTTP 200
- state = AUTHORIZED

**Expected ledger delta (append-only)**
- none

## TV-GET-002 - Action not externally observable until DECISION exists

**Initial conditions**
- Ledger contains entries for (T1, A1) but no DECISION stage exists yet.

**Request**
- GET /agcp/v1/actions/A1

**Expected response**
- HTTP 404

**Expected ledger delta (append-only)**
- none

**Determinism checks**
- SUBMITTED_TRANSIENT must not be returned by GET

# D. Cosign endpoint test vectors

## TV-COS-001 - Valid cosign submitted, quorum not satisfied

**Initial conditions**
- Action A1 derived state = PENDING_HITL
- required_cosign_roles = ["RISK_OFFICER", "SECURITY_LEAD"]
- a valid cosign token CT1 for "RISK_OFFICER" is available

**Request**
- POST /agcp/v1/actions/A1/cosign
- Body: { tenant_id: T1, action_id: A1, cosign_token: CT1 }

**Expected response**
- HTTP 200
- state = PENDING_HITL

**Expected ledger delta (append-only)**
- none (or COSIGN_RECORDED only, if your design records cosigns in ledger; if recorded, it must be append-only and tenant-bound)

**Determinism checks**
- no EXECUTION_AUTHORIZED stage is appended until quorum satisfied

## TV-COS-002 - Cosign completes quorum -> AUTHORIZED

**Initial conditions**
- Action A1 derived state = PENDING_HITL
- required_cosign_roles = ["RISK_OFFICER"]
- valid cosign token CT1 is available and satisfies HITL

**Request**
- POST /agcp/v1/actions/A1/cosign
- Body: { tenant_id: T1, action_id: A1, cosign_token: CT1 }

**Expected response**
- HTTP 200
- state = AUTHORIZED

**Expected ledger delta (append-only)**
- EXECUTION_AUTHORIZED

**Determinism checks**
- derived state becomes AUTHORIZED only after EXECUTION_AUTHORIZED appears in ledger

# E. Commit endpoint test vectors

## TV-COM-001 - Commit authorized action -> EXECUTED

**Initial conditions**
- tenant_state(T1) = ACTIVE
- Action A1 derived state = AUTHORIZED

**Request**
- POST /agcp/v1/executions/commit
- Body: { tenant_id: T1, action_id: A1, ledger_authorization_ref: LAR1 }

**Expected response**
- HTTP 200
- state = EXECUTED

**Expected ledger delta (append-only)**
- EXECUTION_COMMITTED

**Determinism checks**
- derived state becomes EXECUTED after commit

## TV-COM-002 - Commit when PENDING_HITL -> conflict

**Initial conditions**
- Action A1 derived state = PENDING_HITL

**Request**
- POST /agcp/v1/executions/commit

**Expected response**
- HTTP 409
- rejection_code = ACTION_NOT_AUTHORIZED

**Expected ledger delta (append-only)**
- none

## TV-COM-003 - Commit when REJECTED -> conflict

**Initial conditions**
- Action A1 derived state = REJECTED

**Request**
- POST /agcp/v1/executions/commit

**Expected response**
- HTTP 409
- rejection_code = ACTION_NOT_AUTHORIZED

**Expected ledger delta (append-only)**
- none

# F. Cross-tenant safety tests

## TV-XTEN-001 - Cross-tenant GET denied

**Initial conditions**
- Action A1 belongs to tenant T2
- Caller is tenant T1

**Request**
- GET /agcp/v1/actions/A1

**Expected response**
- HTTP 404 (or 403, if your policy is explicit denial)

**Expected ledger delta (append-only)**
- none

## TV-XTEN-002 - Cross-tenant commit denied

**Initial conditions**
- Action A1 belongs to tenant T2
- Caller is tenant T1

**Request**
- POST /agcp/v1/executions/commit

**Expected response**
- HTTP 403
- rejection_code = TENANT_SCOPE_VIOLATION

**Expected ledger delta (append-only)**
- none

# G. Harness-level determinism tests

## TV-META-001 - Stage ordering invariant

**Procedure**
- Submit a valid request
- Retrieve ledger entries

**Assertions**
Stages appear in exact order:
- SCHEMA_VALIDATION
- PROVENANCE_VERIFICATION
- TENANT_STATE_VALIDATION
- POLICY_RESOLUTION
- PEC_CONSTRAINTS
- PEC_INVARIANTS
- PEC_HITL
- DECISION
- (optional) EXECUTION_AUTHORIZED

## TV-META-002 - Idempotent replay

**Procedure**
- Submit request with key K1
- Submit identical request again with same key K1

**Assertions**
- response identical
- no additional ledger entries
- action_id identical

## TV-META-003 - Ledger-derived state equals API state

**Procedure**
- Compute derived lifecycle state from ordered ledger entries
- Compare to API-reported state

**Assertions**
- response state equals derived state
- SUBMITTED_TRANSIENT must never be externally returned

# Relationship to AGCP Conformance

These vectors support validation of the requirements defined in:
- AGCP Core Specification
- AGCP Conformance Specification
- AGCP Ledger Storage Contract
- AGCP Policy Evaluation Contract

Passing all vectors is required for deterministic conformance validation.
