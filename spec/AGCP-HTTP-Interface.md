# AGCP HTTP Interface Specification v0.9.0

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  
**Applies To:** All AGCP-conformant implementations

---

# 1. Introduction

This document defines the required HTTP interface for interacting with an AGCP implementation.

The HTTP interface standardizes:

- Tenant provisioning
- Policy and registry artifact management
- Action submission
- Decision retrieval
- HITL cosign flows
- Execution commit
- Ledger access
- Metadata/version discovery

This specification defines behavioral requirements, **not implementation architecture**.

---

# 2. General Protocol Requirements

## 2.1 Transport

AGCP implementations **MUST** support:

- HTTPS over TLS 1.2 or higher.

Plain HTTP **MUST NOT** be supported in production deployments.

---

## 2.2 Media Type

All requests and responses **MUST** use:

```
Content-Type: application/json
```

---

## 2.3 Version Header

All responses **MUST** include:

```
AGCP-Spec-Version: 0.9.0
```

Requests **MAY** include:

```
AGCP-Spec-Version: 0.9
```

If an unsupported **MAJOR** version is requested, the implementation **MUST** return:

```
HTTP 400
rejection_code: UNSUPPORTED_SPEC_VERSION
```

---

## 2.4 Error Response Format

All error responses **MUST** conform to:

```json
{
  "error": {
    "rejection_code": "STRING",
    "message": "Human-readable explanation",
    "details": {}
  }
}
```

`rejection_code` **MUST** exist in the rejection-code registry.

---

# 3. Metadata Endpoint

## 3.1 GET /agcp/v1/meta

Returns implementation metadata.

### Response

```json
{
  "implementation_name": "string",
  "implementation_version": "string",
  "supported_spec_versions": ["0.9"],
  "supported_profiles": ["L1","L2","L3","L4","L5"],
  "crypto_profiles": ["LEGACY","PQC","HYBRID"]
}
```

This endpoint **MUST** be accessible without tenant context.

---

# 4. Tenant Management

## 4.1 POST /agcp/v1/tenants

Creates a new tenant.

### Request

```json
{
  "tenant_id": "string",
  "initial_state": "PROVISIONED"
}
```

### Response

```json
{
  "tenant_id": "string",
  "state": "PROVISIONED"
}
```

`tenant_id` **MUST** be globally unique within the deployment.

---

## 4.2 GET /agcp/v1/tenants/{tenant_id}

Returns tenant state.

---

## 4.3 PATCH /agcp/v1/tenants/{tenant_id}

Transitions tenant state.

Allowed transitions:

```
PROVISIONED → ACTIVE
ACTIVE → SUSPENDED
ACTIVE → DECOMMISSIONED
SUSPENDED → ACTIVE
```

Invalid transitions **MUST** return:

```
HTTP 422
rejection_code: TENANT_STATE_INVALID
```

---

# 5. Policy Module Management

## 5.1 POST /agcp/v1/policy-modules

Registers a Policy Evaluation Module (PEM).

### Request

```json
{
  "tenant_id": "string",
  "module_id": "string",
  "version": "string",
  "module_hash": "string",
  "artifact": "base64-encoded or URI",
  "signature": "string"
}
```

### Response

```json
{
  "module_id": "string",
  "version": "string",
  "status": "REGISTERED"
}
```

If module fails integrity validation:

```
HTTP 422
rejection_code: POLICY_MODULE_INVALID
```

---

# 6. Policy Artifact Management

## 6.1 POST /agcp/v1/policies

Registers a policy referencing a module.

### Request

Conforms to `PolicyArtifact.json`.

Key fields:

- tenant_id
- policy_id
- version
- policy_module_ref
- effective_start
- effective_end
- status

### Response

```json
{
  "policy_id": "string",
  "version": "string",
  "status": "ACTIVE"
}
```

If referenced module unavailable:

```
rejection_code: POLICY_MODULE_UNAVAILABLE
```

---

# 7. Constraint Management

## 7.1 POST /agcp/v1/constraints

Registers a `ConstraintArtifact`.

Request body **MUST** conform to `ConstraintArtifact.json`.

Unknown constraint type **MUST** be rejected.

---

# 8. Invariant Management

## 8.1 POST /agcp/v1/invariants

Registers an `InvariantDefinition`.

Must include:

- invariant_type
- evaluation_ref
- enforcement_level

Unknown invariant type **MUST** be rejected.

---

# 9. Exception Management

## 9.1 POST /agcp/v1/exceptions

Registers an `ExceptionArtifact`.

Must include:

- scope
- expiration
- approvals

