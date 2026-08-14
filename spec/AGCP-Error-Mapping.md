# AGCP Endpoint-Level Error Mapping

**Status:** Normative  
**Artifact Lifecycle:** Current  
**Specification Version:** 2.0.8  
**Repository Release Target:** AGCP v2.0.8  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.8 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-14  
**Series:** AGCP Core  
**Scope:** HTTP status codes, rejection codes, and Governance Evidence behavior for the AGCP HTTP interface.

---

# 1. Purpose

This document defines the required mapping between HTTP status codes, AGCP rejection codes, and Governance Evidence behavior for AGCP HTTP endpoints.

It is aligned with:

- `api/AGCP-HTTP-Contract.yaml`
- `spec/AGCP-HTTP-Interface-Specification.md`
- AGCP Core Specification
- AGCP rejection-code registry

The OpenAPI contract defines endpoint schemas and response structures. This document defines the required error semantics for those endpoints.

---

# 2. General Error Rules

Implementations SHALL comply with the following rules.

1. Error responses SHALL conform to the `ErrorResponse` schema defined in `api/AGCP-HTTP-Contract.yaml`.

2. Error responses SHALL include a `rejection_code`.

3. `rejection_code` values SHALL be selected from the AGCP rejection-code registry or from an implementation extension registry that does not weaken AGCP normative behavior.

4. HTTP status codes SHALL represent protocol-level semantics.

5. Rejection codes SHALL represent governance-level semantics.

6. Governance Evidence SHALL be produced for governance-significant refusals, denials, failed evaluations, authorization failures, Commit Boundary failures, artifact validation failures, and governed re-evaluation outcomes where the implementation has sufficient context to associate evidence with a governed object.

7. Governance Evidence SHALL NOT be required for unauthenticated requests, malformed requests that cannot be associated with a tenant or governed object, or pre-governance transport failures.

8. Cross-tenant and unauthorized cross-domain access SHALL NOT disclose protected resource existence unless the implementation explicitly adopts a forbid profile.

---

# 3. Cross-Tenant and Cross-Domain Handling

Implementations SHALL apply one cross-scope disclosure strategy consistently.

## 3.1 Hide Profile

The implementation returns:

```text
HTTP 404
rejection_code: RESOURCE_NOT_FOUND
```

## 3.2 Forbid Profile

The implementation returns:

```text
HTTP 403
rejection_code: TENANT_SCOPE_VIOLATION
```

or:

```text
HTTP 403
rejection_code: GOVERNANCE_DOMAIN_VIOLATION
```

The selected strategy SHALL be applied uniformly across protected retrieval endpoints.

---

# 4. POST /agcp/v2/proposals/submit

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Malformed JSON or schema validation failure before tenant association | 400 | SCHEMA_VALIDATION_FAILED | NO |
| Schema validation failure after tenant/proposal association | 400 | SCHEMA_VALIDATION_FAILED | YES |
| Provenance invalid | 400 | PROVENANCE_INVALID | YES |
| Tenant state invalid | 403 | TENANT_STATE_INVALID | YES |
| Tenant scope violation | 403 | TENANT_SCOPE_VIOLATION | YES |
| Governance domain violation | 403 | GOVERNANCE_DOMAIN_VIOLATION | YES |
| Policy not found | 422 | POLICY_NOT_FOUND | YES |
| Canonical State invalid or unavailable | 422 or 503 | CANONICAL_STATE_INVALID or CANONICAL_STATE_UNAVAILABLE | YES |
| Authority Lineage invalid | 403 | AUTHORITY_LINEAGE_INVALID | YES |
| Proposal structural refusal | 400 | PROPOSAL_STRUCTURAL_REFUSAL | YES |
| Governance denial | 200 | GOVERNANCE_DENIED | YES |
| Governance Approval or human adjudication required (`Pending Human Review` outcome) | 200 | GOVERNANCE_APPROVAL_REQUIRED | YES |
| Governed re-evaluation required | 200 or 409 | GOVERNED_REEVALUATION_REQUIRED | YES |
| Policy module unavailable | 503 | POLICY_MODULE_UNAVAILABLE | YES |
| Policy evaluation output invalid | 422 | POLICY_EVALUATION_OUTPUT_INVALID | YES |
| Policy module nondeterministic | 422 | POLICY_MODULE_NONDETERMINISTIC | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- Governance denial is a valid governance outcome, not a transport failure.
- Pending Human Review is a valid governance outcome, not a transport failure.
- Structural Refusal may be returned as an error response when the Proposal cannot be qualified.
- Idempotency conflicts SHALL NOT produce new Governance Evidence because the request is rejected before new governance processing begins.

---

# 5. GET /agcp/v2/proposals/{proposal_id}

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Proposal not found | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, forbid profile | 403 | TENANT_SCOPE_VIOLATION | NO |
| Governance-domain violation, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Governance-domain violation, forbid profile | 403 | GOVERNANCE_DOMAIN_VIOLATION | NO |

Notes:

- Retrieval failures SHALL NOT create new Governance Evidence unless the implementation explicitly records access-denial evidence as an implementation extension.
- Retrieval SHALL NOT expose transient internal processing states.

