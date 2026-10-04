# AGCP HTTP Interface Specification

**Status:** Normative\
**Interface Identifier:** IF-001\
**Interface Version:** v2\
**AGCP Specification Release:** v2.1.0\
**Artifact Lifecycle:** Current\
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.1.0 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-14  
**Applies To:** All AGCP-conformant implementations

------------------------------------------------------------------------

# 1. Purpose

This specification defines the normative HTTP protocol requirements for
AGCP-conformant implementations.

The machine-readable HTTP surface, including paths, operations, request
bodies, response bodies, and schemas, is defined by:

`api/AGCP-HTTP-Contract.yaml`

The published AGCP Runtime Governance Conformance Requirements (CRs) and the AGCP Core Specification establish the higher-precedence normative governance behavior, lifecycle semantics, and processing requirements. This Interface Specification is an applicable normative Companion Specification for IF-001 and SHALL remain consistent with those sources.

------------------------------------------------------------------------

# 2. Scope

This specification defines:

-   HTTP protocol semantics
-   Endpoint behavior
-   Authentication expectations
-   Idempotency requirements
-   Error semantics
-   Determinism requirements
-   Tenant and governance-domain isolation
-   Conformance requirements

It does **not** redefine request or response schemas already defined in
the OpenAPI contract.

------------------------------------------------------------------------

# 3. Relationship to the OpenAPI Contract

The OpenAPI contract is the authoritative definition of:

-   Paths
-   Operations
-   Parameters
-   Request bodies
-   Response bodies
-   Common schemas
-   Error schemas

Implementations SHALL conform to both this specification and
`api/AGCP-HTTP-Contract.yaml`.

Conflicts SHALL be resolved using the Core-defined precedence order: published CRs first, then the Core Specification, then this expressly adopted normative Interface Specification. Within IF-001, this specification governs HTTP protocol semantics and the OpenAPI contract governs the machine-readable HTTP representation; neither artifact may weaken or contradict a higher-precedence normative source.


## 3.1 Interface and path versioning

IF-001 uses the canonical path namespace `/agcp/v2`. The path major version is aligned with the version 2 HTTP interface contract for the AGCP v2 interface series. The current contract revision is v2.1.0 and is part of the published v2.1.0 Public Review Controlled Baseline. It is not an independently maintained `/agcp/v1` transport version. This release defines no `/agcp/v1` compatibility routes, aliases, redirects, or fallback request representations.

------------------------------------------------------------------------

# 4. General Protocol Requirements

Implementations SHALL:

-   support HTTPS using TLS 1.2 or later;
-   exchange JSON payloads using `application/json`;
-   authenticate requests except where explicitly documented;
-   preserve deterministic externally observable behavior;
-   enforce tenant and governance-domain isolation.

------------------------------------------------------------------------

# 5. Endpoint Semantics

IF-001 defines the following ten mandatory HTTP operations. The method, path, and
operation identifier set in this table SHALL remain synchronized with
`api/AGCP-HTTP-Contract.yaml`.

| Method | Path | OpenAPI operationId |
|---|---|---|
| `GET` | `/agcp/v2/meta` | `getMetadata` |
| `POST` | `/agcp/v2/proposals/submit` | `submitProposal` |
| `GET` | `/agcp/v2/proposals/{proposal_id}` | `getProposal` |
| `POST` | `/agcp/v2/proposals/{proposal_id}/governance-approvals` | `submitGovernanceApproval` |
| `GET` | `/agcp/v2/execution-authorizations/{authorization_id}` | `getExecutionAuthorization` |
| `POST` | `/agcp/v2/commit-boundary/commit` | `commitBoundaryProcessing` |
| `GET` | `/agcp/v2/governance-evidence/{evidence_id}` | `getGovernanceEvidence` |
| `POST` | `/agcp/v2/governance-artifacts/policy-modules` | `registerPolicyEvaluationModule` |
| `POST` | `/agcp/v2/governance-artifacts/policies` | `registerGovernancePolicy` |
| `GET` | `/agcp/v2/governance-artifacts/{artifact_id}` | `getGovernanceArtifact` |

