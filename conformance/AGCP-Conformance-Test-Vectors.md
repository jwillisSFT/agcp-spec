# AGCP Conformance Test Vectors

**Status:** Informational human-readable mirror  
**Authoritative executable source:** `AGCP-Conformance-Harness-Spec.yml`  
**Controlled request-parameter validation:** `AGCP-harness-request-parameter-validation.json`  
**Synchronized vector count:** 54

---

## Purpose

This document is the human-readable rendering of the executable AGCP conformance vector catalog.
It SHALL contain exactly the same vector identifiers as `AGCP-Conformance-Harness-Spec.yml` and
SHALL NOT define independent vectors, aliases, or alternate meanings for an executable vector ID.

The authoritative conformance traceability chain remains:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
        v
Harness Test Vector
```

Harness vectors provide executable realization and do not create independent normative requirements.

---

## Catalog synchronization rule

- The YAML harness specification is the authoritative executable catalog.
- This Markdown file is generated or reviewed against that YAML catalog.
- Vector identifier sets, names, requests, setup conditions, captures, and expected outcomes must remain synchronized.
- Catalog validation fails if either file contains an identifier absent from the other.
- Every primary request and every HTTP setup prestep SHALL supply all path, query, and header parameters required by `../api/AGCP-HTTP-Contract.yaml`; the controlled result is recorded in `AGCP-harness-request-parameter-validation.json`.
- Governance Approval vectors that exercise semantic cryptographic failure SHALL remain structurally valid under `GovernanceApprovalRequest` and DS-026. After schema validation, the harness SHALL independently verify signature, key, and artifact-digest bindings and apply the declared semantic verifier result.

## Complete vector index

| ID | Name |
|---|---|
| `TV-PROP-001` | Submit qualified proposal -> Authorized for Commit Boundary Processing |
| `TV-PROP-002` | Submit proposal requiring governed human adjudication -> Pending Human Review outcome |
| `TV-PROP-003` | Submit proposal with hard invariant failure -> Denied |
| `TV-PROP-004` | DS-013 wrapper with malformed DS-021 proposal -> Structural Refusal / schema rejection |
| `TV-PROP-005` | Invalid provenance -> PROVENANCE_INVALID |
| `TV-PROP-006` | Tenant not ACTIVE -> TENANT_STATE_INVALID |
| `TV-PROP-007` | Policy not found -> POLICY_NOT_FOUND |
| `TV-PROP-008` | Idempotent replay with identical proposal payload -> same Proposal View and no new Governance Ledger Events |
| `TV-PROP-009` | Idempotency conflict -> IDEMPOTENCY_CONFLICT |
| `TV-GET-001` | Get authorized Proposal View returns externally observable governance state and never SUBMITTED |
| `TV-GET-002` | Pre-decision proposal state is not externally observable |
| `TV-GAPP-001` | Partial Governance Approval quorum -> Pending Human Review outcome remains |
| `TV-GAPP-002` | Valid Governance Approval Artifact completes quorum -> Execution Authorization available |
| `TV-GAPP-003` | Expired Governance Approval Artifact -> GOVERNANCE_APPROVAL_EXPIRED |
| `TV-GAPP-004` | Schema-valid Governance Approval Artifact with invalid signature material -> GOVERNANCE_APPROVAL_INVALID |
| `TV-COMMIT-001` | Commit Boundary succeeds with valid Execution Authorization |
| `TV-COMMIT-002` | Commit Boundary while governed approval remains incomplete -> ACTION_NOT_AUTHORIZED |
| `TV-COMMIT-003` | Commit Boundary with mismatched authorization -> ACTION_NOT_AUTHORIZED |
| `TV-COMMIT-004` | Commit replay after Commit Successful -> ACTION_NOT_AUTHORIZED |
| `TV-COMMIT-005` | Commit Boundary when tenant not ACTIVE -> TENANT_STATE_INVALID |
| `TV-EVID-001` | Governance Evidence view validates DS-040 Governance Ledger Event references |
| `TV-STATE-001` | Canonical State resolution from qualified authoritative sources succeeds |
| `TV-STATE-002` | Canonical State resolution rejects reordered incorporated ledger history |
| `TV-XTEN-SETUP` | Setup tenant T2 proposal for cross-tenant tests |
| `TV-XTEN-001` | Cross-tenant Proposal View access is forbidden or hidden |
| `TV-XTEN-002` | Cross-tenant Governance Approval Artifact submission is forbidden or hidden |
| `TV-XTEN-003` | Cross-tenant Commit Boundary is forbidden or hidden |
| `TV-XTEN-004` | Cross-tenant Governance Evidence access is forbidden or hidden |
| `TV-META-001` | Implementation metadata advertises the controlled IF-001 and conformance surface |
| `TV-EAUTH-001` | Retrieve an available Execution Authorization view |
| `TV-EAUTH-002` | Unknown Execution Authorization is not found |
| `TV-EAUTH-003` | Cross-tenant Execution Authorization access is forbidden or hidden |
| `TV-PEM-001` | Register a schema-valid Policy Evaluation Module without activating it |
| `TV-PEM-002` | Malformed Policy Evaluation Module registration is rejected before governance processing |
| `TV-PEM-003` | Cross-tenant Policy Evaluation Module registration is forbidden |
| `TV-PEM-004` | Equivalent Policy Evaluation Module registration replay is idempotent |
| `TV-PEM-005` | Conflicting Policy Evaluation Module registration replay is rejected |
| `TV-POL-001` | Register a schema-valid Governance Policy without activating it |
| `TV-POL-002` | Malformed Governance Policy registration is rejected before governance processing |
| `TV-POL-003` | Cross-tenant Governance Policy registration is forbidden |
| `TV-POL-004` | Equivalent Governance Policy registration replay is idempotent |
| `TV-POL-005` | Conflicting Governance Policy registration replay is rejected |
| `TV-GART-001` | Retrieve a registered Governance Artifact view |
| `TV-GART-002` | Unknown Governance Artifact is not found |
| `TV-GART-003` | Cross-tenant Governance Artifact access is forbidden or hidden |
| `TV-GCFG-001` | Validate active Governance Configuration, controlled change requirements, and risk-based re-evaluation configuration |
| `TV-GCOMP-001` | Equivalent qualified governance inputs compile deterministically to the same machine-evaluable artifact and lineage |
| `TV-GCONST-001` | Constitutional validation preserves protected constraints and permits activation eligibility |
| `TV-GCONST-002` | Attempted weakening of a protected constitutional constraint fails validation and cannot become activation-eligible |
| `TV-GOMIT-001` | Material governance omission is detected before activation eligibility |
| `TV-GSELF-001` | A governed system cannot directly modify its active admissibility conditions |
| `TV-GACT-001` | Approved and validated governance package activates atomically with evidence, lineage, and Governance Version establishment |
| `TV-GACT-002` | Injected member-activation failure prevents partial activation and preserves the prior authoritative version |
| `TV-GROLL-001` | Governed rollback restores the prior Governance Version atomically and preserves evidence and lineage |

---

# Proposal Submission and Qualification

## TV-PROP-001 — Submit qualified proposal -> Authorized for Commit Boundary Processing

### Traceability and applicability

```yaml
profiles:
- L1
- L2
- L3
- L4
concepts:
- Proposal Qualification
- Governance Decision Function
- Execution Authorization
- Governance Evidence
- Append-Only Governance Ledger
```

### Initial conditions and setup

```yaml
auth_as: T1
hooks:
  tenant_state:
    T1: ACTIVE
  policy_resolution:
    P1: found
  pec:
    constraints_outcome: PASS
    invariants_hard_fail: false
    governance_approval_required: false
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_001
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-001
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: do_something
      statement: Test governed action do_something.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: do_something
      effect_representation:
        action_type: do_something
        parameters:
          amount: 10
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: do_something
        parameters:
          amount: 10
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-001
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-001
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-001
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-001
  extensions:
    x-agcp.test-vector: P-PROP-001
```

### Captured values

```yaml
save_proposal_id_as: P_PROP_001
save_authorization_id_as: EA_PROP_001
save_governance_evidence_refs_as: EV_PROP_001
```

### Expected result

```yaml
http:
  status: 200
  body:
    qualification_outcome: Qualified Proposal
    governance_decision: Authorized
    execution_authorization: Authorized for Commit Boundary Processing
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Qualified Proposal
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Governance Decision Function
  match:
    outcome: Authorized
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Execution Authorization
  match:
    outcome: Authorized for Commit Boundary Processing
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
governance_evidence:
  required: true
  schema: governance_evidence.json
  requires_ledger_reference: true
schema: proposal_view.json
```

---

## TV-PROP-002 — Submit proposal requiring governed human adjudication -> Pending Human Review outcome

### Initial conditions and setup

```yaml
auth_as: T1
hooks:
  tenant_state:
    T1: ACTIVE
  policy_resolution:
    P1: found
  pec:
    constraints_outcome: PASS
    invariants_hard_fail: false
    governance_approval_required: true
    required_approval_roles:
    - RISK_OFFICER
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_002
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-002
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: needs_review
      statement: Test governed action needs_review.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: needs_review
      effect_representation:
        action_type: needs_review
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: needs_review
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-002
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-002
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-002
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-002
  extensions:
    x-agcp.test-vector: P-PROP-002
