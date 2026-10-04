# AGCP Harness Check Registry

**Status:** Informational executable mapping, synchronized for the current v2.1.x development set  
**Canonical machine-readable source:** [`harness-checks.json`](harness-checks.json)  
**Fixture mapping:** [`fixture-mapping.json`](fixture-mapping.json)  
**Synchronization:** `AGCP-v2.1.x-HARNESS-VECTOR-CHECK-SYNC-2026-10-03`

> Harness Checks are reusable executable capability checks that support portions of Formal Test Cases. They are not independent normative requirements or assessment authorities.

## Development status

The check and injection inventory is under active development. The checks below represent the executable capabilities identified to date; they are not an assertion that every useful internal test point has been identified or implemented by every reference/runtime implementation. Implementation-specific hooks may evolve while the externally observable test semantics remain stable.

## Registry

| Harness Check ID | Validated capability | Vectors |
|---|---|---:|
| `CHECK-PROPOSAL-QUALIFICATION` | Proposal Qualification accepts valid proposals and refuses malformed or inadmissible proposals. | 4 |
| `CHECK-GOVERNANCE-DECISION` | Governance Decision Function (PDP role) produces deterministic governance outcomes from qualified proposals and authoritative inputs and remains distinct from GRF commit-time realization. | 5 |
| `CHECK-GOVERNANCE-APPROVAL` | Human adjudication and Governance Approval Artifacts are enforced when required and cannot be bypassed before Commit-Bound Admissibility. | 6 |
| `CHECK-EXECUTION-AUTHORIZATION` | Execution Authorization is produced only after required governance prerequisites are satisfied. | 6 |
| `CHECK-COMMIT-BOUNDARY` | Commit processing invokes the GRF to establish current eligibility, apply the selected PEP Profile, assemble Enforcement Context, and require PEP mediation before the governed consequence. | 11 |
| `CHECK-GOVERNANCE-EVIDENCE` | Governance Evidence is produced, linked, attributable, integrity-protected, and sufficient for audit and deterministic replay. | 11 |
| `CHECK-APPEND-ONLY-GOVERNANCE-LEDGER` | DS-040 Governance Ledger Events preserve immutable, attributable, integrity-linked, and authoritatively ordered governance history. | 4 |
| `CHECK-CANONICAL-STATE` | Canonical State is deterministically resolved from applicable qualified authoritative governance sources; incorporated Governance Ledger records use authoritative ledger ordering. | 3 |
| `CHECK-IDEMPOTENCY` | Repeated proposal submission with the same idempotency key or replay-protection mechanism does not create conflicting governance state. | 7 |
| `CHECK-TENANT-STATE-GATING` | Tenant lifecycle state gates proposal submission, Execution Authorization, and Commit Boundary processing. | 2 |
| `CHECK-TENANT-AND-DOMAIN-ISOLATION` | Tenant and Governance Domain isolation prevent unauthorized cross-boundary governance operations. | 9 |
| `CHECK-PROVENANCE` | Governance-significant requests and artifacts include valid provenance and reject invalid provenance. | 3 |
| `CHECK-REGISTRIES` | Governance processing uses published registries and rejects unknown registered values. | 8 |
| `CHECK-QUALIFIED-GOVERNANCE-INPUTS` | Canonical State, Governance Evidence, identity/authorization facts, and authority are independently qualified or re-derived at the applicable evaluation horizon before commitment. | 11 |
| `CHECK-LIFECYCLE-AND-CONTINUATION` | Derived Lifecycle State and Continuation Integrity preserve governed nonterminal progression, degradation, re-evaluation, and recovery. | 6 |
| `CHECK-GOVERNANCE-COMPILATION-ACTIVATION` | Governance Configuration, deterministic compilation, constitutional validation, constitutional constraint preservation, omission analysis, governance self-protection, atomic Controlled Governance Activation, prior-version preservation, governed rollback, evidence, and lineage are executable and traceable. | 9 |
| `CHECK-HTTP-INTERFACE-CONTRACT` | All ten mandatory IF-001 operations are executable with schema-valid positive coverage and applicable negative, tenant/domain-isolation, and idempotency coverage. | 33 |
| `CHECK-IDENTITY-AUTHORIZATION-QUALIFICATION` | IAS Profile resolution produces qualified identity and authorization facts (DS-053) from authoritative sources without converting claimant assertions into authority or producing a Governance Decision/Execution Authorization by itself. | 5 |
| `CHECK-GOVERNANCE-REALIZATION` | The GRF independently establishes current commit eligibility from current canonical state, evidence, authority, lifecycle, validity, and binding conditions, invokes GDF re-evaluation when required, and constructs the enforcement-facing context without becoming the policy decision function. | 4 |
| `CHECK-PEP-ENFORCEMENT-BINDING` | The PEP enforces the exact GRF-authorized consequence using the selected PEP Profile and Governance Enforcement Binding, rejecting unsupported/non-faithful mappings, context tampering, binding mismatch, replay, and unqualified GRF callers. | 6 |
| `CHECK-GOVERNED-EXECUTION-OUTCOME` | Where execution is asynchronous or otherwise distinct from commitment, DS-052 records the subsequent operational outcome and lifecycle remains COMMITTED until execution-outcome evidence establishes EXECUTED or EXECUTION_FAILED. | 2 |

