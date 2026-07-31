# AGCP Specification Changelog

## 2026-07-31 — AGCP v2.0.0 comparison-based release notes

- Added `RELEASE_NOTES_v2.0.0.md` at the repository root, based on a file-, interface-, schema-, specification-, lifecycle-, traceability-, and conformance-level comparison with the attached `agcp-spec-v.1.0.0.zip` archive.
- Documented the cross-major compatibility boundary, `/agcp/v2` interface migration, proposal-centric data model, Canonical State source-resolution model, Commit-Bound Admissibility, Governance Realization, Governance Evidence, Continuation Integrity, governance compilation, conformance expansion, removed/replaced artifacts, and implementer migration checklist.
- Recorded the comparison archive's internal version-label discrepancy without altering either source archive.
- Updated the root README to link the release notes and synchronized its controlled conformance counts to 17 Harness Checks, 54 Harness Test Vectors, and 29 controlled fixtures.


## 2026-07-31 - F-17 proposed Companion_Spec lifecycle disposition correction

- Added the controlled `Companion_Spec_Disposition` field to the authoritative RTM workbook without changing existing CR, NS, TC, DS, IF, REG, lifecycle, or normative-status mappings.
- Classified all 55 references across 47 RTM rows and 10 absent proposed/expanded companion paths as `Planned / Non-Baseline`; the artifacts remain roadmap/backlog items and are not required for AGCP v2.0.0 conformance or for the affected rows to remain Accepted and Complete.
- Added `governance/RTM-1.45-companion-artifact-disposition-validation.json` and regenerated the RTM format/change validation to prove that every Companion_Spec entry has an explicit baseline disposition.
- Refreshed the active OpenAPI migration validation RTM source hash after the controlled workbook change.


## 2026-07-31 — F-16 Canonical State source-resolution terminology correction

- Replaced unqualified “Canonical State reconstruction” wording in `conformance/AGCP-Conformance.md` with `Canonical State resolution` for runtime evaluation.
- Renamed the L3+ test section to `Canonical State Resolution and Replay Reproduction Tests` and qualified replay as reproduction of Canonical State resolution from recorded qualified source versions and applicable ordered Governance Ledger records.
- Corrected negative-test and conformance-failure language so failures concern invalid resolution or invalid replay reproduction rather than reconstruction from recorded history alone.
- Updated `lifecycle/AGCP Governance Lifecycle Model.md` with the same source-resolution and replay qualification.
- Confirmed that remaining repository uses of `reconstruct` are explicitly tied to authoritative sources, source versions, applicable ordered ledger records, or reproduction of an already resolved Canonical State view.


## 2026-07-31 — F-15 traceability-versus-precedence wording correction

- Replaced ambiguous “authoritative chain”/directional NS-to-CR-to-TC wording in the Harness Check Registry with the controlled bidirectional traceability relationship `CR ↔ Core-derived NS identifiers ↔ TC`.
- Clarified that the RTM controls CR/Core-derived-NS/TC relationships, while `test-mapping.json` extends TC traceability to Harness Checks and Test Vectors.
- Stated explicitly that traceability relationships do not alter the CR-first normative precedence model.
- Corrected the remaining ambiguous future-evolution statement in `conformance/README.md` so it cannot be read as reversing normative precedence.
- Refreshed the controlled Governance Compilation and Activation validation record after the Harness Check Registry source changed.


## 2026-07-31 — F-14 retired Human Review Artifact terminology correction

- Replaced active “Human-review artifacts” terminology in `spec/AGCP-Error-Mapping.md` with the controlled `DS-026 Governance Approval Artifact` representation.
- Replaced “Human-review submission” with “Governance Approval Artifact submission” while preserving the mandatory prohibition against submission itself performing execution.
- Preserved `Pending Human Review` solely as the controlled governance outcome and confirmed that remaining `Human Review Artifact` references are explicitly legacy, retired, or historical rather than active representations.
- Refreshed controlled validation records that embed the normative Error Mapping source hash and added active-representation terminology validation.


## 2026-07-31 — F-13 OpenAPI migration validation baseline correction