## IF-001 Contract Parity Summary

The following operation contract summary is normative for the human-readable IF-001
specification and SHALL remain synchronized with `api/AGCP-HTTP-Contract.yaml`.
Parameter notation is `location:name`. `none` means that the operation has no required
parameter or JSON request body. Response-status sets include both success and
non-success responses.

| Method | Path | operationId | Required parameters | JSON request schema | Permitted response statuses |
|---|---|---|---|---|---|
| `GET` | `/agcp/v2/meta` | `getMetadata` | `none` | `none` | `200` |
| `POST` | `/agcp/v2/proposals/submit` | `submitProposal` | `header:Idempotency-Key` | `ProposalSubmitRequest` | `200, 400, 403, 409, 422, 503` |
| `GET` | `/agcp/v2/proposals/{proposal_id}` | `getProposal` | `path:proposal_id`, `query:tenant_id`, `query:governance_domain_id` | `none` | `200, 403, 404` |
| `POST` | `/agcp/v2/proposals/{proposal_id}/governance-approvals` | `submitGovernanceApproval` | `path:proposal_id`, `header:Idempotency-Key` | `GovernanceApprovalSubmission` | `200, 400, 403, 404, 409, 422` |
| `GET` | `/agcp/v2/execution-authorizations/{authorization_id}` | `getExecutionAuthorization` | `path:authorization_id`, `query:tenant_id`, `query:governance_domain_id` | `none` | `200, 403, 404` |
| `POST` | `/agcp/v2/commit-boundary/commit` | `commitBoundaryProcessing` | `header:Idempotency-Key` | `CommitBoundaryRequest` | `200, 400, 403, 404, 409, 422, 503` |
| `GET` | `/agcp/v2/governance-evidence/{evidence_id}` | `getGovernanceEvidence` | `path:evidence_id`, `query:tenant_id`, `query:governance_domain_id` | `none` | `200, 403, 404, 422` |
| `POST` | `/agcp/v2/governance-artifacts/policy-modules` | `registerPolicyEvaluationModule` | `header:Idempotency-Key` | `PolicyEvaluationModuleArtifact` | `200, 400, 403, 409, 422, 503` |
| `POST` | `/agcp/v2/governance-artifacts/policies` | `registerGovernancePolicy` | `header:Idempotency-Key` | `GovernancePolicyArtifact` | `200, 400, 403, 409, 422, 503` |
| `GET` | `/agcp/v2/governance-artifacts/{artifact_id}` | `getGovernanceArtifact` | `path:artifact_id`, `query:tenant_id`, `query:governance_domain_id` | `none` | `200, 403, 404` |

For every operation requiring `tenant_id` and `governance_domain_id` query
parameters, the pair SHALL identify the tenant and Governance Domain in which the
resource is resolved. An implementation SHALL NOT infer, substitute, or broaden that
scope from a path identifier, authenticated identity, or another request context.
Existence and requester authority SHALL be evaluated within the supplied pair, and a
scope or disclosure failure SHALL use the operation's declared `403` or `404` response
as applicable.

For every operation requiring `Idempotency-Key`, the key SHALL be scoped to the
`tenant_id` carried by the canonical request body and to the endpoint. Equivalent reuse
SHALL NOT create a duplicate governance-significant effect. Conflicting reuse SHALL
produce the declared `409` response with rejection code `IDEMPOTENCY_CONFLICT`.

For every IF-001 request body or submitted artifact containing `provenance`, the
provenance member SHALL conform to `schemas/common.json#/$defs/provenance` and the
AGCP Provenance Wire Format Specification. `signer`, `kid`, `alg`, `signed_at`,
`nonce`, `scope`, and the detached `signature` string are direct provenance fields.
The nested legacy signature-object representation SHALL be rejected by schema
validation. Provenance schema validation, protected-header comparison, key and
algorithm authorization, canonical payload reconstruction, signature verification,
scope enforcement, expiration, and nonce uniqueness SHALL complete before governance
processing relies on the signed content.

