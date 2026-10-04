# AGCP Identity and Authorization Store Profile Specification

**Status:** Controlled implementer specification  
**Profile Type:** IAS Profile  
**Profile Format Version:** 1.0.0  
**Repository Release Target:** AGCP v2.1.x

## 1. Purpose

The Identity and Authorization Store (IAS) Profile declares how an AGCP implementation resolves authoritative identity plus identity-system authorization/entitlement information used as governance input.

An IAS Profile may describe one authoritative store or a controlled composition of multiple sources. Each source's authoritative fact scope and precedence SHALL be explicit.

## 2. Relationship to AGCP authority

IAS data may establish facts such as subject identity, account state, Tenant/Domain membership, role, group, entitlement, governance permission, reviewer class, delegated authority, scope, and validity.

IAS data is not AGCP Execution Authorization, does not itself create a Governance Approval Artifact, and does not itself produce a Governance Decision or commit result. The GDF/PDP and GRF consume qualified IAS facts according to governance and lifecycle semantics.

## 3. Required profile identity

The IAS Profile SHALL contain a stable profile ID, semantic version, SHA-256 digest, and controlled artifact reference.

## 4. Authoritative sources

For each source the profile SHALL define:

- source ID and type;
- authoritative fact classes;
- subject/account identifier keys;
- Tenant/Domain scoping;
- resolution interface or adapter;
- service/workload identity used by AGCP;
- trust/integrity basis;
- freshness/cache/TTL rules;
- outage and stale-data behavior; and
- evidence/provenance requirements.

## 5. Subject resolution

The profile SHALL define how an authenticated subject is mapped to a stable authoritative subject/account record. Claimant-supplied display names or account labels SHALL NOT become authoritative merely by assertion.

Ambiguous, missing, conflicting, or unverifiable mappings SHALL fail closed for governance functions requiring the identity.

## 6. Authorization and entitlement facts

The profile SHALL identify governance-significant fact classes, including as applicable:

- account active/disabled/suspended/revoked status;
- Tenant and Governance Domain membership;
- roles;
- groups;
- entitlements;
- governance permissions;
- reviewer classes;
- scope restrictions;
- delegation/authority attributes;
- separation-of-duty attributes;
- effective/expiry periods; and
- revocation/supersession state.

The profile SHALL define the semantic meaning and authoritative source of each declared fact class.

## 7. Source composition and precedence

If multiple sources are used, the IAS Profile SHALL specify deterministic precedence, merge rules, conflict behavior, and fact ownership. A lower-authority source SHALL NOT override a higher-authority source for the same declared fact class.

## 8. Freshness and revalidation

The profile SHALL define freshness and cache semantics for each commitment-sensitive fact class. When governance requires current authority at commitment, the GRF SHALL re-resolve or revalidate those fact classes according to the profile.

## 9. Failure behavior

Required identity or authorization/entitlement facts that are unavailable, stale beyond allowed bounds, conflicting, invalid, revoked, or unverifiable SHALL produce a profile-defined non-execution path. The implementation SHALL NOT replace them with claimant assertions or speculative defaults.

## 10. Security

The profile SHALL reference protected service credentials rather than contain secrets. Least privilege SHALL limit the AGCP identity-resolution workload to the facts and subjects required by the declared scope.

## 11. Evidence

Evidence SHALL be sufficient to reconstruct which IAS Profile and source versions were used, the stable subject/account identity, the governance-significant fact basis, freshness result, and any failure or conflict disposition without unnecessarily exposing sensitive directory contents.

## 12. Conformance and profile-specific testing

Deployment-specific tests SHOULD include unresolved subject, disabled/revoked account, stale entitlement, missing required role, scope mismatch, Tenant/Domain mismatch, conflicting source, source unavailable, and claimant-substitution cases.