```

### Captured values

```yaml
save_proposal_id_as: P_PROP_002
save_governance_decision_ref_as: GD_PROP_002
```

### Expected result

```yaml
http:
  status: 200
  body:
    qualification_outcome: Qualified Proposal
    governance_decision: Pending Human Review
    required_approval_roles:
    - RISK_OFFICER
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Qualified Proposal
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Governance Decision Function
  match:
    outcome: Pending Human Review
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
governance_evidence:
  required: true
  requires_ledger_reference: true
```

---

## TV-PROP-003 — Submit proposal with hard invariant failure -> Denied

### Initial conditions and setup

```yaml
auth_as: T1
hooks:
  tenant_state:
    T1: ACTIVE
  policy_resolution:
    P1: found
  pec:
    constraints_outcome: PASS
    invariants_hard_fail: true
    invariants_rejection_code: GOVERNANCE_DENIED
    governance_approval_required: false
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_003
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-003
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: violates_hard_invariant
      statement: Test governed action violates_hard_invariant.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: violates_hard_invariant
      effect_representation:
        action_type: violates_hard_invariant
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: violates_hard_invariant
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-003
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-003
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-003
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-003
  extensions:
    x-agcp.test-vector: P-PROP-003
```

### Captured values

```yaml
save_proposal_id_as: P_PROP_003
```

### Expected result

```yaml
http:
  status: 200
  body:
    qualification_outcome: Qualified Proposal
    governance_decision: Denied
    rejection_code: GOVERNANCE_DENIED
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Qualified Proposal
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Governance Decision Function
  match:
    outcome: Denied
    rejection_code: GOVERNANCE_DENIED
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
governance_evidence:
  required: true
  requires_ledger_reference: true
```

---

## TV-PROP-004 — DS-013 wrapper with malformed DS-021 proposal -> Structural Refusal / schema rejection

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_004
body:
  proposal:
    bogus: true
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-004
  extensions:
    x-agcp.test-vector: TV-PROP-004
```

### Expected result

```yaml
http:
  status: 400
  body:
    rejection_code: SCHEMA_VALIDATION_FAILED
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Structural Refusal
    rejection_code: SCHEMA_VALIDATION_FAILED
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
```

---

## TV-PROP-005 — Invalid provenance -> PROVENANCE_INVALID

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_005
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-005
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: x
      statement: Test governed action x.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: x
      effect_representation:
        action_type: x
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: x
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-005
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-005
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-005
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_INVALID
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-005
  extensions:
    x-agcp.test-vector: P-PROP-005
```

### Expected result

```yaml
http:
  status: 400
  body:
    rejection_code: PROVENANCE_INVALID
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Structural Refusal
    rejection_code: PROVENANCE_INVALID
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
```

---

## TV-PROP-006 — Tenant not ACTIVE -> TENANT_STATE_INVALID

### Initial conditions and setup

```yaml
auth_as: T1
hooks:
  tenant_state:
    T1: SUSPENDED
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_006
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-006
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: x
      statement: Test governed action x.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: x
      effect_representation:
        action_type: x
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: x
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-006
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-006
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-006
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-006
  extensions:
    x-agcp.test-vector: P-PROP-006
```

### Expected result

```yaml
http:
  status: 403
  body:
    rejection_code: TENANT_STATE_INVALID
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Structural Refusal
    rejection_code: TENANT_STATE_INVALID
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
```

---

## TV-PROP-007 — Policy not found -> POLICY_NOT_FOUND

### Initial conditions and setup

```yaml
auth_as: T1
hooks:
  tenant_state:
    T1: ACTIVE
  policy_resolution:
    P_MISSING: not_found
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_007
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-PROP-007
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: x
      statement: Test governed action x.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: x
      effect_representation:
        action_type: x
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P_MISSING
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      artifact_uri: https://agcp.example/policies/P_MISSING
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: x
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-PROP-007
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-PROP-007
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-PROP-007
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-007
  extensions:
    x-agcp.test-vector: P-PROP-007
```

### Expected result

```yaml
http:
  status: 422
  body:
    rejection_code: POLICY_NOT_FOUND
ledger_append:
- stage: Proposal Qualification
  match:
    outcome: Qualified Proposal
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Governance Decision Function
  match:
    outcome: Structural Refusal
    rejection_code: POLICY_NOT_FOUND
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
```

---

## TV-PROP-008 — Idempotent replay with identical proposal payload -> same Proposal View and no new Governance Ledger Events

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/proposals/submit
  headers:
    Idempotency-Key: K_PROP_008
  body:
    proposal:
      tenant_id: T1
      governance_domain_id: domain-primary
      proposal_identity:
        proposal_id: P-IDEM-008
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      proposal_kind: SIMPLE
      operational_intent:
        intent_type: idem_ok
        statement: Test governed action idem_ok.
      target:
        target_id: target-primary
        target_type: TEST_RESOURCE
        tenant_id: T1
        governance_domain_id: domain-primary
      requested_effect:
        effect_type: idem_ok
        effect_representation:
          action_type: idem_ok
          parameters: {}
        effect_digest:
          algorithm: SHA-256
          value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      policy_refs:
      - policy_id: P1
        policy_version: 1.0.0
        policy_digest:
          algorithm: SHA-256
          value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        artifact_uri: https://agcp.example/policies/P1
        tenant_id: T1
        governance_domain_id: domain-primary
        status: Active
      action_representation:
        representation_type: agcp.test.action
        representation_version: 1.0.0
        content_type: application/json
        canonicalization: JCS
        payload:
          action_type: idem_ok
          parameters: {}
        payload_digest:
          algorithm: SHA-256
          value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
      governance_context:
        governance_context_id: GCX-P-IDEM-008
        governance_context_version: 1.0.0
        proposal_identity:
          proposal_id: P-IDEM-008
          tenant_id: T1
          governance_domain_id: domain-primary
          canonical_content_digest:
            algorithm: SHA-256
            value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          originator:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
        tenant_id: T1
        governance_domain_id: domain-primary
        attribution:
          principal:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
          attributed_at: '2026-07-30T16:00:00Z'
        created_at: '2026-07-30T16:00:00Z'
        context_digest:
          algorithm: SHA-256
          value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        canonical_state_ref:
          canonical_state_id: CS1
          canonical_state_version: 1.0.0
          canonical_state_digest:
            algorithm: SHA-256
            value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
          resolved_at: '2026-07-30T16:00:00Z'
        authority_lineage_ref:
          authority_lineage_id: AL1
          lineage_version: 1.0.0
          lineage_digest:
            algorithm: SHA-256
            value: '1111111111111111111111111111111111111111111111111111111111111111'
          proposal_id: P-IDEM-008
          tenant_id: T1
          governance_domain_id: domain-primary
        governance_configuration_ref:
          governance_configuration_id: CFG1
          configuration_version: 1.0.0
          configuration_status: ACTIVE
          configuration_digest:
            algorithm: SHA-256
            value: '2222222222222222222222222222222222222222222222222222222222222222'
          governance_version_ref:
            governance_version_id: GV1
            version: 1.0.0
          tenant_id: T1
          governance_domain_id: domain-primary
          effective_at: '2026-07-30T16:00:00Z'
      provenance:
        signer: client:test
        signature:
          alg: Ed25519
          kid: kid-test
          sig: SIG_VALID_123
        signed_at: '2026-07-30T16:00:00Z'
    submitted_at: '2026-07-30T16:00:00Z'
    client_request_id: CR-TV-PROP-008
    extensions:
      x-agcp.test-vector: P-IDEM-008
  expect_status: 200
  capture:
    save_proposal_id_as: P_IDEM_008
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_008
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-IDEM-008
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: idem_ok
      statement: Test governed action idem_ok.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: idem_ok
      effect_representation:
        action_type: idem_ok
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: idem_ok
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-IDEM-008
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-IDEM-008
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-IDEM-008
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-PROP-008
  extensions:
    x-agcp.test-vector: P-IDEM-008
```

### Expected result

```yaml
http:
  status: 200
  body:
    proposal_id: ${P_IDEM_008}
ledger_no_append: true
```

---

