# AGCP OpenAPI v2.1.x Migration Update

**Date:** 2026-10-03

This synchronization preserves the `/agcp/v2` public namespace and IF-001 through IF-005 identifiers. No IF-006 is introduced.

Key changes:

- `/commit-boundary/commit` now invokes Governance Realization; the GRF independently re-establishes current authority/state/evidence/bindings, selects/applies the PEP Profile, constructs Enforcement Context, and mediates the PEP.
- `Commit Successful` records commitment, not universal completion of asynchronous target execution. DS-052 carries post-commit operational outcome.
- Governance-approval ingress treats claimed identity, roles, entitlements, and authorization as non-authoritative; the server performs IAS qualification represented by DS-053.
- `/meta` advertises IAS and PEP Profile bindings when applicable.
- IF-003 observations distinguish IAS qualification, GDF/PDP, GRF, PEP enforcement, commitment, and execution outcome.
- IF-005 authority fixtures may emulate identity/account/role/group/entitlement/authorization source conditions, while normal governance processing derives the result.

IAS lookup and GRF-to-PEP transport remain implementation/profile-defined rather than standardized public HTTP interfaces.
