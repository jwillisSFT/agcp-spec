# AGCP HTTP Reference Implementation Pseudocode

**Status:** Informational  
**Series:** AGCP Core  
**Applies To:** AGCP HTTP Interface implementations

---

# 1. Purpose

This document provides informational reference pseudocode for an AGCP HTTP interface implementation.

It illustrates one deterministic way to implement the HTTP-facing behavior defined by:

- AGCP Core Specification
- AGCP HTTP Interface Specification
- `api/AGCP-HTTP-Contract.yaml`
- AGCP Error Mapping
- AGCP rejection-code registry
- AGCP conformance requirements

This document is not normative. If this document conflicts with the AGCP Core Specification, the AGCP HTTP Interface Specification, or `api/AGCP-HTTP-Contract.yaml`, those documents govern.

Implementations MAY use different internal architecture, storage systems, concurrency models, or component boundaries provided that externally observable behavior remains conformant.

---

# 2. Reference Architecture Assumptions

The reference implementation assumes the following externally observable governance pipeline:

1. Proposal Qualification
2. Governance Decision Function
3. Execution Authorization or another eligible nonterminal state
4. Continuation Integrity, where applicable while the Proposal remains nonterminal and until final Commit-Bound Admissibility is resolved
5. Governance Realization and Commit Boundary processing

Governance Evidence is a cross-cutting supporting service generated during each applicable governance-significant stage; it is not a final sequential stage.

The reference implementation assumes the following HTTP endpoints from `api/AGCP-HTTP-Contract.yaml`:

- `GET /agcp/v2/meta`
- `POST /agcp/v2/proposals/submit`
- `GET /agcp/v2/proposals/{proposal_id}`
- `POST /agcp/v2/proposals/{proposal_id}/governance-approvals`
- `GET /agcp/v2/execution-authorizations/{authorization_id}`
- `POST /agcp/v2/commit-boundary/commit`
- `GET /agcp/v2/governance-evidence/{evidence_id}`
- governance artifact registration and retrieval endpoints

---

# 3. Core Data Model Assumptions

## 3.1 Proposal

A Proposal represents a governance-significant request submitted to AGCP processing.

Reference fields:

```text
proposal_id
tenant_id
governance_domain_id
action_id
action_representation
governance_context
provenance
idempotency_key
```

## 3.2 Governance Evidence

Governance Evidence is the externally observable audit and replay basis for AGCP processing.

Reference fields:

```text
governance_evidence_id
tenant_id
governance_domain_id
associated_object_id
stage
processing_outcome
proposal_id
action_id
canonical_state_ref
policy_ref
authority_lineage_ref
processing_timestamp
```

## 3.3 Execution Authorization

Execution Authorization is an authorization artifact produced after a governance decision permits progression toward Commit Boundary processing.

Reference fields:

```text
authorization_id
proposal_id
action_id
tenant_id
governance_domain_id
authorization_outcome
canonical_state_ref
authority_lineage_ref
governance_evidence_refs
```

## 3.4 Commit Boundary Result

Commit Boundary processing binds authoritative Execution Authorization to the governance-significant Action immediately before execution.

Reference fields:

```text
commit_boundary_ref
proposal_id
action_id
tenant_id
governance_domain_id
commit_outcome
governance_evidence_refs
```

---

# 4. Enumerations

## 4.1 QualificationOutcome

```text
Qualified Proposal
Structural Refusal
```

## 4.2 GovernanceOutcome

```text
Authorized
Denied
Structural Refusal
Pending Human Review
Deferred
Governed Re-evaluation Required
```

## 4.3 ExecutionAuthorizationOutcome

```text
Authorized for Commit Boundary Processing
Authorization Failure
Governed Re-evaluation Required
```

## 4.4 CommitBoundaryOutcome

```text
Commit Successful
Commit Failed
Governed Re-evaluation Required
```

## 4.5 ContinuationOutcome

```text
PROPOSAL_REMAINS_AUTHORIZED
PROPOSAL_REMAINS_VIABLE
GOVERNED_RE_EVALUATION_REQUIRED
DEGRADED
COMMITMENT_SUSPENDED
PROPOSAL_RESTORED_TO_ELIGIBLE_STATE
PROPOSAL_TRANSITIONED_TO_NON_EXECUTABLE_LIFECYCLE_STATE
GOVERNED_TERMINAL_OUTCOME
```

