# AGCP Conformance Test Matrix

**Status:** Informational

This document provides a human-readable capability index for the executable conformance harness.
The governing relationship among Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, and conformance determinations is defined in `AGCP-Conformance-Traceability-and-Automation-Model.md`.
The executable vector catalog is maintained in:

```text
/conformance/AGCP-Conformance-Harness-Spec.yml
```

Its exact human-readable mirror is:

```text
/conformance/AGCP-Conformance-Test-Vectors.md
```

The authoritative machine-readable NS/CR/TC/DS/IF/REG/fixture/Harness-Check/Test-Vector mapping is:

```text
/conformance/test-mapping.json
```

---

# Conformance traceability and automation model

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
Formal Test Case (TC)
        |
        +--> non-automated evidence and procedures
        |
        +--> Harness Checks
                 |
                 v
             Harness Test Vectors
                 |
                 v
             execution evidence
        |
        v
TC assessment result
```

Harness Checks and Harness Test Vectors provide executable support for portions of Formal Test Cases and SHALL NOT introduce additional normative requirements or independently establish conformance.

---

# Capability matrix

| Validated capability | Current executable vectors |
|---|---|
| Proposal qualification and positive authorization path | `TV-PROP-001` |
| Governance approval required | `TV-PROP-002` |
| Governance denial through hard invariant | `TV-PROP-003` |
| Structural refusal and proposal-schema rejection | `TV-PROP-004` |
| Provenance validation | `TV-PROP-005` |
| Tenant operational-state validation | `TV-PROP-006` |
| Policy resolution | `TV-PROP-007` |
| Idempotent replay and idempotency conflict | `TV-PROP-008`, `TV-PROP-009` |
| Externally observable Proposal View and transient-state suppression | `TV-GET-001`, `TV-GET-002` |
| Partial quorum and completed quorum | `TV-GAPP-001`, `TV-GAPP-002` |
| Expired and invalid Governance Approval Artifacts | `TV-GAPP-003`, `TV-GAPP-004` |
| Successful Governance Realization and Commit Boundary | `TV-COMMIT-001` |
| Incomplete approval, mismatched authorization, replay, and inactive-Tenant commit rejection | `TV-COMMIT-002`, `TV-COMMIT-003`, `TV-COMMIT-004`, `TV-COMMIT-005` |
| Governance Evidence and DS-040 ledger-event references | `TV-EVID-001` |
| Canonical State source resolution and ledger-ordering integrity | `TV-STATE-001`, `TV-STATE-002` |
| Cross-Tenant setup and isolation across Proposal, approval, commitment, and evidence interfaces | `TV-XTEN-SETUP`, `TV-XTEN-001`, `TV-XTEN-002`, `TV-XTEN-003`, `TV-XTEN-004` |
| IF-001 metadata discovery | `TV-META-001` |
| Execution Authorization retrieval, not-found handling, and isolation | `TV-EAUTH-001`, `TV-EAUTH-002`, `TV-EAUTH-003` |
| Policy Evaluation Module registration, validation, isolation, and idempotency | `TV-PEM-001`, `TV-PEM-002`, `TV-PEM-003`, `TV-PEM-004`, `TV-PEM-005` |
| Governance Policy registration, validation, isolation, and idempotency | `TV-POL-001`, `TV-POL-002`, `TV-POL-003`, `TV-POL-004`, `TV-POL-005` |
| Governance Artifact retrieval, not-found handling, and isolation | `TV-GART-001`, `TV-GART-002`, `TV-GART-003` |
| Governance Configuration and risk-based re-evaluation controls | `TV-GCFG-001` |
| Deterministic Governance Compilation and source-to-output lineage | `TV-GCOMP-001` |
| Constitutional validation and protected-constraint preservation | `TV-GCONST-001`, `TV-GCONST-002` |
| Governance Omission Analysis | `TV-GOMIT-001` |
| Governance self-protection and self-modification isolation | `TV-GSELF-001` |
| Atomic Controlled Governance Activation and failure preservation | `TV-GACT-001`, `TV-GACT-002` |
| Governed rollback, evidence, lineage, and replay | `TV-GROLL-001` |

---

# Mandatory IF-001 operation coverage

| Mandatory operation | Positive vector | Applicable negative, isolation, and idempotency coverage |
|---|---|---|
| `GET /agcp/v2/meta` (`getMetadata`) | `TV-META-001` | Not applicable: public, parameterless operation with only a declared `200` response |
| `POST /agcp/v2/proposals/submit` (`submitProposal`) | `TV-PROP-001` | `TV-PROP-004` through `TV-PROP-009`, `TV-XTEN-SETUP` |
| `GET /agcp/v2/proposals/{proposal_id}` (`getProposal`) | `TV-GET-001` | `TV-GET-002`, `TV-XTEN-001` |
| `POST /agcp/v2/proposals/{proposal_id}/governance-approvals` (`submitGovernanceApproval`) | `TV-GAPP-001`, `TV-GAPP-002` | `TV-GAPP-003`, `TV-GAPP-004`, `TV-XTEN-002` |
| `GET /agcp/v2/execution-authorizations/{authorization_id}` (`getExecutionAuthorization`) | `TV-EAUTH-001` | `TV-EAUTH-002`, `TV-EAUTH-003` |
| `POST /agcp/v2/commit-boundary/commit` (`commitBoundaryProcessing`) | `TV-COMMIT-001` | `TV-COMMIT-002` through `TV-COMMIT-005`, `TV-XTEN-003` |
| `GET /agcp/v2/governance-evidence/{evidence_id}` (`getGovernanceEvidence`) | `TV-EVID-001` | `TV-XTEN-004` |
| `POST /agcp/v2/governance-artifacts/policy-modules` (`registerPolicyEvaluationModule`) | `TV-PEM-001` | `TV-PEM-002`, `TV-PEM-003`, `TV-PEM-004`, `TV-PEM-005` |
| `POST /agcp/v2/governance-artifacts/policies` (`registerGovernancePolicy`) | `TV-POL-001` | `TV-POL-002`, `TV-POL-003`, `TV-POL-004`, `TV-POL-005` |
| `GET /agcp/v2/governance-artifacts/{artifact_id}` (`getGovernanceArtifact`) | `TV-GART-001` | `TV-GART-002`, `TV-GART-003` |

Every mandatory operation has a schema-valid positive vector. Negative, tenant/domain-isolation, and idempotency vectors are required where the operation contract makes those behaviors applicable.

---

# Complete synchronized vector index

The following identifier set is identical to the executable and human-readable catalogs.

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
| `TV-GAPP-002` | Valid Governance Approval Submission is qualified into an authoritative artifact and completes quorum -> Execution Authorization available |
| `TV-GAPP-003` | Expired Governance Approval Submission -> GOVERNANCE_APPROVAL_EXPIRED |
| `TV-GAPP-004` | Invalid Governance Approval Submission provenance -> GOVERNANCE_APPROVAL_INVALID |
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
| `TV-XTEN-002` | Cross-tenant Governance Approval Submission is forbidden or hidden |
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

# Coverage expectations

- Every vector identifier in the YAML harness SHALL appear in the Markdown mirror.
- The Markdown mirror SHALL NOT introduce additional or alternate vector identifiers.
- Every vector name and substantive scenario SHALL agree across both representations.
- `test-mapping.json` remains the authoritative TC-level machine-readable traceability source.
- Every TC record SHALL contain one or more valid `harness_check_ids`.
- Every TC record SHALL contain `test_vector_ids`, `supporting_test_vector_ids`, and a controlled `test_vector_mapping_status`.
- A TC without a dedicated executable vector SHALL use `NO_DEDICATED_EXECUTABLE_VECTOR` and retain an explicit disposition rather than implying missing traceability.
- Every Harness Check and every current Harness Test Vector SHALL be referenced by at least one TC mapping.
- Harness checks and fixture mappings may reference any identifier in this synchronized catalog.


## P1-12 content-digest contract

| Capability | Formal tests | Supporting vectors | Required result |
|---|---|---|---|
| Exact digest algorithm/output-length and lowercase encoding | TC-042, TC-052, TC-064, TC-066 | `conformance/digests/AGCP-Content-Digest-Test-Vectors.json` | All valid vectors accepted; all mismatch, uppercase, ambiguous, malformed, missing, and undeclared-property vectors rejected before governance reliance. |

## P1-03/P1-09/P1-14/P1-17 Coverage

The public conformance set verifies `404 RESOURCE_NOT_FOUND`, `429 REQUEST_THROTTLED` with `Retry-After`, `503 CAPACITY_UNAVAILABLE`, non-creation of Governance Outcomes for transport/service rejection, governance quota denial as an authoritative outcome, and DS-003 immutable baseline/profile/schema/validator/active-governance advertisements.

## P0-10 semantic fixture coverage

The public conformance package verifies that all 14 corrected positive fixtures are internally consistent across declared binding groups. Ten negative vectors remain structurally valid while introducing one semantic mismatch class each. Fifteen P0-06 claimant-assertion vectors verify that untrusted DS-045 ingress cannot assert authoritative AGCP-derived fields.