For every IF-001 request, response, or referenced artifact containing an algorithm-explicit content digest, the digest SHALL conform to `schemas/common.json#/$defs/content_digest`. The digest value SHALL be lowercase hexadecimal and SHALL contain exactly 64 characters for `SHA-256` and `BLAKE2B-256`, 96 characters for `SHA-384`, and 128 characters for `SHA-512` and `BLAKE2B-512`. A declared algorithm paired with a different length, uppercase hexadecimal, a non-hexadecimal value, or the ambiguous identifier `BLAKE2B` SHALL fail schema validation before governance processing relies on the digest.

## 5.1 Metadata

`GET /agcp/v2/meta`

Returns implementation metadata and supported capabilities.

The response SHALL conform to `MetadataResponse`.

------------------------------------------------------------------------

## 5.2 Proposal Submission

`POST /agcp/v2/proposals/submit`

Initiates the AGCP governance pipeline.

The request SHALL conform to `ProposalSubmitRequest`.

The response SHALL conform to `ProposalView`.

Processing SHALL follow the governance pipeline defined by the AGCP Core
Specification.

Clients SHALL provide an `Idempotency-Key` header.

------------------------------------------------------------------------

## 5.3 Proposal Retrieval

`GET /agcp/v2/proposals/{proposal_id}`

Returns the authoritative externally observable Proposal representation.

The request SHALL provide `proposal_id` as a required path parameter and SHALL
provide `tenant_id` and `governance_domain_id` as required query parameters. The
query-parameter pair SHALL identify the tenant and Governance Domain in which the
Proposal is resolved and SHALL be processed according to the scope semantics defined
in the IF-001 Contract Parity Summary.

Responses SHALL conform to `ProposalView`.

------------------------------------------------------------------------

## 5.4 Governance Approval and Human Adjudication

Human governance participation uses the controlled Governance Approval Submission ingress contract. A submission is a claimant command, not an authoritative approval record.

IF-001 governance-approval ingress SHALL NOT accept DS-026 Governance Approval Artifact as a client-supplied command body. It SHALL accept DS-045 Governance Approval Submission and independently create or qualify authoritative DS-026 evidence.

The caller SHALL be authenticated according to the controlling Implementation Profile. `claimed_approver` and any caller-supplied role, group, entitlement, reviewer class, delegation, permission, or authority-scope field are non-authoritative claims.

Before creating or qualifying the authoritative Governance Approval Artifact, AGCP SHALL bind the authenticated subject to the submission and resolve the authoritative identity and authorization/entitlement record through the implementation-selected IAS Profile. The resulting eligibility determination SHALL follow the Human Adjudication and Governance Approval Specification.

The HTTP interface SHALL NOT permit a claimant to self-assert AGCP verification, current approval eligibility, quorum satisfaction, or authoritative identity/entitlement state.

## 5.5 Execution Authorization

Execution Authorization retrieval exposes the authoritative authorization state associated with the governed proposal according to the Core and controlled schemas.

A successful read of an Execution Authorization SHALL NOT be interpreted as a commit, a target effect, or proof that the authorization is still usable at the time of commitment. Current commitment-sensitive conditions are established later by the Governance Realization Function (GRF).

Clients SHALL treat the returned authorization as an input to the subsequent governed progression defined by the lifecycle and controlling Implementation Profile.

## 5.6 Commit Boundary

`POST /agcp/v2/commit-boundary/commit` is the public IF-001 invocation for Governance Realization / commit-bound processing. The endpoint SHALL NOT be interpreted as a direct PEP endpoint.

For an eligible request, the GRF SHALL, as applicable:

1. validate the Execution Authorization and proposal binding;
2. re-establish current commitment-sensitive authority, Canonical State, evidence, lifecycle, and prior-use conditions;
3. perform Governance Binding Validation and Commit-Bound Admissibility;
4. apply the Implementation Profile-selected PEP Profile or equivalent controlled enforcement mapping;
5. construct or complete the integrity-protected Enforcement Context; and
6. invoke or coordinate the selected PEP through the protected enforcement path.

The PEP SHALL control whether the exact commit-eligible governed transition crosses the enforcement boundary. The GRF and PEP MAY be co-located, but their logical responsibilities remain distinct and testable.

