# Step 5 Workflow Schema Refactor

The six highest-priority workflow schemas were comprehensively refactored to consume the canonical DS-021 through DS-037 governance objects directly.

## Updated schemas

- DS-014 `proposal_view.json`
- DS-015 `governance_decision_result.json`
- DS-017 `execution_authorization_view.json`
- DS-018 `commit_boundary_request.json`
- DS-019 `commit_boundary_result.json`
- DS-020 `governance_evidence.json`

## Clean migration changes

The generic shared aliases `governance_decision_ref`, `execution_authorization_ref`, `governance_evidence_ref`, and `stage_evidence_ref` were removed from `common.json`. Canonical reference definitions are now owned by their respective workflow schemas. Arbitrary workflow `metadata`, `decision_basis`, `authorization_basis`, `commit_basis`, and evidence payload objects were replaced with closed, typed, integrity-bound structures or namespaced extension containers.

## Direct canonical dependencies

The refactored schemas directly consume the canonical proposal, context, Canonical State, authority, approval, receipt, refusal, qualification, composite-governance, binding, resulting-state, adjudication, and Enforcement Context schemas.