## Detailed check definitions

### CHECK-PROPOSAL-QUALIFICATION

**Severity:** MUST  
**Validated capability:** Proposal Qualification accepts valid proposals and refuses malformed or inadmissible proposals.

**Pipeline stages:** `Proposal Qualification`

**Schemas:** `schemas/proposal_submit_request.json`, `schemas/proposal_view.json`, `schemas/error_response.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-PROP-004`, `TV-PROP-005`, `TV-PROP-006`

**Expected behavior**

- Valid proposals proceed to governance processing.
- Structurally invalid proposals are refused or rejected using the applicable rejection code.
- Proposal Qualification produces Governance Evidence where required.
- No Execution Authorization or Commit Boundary processing occurs for structurally refused proposals.

**Required evidence**

- Proposal record
- Proposal Qualification outcome
- Governance Evidence reference
- Applicable rejection code

### CHECK-GOVERNANCE-DECISION

**Severity:** MUST  
**Validated capability:** Governance Decision Function (PDP role) produces deterministic governance outcomes from qualified proposals and authoritative inputs and remains distinct from GRF commit-time realization.

**Pipeline stages:** `Governance Decision Function`

**Schemas:** `schemas/governance_decision_result.json`, `schemas/constraint_evaluation.json`, `schemas/invariant_evaluation.json`, `schemas/deterministic_adjudication_result.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-PROP-002`, `TV-PROP-003`, `TV-PROP-007`, `TV-GRF-003`

**Fixtures:** `schemas/examples/ds011-constraint-evaluation-satisfied.json`, `schemas/examples/ds011-constraint-evaluation-violated.json`, `schemas/examples/ds012-invariant-evaluation-preserved.json`, `schemas/examples/ds012-invariant-evaluation-hard-violation.json`

**Expected behavior**

- Authorized decisions are produced only when applicable governance policy permits the Proposal.
- Denied decisions are produced when applicable governance policy rejects the Proposal.
- Pending human adjudication is produced when governance policy requires governed human adjudication or Governance Approval.
- Governance decisions are deterministic for identical authoritative inputs.

**Required evidence**

- Governance Decision Result
- Policy reference
- Canonical State reference
- Authority Lineage reference
- Governance Evidence reference

### CHECK-GOVERNANCE-APPROVAL

**Severity:** MUST  
**Validated capability:** Human adjudication and Governance Approval Artifacts are enforced when required and cannot be bypassed before Commit-Bound Admissibility.

**Pipeline stages:** `Human Adjudication and Governance Approval`

**Schemas:** `schemas/governance_approval_artifact.json`, `schemas/governance_lifecycle_record.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-GAPP-001`, `TV-GAPP-002`, `TV-GAPP-003`, `TV-GAPP-004`, `TV-IAS-001`, `TV-IAS-002`

**Fixtures:** `schemas/examples/ds026-governance-approval-partial-quorum.json`, `schemas/examples/ds026-governance-approval-completed-quorum.json`

**Expected behavior**

- Valid partial quorum is accumulated without being treated as completed quorum.
- Completion of required quorum establishes eligibility for the applicable lifecycle transition, subject to all other governance conditions.
- Approval or quorum completion does not itself constitute authority at commitment or permission to execute.
- Invalid, expired, unauthorized, replayed, revoked, withdrawn, or superseded Governance Approval Artifacts do not support progression.
- Governance Approval Artifacts are bound to the applicable Proposal Identity, lifecycle state, tenant, governance domain, target, scope, validity conditions, and Authority Lineage.

