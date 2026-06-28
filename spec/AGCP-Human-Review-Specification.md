# AGCP Human Review Specification

**Status:** Normative

## 1. Purpose

This specification defines the normative structure and processing
requirements for Human Review within AGCP.

Human Review replaces the earlier HITL token model with a
governance-centric model supporting deterministic reviewer
authorization, quorum evaluation, Governance Evidence generation, and
Authority Lineage validation.

## 2. Scope

This specification applies to every AGCP implementation that supports
governance decisions requiring human participation.

It complements:

-   AGCP Core Specification
-   Policy Evaluation Contract (PEC)
-   AGCP HTTP Interface Specification
-   Governance Evidence Specification
-   Human Review Artifact schema (`schemas/human_review_artifact.json`)

## 3. Human Review Model

Human Review is performed against a Proposal and associated Governance
Decision.

A review SHALL be bound to:

-   tenant_id
-   governance_domain_id
-   proposal_id
-   action_id (when applicable)
-   Governance Context
-   Canonical State
-   Authority Lineage

## 4. Review Lifecycle

Possible review states are:

-   Pending
-   Approved
-   Rejected
-   Expired
-   Withdrawn

When quorum is satisfied, the Governance Decision proceeds to Execution
Authorization.

## 5. Reviewer Authorization

A reviewer SHALL:

-   possess the required governance role;
-   be authorized through the applicable Authority Lineage;
-   authenticate using an approved cryptographic credential.

Reviewer authorization SHALL be tenant-scoped.

## 6. Cryptographic Binding

Each review decision SHALL be cryptographically bound to:

-   tenant_id
-   governance_domain_id
-   proposal_id
-   action_id (if present)
-   reviewer identity
-   Authority Lineage reference
-   review timestamp
-   review decision
-   nonce

Modification of any bound field SHALL invalidate the signature.

## 7. Canonicalization

Before signing:

1.  Remove the signature field.
2.  Sort object keys lexicographically.
3.  Preserve array ordering.
4.  Serialize as minimal UTF-8 JSON.

The resulting byte sequence SHALL be the canonical representation.

## 8. Signature Requirements

Implementations SHALL support at least one of:

-   Ed25519
-   ES256
-   RS256

Signatures SHALL be detached and verifiable from the canonical
representation.

## 9. Replay Protection

Review submissions SHALL include a nonce.

The tuple:

-   tenant_id
-   proposal_id
-   reviewer
-   nonce

SHALL be unique within the replay window.

Previously accepted review decisions SHALL NOT be replayed.

## 10. Quorum Evaluation

Required reviewer roles SHALL be defined by applicable governance
policy.

Quorum SHALL be evaluated deterministically.

Duplicate approvals from the same reviewer SHALL NOT satisfy additional
quorum requirements.

## 11. Governance Evidence

Every accepted review decision SHALL produce Governance Evidence.

Evidence SHALL reference:

-   Proposal
-   Governance Decision
-   reviewer
-   Authority Lineage
-   review outcome
-   timestamp

## 12. Human Review Artifact

The canonical externally observable representation of Human Review SHALL
conform to:

`schemas/human_review_artifact.json`

## 13. Security Considerations

Implementations SHALL:

-   verify reviewer authorization;
-   validate signatures;
-   enforce replay protection;
-   preserve tenant isolation;
-   generate immutable Governance Evidence.

## 14. Versioning

Repository releases govern specification versioning.

This specification intentionally contains no embedded specification
version.
