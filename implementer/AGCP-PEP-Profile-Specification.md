# AGCP PEP Profile Specification

**Status:** Controlled implementer specification  
**Profile Type:** PEP Profile  
**Profile Format Version:** 1.0.0  
**Repository Release Target:** AGCP v2.1.x

## 1. Purpose

A PEP Profile defines how the Governance Realization Function (GRF) maps an exact commit-eligible governed transition and its Enforcement Context to one concrete Policy Enforcement Point interface and target-authority boundary.

## 2. Architectural ownership

The GRF selects and applies the PEP Profile. The PEP enforces the resulting request. The PEP Profile is not a policy engine and SHALL NOT reinterpret or widen the Governance Decision.

## 3. Profile identity

The profile SHALL have a stable ID, semantic version, SHA-256 digest, and controlled artifact reference.

## 4. PEP interface and caller authentication

The profile SHALL define:

- PEP implementation/interface identity;
- endpoint, RPC, in-process, or adapter boundary;
- allowed GRF/control-plane caller identity;
- authentication/integrity requirements; and
- timeout/retry behavior consistent with idempotency and single-use semantics.

## 5. Supported action and target mappings

For each supported governed operation, the profile SHALL define exact action type, target type, required source fields, target-identifier mapping, allowed deterministic transformations, and PEP operation.

A mapping SHALL preserve proposal identity, authorization, action, target, Tenant/Domain, current commit eligibility, validity, execution constraints, and any other governance-significant binding required by the operation.

## 6. No approximate enforcement

If no faithful mapping exists, the GRF/PEP path SHALL fail closed. It SHALL NOT substitute a similar action, widen targets, discard governance-significant fields, weaken conditions, or infer unsupported execution semantics.

## 7. Enforcement Context

The profile SHALL declare the Enforcement Context fields or references required by the PEP, including proposal/authorization/commit/binding/profile information necessary to prevent mismatch or replay.

## 8. Idempotency, single use, and validity

The profile SHALL define idempotency keys, replay prevention, authorization consumption, single-use behavior, validity windows, and safe retry semantics.

## 9. PEP response and outcome mapping

The profile SHALL deterministically map PEP responses to AGCP enforcement/commit/execution evidence states. Unknown or integrity-invalid responses SHALL fail closed.

## 10. Commitment versus target completion

The profile SHALL declare whether the PEP/target operation is atomic with commitment, asynchronous/distinct, or operation-dependent. Where distinct, commitment evidence and later execution-outcome evidence SHALL be separately reconstructable.

## 11. PEP-to-target authority

The profile SHALL identify the target-authority/credential reference used by the PEP and the scope of targets/effects it can produce. Proposal-side principals and GRF-only principals SHALL NOT automatically possess target credentials.

## 12. Evidence and receipts

The profile SHALL define required PEP request/response digests, target receipts, and execution evidence sufficient to bind the operational outcome to the exact governed transition.

## 13. Testing

Profile-specific tests SHOULD include unsupported action, target mismatch, authorization mismatch, stale/replayed request, profile substitution, widened target, dropped required field, wrong GRF caller, direct target bypass, duplicate effect, PEP refusal, and asynchronous completion/failure cases.