A successful Commit Boundary Result means that AGCP accepted the exact governed transition for application at the defined commitment point. It SHALL NOT universally be interpreted as proof that a downstream asynchronous target operation has already completed. Where commitment and target completion are distinct, later execution/outcome evidence SHALL establish operational realization.

The controlling Implementation Profile and PEP Profile define protected GRF-to-PEP interface details. IF-001 does not standardize a public generic PEP API.

## 5.7 Governance Evidence

`GET /agcp/v2/governance-evidence/{evidence_id}`

Returns Governance Evidence.

The request SHALL provide `evidence_id` as a required path parameter and SHALL
provide `tenant_id` and `governance_domain_id` as required query parameters. The
query-parameter pair SHALL identify the tenant and Governance Domain in which the
Governance Evidence is resolved and SHALL be processed according to the scope
semantics defined in the IF-001 Contract Parity Summary.

Responses SHALL conform to `GovernanceEvidenceView`.

Governance Evidence is generated throughout applicable governance-significant processing as
a cross-cutting supporting service. Placement of this retrieval operation after the Commit
Boundary operation in this interface document SHALL NOT be interpreted as a sequential pipeline
stage or as limiting evidence generation to post-commit processing.

------------------------------------------------------------------------

## 5.8 Governance Artifact Management

Governance artifact operations SHALL use the schemas, parameters, request bodies,
responses, and error representations defined by the OpenAPI contract. Governance
artifact registration SHALL remain distinct from controlled operational activation.

### 5.8.1 Policy Evaluation Module Registration

`POST /agcp/v2/governance-artifacts/policy-modules`

Registers an integrity-bound, tenant-scoped, and governance-domain-scoped Policy
Evaluation Module artifact.

The request body SHALL conform to `PolicyEvaluationModuleArtifact`.

The response SHALL conform to `GovernanceArtifactView`.

Clients SHALL provide an `Idempotency-Key` header. Equivalent requests using the same
key SHALL be processed according to the IF-001 idempotency rules; a conflicting reuse
SHALL be rejected.

Registration processing SHALL validate the artifact's structure, provenance, integrity,
deterministic interface and behavior, policy and configuration bindings, registry and
compilation bindings, lineage, validation status, authority, tenant, and governance-domain
scope as applicable.

Registration SHALL NOT make the Policy Evaluation Module operationally effective.
Operational activation SHALL occur only after all applicable governance compilation,
constitutional validation, omission-analysis, Governance Self-Protection, approval, and
controlled-activation prerequisites have been satisfied.

### 5.8.2 Governance Policy Registration

`POST /agcp/v2/governance-artifacts/policies`

Registers a tenant-scoped and governance-domain-scoped Governance Policy Artifact.

The request body SHALL conform to `GovernancePolicyArtifact`.

The response SHALL conform to `GovernanceArtifactView`.

Clients SHALL provide an `Idempotency-Key` header. Equivalent requests using the same
key SHALL be processed according to the IF-001 idempotency rules; a conflicting reuse
SHALL be rejected.

Registration processing SHALL validate the policy artifact's structure, provenance,
integrity, authority, referenced Policy Evaluation Module, tenant and governance-domain
scope, and applicable governance bindings.

Policy registration and policy activation are distinct governance events. Registration
SHALL NOT activate the policy. Operational activation SHALL occur only through the
applicable Governance Self-Protection, validation, approval, compilation, and controlled-
activation requirements.

### 5.8.3 Governance Artifact Retrieval

`GET /agcp/v2/governance-artifacts/{artifact_id}`

Returns the authoritative externally observable Governance Artifact representation for
the requested identifier.

The request SHALL provide `artifact_id` as a path parameter and SHALL provide
`tenant_id` and `governance_domain_id` as query parameters.

The response SHALL conform to `GovernanceArtifactView`.

Retrieval SHALL preserve tenant and governance-domain isolation. An implementation
SHALL return the OpenAPI-defined forbidden or not-found response, as applicable, when
the artifact does not exist or the requester is not permitted to access the applicable
tenant or governance domain.

