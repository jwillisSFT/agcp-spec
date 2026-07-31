# DS-012 Governance Invariant Evaluation Update

## Scope

`invariant_evaluation.json` has been comprehensively refactored as the canonical, attributable, integrity-protected invariant-evaluation result for AGCP v2.0.

## Completed model changes

- Added stable evaluation identity and explicit result type.
- Bound every result to DS-008 Governance Invariant Definition, DS-021 Governed Action Proposal and Proposal Identity, Tenant, governance domain, target, evaluation horizon, active Governance Version, DS-041 Governance Configuration, and applicable DS-006 policies.
- Added qualified-input status and integrity digests for proposal, invariant, target, policy set, configuration, Governance Version, Canonical State, evidence, authority, lifecycle, and the complete evaluation input set.
- Added attributable Governance Evidence, provenance, evaluation digest, cryptographic integrity signature, and deterministic replay material.
- Added outcome-specific validation for `PRESERVED`, `VIOLATED`, `INDETERMINATE`, and `NOT_APPLICABLE`.
- Added explicit `structural_refusal_effect`, `escalation_effect`, and `lifecycle_effect` objects.
- Required Governance Evidence for every invariant-evaluation result.
- Required hard-invariant violation to produce Structural Refusal and a terminal `STRUCTURALLY_REFUSED` lifecycle effect.
- Required escalation outcomes to identify governed escalation type, reason, target lifecycle state, and applicable approval evidence.
- Removed unrestricted `metadata`; only bounded namespaced extensions remain.
- Retired the now-unused shared `pass_fail_enum` definition from `common.json`.

## Integrated artifacts

- `api/AGCP-HTTP-Contract.yaml` now exposes `InvariantEvaluation` and `InvariantEvaluationRef`.
- Schema Catalog advanced to `1.0.37`.
- RTM advanced to `RTM-1.40` and maps DS-012 to 9 semantically applicable Conformance Requirements.

## Validation summary

- 44 Draft 2020-12 schemas validated.
- 3396 schema references and JSON Pointer fragments resolved.
- Positive tests passed for preserved, hard-violation Structural Refusal, soft-violation escalation, indeterminate re-evaluation, and not-applicable outcomes.
- Negative tests reject missing identity, unrestricted metadata, unqualified preserved outcomes, incomplete refusal or escalation effects, missing Governance Evidence, lifecycle mismatches, arrival-time governance, execution-authority claims, and unhashed invariant references.
- All 63 remaining shared definitions are actively reachable.
- RTM workbook structure and formatting were preserved.
