# DS-016 Retirement and DS-026 Canonical Approval Migration

## Status

Completed on 2026-07-30.

## Retirement action

- Removed `schemas/human_review_artifact.json` from the active AGCP v2.0 schema set.
- Preserved `DS-016` only as a permanently retired, non-reusable historical identifier in the Schema Catalog.
- Recorded `DS-026` `governance_approval_artifact.json` as the sole active approval and adjudication schema.
- Removed DS-016 from all active schema dependency and dependent-schema relationships.

## Interface and implementation cleanup

- Removed the `HumanReviewArtifact` OpenAPI component.
- Replaced `HumanReviewRequest` with `GovernanceApprovalRequest`.
- Removed the `human_review_artifact` compatibility property and one-of fallback.
- Updated the reference implementation to require `request.governance_approval_artifact` directly.
- Updated the HTTP Interface Specification to require the canonical request property exclusively.

## Conformance cleanup

- Removed `human_review_artifact.json` from harness check mappings.
- Updated conformance-harness approval submissions to use `governance_approval_artifact`.
- Replaced compatibility-oriented review-artifact fields with Governance Approval Artifact fixture references and canonical terminology.
- Preserved the governed `Pending Human Review` outcome where it remains part of the normative lifecycle vocabulary; this is a governance outcome, not a DS-016 compatibility object.

## Human adjudication specification

The Human Adjudication and Governance Approval Specification now identifies DS-026 as the only active approval-artifact schema. It contains no DS-016 filename, alias, or alternate request-property allowance.

## Catalog and traceability

- Schema Catalog version: `1.0.40`.
- Active implemented schemas: `43`.
- Retired DS identifiers: `1`.
- Total permanently assigned DS identifiers: `44`.
- RTM dataset version: `RTM-1.43`.
- Historical RTM notes retain DS-016 retirement and supersession context, while active `DS_ID` mappings use DS-026 and active repository paths point to `schemas/governance_approval_artifact.json`.

## Validation result

- 43 Draft 2020-12 active schemas passed metaschema validation.
- 3,579 local schema references and JSON Pointer fragments resolved.
- OpenAPI and conformance-harness YAML parsed successfully.
- No active OpenAPI, reference-implementation, harness, or specification compatibility property remains.
- Catalog hashes matched all active schema files.
- RTM styles, dimensions, merged cells, widths, heights, formulas, theme, and workbook structure were preserved.