------------------------------------------------------------------------

# 6. Error Semantics

Error responses SHALL conform to `ErrorResponse`.

Rejection codes SHALL be selected from the AGCP rejection-code registry.

HTTP status codes SHALL distinguish transport semantics while rejection
codes identify governance semantics.

------------------------------------------------------------------------

# 7. Determinism

Identical authoritative inputs SHALL produce identical externally
observable HTTP responses, governance outcomes, and Governance Evidence
references.

------------------------------------------------------------------------

# 8. Tenant and Governance-Domain Isolation

Except where explicitly documented, requests SHALL include tenant
context.

Implementations SHALL prevent unauthorized cross-tenant and cross-domain
access.

------------------------------------------------------------------------

# 9. Security

Implementations SHALL:

-   authenticate requests;
-   validate provenance;
-   protect Authority Lineage;
-   preserve Canonical State integrity;
-   prevent replay;
-   enforce authorization before Commit Boundary processing.

------------------------------------------------------------------------

# 10. Conformance

An implementation claiming AGCP conformance SHALL:

-   implement all mandatory operations defined in
    `api/AGCP-HTTP-Contract.yaml`;
-   preserve deterministic behavior;
-   enforce governance ordering;
-   produce schema-conformant requests and responses;
-   enforce tenant and governance-domain isolation;
-   produce Governance Evidence consistent with the AGCP Core
    Specification.

Executable IF-001 operation coverage SHALL include at least one schema-valid positive
vector for each of the ten mandatory operations. For an operation introduced into the
executable coverage set, the controlled coverage record SHALL also identify the
applicable negative and tenant/Governance-Domain-isolation scenarios. Operations that
require `Idempotency-Key` and are introduced into the coverage set SHALL include both
equivalent-replay and conflicting-reuse scenarios unless an explicit controlled
disposition states why those scenarios are not applicable.

For the five operations added to close the previously absent operation coverage:

-   Execution Authorization retrieval and governance-artifact retrieval include positive,
    not-found, and cross-scope isolation vectors;
-   Policy Evaluation Module and Governance Policy registration include positive,
    malformed-request, cross-scope isolation, equivalent-replay, and conflicting-reuse
    vectors; and
-   metadata discovery includes a schema-valid positive vector only.

`GET /agcp/v2/meta` is intentionally unauthenticated, has no tenant or Governance
Domain parameter, has no idempotency key, and declares only a `200` response. Negative,
isolation, and idempotency vectors are therefore not applicable to that operation unless
IF-001 is revised to declare such behavior.

The controlled executable coverage is defined by
`conformance/AGCP-Conformance-Harness-Spec.yml`, mirrored in
`conformance/AGCP-Conformance-Test-Vectors.md`, and traced through
`conformance/test-mapping.json`. Harness coverage supports the Formal Test Cases and
SHALL NOT independently establish conformance.

------------------------------------------------------------------------

# 11. Non-Goals

This specification does not define:

-   internal architecture;
-   storage implementation;
-   database schema;
-   deployment topology;
-   policy language;
-   implementation language;
-   user interface design.

## 6.1 Public Not-Found Normalization

Every public IF-001 protected-resource lookup failure SHALL return HTTP 404 with rejection code `RESOURCE_NOT_FOUND`, whether the object is absent or its existence is hidden by tenant, Governance Domain, or disclosure policy. `PROPOSAL_NOT_FOUND`, `AUTHORIZATION_NOT_FOUND`, `GOVERNANCE_EVIDENCE_NOT_FOUND`, and `GOVERNANCE_ARTIFACT_NOT_FOUND` are deprecated for public IF-001 responses and MAY be retained only in protected diagnostics or Governance Evidence.

## 6.2 Pre-Governance Throttling and Capacity

Pre-governance throttling SHALL return HTTP 429 with rejection code `REQUEST_THROTTLED` and a required `Retry-After` header encoded as delay-seconds. A system or node that cannot safely begin processing because capacity is unavailable SHALL return HTTP 503 with rejection code `CAPACITY_UNAVAILABLE`. These conditions occur before an authoritative governance decision and SHALL NOT be represented as Governance Outcomes. A policy or entitlement quota evaluated by governance remains an authoritative Governance Outcome rather than an HTTP 429 transport rejection.