- Refreshed `api/AGCP-OpenAPI-v2-migration-validation.json` from the stale `RTM-1.44` reference to the active controlled `RTM-1.45` baseline.
- Classified the PASS record explicitly as an active controlled-baseline validation, added the controlled RTM artifact and hash, and revalidated all 122 CR rows and 40 IF-001 mappings.
- Updated `api/AGCP-OPENAPI-V2-MIGRATION-UPDATE.md` to distinguish the historical RTM-1.43-to-RTM-1.44 migration step from the current RTM-1.45 validation state and refreshed its validation metrics.


## 2026-07-31 — F-12 Conformance Specification Markdown fence correction

- Removed the stray closing code fence after Section 2 of `conformance/AGCP-Conformance.md`.
- Restored normal Markdown parsing for Sections 3 and later so normative prose, headings, anchors, tables, and examples render as intended.
- Revalidated all fenced blocks and confirmed that each remaining fence pair encloses only its intended example.


## 2026-07-31 — F-11 Governance Evidence obligation correction in normative Error Mapping

- Replaced the weakened `SHOULD` formulation for Policy Evaluation Module artifact validation failures with a `SHALL` obligation aligned with Core Sections 10.1, 10.3, and 10.8 and Normative Statements NS-10.1-02, NS-10.3-01, and NS-10.8-01.
- Added the same mandatory Governance Evidence rule to Governance Policy artifact validation failures so both governance-artifact registration operations apply the obligation consistently.
- Retained the Core-aligned applicability qualifier: evidence is required where the implementation has sufficient context to associate the failure with a tenant, governed object, or governance artifact.
- Confirmed that `spec/AGCP-Core.docx` and `spec/AGCP Normative Statements.docx` already contain the controlling mandatory language and required no modification.
- Refreshed all controlled validation records that embed the normative Error Mapping source hash and added explicit modal-strength validation.


## 2026-07-31 — F-10 Continuation Integrity and Commit Boundary normative-restatement correction

- Corrected Section 9 of `lifecycle/AGCP Governance Progression Implementation Guide.md` so mandatory Continuation Integrity, risk-based re-evaluation, Governance Realization, Commit Boundary, and non-commit obligations are restated with `SHALL` and `SHALL NOT` language matching the controlled Core.
- Replaced “immediately before governed execution” and the checklist’s “immediately before enforcement” wording with the Core-defined timing, “immediately before commitment.”
- Labeled the corrected section explicitly as a normative restatement that does not create or modify obligations and remains subordinate to the controlling Core and Normative Statements.
- Confirmed that `spec/AGCP-Core.docx` and `spec/AGCP Normative Statements.docx` already contain the controlling mandatory language and required no modification.


## 2026-07-31 — F-09 Governance Compilation and Controlled Activation executable coverage

- Added nine substantive Harness Test Vectors for Governance Configuration, deterministic compilation, constitutional validation and constraint preservation, omission analysis, Governance Self-Protection, atomic Controlled Governance Activation, failure preservation, governed rollback, evidence, lineage, and replay.
- Bound the vectors to `CHECK-GOVERNANCE-COMPILATION-ACTIVATION` and directly mapped them to TC-110, TC-111, TC-112, TC-113, TC-114, TC-117, and TC-122.
- Added a controlled validation record proving that every `MUST` Harness Check has substantive executable coverage and every expected behavior declared by the compilation/activation check is asserted.


## Complete executable IF-001 operation coverage — 2026-07-31

- Added seventeen Harness Test Vectors for the five previously uncovered mandatory IF-001 operations: metadata discovery, Execution Authorization retrieval, Policy Evaluation Module registration, Governance Policy registration, and governance-artifact retrieval.
- Added schema-valid positive coverage for all five operations, declared negative and tenant/Governance-Domain-isolation scenarios where applicable, and equivalent-replay plus conflicting-reuse idempotency scenarios for both governance-artifact registration operations.
- Added five controlled response fixtures for DS-003, DS-005, DS-006, DS-010, and DS-017 and synchronized `fixture-mapping.json` and fixture validation.
- Added `CHECK-HTTP-INTERFACE-CONTRACT`, expanded related Harness Checks, synchronized the Markdown vector mirror, Test Matrix, and all 122 TC mapping records, and increased the controlled catalog to 17 Harness Checks and 45 Harness Test Vectors.
- Added `conformance/AGCP-if001-executable-operation-coverage-validation.json` and expanded the HTTP Interface Specification conformance section to define executable operation-coverage expectations without making harness results an independent conformance authority.
- Confirmed that `api/AGCP-HTTP-Contract.yaml` already defined the ten mandatory operations and required no modification.