## TV-PROP-009 — Idempotency conflict -> IDEMPOTENCY_CONFLICT

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/proposals/submit
  headers:
    Idempotency-Key: K_PROP_009
  body:
    proposal:
      tenant_id: T1
      governance_domain_id: domain-primary
      proposal_identity:
        proposal_id: P-IDEM-009
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      proposal_kind: SIMPLE
      operational_intent:
        intent_type: idem_conflict_v1
        statement: Test governed action idem_conflict_v1.
      target:
        target_id: target-primary
        target_type: TEST_RESOURCE
        tenant_id: T1
        governance_domain_id: domain-primary
      requested_effect:
        effect_type: idem_conflict_v1
        effect_representation:
          action_type: idem_conflict_v1
          parameters: {}
        effect_digest:
          algorithm: SHA-256
          value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
      policy_refs:
      - policy_id: P1
        policy_version: 1.0.0
        policy_digest:
          algorithm: SHA-256
          value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        artifact_uri: https://agcp.example/policies/P1
        tenant_id: T1
        governance_domain_id: domain-primary
        status: Active
      action_representation:
        representation_type: agcp.test.action
        representation_version: 1.0.0
        content_type: application/json
        canonicalization: JCS
        payload:
          action_type: idem_conflict_v1
          parameters: {}
        payload_digest:
          algorithm: SHA-256
          value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
      governance_context:
        governance_context_id: GCX-P-IDEM-009
        governance_context_version: 1.0.0
        proposal_identity:
          proposal_id: P-IDEM-009
          tenant_id: T1
          governance_domain_id: domain-primary
          canonical_content_digest:
            algorithm: SHA-256
            value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          originator:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
        tenant_id: T1
        governance_domain_id: domain-primary
        attribution:
          principal:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
          attributed_at: '2026-07-30T16:00:00Z'
        created_at: '2026-07-30T16:00:00Z'
        context_digest:
          algorithm: SHA-256
          value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        canonical_state_ref:
          canonical_state_id: CS1
          canonical_state_version: 1.0.0
          canonical_state_digest:
            algorithm: SHA-256
            value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
          resolved_at: '2026-07-30T16:00:00Z'
        authority_lineage_ref:
          authority_lineage_id: AL1
          lineage_version: 1.0.0
          lineage_digest:
            algorithm: SHA-256
            value: '1111111111111111111111111111111111111111111111111111111111111111'
          proposal_id: P-IDEM-009
          tenant_id: T1
          governance_domain_id: domain-primary
        governance_configuration_ref:
          governance_configuration_id: CFG1
          configuration_version: 1.0.0
          configuration_status: ACTIVE
          configuration_digest:
            algorithm: SHA-256
            value: '2222222222222222222222222222222222222222222222222222222222222222'
          governance_version_ref:
            governance_version_id: GV1
            version: 1.0.0
          tenant_id: T1
          governance_domain_id: domain-primary
          effective_at: '2026-07-30T16:00:00Z'
      provenance:
        signer: client:test
        signature:
          alg: Ed25519
          kid: kid-test
          sig: SIG_VALID_123
        signed_at: '2026-07-30T16:00:00Z'
    submitted_at: '2026-07-30T16:00:00Z'
    client_request_id: CR-PROP-009-A
    extensions:
      x-agcp.test-vector: P-IDEM-009
  expect_status: 200
  capture:
    save_proposal_id_as: P_IDEM_009
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_PROP_009
body:
  proposal:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_identity:
      proposal_id: P-IDEM-009
      tenant_id: T1
      governance_domain_id: domain-primary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T1
        governance_domain_id: domain-primary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: idem_conflict_v2
      statement: Test governed action idem_conflict_v2.
    target:
      target_id: target-primary
      target_type: TEST_RESOURCE
      tenant_id: T1
      governance_domain_id: domain-primary
    requested_effect:
      effect_type: idem_conflict_v2
      effect_representation:
        action_type: idem_conflict_v2
        parameters: {}
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T1
      governance_domain_id: domain-primary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: idem_conflict_v2
        parameters: {}
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-IDEM-009
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-IDEM-009
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-IDEM-009
        tenant_id: T1
        governance_domain_id: domain-primary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T1
        governance_domain_id: domain-primary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-PROP-009-B
  extensions:
    x-agcp.test-vector: P-IDEM-009
```

### Expected result

```yaml
http:
  status: 409
  body:
    rejection_code: IDEMPOTENCY_CONFLICT
ledger_no_append: true
```

---

# Proposal Retrieval and External State

## TV-GET-001 — Get authorized Proposal View returns externally observable governance state and never SUBMITTED

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/proposals/${P_PROP_001}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 200
  body:
    proposal_id: ${P_PROP_001}
    governance_decision: Authorized
    execution_authorization: Authorized for Commit Boundary Processing
ledger_no_append: true
schema: proposal_view.json
```

---

## TV-GET-002 — Pre-decision proposal state is not externally observable

### Initial conditions and setup

```yaml
auth_as: T1
fixtures:
  create_proposal_with_ledger_only:
    tenant_id: T1
    proposal_id: P_TRANSIENT_002
    ledger_entries:
    - stage: Proposal Qualification
      data:
        started: true
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/proposals/P_TRANSIENT_002
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 404
  body:
    rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

# Governance Approval and Adjudication

## TV-GAPP-001 — Partial Governance Approval quorum -> Pending Human Review outcome remains

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/proposals/submit
  headers:
    Idempotency-Key: K_GAPP_001
  body:
    proposal:
      tenant_id: T1
      governance_domain_id: domain-primary
      proposal_identity:
        proposal_id: P-GAPP-001
        tenant_id: T1
        governance_domain_id: domain-primary
        canonical_content_digest:
          algorithm: SHA-256
          value: '3333333333333333333333333333333333333333333333333333333333333333'
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T1
          governance_domain_id: domain-primary
      proposal_kind: SIMPLE
      operational_intent:
        intent_type: governance_approval_two_roles
        statement: Test governed action requiring Risk Officer and Security Lead approval.
      target:
        target_id: target-primary
        target_type: TEST_RESOURCE
        tenant_id: T1
        governance_domain_id: domain-primary
      requested_effect:
        effect_type: governance_approval_two_roles
        effect_representation:
          action_type: governance_approval_two_roles
          parameters: {}
        effect_digest:
          algorithm: SHA-256
          value: '4444444444444444444444444444444444444444444444444444444444444444'
      policy_refs:
      - policy_id: P1
        policy_version: 1.0.0
        policy_digest:
          algorithm: SHA-256
          value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        artifact_uri: https://agcp.example/policies/P1
        tenant_id: T1
        governance_domain_id: domain-primary
        status: Active
      action_representation:
        representation_type: agcp.test.action
        representation_version: 1.0.0
        content_type: application/json
        canonicalization: JCS
        payload:
          action_type: governance_approval_two_roles
          parameters: {}
        payload_digest:
          algorithm: SHA-256
          value: '5555555555555555555555555555555555555555555555555555555555555555'
      governance_context:
        governance_context_id: GCX-P-GAPP-001
        governance_context_version: 1.0.0
        proposal_identity:
          proposal_id: P-GAPP-001
          tenant_id: T1
          governance_domain_id: domain-primary
          canonical_content_digest:
            algorithm: SHA-256
            value: '3333333333333333333333333333333333333333333333333333333333333333'
          originator:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
        tenant_id: T1
        governance_domain_id: domain-primary
        attribution:
          principal:
            principal_id: client:test
            principal_type: SERVICE
            tenant_id: T1
            governance_domain_id: domain-primary
          attributed_at: '2026-07-30T16:00:00Z'
        created_at: '2026-07-30T16:00:00Z'
        context_digest:
          algorithm: SHA-256
          value: '6666666666666666666666666666666666666666666666666666666666666666'
        canonical_state_ref:
          canonical_state_id: CS1
          canonical_state_version: 1.0.0
          canonical_state_digest:
            algorithm: SHA-256
            value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
          resolved_at: '2026-07-30T16:00:00Z'
        authority_lineage_ref:
          authority_lineage_id: AL1
          lineage_version: 1.0.0
          lineage_digest:
            algorithm: SHA-256
            value: '1111111111111111111111111111111111111111111111111111111111111111'
          proposal_id: P-GAPP-001
          tenant_id: T1
          governance_domain_id: domain-primary
        governance_configuration_ref:
          governance_configuration_id: CFG1
          configuration_version: 1.0.0
          configuration_status: ACTIVE
          configuration_digest:
            algorithm: SHA-256
            value: '2222222222222222222222222222222222222222222222222222222222222222'
          governance_version_ref:
            governance_version_id: GV1
            version: 1.0.0
          tenant_id: T1
          governance_domain_id: domain-primary
          effective_at: '2026-07-30T16:00:00Z'
      provenance:
        signer: client:test
        signature:
          alg: Ed25519
          kid: kid-test
          sig: SIG_VALID_123
        signed_at: '2026-07-30T16:00:00Z'
    submitted_at: '2026-07-30T16:00:00Z'
    client_request_id: CR-TV-GAPP-001
    extensions:
      x-agcp.test-vector: P-GAPP-001
  hooks:
    pec:
      constraints_outcome: PASS
      invariants_hard_fail: false
      governance_approval_required: true
      required_approval_roles:
      - RISK_OFFICER
      - SECURITY_LEAD
  expect_status: 200
  expect_body:
    governance_decision: Pending Human Review
  capture:
    save_proposal_id_as: P_GAPP_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/${P_GAPP_001}/governance-approvals
headers:
  Idempotency-Key: K_GAPP_001_APPROVAL
body:
  tenant_id: T1
  governance_domain_id: domain-primary
  provenance:
    signer: client:test
    signature:
      alg: Ed25519
      kid: kid-test
      sig: SIG_VALID
    signed_at: '2026-02-25T12:00:00Z'
  governance_approval_artifact:
    $fixture: ../schemas/examples/ds026-governance-approval-partial-quorum.json
    $overrides:
      proposal_identity.proposal_id: ${P_GAPP_001}
      proposal_identity.tenant_id: T1
      proposal_identity.governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      target.tenant_id: T1
      target.governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 200
  body:
    governance_decision: Pending Human Review
    quorum_satisfied: false
ledger_append:
- stage: Governance Decision Function
  match:
    governance_approval_recorded: true
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
governance_evidence:
  required: true
  requires_ledger_reference: true
schema: proposal_view.json
```

