# AGCP OpenAPI v2 Migration Update and Current Repository Validation

## Scope

This document records the completed migration of the AGCP HTTP interface to IF-001, the version 2 HTTP surface for the AGCP v2.0.4 public release, and its validation against the controlling AGCP v2.0.4 Public Review Controlled Baseline. It is a current controlled release record.

- Controlled RTM baseline: `RTM-1.46`
- Baseline date: `2026-07-30`
- Validation record: `api/AGCP-OpenAPI-v2-migration-validation.json`
- Validation time: `2026-07-31T12:00:00Z`

## Version disposition

- Canonical path namespace: `/agcp/v2`
- Interface identifier: `IF-001`
- OpenAPI version: `3.1.0`
- Contract version: `2.0.4`
- Artifact lifecycle state: `CURRENT`
- Repository release target: `v2.0.4`
- Repository release target status: `PUBLIC_REVIEW_CONTROLLED_BASELINE`
- Controlling published baseline: `v2.0.0`
- Controlling baseline status: `PUBLIC_REVIEW_CONTROLLED_BASELINE`
- `/agcp/v1` is not independently versioned and is not retained as a compatibility surface.
- No v1 routes, aliases, redirects, fallback payloads, or deprecated approval properties are active.

## Endpoint migration

All ten operations use `/agcp/v2`.

The normative HTTP Interface Specification now documents the same ten method/path and
`operationId` combinations as the OpenAPI contract. This includes the three Governance
Artifact operations:

- `POST /agcp/v2/governance-artifacts/policy-modules` — `registerPolicyEvaluationModule`;
- `POST /agcp/v2/governance-artifacts/policies` — `registerGovernancePolicy`; and
- `GET /agcp/v2/governance-artifacts/{artifact_id}` — `getGovernanceArtifact`.

The governed approval endpoint is:

`POST /agcp/v2/proposals/{proposal_id}/governance-approvals`

It accepts exactly one DS-045 Governance Approval Submission. DS-026 Governance Approval Artifact is an authoritative AGCP-created or AGCP-qualified record and is not accepted as request content. The retired DS-016 representation and `/human-review` route are not accepted.

## Canonical schema references

The OpenAPI contract now references authoritative schemas for:

- DS-003 Metadata Response;
- Governance Outcome;
- Proposal Qualification Outcome;
- Execution Authorization Outcome;
- Commit Boundary Outcome;
- Governance Artifact Status;
- Governance Pipeline Stage;
- Rejection Code;
- Provenance;
- Governance Policy reference;
- Action Representation;
- Canonical State reference.

The listed governance-significant definitions are no longer independently embedded in the OpenAPI contract.

## Governance Approval terminology

The following rejection codes were replaced without compatibility aliases:

- `PENDING_HUMAN_REVIEW` -> `GOVERNANCE_APPROVAL_REQUIRED`
- `HUMAN_REVIEW_INVALID` -> `GOVERNANCE_APPROVAL_INVALID`
- `HUMAN_REVIEW_EXPIRED` -> `GOVERNANCE_APPROVAL_EXPIRED`

The controlled constraint and invariant registry identifiers were similarly migrated from `HUMAN_REVIEW_*` to `GOVERNANCE_APPROVAL_*` terminology. Registry entry, entry-set, and document digests were regenerated.

`Pending Human Review` remains a Core-defined governance outcome. It is consumed through the canonical common schema and is not redefined by OpenAPI.

## Synchronized artifacts

The migration updates:

- OpenAPI contract;
- HTTP Interface Specification;
- endpoint error mapping;
- HTTP reference implementation pseudocode;
- conformance harness and harness checks;
- conformance test vectors, matrix, manifest, and supporting documentation;
- provenance, multitenant, and ledger interface terminology;
- constraint, invariant, and rejection-code registries;
- RTM IF mappings.

## Traceability

The HTTP interface is assigned `IF-001`.

The original IF-001 migration advanced the RTM dataset from `RTM-1.43` to `RTM-1.44`. That statement describes the historical migration step only. The active validation has now been refreshed against the controlled `RTM-1.46` baseline. All 122 CR records identify `RTM-1.46`, and the 40 CR records whose repository mappings include the HTTP contract or HTTP Interface Specification continue to identify `IF-001`.

No schema catalog increment was required because no Data Schema definition changed.

## Validation summary

- Validation classification: active controlled baseline.
- Controlled RTM dataset: `RTM-1.46`.
- All 122 CR records identify `RTM-1.46`; 40 records retain `IF-001` mappings.
- 44 active Draft 2020-12 schemas passed metaschema validation.
- 3,579 cross-schema references resolved.
- All three registry documents passed DS-044 validation and digest verification.
- OpenAPI strict YAML parsing passed with no duplicate keys.
- 10 v2 paths and 10 unique operations were validated.
- The HTTP Interface Specification and OpenAPI contract match for method, path, `operationId`, 18 required parameter instances, five JSON request schemas, and 45 response-status instances.
- 149 OpenAPI references resolved.
- All ten mandatory IF-001 operations have schema-valid positive executable coverage.
- The conformance catalog contains 54 Harness Test Vectors and 17 MUST Harness Checks.
- All 52 HTTP primary and setup requests satisfy required OpenAPI parameters and declared response sets.
- All 29 controlled conformance fixtures validate.
- No active `/agcp/v1` route remains.
- No `/human-review` route, retired approval property, or retired human-review rejection code remains active.
- RTM formatting, styles, formulas, dimensions, merged cells, widths, heights, and theme remain preserved.

## P0-06 command/record separation

The governance-approval POST operation now references `schemas/governance_approval_submission.json` (DS-045). `schemas/governance_approval_artifact.json` (DS-026) remains the authoritative record schema and requires `artifact_origin: AGCP_CREATED_OR_QUALIFIED`. Claimant attempts to submit server-derived verification, eligibility, quorum, lifecycle, evidence, digest, replay, or ledger fields are rejected structurally.

## v2.0.4 Error and Metadata Reconciliation

OpenAPI 2.0.4 now uses reusable `PublicNotFound`, `TooManyRequests`, and `ServiceUnavailable` responses. All public 404 responses use `RESOURCE_NOT_FOUND`; every operation declares 429 with required delay-seconds `Retry-After` and 503 for capacity/dependency unavailability. `GET /agcp/v2/meta` is bound to the expanded DS-003 immutable baseline, profile, schema/validator, and active-governance contract.
