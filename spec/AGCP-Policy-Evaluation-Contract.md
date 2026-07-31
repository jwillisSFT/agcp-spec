# AGCP Policy Evaluation Contract (PEC) Specification 

**Status:** Normative\
**Interface Identifier:** IF-002\
**Interface Version:** v2\
**Contract Version:** 2.0.0\
**AGCP Specification Release:** v2.0.0\
**Series:** AGCP Core\
**Applies To:** All AGCP-conformant implementations

## 1. Purpose

The Policy Evaluation Contract (PEC) defines the normative behavioral
contract between the Governance Decision Function (GDF) and a Policy
Evaluation Module (PEM). It standardizes deterministic evaluation of
governance policy while remaining independent of policy language,
execution engine, or implementation technology.

PEC SHALL provide:

-   Deterministic policy evaluation
-   Engine independence
-   Implementation independence
-   Tenant and governance-domain isolation
-   Canonical State--based evaluation
-   Governance Evidence production
-   Conformance testability

PEC does **not** define:

-   A policy language
-   A rule engine
-   A bytecode format
-   A deployment architecture

## 2. Architectural Context

PEC is a component of the Governance Decision Function defined by the
AGCP Core Specification.

The normative governance pipeline is:

1.  Proposal Qualification
2.  Governance Decision Function
    -   Canonical State establishment
    -   Policy resolution
    -   Policy Evaluation Module (PEC)
    -   Policy interaction resolution
    -   Governance outcome determination
3.  Execution Authorization
4.  Continuation Integrity for nonterminal Proposals until final Commit-Bound Admissibility
5.  Governance Realization and Commit Boundary processing

PEC SHALL NOT perform Execution Authorization, Commit Boundary
processing, or Continuation Integrity processing.

## 3. Design Principles

PEC SHALL be:

-   Deterministic
-   Side-effect free
-   Replayable
-   Tenant isolated
-   Governance-domain isolated
-   Canonical State driven
-   Implementation independent

## 4. Terminology

-   **PEC** --- Policy Evaluation Contract.
-   **PEM** --- Policy Evaluation Module implementing this contract.
-   **GDF** --- Governance Decision Function.
-   **Canonical State** --- Authoritative governance state used for
    evaluation.
-   **Governance Context** --- Context required to evaluate a Qualified
    Proposal.
-   **Authority Lineage** --- Authoritative chain establishing
    governance authority.

## 5. Required Inputs

A PEC implementation SHALL receive at minimum:

-   Qualified Proposal
-   Canonical State reference
-   Governance Context
-   Applicable governance policy
-   Resolved constraints
-   Resolved invariants
-   Resolved exceptions
-   Authority Lineage
-   Tenant context
-   Governance domain context
-   Governance configuration reference

Inputs SHALL be deterministic and replayable.

## 6. Determinism Requirements

PEC SHALL NOT depend upon:

-   Current system time (except authoritative timestamps supplied in
    inputs)
-   Random values
-   Environment variables
-   Mutable global state
-   Network access
-   External side effects

Identical authoritative inputs SHALL produce identical outputs.

## 7. Evaluation Responsibilities

The PEM SHALL evaluate:

1.  Constraints
2.  Invariants
3.  Governance Approval and governed human-adjudication requirements
4.  Applicable policy interactions

The PEM SHALL return sufficient information for the Governance Decision
Function to produce an authoritative governance outcome.

## 8. Governance Outcomes

PEC SHALL support the governance outcomes defined by the AGCP Core
Specification:

-   Authorized
-   Denied
-   Structural Refusal
-   Pending Human Review
-   Deferred
-   Governed Re-evaluation Required

The Governance Decision Function remains the authoritative producer of
governance outcomes.

## 9. Canonical State

All evaluations SHALL be performed against authoritative Canonical
State.

Non-authoritative observations, telemetry, cached state, or speculative
state SHALL NOT supersede Canonical State.

## 10. Authority Lineage

Policy evaluation SHALL preserve Authority Lineage and SHALL NOT expand
or weaken delegated authority.

## 11. Governance Evidence

PEC SHALL produce sufficient evidence to support:

-   Deterministic replay
-   Governance interpretation
-   Traceability
-   Attribution
-   Integrity

## 12. Side Effects

PEC SHALL NOT:

-   Commit execution
-   Modify Canonical State
-   Update governance configuration
-   Append Governance Evidence directly
-   Modify external systems

All side effects occur outside PEC.

## 13. Deterministic Replay

Replay using identical authoritative inputs SHALL reproduce the same
policy interpretation and support the Governance Decision Function
replay requirements defined by the AGCP Core Specification.

## 14. Conformance

Conformant implementations SHALL satisfy all applicable AGCP Runtime
Governance Requirements and Normative Statements governing Proposal
Qualification, Governance Decision Function, Canonical State, Governance
Evidence, Authority Lineage, and deterministic replay.

## 15. Security

Implementations SHOULD integrity-protect Policy Evaluation Modules
through authenticated distribution, version control, and cryptographic
verification.

## 16. Versioning

Breaking interface changes require a MAJOR version increment.

Backward-compatible additions require a MINOR version increment.

Editorial clarifications require a PATCH increment.

## 17. Summary

The Policy Evaluation Contract standardizes deterministic policy
evaluation while preserving implementation independence. It forms a
normative component of the Governance Decision Function and ensures
policy evaluation remains replayable, testable, Canonical State--driven,
and consistent with the AGCP Core Specification.
