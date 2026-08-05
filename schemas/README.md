# AGCP JSON Schemas

This directory contains the authoritative JSON Schema Draft 2020-12 definitions for the AGCP v2.0.1 schema set, together with the controlled Data Schema Catalog, validation records, implementation reports, and schema examples.

## Current Release Status

- AGCP specification version: `v2.0.1`
- Schema Catalog identifier: `DS-CATALOG-1.0`
- Schema Catalog version: `1.0.50`
- Catalog publication status: `CURRENT`
- Artifact lifecycle state: `CURRENT`
- Repository release target: `v2.0.1` (`UNRELEASED_ACCUMULATED_CORRECTION_SET`)
- Controlling published baseline: `v2.0.0` (`PUBLIC_REVIEW_CONTROLLED_BASELINE`)
- Baseline date: `2026-07-30`
- Active implemented schemas: **44**
- Permanently assigned DS identifiers: **45** (`DS-001` through `DS-045`)
- Retired DS identifiers: **1**
- Proposed or reserved schemas: **0**
- Registry payloads duplicated under `schemas/`: **0**

The completed namespace therefore consists of **44 active schemas plus the permanently retired DS-016 identifier**. DS identifiers are stable and SHALL NOT be reassigned. Schema content versions are governed by repository releases and catalog hashes.

## Authoritative Catalog

- Human-readable catalog: [`SCHEMA-CATALOG.md`](SCHEMA-CATALOG.md)
- Machine-readable catalog: [`catalog/schema-catalog.json`](catalog/schema-catalog.json)
- Tabular catalog: [`catalog/schema-catalog.csv`](catalog/schema-catalog.csv)
- Catalog validation: [`catalog/schema-catalog-validation.json`](catalog/schema-catalog-validation.json)
- RTM/CR mapping parity: all 44 active catalog entries match the authoritative RTM-1.46 `DS_ID` assignments.
- Reverse dependency parity: all 44 active `dependent_schemas` lists match the inverse of the active `schema_dependencies` graph.

## Active Implemented Schema Assignments

| DS ID | Schema | Category |
|---|---|---|
| `DS-001` | [`common.json`](common.json) | Common Infrastructure |
| `DS-002` | [`error_response.json`](error_response.json) | Common Infrastructure |
| `DS-003` | [`meta_response.json`](meta_response.json) | Common Infrastructure |
| `DS-004` | [`tenant.json`](tenant.json) | Common Infrastructure |
| `DS-005` | [`policy_evaluation_module_artifact.json`](policy_evaluation_module_artifact.json) | Governance Artifact |
| `DS-006` | [`policy_artifact.json`](policy_artifact.json) | Governance Artifact |
| `DS-007` | [`constraint_artifact.json`](constraint_artifact.json) | Governance Artifact |
| `DS-008` | [`invariant_definition.json`](invariant_definition.json) | Governance Artifact |
| `DS-009` | [`exception_artifact.json`](exception_artifact.json) | Governance Artifact |
| `DS-010` | [`governance_artifact_view.json`](governance_artifact_view.json) | Governance Artifact |
| `DS-011` | [`constraint_evaluation.json`](constraint_evaluation.json) | Evaluation Result |
| `DS-012` | [`invariant_evaluation.json`](invariant_evaluation.json) | Evaluation Result |
| `DS-013` | [`proposal_submit_request.json`](proposal_submit_request.json) | Governance Workflow |
| `DS-014` | [`proposal_view.json`](proposal_view.json) | Governance Workflow |
| `DS-015` | [`governance_decision_result.json`](governance_decision_result.json) | Governance Workflow |
| `DS-017` | [`execution_authorization_view.json`](execution_authorization_view.json) | Governance Workflow |
| `DS-018` | [`commit_boundary_request.json`](commit_boundary_request.json) | Governance Workflow |
| `DS-019` | [`commit_boundary_result.json`](commit_boundary_result.json) | Governance Workflow |
| `DS-020` | [`governance_evidence.json`](governance_evidence.json) | Governance Workflow |
| `DS-021` | [`governed_action_proposal.json`](governed_action_proposal.json) | Canonical Governance Object |
| `DS-022` | [`governance_context_envelope.json`](governance_context_envelope.json) | Canonical Governance Object |
| `DS-023` | [`canonical_state.json`](canonical_state.json) | Canonical Governance Object |
| `DS-024` | [`authority_lineage.json`](authority_lineage.json) | Authority |
| `DS-025` | [`delegation_artifact.json`](delegation_artifact.json) | Authority |
| `DS-026` | [`governance_approval_artifact.json`](governance_approval_artifact.json) | Approval and Adjudication |
| `DS-027` | [`governance_receipt.json`](governance_receipt.json) | Evidence and Provenance |
| `DS-028` | [`refusal_record.json`](refusal_record.json) | Evidence and Provenance |
| `DS-029` | [`enforcement_context.json`](enforcement_context.json) | Commit and Enforcement |
| `DS-030` | [`governance_binding_validation_result.json`](governance_binding_validation_result.json) | Commit and Enforcement |
| `DS-031` | [`resulting_state_validation_result.json`](resulting_state_validation_result.json) | Commit and Enforcement |
| `DS-032` | [`state_qualification_result.json`](state_qualification_result.json) | Qualification |
| `DS-033` | [`evidence_qualification_result.json`](evidence_qualification_result.json) | Qualification |
| `DS-034` | [`authority_rederivation_result.json`](authority_rederivation_result.json) | Authority |
| `DS-035` | [`bind_set.json`](bind_set.json) | Composite Governance |
| `DS-036` | [`governance_dependency_graph.json`](governance_dependency_graph.json) | Composite Governance |
| `DS-037` | [`deterministic_adjudication_result.json`](deterministic_adjudication_result.json) | Composite Governance |
| `DS-038` | [`governance_lifecycle_record.json`](governance_lifecycle_record.json) | Lifecycle and Continuation |
| `DS-039` | [`continuation_integrity_result.json`](continuation_integrity_result.json) | Lifecycle and Continuation |
| `DS-040` | [`governance_ledger_event.json`](governance_ledger_event.json) | Evidence and Provenance |
| `DS-041` | [`governance_configuration.json`](governance_configuration.json) | Governance Compilation |
| `DS-042` | [`compiled_governance_artifact.json`](compiled_governance_artifact.json) | Governance Compilation |
| `DS-043` | [`controlled_governance_activation.json`](controlled_governance_activation.json) | Governance Compilation |
| `DS-044` | [`registry_document.schema.json`](registry_document.schema.json) | Registry Validation |
| `DS-045` | [`governance_approval_submission.json`](governance_approval_submission.json) | Approval and Adjudication |

