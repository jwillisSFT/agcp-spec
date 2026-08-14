# AGCP Data Schema Catalog

- Catalog ID: `DS-CATALOG-1.0`
- Catalog version: `1.0.50`
- Specification version: `v2.0.5`
- Publication status: `CURRENT`
- Artifact lifecycle state: `CURRENT`
- Repository release target: `v2.0.5` (`PUBLIC_REVIEW_CONTROLLED_BASELINE`)
- Controlling published baseline: `v2.0.5` (`PUBLIC_REVIEW_CONTROLLED_BASELINE`)
- Baseline date: `2026-08-05`
- Last modified: `2026-08-03`

## Active Implemented Schemas

| DS ID | Filename | Category | Dependencies |
|---|---|---|---|
| `DS-001` | `common.json` | Common Infrastructure | DS-006; DS-007; DS-008; DS-020; DS-040; DS-041; DS-043 |
| `DS-002` | `error_response.json` | Common Infrastructure | DS-001; DS-028 |
| `DS-003` | `meta_response.json` | Common Infrastructure | DS-001; DS-020; DS-044 |
| `DS-004` | `tenant.json` | Common Infrastructure | DS-001; DS-006; DS-020; DS-024; DS-026; DS-040; DS-041; DS-043; DS-044 |
| `DS-005` | `policy_evaluation_module_artifact.json` | Governance Artifact | DS-001; DS-006; DS-020; DS-041; DS-042; DS-043; DS-044 |
| `DS-006` | `policy_artifact.json` | Governance Artifact | DS-001; DS-005; DS-007; DS-008; DS-020; DS-026; DS-038; DS-041; DS-042; DS-043; DS-044 |
| `DS-007` | `constraint_artifact.json` | Governance Artifact | DS-001; DS-005; DS-006; DS-020; DS-026; DS-041; DS-042; DS-043; DS-044 |
| `DS-008` | `invariant_definition.json` | Governance Artifact | DS-001; DS-005; DS-006; DS-020; DS-026; DS-041; DS-042; DS-043; DS-044 |
| `DS-009` | `exception_artifact.json` | Governance Artifact | DS-001; DS-005; DS-006; DS-007; DS-008; DS-020; DS-024; DS-025; DS-026; DS-041; DS-042; DS-043 |
| `DS-010` | `governance_artifact_view.json` | Governance Artifact | DS-001; DS-020; DS-040; DS-041; DS-042; DS-043 |
| `DS-011` | `constraint_evaluation.json` | Evaluation Result | DS-001; DS-006; DS-007; DS-020; DS-021; DS-023; DS-024; DS-028; DS-032; DS-033; DS-038; DS-041 |
| `DS-012` | `invariant_evaluation.json` | Evaluation Result | DS-001; DS-006; DS-008; DS-020; DS-021; DS-023; DS-024; DS-026; DS-028; DS-032; DS-033; DS-038; DS-041 |
| `DS-013` | `proposal_submit_request.json` | Governance Workflow | DS-001; DS-021 |
| `DS-014` | `proposal_view.json` | Governance Workflow | DS-001; DS-015; DS-017; DS-018; DS-019; DS-020; DS-021; DS-022; DS-023; DS-024; DS-027; DS-028; DS-029; DS-030; DS-031; DS-034; DS-035; DS-036; DS-037; DS-038; DS-039 |
| `DS-015` | `governance_decision_result.json` | Governance Workflow | DS-001; DS-006; DS-009; DS-011; DS-012; DS-020; DS-021; DS-022; DS-023; DS-024; DS-026; DS-027; DS-028; DS-032; DS-033; DS-041 |
| `DS-017` | `execution_authorization_view.json` | Governance Workflow | DS-001; DS-006; DS-015; DS-019; DS-020; DS-021; DS-022; DS-023; DS-024; DS-026; DS-027; DS-032; DS-033; DS-038; DS-041 |
| `DS-018` | `commit_boundary_request.json` | Governance Workflow | DS-001; DS-015; DS-017; DS-021; DS-029; DS-030; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036; DS-037; DS-039 |
| `DS-019` | `commit_boundary_result.json` | Governance Workflow | DS-001; DS-015; DS-017; DS-018; DS-020; DS-021; DS-027; DS-028; DS-029; DS-030; DS-031; DS-034; DS-035; DS-036; DS-037; DS-038 |
| `DS-020` | `governance_evidence.json` | Governance Workflow | DS-001; DS-006; DS-009; DS-015; DS-017; DS-018; DS-019; DS-021; DS-022; DS-023; DS-024; DS-026; DS-027; DS-028; DS-029; DS-030; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036; DS-037; DS-038; DS-039; DS-040 |
| `DS-021` | `governed_action_proposal.json` | Canonical Governance Object | DS-001; DS-006; DS-022; DS-024; DS-035; DS-036 |
| `DS-022` | `governance_context_envelope.json` | Canonical Governance Object | DS-001; DS-006; DS-015; DS-017; DS-020; DS-024; DS-025; DS-026; DS-028; DS-030; DS-033; DS-036; DS-037; DS-038; DS-041 |
| `DS-023` | `canonical_state.json` | Canonical Governance Object | DS-001; DS-020; DS-032; DS-033; DS-038; DS-040 |
| `DS-024` | `authority_lineage.json` | Authority | DS-001; DS-006; DS-017; DS-020; DS-025; DS-026 |
| `DS-025` | `delegation_artifact.json` | Authority | DS-001; DS-006; DS-007; DS-020; DS-024 |
| `DS-026` | `governance_approval_artifact.json` | Approval and Adjudication | DS-001; DS-006; DS-007; DS-015; DS-020; DS-033; DS-038 |
| `DS-027` | `governance_receipt.json` | Evidence and Provenance | DS-001; DS-015; DS-017; DS-020; DS-026; DS-029; DS-030; DS-031; DS-033; DS-037; DS-038; DS-039; DS-040 |
| `DS-028` | `refusal_record.json` | Evidence and Provenance | DS-001; DS-007; DS-008; DS-015; DS-020; DS-026; DS-027; DS-029; DS-030; DS-032; DS-033; DS-038; DS-040 |
| `DS-029` | `enforcement_context.json` | Commit and Enforcement | DS-001; DS-006; DS-015; DS-017; DS-020; DS-024; DS-026; DS-030; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036; DS-037; DS-038; DS-039; DS-041 |
| `DS-030` | `governance_binding_validation_result.json` | Commit and Enforcement | DS-001; DS-006; DS-015; DS-017; DS-020; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036; DS-037; DS-038; DS-041 |
| `DS-031` | `resulting_state_validation_result.json` | Commit and Enforcement | DS-001; DS-006; DS-032; DS-033; DS-035; DS-036; DS-040 |
| `DS-032` | `state_qualification_result.json` | Qualification | DS-001; DS-020 |
| `DS-033` | `evidence_qualification_result.json` | Qualification | DS-001; DS-006; DS-020; DS-024 |
| `DS-034` | `authority_rederivation_result.json` | Authority | DS-001; DS-006; DS-007; DS-015; DS-017; DS-020; DS-024; DS-025; DS-026; DS-032; DS-033; DS-038; DS-041 |
| `DS-035` | `bind_set.json` | Composite Governance | DS-001; DS-006; DS-036 |
| `DS-036` | `governance_dependency_graph.json` | Composite Governance | DS-001; DS-006; DS-007; DS-008; DS-020; DS-024; DS-035; DS-038 |
| `DS-037` | `deterministic_adjudication_result.json` | Composite Governance | DS-001; DS-006; DS-015; DS-017; DS-020; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036 |
| `DS-038` | `governance_lifecycle_record.json` | Lifecycle and Continuation | DS-001; DS-006; DS-015; DS-017; DS-019; DS-020; DS-021; DS-026; DS-027; DS-028; DS-039; DS-040; DS-041 |
| `DS-039` | `continuation_integrity_result.json` | Lifecycle and Continuation | DS-001; DS-006; DS-017; DS-020; DS-021; DS-022; DS-023; DS-024; DS-027; DS-028; DS-030; DS-032; DS-033; DS-034; DS-036; DS-038; DS-040; DS-041 |
| `DS-040` | `governance_ledger_event.json` | Evidence and Provenance | DS-001; DS-006; DS-007; DS-008; DS-015; DS-017; DS-018; DS-019; DS-020; DS-021; DS-022; DS-023; DS-024; DS-026; DS-027; DS-028; DS-029; DS-030; DS-031; DS-032; DS-033; DS-034; DS-035; DS-036; DS-037; DS-038; DS-039; DS-041; DS-042; DS-043 |
| `DS-041` | `governance_configuration.json` | Governance Compilation | DS-001; DS-006; DS-020; DS-026; DS-038; DS-043 |
| `DS-042` | `compiled_governance_artifact.json` | Governance Compilation | DS-001; DS-007; DS-008; DS-020; DS-026; DS-041; DS-044 |
| `DS-043` | `controlled_governance_activation.json` | Governance Compilation | DS-001; DS-020; DS-026; DS-040; DS-041; DS-042 |
| `DS-044` | `registry_document.schema.json` | Registry Validation | DS-001 |
| `DS-045` | `governance_approval_submission.json` | Approval and Adjudication | DS-001; DS-006; DS-026 |