---

## TV-GAPP-002 — Valid Governance Approval Artifact completes quorum -> Execution Authorization available

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_002
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/${P_PROP_002}/governance-approvals
headers:
  Idempotency-Key: K_GAPP_002
body:
  tenant_id: T1
  governance_domain_id: domain-primary
  provenance:
    signer: client:test
    signature:
      alg: Ed25519
      kid: kid-test
      sig: SIG_VALID
    signed_at: '2026-02-25T12:00:00Z'
  governance_approval_artifact:
    $fixture: ../schemas/examples/ds026-governance-approval-completed-quorum.json
    $overrides:
      proposal_identity.proposal_id: ${P_PROP_002}
      proposal_identity.tenant_id: T1
      proposal_identity.governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      target.tenant_id: T1
      target.governance_domain_id: domain-primary
```

### Captured values

```yaml
save_authorization_id_as: EA_GAPP_002
```

### Expected result

```yaml
http:
  status: 200
  body:
    governance_decision: Authorized
    execution_authorization: Authorized for Commit Boundary Processing
ledger_append:
- stage: Governance Decision Function
  match:
    governance_approval_quorum_satisfied: true
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
- stage: Execution Authorization
  match:
    outcome: Authorized for Commit Boundary Processing
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
schema: proposal_view.json
```

---

## TV-GAPP-003 — Expired Governance Approval Artifact -> GOVERNANCE_APPROVAL_EXPIRED

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_002
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/${P_PROP_002}/governance-approvals
headers:
  Idempotency-Key: K_GAPP_003
body:
  tenant_id: T1
  governance_domain_id: domain-primary
  provenance:
    signer: client:test
    signature:
      alg: Ed25519
      kid: kid-test
      sig: SIG_VALID
    signed_at: '2026-02-25T12:00:00Z'
  governance_approval_artifact:
    $fixture: ../schemas/examples/ds026-governance-approval-partial-quorum.json
    $overrides:
      proposal_identity.proposal_id: ${P_PROP_002}
      proposal_identity.tenant_id: T1
      proposal_identity.governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      target.tenant_id: T1
      target.governance_domain_id: domain-primary
      status: EXPIRED
      artifact_termination:
        termination_type: EXPIRED
        effective_at: '2026-07-30T16:00:00Z'
        reason_code: VALIDITY_WINDOW_EXPIRED
        reason: The Governance Approval Artifact validity window expired before use.
        terminated_by:
          principal:
            principal_id: approval-lifecycle-service
            principal_type: SYSTEM
          attributed_at: '2026-07-30T16:00:00Z'
        termination_authority_lineage_ref:
          authority_lineage_id: authority-lineage-1
          authority_lineage_digest:
            algorithm: SHA-256
            value: '3333333333333333333333333333333333333333333333333333333333333333'
          lineage_version: 2.0.0
          evaluated_at: '2026-07-30T16:00:00Z'
        governance_evidence_refs:
        - governance_evidence_id: evidence-expiration-1
          evidence_digest:
            algorithm: SHA-256
            value: '9999999999999999999999999999999999999999999999999999999999999999'
```

### Expected result

```yaml
http:
  status: 409
  body:
    rejection_code: GOVERNANCE_APPROVAL_EXPIRED
ledger_no_append: true
```

---

## TV-GAPP-004 — Schema-valid Governance Approval Artifact with invalid signature material -> GOVERNANCE_APPROVAL_INVALID

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_002
hooks:
  cryptographic_verifier:
    governance_approval_artifact:
      independent_verification_required: true
      target_artifact_id: approval-partial-1
      signature_valid: false
      key_binding_valid: false
      artifact_digest_binding_valid: false
      failure_reason: INVALID_SIGNATURE_AND_KEY_BINDING
      rejection_code: GOVERNANCE_APPROVAL_INVALID
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/${P_PROP_002}/governance-approvals
headers:
  Idempotency-Key: K_GAPP_004
body:
  tenant_id: T1
  governance_domain_id: domain-primary
  provenance:
    signer: client:test
    signature:
      alg: Ed25519
      kid: kid-test
      sig: SIG_VALID
    signed_at: '2026-02-25T12:00:00Z'
  governance_approval_artifact:
    $fixture: ../schemas/examples/ds026-governance-approval-partial-quorum.json
    $overrides:
      proposal_identity.proposal_id: ${P_PROP_002}
      proposal_identity.tenant_id: T1
      proposal_identity.governance_domain_id: domain-primary
      tenant_id: T1
      governance_domain_id: domain-primary
      target.tenant_id: T1
      target.governance_domain_id: domain-primary
      cryptographic_verification.verification_outcome: VERIFIED
      cryptographic_verification.signature.kid: key-unbound-tv-gapp-004
      cryptographic_verification.signature.sig: SIG_INVALID_FOR_ARTIFACT_DIGEST
```

### Expected result

```yaml
request_validation:
  governance_approval_request: PASS
  governance_approval_artifact_ds026: PASS
semantic_verification:
  cryptographic_verifier_invoked: true
  signature_valid: false
  key_binding_valid: false
  artifact_digest_binding_valid: false
  outcome: FAILED
  rejection_code: GOVERNANCE_APPROVAL_INVALID
http:
  status: 422
  body:
    rejection_code: GOVERNANCE_APPROVAL_INVALID
ledger_no_append: true
```

---

# Governance Realization and Commit Boundary

## TV-COMMIT-001 — Commit Boundary succeeds with valid Execution Authorization

### Initial conditions and setup

```yaml
auth_as: T1
use_authorization_id: EA_PROP_001
hooks:
  tenant_state:
    T1: ACTIVE
read_execution_authorization:
  authorization_id: ${EA_PROP_001}
  save_as: EA_VIEW_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_COMMIT_001
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_PROP_001}
    proposal_ref.proposal_identity.tenant_id: T1
    proposal_ref.proposal_identity.governance_domain_id: domain-primary
    proposal_ref.target_ref.tenant_id: T1
    proposal_ref.target_ref.governance_domain_id: domain-primary
    action_id: A_PROP_001
    governance_decision_ref.governance_decision_id: GD_PROP_001
    execution_authorization_ref.authorization_id: ${EA_PROP_001}
    enforcement_context.proposal_identity.proposal_id: ${P_PROP_001}
    enforcement_context.proposal_identity.tenant_id: T1
    enforcement_context.proposal_identity.governance_domain_id: domain-primary
    enforcement_context.action_id: A_PROP_001
    enforcement_context.tenant_id: T1
    enforcement_context.governance_domain_id: domain-primary
    enforcement_context.governance_decision_ref.governance_decision_id: GD_PROP_001
    enforcement_context.execution_authorization_ref.authorization_id: ${EA_PROP_001}
```

### Captured values

```yaml
save_commit_boundary_ref_as: CB_COMMIT_001
save_governance_evidence_refs_as: EV_COMMIT_001
```

### Expected result

```yaml
http:
  status: 200
  body:
    commit_boundary_outcome: Commit Successful
ledger_append:
- stage: Commit Boundary
  match:
    outcome: Commit Successful
  ledger_event:
    required: true
    schema: governance_ledger_event.json
    validate_required_structures:
    - ordering_scope
    - ledger_position
    - event_subject
    - event_artifact_refs
    - governance_basis
    - evidence_binding
    - causality
    - event_time
    - append_only_controls
    - integrity_protection
    - attribution
    - provenance
    - replay_material
    - semantic_assertions
governance_evidence:
  required: true
  requires_ledger_reference: true
schema_fixture: ../schemas/examples/ds019-commit-boundary-result-success.json
schema: commit_boundary_result.json
```

---

## TV-COMMIT-002 — Commit Boundary while governed approval remains incomplete -> ACTION_NOT_AUTHORIZED

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_GAPP_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_COMMIT_002
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_GAPP_001}
    proposal_ref.proposal_identity.tenant_id: T1
    proposal_ref.proposal_identity.governance_domain_id: domain-primary
    proposal_ref.target_ref.tenant_id: T1
    proposal_ref.target_ref.governance_domain_id: domain-primary
    action_id: A_PENDING
    governance_decision_ref.governance_decision_id: governance-decision-pending
    execution_authorization_ref.authorization_id: EA_SHOULD_NOT_EXIST
    enforcement_context.proposal_identity.proposal_id: ${P_GAPP_001}
    enforcement_context.proposal_identity.tenant_id: T1
    enforcement_context.proposal_identity.governance_domain_id: domain-primary
    enforcement_context.action_id: A_PENDING
    enforcement_context.tenant_id: T1
    enforcement_context.governance_domain_id: domain-primary
    enforcement_context.governance_decision_ref.governance_decision_id: governance-decision-pending
    enforcement_context.execution_authorization_ref.authorization_id: EA_SHOULD_NOT_EXIST
```

### Expected result

```yaml
http:
  status: 409
  body:
    rejection_code: ACTION_NOT_AUTHORIZED
ledger_no_append: true
```