**Required evidence**

- Governance Approval Artifact
- Approver identity
- Authority Lineage reference
- Lifecycle-state binding
- Quorum contribution and status where applicable
- Cryptographic verification evidence
- Governance Evidence reference

### CHECK-EXECUTION-AUTHORIZATION

**Severity:** MUST  
**Validated capability:** Execution Authorization is produced only after required governance prerequisites are satisfied.

**Pipeline stages:** `Execution Authorization`

**Schemas:** `schemas/execution_authorization_view.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-GAPP-002`, `TV-COMMIT-003`, `TV-EAUTH-001`, `TV-EAUTH-002`, `TV-EAUTH-003`

**Expected behavior**

- Execution Authorization succeeds only after valid Governance Decision and required governed approval or adjudication completion.
- Execution Authorization fails when required authority, Canonical State, governance configuration, tenant state, or Governance Domain conditions are not satisfied.
- Execution Authorization does not itself perform execution.
- Execution Authorization produces Governance Evidence and an ordered DS-040 Governance Ledger Event where required.

**Required evidence**

- Execution Authorization artifact
- Authorization outcome
- Proposal reference
- Authority Lineage reference
- Canonical State reference
- Governance Evidence reference

### CHECK-COMMIT-BOUNDARY

**Severity:** MUST  
**Validated capability:** Commit processing invokes the GRF to establish current eligibility, apply the selected PEP Profile, assemble Enforcement Context, and require PEP mediation before the governed consequence.

**Pipeline stages:** `Commit Boundary`

**Schemas:** `schemas/commit_boundary_request.json`, `schemas/commit_boundary_result.json`, `schemas/enforcement_context.json`, `schemas/governance_binding_validation_result.json`, `schemas/resulting_state_validation_result.json`, `schemas/state_qualification_result.json`, `schemas/evidence_qualification_result.json`, `schemas/authority_rederivation_result.json`, `schemas/continuation_integrity_result.json`

**Harness Test Vectors:** `TV-COMMIT-001`, `TV-COMMIT-002`, `TV-COMMIT-003`, `TV-COMMIT-004`, `TV-COMMIT-005`, `TV-GRF-001`, `TV-GRF-002`, `TV-GRF-003`, `TV-GRF-004`, `TV-PEP-001`, `TV-PEP-002`

**Fixtures:** `schemas/examples/ds018-commit-boundary-request-single.json`, `schemas/examples/ds019-commit-boundary-result-success.json`, `schemas/examples/ds019-commit-boundary-result-refusal.json`, `schemas/examples/ds029-enforcement-context-admissible.json`, `schemas/examples/ds029-enforcement-context-prevent.json`

**Expected behavior**

- The caller requests commit processing using DS-018 and does not authoritatively supply DS-029 Enforcement Context.
- The GRF independently re-establishes current authority, state, evidence, validity, lifecycle, and binding sufficiency.
- The GRF selects/applies the controlling PEP Profile and assembles the Enforcement Context.
- The PEP mediates the governed consequence and fails closed on invalid, stale, mismatched, replayed, unsupported, or unrepresentable enforcement.

**Required evidence**

- Commit Boundary request
- Commit Boundary result
- Execution Authorization reference
- Canonical State reference
- Governance Evidence reference
- DS-040 Governance Ledger Event reference

### CHECK-GOVERNANCE-EVIDENCE

**Severity:** MUST  
**Validated capability:** Governance Evidence is produced, linked, attributable, integrity-protected, and sufficient for audit and deterministic replay.

**Pipeline stages:** `Governance Evidence`

**Schemas:** `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-EVID-001`, `TV-PROP-001`, `TV-COMMIT-001`, `TV-IAS-003`, `TV-GRF-002`, `TV-PEP-003`, `TV-PEP-004`, `TV-PEP-005`, `TV-PEP-006`, `TV-EXEC-001`, `TV-EXEC-002`

**Expected behavior**

- Governance Evidence conforms to the published schema.
- Governance Evidence includes required references to tenant, proposal, governance stage, outcome, provenance, and ledger reference.
- Governance Evidence remains attributable and integrity-protected.
- Governance Evidence supports deterministic replay and independent verification.

**Required evidence**

- governance_evidence_id
- tenant_id
- proposal_id
- governance_stage
- stage_outcome
- integrity_signature
- ledger_reference

### CHECK-APPEND-ONLY-GOVERNANCE-LEDGER

