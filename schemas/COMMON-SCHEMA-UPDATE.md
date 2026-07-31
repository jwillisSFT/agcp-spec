# AGCP `common.json` Update Report

**Artifact:** `schemas/common.json`  
**DS identifier:** `DS-001`  
**Schema dialect:** JSON Schema Draft 2020-12  
**Baseline:** AGCP v2.0  
**Updated:** 2026-07-29

## Result

- Definitions before update: **33**
- Definitions after update: **141**
- Existing definition names retained: **33**
- New definitions added: **108**
- Definition names removed: **0**
- Existing definitions enhanced: **32**

No existing `$defs` name used by the other implemented schemas was removed. The remaining 19 implemented schemas continue to resolve all references to `common.json`.

## Principal changes

- Established stable identifier types for Proposal Identity, Governance Version, Canonical State, authority, evidence, receipts, refusals, lifecycle, ledger events, composite governance, enforcement, and validation results.
- Added algorithm-explicit content digests while retaining the legacy `hash_hex` type.
- Expanded Canonical State, Governance Context, Authority Lineage, Governance Configuration, policy, decision, authorization, evidence, receipt, refusal, approval, lifecycle, ledger, bind-set, dependency-graph, and enforcement references.
- Added State Qualification and Evidence Qualification dimensions and result structures.
- Added proposal-specific governance binding and Governance Binding Validation structures.
- Added Derived Lifecycle State, terminality, Continuation Integrity, Risk-Based Re-Evaluation, Continuation Recovery-related outcomes, partial quorum, and approval types.
- Added Admissible Set, Deterministic Adjudication, Bind Set, dependency, coupling, Partial-Bind Admissibility, and Resulting-State Validation types.
- Added Policy Enforcement Point and enforcement-result types.
- Added Governance Compilation and Controlled Governance Activation references.
- Added `INACTIVE` to the Tenant state vocabulary.
- Corrected pipeline vocabulary so Continuation Integrity is represented before final Commit-Bound Admissibility and added Governance Realization, Policy Enforcement Point, Governance Compilation, and Controlled Governance Activation.
- Retained legacy continuation values for compatibility but marked them for migration to the v2.0 pre-commit continuation vocabulary.

## Compatibility

### Reference compatibility

All 33 previously available definition names remain present. Existing `$ref` paths therefore continue to resolve.

### Instance compatibility considerations

Identifier and rejection-code types now include lexical patterns. Existing conformant identifier forms using letters, numbers, period, underscore, colon, slash, at-sign, plus, or hyphen remain valid; identifiers containing spaces or ungoverned punctuation will require normalization. This is intentional because stable governance identifiers must be machine-safe and transport-independent.

Existing reference objects retain their prior minimum required fields. Newly added binding, version, qualification, digest, target, lifecycle, and attribution fields are optional until the dependent schemas are revised to require them.

## New definitions by category

### Identifiers and lexical types

- `activation_id`
- `adjudication_id`
- `admissible_set_id`
- `approval_artifact_id`
- `authority_lineage_id`
- `authority_rederivation_result_id`
- `bind_set_id`
- `canonical_state_id`
- `compiled_artifact_id`
- `constraint_id`
- `continuation_result_id`
- `dependency_graph_id`
- `enforcement_context_id`
- `evaluation_id`
- `evidence_id`
- `governance_configuration_id`
- `governance_context_id`
- `governance_decision_id`
- `governance_receipt_id`
- `governance_version_id`
- `hash_algorithm_enum`
- `identifier`
- `invariant_id`
- `ledger_event_id`
- `ledger_id`
- `lifecycle_record_id`
- `lineage_id`
- `partial_bind_result_id`
- `policy_enforcement_point_id`
- `refusal_record_id`
- `registry_id`
- `resulting_state_validation_id`
- `risk_re_evaluation_id`
- `sequence_number`
- `target_id`
- `version_string`

### Integrity, attribution, and provenance

- `attribution`
- `content_digest`

### Governance states and outcomes

