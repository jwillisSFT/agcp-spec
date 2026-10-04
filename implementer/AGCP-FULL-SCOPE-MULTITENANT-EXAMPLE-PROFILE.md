# AGCP Full-Scope Multitenant Reference Implementation Profile - Informational Example

**Status:** Informational example; not a conformance claim  
**Profile version:** 2.0.0  
**Profile format:** 2.0.0  
**AGCP baseline:** v2.1.x

## 1. Purpose

This example demonstrates one generic full-scope multitenant realization of AGCP without prescribing products, hosting platforms, customer-specific names, or deployment values.

## 2. Architectural placement

The example contains logically distinct Proposal Qualification, GDF/PDP, Execution Authorization, GRF, PEP, ledger/evidence, Canonical State, governance repository, and identity/authorization resolution functions.

GDF/PDP and GRF may execute in the same protected control-plane service, but decision evidence and commit-realization evidence remain distinguishable.

```text
Proposer -> Proposal Qualification -> GDF/PDP -> Execution Authorization
                                        |               |
                                        |               v
                                        +------> GRF / Commit-Bound Admissibility
                                                    |
                                             selected PEP Profile
                                                    |
                                             Enforcement Context
                                                    v
                                                   PEP
                                                    v
                                                Target
```

## 3. Identity and authorization

The example references `IAS-GENERIC-ENTERPRISE-EXAMPLE`.

Authenticated human subjects are resolved to stable authoritative identities. Current account status, Tenant/Domain membership, roles, groups, entitlements, governance permissions, reviewer classes, scopes, and delegation attributes may become qualified governance input.

Those identity-system authorizations are not AGCP Execution Authorization. The GDF/PDP determines whether they satisfy the applicable governance conditions. The GRF revalidates commitment-sensitive authority when required.

## 4. Human review

Governance Approval Submissions are claimant commands. The authoritative approval artifact is created/qualified only after authenticated-subject binding, IAS resolution, proposal/scope binding, cryptographic verification, lifecycle checks, and quorum processing.

## 5. Canonical State and policy evaluation

Canonical State is resolved through declared authoritative source adapters. PEM evaluation is deterministic, side-effect free, and consumes qualified identity/authorization facts as inputs rather than performing live identity-store queries.

## 6. Governance Realization

The GRF validates the current Execution Authorization, proposal identity, state/evidence, authority, lifecycle, prior-use status, and target/action bindings. It then applies the selected PEP Profile.

## 7. PEP and target

The example references `PEP-GENERIC-ACTION-ADAPTER-EXAMPLE`. The PEP is positioned immediately adjacent to the protected target/adapter path and is the only ordinary governance component permitted to invoke the governed target using target-authority credentials.

Direct target credentials are unavailable to proposers, human reviewers, policy modules, and GDF-only components.

## 8. Multitenancy

Tenant and Governance Domain isolation applies to proposals, policy/configuration, identity/entitlement resolution, authority, approvals, authorizations, GRF processing, PEP Profile selection, Enforcement Context, PEP credentials, target scope, evidence, and ledger state.

## 9. Commitment and execution

This example permits operation-specific asynchronous execution. Commitment records acceptance of the exact transition at the protected boundary. Later target-outcome evidence establishes operational completion or failure when distinct.

## 10. Management and test control

Production management and isolated test-control authority are separate from human governance, GDF/PDP, GRF, PEP, and target authority. Test controls may establish source conditions but may not inject decisions or commit results.

## 11. Required negative tests

The example implementation would test:

- unresolved/disabled/revoked human identity;
- missing or revoked reviewer entitlement;
- cross-Tenant identity/entitlement substitution;
- GDF/PDP decision used as direct execution authority;
- stale/revoked Execution Authorization;
- current-state or target-binding change before commitment;
- unsupported PEP mapping;
- PEP Profile substitution;
- wrong GRF caller;
- direct target bypass;
- duplicate/single-use replay; and
- asynchronous target failure after successful commitment.

## 12. Informational status

This document is an architectural example only. A deployment claiming conformance requires its own controlled authoritative Implementation Profile, IAS Profile, PEP Profile(s), objective evidence, and applicable conformance results.