**Severity:** MUST  
**Validated capability:** DS-040 Governance Ledger Events preserve immutable, attributable, integrity-linked, and authoritatively ordered governance history.

**Pipeline stages:** `Append-Only Governance Ledger`

**Schemas:** `schemas/governance_ledger_event.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-EVID-001`, `TV-STATE-001`, `TV-STATE-002`

**Fixtures:** `schemas/examples/ds040-governance-ledger-event-genesis.json`, `schemas/examples/ds040-governance-ledger-event-sequenced.json`

**Expected behavior**

- Every appended governance record validates against schemas/governance_ledger_event.json.
- Governance Ledger Events are immutable and append-only after append.
- Ordering is determined within the declared ordering_scope by ledger_position.sequence.
- Genesis and non-genesis events satisfy DS-040 predecessor-binding conditions.
- Event subject, typed artifact references, governance basis, evidence binding, causality, integrity protection, attribution, provenance, replay material, and semantic assertions are present and valid.
- Timestamp, arrival, storage, node, transport, and implementation scheduling are not accepted as authoritative ordering bases.
- Tampered, deleted, substituted, detached, or reordered event histories are rejected or produce non-equivalent ledger-derived results.

**Required evidence**

- ledger_event_id
- event_version
- record_type
- event_type
- event_category
- ledger_id
- ordering_scope
- ledger_position
- tenant_id
- governance_domain_id
- event_subject
- event_artifact_refs
- governance_basis
- evidence_binding
- causality
- event_time
- append_status
- append_only_controls
- integrity_protection
- attribution
- provenance
- replay_material
- semantic_assertions
- event_uri

### CHECK-CANONICAL-STATE

**Severity:** MUST  
**Validated capability:** Canonical State is deterministically resolved from applicable qualified authoritative governance sources; incorporated Governance Ledger records use authoritative ledger ordering.

**Pipeline stages:** `Canonical State Resolution`, `Deterministic Replay`

**Schemas:** `schemas/canonical_state.json`, `schemas/state_qualification_result.json`, `schemas/governance_ledger_event.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-STATE-001`, `TV-STATE-002`, `TV-COMMIT-001`

**Fixtures:** `schemas/examples/ds032-state-qualification-qualified.json`, `schemas/examples/ds032-state-qualification-not-qualified.json`

**Expected behavior**

- Canonical State is reproducible from the same complete set of qualified authoritative source versions used for the evaluation.
- Incorporated Governance Ledger records and Derived Lifecycle State are interpreted using authoritative ledger ordering.
- Materialized Canonical State views are verifiable against the applicable qualified authoritative sources and ordered Governance Ledger records.
- Reordered ledger histories are rejected or produce non-equivalent ledger-derived event or lifecycle state.
- Timestamp or implementation-specific storage ordering is not accepted as a substitute for authoritative ledger ordering.

**Required evidence**

- Canonical State reference
- Qualified authoritative source references and versions
- Applicable ordered Governance Ledger records and ledger positions
- Governance Evidence references
- Canonical State resolution and replay evidence

### CHECK-IDEMPOTENCY

**Severity:** MUST  
**Validated capability:** Repeated proposal submission with the same idempotency key or replay-protection mechanism does not create conflicting governance state.

**Pipeline stages:** `Proposal Qualification`, `Governance Evidence`, `Append-Only Governance Ledger`

**Harness Test Vectors:** `TV-PROP-008`, `TV-PROP-009`, `TV-COMMIT-004`, `TV-PEM-004`, `TV-PEM-005`, `TV-POL-004`, `TV-POL-005`

**Expected behavior**

- Identical replay produces an equivalent response.
- Conflicting replay is rejected.
- No duplicate governance-significant ledger event is appended unless explicitly permitted by idempotency semantics.
- Governance Evidence remains consistent.

**Required evidence**

- Idempotency or replay-protection key
- Proposal reference
- Governance Evidence reference
- DS-040 Governance Ledger Events before and after replay

### CHECK-TENANT-STATE-GATING

**Severity:** MUST  
**Validated capability:** Tenant lifecycle state gates proposal submission, Execution Authorization, and Commit Boundary processing.

**Pipeline stages:** `Tenant and Governance Domain Isolation`, `Proposal Qualification`, `Execution Authorization`, `Commit Boundary`

**Schemas:** `schemas/tenant.json`