---

# 6. POST /agcp/v2/proposals/{proposal_id}/governance-approvals

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Malformed request | 400 | SCHEMA_VALIDATION_FAILED | NO |
| Proposal not found | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, forbid profile | 403 | TENANT_SCOPE_VIOLATION | NO |
| Governance-domain violation | 403 | GOVERNANCE_DOMAIN_VIOLATION | NO |
| Governance Approval Artifact invalid | 422 | GOVERNANCE_APPROVAL_INVALID | YES |
| Governance Approval Artifact expired | 409 | GOVERNANCE_APPROVAL_EXPIRED | YES |
| Proposal not in Pending Human Review or Deferred state | 409 | GOVERNED_REEVALUATION_REQUIRED | YES |
| Authority Lineage invalid | 403 | AUTHORITY_LINEAGE_INVALID | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- DS-045 Governance Approval Submissions are untrusted governed commands received through IF-001.
- A Governance Approval Submission SHALL NOT itself assert AGCP verification, eligibility, replay uniqueness, quorum completion, lifecycle effects, Canonical State resolution, authority at commitment, or ledger sequencing, and SHALL NOT itself perform execution.
- DS-026 Governance Approval Artifacts are authoritative AGCP-created or AGCP-qualified records produced only after the required validation and governance processing.
- If Governance Approval processing causes the governance decision to become Authorized, subsequent Execution Authorization behavior SHALL be reflected in Governance Evidence.

---

# 7. GET /agcp/v2/execution-authorizations/{authorization_id}

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Authorization not found | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, forbid profile | 403 | TENANT_SCOPE_VIOLATION | NO |
| Governance-domain violation, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Governance-domain violation, forbid profile | 403 | GOVERNANCE_DOMAIN_VIOLATION | NO |

Notes:

- Retrieving Execution Authorization SHALL NOT execute or commit an Action.
- Retrieval failures do not require new Governance Evidence.

---

# 8. POST /agcp/v2/commit-boundary/commit

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Malformed request | 400 | SCHEMA_VALIDATION_FAILED | NO |
| Tenant state invalid | 403 | TENANT_STATE_INVALID | YES |
| Tenant scope violation | 403 | TENANT_SCOPE_VIOLATION | YES |
| Governance-domain violation | 403 | GOVERNANCE_DOMAIN_VIOLATION | YES |
| Proposal not found | 404 | RESOURCE_NOT_FOUND | NO |
| Execution Authorization not found | 409 | EXECUTION_AUTHORIZATION_INVALID | YES |
| Execution Authorization invalid, expired, revoked, or consumed | 409 | EXECUTION_AUTHORIZATION_INVALID | YES |
| Action not authorized for Commit Boundary processing | 409 | ACTION_NOT_AUTHORIZED | YES |
| Action Representation mutated after qualification | 409 | ACTION_REPRESENTATION_MUTATED | YES |
| Governance Context invalid | 409 | GOVERNANCE_CONTEXT_INVALID | YES |
| Canonical State invalid or unavailable | 422 or 503 | CANONICAL_STATE_INVALID or CANONICAL_STATE_UNAVAILABLE | YES |
| Authority Lineage invalid | 403 | AUTHORITY_LINEAGE_INVALID | YES |
| Authority revoked | 403 | AUTHORITY_REVOKED | YES |
| Authority replay detected | 409 | AUTHORITY_REPLAY_DETECTED | YES |
| Commit prerequisite failure | 422 | COMMIT_BOUNDARY_FAILED | YES |
| Governed re-evaluation required | 409 | GOVERNED_REEVALUATION_REQUIRED | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- Commit Boundary failure SHALL NOT make the Action operationally real.
- Successful Commit Boundary processing SHALL produce Governance Evidence.
- Replay or reuse of consumed authorization SHALL fail.

---

# 9. GET /agcp/v2/governance-evidence/{evidence_id}

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Governance Evidence not found | 404 | RESOURCE_NOT_FOUND | NO |
| Governance Evidence incomplete or invalid | 422 | GOVERNANCE_EVIDENCE_INVALID | NO |
| Cross-tenant access, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, forbid profile | 403 | TENANT_SCOPE_VIOLATION | NO |
| Governance-domain violation, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Governance-domain violation, forbid profile | 403 | GOVERNANCE_DOMAIN_VIOLATION | NO |

Notes:

- Retrieval of Governance Evidence SHALL preserve tenant and governance-domain isolation.
- Invalid evidence SHALL NOT be treated as sufficient for deterministic replay.

---

# 10. POST /agcp/v2/governance-artifacts/policy-modules

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Malformed artifact request | 400 | SCHEMA_VALIDATION_FAILED | NO |
| Tenant state invalid | 403 | TENANT_STATE_INVALID | YES |
| Tenant scope violation | 403 | TENANT_SCOPE_VIOLATION | YES |
| Governance-domain violation | 403 | GOVERNANCE_DOMAIN_VIOLATION | YES |
| Artifact integrity validation failed | 422 | GOVERNANCE_ARTIFACT_INVALID | YES |
| Unauthorized artifact registration | 403 | GOVERNANCE_ARTIFACT_UNAUTHORIZED | YES |
| Policy module unavailable | 503 | POLICY_MODULE_UNAVAILABLE | YES |
| Policy module nondeterministic | 422 | POLICY_MODULE_NONDETERMINISTIC | YES |
| Artifact activation denied | 422 | GOVERNANCE_ARTIFACT_ACTIVATION_DENIED | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- Registration SHALL NOT imply operational activation.
- Policy Evaluation Module artifact validation failures are governance-significant and SHALL produce Governance Evidence where the implementation has sufficient context to associate the failure with a tenant, governed object, or governance artifact.