Expired exceptions **MUST NOT** be considered during PEC evaluation.

---

# 10. Action Submission

## 10.1 POST /agcp/v1/actions/submit

Submits an `ActionEnvelope` for evaluation.

### Request

Conforms to `ActionEnvelope.json`.

---

### Validation Ordering (Mandatory)

Upon submission, implementation **MUST** perform:

1. Schema validation
2. Provenance signature verification
3. Tenant state validation
4. Policy resolution
5. PEC constraint evaluation
6. PEC invariant evaluation
7. PEC HITL evaluation
8. Decision computation
9. Ledger append

---

### Response

Conforms to `ValidationResult.json`.

Possible decisions:

```
ACCEPT
REJECT
PENDING_HITL
```

If duplicate `idempotency_key` with mismatched payload:

```
HTTP 409
rejection_code: IDEMPOTENCY_CONFLICT
```

---

# 11. Action Retrieval

## 11.1 GET /agcp/v1/actions/{action_id}

Returns the canonical governance status of an action.

The response **MUST** conform to:

```
ActionStatusResponse.json
```

The lifecycle state **SHALL** reflect the **Action Lifecycle Model** defined in the Core Specification.

---

## Response Semantics

The response **SHALL** include:

- Current lifecycle state
- Decision outcome
- Rejection code (if applicable)
- HITL requirements (if pending)
- Constraint evaluation results
- Invariant evaluation results
- Ledger authorization reference (if AUTHORIZED or EXECUTED)
- Execution result (if EXECUTED)
- Latest ledger entry reference

`SUBMITTED` state **SHALL NOT** be externally observable.

If `action_id` does not exist within tenant scope:

```
HTTP 404
rejection_code: ACTION_NOT_FOUND
```

Cross-tenant retrieval **MUST** return:

```
HTTP 403
rejection_code: TENANT_SCOPE_VIOLATION
```

---

# 12. HITL Cosign

## 12.1 POST /agcp/v1/actions/{action_id}/cosign

### Request

```json
{
  "tenant_id": "string",
  "cosign_token": "string"
}
```

Invalid token **MUST** return:

```
rejection_code: COSIGN_INVALID
```

Expired token **MUST** return:

```
rejection_code: COSIGN_EXPIRED
```

Upon quorum satisfaction, action state transitions to:

```
AUTHORIZED
```

---

# 13. Execution Commit

## 13.1 POST /agcp/v1/executions/commit

Commits execution of an authorized action.

### Request

```json
{
  "tenant_id": "string",
  "action_id": "string",
  "ledger_authorization_ref": "string",
  "execution_result": {}
}
```

Implementation **MUST** verify:

- action state is `AUTHORIZED`
- ledger reference matches
- tenant scope matches

If invalid:

```
rejection_code: ACTION_NOT_AUTHORIZED
```

Execution result **MUST** be appended to the ledger.

---

# 14. Ledger Access

## 14.1 GET /agcp/v1/ledger/entries/{ledger_ref}

Returns ledger entry.

Cross-tenant access **MUST** return:

```
HTTP 403
rejection_code: TENANT_SCOPE_VIOLATION
```

---

# 15. Determinism Requirements

Identical `ActionEnvelope` submissions **MUST** produce identical decision results when:

- tenant state unchanged
- registry unchanged
- policy unchanged

Replay determinism **MUST** be testable via the conformance harness.

---

# 16. Multitenant Requirements

All endpoints except `/meta` **MUST** require `tenant_id`.

Implementations **MUST** enforce tenant namespace isolation.

---

# 17. Status Codes

Standard HTTP status usage:

```
200 OK
201 Created
400 Bad Request
403 Forbidden
409 Conflict
422 Unprocessable Entity
503 Service Unavailable
```

Rejection codes provide semantic detail.

---

# 18. Conformance Requirements

An implementation **MUST**:

- Implement all **REQUIRED** endpoints
- Enforce ordering guarantees
- Enforce deterministic PEC evaluation
- Enforce multitenant isolation
- Produce structured error responses

---

# 19. Versioning & Compatibility

Within a **MAJOR** version:

- **MINOR** versions **MUST** remain compatible.

Unsupported **MAJOR** versions **MUST** be rejected.

---

# 20. Security Considerations

All endpoints **MUST** require authentication (implementation-defined).

- Envelope signature **MUST** be verified
- Cosign tokens **MUST** be verified
- Policy modules **MUST** be integrity-checked
- Replay protection **MUST** be enforced

---

# 21. Non-Goals

This specification **does not define**:

- Internal storage architecture
- Database schema
- Clustering model
- Performance thresholds
- Policy language implementation
- UI design
