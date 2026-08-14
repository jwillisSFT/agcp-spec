# AGCP Human Adjudication and Governance Approval Specification

**Status:** Normative  
**Artifact Lifecycle:** Current  
**Specification Version:** 2.0.5  
**Repository Release Target:** AGCP v2.0.5  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.5 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-05  

## 1. Purpose

This specification defines the normative structure and processing requirements for human adjudication, governed approval, cosignature, risk acceptance, cancellation, withdrawal, and quorum participation within AGCP.

The public ingress command is the Governance Approval Submission defined by `schemas/governance_approval_submission.json` (DS-045). The canonical authoritative approval record is the Governance Approval Artifact defined by `schemas/governance_approval_artifact.json` (DS-026). Claimant submissions and AGCP-created or AGCP-qualified records are distinct objects and SHALL NOT be conflated.

## 2. Scope

This specification applies to every AGCP implementation that supports governance decisions requiring human or governed approval participation.

It complements:

- the AGCP Core Specification (`AGCP-Core.docx`);
- the Architecture Reference Model (`Architecture Reference Model.docx`);
- the Policy Evaluation Contract (`AGCP-Policy-Evaluation-Contract.md`);
- the AGCP HTTP Interface Specification (`AGCP-HTTP-Interface-Specification.md`);
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`);
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`);
- the Governance Approval Submission schema (`../schemas/governance_approval_submission.json`); and
- the Governance Approval Artifact schema (`../schemas/governance_approval_artifact.json`).

## 3. Governance Approval Model

A Governance Approval Artifact SHALL be bound to:

- eligible Proposal Identity;
- Tenant and governance domain;
- target and governance scope;
- eligible Derived Lifecycle State;
- applicable policy and Governance Version;
- validity conditions;
- accountable approver identity and Authority Lineage;
- Canonical State basis at adjudication; and
- attributable Governance Evidence.

Approval, negative adjudication, cosignature, risk acceptance, cancellation, withdrawal, and quorum participation SHALL be represented as cryptographically attributable and verifiable Governance Approval Artifacts.


### 3.1 Submission and Authoritative Record Separation

A claimant SHALL submit DS-045 `GovernanceApprovalSubmission`. A claimant SHALL NOT submit DS-026 `GovernanceApprovalArtifact` and SHALL NOT assert AGCP verification, eligibility, Canonical State qualification, Authority Lineage qualification, replay uniqueness, quorum arithmetic, lifecycle effects, Governance Evidence, artifact digest, or Governance Ledger ordering.

AGCP SHALL independently process the submission and create or qualify DS-026 only after all applicable identity, authority, validity, signature, replay, Tenant, Governance Domain, scope, lifecycle, policy, Canonical State, quorum, evidence, and ordering checks are complete. DS-026 SHALL carry `artifact_origin = AGCP_CREATED_OR_QUALIFIED`.

## 4. Approval Status and Lifecycle

Approval artifact status values are:

- ACTIVE;
- EXPIRED;
- CANCELLED;
- WITHDRAWN;
- REVOKED; and
- SUPERSEDED.

Only an ACTIVE artifact may contribute to current approval or quorum evaluation, subject to current policy, lifecycle, authority, validity, Canonical State, and other applicable governance conditions.

Expiration, cancellation, withdrawal, revocation, and supersession SHALL preserve history, attribution, reason, and evidence while preventing the artifact from supporting commitment.

## 5. Approver Eligibility

An approver SHALL:

- possess the required governance role or governed authority;
- be eligible under current Tenant, governance-domain, subject-status, lifecycle, scope, and policy conditions;
- possess attributable Authority Lineage; and
- authenticate using an approved cryptographic credential.

Approver eligibility SHALL be verified for the specific Proposal Identity and artifact scope.

## 6. Cryptographic Binding

Each Governance Approval Artifact SHALL be cryptographically bound to its canonical content, including:

- approval artifact identity and version;
- Proposal Identity;
- Tenant and governance domain;
- target and scope;
- lifecycle-state binding;
- decision and approval kind;
- approver identity;
- Authority Lineage reference;
- policy and Governance Version;
- validity window;
- Canonical State reference;
- issuance time;
- replay-protection values; and
- artifact digest.

Modification of any bound field SHALL invalidate verification.

## 7. Canonicalization

The applicable implementation profile SHALL identify the canonicalization method used before digest and signature calculation. The canonicalization method SHALL be recorded in the Governance Approval Artifact.

## 8. Signature Requirements

Signatures SHALL be detached or embedded in a manner that permits independent verification of the canonical artifact representation. The applicable implementation profile SHALL define permitted cryptographic algorithms and verification profiles.

## 9. Replay Protection

Governance Approval Artifacts SHALL include replay-protection material bound to the proposal, approver, Tenant, governance domain, scope, validity horizon, and decision. Previously accepted artifacts SHALL NOT be replayed for a different proposal or governance context.

## 10. Quorum Accumulation

Governance escalation SHALL support deterministic accumulation of valid partial quorum through one or more Governance Approval Artifacts.

Only artifacts that pass eligibility, validity, signature, duplication, Tenant, domain, scope, and lifecycle checks may contribute to quorum.

Duplicate contributions from the same principal SHALL NOT satisfy additional distinct-principal requirements.

Completion of required quorum SHALL make the Proposal eligible for the applicable lifecycle transition, subject to all other governance conditions. It SHALL NOT itself constitute authority at commitment or permission to execute.

## 11. Negative Adjudication, Cancellation, and Withdrawal

Governance Approval Artifacts SHALL support negative adjudication. Authorized governance authorities SHALL be able to cancel pending Proposals before commitment. Approvers or governance authorities may withdraw artifacts where policy permits.

Negative adjudication, cancellation, and withdrawal SHALL record attributable reason, authority, effective time, lifecycle effect, and Governance Evidence.

## 12. Governance Evidence

Every accepted Governance Approval Artifact SHALL produce or reference Governance Evidence sufficient to reconstruct:

- the Proposal Identity and lifecycle state;
- the decision and approval kind;
- the approver and eligibility basis;
- the Authority Lineage;
- the applicable policy and Governance Version;
- the validity and signature-verification results;
- any quorum contribution and accumulated state; and
- any expiration, cancellation, withdrawal, revocation, or supersession.

## 13. Canonical Schema

The authoritative externally observable representation SHALL conform exclusively to:

`schemas/governance_approval_artifact.json` (DS-026)

DS-045 is the sole active approval-submission ingress schema. DS-026 is the sole active authoritative approval-artifact schema. The two schemas are intentionally non-interchangeable.

## 14. Commit-Time Interpretation

A Governance Approval Artifact is evidence used during governance evaluation, Authority Re-Derivation, lifecycle progression, and Commit-Bound Admissibility. Approval or quorum completion SHALL NOT itself constitute authority at commitment, final admissibility, or permission to execute.

Current qualified governance inputs SHALL be re-evaluated before commitment.

## 15. Versioning

Repository releases govern specification versioning. This specification intentionally contains no embedded release number.