---

# 11. POST /agcp/v2/governance-artifacts/policies

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Malformed policy artifact | 400 | SCHEMA_VALIDATION_FAILED | NO |
| Tenant state invalid | 403 | TENANT_STATE_INVALID | YES |
| Tenant scope violation | 403 | TENANT_SCOPE_VIOLATION | YES |
| Governance-domain violation | 403 | GOVERNANCE_DOMAIN_VIOLATION | YES |
| Referenced policy module unavailable | 503 | POLICY_MODULE_UNAVAILABLE | YES |
| Policy artifact invalid | 422 | GOVERNANCE_ARTIFACT_INVALID | YES |
| Unauthorized policy registration | 403 | GOVERNANCE_ARTIFACT_UNAUTHORIZED | YES |
| Policy activation denied | 422 | GOVERNANCE_ARTIFACT_ACTIVATION_DENIED | YES |
| Idempotency conflict | 409 | IDEMPOTENCY_CONFLICT | NO |

Notes:

- Policy registration and policy activation are distinct governance events.
- Activation SHALL occur only after applicable governance validation succeeds.
- Governance Policy artifact validation failures are governance-significant and SHALL produce Governance Evidence where the implementation has sufficient context to associate the failure with a tenant, governed object, or governance artifact.

---

# 12. GET /agcp/v2/governance-artifacts/{artifact_id}

| Failure Path | HTTP Status | rejection_code | Governance Evidence |
|---|---:|---|---|
| Artifact not found | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Cross-tenant access, forbid profile | 403 | TENANT_SCOPE_VIOLATION | NO |
| Governance-domain violation, hide profile | 404 | RESOURCE_NOT_FOUND | NO |
| Governance-domain violation, forbid profile | 403 | GOVERNANCE_DOMAIN_VIOLATION | NO |

Notes:

- Retrieval failures do not require new Governance Evidence.
- Access-denial evidence MAY be recorded as an implementation extension.

---

# 13. HTTP Status Code Guidance

| HTTP Status | Meaning |
|---:|---|
| 200 | Request processed and authoritative AGCP response returned |
| 400 | Request malformed or structurally invalid |
| 403 | Tenant, governance-domain, authority, or authorization prohibition |
| 404 | Resource not found or intentionally hidden |
| 409 | Conflict with current governance state, authorization state, idempotency, replay, or transition state |
| 422 | Semantically invalid governance artifact, evidence, policy, Canonical State, or validation result |
| 503 | Required governance dependency unavailable |

---

# 14. Governance Evidence Rules

Governance Evidence SHALL be produced when:

- a Proposal is qualified;
- a Proposal is structurally refused after association;
- the Governance Decision Function produces an outcome;
- Execution Authorization produces an outcome;
- Commit Boundary processing succeeds or fails after association;
- Governance Self-Protection validates, rejects, or requires re-evaluation of a governance artifact;
- governed re-evaluation is required;
- deterministic replay succeeds or fails where replay is an exposed operation.

Governance Evidence SHALL NOT be required when:

- a request is malformed before tenant or governed-object association;
- authentication fails before governance processing begins;
- a protected resource is not found;
- a cross-tenant retrieval is rejected without disclosing protected resource state;
- an idempotency conflict prevents new governance processing.

---

# 15. Breaking Change Guidance

A change to any of the following is a breaking interface change:

- required HTTP status code mapping;
- required rejection code mapping;
- required `ErrorResponse` structure;
- required Governance Evidence behavior;
- endpoint path or method;
- required request or response schema.

Specification release versioning is managed by repository release tags.
# 11. Public Not-Found, Throttling, Capacity, and Governance-Denial Separation

| Condition | HTTP | Public rejection code | Governance Outcome | Retry-After |
|---|---:|---|---|---|
| Protected resource absent or existence hidden | 404 | `RESOURCE_NOT_FOUND` | No | No |
| Pre-governance throttling | 429 | `REQUEST_THROTTLED` | No | Required, delay-seconds |
| System or node capacity unavailable before processing | 503 | `CAPACITY_UNAVAILABLE` | No | Optional |
| Required service dependency unavailable | 503 | Applicable dependency code | No | Optional |
| Governance quota, entitlement, or policy denial | 200 authoritative result | Governance Outcome | Yes | Not applicable |

Resource-specific not-found codes are deprecated for public IF-001 responses. The protected reason MAY be retained in Governance Evidence or telemetry. HTTP 429 and capacity-based HTTP 503 are transport/service conditions and SHALL NOT be reported as governance denial, Structural Refusal, or authorization outcome.
