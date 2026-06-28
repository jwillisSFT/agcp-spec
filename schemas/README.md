# AGCP Schemas

This directory contains the normative JSON Schemas used by
AGCP-conformant implementations. These schemas define the canonical
exchange formats used by the HTTP contract and related specifications.

## Design Principles

The schema set is organized around the AGCP governance lifecycle rather
than implementation-specific runtime objects.

Goals:

-   Deterministic behavior
-   Stable, implementation-independent interfaces
-   Clear separation between governance artifacts and governance results
-   Reuse through `common.json`
-   Repository release-based versioning (schemas do not embed
    specification versions)

## Schema Categories

### Common Infrastructure

  -----------------------------------------------------------------------
  Schema                              Purpose
  ----------------------------------- -----------------------------------
  `common.json`                       Shared definitions, identifiers,
                                      enumerations, and reusable types

  `error_response.json`               Standard HTTP/API error response

  `meta_response.json`                Implementation capability discovery

  `tenant.json`                       Tenant definition
  -----------------------------------------------------------------------

### Governance Artifact Schemas

-   `policy_evaluation_module_artifact.json`
-   `policy_artifact.json`
-   `constraint_artifact.json`
-   `invariant_definition.json`
-   `exception_artifact.json`
-   `governance_artifact_view.json`

These define governance artifacts managed by an AGCP implementation.

### Registry Files

-   `constraint-type-registry.json`
-   `invariant-type-registry.json`
-   `rejection-code-registry.json`

### Evaluation Result Schemas

-   `constraint_evaluation.json`
-   `invariant_evaluation.json`

These capture deterministic evaluation results.

### Governance Workflow

-   `proposal_submit_request.json`
-   `proposal_view.json`
-   `governance_decision_result.json`
-   `human_review_artifact.json`
-   `execution_authorization_view.json`
-   `commit_boundary_request.json`
-   `commit_boundary_result.json`
-   `governance_evidence.json`

These model the externally observable governance lifecycle.

## Governance Lifecycle

``` text
Proposal Submission
        ↓
Proposal Qualification
        ↓
Governance Decision Function
        ↓
Human Review (when required)
        ↓
Execution Authorization
        ↓
Commit Boundary
        ↓
Governance Evidence
```

## Schema Relationships

-   `common.json` supplies shared definitions reused throughout the
    schema set.
-   Governance artifact schemas define reusable governance objects.
-   Evaluation schemas describe deterministic policy evaluation results.
-   Workflow schemas define request, response, and lifecycle objects.
-   Governance Evidence provides the canonical evidence record for
    governance-significant processing.

## Versioning

Schema versioning follows repository releases. Individual schema files
intentionally do not embed specification version numbers.

## Normative References

These schemas are intended to be used with:

-   AGCP Core Specification
-   AGCP HTTP Interface Specification
-   AGCP HTTP Contract (OpenAPI)
-   Policy Evaluation Contract (PEC)
-   Governance registries
-   AGCP Conformance Specification