---

## TV-COMMIT-003 — Commit Boundary with mismatched authorization -> ACTION_NOT_AUTHORIZED

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_COMMIT_003
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_PROP_001}
    proposal_ref.proposal_identity.tenant_id: T1
    proposal_ref.proposal_identity.governance_domain_id: domain-primary
    proposal_ref.target_ref.tenant_id: T1
    proposal_ref.target_ref.governance_domain_id: domain-primary
    action_id: A_PROP_001
    governance_decision_ref.governance_decision_id: GD_PROP_001
    execution_authorization_ref.authorization_id: EA_BAD
    enforcement_context.proposal_identity.proposal_id: ${P_PROP_001}
    enforcement_context.proposal_identity.tenant_id: T1
    enforcement_context.proposal_identity.governance_domain_id: domain-primary
    enforcement_context.action_id: A_PROP_001
    enforcement_context.tenant_id: T1
    enforcement_context.governance_domain_id: domain-primary
    enforcement_context.governance_decision_ref.governance_decision_id: GD_PROP_001
    enforcement_context.execution_authorization_ref.authorization_id: EA_BAD
```

### Expected result

```yaml
http:
  status: 409
  body:
    rejection_code: ACTION_NOT_AUTHORIZED
ledger_no_append: true
governance_refusal_fixture: ../schemas/examples/ds019-commit-boundary-result-refusal.json
```

---

## TV-COMMIT-004 — Commit replay after Commit Successful -> ACTION_NOT_AUTHORIZED

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
ensure_commit_boundary_outcome: Commit Successful
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_COMMIT_004
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_PROP_001}
    proposal_ref.proposal_identity.tenant_id: T1
    proposal_ref.proposal_identity.governance_domain_id: domain-primary
    proposal_ref.target_ref.tenant_id: T1
    proposal_ref.target_ref.governance_domain_id: domain-primary
    action_id: A_PROP_001
    governance_decision_ref.governance_decision_id: GD_PROP_001
    execution_authorization_ref.authorization_id: ${EA_PROP_001}
    enforcement_context.proposal_identity.proposal_id: ${P_PROP_001}
    enforcement_context.proposal_identity.tenant_id: T1
    enforcement_context.proposal_identity.governance_domain_id: domain-primary
    enforcement_context.action_id: A_PROP_001
    enforcement_context.tenant_id: T1
    enforcement_context.governance_domain_id: domain-primary
    enforcement_context.governance_decision_ref.governance_decision_id: GD_PROP_001
    enforcement_context.execution_authorization_ref.authorization_id: ${EA_PROP_001}
```

### Expected result

```yaml
http:
  status: 409
  body:
    rejection_code: ACTION_NOT_AUTHORIZED
ledger_no_append: true
```

---

## TV-COMMIT-005 — Commit Boundary when tenant not ACTIVE -> TENANT_STATE_INVALID

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
hooks:
  tenant_state:
    T1: SUSPENDED
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_COMMIT_005
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_PROP_001}
    proposal_ref.proposal_identity.tenant_id: T1
    proposal_ref.proposal_identity.governance_domain_id: domain-primary
    proposal_ref.target_ref.tenant_id: T1
    proposal_ref.target_ref.governance_domain_id: domain-primary
    action_id: A_PROP_001
    governance_decision_ref.governance_decision_id: GD_PROP_001
    execution_authorization_ref.authorization_id: ${EA_PROP_001}
    enforcement_context.proposal_identity.proposal_id: ${P_PROP_001}
    enforcement_context.proposal_identity.tenant_id: T1
    enforcement_context.proposal_identity.governance_domain_id: domain-primary
    enforcement_context.action_id: A_PROP_001
    enforcement_context.tenant_id: T1
    enforcement_context.governance_domain_id: domain-primary
    enforcement_context.governance_decision_ref.governance_decision_id: GD_PROP_001
    enforcement_context.execution_authorization_ref.authorization_id: ${EA_PROP_001}
```

### Expected result

```yaml
http:
  status: 403
  body:
    rejection_code: TENANT_STATE_INVALID
ledger_no_append: true
```

---

# Governance Evidence

## TV-EVID-001 — Governance Evidence view validates DS-040 Governance Ledger Event references

### Initial conditions and setup

```yaml
auth_as: T1
use_governance_evidence_ref: ${EV_PROP_001[0]}
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/governance-evidence/${EV_PROP_001[0]}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 200
  body:
    governance_evidence_id: ${EV_PROP_001[0]}
    ledger_event_refs:
    - ledger_event_id: __PRESENT__
      event_version: __PRESENT__
      event_type: __PRESENT__
      event_category: __PRESENT__
      ledger_position:
        ledger_id: __PRESENT__
        stream_id: __PRESENT__
        sequence: __PRESENT__
        event_id: __PRESENT__
        event_digest: __PRESENT__
        chain_digest: __PRESENT__
        stream_head_after_append: true
      tenant_id: __PRESENT__
      governance_domain_id: __PRESENT__
      event_digest: __PRESENT__
      appended_at: __PRESENT__
schema: governance_evidence.json
ledger_no_append: true
```

---

# Canonical State Resolution

## TV-STATE-001 — Canonical State resolution from qualified authoritative sources succeeds

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
fixtures:
  qualified_authoritative_sources_for: ${P_PROP_001}
  ordered_ledger_history_for: ${P_PROP_001}
```

### Request or harness operation

```yaml
harness_operation: resolve_canonical_state
source_set: qualified_authoritative_governance_sources
proposal_id: ${P_PROP_001}
```

### Expected result

```yaml
canonical_state:
  matches: ${canonical_state_ref.valid}
  resolved_from_qualified_authoritative_sources: true
  incorporated_ledger_records_use_authoritative_ordering: true
governance_evidence:
  integrity_verified: true
source_provenance:
  verified: true
```

---

## TV-STATE-002 — Canonical State resolution rejects reordered incorporated ledger history

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_PROP_001
fixtures:
  qualified_authoritative_sources_for: ${P_PROP_001}
  reordered_same_ledger_entries_for: ${P_PROP_001}
```

### Request or harness operation

```yaml
harness_operation: resolve_canonical_state
source_set: qualified_authoritative_sources_with_reordered_ledger_component
proposal_id: ${P_PROP_001}
```

### Expected result

```yaml
result:
  ledger_derived_state_accepted_as_equivalent: false
must_reject_or_produce_non_equivalent_ledger_derived_state: true
timestamp_or_storage_order_must_not_override_sequence_order: true
```

---

# Cross-Tenant Isolation

## TV-XTEN-SETUP — Setup tenant T2 proposal for cross-tenant tests

### Traceability and applicability

```yaml
profiles:
- L1
- L2
- L3
- L4
concepts:
- Proposal Qualification
- Tenant and Governance Domain Isolation
- Execution Authorization
```

### Initial conditions and setup

```yaml
auth_as: T2
hooks:
  tenant_state:
    T2: ACTIVE
  policy_resolution:
    P1: found
  pec:
    constraints_outcome: PASS
    invariants_hard_fail: false
    governance_approval_required: false
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/submit
headers:
  Idempotency-Key: K_XTEN_SETUP
body:
  proposal:
    tenant_id: T2
    governance_domain_id: domain-secondary
    proposal_identity:
      proposal_id: P-XTEN-SETUP
      tenant_id: T2
      governance_domain_id: domain-secondary
      canonical_content_digest:
        algorithm: SHA-256
        value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      originator:
        principal_id: client:test
        principal_type: SERVICE
        tenant_id: T2
        governance_domain_id: domain-secondary
    proposal_kind: SIMPLE
    operational_intent:
      intent_type: belongs_to_T2
      statement: Test governed action belongs_to_T2.
    target:
      target_id: target-secondary
      target_type: TEST_RESOURCE
      tenant_id: T2
      governance_domain_id: domain-secondary
    requested_effect:
      effect_type: belongs_to_T2
      effect_representation:
        action_type: belongs_to_T2
        parameters:
          tenant_marker: T2
      effect_digest:
        algorithm: SHA-256
        value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    policy_refs:
    - policy_id: P1
      policy_version: 1.0.0
      policy_digest:
        algorithm: SHA-256
        value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
      artifact_uri: https://agcp.example/policies/P1
      tenant_id: T2
      governance_domain_id: domain-secondary
      status: Active
    action_representation:
      representation_type: agcp.test.action
      representation_version: 1.0.0
      content_type: application/json
      canonicalization: JCS
      payload:
        action_type: belongs_to_T2
        parameters:
          tenant_marker: T2
      payload_digest:
        algorithm: SHA-256
        value: dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    governance_context:
      governance_context_id: GCX-P-XTEN-SETUP
      governance_context_version: 1.0.0
      proposal_identity:
        proposal_id: P-XTEN-SETUP
        tenant_id: T2
        governance_domain_id: domain-secondary
        canonical_content_digest:
          algorithm: SHA-256
          value: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        originator:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T2
          governance_domain_id: domain-secondary
      tenant_id: T2
      governance_domain_id: domain-secondary
      attribution:
        principal:
          principal_id: client:test
          principal_type: SERVICE
          tenant_id: T2
          governance_domain_id: domain-secondary
        attributed_at: '2026-07-30T16:00:00Z'
      created_at: '2026-07-30T16:00:00Z'
      context_digest:
        algorithm: SHA-256
        value: eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      canonical_state_ref:
        canonical_state_id: CS1
        canonical_state_version: 1.0.0
        canonical_state_digest:
          algorithm: SHA-256
          value: ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        resolved_at: '2026-07-30T16:00:00Z'
      authority_lineage_ref:
        authority_lineage_id: AL1
        lineage_version: 1.0.0
        lineage_digest:
          algorithm: SHA-256
          value: '1111111111111111111111111111111111111111111111111111111111111111'
        proposal_id: P-XTEN-SETUP
        tenant_id: T2
        governance_domain_id: domain-secondary
      governance_configuration_ref:
        governance_configuration_id: CFG1
        configuration_version: 1.0.0
        configuration_status: ACTIVE
        configuration_digest:
          algorithm: SHA-256
          value: '2222222222222222222222222222222222222222222222222222222222222222'
        governance_version_ref:
          governance_version_id: GV1
          version: 1.0.0
        tenant_id: T2
        governance_domain_id: domain-secondary
        effective_at: '2026-07-30T16:00:00Z'
    provenance:
      signer: client:test
      signature:
        alg: Ed25519
        kid: kid-test
        sig: SIG_VALID_123
      signed_at: '2026-07-30T16:00:00Z'
  submitted_at: '2026-07-30T16:00:00Z'
  client_request_id: CR-TV-XTEN-SETUP
  extensions:
    x-agcp.test-vector: TV-XTEN-SETUP
