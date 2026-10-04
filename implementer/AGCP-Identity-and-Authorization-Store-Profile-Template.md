# AGCP Identity and Authorization Store Profile Template

## 1. Profile Control

- Profile ID:
- Version:
- SHA-256:
- Owner:
- Applies to Implementation Profile:

## 2. Authoritative Sources

| Source ID | Type | Authoritative fact classes | Subject keys | Resolution interface | Service identity ref | Freshness |
|---|---|---|---|---|---|---|
| | | | | | | |

## 3. Subject Resolution

- Authenticated subject key:
- Stable subject ID:
- Account ID:
- Tenant/Domain mapping:
- Ambiguous/missing mapping behavior:

## 4. Authorization and Entitlement Facts

| Fact | Meaning | Authoritative source | Commitment-sensitive | Scope/validity |
|---|---|---|---|---|
| account_status | | | | |
| tenant_membership | | | | |
| role | | | | |
| group | | | | |
| entitlement | | | | |
| governance_permission | | | | |
| reviewer_class | | | | |
| delegation / authority | | | | |

## 5. Source Precedence and Conflict Rules

Describe precedence, merge, conflict, and fail-closed behavior.

## 6. Freshness and Cache

Document TTL, refresh, stale-data handling, and commitment-time revalidation.

## 7. Failure Behavior

Document unavailable, stale, conflict, disabled/revoked, missing-entitlement, and scope-mismatch behavior.

## 8. Security

Document service credential references, least privilege, transport protection, and secret handling.

## 9. Evidence and Privacy

Document evidence fields, profile/source references, and sensitive-data minimization.

## 10. Profile-Specific Tests

Include unresolved subject, disabled account, entitlement removal, role/scope mismatch, cross-Tenant substitution, conflicting source, source outage, and stale-cache tests.
