# DS-011 Governance Constraint Evaluation Result Update

## Scope

This update comprehensively refactors `constraint_evaluation.json` for the AGCP v2.0 schema model.

## Canonical evaluation binding

DS-011 now binds every constraint evaluation to:

- a stable evaluation identity;
- the canonical DS-007 Governance Constraint Artifact;
- the canonical DS-021 Governed Action Proposal and Proposal Identity;
- Tenant, governance domain, and target;
- governance pipeline stage and evaluation horizon;
- active Governance Version and DS-041 Governance Configuration;
- applicable DS-006 Governance Policy artifacts;
- qualified Canonical State, evidence, authority, and lifecycle inputs when required;
- a complete set of integrity-protected qualified-input digests.

## Deterministic outcome model

The canonical outcomes are:

- `SATISFIED`;
- `VIOLATED`;
- `INDETERMINATE`;
- `NOT_APPLICABLE`.

Outcome-specific conditional validation prevents contradictory objects. Satisfied evaluations require all required inputs to be qualified. Violated and indeterminate evaluations require their controlling reason and condition or dimension basis. Structural Refusal requires both a registered rejection code and a DS-028 Refusal Record.

## Evidence, attribution, integrity, and replay

DS-011 now requires Governance Evidence, accountable attribution, provenance, result digest, cryptographic integrity proof, explicit deterministic ordering basis, and replay material. Arrival timing and implementation-specific scheduling cannot serve as governance bases.

## Clean migration

The unrestricted `metadata` property was removed. The obsolete shared `constraint_outcome_enum` definition was removed from `common.json`; DS-011 now owns its canonical outcome vocabulary. No backward-compatibility alias was retained.

## Traceability

DS-011 is mapped to ARM-105, ARM-202, ARM-203, ARM-204, ARM-505, ARM-506, ARM-601, ARM-604, ARM-606, and ARM-701, with corresponding Normative Statements and CR-001, CR-063 through CR-066, CR-075, CR-076, and CR-078.

## Validation result

All 44 Draft 2020-12 schemas passed metaschema validation. All cross-schema references resolved. Positive satisfied, violated, and not-applicable cases passed. Negative tests rejected missing identity, unrestricted metadata, contradictory qualification, missing violation basis, incomplete Structural Refusal, arrival-time ordering, execution-authority claims, missing qualified-evidence bindings, unhashed constraints, and unversioned policies.
