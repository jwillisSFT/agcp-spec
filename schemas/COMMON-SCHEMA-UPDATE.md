# AGCP `common.json` Controlled-Baseline Update Report

**Artifact:** `schemas/common.json`  
**DS identifier:** `DS-001`  
**Schema dialect:** JSON Schema Draft 2020-12  
**Specification baseline:** AGCP v2.0.0  
**Schema Catalog version:** `1.0.44`  
**Updated:** 2026-07-31

---

## 1. Purpose

This report documents the current controlled-baseline state of `schemas/common.json` and replaces earlier intermediate update metrics that no longer describe the final AGCP v2.0.0 schema package.

`DS-001` is the shared definitions library for the active AGCP v2.0.0 schema set. It contains only definitions that are directly referenced by active schemas or are transitively required by other definitions in `common.json`.

Canonical domain objects, artifact schemas, result schemas, and registry documents remain owned by their assigned DS schemas. `common.json` does not serve as a compatibility-alias library and does not supersede those assigned schemas.

---

## 2. Controlled-Baseline Result

| Measure | Current result |
|---|---:|
| Active cataloged schemas | 43 |
| Definitions in `common.json` | 62 |
| Definitions directly referenced by active dependent schemas | 55 |
| Definitions used transitively through internal `common.json` references | 7 additional definitions |
| Total reachable definitions | 62 |
| Unused definitions | 0 |
| External `common.json#/$defs/...` reference occurrences | 1,890 |
| Internal `#/$defs/...` reference occurrences | 98 |
| Retired obsolete definition | `pass_fail_enum` |
| Obsolete references to `pass_fail_enum` | 0 |
| Catalog SHA-256 match | PASS |

The current `common.json` contains 62 definitions. Fifty-five are referenced directly by one or more of the 42 dependent active schemas. The remaining seven are referenced internally by shared structures and are therefore transitively required. All 62 definitions are reachable from the active schema set.

---

## 3. Clarification of Earlier Metrics

An earlier version of this report stated that `common.json` contained 141 definitions and that 108 definitions had been added. Those figures described an intermediate expansion and are not valid for the final controlled AGCP v2.0.0 baseline.

During baseline normalization:

- canonical object and result ownership was returned to the applicable DS schemas;
- backward-compatibility aliases were removed;
- unused shared definitions were pruned;
- Governance Ledger identifiers and event structures remained owned by DS-040;
- `pass_fail_enum` was retired; and
- `common.json` was reduced to the shared definitions reachable from the active schema set.

The authoritative current count is therefore **62**, not 141.

---

## 4. Principal Controlled-Baseline Changes

The controlled v2.0.0 `common.json`:

- establishes stable, machine-safe identifiers for proposals, actions, tenants, Governance Domains, decisions, evidence, authorization, Canonical State, authority, receipts, refusals, approvals, enforcement, versions, targets, evaluations, re-evaluation, and lineage;
- provides common timestamp, URI, version, sequence, digest, and rejection-code types;
- provides outcome and status vocabularies for proposal qualification, governance evaluation, execution authorization, commitment, artifact lifecycle, qualification, quorum, composite coupling, and risk-based re-evaluation;
- provides integrity, signature, accountable-principal, attribution, provenance, and validity structures;
- provides common governance-scope, evaluation-horizon, target, authoritative-source, governance-version, Canonical State, authority-lineage, Governance Context, evidence, receipt, and qualification-result references;
- provides Proposal Identity, mission/task lineage, quorum, governance-basis, and Risk-Based Re-Evaluation structures;
- represents Continuation Integrity before final Commit-Bound Admissibility in the governance-processing vocabulary;
- includes Governance Realization, Policy Enforcement Point, Governance Compilation, and Controlled Governance Activation in the governance-processing vocabulary;
- retains `hash_hex` only as a legacy shared digest scalar while providing algorithm-explicit `content_digest`; and
- excludes obsolete compatibility aliases and the retired `pass_fail_enum` definition.

---

## 5. Definition Inventory

### 5.1 Stable identifiers and scalar types

- `identifier`
- `tenant_id`
- `governance_domain_id`
- `proposal_id`
- `action_id`
- `authorization_id`
- `governance_decision_id`
- `governance_evidence_id`
- `artifact_id`
- `governance_context_id`
- `canonical_state_id`
- `authority_lineage_id`
- `governance_version_id`
- `governance_receipt_id`
- `refusal_record_id`
- `approval_artifact_id`
- `enforcement_context_id`
- `risk_re_evaluation_id`
- `evaluation_id`
- `target_id`
- `policy_enforcement_point_id`
- `lineage_id`
- `timestamp_rfc3339`
- `uri`
- `version_string`
- `sequence_number`
- `hash_hex`
- `rejection_code`

### 5.2 Controlled enumerations

- `hash_algorithm_enum`
- `qualification_outcome_enum`
- `governance_outcome_enum`
- `execution_authorization_outcome_enum`
- `commit_boundary_outcome_enum`
- `governance_artifact_status_enum`
- `governance_pipeline_stage_enum`
- `overall_qualification_outcome_enum`
- `quorum_status_enum`
- `composite_coupling_semantics_enum`
- `risk_re_evaluation_disposition_enum`

### 5.3 Integrity, attribution, and provenance structures

- `content_digest`
- `signature`
- `principal`
- `attribution`
- `provenance`

### 5.4 Scope, horizon, and canonical reference structures