```

### Captured values

```yaml
save_proposal_id_as: P_T2_001
save_authorization_id_as: EA_T2_001
save_governance_evidence_refs_as: EV_T2_001
```

### Expected result

```yaml
http:
  status: 200
  body:
    qualification_outcome: Qualified Proposal
    governance_decision: Authorized
    execution_authorization: Authorized for Commit Boundary Processing
governance_evidence:
  required: true
  schema: governance_evidence.json
  requires_ledger_reference: true
```

---

## TV-XTEN-001 — Cross-tenant Proposal View access is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_T2_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/proposals/${P_T2_001}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-XTEN-002 — Cross-tenant Governance Approval Artifact submission is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_T2_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/proposals/${P_T2_001}/governance-approvals
headers:
  Idempotency-Key: K_XTEN_002
body:
  tenant_id: T1
  governance_domain_id: domain-primary
  provenance:
    signer: client:test
    signature:
      alg: Ed25519
      kid: kid-test
      sig: SIG_VALID
    signed_at: '2026-02-25T12:00:00Z'
  governance_approval_artifact:
    $fixture: ../schemas/examples/ds026-governance-approval-partial-quorum.json
    $overrides:
      proposal_identity.proposal_id: ${P_T2_001}
      proposal_identity.tenant_id: T2
      proposal_identity.governance_domain_id: domain-secondary
      tenant_id: T2
      governance_domain_id: domain-secondary
      target.tenant_id: T2
      target.governance_domain_id: domain-secondary
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-XTEN-003 — Cross-tenant Commit Boundary is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
use_proposal_id: P_T2_001
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/commit-boundary/commit
headers:
  Idempotency-Key: K_XTEN_003
body:
  $fixture: ../schemas/examples/ds018-commit-boundary-request-single.json
  $overrides:
    tenant_id: T1
    governance_domain_id: domain-primary
    proposal_ref.proposal_identity.proposal_id: ${P_T2_001}
    proposal_ref.proposal_identity.tenant_id: T2
    proposal_ref.proposal_identity.governance_domain_id: domain-secondary
    proposal_ref.target_ref.tenant_id: T2
    proposal_ref.target_ref.governance_domain_id: domain-secondary
    action_id: A_T2_001
    governance_decision_ref.governance_decision_id: GD_T2_001
    execution_authorization_ref.authorization_id: ${EA_T2_001}
    enforcement_context.proposal_identity.proposal_id: ${P_T2_001}
    enforcement_context.proposal_identity.tenant_id: T2
    enforcement_context.proposal_identity.governance_domain_id: domain-secondary
    enforcement_context.action_id: A_T2_001
    enforcement_context.tenant_id: T2
    enforcement_context.governance_domain_id: domain-secondary
    enforcement_context.governance_decision_ref.governance_decision_id: GD_T2_001
    enforcement_context.execution_authorization_ref.authorization_id: ${EA_T2_001}
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-XTEN-004 — Cross-tenant Governance Evidence access is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
use_governance_evidence_ref: EV_T2_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/governance-evidence/EV_T2_001
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-META-001 — Implementation metadata advertises the controlled IF-001 and conformance surface

### Initial conditions and setup

```yaml
{}
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/meta
```

### Expected result

```yaml
http:
  status: 200
  body:
    response_type: AGCP_IMPLEMENTATION_METADATA
    default_agcp_release_id: AGCP-v2.0.0
    http_contract:
      supported_path_versions:
      - /agcp/v2
schema: meta_response.json
ledger_no_append: true
schema_fixture: ../schemas/examples/ds003-implementation-metadata-response.json
```

---

## TV-EAUTH-001 — Retrieve an available Execution Authorization view

### Initial conditions and setup

```yaml
auth_as: T1
use_authorization_id: EA_PROP_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/execution-authorizations/${EA_PROP_001}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 200
  body:
    authorization_id: ${EA_PROP_001}
    authorized_for_commit_boundary: true
    consumption_state: AVAILABLE
schema: execution_authorization_view.json
ledger_no_append: true
schema_fixture: ../schemas/examples/ds017-execution-authorization-view-authorized.json
```

---

## TV-EAUTH-002 — Unknown Execution Authorization is not found

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/execution-authorizations/EA-NOT-FOUND
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 404
  body:
    rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-EAUTH-003 — Cross-tenant Execution Authorization access is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
use_authorization_id: EA_T2_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/execution-authorizations/${EA_T2_001}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-PEM-001 — Register a schema-valid Policy Evaluation Module without activating it

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policy-modules
headers:
  Idempotency-Key: K_PEM_001
body:
  $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  $overrides:
    module_id: PEM-TV-001
    tenant_id: T1
    governance_domain_id: domain-primary
```

### Expected result

```yaml
request_validation:
  policy_evaluation_module_artifact: PASS
http:
  status: 200
  body:
    artifact_identity:
      artifact_type: POLICY_EVALUATION_MODULE
    artifact_status: Registered
    tenant_id: T1
    governance_domain_id: domain-primary
schema: governance_artifact_view.json
capture:
  save_governance_artifact_id_as: GART_PEM_001
governance_activation_occurred: false
schema_fixture: ../schemas/examples/ds010-governance-artifact-view-registered.json
```

---

## TV-PEM-002 — Malformed Policy Evaluation Module registration is rejected before governance processing

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policy-modules
headers:
  Idempotency-Key: K_PEM_002
body:
  $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  $overrides:
    module_id: ''
```

### Expected result

```yaml
request_validation:
  policy_evaluation_module_artifact: FAIL
http:
  status: 400
  body:
    rejection_code: SCHEMA_VALIDATION_FAILED
ledger_no_append: true
```

---

## TV-PEM-003 — Cross-tenant Policy Evaluation Module registration is forbidden

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policy-modules
headers:
  Idempotency-Key: K_PEM_003
body:
  $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  $overrides:
    module_id: PEM-TV-T2-003
    tenant_id: T2
    governance_domain_id: domain-secondary
    effective_scope.tenant_id: T2
    governance_configuration_binding.tenant_id: T2
    governance_configuration_binding.governance_domain_id: domain-secondary
    supported_policy_refs[0].tenant_id: T2
    supported_policy_refs[0].governance_domain_id: domain-secondary
```

### Expected result

```yaml
request_validation:
  policy_evaluation_module_artifact: PASS
http:
  status: 403
  body:
    rejection_code: TENANT_SCOPE_VIOLATION
ledger_no_append: true
```

---

## TV-PEM-004 — Equivalent Policy Evaluation Module registration replay is idempotent

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/governance-artifacts/policy-modules
  headers:
    Idempotency-Key: K_PEM_004
  body:
    $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
    $overrides:
      module_id: PEM-TV-004
  expect_status: 200
  capture:
    save_governance_artifact_id_as: GART_PEM_004
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policy-modules
headers:
  Idempotency-Key: K_PEM_004
body:
  $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  $overrides:
    module_id: PEM-TV-004
```

### Expected result

```yaml
request_validation:
  policy_evaluation_module_artifact: PASS
http:
  status: 200
  body:
    artifact_identity:
      artifact_id: ${GART_PEM_004}
ledger_no_append: true
equivalent_to_prestep_response: true
```

---

## TV-PEM-005 — Conflicting Policy Evaluation Module registration replay is rejected

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/governance-artifacts/policy-modules
  headers:
    Idempotency-Key: K_PEM_005
  body:
    $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
    $overrides:
      module_id: PEM-TV-005
      module_version: 1.0.0
  expect_status: 200
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policy-modules
headers:
  Idempotency-Key: K_PEM_005
body:
  $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  $overrides:
    module_id: PEM-TV-005
    module_version: 1.0.1
    module_digest.value: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
```