These outcomes apply only while a Proposal remains nonterminal before commitment. Separately defined post-commit operational controls are outside Continuation Integrity.

---

# 5. Storage Interfaces

These storage interfaces are illustrative only.

## 5.1 Idempotency Store

```text
idempotency_get(tenant_id, endpoint_id, idempotency_key)
idempotency_put_if_absent(record)
```

Reference record:

```text
tenant_id
endpoint_id
idempotency_key
request_fingerprint
response_ref
created_at
```

## 5.2 Proposal Store

```text
proposal_get(tenant_id, governance_domain_id, proposal_id)
proposal_create_if_absent(proposal_record)
proposal_update(proposal_record)
```

## 5.3 Execution Authorization Store

```text
authorization_get(tenant_id, governance_domain_id, authorization_id)
authorization_create(authorization_record)
authorization_mark_consumed(authorization_id)
```

## 5.4 Governance Evidence Store

```text
evidence_append(evidence_record)
evidence_get(tenant_id, governance_domain_id, evidence_id)
evidence_list_for_object(tenant_id, governance_domain_id, associated_object_id)
```

## 5.5 Governance Artifact Store

```text
artifact_register(artifact_record)
artifact_get(tenant_id, governance_domain_id, artifact_id)
artifact_activate(artifact_id)
artifact_reject(artifact_id)
```

---

# 6. Deterministic Helper Functions

## 6.1 Canonical Request Fingerprint

```text
function canonical_fingerprint(json_obj):

    canonical = canonicalize_json(json_obj)
    return sha256_hex(canonical)
```

Canonicalization should:

- recursively sort object keys;
- normalize whitespace;
- encode as UTF-8;
- preserve semantic JSON values;
- produce stable output for identical input.

## 6.2 Provenance Wire Verification

```text
function verify_provenance(containing_object):

    validate_schema(containing_object)

    provenance = containing_object.provenance
    require provenance has exactly:
        signer, kid, alg, signed_at, optional expires_at,
        nonce, scope, signature

    protected_b64, signature_b64 = split_exactly_once(provenance.signature, "..")
    protected = decode_base64url_json(protected_b64)

    require protected.typ == "AGCP+PROV"
    require protected.alg == provenance.alg
    require protected.kid == provenance.kid
    require signature_algorithm_allowed(provenance.alg)

    key = resolve_tenant_scoped_verification_key(
        provenance.signer,
        provenance.kid,
        provenance.alg
    )

    enforce_signed_at_and_optional_expiration(provenance)
    enforce_scope_for_operation(provenance.scope)
    enforce_nonce_uniqueness(
        tenant_id=containing_object.tenant_id,
        signer=provenance.signer,
        scope=provenance.scope,
        nonce=provenance.nonce
    )

    unsigned = deep_copy(containing_object)
    remove unsigned.provenance.signature
    canonical_payload = rfc8785_jcs_utf8(unsigned)
    payload_b64 = base64url_without_padding(canonical_payload)
    signing_input = protected_b64 + "." + payload_b64

    if not verify_signature(key, provenance.alg, signing_input, signature_b64):
        record_provenance_evidence(PROVENANCE_INVALID)
        return error_response(400, PROVENANCE_INVALID)

    record_provenance_evidence(PROVENANCE_VALID)
    return OK
```

The nested legacy `provenance.signature.{alg,kid,sig}` object is not accepted. Digest
algorithm identifiers such as `SHA-256` are not signature algorithms.

## 6.3 Tenant and Governance-Domain Validation

```text
function require_tenant_and_domain_valid(tenant_id, governance_domain_id):

    tenant_state = tenant_get_state(tenant_id)

    if tenant_state is not ACTIVE:
        return error_response(403, TENANT_STATE_INVALID)

    if not governance_domain_exists(tenant_id, governance_domain_id):
        return error_response(403, GOVERNANCE_DOMAIN_VIOLATION)

    return OK
```

## 6.4 Tenant Scope Check

```text
function require_same_tenant(request_tenant, resource_tenant):

    if request_tenant != resource_tenant:
        return error_response(403, TENANT_SCOPE_VIOLATION)

    return OK
```

## 6.5 Governance Evidence Append