## IF-001 human-readable parameter and complete contract parity — 2026-07-31

- Added the required `tenant_id` and `governance_domain_id` query-parameter obligations to Proposal, Execution Authorization, and Governance Evidence retrieval in Sections 5.3, 5.5, and 5.7 of the HTTP Interface Specification.
- Added the required `Idempotency-Key` header and endpoint-plus-tenant idempotency scope to Governance Approval submission and Commit Boundary processing in Sections 5.4 and 5.6.
- Added a normative IF-001 Contract Parity Summary covering all ten operations, including method, path, `operationId`, required parameters, JSON request schema, and complete response-status set.
- Confirmed that `api/AGCP-HTTP-Contract.yaml` already contained the authoritative required parameters and required no modification.
- Regenerated `api/interface-traceability-validation.json` and `api/AGCP-OpenAPI-v2-migration-validation.json` to validate complete Interface Specification/OpenAPI parity rather than operation identities and Error Mapping response sets alone.

## Complete OpenAPI/Error Mapping response-set synchronization — 2026-07-31

- Added HTTP 422 `ErrorResponse` to `getGovernanceEvidence` for incomplete or invalid Governance Evidence.
- Added HTTP 409 idempotency-conflict and HTTP 503 dependency-unavailable `ErrorResponse` declarations to `registerPolicyEvaluationModule` and `registerGovernancePolicy`.
- Preserved the HTTP 404 declarations previously added to `submitGovernanceApproval` and `commitBoundaryProcessing` under F-05.
- Confirmed that `spec/AGCP-Error-Mapping.md` already contained the authoritative status sets and required no textual modification.
- Regenerated `api/interface-traceability-validation.json` and `api/AGCP-OpenAPI-v2-migration-validation.json` to compare complete non-success response sets for every Error-Mapping-governed IF-001 operation, rather than operation identities alone.
- Refreshed dependent harness validation records against the updated IF-001 contract.

## Harness/OpenAPI response-set synchronization — 2026-07-31

- Added HTTP 404 `ErrorResponse` declarations to `submitGovernanceApproval` and `commitBoundaryProcessing` so the selected `HIDE_404` cross-scope disclosure strategy is permitted by IF-001.
- Preserved the authoritative Harness Test Vector expectations: `TV-XTEN-002` and `TV-XTEN-003` continue to allow `403 / TENANT_SCOPE_VIOLATION` under `FORBID_403` and `404 / RESOURCE_NOT_FOUND` under `HIDE_404`.
- Confirmed that `spec/AGCP-Error-Mapping.md` already defines the applicable 404 semantics and required no modification.
- Extended `conformance/AGCP-harness-error-model-validation.json` to validate every primary and setup expected status against the matched OpenAPI operation.
- Refreshed `conformance/AGCP-harness-request-parameter-validation.json` against the updated IF-001 contract.

## Harness error-model synchronization — 2026-07-31

- Corrected `TV-PROP-007` to expect HTTP 422 with `POLICY_NOT_FOUND`, matching the normative Error Mapping and active rejection-code registry.
- Corrected `TV-GET-002` to use `RESOURCE_NOT_FOUND` for its HTTP 404 externally hidden/transient Proposal View outcome.
- Corrected the `HIDE_404` branches of `TV-XTEN-001` through `TV-XTEN-004` to use `RESOURCE_NOT_FOUND`; retained `TENANT_SCOPE_VIOLATION` for the `FORBID_403` branches.
- Synchronized the authoritative YAML harness and Markdown Test Vector mirror.
- Added `conformance/AGCP-harness-error-model-validation.json` as the controlled validation record for all declared harness rejection-code/HTTP-status pairs.
- Confirmed that `spec/AGCP-Error-Mapping.md` and `registries/rejection-code-registry.json` were already correct and required no modification.

## TV-GAPP-004 semantic cryptographic-verification correction — 2026-07-31

