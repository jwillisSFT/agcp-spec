# AGCP HTTP Interface Specification

**Status:** Normative\
**Series:** AGCP Core\
**Applies To:** All AGCP-conformant implementations

------------------------------------------------------------------------

# 1. Introduction

This specification defines the normative HTTP interface for interacting
with an AGCP-conformant Governance Control Plane.

The HTTP interface standardizes:

-   Proposal submission
-   Proposal and Action retrieval
-   Human review interaction
-   Execution Authorization retrieval
-   Commit Boundary processing
-   Governance Evidence retrieval
-   Tenant-scoped governance artifact management
-   Metadata discovery

This specification defines externally observable behavior and interface
requirements. It does not prescribe implementation architecture.

------------------------------------------------------------------------

# 2. General Protocol Requirements

## 2.1 Transport

Implementations SHALL support HTTPS using TLS 1.2 or higher.

Plain HTTP SHALL NOT be supported in production deployments.

## 2.2 Media Type

All requests and responses SHALL use:

    Content-Type: application/json

## 2.3 Specification Identification

Implementations MAY expose supported specification identifiers through
metadata endpoints.

Repository releases are the authoritative versioning mechanism for this
specification.

## 2.4 Error Responses

All error responses SHALL include:

-   rejection_code
-   message
-   optional detail
-   applicable governance evidence reference where available

Rejection codes SHALL correspond to the AGCP rejection-code registry.

------------------------------------------------------------------------

# 3. Metadata Endpoint

`GET /agcp/v1/meta`

Returns implementation metadata including supported conformance levels,
supported governance capabilities, and implementation identification.

This endpoint SHALL be accessible without tenant context.

------------------------------------------------------------------------

# 4. Tenant and Governance Domain Management

Implementations SHALL support tenant-scoped governance.

All governance operations SHALL enforce tenant isolation and
governance-domain isolation.

Cross-tenant or unauthorized cross-domain requests SHALL fail.

------------------------------------------------------------------------

# 5. Governance Artifact Management

The interface SHALL support management of:

-   Policy Evaluation Modules
-   Governance Policies
-   Constraints
-   Invariants
-   Exceptions
-   Governance Configuration

Artifact validation SHALL occur prior to activation.

------------------------------------------------------------------------

# 6. Proposal Submission

`POST /agcp/v1/proposals/submit`

Proposal submission SHALL initiate the normative governance pipeline.

The observable processing sequence SHALL be:

1.  Proposal Qualification
2.  Governance Decision Function
3.  Execution Authorization
4.  Commit Boundary
5.  Continuation Integrity (where applicable)

Transient internal processing states SHALL NOT be externally observable.

------------------------------------------------------------------------

# 7. Proposal Retrieval

The interface SHALL expose the authoritative externally observable
Proposal state and governance outcome.

Responses SHALL include applicable references to:

-   Canonical State
-   Governance Context
-   Authority Lineage
-   Governance Evidence
-   Execution Authorization (where applicable)

------------------------------------------------------------------------

# 8. Human Review

Interfaces supporting Pending Human Review SHALL permit governed
submission of human-review artifacts in accordance with applicable
governance policy.

------------------------------------------------------------------------

# 9. Execution Authorization

Execution Authorization resources SHALL expose only authoritative
authorization information and SHALL NOT themselves initiate execution.

------------------------------------------------------------------------

# 10. Commit Boundary

Commit Boundary requests SHALL verify:

-   authoritative Execution Authorization
-   Canonical State validity
-   Authority Lineage validity
-   tenant and governance-domain constraints
-   governance configuration validity

Successful Commit Boundary processing SHALL bind authoritative execution
authorization to the governance-significant Action immediately before
execution.

------------------------------------------------------------------------

# 11. Governance Evidence

Interfaces SHALL permit retrieval of Governance Evidence sufficient for:

-   audit
-   deterministic replay
-   traceability
-   conformance assessment
-   forensic reconstruction

------------------------------------------------------------------------

# 12. Determinism

Identical authoritative inputs SHALL produce identical governance
interpretation and observable governance outcomes.

------------------------------------------------------------------------

# 13. Multitenant Requirements

All governance operations except metadata discovery SHALL require tenant
context and enforce tenant isolation.

------------------------------------------------------------------------

# 14. HTTP Status Codes

Standard HTTP status codes SHALL be used.

Application-specific semantics SHALL be conveyed using AGCP rejection
codes.

------------------------------------------------------------------------

# 15. Conformance

Implementations claiming AGCP conformance SHALL implement all mandatory
endpoints and SHALL preserve deterministic behavior, governance
ordering, tenant isolation, governance evidence production, and
authoritative governance outcomes.

------------------------------------------------------------------------

# 16. Security Considerations

Implementations SHALL authenticate requests, validate provenance,
protect Authority Lineage, preserve Canonical State integrity, and
prevent replay.

------------------------------------------------------------------------

# 17. Non-Goals

This specification does not define:

-   internal storage architecture
-   implementation language
-   database schema
-   deployment topology
-   policy language
-   user interface design