```text
function record_evidence(stage, associated_object_id, processing_outcome, context):

    evidence = {
        governance_evidence_id: new_id(),
        tenant_id: context.tenant_id,
        governance_domain_id: context.governance_domain_id,
        associated_object_id: associated_object_id,
        stage: stage,
        processing_outcome: processing_outcome,
        proposal_id: context.proposal_id,
        action_id: context.action_id,
        canonical_state_ref: context.canonical_state_ref,
        policy_ref: context.policy_ref,
        authority_lineage_ref: context.authority_lineage_ref,
        processing_timestamp: authoritative_timestamp()
    }

    evidence_append(evidence)

    return evidence.governance_evidence_id
```

---

# 7. Proposal Submission Reference Flow

Endpoint:

```text
POST /agcp/v2/proposals/submit
```

Reference pseudocode:

```text
function submit_proposal(request, idempotency_key):

    endpoint_id = "POST /agcp/v2/proposals/submit"

    validate_schema(request, ProposalSubmitRequest)

    fingerprint = canonical_fingerprint(request)

    existing = idempotency_get(request.tenant_id, endpoint_id, idempotency_key)

    if existing exists:
        if existing.request_fingerprint != fingerprint:
            return error_response(409, IDEMPOTENCY_CONFLICT)
        return load_response(existing.response_ref)

    require_tenant_and_domain_valid(
        request.tenant_id,
        request.governance_domain_id
    )

    verify_provenance(request.provenance)

    proposal = create_proposal_record(request)

    qualification = run_proposal_qualification(proposal)

    record_evidence(
        "Proposal Qualification",
        proposal.proposal_id,
        qualification.outcome,
        proposal.context
    )

    if qualification.outcome == "Structural Refusal":
        view = build_proposal_view(
            proposal,
            qualification_outcome = "Structural Refusal",
            governance_outcome = "Structural Refusal"
        )

        persist_idempotent_response(idempotency_key, fingerprint, view)

        return response(200, view)

    canonical_state_ref = resolve_canonical_state(proposal)

    policy_set = resolve_applicable_policy(proposal, canonical_state_ref)

    authority_lineage_ref = resolve_authority_lineage(proposal)

    governance_decision = run_governance_decision_function(
        proposal,
        canonical_state_ref,
        policy_set,
        authority_lineage_ref
    )

    record_evidence(
        "Governance Decision Function",
        proposal.proposal_id,
        governance_decision.outcome,
        proposal.context
    )

    authorization = null

    if governance_decision.outcome == "Authorized":
        authorization = run_execution_authorization(
            proposal,
            governance_decision,
            canonical_state_ref,
            authority_lineage_ref
        )

        record_evidence(
            "Execution Authorization",
            proposal.proposal_id,
            authorization.outcome,
            proposal.context
        )

    view = build_proposal_view(
        proposal,
        qualification_outcome = qualification.outcome,
        governance_outcome = governance_decision.outcome,
        execution_authorization_ref = authorization.authorization_id if authorization exists
    )

    persist_idempotent_response(idempotency_key, fingerprint, view)

    return response(200, view)
```

Expected externally observable behavior:

- Transient internal processing states are not returned.
- Structural Refusal is returned as an authoritative governance outcome.
- Authorized does not itself execute the Action.
- Execution requires later Commit Boundary processing.
- Governance Evidence references are produced for applicable stages.

---

# 8. Proposal Retrieval Reference Flow

Endpoint:

```text
GET /agcp/v2/proposals/{proposal_id}
```

Reference pseudocode:

```text
function get_proposal(tenant_id, governance_domain_id, proposal_id):

    require_tenant_and_domain_valid(tenant_id, governance_domain_id)

    proposal = proposal_get(tenant_id, governance_domain_id, proposal_id)

    if proposal does not exist:
        return public_not_found(PROPOSAL_NOT_FOUND)

    evidence_refs = evidence_list_for_object(
        tenant_id,
        governance_domain_id,
        proposal_id
    )

    view = build_proposal_view_from_records(proposal, evidence_refs)

    return response(200, view)
```

The response conforms to `ProposalView` in `api/AGCP-HTTP-Contract.yaml`.

---

# 9. Governance Approval and Human Adjudication Reference Flow

Endpoint:

```text
POST /agcp/v2/proposals/{proposal_id}/governance-approvals
```

Reference pseudocode:

```text
function submit_governance_approval(proposal_id, submission, idempotency_key):

    validate_schema(submission, GovernanceApprovalSubmission_DS045)
    reject_if_schema_matches(submission, GovernanceApprovalArtifact_DS026)

    require_tenant_and_domain_valid(
        submission.tenant_id,
        submission.governance_domain_id
    )

    proposal = load_proposal(proposal_id)
    require_equal(proposal.tenant_id, submission.tenant_id)
    require_equal(proposal.governance_domain_id, submission.governance_domain_id)
    require_equal(proposal.proposal_identity, submission.proposal_identity)
    require_equal(proposal.target, submission.target)

    enforce_idempotency(
        tenant_id = submission.tenant_id,
        endpoint = "submitGovernanceApproval",
        idempotency_key = idempotency_key,
        request_digest = canonical_digest(submission)
    )

    verify_provenance(submission)
    authenticated_actor = bind_authenticated_subject(submission.claimed_approver)
    canonical_state = resolve_current_qualified_canonical_state(proposal)
    authority = rederive_current_authority(authenticated_actor, proposal, canonical_state)
    eligibility = evaluate_approver_eligibility(authenticated_actor, proposal, submission, authority)
    replay_result = verify_and_reserve_replay_tuple(submission.provenance, proposal)
    validity = evaluate_submission_validity(submission.validity_window, canonical_state.current_time)

    if any_failed(authority, eligibility, replay_result, validity):
        record_governance_evidence_and_refusal()
        return mapped_rejection()

    quorum_result = deterministically_evaluate_quorum(
        proposal, submission, authenticated_actor, canonical_state
    )
    lifecycle_effect = derive_governed_lifecycle_effect(
        proposal, submission, quorum_result, canonical_state
    )

    artifact = create_governance_approval_artifact_DS026(
        artifact_origin = "AGCP_CREATED_OR_QUALIFIED",
        submission = submission,
        authenticated_actor = authenticated_actor,
        canonical_state = canonical_state,
        authority = authority,
        eligibility = eligibility,
        replay_result = replay_result,
        quorum_result = quorum_result,
        lifecycle_effect = lifecycle_effect
    )

    atomically_persist_artifact_evidence_ledger_and_idempotency(artifact)
    return response(200, build_proposal_view_from_current_state(proposal))
```

Governance Approval Submissions are untrusted governed inputs. Governance Approval Artifacts are authoritative AGCP-created or AGCP-qualified evidence. Neither object executes the Action or establishes authority at commitment.

---

# 10. Execution Authorization Retrieval Reference Flow

Endpoint:

```text
GET /agcp/v2/execution-authorizations/{authorization_id}
```

Reference pseudocode:

```text
function get_execution_authorization(
    tenant_id,
    governance_domain_id,
    authorization_id
):

    require_tenant_and_domain_valid(tenant_id, governance_domain_id)

    authorization = authorization_get(
        tenant_id,
        governance_domain_id,
        authorization_id
    )

    if authorization does not exist:
        return public_not_found(AUTHORIZATION_NOT_FOUND)

    return response(200, build_execution_authorization_view(authorization))
```

Execution Authorization retrieval does not execute or commit the Action.

---

# 11. Continuation Integrity Reference Flow

Continuation Integrity is a pre-commit governance service for authorized or otherwise eligible nonterminal Proposals. It does not govern an Action after successful commitment.

Reference pseudocode:

```text
function maintain_continuation_integrity(proposal_identity, evaluation_horizon):
    proposal = proposal_get_by_identity(proposal_identity)

    if proposal does not exist:
        return public_not_found(PROPOSAL_NOT_FOUND)

    if proposal.lifecycle_state is terminal:
        return build_continuation_result(
            proposal_identity,
            "PROPOSAL_TRANSITIONED_TO_NON_EXECUTABLE_LIFECYCLE_STATE"
        )

    if proposal.commit_boundary_outcome == "Commit Successful":
        return error_response(409, CONTINUATION_INTEGRITY_NOT_APPLICABLE_POST_COMMIT)

    changes = detect_material_governance_condition_changes(
        proposal,
        evaluation_horizon,
        active_risk_based_governance_configuration()
    )

    if changes affect proposal:
        result = deterministically_re_evaluate_nonterminal_proposal(
            proposal,
            changes,
            evaluation_horizon
        )
    else:
        result = verify_continuation_basis_and_admissible_path_viability(
            proposal,
            evaluation_horizon
        )

    if result.continuation_basis cannot be established:
        result = apply_policy_defined_pre_commit_disposition(
            proposal,
            result
        )

    record_evidence(
        "Continuation Integrity",
        proposal_identity.proposal_id,
        result.outcome,
        result.governance_basis
    )

    return build_continuation_integrity_result(result)
```