- Kept the `TV-GAPP-004` Governance Approval request structurally valid under the IF-001 `GovernanceApprovalRequest` wrapper and DS-026.
- Replaced the schema-invalid `cryptographic_verification.verification_outcome: FAILED` override with the DS-026-required `VERIFIED` value plus schema-valid invalid signature and key-binding material.
- Added an explicit harness cryptographic-verifier hook that independently re-verifies the submitted artifact after schema validation and returns `GOVERNANCE_APPROVAL_INVALID` for the declared signature, key-binding, and artifact-digest-binding failure.
- Preserved the required `Idempotency-Key`, HTTP 422 outcome, rejection code, and no-ledger-append expectation.
- Synchronized the executable YAML and Markdown vector representations.
- Confirmed that `schemas/governance_approval_artifact.json` was already correct and required no modification.

## TV-GAPP-001 DS-013/DS-021 setup correction — 2026-07-31

- Replaced the retired flattened proposal-submission body in the `TV-GAPP-001` setup prestep with the active DS-013 `ProposalSubmitRequest` wrapper.
- Added a complete nested DS-021 `GovernedActionProposal` for the approval-required two-role scenario.
- Preserved the PEC approval-required hooks, expected `Pending Human Review` outcome, and `P_GAPP_001` capture used by the primary Governance Approval request.
- Synchronized the executable YAML and Markdown vector representations.
- Confirmed that `schemas/proposal_submit_request.json` and `schemas/governed_action_proposal.json` were already correct and required no modification.

## Harness IF-001 required-parameter synchronization — 2026-07-31

- Added the required `tenant_id` and `governance_domain_id` query parameters to five GET vectors in both the authoritative YAML harness and its Markdown mirror.
- Added a unique `Idempotency-Key` header to eleven Governance Approval and Commit Boundary POST vectors in both catalogs.
- Added `conformance/AGCP-harness-request-parameter-validation.json` as the controlled record for all 29 primary requests and HTTP setup presteps.
- Verified every request against `api/AGCP-HTTP-Contract.yaml`; no declared vector outcome is preempted by missing path, query, or header parameters.
- The IF-001 OpenAPI contract was already correct and was not modified.

## Conformance traceability and automation relationship model — 2026-07-30

- Added `conformance/AGCP-Conformance-Traceability-and-Automation-Model.md` as the normative control document for conformance-artifact relationship semantics.
- Defined the distinct roles and authority boundaries of CRs, Core-derived NS identifiers, the RTM, Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, assessment results, and profile claims.
- Established that Formal Test Cases remain the authoritative assessment procedures and that harness artifacts automate portions of those procedures without independently creating requirements or granting conformance.
- Defined controlled many-to-many mappings, no-dedicated-vector dispositions, conformance-level semantics, pass/fail authority, evidence attribution, and machine-readable synchronization rules.
- Added discoverability references in the root architecture and README, the conformance package, the Conformance Test Suite, the Harness Check Registry, the Test Matrix, and the conformance manifest.
- No CR, Core requirement, Companion Specification obligation, RTM mapping, Test Case criterion, schema, interface, registry, Harness Check, or Harness Test Vector was changed.

## Schema Catalog reverse-dependency synchronization — 2026-07-30

- Advanced the Schema Catalog to Version 1.0.44.
- Recomputed every active `dependent_schemas` list from the inverse of the controlled `schema_dependencies` graph.
- Added missing reverse dependencies for DS-001, DS-007, DS-020, DS-021, DS-023, DS-024, DS-026, DS-028, DS-032, DS-033, DS-038, and DS-041.
- Added catalog-wide reverse-dependency parity validation covering all 43 active schema entries.
- No schema content, schema identifier, schema hash, OpenAPI contract, normative requirement, RTM mapping, or RTM workbook content changed.

## Schema Catalog RTM/CR mapping synchronization — 2026-07-30

- Advanced the Schema Catalog to Version 1.0.43.
- Synchronized the RTM and CR mappings for DS-015, DS-017, DS-021, DS-028, DS-037, and DS-040 with the authoritative RTM-1.45 `DS_ID` assignments.
- Added RTM-to-catalog parity validation covering all 43 active schema entries.
- No schema content, schema identifier, schema hash, OpenAPI contract, normative requirement, or RTM workbook content changed.

## Duplicate validation-payload cleanup — 2026-07-30