### Expected result

```yaml
request_validation:
  policy_evaluation_module_artifact: PASS
http:
  status: 409
  body:
    rejection_code: IDEMPOTENCY_CONFLICT
ledger_no_append: true
```

---

## TV-POL-001 — Register a schema-valid Governance Policy without activating it

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policies
headers:
  Idempotency-Key: K_POL_001
body:
  $fixture: ../schemas/examples/ds006-governance-policy-registered.json
  $overrides:
    policy_id: POLICY-TV-001
    tenant_id: T1
    governance_domain_id: domain-primary
```

### Expected result

```yaml
request_validation:
  governance_policy_artifact: PASS
http:
  status: 200
  body:
    artifact_identity:
      artifact_type: GOVERNANCE_POLICY
    artifact_status: Registered
    tenant_id: T1
    governance_domain_id: domain-primary
schema: governance_artifact_view.json
capture:
  save_governance_artifact_id_as: GART_POL_001
governance_activation_occurred: false
schema_fixture: ../schemas/examples/ds010-governance-artifact-view-registered.json
```

---

## TV-POL-002 — Malformed Governance Policy registration is rejected before governance processing

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policies
headers:
  Idempotency-Key: K_POL_002
body:
  $fixture: ../schemas/examples/ds006-governance-policy-registered.json
  $overrides:
    policy_id: ''
```

### Expected result

```yaml
request_validation:
  governance_policy_artifact: FAIL
http:
  status: 400
  body:
    rejection_code: SCHEMA_VALIDATION_FAILED
ledger_no_append: true
```

---

## TV-POL-003 — Cross-tenant Governance Policy registration is forbidden

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policies
headers:
  Idempotency-Key: K_POL_003
body:
  $fixture: ../schemas/examples/ds006-governance-policy-registered.json
  $overrides:
    policy_id: POLICY-TV-T2-003
    tenant_id: T2
    governance_domain_id: domain-secondary
    effective_scope.tenant_id: T2
    governance_configuration_binding.tenant_id: T2
    governance_configuration_binding.governance_domain_id: domain-secondary
```

### Expected result

```yaml
request_validation:
  governance_policy_artifact: PASS
http:
  status: 403
  body:
    rejection_code: TENANT_SCOPE_VIOLATION
ledger_no_append: true
```

---

## TV-POL-004 — Equivalent Governance Policy registration replay is idempotent

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/governance-artifacts/policies
  headers:
    Idempotency-Key: K_POL_004
  body:
    $fixture: ../schemas/examples/ds006-governance-policy-registered.json
    $overrides:
      policy_id: POLICY-TV-004
  expect_status: 200
  capture:
    save_governance_artifact_id_as: GART_POL_004
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policies
headers:
  Idempotency-Key: K_POL_004
body:
  $fixture: ../schemas/examples/ds006-governance-policy-registered.json
  $overrides:
    policy_id: POLICY-TV-004
```

### Expected result

```yaml
request_validation:
  governance_policy_artifact: PASS
http:
  status: 200
  body:
    artifact_identity:
      artifact_id: ${GART_POL_004}
ledger_no_append: true
equivalent_to_prestep_response: true
```

---

## TV-POL-005 — Conflicting Governance Policy registration replay is rejected

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/governance-artifacts/policies
  headers:
    Idempotency-Key: K_POL_005
  body:
    $fixture: ../schemas/examples/ds006-governance-policy-registered.json
    $overrides:
      policy_id: POLICY-TV-005
      policy_version: 1.0.0
  expect_status: 200
```

### Request or harness operation

```yaml
method: POST
path: /agcp/v2/governance-artifacts/policies
headers:
  Idempotency-Key: K_POL_005
body:
  $fixture: ../schemas/examples/ds006-governance-policy-registered.json
  $overrides:
    policy_id: POLICY-TV-005
    policy_version: 1.0.1
    policy_digest.value: cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
```

### Expected result

```yaml
request_validation:
  governance_policy_artifact: PASS
http:
  status: 409
  body:
    rejection_code: IDEMPOTENCY_CONFLICT
ledger_no_append: true
```

---

## TV-GART-001 — Retrieve a registered Governance Artifact view

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- method: POST
  path: /agcp/v2/governance-artifacts/policy-modules
  headers:
    Idempotency-Key: K_GART_001_SETUP
  body:
    $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
    $overrides:
      module_id: PEM-GART-001
  expect_status: 200
  capture:
    save_governance_artifact_id_as: GART_001
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/governance-artifacts/${GART_001}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 200
  body:
    governance_artifact_view_id: __PRESENT__
    artifact_status: Registered
    tenant_id: T1
    governance_domain_id: domain-primary
schema: governance_artifact_view.json
ledger_no_append: true
schema_fixture: ../schemas/examples/ds010-governance-artifact-view-registered.json
```

---

## TV-GART-002 — Unknown Governance Artifact is not found

### Initial conditions and setup

```yaml
auth_as: T1
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/governance-artifacts/ART-NOT-FOUND
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status: 404
  body:
    rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-GART-003 — Cross-tenant Governance Artifact access is forbidden or hidden

### Initial conditions and setup

```yaml
auth_as: T1
presteps:
- auth_as: T2
  method: POST
  path: /agcp/v2/governance-artifacts/policy-modules
  headers:
    Idempotency-Key: K_GART_003_SETUP
  body:
    $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
    $overrides:
      module_id: PEM-GART-T2-003
      tenant_id: T2
      governance_domain_id: domain-secondary
      effective_scope.tenant_id: T2
      governance_configuration_binding.tenant_id: T2
      governance_configuration_binding.governance_domain_id: domain-secondary
      supported_policy_refs[0].tenant_id: T2
      supported_policy_refs[0].governance_domain_id: domain-secondary
  expect_status: 200
  capture:
    save_governance_artifact_id_as: GART_T2_003
```

### Request or harness operation

```yaml
method: GET
path: /agcp/v2/governance-artifacts/${GART_T2_003}
query:
  tenant_id: T1
  governance_domain_id: domain-primary
```

### Expected result

```yaml
http:
  status_by_strategy:
    FORBID_403:
      status: 403
      body:
        rejection_code: TENANT_SCOPE_VIOLATION
    HIDE_404:
      status: 404
      body:
        rejection_code: RESOURCE_NOT_FOUND
ledger_no_append: true
```

---

## TV-GCFG-001 — Validate active Governance Configuration, controlled change requirements, and risk-based re-evaluation configuration

### Initial conditions and setup

```yaml
fixtures:
  governance_configuration: ../schemas/examples/ds041-governance-configuration-active.json
authoritative_active_governance_version: gv-2.0.0
```

### Request or harness operation

```yaml
harness_operation: validate_governance_configuration
artifact:
  $fixture: ../schemas/examples/ds041-governance-configuration-active.json
validation_scope:
- SCHEMA
- CONFIGURATION_MANIFEST
- CHANGE_CONTROL
- RISK_BASED_RE_EVALUATION
- SELF_MODIFICATION_ISOLATION
```

### Expected result

```yaml
schema_validation:
  governance_configuration.json: PASS
configuration_status: ACTIVE
configuration_manifest:
  manifest_complete: true
  hidden_configuration_present: false
  implicit_configuration_influences_decisions: false
change_control:
  governance_compilation_required: true
  constitutional_validation_required: true
  governance_omission_analysis_required: true
  controlled_activation_required: true
  direct_self_modification_prohibited: true
  prior_authoritative_version_preserved_on_failure: true
  external_approval_artifact_refs: __NON_EMPTY__
risk_based_re_evaluation_configuration:
  enabled: true
  deterministic_selection_required: true
  preserves_unaffected_proposals: true
  arrival_timing_used_as_governance_basis: false
  requires_attributable_outcome_evidence: true
semantic_assertions:
  configuration_establishes_authority_at_commitment: false
  configuration_authorizes_execution: false
  configuration_activates_itself: false
  governed_system_can_directly_modify_admissibility_conditions: false
governance_evidence_refs: __NON_EMPTY__
```

---

## TV-GCOMP-001 — Equivalent qualified governance inputs compile deterministically to the same machine-evaluable artifact and lineage

### Initial conditions and setup

```yaml
fixtures:
  governance_configuration: ../schemas/examples/ds041-governance-configuration-active.json
  policy_evaluation_module: ../schemas/examples/ds005-policy-evaluation-module-registered.json
  governance_policy: ../schemas/examples/ds006-governance-policy-registered.json
compiler:
  compiler_id: compiler-id-1
  compiler_version: 1.0.0
  deterministic_build_id: BUILD-F09-001
repeat_count: 2
```

### Request or harness operation

```yaml
harness_operation: compile_governance_configuration
governance_configuration:
  $fixture: ../schemas/examples/ds041-governance-configuration-active.json
source_artifacts:
- $fixture: ../schemas/examples/ds005-policy-evaluation-module-registered.json
- $fixture: ../schemas/examples/ds006-governance-policy-registered.json
compilation_mode: DETERMINISTIC_REPLAY
```

### Expected result

```yaml
compilation_runs: 2
each_output_schema_validation:
  compiled_governance_artifact.json: PASS
