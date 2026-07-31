# DS-037 Deterministic Adjudication Result Update

## Status

Implemented on 2026-07-29 as `schemas/deterministic_adjudication_result.json`.

## Purpose

DS-037 records how a complete Admissible Set of multiple currently admissible transitions was resolved for one governance horizon. It uses explicit governance-significant ordering, conflict, dependency, resource, priority, state, and policy conditions and prohibits arrival timing, transport timing, node-local scheduling, and implementation-specific behavior as governance bases.

## Outcomes

- `CANDIDATE_SELECTED`
- `EXECUTABLE_SUBSET_SELECTED`
- `NO_CANDIDATE_SELECTED`
- `INDETERMINATE`

The result does not establish authority, authorize execution, validate Governance Binding, or commit a transition. Selected candidates remain subject to Governance Binding Validation and Commit Boundary enforcement.

## Integration

- `governance_receipt.json` records DS-037 outcomes with receipt type `DETERMINISTIC_ADJUDICATION`.
- `governance_context_envelope.json` may preserve a DS-037 result reference.
- `governance_evidence.json` may aggregate DS-037 result references.
- `common.json` no longer contains the unused transitional partial-bind result aliases.
- OpenAPI exposes DS-037 and its reference definition.
- RTM-1.22 maps DS-037 to CR-094 and CR-095.