- `activation_outcome_enum`
- `adjudication_outcome_enum`
- `admissibility_outcome_enum`
- `approval_decision_enum`
- `authority_rederivation_outcome_enum`
- `binding_validation_outcome_enum`
- `composite_coupling_semantics_enum`
- `continuation_integrity_outcome_enum`
- `dependency_type_enum`
- `derived_lifecycle_state`
- `derived_lifecycle_state_base_enum`
- `enforcement_outcome_enum`
- `governance_processing_function_enum`
- `hash_algorithm_enum`
- `overall_qualification_outcome_enum`
- `qualification_status_enum`
- `quorum_status_enum`
- `resulting_state_validation_outcome_enum`
- `risk_re_evaluation_disposition_enum`
- `terminality_enum`

### Canonical governance references

- `admissible_set_ref`
- `authoritative_source_ref`
- `authority_rederivation_result_ref`
- `bind_set_ref`
- `compiled_governance_artifact_ref`
- `continuation_integrity_result_ref`
- `controlled_governance_activation_ref`
- `dependency_ref`
- `deterministic_adjudication_result_ref`
- `enforcement_context_ref`
- `evidence_qualification_result_ref`
- `execution_authorization_ref`
- `governance_approval_artifact_ref`
- `governance_decision_ref`
- `governance_dependency_graph_ref`
- `governance_evidence_ref`
- `governance_lifecycle_record_ref`
- `governance_receipt_ref`
- `governance_version_ref`
- `ledger_event_ref`
- `lifecycle_state_ref`
- `mission_task_lineage_ref`
- `partial_bind_result_ref`
- `qualified_evidence_ref`
- `refusal_record_ref`
- `resulting_state_validation_result_ref`
- `state_qualification_result_ref`
- `target_ref`

### Qualification and governance basis

- `authoritative_source_ref`
- `evaluation_horizon`
- `evidence_qualification_dimensions`
- `evidence_qualification_result`
- `evidence_qualification_result_ref`
- `governance_basis`
- `governance_scope`
- `overall_qualification_outcome_enum`
- `qualification_status_enum`
- `state_qualification_dimensions`
- `state_qualification_result`
- `state_qualification_result_ref`

### Binding, commit, and enforcement

- `enforcement_result`
- `governance_binding`
- `governance_binding_validation_result`
- `target_ref`

### Composite governance

- `admissible_set_ref`
- `dependency_ref`
- `deterministic_adjudication_result`
- `partial_bind_result`
- `resulting_state_validation_result`

### Lifecycle, continuation, and re-evaluation

- `authority_rederivation_result`
- `continuation_integrity_result`
- `mission_task_lineage_ref`
- `proposal_identity`
- `quorum_requirement`
- `quorum_state`
- `risk_based_re_evaluation_result`

### Additional shared structures

- `constraint_ref`
- `invariant_ref`
- `ledger_position`
- `validity_window`

## Validation

- JSON parse: **PASS**
- Draft 2020-12 metaschema validation for all 20 implemented schemas: **PASS**
- Resolution of all 225 existing `common.json` reference occurrences: **PASS**
- Internal `$defs` reference resolution: **PASS**
- Rejection-code registry compatibility: **PASS**
- Positive sample validation for new foundational types: **PASS**
- Negative test rejection: **PASS**
- Catalog hash consistency: **PASS**
- ARM and NS traceability identifier existence: **PASS**

## Files updated

- `schemas/common.json`
- `schemas/README.md`
- `schemas/SCHEMA-CATALOG.md`
- `schemas/catalog/schema-catalog.json`
- `schemas/catalog/schema-catalog.csv`
- `schemas/catalog/schema-catalog-validation.json`
- `schemas/catalog/common-schema-validation.json`

## Normative basis

- `spec/Architecture Reference Model.docx`
- `spec/AGCP-Core.docx`, especially Sections 4, 6.6A, 7.6A, 8.6A, 9.6A-B, 10.8A, 13.6A-C, 15.6A-B, and 16.6A
- `spec/AGCP Normative Statements.docx`
- `spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv`