## Retired DS Identifiers

| DS ID | Historical schema | Disposition |
|---|---|---|
| `DS-016` | `human_review_artifact.json` | Permanently retired; superseded by `DS-026`. The identifier remains reserved for historical traceability and is not part of the active schema set. |

`human_review_artifact.json` is not present in the active repository. DS-026 `governance_approval_artifact.json` is the sole active approval, adjudication, cosignature, quorum-participation, cancellation, withdrawal, and risk-acceptance schema.

## Canonical Schema Architecture

### Common infrastructure and implementation metadata

- DS-001 provides only actively used shared definitions. Transitional and backward-compatibility aliases are not retained.
- DS-002 separates transport and application errors from Structural Refusal.
- DS-003 advertises supported AGCP releases, schema-set identity and hashes, implementation profiles, registry releases, conformance levels, governance capabilities, and HTTP contract identity.
- DS-004 provides the authoritative Tenant governance record, including state and configuration history, isolation controls, evidence, attribution, and integrity protection.

### Governance artifacts and deterministic evaluation

- DS-005 through DS-010 define policy modules, policies, constraints, invariants, exceptions, and the canonical governance-artifact read model.
- DS-011 and DS-012 define proposal-specific, integrity-protected constraint and invariant evaluation results with qualified-input bindings, Governance Version, evidence, refusal, escalation, and lifecycle effects.

### Proposal, context, state, authority, and approval

- DS-013 is the proposal-submission transport wrapper.
- DS-021 defines the canonical Governed Action Proposal and Proposal Identity.
- DS-022 defines the attributable and versioned Governance Context Envelope.
- DS-023 defines Canonical State and references DS-032 for its State Qualification Result.
- DS-024 and DS-025 define Authority Lineage and Delegation Artifacts.
- DS-026 defines the sole active authoritative Governance Approval Artifact.
- DS-045 defines the separate untrusted Governance Approval Submission accepted at IF-001 ingress.

### Qualification, commitment, enforcement, and composite governance

- DS-029 through DS-037 provide Enforcement Context, Governance Binding Validation, Resulting-State Validation, State Qualification, Evidence Qualification, Authority Re-Derivation, Bind Sets, Governance Dependency Graphs, and Deterministic Adjudication.
- DS-015, DS-017, DS-018, and DS-019 reference those canonical results directly for governance decisions, Execution Authorization, Commit Boundary requests, and Commit Boundary results.
- DS-035 through DS-037 preserve complete Bind Set, dependency, coupling, partial-bind, Admissible Set, and deterministic selection semantics without using arrival timing as a governance basis.

### Evidence, receipt, refusal, lifecycle, continuation, and ledger

- DS-020 defines typed Governance Evidence with evidence continuity, provenance-chain continuity, qualification, ordering, receipts, refusals, enforcement, and ledger references.
- DS-027 defines Governance Receipts for non-refusal governance results.
- DS-028 defines Refusal Records for Structural Refusal.
- DS-038 defines the authoritative Proposal-Identity-bound Governance Lifecycle Record and Derived Lifecycle State history.
- DS-039 defines Continuation Integrity, degradation, Admissible Path Viability, governed re-evaluation, and recovery for nonterminal proposals.
- DS-040 defines append-only, integrity-linked, totally ordered Governance Ledger events.