**Harness Test Vectors:** `TV-PROP-006`, `TV-COMMIT-005`

**Expected behavior**

- ACTIVE tenants may perform permitted governance operations.
- PROVISIONED, SUSPENDED, or DECOMMISSIONED tenants are restricted according to the Core Specification.
- Tenant state violations are rejected using the applicable rejection code.
- Tenant state enforcement is deterministic and tenant-scoped.

**Required evidence**

- Tenant record
- Tenant state
- Governance Evidence reference
- Applicable rejection code

### CHECK-TENANT-AND-DOMAIN-ISOLATION

**Severity:** MUST  
**Validated capability:** Tenant and Governance Domain isolation prevent unauthorized cross-boundary governance operations.

**Pipeline stages:** `Tenant and Governance Domain Isolation`, `Cross-Domain Authority Isolation`

**Schemas:** `schemas/tenant.json`, `schemas/canonical_state.json`, `schemas/authority_lineage.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-XTEN-001`, `TV-XTEN-002`, `TV-XTEN-003`, `TV-XTEN-004`, `TV-EAUTH-003`, `TV-PEM-003`, `TV-POL-003`, `TV-GART-003`, `TV-IAS-005`

**Expected behavior**

- Unauthorized cross-tenant operations are rejected.
- Unauthorized cross-domain operations are rejected where Governance Domains are implemented.
- Cross-boundary operations do not mutate unauthorized governance state.
- Cross-boundary operations do not append successful unauthorized Commit Boundary entries.
- Tenant and Governance Domain non-disclosure behavior is preserved where applicable.

**Required evidence**

- Tenant context
- Governance Domain context
- Access decision
- Applicable rejection code
- Governance Evidence reference where recorded

### CHECK-PROVENANCE

**Severity:** MUST  
**Validated capability:** Governance-significant requests and artifacts include valid provenance and reject invalid provenance.

**Pipeline stages:** `Proposal Qualification`, `Governance Approval and Adjudication`, `Execution Authorization`, `Commit Boundary`, `Governance Evidence`

**Schemas:** `schemas/common.json`, `schemas/governance_evidence.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-PROP-005`, `TV-GAPP-004`

**Expected behavior**

- Valid provenance is accepted when otherwise authorized.
- Invalid provenance is rejected before governance processing continues.
- Provenance is tenant-scoped.
- Replay protection is enforced for provenance-bearing artifacts.

**Required evidence**

- Provenance object
- Signature verification result
- Replay-protection result
- Applicable rejection code

### CHECK-REGISTRIES

**Severity:** MUST  
**Validated capability:** Governance processing uses published registries and rejects unknown registered values.

**Pipeline stages:** `Governance Decision Function`, `Policy Evaluation Contract`

**Schemas:** `schemas/registry_document.schema.json`

**Harness Test Vectors:** `TV-PROP-003`, `TV-PROP-004`, `TV-PEM-001`, `TV-PEM-002`, `TV-POL-001`, `TV-POL-002`, `TV-GART-001`, `TV-GART-002`

**Fixtures:** `schemas/examples/ds044-registry-document-capability-example.json`

**Expected behavior**

- Each authoritative registry payload validates against schemas/registry_document.schema.json and passes integrity verification.
- Unknown constraint types are rejected.
- Unknown invariant types are rejected.
- Referenced rejection codes exist in the rejection-code registry.
- Registry lookup is deterministic and tenant-scoped where applicable.

**Required evidence**

- DS-044 registry validation result
- Registry reference
- Registry lookup result
- Applicable rejection code

### CHECK-QUALIFIED-GOVERNANCE-INPUTS

**Severity:** MUST  
**Validated capability:** Canonical State, Governance Evidence, identity/authorization facts, and authority are independently qualified or re-derived at the applicable evaluation horizon before commitment.

**Pipeline stages:** `State Qualification`, `Evidence Qualification`, `Authority Re-Derivation`

**Schemas:** `schemas/state_qualification_result.json`, `schemas/evidence_qualification_result.json`, `schemas/authority_rederivation_result.json`

**Harness Test Vectors:** `TV-STATE-001`, `TV-STATE-002`, `TV-COMMIT-001`, `TV-IAS-001`, `TV-IAS-002`, `TV-IAS-003`, `TV-IAS-004`, `TV-IAS-005`, `TV-GRF-001`, `TV-GRF-002`, `TV-GRF-004`