outputs_semantically_equivalent: true
artifact_digest_equal: true
machine_evaluable_representation_digest_equal: true
deterministic_build_id_equal: true
source_manifest_complete: true
validated_dependency_set_complete: true
governance_artifact_lineage:
  lineage_complete: true
  lineage_replayable: true
  source_to_output_traceability_complete: true
semantic_preservation:
  governance_intent_preserved: true
  constraints_preserved: true
  invariants_preserved: true
  refusal_paths_preserved: true
  evidence_requirements_preserved: true
  authority_rules_preserved: true
  commit_meaning_preserved: true
activation_eligibility: ELIGIBLE
does_not_establish_authority_or_activate: true
schema_fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
```

---

## TV-GCONST-001 — Constitutional validation preserves protected constraints and permits activation eligibility

### Initial conditions and setup

```yaml
fixtures:
  compiled_governance_artifact: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
```

### Request or harness operation

```yaml
harness_operation: validate_compiled_governance_artifact
artifact:
  $fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
validation_scope:
- CONSTITUTIONAL_VALIDATION
- SEMANTIC_PRESERVATION
- GOVERNANCE_SELF_PROTECTION
```

### Expected result

```yaml
schema_validation:
  compiled_governance_artifact.json: PASS
constitutional_validation_result:
  outcome: PASSED
  findings: []
semantic_preservation:
  protected_constraints_non_derogable: true
  constraints_preserved: true
  invariants_preserved: true
  refusal_paths_preserved: true
  commit_meaning_preserved: true
governance_self_protection_assessment:
  constitutional_constraints_preserved: true
  protected_safeguards_not_weakened: true
  governance_bypass_not_introduced: true
  required_safeguards_not_disabled: true
activation_eligibility: ELIGIBLE
governance_evidence_refs: __NON_EMPTY__
```

---

## TV-GCONST-002 — Attempted weakening of a protected constitutional constraint fails validation and cannot become activation-eligible

### Initial conditions and setup

```yaml
baseline_artifact:
  $fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
authoritative_active_governance_version: gv-2.0.0
```

### Request or harness operation

```yaml
harness_operation: compile_and_validate_governance_change
baseline:
  $fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
proposed_change:
  protected_semantic: COMMIT_BOUNDARY_NON_BYPASSABILITY
  mutation: WEAKEN
  requested_value: false
```

### Expected result

```yaml
constitutional_validation_result:
  outcome: FAIL
  finding_class: PROTECTED_CONSTRAINT_WEAKENED
semantic_preservation:
  protected_constraints_non_derogable: false
governance_self_protection_assessment:
  protected_safeguards_not_weakened: false
activation_eligibility: INELIGIBLE
compiled_artifact_published_as_validated: false
controlled_activation_attempted: false
authoritative_governance_version: gv-2.0.0
governance_evidence:
  finding_recorded: true
  source_lineage_preserved: true
```

---

## TV-GOMIT-001 — Material governance omission is detected before activation eligibility

### Initial conditions and setup

```yaml
baseline_artifact:
  $fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
authoritative_active_governance_version: gv-2.0.0
```

### Request or harness operation

```yaml
harness_operation: perform_governance_omission_analysis
baseline:
  $fixture: ../schemas/examples/ds042-compiled-governance-artifact-validated.json
omission_injection:
  category: COMMIT_RULES
  required_source_artifact_id: intent-1
  omitted_semantic: COMMIT_BOUNDARY_ENFORCEMENT
```

### Expected result

```yaml
governance_omission_analysis_result:
  outcome: FAIL
  material_omission_detected: true
  omission_category: COMMIT_RULES
traceability_coverage_complete: false
governance_self_protection_assessment:
  material_governance_omissions_absent: false
activation_eligibility: INELIGIBLE
controlled_activation_attempted: false
authoritative_governance_version: gv-2.0.0
governance_evidence:
  omission_finding_recorded: true
  source_lineage_preserved: true
```

---

## TV-GSELF-001 — A governed system cannot directly modify its active admissibility conditions

### Initial conditions and setup

```yaml
active_configuration:
  $fixture: ../schemas/examples/ds041-governance-configuration-active.json
authoritative_active_governance_version: gv-2.0.0
actor_class: GOVERNED_SYSTEM
```

### Request or harness operation

```yaml
harness_operation: attempt_direct_governance_self_modification
target_setting_path: runtime.commit_boundary.enabled
requested_value: false
external_approval_artifact: null
compiled_governance_artifact: null
controlled_activation_record: null
```

### Expected result

```yaml
modification_permitted: false
structural_refusal: true
active_configuration_unchanged: true
authoritative_governance_version: gv-2.0.0
bypass_path_created: false
change_control:
  external_approval_required: true
  governance_compilation_required: true
  constitutional_validation_required: true
  controlled_activation_required: true
governance_evidence:
  attempt_attributed: true
  target_setting_recorded: true
  refusal_recorded: true
```

---

## TV-GACT-001 — Approved and validated governance package activates atomically with evidence, lineage, and Governance Version establishment

### Initial conditions and setup

```yaml
activation_record:
  $fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
prior_authoritative_governance_version: gv-1.9.0
```

### Request or harness operation

```yaml
harness_operation: activate_governance_package
activation:
  $fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
fault_injection: NONE
```

### Expected result

```yaml
schema_validation:
  controlled_governance_activation.json: PASS
approval_basis:
  external_approval_verified: true
  scope_covers_entire_package: true
  approval_current: true
validation_basis:
  all_compiled_artifacts_validated: true
  constitutional_validation_passed: true
  governance_omission_analysis_passed: true
  governance_self_protection_passed: true
  package_dependency_closure_valid: true
activation_atomicity:
  atomic_activation: true
  partial_activation_prohibited: true
  partial_activation_occurred: false
  interdependent_artifacts_activated_together: true
  member_count_consistent: true
activation_result:
  outcome: ACTIVATED
  disposition: AUTHORITATIVE_FOR_RUNTIME_EVALUATION
  authoritative_version_changed: true
governance_version_establishment:
  version_established: true
  package_digest_matches_version: true
  activation_record_bound: true
  version_immutable: true
  historical_replay_supported: true
governance_evidence_refs: __NON_EMPTY__
governance_ledger_event_ref: __PRESENT__
replay_material:
  deterministic_replay_supported: true
schema_fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
```

---

## TV-GACT-002 — Injected member-activation failure prevents partial activation and preserves the prior authoritative version

### Initial conditions and setup

```yaml
activation_record:
  $fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
prior_authoritative_governance_version: gv-1.9.0
```

### Request or harness operation

```yaml
harness_operation: activate_governance_package
activation:
  $fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
fault_injection:
  stage: ACTIVATE_PACKAGE_MEMBER
  member_index: 2
  failure: AUTHORITATIVE_STORE_WRITE_FAILED
```

### Expected result

```yaml
activation_result:
  outcome: FAILED
  authoritative_version_changed: false
activation_atomicity:
  atomic_activation: true
  partial_activation_prohibited: true
  partial_activation_occurred: false
prior_authoritative_governance_version: gv-1.9.0
candidate_governance_version_established: false
authoritative_store_partial_update: false
rollback_basis:
  rollback_supported: true
  prior_version_restorable: true
governance_evidence:
  failure_attributed: true
  failed_member_recorded: true
  transaction_digest_recorded: true
governance_ledger_event:
  activation_failure_recorded: true
```

---

## TV-GROLL-001 — Governed rollback restores the prior Governance Version atomically and preserves evidence and lineage

### Initial conditions and setup

```yaml
completed_activation:
  $fixture: ../schemas/examples/ds043-controlled-governance-activation-activated.json
current_governance_version: gv-2.0.0
rollback_target_governance_version: gv-1.9.0
```

### Request or harness operation

```yaml
harness_operation: rollback_governance_activation
activation_ref: CGA-ACTIVATION-1
rollback_target_governance_version: gv-1.9.0
rollback_trigger: POST_ACTIVATION_ASSURANCE_FAILURE
require_external_approval: true
```

### Expected result

```yaml
rollback_authorized: true
rollback_executed: true
rollback_atomic: true
partial_rollback_occurred: false
authoritative_governance_version: gv-1.9.0
superseded_version_preserved_for_history: true
rollback_basis:
  rollback_supported: true
  prior_version_restorable: true
  rollback_evidence_refs: __NON_EMPTY__
governance_evidence:
  approval_basis_recorded: true
  rollback_trigger_recorded: true
  before_and_after_store_digests_recorded: true
  lineage_preserved: true
governance_ledger_event:
  rollback_recorded: true
  authoritative_ordering_preserved: true
deterministic_replay_supported: true
```

---

# Fixture and schema validation

Fixture references are resolved before OpenAPI and request-schema validation. Each executable
request or fixture SHALL be validated against the schema and interface contract identified in
the YAML vector. DS-040 ledger-event expectations SHALL validate against
`schemas/governance_ledger_event.json`.

# Relationship to AGCP conformance

Passing applicable vectors supports deterministic conformance validation but does not supersede
the authoritative CR set, Core Specification, Architecture Reference Model, RTM, or formal
Conformance Test Suite.