A Proposal may proceed toward Governance Realization and Commit Boundary processing only when its continuation result permits progression and all final Commit-Bound Admissibility conditions are satisfied.

---

# 12. Commit Boundary Reference Flow

Endpoint:

```text
POST /agcp/v2/commit-boundary/commit
```

Reference pseudocode:

```text
function commit_boundary(request, idempotency_key):
    validate_schema(request, "commit_boundary_request.json")
    require_interface_version("IF-001", "v2")
    verify_idempotency(idempotency_key, request.request_digest)
    verify_provenance(request.provenance)

    proposal_identity = request.proposal_ref.proposal_identity
    proposal = proposal_get(
        request.tenant_id,
        request.governance_domain_id,
        proposal_identity.proposal_id
    )

    if proposal does not exist:
        return public_not_found(PROPOSAL_NOT_FOUND)

    authorization = authorization_get(
        request.tenant_id,
        request.governance_domain_id,
        request.execution_authorization_ref.authorization_id
    )

    if authorization does not exist:
        return error_response(409, EXECUTION_AUTHORIZATION_INVALID)

    if authorization.action_id != request.action_id:
        return error_response(409, EXECUTION_AUTHORIZATION_INVALID)

    if authorization.outcome != "Authorized for Commit Boundary Processing":
        return error_response(409, ACTION_NOT_AUTHORIZED)

    verify_state_qualification(request.state_qualification_result_ref)
    verify_evidence_qualification(request.qualified_evidence_refs)
    verify_authority_rederivation(request.authority_rederivation_result_ref)
    verify_governance_binding(request.governance_binding_validation_result_ref)
    verify_resulting_state(request.resulting_state_validation_result_ref)
    verify_continuation_integrity(request.enforcement_context.continuation_integrity_result_ref)

    commit_result = perform_commit_boundary_binding(
        proposal,
        authorization,
        request.enforcement_context
    )

    if commit_result.outcome == "Commit Successful":
        authorization_mark_consumed(authorization.authorization_id)

    record_evidence(
        "Commit Boundary",
        proposal_identity.proposal_id,
        commit_result.outcome,
        request.enforcement_context
    )

    return response(200, build_commit_boundary_result(commit_result))
```

The DS-018 Commit Boundary Request supplies the canonical current governance basis, including Enforcement Context. Transitional commit-request fields are not accepted. Commit Boundary processing is the only illustrated point at which authorized execution may become operationally real.

---

# 13. Governance Evidence Retrieval Reference Flow

Endpoint:

```text
GET /agcp/v2/governance-evidence/{evidence_id}
```

Reference pseudocode:

```text
function get_governance_evidence(
    tenant_id,
    governance_domain_id,
    evidence_id
):

    require_tenant_and_domain_valid(tenant_id, governance_domain_id)

    evidence = evidence_get(
        tenant_id,
        governance_domain_id,
        evidence_id
    )

    if evidence does not exist:
        return error_response(404, GOVERNANCE_EVIDENCE_INVALID)

    return response(200, build_governance_evidence_view(evidence))
```

Governance Evidence retrieval is tenant-scoped and governance-domain-scoped.

---

# 14. Governance Artifact Registration Reference Flow

Example endpoint:

```text
POST /agcp/v2/governance-artifacts/policy-modules
```

Reference pseudocode:

```text
function register_policy_evaluation_module(request, idempotency_key):

    validate_schema(request, PolicyEvaluationModuleArtifact)

    require_tenant_and_domain_valid(
        request.tenant_id,
        request.governance_domain_id
    )

    verify_provenance(request.provenance)

    integrity_result = validate_artifact_integrity(request)

    if integrity_result failed:
        record_evidence(
            "Governance Self-Protection",
            request.artifact_id,
            "Rejected",
            request.context
        )

        return error_response(422, GOVERNANCE_ARTIFACT_INVALID)

    determinism_result = validate_policy_module_determinism(request)

    if determinism_result failed:
        record_evidence(
            "Governance Self-Protection",
            request.artifact_id,
            "Rejected",
            request.context
        )

        return error_response(422, POLICY_MODULE_NONDETERMINISTIC)

    artifact = artifact_register(request)

    record_evidence(
        "Governance Self-Protection",
        artifact.artifact_id,
        "Registered",
        artifact.context
    )

    return response(200, build_governance_artifact_view(artifact))
```

