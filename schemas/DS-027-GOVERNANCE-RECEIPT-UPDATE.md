# DS-027 Governance Receipt Update

## Status

Implemented `DS-027 governance_receipt.json` as the canonical attributable, integrity-protected record for every non-refusal governance result. Structural Refusal remains outside DS-027 and is represented by the reserved DS-028 Refusal Record.

## Canonical scope

DS-027 records proposal qualification, governance decision, execution authorization, approval or adjudication, commitment, enforcement, execution outcome, lifecycle transition, continuation-integrity, risk-based re-evaluation, and other explicitly non-refusal outcomes.

The receipt binds Proposal Identity, tenant, governance domain, target, Governance Version, qualified governance basis, evidence, authority, lifecycle, and the recorded result. It requires attribution, integrity protection, Governance Ledger recording or reference, Evidence Continuity, and independent replay-verification material.

## Dependent schema changes

- `governance_decision_result.json`: non-refusal decisions require a Governance Receipt; Structural Refusal requires a Refusal Record reference.
- `execution_authorization_view.json`: every authorization outcome requires a Governance Receipt.
- `commit_boundary_result.json`: every represented Commit Boundary outcome requires a Governance Receipt.
- `proposal_view.json`: exposes receipt and refusal references across the proposal lifecycle.
- `governance_evidence.json`: may aggregate receipt, refusal, and ledger-event references.

## Traceability

RTM RTM-1.14 maps DS-027 to CR-062 through CR-069 and CR-086. Schema Catalog 1.0.9 marks DS-027 Implemented and Active.