- Retained DS-specific validation records for DS-032, DS-033, and DS-034 in the authoritative `schemas/` location.
- Removed the byte-identical redundant copies from `schemas/catalog/`.
- Retained the catalog-wide validation record at `schemas/catalog/schema-catalog-validation.json`, as referenced by `schemas/README.md`.
- Removed the byte-identical redundant root-level `schemas/schema-catalog-validation.json` copy.
- No schema content, catalog assignment, catalog hash, OpenAPI contract, fixture, or normative mapping changed.

## DS-013 obsolete metadata-field removal — 2026-07-30

- Removed the deprecated top-level `metadata` compatibility property from `schemas/proposal_submit_request.json`.
- Established `extensions` as the sole namespace-qualified extension container for DS-013.
- Updated the DS-013 schema-catalog hash and advanced the schema catalog to Version 1.0.42.
- Confirmed that payloads containing the removed top-level member are rejected because DS-013 prohibits additional properties.

## DS-016 retirement — 2026-07-30

- Removed `schemas/human_review_artifact.json` from the active AGCP v2.0 schema set.
- Retained DS-016 only as a permanently retired, superseded identifier in the Schema Catalog.
- Established DS-026 `governance_approval_artifact.json` as the sole active approval and adjudication schema.
- Removed OpenAPI, reference-implementation, and conformance-harness compatibility handling.


**Status:** Informational  
**Current Published Normative Release:** v2.0.0

---

# Purpose

This document records the published release history of the Artificial Intelligence Governance Control Plane (AGCP).

Each published release identifies the normative specification set, schemas, registries, conformance artifacts, and supporting documentation applicable to that release.

Versioning follows Semantic Versioning (MAJOR.MINOR.PATCH).

The governing rules for versioning, compatibility, and release management are defined in:

`governance/AGCP-Versioning.md`

---

# Version 2.0.0

**Release Status:** Current Published Normative Release

## Summary

Version 2.0.0 represents the current published normative AGCP release.

This release introduces the governance progression architecture centered on Proposal Qualification, Governance Decision Function, governed approval and adjudication, Execution Authorization or another eligible nonterminal state, applicable pre-commit Continuation Integrity, Governance Realization and final Commit-Bound Admissibility, and Policy Enforcement Point/Commit Boundary processing. Governance Evidence operates as a cross-cutting supporting service throughout applicable governance-significant processing. The release also establishes the Append-Only Governance Ledger and Canonical State deterministically resolved from qualified authoritative governance sources, with the ledger authoritative for recorded governance events, event ordering, and Derived Lifecycle State.

## Major Highlights

- Governance progression model
- Canonical State architecture
- Ordered Append-Only Governance Ledger
- Governance Evidence framework
- Updated conformance architecture
- Repository-wide documentation modernization

---

# Version 1.0.3

**Release Status:** Public Normative Release

## Summary

Version 1.0.3 represents the mature public AGCP 1.x specification series.

This release stabilized the core governance architecture and provided the basis for subsequent architectural evolution incorporated into Version 2.0.0.

---

# Version 0.9.0

**Release Status:** Initial Public Review

## Summary

Version 0.9.0 was the initial public review release.

It established the initial public specification set and solicited implementation and community feedback that informed the Version 1.x and Version 2.x releases.

---

# Changelog Format

Future releases SHOULD include:

- Version
- Release Date
- Release Status
- Summary
- Normative Specification Changes
- Schema Changes
- Registry Changes
- Conformance Changes
- Documentation Changes
- Security Changes
- Compatibility Impact
- Migration Guidance (if applicable)

---

# Example Future Entry

## Version 2.1.0

**Release Status:** Minor Release

### Summary

Adds backward-compatible governance capabilities and clarifications.

### Normative Specification Changes

- Clarified Governance Decision Function semantics.
- Expanded Human Review guidance.

### Schema Changes

- Added optional governance metadata fields.

### Registry Changes

- Added new governance evidence type.

### Conformance Changes

- Added new Conformance Requirements and Test Cases.

### Documentation Changes

- Expanded implementation guidance.

### Compatibility Impact

Backward compatible within the Version 2 MAJOR release.

### Migration Guidance

Existing Version 2.0.x implementations remain compatible without modification.
