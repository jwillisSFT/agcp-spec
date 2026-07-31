# AGCP Schema Examples and Conformance Fixtures

**Status:** Informative validation fixtures  
**Applicable release:** AGCP v2.0.0  
**Machine-readable mapping:** [`../../conformance/fixture-mapping.json`](../../conformance/fixture-mapping.json)

These files are non-authoritative examples. Each example validates against the exact active schema identified below. The authoritative registries remain under `registries/`; the DS-044 example is an informative synthetic registry used only for validator testing.

| Fixture | DS | Authoritative schema | Scenario |
|---|---:|---|---|
| [`ds011-constraint-evaluation-satisfied.json`](ds011-constraint-evaluation-satisfied.json) | DS-011 | [`../constraint_evaluation.json`](../constraint_evaluation.json) | Constraint evaluation satisfied with qualified deterministic inputs. |
| [`ds011-constraint-evaluation-violated.json`](ds011-constraint-evaluation-violated.json) | DS-011 | [`../constraint_evaluation.json`](../constraint_evaluation.json) | Constraint violation producing Structural Refusal. |
| [`ds012-invariant-evaluation-preserved.json`](ds012-invariant-evaluation-preserved.json) | DS-012 | [`../invariant_evaluation.json`](../invariant_evaluation.json) | Invariant preserved under qualified inputs. |
| [`ds012-invariant-evaluation-hard-violation.json`](ds012-invariant-evaluation-hard-violation.json) | DS-012 | [`../invariant_evaluation.json`](../invariant_evaluation.json) | Hard invariant violation with explicit refusal and lifecycle effects. |
| [`ds018-commit-boundary-request-single.json`](ds018-commit-boundary-request-single.json) | DS-018 | [`../commit_boundary_request.json`](../commit_boundary_request.json) | Current single-transition Commit Boundary request without removed execution_context. |
| [`ds019-commit-boundary-result-success.json`](ds019-commit-boundary-result-success.json) | DS-019 | [`../commit_boundary_result.json`](../commit_boundary_result.json) | Successful Commit Boundary result. |
| [`ds019-commit-boundary-result-refusal.json`](ds019-commit-boundary-result-refusal.json) | DS-019 | [`../commit_boundary_result.json`](../commit_boundary_result.json) | Commit Boundary Structural Refusal result. |
| [`ds026-governance-approval-partial-quorum.json`](ds026-governance-approval-partial-quorum.json) | DS-026 | [`../governance_approval_artifact.json`](../governance_approval_artifact.json) | Governance Approval Artifact contributing to partial quorum. |
| [`ds026-governance-approval-completed-quorum.json`](ds026-governance-approval-completed-quorum.json) | DS-026 | [`../governance_approval_artifact.json`](../governance_approval_artifact.json) | Governance Approval Artifact satisfying quorum. |
| [`ds029-enforcement-context-admissible.json`](ds029-enforcement-context-admissible.json) | DS-029 | [`../enforcement_context.json`](../enforcement_context.json) | Enforcement Context permitting bind only when all current bindings match. |
| [`ds029-enforcement-context-prevent.json`](ds029-enforcement-context-prevent.json) | DS-029 | [`../enforcement_context.json`](../enforcement_context.json) | Enforcement Context directing prevention of bind. |
| [`ds032-state-qualification-qualified.json`](ds032-state-qualification-qualified.json) | DS-032 | [`../state_qualification_result.json`](../state_qualification_result.json) | Canonical State qualification succeeds. |
| [`ds032-state-qualification-not-qualified.json`](ds032-state-qualification-not-qualified.json) | DS-032 | [`../state_qualification_result.json`](../state_qualification_result.json) | Canonical State qualification fails. |
| [`ds033-evidence-qualification-qualified.json`](ds033-evidence-qualification-qualified.json) | DS-033 | [`../evidence_qualification_result.json`](../evidence_qualification_result.json) | Governance Evidence qualification succeeds. |
| [`ds033-evidence-qualification-not-qualified.json`](ds033-evidence-qualification-not-qualified.json) | DS-033 | [`../evidence_qualification_result.json`](../evidence_qualification_result.json) | Governance Evidence qualification fails. |
| [`ds038-governance-lifecycle-authorized.json`](ds038-governance-lifecycle-authorized.json) | DS-038 | [`../governance_lifecycle_record.json`](../governance_lifecycle_record.json) | Ledger-derived lifecycle transition to Authorized. |
| [`ds039-continuation-integrity-degraded.json`](ds039-continuation-integrity-degraded.json) | DS-039 | [`../continuation_integrity_result.json`](../continuation_integrity_result.json) | Continuation degradation requiring governed re-evaluation. |
| [`ds039-continuation-integrity-recovered.json`](ds039-continuation-integrity-recovered.json) | DS-039 | [`../continuation_integrity_result.json`](../continuation_integrity_result.json) | Governed recovery restoring commitment eligibility. |
| [`ds040-governance-ledger-event-genesis.json`](ds040-governance-ledger-event-genesis.json) | DS-040 | [`../governance_ledger_event.json`](../governance_ledger_event.json) | Genesis ledger event with authoritative sequence position. |
| [`ds040-governance-ledger-event-sequenced.json`](ds040-governance-ledger-event-sequenced.json) | DS-040 | [`../governance_ledger_event.json`](../governance_ledger_event.json) | Non-genesis ledger event with predecessor and chain digest. |
| [`ds041-governance-configuration-active.json`](ds041-governance-configuration-active.json) | DS-041 | [`../governance_configuration.json`](../governance_configuration.json) | Active Governance Configuration including risk-based re-evaluation controls. |
| [`ds042-compiled-governance-artifact-validated.json`](ds042-compiled-governance-artifact-validated.json) | DS-042 | [`../compiled_governance_artifact.json`](../compiled_governance_artifact.json) | Compiled Governance Artifact passing constitutional validation and omission analysis. |
| [`ds043-controlled-governance-activation-activated.json`](ds043-controlled-governance-activation-activated.json) | DS-043 | [`../controlled_governance_activation.json`](../controlled_governance_activation.json) | Atomic controlled activation of a validated governance package. |
| [`ds044-registry-document-capability-example.json`](ds044-registry-document-capability-example.json) | DS-044 | [`../registry_document.schema.json`](../registry_document.schema.json) | Non-authoritative capability registry document validating DS-044. |

## Validation requirements

- Validate all examples as JSON Schema Draft 2020-12 instances with complete cross-schema reference resolution.
- Treat example digest values as structurally representative unless a validation report explicitly verifies semantic digest recomputation.
- Resolve harness fixture references before validating HTTP request wrappers against IF-001.
- Do not use example registries as normative controlled vocabularies.
