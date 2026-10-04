# AGCP Policy Evaluation Contract (PEC) Specification 

**Status:** Normative\
**Interface Identifier:** IF-002\
**Interface Version:** v2\
**Contract Version:** 2.1.0\
**AGCP Specification Release:** v2.1.0\
**Artifact Lifecycle:** Current\
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.1.0 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-15  
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
-   A universal bytecode format or ABI
-   A deployment architecture

A controlled Implementation Profile MAY adopt a profile-specific machine contract that specializes IF-002 for a selected runtime. Such a companion SHALL preserve this specification, SHALL identify its exact applicability, and SHALL NOT be interpreted as a universal AGCP technology requirement.

## 2. Architectural Context

PEC is a component of the Governance Decision Function (GDF) defined by the AGCP Core Specification. Within AGCP, the GDF realizes the Policy Decision Point (PDP) functional role.

The normative governance pipeline is:

1. Proposal Qualification;
2. Governance Decision Function / PDP;
   - Canonical State establishment;
   - qualified identity-and-authorization context resolution where applicable;
   - policy resolution;
   - Policy Evaluation Module (PEC);
   - policy interaction resolution; and
   - Governance Decision production;
3. Execution Authorization;
4. Continuation Integrity and governed re-evaluation for nonterminal Proposals as applicable;
5. Governance Realization / Commit-Bound Admissibility; and
6. Policy Enforcement Point (PEP) mediation at the protected enforcement boundary.

A Governance Decision produced through the GDF/PDP does not by itself establish commit-bound execution eligibility.

PEC SHALL NOT perform Execution Authorization, Governance Realization, Commit Boundary processing, PEP enforcement, or Continuation Integrity processing.

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

- **PEC** --- Policy Evaluation Contract.
- **PEM** --- Policy Evaluation Module implementing this contract.
- **GDF** --- Governance Decision Function; the AGCP realization of the PDP functional role.
- **PDP** --- Policy Decision Point functional role that evaluates policy/governance inputs and renders a decision.
- **GRF** --- Governance Realization Function that establishes current commit eligibility and prepares enforcement realization.
- **Canonical State** --- Authoritative governance state used for evaluation.
- **Governance Context** --- Context required to evaluate a Qualified Proposal.
- **Authority Lineage** --- Authoritative chain establishing governance authority.
- **Qualified Identity and Authorization Context** --- deterministic, replayable identity plus identity-system role/group/entitlement/governance-authorization facts resolved through the controlling IAS Profile. It is not AGCP Execution Authorization.

## 5. Required Inputs

A PEC implementation SHALL receive at minimum:

- Qualified Proposal;
- Canonical State reference;
- Governance Context;
- Applicable governance policy;
- Resolved constraints;
- Resolved invariants;
- Resolved exceptions;
- Authority Lineage;
- Tenant context;
- Governance Domain context; and
- Governance Configuration reference.

When policy depends on human or workload identity authorization, the GDF SHALL additionally supply a Qualified Identity and Authorization Context resolved upstream through the controlling IAS Profile.

The Qualified Identity and Authorization Context MAY include stable subject identity, account status, Tenant/Domain membership, roles, groups, entitlements, governance permissions, reviewer classes, delegation/authority attributes, scopes, validity, and source/profile integrity references required by the policy.

PEC SHALL consume the qualified deterministic representation. A PEM SHALL NOT directly query a live identity/authorization store, entitlement service, directory, or other network source during evaluation.

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

The Governance Decision Function / PDP remains the authoritative producer of governance outcomes. A favorable outcome is not, by itself, current commit eligibility or permission to execute.

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

All side effects occur outside PEC. Identity/authorization resolution and refresh also occur outside the PEM and are supplied as qualified deterministic inputs.

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

The Policy Evaluation Contract standardizes deterministic policy evaluation while preserving implementation independence. It forms a normative component of the Governance Decision Function / PDP and ensures policy evaluation remains replayable, testable, Canonical State-driven, and free of direct external side effects.

PEC may evaluate qualified identity/authorization facts such as roles and entitlements, but those facts are resolved upstream through the IAS Profile. PEC does not establish AGCP Execution Authorization, current commit eligibility, Governance Realization, or PEP enforcement.

## Mandatory policy resolution is fail-closed

When a qualified Proposal or active Governance Configuration identifies a mandatory policy, policy module, constraint set, or invariant set, the runtime SHALL resolve and validate that exact current controlled artifact before producing an admissible governance decision. A missing, unresolved, invalid, inactive, mismatched, or out-of-scope mandatory policy basis SHALL NOT fall back to a permissive default and SHALL NOT authorize the Proposal. The governed result SHALL be Structural Refusal or another higher-precedence prohibited-progression outcome required by the Core and applicable Formal Test Case, with attributable Governance Evidence.

## Machine-readable v2.1.x synchronization

Policy evaluation may consume DS-053 qualified identity/authorization inputs when governance requires them. The GDF/PDP remains deterministic and side-effect free; it does not perform live IAS lookup inside a PEM, Governance Realization, or PEP enforcement.
