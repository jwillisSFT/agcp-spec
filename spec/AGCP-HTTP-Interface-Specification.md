# AGCP HTTP Interface Specification

**Status:** Normative\
**Interface Identifier:** IF-001\
**Interface Version:** v2\
**AGCP Specification Release:** v2.0.5\
**Artifact Lifecycle:** Current\
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.5 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-05  
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

IF-001 uses the canonical path namespace `/agcp/v2`. The path major version is aligned with the version 2 HTTP interface contract for the AGCP v2 interface series. The current contract revision is v2.0.5 and is part of the published v2.0.5 Public Review Controlled Baseline. It is not an independently maintained `/agcp/v1` transport version. This release defines no `/agcp/v1` compatibility routes, aliases, redirects, or fallback request representations.

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

`POST /agcp/v2/proposals/{proposal_id}/governance-approvals`

Accepts one DS-045 `GovernanceApprovalSubmission` as untrusted claimant ingress for human adjudication, cosignature, risk acceptance, cancellation, withdrawal, or quorum participation. The operation SHALL NOT accept DS-026 `GovernanceApprovalArtifact` as request content.

The submission MAY carry claimant-provided approval content, claimed approver identity, claimant provenance, validity intent, and quorum association. It SHALL NOT carry or authoritatively assert AGCP-created fields, including approval-artifact identity or status, signature-verification outcome, replay uniqueness, approver eligibility, current lifecycle eligibility, Canonical State qualification, Authority Lineage qualification, Governance Evidence, quorum count or completion, lifecycle effect, artifact digest, semantic-verification results, or Governance Ledger ordering.

AGCP SHALL validate DS-045 and provenance first; bind the authenticated subject, Tenant, Governance Domain, Proposal Identity, target, scope, and policy context; resolve current qualified governance inputs; independently verify authority, eligibility, validity, replay uniqueness, and signature; deterministically evaluate quorum and lifecycle effects; record Governance Evidence and ordered Governance Ledger events; and only then create or qualify a DS-026 `GovernanceApprovalArtifact`.

Clients SHALL provide an `Idempotency-Key` header. The key SHALL be scoped to the `tenant_id` carried by `GovernanceApprovalSubmission` and to this endpoint. Equivalent reuse SHALL NOT create duplicate approval, adjudication, cosignature, risk-acceptance, cancellation, withdrawal, artifact, evidence, ledger, or quorum effects; conflicting reuse SHALL produce `409` with rejection code `IDEMPOTENCY_CONFLICT`.

Responses SHALL conform to `ProposalView`. Any DS-026 record returned or referenced in the resulting view is authoritative AGCP-created or AGCP-qualified evidence, not an echo of claimant-supplied record state.

------------------------------------------------------------------------

## 5.5 Execution Authorization

`GET /agcp/v2/execution-authorizations/{authorization_id}`

Returns the authoritative Execution Authorization representation.

The request SHALL provide `authorization_id` as a required path parameter and SHALL
provide `tenant_id` and `governance_domain_id` as required query parameters. The
query-parameter pair SHALL identify the tenant and Governance Domain in which the
Execution Authorization is resolved and SHALL be processed according to the scope
semantics defined in the IF-001 Contract Parity Summary.

Responses SHALL conform to `ExecutionAuthorizationView`.

------------------------------------------------------------------------

## 5.6 Commit Boundary

`POST /agcp/v2/commit-boundary/commit`

Performs Commit Boundary processing.

Requests SHALL conform to `CommitBoundaryRequest`.

Clients SHALL provide an `Idempotency-Key` header. The key SHALL be scoped to the
`tenant_id` carried by `CommitBoundaryRequest` and to this endpoint. Equivalent reuse
SHALL NOT produce a duplicate commitment or governed consequence; conflicting reuse
SHALL produce `409` with rejection code `IDEMPOTENCY_CONFLICT`.

Responses SHALL conform to `CommitBoundaryResult`.

Commit Boundary processing SHALL NOT be attempted unless Proposal Qualification,
Governance Decision Function processing, Execution Authorization, and any applicable
pre-commit Continuation Integrity obligations for the nonterminal Proposal have been
successfully satisfied.

At the Commit Boundary, the Governance Realization Function SHALL coordinate current
Canonical State Resolution, State Qualification, Evidence Qualification, Authority
Re-Derivation, Governance Binding Validation, Commit-Bound Admissibility, and enforcement
through the applicable Policy Enforcement Point.

------------------------------------------------------------------------

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
