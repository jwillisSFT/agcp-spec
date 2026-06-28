# AGCP HTTP Interface Specification

**Status:** Normative\
**Series:** AGCP Core\
**Applies To:** All AGCP-conformant implementations

------------------------------------------------------------------------

# 1. Purpose

This specification defines the normative HTTP protocol requirements for
AGCP-conformant implementations.

The machine-readable HTTP surface, including paths, operations, request
bodies, response bodies, and schemas, is defined by:

`api/AGCP-HTTP-Contract.yaml`

The AGCP Core Specification remains the authoritative source for
governance behavior, lifecycle semantics, and processing requirements.

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

Where a conflict exists, the AGCP Core Specification governs behavioral
requirements while the OpenAPI contract governs HTTP representation.

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

## 5.1 Metadata

`GET /agcp/v1/meta`

Returns implementation metadata and supported capabilities.

The response SHALL conform to `MetadataResponse`.

------------------------------------------------------------------------

## 5.2 Proposal Submission

`POST /agcp/v1/proposals/submit`

Initiates the AGCP governance pipeline.

The request SHALL conform to `ProposalSubmitRequest`.

The response SHALL conform to `ProposalView`.

Processing SHALL follow the governance pipeline defined by the AGCP Core
Specification.

Clients SHALL provide an `Idempotency-Key` header.

------------------------------------------------------------------------

## 5.3 Proposal Retrieval

`GET /agcp/v1/proposals/{proposal_id}`

Returns the authoritative externally observable Proposal representation.

Responses SHALL conform to `ProposalView`.

------------------------------------------------------------------------

## 5.4 Human Review

`POST /agcp/v1/proposals/{proposal_id}/human-review`

Allows governed submission of human-review artifacts.

Requests SHALL conform to `HumanReviewRequest`.

Responses SHALL conform to `ProposalView`.

------------------------------------------------------------------------

## 5.5 Execution Authorization

`GET /agcp/v1/execution-authorizations/{authorization_id}`

Returns the authoritative Execution Authorization representation.

Responses SHALL conform to `ExecutionAuthorizationView`.

------------------------------------------------------------------------

## 5.6 Commit Boundary

`POST /agcp/v1/commit-boundary/commit`

Performs Commit Boundary processing.

Requests SHALL conform to `CommitBoundaryRequest`.

Responses SHALL conform to `CommitBoundaryResult`.

Commit Boundary SHALL NOT be attempted unless Proposal Qualification,
Governance Decision Function processing, and Execution Authorization
have completed successfully.

------------------------------------------------------------------------

## 5.7 Governance Evidence

`GET /agcp/v1/governance-evidence/{evidence_id}`

Returns Governance Evidence.

Responses SHALL conform to `GovernanceEvidenceView`.

------------------------------------------------------------------------

## 5.8 Governance Artifact Management

Governance artifact endpoints SHALL use the schemas defined for
governance artifacts in the OpenAPI contract.

Artifact registration SHALL NOT imply operational activation.

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