Artifact registration does not necessarily imply operational activation.

---

# 15. Deterministic Replay Reference Flow

```text
function deterministic_replay(proposal_id, evidence_refs):

    evidence_set = load_evidence_set(evidence_refs)

    verify_evidence_integrity(evidence_set)

    reconstructed_inputs = reconstruct_authoritative_inputs(evidence_set)

    replayed_qualification = replay_proposal_qualification(
        reconstructed_inputs
    )

    replayed_decision = replay_governance_decision_function(
        reconstructed_inputs
    )

    replayed_authorization = replay_execution_authorization(
        reconstructed_inputs
    )

    replayed_commit = replay_commit_boundary_processing(
        reconstructed_inputs
    )

    compare_replay_to_original(
        replayed_qualification,
        replayed_decision,
        replayed_authorization,
        replayed_commit,
        evidence_set
    )

    return replay_result
```

Replay is successful only when the governance interpretation is reproduced from authoritative Governance Evidence and referenced authoritative inputs.

---

# 16. Determinism Requirements Illustrated

A conformant implementation should ensure that:

1. Proposal Qualification occurs before Governance Decision Function processing.
2. Governance Decision Function processing occurs before Execution Authorization.
3. Continuation Integrity applies, where required, only while the Proposal remains nonterminal before commitment.
4. A Proposal lacking a verified continuation basis or viable admissible path cannot proceed to commitment.
5. Governance Realization and Commit Boundary processing occur after applicable pre-commit Continuation Integrity and before execution becomes operationally real.
6. Governance Evidence is produced for applicable governance-significant processing as a cross-cutting supporting service.
7. Canonical State is authoritative over runtime observation.
8. Authority Lineage is preserved and validated.
9. Tenant and governance-domain isolation are enforced.
10. Idempotency prevents duplicate or conflicting request processing.
11. Deterministic replay reproduces governance interpretation from Governance Evidence.

---

# 17. Relationship to Normative Specifications

This document illustrates one possible deterministic reference implementation approach.

The normative requirements are defined by:

- AGCP Core Specification
- AGCP HTTP Interface Specification
- `api/AGCP-HTTP-Contract.yaml`
- AGCP Conformance Specification
- AGCP Error Mapping
- AGCP rejection-code registry

Implementations need not follow this internal pseudocode, but externally observable HTTP behavior must conform to the normative AGCP specifications.

# 17. Public Error and Metadata Helpers

```text
function public_not_found(protected_reason):
    record_protected_diagnostic(protected_reason)
    return error_response(404, RESOURCE_NOT_FOUND,
        retryable=false, governance_evidence_generated=false,
        transport_disposition=NOT_FOUND)

function pre_governance_throttle(retry_after_seconds):
    require retry_after_seconds > 0
    return response(429, header("Retry-After", retry_after_seconds),
        error_response(429, REQUEST_THROTTLED, retryable=true,
        governance_evidence_generated=false, transport_disposition=THROTTLED,
        retry_after_seconds=retry_after_seconds))

function capacity_unavailable():
    return error_response(503, CAPACITY_UNAVAILABLE, retryable=true,
        governance_evidence_generated=false, transport_disposition=CAPACITY_UNAVAILABLE)

function build_metadata():
    baseline = load_pinned_immutable_baseline_record()
    require baseline.digest verified
    require baseline.uri is null only while publication_status == UNPUBLISHED
    require baseline.uri does not identify a moving branch
    validators = load_generated_validator_manifest_bound_to_schema_set()
    active = load_active_governance_activation()
    return signed_metadata_response(baseline, implementation_profile_digest,
        schema_set_digest, validators.validator_set_digest, active.governance_version,
        optional_public_safe_deployment_binding)
```

All retrieval flows return `public_not_found(...)` rather than exposing object-specific not-found codes. Throttling and capacity checks run before governance evaluation. Governance quota or entitlement denial remains an authoritative governance result.