## Retired DS Identifiers

| DS ID | Historical filename | Superseded by | Retirement status |
|---|---|---|---|
| `DS-016` | `human_review_artifact.json` | `DS-026` | Permanently retired; identifier reserved; no active schema file |

## Traceability Closure

- RTM dataset: `RTM-1.46`
- DS mappings: **122 assigned + 0 explicit N/A = 122/122 dispositioned**
- IF mappings: **84 assigned + 38 explicit N/A = 122/122 dispositioned**
- REG mappings: **117 assigned + 5 explicit N/A = 122/122 dispositioned**
- Registry entries with permanent IDs and direct ARM/NS/CR references: **94**
- Catalog RTM/CR mappings matching authoritative RTM-1.46 DS assignments: **44/44 active schemas**
- Corrected catalog entries in Version 1.0.43: **DS-015, DS-017, DS-021, DS-028, DS-037, and DS-040**
- Reverse dependency parity in Version 1.0.44: **44/44 active schemas**; corrected entries: **DS-001, DS-007, DS-020, DS-021, DS-023, DS-024, DS-026, DS-028, DS-032, DS-033, DS-038, and DS-041**.

## Catalog Integrity

The machine-readable catalog records canonical schema identifiers, lifecycle state, traceability, dependencies, repository paths, and SHA-256 content hashes for the active controlled schema set. Retired identifiers are maintained separately as historical namespace records and are excluded from active schema validation and release manifests.

## DS-001 Provenance Wire Contract

The `provenance` definition in `common.json` is the machine-readable representation of the normative AGCP Provenance Wire Format. It requires top-level `signer`, `kid`, `alg`, `signed_at`, `nonce`, `scope`, and detached `signature`, permits optional `expires_at`, rejects undeclared fields, and is explicitly mapped to CR-005 and IF-001.

## P1-12 algorithm-specific digest enforcement

Catalog version 1.0.50 records the corrected DS-001 hash and direct traceability to CR-042, CR-052, CR-064, and CR-066. Dependent schemas inherit the exact algorithm/output-length and lowercase-hexadecimal contract from DS-001.