**Fixtures:** `schemas/examples/ds032-state-qualification-qualified.json`, `schemas/examples/ds032-state-qualification-not-qualified.json`, `schemas/examples/ds033-evidence-qualification-qualified.json`, `schemas/examples/ds033-evidence-qualification-not-qualified.json`

**Expected behavior**

- Qualification results are attributable, integrity-protected, and proposal-specific where applicable.
- Unqualified state or evidence cannot support admissibility.
- Authority is re-derived from current qualified governance inputs before commitment.

**Required evidence**

- State Qualification Result
- Evidence Qualification Result
- Authority Re-Derivation Result
- Governance Evidence references

### CHECK-LIFECYCLE-AND-CONTINUATION

**Severity:** MUST  
**Validated capability:** Derived Lifecycle State and Continuation Integrity preserve governed nonterminal progression, degradation, re-evaluation, and recovery.

**Pipeline stages:** `Derived Lifecycle State`, `Continuation Integrity`, `Risk-Based Re-Evaluation`

**Schemas:** `schemas/governance_lifecycle_record.json`, `schemas/continuation_integrity_result.json`, `schemas/governance_ledger_event.json`

**Harness Test Vectors:** `TV-PROP-001`, `TV-COMMIT-001`, `TV-COMMIT-002`, `TV-EXEC-001`, `TV-EXEC-002`, `TV-GRF-003`

**Fixtures:** `schemas/examples/ds038-governance-lifecycle-authorized.json`, `schemas/examples/ds039-continuation-integrity-degraded.json`, `schemas/examples/ds039-continuation-integrity-recovered.json`

**Expected behavior**

- Lifecycle state is derived from ordered authoritative governance records.
- Material governance changes deterministically degrade affected nonterminal proposals.
- Governed recovery does not bypass renewed Commit-Bound Admissibility.

**Required evidence**

- Lifecycle record
- Continuation Integrity result
- Risk-based re-evaluation evidence
- Governance Ledger event references

### CHECK-GOVERNANCE-COMPILATION-ACTIVATION

**Severity:** MUST  
**Validated capability:** Governance Configuration, deterministic compilation, constitutional validation, constitutional constraint preservation, omission analysis, governance self-protection, atomic Controlled Governance Activation, prior-version preservation, governed rollback, evidence, and lineage are executable and traceable.

**Pipeline stages:** `Governance Configuration`, `Governance Compilation`, `Controlled Governance Activation`

**Schemas:** `schemas/governance_configuration.json`, `schemas/compiled_governance_artifact.json`, `schemas/controlled_governance_activation.json`, `schemas/policy_evaluation_module_artifact.json`, `schemas/policy_artifact.json`, `schemas/governance_artifact_view.json`

**Harness Test Vectors:** `TV-GCFG-001`, `TV-GCOMP-001`, `TV-GCONST-001`, `TV-GCONST-002`, `TV-GOMIT-001`, `TV-GSELF-001`, `TV-GACT-001`, `TV-GACT-002`, `TV-GROLL-001`

**Fixtures:** `schemas/examples/ds041-governance-configuration-active.json`, `schemas/examples/ds042-compiled-governance-artifact-validated.json`, `schemas/examples/ds043-controlled-governance-activation-activated.json`, `schemas/examples/ds005-policy-evaluation-module-registered.json`, `schemas/examples/ds006-governance-policy-registered.json`, `schemas/examples/ds010-governance-artifact-view-registered.json`

**Expected behavior**

- Governance Configuration is explicit, versioned, attributable, externally approved for change, and requires compilation, validation, omission analysis, and controlled activation.
- Equivalent qualified governance inputs compile to equivalent machine-evaluable artifacts with complete deterministic source-to-output lineage.
- Constitutional validation preserves protected constraints and prevents weakened safeguards from becoming activation-eligible.
- Governance Omission Analysis detects material omissions before activation eligibility.
- Governed systems cannot directly modify active admissibility conditions or bypass external approval and controlled activation.
- Only an approved and validated package becomes authoritative, and activation is atomic with no partial activation.
- Activation failure preserves the prior authoritative Governance Version and records attributable evidence.
- Governed rollback restores an approved prior Governance Version atomically while preserving evidence, lineage, ledger ordering, and deterministic replay.

**Required evidence**

- Governance Configuration
- Compiled Governance Artifact
- Constitutional Validation result
- Governance Omission Analysis result
- Governance Self-Protection assessment
- Controlled Governance Activation
- Rollback basis and outcome
- Governance Evidence and Governance Ledger references
- Source-to-output and activation lineage

