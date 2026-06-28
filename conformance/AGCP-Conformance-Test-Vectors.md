# AGCP Conformance Test Vectors

**Status:** Informational  
**Purpose:** Deterministic Conformance Harness Test Vectors

---

## Purpose

This document defines deterministic conformance test vectors for AGCP.

Each vector defines:

- initial conditions;
- request or harness action;
- expected externally observable response;
- expected Governance Evidence;
- expected Append-Only Governance Ledger effects; and
- deterministic replay or reconstruction assertions where applicable.

These vectors are intended to support the AGCP Conformance Specification, AGCP Conformance Harness Specification, and AGCP Conformance Test Suite.

They are informational test-vector guidance. The authoritative conformance traceability model remains:

```text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

---

# A. Conventions Used in Test Vectors

## A.1 Identifiers

Unless otherwise specified, vectors use the following identifiers:

```text
tenant_id: T1
governance_domain_id: GD1
proposal_id: P1
action_id: A1
authorization_id: AUTH1
governance_evidence_id: EV1
ledger_entry_id: LE1
ledger_sequence_value: 1
```

Additional tenants and governance domains use:

```text
tenant_id: T2
governance_domain_id: GD2
```

## A.2 Governance Pipeline Stages

The primary AGCP governance pipeline is:

```text
Proposal Qualification
Governance Decision Function
Human Review, where required
Execution Authorization
Commit Boundary
Continuation Integrity, where applicable
```

Supporting services include:

```text
Governance Evidence
Append-Only Governance Ledger
Tenant and Governance Domain Isolation
Delegation and Authority Lineage
Cross-Domain Authority Isolation
Governance Self-Protection
Autonomous Coordination
```

## A.3 Append-Only Governance Ledger Entry Model

Each ledger entry used by these vectors is represented as:

```yaml
ledger_entry_id:
tenant_id:
governance_domain_id:
ledger_sequence_value:
artifact_type:
artifact_reference:
governance_evidence_reference:
previous_ledger_entry_hash:
```

Implementations MAY include additional fields.

The harness SHALL validate:

- append-only behavior;
- immutable entries;
- sequence ordering;
- tenant and governance domain scope;
- Governance Evidence linkage;
- Canonical State reconstruction behavior.

## A.4 Canonical State Assertions

Canonical State SHALL be derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered ledger can be deterministically reproduced.

The harness SHALL verify:

- ledger sequence order is authoritative;
- timestamp order is not authoritative;
- reordered ledger entries are rejected or produce non-equivalent Canonical State;
- materialized Canonical State views are reproducible from ordered ledger entries.

---

# B. Proposal Submission Test Vectors

## TV-PROP-001 — Valid Proposal Qualifies

### Initial Conditions

- Tenant `T1` exists.
- Tenant `T1` is `ACTIVE`.
- Governance Domain `GD1` exists.
- Applicable governance configuration exists.
- Applicable policy artifacts exist.
- Authority Lineage is valid.
- Provenance is valid.

### Request

```http
POST /agcp/v1/proposals
```

Body:

```json
{
  "tenant_id": "T1",
  "governance_domain_id": "GD1",
  "proposal_id": "P1",
  "action": {
    "action_id": "A1",
    "action_type": "example.valid"
  },
  "governance_context_ref": {
    "governance_context_id": "GCX1"
  },
  "provenance": "valid"
}
```

### Expected Response

- HTTP 200 or HTTP 201
- Proposal accepted for governance processing
- Proposal View or Governance Decision Result is returned or made retrievable
- No execution occurs

### Expected Governance Evidence

Evidence SHALL be produced for:

- Proposal Qualification
- provenance validation
- tenant and Governance Domain validation

### Expected Ledger Delta

Append one or more ordered ledger entries recording:

- Proposal submission
- Proposal Qualification outcome
- associated Governance Evidence reference

### Determinism Assertions

- Same proposal and authoritative inputs produce the same qualification outcome.
- Ledger sequence order is preserved.
- Canonical State is not altered except through valid ledger-recorded governance events.

---

## TV-PROP-002 — Structurally Invalid Proposal Refused

### Initial Conditions

- Tenant `T1` exists.
- Tenant `T1` is `ACTIVE`.

### Request

```http
POST /agcp/v1/proposals
```

Body contains a malformed or schema-invalid Proposal.

### Expected Response

- HTTP 400 or HTTP 422
- Structural Refusal or schema rejection
- rejection_code reflects the applicable error mapping

### Expected Governance Evidence

Evidence SHALL record:

- failed Proposal Qualification or schema validation
- refusal reason
- applicable rejection code

### Expected Ledger Delta

Append-only ledger behavior SHALL follow the implementation profile.

If the implementation records refused proposals in the ledger, the ledger entry SHALL:

- be tenant scoped;
- be immutable;
- reference Governance Evidence;
- preserve sequence ordering.

### Determinism Assertions

- Invalid structure SHALL be rejected deterministically.
- The Proposal SHALL NOT proceed to Governance Decision evaluation.
- No Execution Authorization or Commit Boundary processing SHALL occur.

---

# C. Governance Decision Test Vectors

## TV-GOV-001 — Governance Decision Authorized

### Initial Conditions

- Proposal `P1` is qualified.
- Canonical State is valid and reproducible from the ordered ledger.
- Applicable policy permits the proposed Action.
- No Human Review is required.

### Harness Action

Evaluate the Governance Decision Function for Proposal `P1`.

### Expected Response

- Governance outcome: `Authorized`
- Governance Decision Result is produced
- No execution occurs

### Expected Governance Evidence

Evidence SHALL include:

- Proposal identity
- Action identity
- Canonical State reference
- policy reference
- Authority Lineage reference
- governance configuration reference
- Governance Decision outcome

### Expected Ledger Delta

Append an ordered ledger entry for the Governance Decision event.

### Determinism Assertions

- Re-evaluation using identical authoritative inputs produces the same Governance Decision.
- Decision result is attributable and verifiable.
- Decision does not itself authorize execution.

---

## TV-GOV-002 — Governance Decision Denied

### Initial Conditions

- Proposal `P1` is qualified.
- Canonical State is valid.
- Applicable policy denies the proposed Action.

### Harness Action

Evaluate the Governance Decision Function for Proposal `P1`.

### Expected Response

- Governance outcome: `Denied`
- rejection_code is present where applicable
- No Execution Authorization is produced
- No Commit Boundary processing occurs

### Expected Governance Evidence

Evidence SHALL record:

- policy evaluation
- denial reason
- rejection code where applicable
- Canonical State reference

### Expected Ledger Delta

Append an ordered ledger entry for the denied Governance Decision.

### Determinism Assertions

- Identical inputs produce identical denial.
- Denied Proposal cannot proceed to Execution Authorization.

---

## TV-GOV-003 — Human Review Required

### Initial Conditions

- Proposal `P1` is qualified.
- Policy requires Human Review before execution authorization.

### Harness Action

Evaluate the Governance Decision Function for Proposal `P1`.

### Expected Response

- Governance outcome: `Pending Human Review`
- required reviewer roles are identified
- No Execution Authorization is produced

### Expected Governance Evidence

Evidence SHALL record:

- Human Review requirement
- required reviewer roles
- policy basis for review

### Expected Ledger Delta

Append an ordered ledger entry for the Governance Decision indicating Human Review is required.

### Determinism Assertions

- Identical authoritative inputs produce the same Human Review requirement.
- No Commit Boundary processing occurs before required Human Review is complete.

---

# D. Human Review Test Vectors

## TV-HR-001 — Human Review Recorded but Quorum Not Satisfied

### Initial Conditions

- Proposal `P1` has Governance Decision outcome `Pending Human Review`.
- Required reviewer roles are `Risk Officer` and `Security Lead`.
- A valid review artifact is submitted by a reviewer satisfying `Risk Officer`.

### Request

Submit or record a Human Review Artifact for Proposal `P1`.

### Expected Response

- Human Review artifact accepted
- Review status remains pending
- Quorum not satisfied
- No Execution Authorization is produced

### Expected Governance Evidence

Evidence SHALL record:

- reviewer identity
- Authority Lineage reference
- review decision
- review timestamp
- quorum status

### Expected Ledger Delta

Append an ordered ledger entry for the Human Review event.

### Determinism Assertions

- Partial Human Review does not authorize execution.
- Duplicate review by the same reviewer does not satisfy additional quorum requirements.

---

## TV-HR-002 — Human Review Completes Quorum

### Initial Conditions

- Proposal `P1` has Governance Decision outcome `Pending Human Review`.
- Required reviewer role is `Risk Officer`.
- A valid Human Review artifact satisfies the required role.

### Request

Submit or record the Human Review Artifact.

### Expected Response

- Human Review accepted
- Quorum satisfied
- Proposal becomes eligible for Execution Authorization

### Expected Governance Evidence

Evidence SHALL record:

- reviewer identity
- role satisfied
- Authority Lineage reference
- quorum satisfaction
- review outcome

### Expected Ledger Delta

Append an ordered ledger entry for the Human Review completion event.

### Determinism Assertions

- Quorum satisfaction is deterministic.
- Execution Authorization is not produced until Human Review requirements are satisfied.

---

## TV-HR-003 — Invalid or Expired Human Review Rejected

### Initial Conditions

- Proposal `P1` requires Human Review.
- Submitted Human Review artifact is expired, invalid, unauthorized, or has invalid provenance.

### Request

Submit the invalid Human Review Artifact.

### Expected Response

- HTTP 400, 403, 409, or 422 according to the Error Mapping Specification
- rejection_code reflects the applicable failure
- Quorum is not satisfied

### Expected Governance Evidence

Evidence SHALL record the rejected Human Review attempt where required by implementation profile.

### Expected Ledger Delta

No authorization ledger entry SHALL be appended.

If the rejected review attempt is recorded, it SHALL be recorded as a rejected governance event with Governance Evidence.

### Determinism Assertions

- Invalid Human Review artifacts SHALL NOT satisfy quorum.
- Expired Human Review artifacts SHALL NOT authorize execution.

---

# E. Execution Authorization Test Vectors

## TV-AUTH-001 — Execution Authorization Succeeds

### Initial Conditions

- Proposal `P1` is qualified.
- Governance Decision outcome is `Authorized`.
- Human Review is either not required or has been completed.
- Authority Lineage remains valid.
- Canonical State remains valid.
- Tenant and Governance Domain constraints are satisfied.

### Harness Action

Request or evaluate Execution Authorization for Proposal `P1`.

### Expected Response

- Execution Authorization outcome: `Authorized for Commit Boundary Processing`
- `authorization_id` present
- No execution occurs

### Expected Governance Evidence

Evidence SHALL record:

- authorization decision
- Proposal reference
- Action reference
- Authority Lineage reference
- Canonical State reference
- governance configuration reference

### Expected Ledger Delta

Append an ordered ledger entry for Execution Authorization.

### Determinism Assertions

- Execution Authorization is deterministic.
- Execution Authorization does not itself perform execution.

---

## TV-AUTH-002 — Execution Authorization Fails

### Initial Conditions

- Proposal `P1` has a Governance Decision.
- Authority Lineage has been revoked, expired, or no longer satisfies required authority.

### Harness Action

Request or evaluate Execution Authorization.

### Expected Response

- Execution Authorization outcome: `Authorization Failure` or `Governed Re-evaluation Required`
- No Commit Boundary processing occurs
- No execution occurs

### Expected Governance Evidence

Evidence SHALL record:

- authorization failure
- authority failure reason
- applicable rejection code

### Expected Ledger Delta

Append an ordered ledger entry for Authorization Failure where required by profile.

### Determinism Assertions

- Invalid authority SHALL prevent Execution Authorization.
- Failed authorization SHALL NOT permit Commit Boundary processing.

---

# F. Commit Boundary Test Vectors

## TV-CB-001 — Commit Boundary Succeeds

### Initial Conditions

- Execution Authorization `AUTH1` exists.
- Authorization remains valid.
- Qualified Action Representation remains unchanged.
- Governance Context remains valid.
- Tenant and Governance Domain constraints remain satisfied.

### Request

Submit Commit Boundary request for authorized Proposal `P1`.

### Expected Response

- Commit Boundary outcome: `Commit Successful`
- governed Action becomes eligible to execute or is executed as defined by implementation profile

### Expected Governance Evidence

Evidence SHALL record:

- authorization reference
- Commit Boundary outcome
- Canonical State reference
- Authority Lineage reference
- execution context
- commit timestamp

### Expected Ledger Delta

Append an ordered ledger entry for Commit Boundary success.

### Determinism Assertions

- Commit Boundary processing is deterministic.
- Execution does not occur before successful Commit Boundary processing.
- Successful Commit Boundary processing is recorded in the ledger.

---

## TV-CB-002 — Commit Boundary Fails Without Authorization

### Initial Conditions

- Proposal `P1` has no valid Execution Authorization.

### Request

Submit Commit Boundary request.

### Expected Response

- Commit Boundary outcome: `Commit Failed` or rejection
- rejection_code reflects missing or invalid authorization
- no execution occurs

### Expected Governance Evidence

Evidence SHALL record failed Commit Boundary attempt where required.

### Expected Ledger Delta

No successful Commit Boundary ledger entry SHALL be appended.

### Determinism Assertions

- Commit Boundary processing SHALL reject missing authorization.
- Execution SHALL NOT occur.

---

## TV-CB-003 — Commit Boundary Requires Current Governance Conditions

### Initial Conditions

- Execution Authorization exists.
- Canonical State, Authority Lineage, Governance Context, or tenant state has changed before commit.

### Request

Submit Commit Boundary request.

### Expected Response

- Commit Boundary outcome: `Commit Failed` or `Governed Re-evaluation Required`
- no execution occurs

### Expected Governance Evidence

Evidence SHALL record the changed condition and failed commit outcome.

### Expected Ledger Delta

Append a failed Commit Boundary event where required by implementation profile.

### Determinism Assertions

- Commit Boundary processing SHALL validate current governance conditions.
- Stale authorization SHALL NOT permit execution.

---

# G. Cross-Tenant and Governance Domain Safety Tests

## TV-XTEN-001 — Cross-Tenant Proposal Access Denied

### Initial Conditions

- Proposal `P1` belongs to tenant `T2`.
- Caller belongs to tenant `T1`.

### Request

Retrieve or operate on Proposal `P1` from tenant `T1`.

### Expected Response

- HTTP 403 or 404 according to the implementation's non-disclosure policy
- If disclosed as denial, rejection_code is `TENANT_SCOPE_VIOLATION`

### Expected Ledger Delta

No governance-significant state change occurs.

### Determinism Assertions

- Tenant isolation is preserved.
- Tenant existence is not leaked where non-disclosure behavior is required.

---

## TV-XTEN-002 — Cross-Tenant Commit Boundary Denied

### Initial Conditions

- Proposal `P1` and authorization `AUTH1` belong to tenant `T2`.
- Caller belongs to tenant `T1`.

### Request

Submit Commit Boundary request from tenant `T1`.

### Expected Response

- HTTP 403
- rejection_code is `TENANT_SCOPE_VIOLATION`

### Expected Ledger Delta

No successful Commit Boundary entry is appended.

### Determinism Assertions

- Cross-tenant Commit Boundary processing is rejected.
- Execution does not occur.

---

## TV-XDOM-001 — Cross-Governance Domain Access Denied

### Initial Conditions

- Proposal `P1` belongs to Governance Domain `GD2`.
- Caller operates within Governance Domain `GD1`.
- No authorized cross-domain trust artifact exists.

### Request

Retrieve or operate on Proposal `P1`.

### Expected Response

- HTTP 403 or 404 according to non-disclosure policy
- If disclosed as denial, rejection_code reflects governance domain violation or tenant scope violation as defined by the Error Mapping Specification

### Expected Ledger Delta

No unauthorized governance state change occurs.

### Determinism Assertions

- Governance Domain isolation is preserved.
- Cross-domain access requires governed authorization.

---

# H. Ledger and Canonical State Reconstruction Tests

## TV-LEDGER-001 — Ledger-Derived Canonical State Matches API View

### Initial Conditions

- Ledger contains ordered entries for Proposal `P1`.
- Governance Evidence references are valid.
- API exposes Proposal View, Governance Decision Result, or Canonical State reference.

### Harness Action

Retrieve ordered ledger entries and reconstruct Canonical State.

### Expected Result

- Reconstructed Canonical State matches externally observable API state.
- Governance Evidence references are valid.
- Ledger sequence order is authoritative.

### Determinism Assertions

- Timestamp order is not used as authoritative ordering.
- Materialized Canonical State, where present, is reproducible from ledger order.

---

## TV-LEDGER-002 — Reordered Ledger History Rejected or Non-Equivalent

### Initial Conditions

- Ledger contains at least two entries for Proposal `P1` whose order affects Canonical State derivation.

### Harness Action

Present the same ledger entries in a different sequence and attempt Canonical State reconstruction.

### Expected Result

- Reordered ledger history is rejected, or
- Reordered ledger history produces a Canonical State that is not accepted as equivalent to the authoritative Canonical State.

### Determinism Assertions

- Ledger sequence order is authoritative.
- Timestamp ordering SHALL NOT override ledger sequence ordering.

---

## TV-LEDGER-003 — Ledger Immutability Violation Detected

### Initial Conditions

- Ledger contains a valid ordered governance history.
- A ledger entry is modified, deleted, reordered, or replaced.

### Harness Action

Attempt replay, reconstruction, or integrity verification.

### Expected Result

- Integrity violation is detected.
- Modified history is rejected.
- Canonical State reconstruction from tampered history is not accepted.

### Determinism Assertions

- Ledger immutability is enforced.
- Governance Evidence integrity remains verifiable.

---

# I. Harness-Level Determinism Tests

## TV-META-001 — Governance Pipeline Ordering

### Procedure

- Submit a valid Proposal.
- Retrieve Governance Evidence and ordered Append-Only Governance Ledger entries.

### Assertions

The following ordering SHALL be preserved where applicable:

```text
Proposal Qualification
Governance Decision Function
Human Review
Execution Authorization
Commit Boundary
Continuation Integrity
```

Supporting Governance Evidence SHALL be associated with each governance-significant event.

---

## TV-META-002 — Idempotent Proposal Submission

### Procedure

- Submit Proposal `P1`.
- Submit the same Proposal again using the same idempotency key or equivalent replay-protection mechanism.

### Assertions

- Response is equivalent.
- No duplicate governance-significant ledger event is appended unless explicitly permitted by the idempotency semantics.
- Proposal identity remains stable.
- Governance Evidence remains consistent.

---

## TV-META-003 — Deterministic Replay

### Procedure

- Execute a complete governed Proposal.
- Retrieve ordered ledger history and Governance Evidence.
- Replay governance processing.

### Assertions

- Replay reproduces Proposal Qualification.
- Replay reproduces Governance Decision interpretation.
- Replay reproduces Execution Authorization interpretation.
- Replay reproduces Commit Boundary interpretation.
- Replay reproduces Canonical State from ledger order.

---

# Relationship to AGCP Conformance

These vectors support validation of the requirements defined in:

- AGCP Core Specification
- AGCP Conformance Specification
- AGCP Append-Only Governance Ledger Specification
- AGCP Policy Evaluation Contract
- AGCP Security Specification
- AGCP Provenance Wire Format Specification
- AGCP Human Review Specification
- AGCP HTTP Interface Specification

Passing applicable vectors supports deterministic conformance validation but does not supersede the authoritative Requirements Traceability Matrix or Conformance Test Suite.