No receipt, refusal, lifecycle, continuation, or ledger schema remains pending or reserved.

### Governance compilation and controlled activation

- DS-041 defines explicit, attributable, versioned Governance Configuration, including risk-based re-evaluation configuration.
- DS-042 defines the machine-evaluable output of Governance Compilation, including lineage, Constitutional Validation, Governance Omission Analysis, and Governance Self-Protection results.
- DS-043 defines externally approved, atomic Controlled Governance Activation and Governance Version establishment.

### Registry validation

- DS-044 validates release-governed registry documents.
- The authoritative registry payloads exist only under [`../registries/`](../registries/):
  - `constraint-type-registry.json`
  - `invariant-type-registry.json`
  - `rejection-code-registry.json`
- Registry payloads are not duplicated under `schemas/` and are not counted as JSON Schemas.

## Governance Processing and Lifecycle Model

```text
Proposal Submission
        |
        v
Proposal Qualification
        |
        v
Governance Decision Function
        |
        v
Execution Authorization
        |
        +----> nonterminal waiting, approval, escalation, degradation,
        |      continuation checks, and governed re-evaluation
        |
        v
Governance Realization and Commit-Bound Admissibility
        |
        v
Policy Enforcement Point and Commit Boundary
        |
        v
Governance Receipt or Refusal Record
        |
        v
Governance Ledger and Derived Lifecycle State
```

Continuation Integrity operates throughout the nonterminal pre-commit interval. It is not a post-commit pipeline stage. Human adjudication, quorum, refusal, degradation, recovery, and governed re-evaluation are governed lifecycle paths rather than mandatory linear stages for every proposal.

## Completed Migration Stages

- **Canonical objects:** DS-021 through DS-028 implemented.
- **Qualification, enforcement, and composite governance:** DS-029 through DS-037 implemented.
- **Workflow refactor:** DS-014, DS-015, DS-017 through DS-020 reference canonical schemas directly.
- **Compilation and activation:** DS-041 through DS-043 implemented and consumed by governance artifacts.
- **Lifecycle, continuation, and ledger:** DS-038 through DS-040 implemented.
- **Registry cleanup and validation:** DS-044 implemented; duplicate registry payloads removed.
- **Clean migration:** DS-016 retired; active compatibility aliases removed.

## Schema-Set Rules

- Canonical schema identifiers use the controlled `https://agcp.ai/schemas/...` namespace.
- Normative schemas carry DS, ARM, NS, CR, lifecycle, release, and repository traceability through schema annotations and the catalog.
- Governance-significant content uses a required canonical core. Extensions must be explicitly namespaced and cannot alter canonical governance meaning.
- Outcome-specific requirements are enforced with conditional validation.
- Canonical objects and results are referenced through their assigned DS schemas rather than re-embedded as transitional definitions.
- Approval, authorization, authority at commitment, admissibility, enforcement, and commitment remain distinct concepts.
- Arrival timing, transport behavior, storage order, and implementation scheduling are not authoritative governance bases.

## Validation and Release Integrity

The schema set is validated as one release graph. Publication validation includes:

- JSON Schema Draft 2020-12 metaschema validation;
- resolution of every local `$ref` and JSON Pointer fragment;
- catalog identifier, lifecycle, path, and SHA-256 verification;
- positive and negative semantic test cases;
- OpenAPI external-reference validation;
- authoritative registry validation and digest verification;
- confirmation that no duplicate registry payloads or active DS-016 compatibility schema remain.

Validation reports and implementation reports are retained in this directory and under [`catalog/`](catalog/).

## Normative and Engineering References

These schemas are maintained with:

- AGCP Runtime Governance Conformance Requirements CR-001 through CR-122;
- AGCP Core Specification;
- AGCP Architecture Reference Model;
- AGCP Normative Statements;
- AGCP Requirements Traceability Framework and Requirements Traceability Matrix;
- AGCP HTTP Interface Specification and OpenAPI contract;
- AGCP Registry Specifications;
- AGCP Conformance Test Suite and Assessment Framework.

Last synchronized: 2026-08-03.

## Traceability closure

The active release uses `RTM-1.46`. Every CR row now has an explicit DS, IF, and REG disposition. IF-001 identifies the HTTP v2 interface; IF-002 identifies the Policy Evaluation Contract. Registry entries `REG-001` through `REG-092` carry direct ARM, NS, and CR references.

## Provenance wire envelope

`common.json#/$defs/provenance` is controlled by `../spec/AGCP-Provenance-Wire-Format-Specification.md`. Dependent schemas reference that single definition and SHALL NOT define a conflicting nested signature object. Controlled examples and vectors use the top-level wire fields and detached signature string.

## P1-12 content-digest contract

DS-001 binds SHA-256, SHA-384, SHA-512, BLAKE2B-256, and BLAKE2B-512 to exact lowercase-hexadecimal output lengths. Forty active dependent schema files inherit the corrected definition through `common.json#/$defs/content_digest`. Controlled examples and negative vectors are published under `schemas/examples/` and `conformance/digests/`.