### CHECK-HTTP-INTERFACE-CONTRACT

**Severity:** MUST  
**Validated capability:** All ten mandatory IF-001 operations are executable with schema-valid positive coverage and applicable negative, tenant/domain-isolation, and idempotency coverage.

**Pipeline stages:** `HTTP Interface`

**Schemas:** `schemas/meta_response.json`, `schemas/proposal_submit_request.json`, `schemas/proposal_view.json`, `schemas/governance_approval_artifact.json`, `schemas/execution_authorization_view.json`, `schemas/commit_boundary_request.json`, `schemas/commit_boundary_result.json`, `schemas/governance_evidence.json`, `schemas/policy_evaluation_module_artifact.json`, `schemas/policy_artifact.json`, `schemas/governance_artifact_view.json`, `schemas/error_response.json`

**Harness Test Vectors:** `TV-META-001`, `TV-PROP-001`, `TV-PROP-004`, `TV-PROP-008`, `TV-PROP-009`, `TV-GET-001`, `TV-GET-002`, `TV-XTEN-001`, `TV-GAPP-001`, `TV-GAPP-003`, `TV-XTEN-002`, `TV-EAUTH-001`, `TV-EAUTH-002`, `TV-EAUTH-003`, `TV-COMMIT-001`, `TV-COMMIT-002`, `TV-COMMIT-004`, `TV-XTEN-003`, `TV-EVID-001`, `TV-XTEN-004`, `TV-PEM-001`, `TV-PEM-002`, `TV-PEM-003`, `TV-PEM-004`, `TV-PEM-005`, `TV-POL-001`, `TV-POL-002`, `TV-POL-003`, `TV-POL-004`, `TV-POL-005`, `TV-GART-001`, `TV-GART-002`, `TV-GART-003`

**Expected behavior**

- Every mandatory IF-001 operation has at least one executable schema-valid positive vector.
- Each applicable declared negative response path is exercised without being preempted by missing request parameters or an invalid positive request.
- Tenant-scoped retrieval and registration operations enforce tenant and Governance Domain isolation.
- Operations requiring Idempotency-Key produce equivalent outcomes for equivalent replay and reject conflicting reuse.
- Harness request parameters, request schemas, and expected statuses remain synchronized with the OpenAPI contract and human-readable Interface Specification.

**Required evidence**

- Matched IF-001 operationId
- Request-parameter validation result
- Request or response schema validation result
- Expected and observed HTTP status
- Rejection code where applicable
- Tenant and Governance Domain scope result
- Idempotency result where applicable

### CHECK-IDENTITY-AUTHORIZATION-QUALIFICATION

**Severity:** MUST  
**Validated capability:** IAS Profile resolution produces qualified identity and authorization facts (DS-053) from authoritative sources without converting claimant assertions into authority or producing a Governance Decision/Execution Authorization by itself.

**Pipeline stages:** `Identity and Authorization Qualification`

**Schemas:** `schemas/identity_authorization_qualification_result.json`

**Harness Test Vectors:** `TV-IAS-001`, `TV-IAS-002`, `TV-IAS-003`, `TV-IAS-004`, `TV-IAS-005`

**Fixtures:** `schemas/examples/ds053-identity-authorization-qualified.json`, `schemas/examples/ds053-identity-authorization-not-qualified.json`, `schemas/examples/ds053-identity-authorization-source-unavailable.json`

**Expected behavior**

- Authenticated subject is resolved through the controlling IAS Profile and authoritative source.
- Claimant-supplied roles, entitlements, reviewer classes, or authorization attributes cannot override authoritative qualification.
- Unavailable, stale, conflicting, disabled, revoked, or out-of-scope authority fails closed as required by the applicable TC/profile.
- DS-053 is governance input and is not AGCP Execution Authorization or a Governance Decision.

**Required evidence**

- DS-053 Identity and Authorization Qualification Result
- IAS Profile identity/version/digest
- Authoritative source reference/version/digest
- Qualification evidence and attribution

### CHECK-GOVERNANCE-REALIZATION

**Severity:** MUST  
**Validated capability:** The GRF independently establishes current commit eligibility from current canonical state, evidence, authority, lifecycle, validity, and binding conditions, invokes GDF re-evaluation when required, and constructs the enforcement-facing context without becoming the policy decision function.