- `validity_window`
- `evaluation_horizon`
- `governance_scope`
- `target_ref`
- `authoritative_source_ref`
- `governance_version_ref`
- `state_qualification_result_ref`
- `evidence_qualification_result_ref`
- `canonical_state_ref`
- `authority_lineage_ref`
- `governance_context_ref`
- `qualified_evidence_ref`
- `governance_receipt_ref`

### 5.5 Proposal, lifecycle, quorum, and governance-basis structures

- `proposal_identity`
- `mission_task_lineage_ref`
- `quorum_requirement`
- `governance_basis`
- `risk_based_re_evaluation_result`

---

## 6. Compatibility and Ownership Rules

### 6.1 Reference compatibility

All `$ref` values used by the 43 active cataloged schemas resolve against the controlled schema package. No active schema references the retired `pass_fail_enum` definition.

The 62 definitions in `common.json` are sufficient for the current active schema set. A definition should not be added solely to preserve an obsolete v1 or intermediate-v2 reference.

### 6.2 Instance compatibility considerations

Identifier definitions apply machine-safe lexical patterns. Existing identifiers composed of letters, numbers, period, underscore, colon, slash, at-sign, plus, or hyphen remain valid when they satisfy the applicable length limits. Identifiers containing spaces or uncontrolled punctuation require normalization.

`hash_hex` remains available for schemas that require a legacy hexadecimal digest scalar. New or revised structures should use `content_digest` when the digest algorithm must be explicit.

### 6.3 DS ownership boundaries

Shared scalar, enumeration, integrity, attribution, provenance, scope, and reference structures belong in DS-001 when they are reused across the active schema set.

Canonical domain objects and specialized results remain owned by their assigned DS schemas, including:

- Canonical State — DS-023;
- Authority Lineage — DS-024;
- Governance Approval Artifact — DS-026;
- Governance Receipt — DS-027;
- Refusal Record — DS-028;
- Enforcement Context — DS-029;
- Governance Binding Validation Result — DS-030;
- Resulting-State Validation Result — DS-031;
- State Qualification Result — DS-032;
- Evidence Qualification Result — DS-033;
- Authority Re-Derivation Result — DS-034;
- Bind Set — DS-035;
- Governance Dependency Graph — DS-036;
- Deterministic Adjudication Result — DS-037;
- Governance Lifecycle Record — DS-038;
- Continuation Integrity Result — DS-039;
- Governance Ledger Event — DS-040;
- Governance Configuration — DS-041;
- Compiled Governance Artifact — DS-042; and
- Controlled Governance Activation — DS-043.

---

## 7. Validation Results

The controlled AGCP v2.0.0 schema package produced the following results:

- JSON parse of `schemas/common.json`: **PASS**
- Draft 2020-12 metaschema validation for all 43 active cataloged schemas: **PASS**
- Resolution of 1,890 external `common.json#/$defs/...` references: **PASS**
- Resolution of 98 internal `#/$defs/...` references: **PASS**
- Reachability of all 62 definitions: **PASS**
- Unused-definition check: **PASS — 0 unused definitions**
- Obsolete `pass_fail_enum` reference check: **PASS — 0 references**
- Cataloged DS-001 SHA-256 comparison: **PASS**
- Schema Catalog dependency consistency: **PASS**

The authoritative validation record is:

```text
schemas/common-schema-validation.json
```

The validation record shall report:

```json
{
  "status": "PASS",
  "validated_at": "2026-07-30",
  "definition_count": 62,
  "used_definition_count": 62,
  "unused_definitions": [],
  "retired_definition": "pass_fail_enum",
  "retired_definition_absent": true,
  "obsolete_references": []
}
```

---

## 8. Validation-File Placement

Schema-specific and artifact-specific validation JSON files are stored under:

```text
schemas/
```

The `schemas/catalog/` directory is reserved for the Schema Catalog dataset and its catalog-level validation artifacts.

Accordingly:

- `schemas/common-schema-validation.json` is the authoritative DS-001 validation report;
- no duplicate `common-schema-validation.json` shall remain under `schemas/catalog/`; and
- `schemas/catalog/schema-catalog-validation.json` remains under `schemas/catalog/` because it validates the catalog itself.

---

## 9. Files Updated or Synchronized

The DS-001 update and baseline normalization affect or synchronize the following files:

- `schemas/common.json`
- `schemas/common-schema-validation.json`
- `schemas/README.md`
- `schemas/SCHEMA-CATALOG.md`
- `schemas/catalog/schema-catalog.json`
- `schemas/catalog/schema-catalog.csv`
- `schemas/catalog/schema-catalog-validation.json`

No duplicate DS-001 validation report is retained in `schemas/catalog/`.

---

## 10. Normative and Architectural Basis

The shared definitions and ownership boundaries are aligned with:

- `spec/Architecture Reference Model.docx`;
- `spec/AGCP-Core.docx`, especially Sections 4, 6.6A, 7.6A, 8.6A, 9.6A-B, 10.8A, 13.6A-C, 15.6A-B, and 16.6A;
- `spec/AGCP Normative Statements.docx`;
- `spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv`;
- `spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx`; and
- `schemas/catalog/schema-catalog.json`.

---

## 11. Controlled-Baseline Conclusion

`schemas/common.json` is internally consistent with the active AGCP v2.0.0 schema set and the Schema Catalog. It contains 62 reachable shared definitions, all active references resolve, no definitions are unused, the obsolete `pass_fail_enum` is absent, and the cataloged SHA-256 hash matches the deployed file.

The earlier 141-definition update metrics are superseded by this controlled-baseline report.
