# AGCP Human Adjudication and Governance Approval Specification

**Status:** Normative  
**Artifact Lifecycle:** Current  
**Specification Version:** 2.1.0  
**Repository Release Target:** AGCP v2.1.0  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.1.0 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-15  

## 1. Purpose

This specification defines the normative structure and processing requirements for human adjudication, governed approval, cosignature, risk acceptance, cancellation, withdrawal, and quorum participation within AGCP.

The public ingress command is the Governance Approval Submission defined by `schemas/governance_approval_submission.json` (DS-045). The canonical authoritative approval record is the Governance Approval Artifact defined by `schemas/governance_approval_artifact.json` (DS-026). Claimant submissions and AGCP-created or AGCP-qualified records are distinct objects and SHALL NOT be conflated.

## 2. Scope

This specification applies to every AGCP implementation that supports governance decisions requiring human or governed approval participation.

It complements:

- the AGCP Core Specification (`AGCP-Core.docx`);
- the Architecture Reference Model (`Architecture Reference Model.docx`);
- the AGCP Trust Model (`AGCP-Trust-Model.md`);
- the Policy Evaluation Contract (`AGCP-Policy-Evaluation-Contract.md`);
- the AGCP HTTP Interface Specification (`AGCP-HTTP-Interface-Specification.md`);
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`);
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`);
- the Governance Approval Submission schema (`../schemas/governance_approval_submission.json`); and
- the Governance Approval Artifact schema (`../schemas/governance_approval_artifact.json`); and
- the implementation-selected Identity and Authorization Store (IAS) Profile defined by the AGCP Implementation Profile framework.

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

A claimant SHALL submit DS-045 `GovernanceApprovalSubmission`. A claimant SHALL NOT submit DS-026 `GovernanceApprovalArtifact` and SHALL NOT assert AGCP verification, eligibility, Canonical State qualification, Authority Lineage qualification, identity authorization or entitlement, replay uniqueness, quorum arithmetic, lifecycle effects, Governance Evidence, artifact digest, or Governance Ledger ordering.

A claimant-supplied approver identifier, role, group, entitlement, reviewer class, delegation claim, governance permission, or authority scope SHALL be treated as an assertion only. It SHALL NOT become authoritative merely because it is syntactically valid or cryptographically signed by the claimant.

AGCP SHALL bind the authenticated subject to the submission and SHALL resolve the authoritative identity and authorization record through the implementation-selected IAS Profile before DS-026 becomes authoritative. AGCP SHALL independently process the submission and create or qualify DS-026 only after all applicable identity, account-status, authorization/entitlement, authority, validity, signature, replay, Tenant, Governance Domain, scope, lifecycle, policy, Canonical State, quorum, evidence, and ordering checks are complete. DS-026 SHALL carry `artifact_origin = AGCP_CREATED_OR_QUALIFIED`.

The IAS Profile supplies qualified identity and identity-system authorization/entitlement information. Those facts are governance inputs; they are not AGCP Execution Authorization and do not themselves determine the Governance Decision.

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

An approver SHALL be resolved as an authoritative human governance principal through the controlling Implementation Profile and its selected IAS Profile.

Approver eligibility SHALL establish, as applicable:

- stable authenticated subject and account identity;
- current account status, including disablement, suspension, revocation, or equivalent ineligibility;
- Tenant and Governance Domain membership;
- required roles, groups, entitlements, governance permissions, or reviewer classes;
- the scope to which those authorizations or entitlements apply;
- applicable delegation or Authority Lineage;
- separation-of-duty, conflict-of-interest, distinct-principal, and quorum constraints;
- validity/effective periods and relevant revocation state; and
- any proposal-, target-, action-, or governance-domain-specific eligibility conditions required by policy.

Approver eligibility SHALL be verified for the specific Proposal Identity and artifact scope. Authentication alone SHALL NOT establish approval eligibility.

### 5.1 Authoritative Identity and Authorization Resolution

The Implementation Profile SHALL identify the IAS Profile used to resolve governance-significant human identity and identity-system authorization/entitlement information.

The IAS Profile SHALL define the authoritative source or sources, stable identifier mapping, authoritative fact scope, source precedence where more than one source is used, freshness/cache rules, failure behavior, and the service identity used for protected resolution.

If required identity or authorization/entitlement information cannot be resolved with the freshness and integrity required by the controlling profile or governance, the approval SHALL NOT become authoritative and SHALL NOT contribute to quorum.

A disabled, revoked, expired, out-of-scope, or otherwise ineligible subject or entitlement SHALL NOT contribute current approval authority even if a prior approval artifact remains cryptographically valid.

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
- the authenticated human subject and stable authoritative account identity;
- the IAS Profile identity/version/digest or equivalent controlled reference;
- the authoritative identity/authorization source or source set used;
- the current account-status result;
- the roles, groups, entitlements, governance permissions, reviewer class, scope, delegation, or other authority basis material to eligibility;
- the Authority Lineage;
- the applicable policy and Governance Version;
- the validity and signature-verification results;
- any quorum contribution and accumulated state; and
- any expiration, cancellation, withdrawal, revocation, supersession, or identity/entitlement invalidation relevant to the approval.

Evidence SHALL preserve identifiers and integrity references without exposing credentials or unnecessary sensitive directory data.

## 13. Canonical Schema

The authoritative externally observable representation SHALL conform exclusively to:

`schemas/governance_approval_artifact.json` (DS-026)

DS-045 is the sole active approval-submission ingress schema. DS-026 is the sole active authoritative approval-artifact schema. The two schemas are intentionally non-interchangeable.

## 14. Commit-Time Interpretation

A Governance Approval Artifact is evidence used during governance evaluation, Authority Re-Derivation, lifecycle progression, Governance Realization, and Commit-Bound Admissibility. Approval or quorum completion SHALL NOT itself constitute authority at commitment, final admissibility, or permission to execute.

The Governance Realization Function (GRF) SHALL use current qualified governance inputs at commitment. When human identity, account status, role, entitlement, governance permission, delegation, or reviewer authority is commitment-sensitive under the controlling governance or Implementation Profile, the GRF SHALL re-resolve or otherwise revalidate that information according to the IAS Profile before the approval is relied upon for commitment.

A cryptographically valid approval whose underlying human authority or entitlement is no longer current SHALL NOT be treated as current commit authority.

## 15. Versioning

Repository releases govern specification versioning. This specification intentionally contains no embedded release number.
## Approval acceptance ordering and lifecycle validity

Before a Governance Approval Submission is admitted as an authoritative Governance Approval Artifact or allowed to contribute to quorum, the implementation SHALL reload the authoritative Proposal and verify that the Proposal is in an approval-eligible nonterminal human-review lifecycle state. A Proposal that is already `AUTHORIZED`, `EXECUTED`, structurally refused, rejected, cancelled, expired, superseded, or otherwise terminal/ineligible SHALL reject the approval submission without creating a quorum contribution.

Approval validity SHALL be evaluated against authoritative current time before quorum contribution. An expired, revoked, replayed, out-of-scope, or otherwise invalid approval SHALL NOT contribute to quorum and SHALL NOT advance the Proposal lifecycle. The accepted artifact SHALL remain bound to the authenticated actor, Proposal Identity, Tenant, Governance Domain, approval role/scope, validity horizon, and current authority determination.