**Pipeline stages:** `Governance Realization Function`, `Commit-Bound Admissibility`

**Schemas:** `schemas/authority_rederivation_result.json`, `schemas/governance_binding_validation_result.json`, `schemas/enforcement_context.json`, `schemas/commit_boundary_result.json`

**Harness Test Vectors:** `TV-GRF-001`, `TV-GRF-002`, `TV-GRF-003`, `TV-GRF-004`

**Expected behavior**

- Prior favorable Governance Decision and Execution Authorization are inputs, not current commit eligibility.
- Current authority is re-derived at the commitment horizon.
- Material policy-relevant change causes governed GDF re-evaluation rather than policy reinterpretation by the GRF.
- The GRF selects/applies the PEP Profile and assembles DS-029 only after current eligibility is established.

**Required evidence**

- DS-034 Authority Re-Derivation Result
- Current Canonical State and evidence references
- DS-030 Governance Binding Validation Result where applicable
- GRF attribution
- PEP Profile reference/digest
- DS-029 Enforcement Context when eligible

### CHECK-PEP-ENFORCEMENT-BINDING

**Severity:** MUST  
**Validated capability:** The PEP enforces the exact GRF-authorized consequence using the selected PEP Profile and Governance Enforcement Binding, rejecting unsupported/non-faithful mappings, context tampering, binding mismatch, replay, and unqualified GRF callers.

**Pipeline stages:** `Policy Enforcement Point`

**Schemas:** `schemas/enforcement_context.json`, `schemas/governance_binding_validation_result.json`, `schemas/commit_boundary_result.json`

**Harness Test Vectors:** `TV-PEP-001`, `TV-PEP-002`, `TV-PEP-003`, `TV-PEP-004`, `TV-PEP-005`, `TV-PEP-006`

**Expected behavior**

- Supported mappings preserve the exact governed action/target semantics.
- Unsupported or unrepresentable mappings fail closed.
- Tampered or substituted Enforcement Context is rejected.
- Governance Enforcement Binding mismatch is rejected.
- The GRF-to-PEP caller binding is enforced, including logically when functions are co-located.

**Required evidence**

- PEP Profile identity/version/digest and mapping ID/digest
- DS-029 Enforcement Context
- Governance Enforcement Binding validation evidence
- Authenticated GRF caller binding where applicable
- PEP enforcement result and target receipt/no-effect evidence

### CHECK-GOVERNED-EXECUTION-OUTCOME

**Severity:** MUST  
**Validated capability:** Where execution is asynchronous or otherwise distinct from commitment, DS-052 records the subsequent operational outcome and lifecycle remains COMMITTED until execution-outcome evidence establishes EXECUTED or EXECUTION_FAILED.

**Pipeline stages:** `Post-Commit Governed Execution Outcome`

**Schemas:** `schemas/governed_execution_outcome.json`, `schemas/governance_lifecycle_record.json`, `schemas/commit_boundary_result.json`

**Harness Test Vectors:** `TV-EXEC-001`, `TV-EXEC-002`

**Fixtures:** `schemas/examples/ds052-governed-execution-outcome-pending.json`, `schemas/examples/ds052-governed-execution-outcome-success.json`, `schemas/examples/ds052-governed-execution-outcome-failed.json`

**Expected behavior**

- Commit Successful does not by itself establish completed operational execution when the profile declares post-commit execution.
- PENDING/IN_PROGRESS execution outcome preserves COMMITTED lifecycle status.
- SUCCEEDED produces the applicable executed lifecycle outcome.
- FAILED records execution failure without rewriting the prior commit result.

**Required evidence**

- DS-019 Commit Boundary Result
- DS-052 Governed Execution Outcome
- Lifecycle transition record
- Target receipt/result references
- Governance Evidence and ledger references

## Synchronization rules

- Harness vector/check identifiers are stable executable-support identifiers and do not create requirements.
- The Formal Test Case remains authoritative for assessment procedure and PASS/FAIL/NOT APPLICABLE determination.
- Test controls establish conditions only; they do not inject desired governance outcomes.
- The current inventory is not asserted to be exhaustive or universally implemented.
- `DS-018` is the caller request for commit processing; the caller does not authoritatively supply `DS-029`.
- GRF current-authority/current-state realization, PEP Profile mapping, Governance Enforcement Binding, and distinct DS-052 execution outcome semantics are explicitly covered by synchronized checks and vectors.