## 6.3 Metadata, Immutable Distribution, and Active Governance

`GET /agcp/v2/meta` SHALL advertise the immutable AGCP baseline bundle identity and digest, the claimed Implementation Profile identity and digest, schema-set and generated-validator-set identities and digests, the active governance version and activation integrity, and the implemented IF-001 contract. A published baseline URI SHALL identify an immutable release artifact and SHALL NOT resolve to a moving branch. Optional deployment, node, workspace, Tenant, and Governance Domain binding SHALL use public-safe opaque identifiers and SHALL NOT expand authority or disclose secrets. Verified claims SHALL remain evidence-bound.

## Management and test-plane separation

Beginning with AGCP v2.1.0, IF-001 remains the governed-action HTTP interface. Governance observation and administrative management are exposed, when implemented, through IF-003 and IF-004 under the separate `api/AGCP-Management-Contract.yaml`. Optional isolated conformance test control uses IF-005. IF-003/004/005 SHALL NOT be used to bypass IF-001 Proposal, Governance Decision, Execution Authorization, Commit Boundary, or ledger semantics.


## 13. Test-Scope Propagation for IF-005

Beginning with the corrected AGCP v2.1.0 management/test-control contract, IF-001 operations other than metadata MAY receive the optional `X-AGCP-Test-Scope` header defined by `api/AGCP-HTTP-Contract.yaml`.

The header is valid only when IF-005 is implemented and enabled and the caller is authorized for the named isolated test scope. When accepted, the exact scope identifier SHALL propagate through the authoritative-source, temporal, authority, evidence, human-review, continuation, and enforcement adapters used by that governed request. Test-scoped inputs SHALL NOT affect requests lacking the same authorized scope.

An implementation SHALL NOT accept an unauthorized test-scope header and then silently process the request with test fixtures.

### 13.1 Proposal transport validation versus Proposal Qualification

DS-013 validates the submission transport envelope. It intentionally does not pre-validate the `proposal` member against DS-021.

The candidate Proposal is untrusted governance input. Proposal Qualification SHALL validate it against DS-021 and all applicable semantic qualification rules. A DS-021 structural failure, missing mandatory proposal dimension, unsupported proposal schema/version, or equivalent proposal-qualification defect SHALL therefore remain capable of producing the authoritative Structural Refusal behavior required by the AGCP Core and Formal Test Cases rather than being converted into a transport-only parsing outcome.

Transport errors remain appropriate for malformed HTTP, invalid JSON, missing transport envelope, authentication failures that prevent governance ingress, or other failures that occur before a candidate Proposal can enter Proposal Qualification.
## Generated governance artifact validation

Before an AGCP-generated or AGCP-qualified governance artifact is persisted, returned as authoritative, or referenced by an authoritative Governance Ledger event, the implementation SHALL validate the artifact against the active controlled DS schema for that artifact type. A schema-invalid internally generated artifact is an implementation failure and SHALL NOT be persisted or exposed as an authoritative governance outcome. This validation is additional to, and does not replace, the semantic obligations of the Core Specification.

## Current-release metadata default

The implementation metadata endpoint SHALL identify the AGCP release actually compiled or configured for the running server. Repository builds produced from this controlled source SHALL derive the default current-release identifier from the root `VERSION` source (or an immutable build artifact generated from it), rather than from an independently maintained hard-coded release literal. Historical supported releases MAY also be advertised, but `default_agcp_release_id` SHALL identify a member of `supported_agcp_releases` and SHALL match the active current-release expectation used by the controlled harness for the running release.

## Machine-readable v2.1.x synchronization

IF-001 now uses DS-018 as the public Governance Realization invocation request. The caller does not provide authoritative commitment-time state, Authority Re-Derivation, Governance Binding Validation, Enforcement Context, PEP identity, or PEP Profile selection. The GRF establishes those facts. DS-019 records commitment and references DS-052 for post-commit execution outcome. Approval ingress is qualified through DS-053.
