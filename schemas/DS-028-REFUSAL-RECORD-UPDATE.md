# DS-028 Refusal Record Implementation Report

## Summary

Implemented `DS-028 refusal_record.json` as the canonical attributable, integrity-protected, Governance-Ledger-recorded, and replay-verifiable record for Structural Refusal.

## Scope boundary

DS-028 documents only Structural Refusal. Policy denial, authorization failure, commit failure, deferral, expiration, cancellation, and governed re-evaluation remain non-refusal governance results documented through DS-027 unless a separate Structural Refusal is applied.

## Required controls

- Proposal Identity, tenant, governance domain, target, and Governance Version binding
- Refusal stage and registered rejection code
- Structured refusal basis for invariant, evidence, Canonical State, binding, authority, dependency, resulting-state, and negative-adjudication failures
- Lifecycle effect proving that operational realization was prevented and execution did not occur
- Attributable Governance Evidence and Evidence Continuity
- Ordered Governance Ledger event reference
- Cryptographic integrity and deterministic replay-verification material

## Updated dependents

- `governance_context_envelope.json`
- `governance_decision_result.json`
- `proposal_view.json`
- `governance_evidence.json`
- `error_response.json`
- `commit_boundary_result.json`

## Traceability

RTM-1.15 maps DS-028 to CR-053, CR-054, CR-055, CR-056, CR-057, CR-060, CR-087, and CR-088.
