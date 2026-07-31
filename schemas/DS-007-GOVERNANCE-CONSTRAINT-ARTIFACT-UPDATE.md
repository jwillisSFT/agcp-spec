# DS-007 Governance Constraint Artifact Update

## Summary

`constraint_artifact.json` was comprehensively revised as the canonical v2.0 Governance Constraint artifact. It now records deterministic constraint semantics, source lineage, protected or constitutional classification, Governance Configuration binding, DS-042 compilation and validation evidence, DS-043 activation, Governance Version, and explicit non-weakening controls.

## Clean migration changes

- Removed `common.json#/$defs/constraint_id` and `common.json#/$defs/constraint_ref`.
- Added `constraint_artifact.json#/$defs/constraint_artifact_ref`.
- Updated 7 active schemas plus `common.json` to reference DS-007 directly.
- Removed unrestricted `parameters` and `metadata` objects.
- Replaced them with digest-bound parameter bindings, deterministic applicability conditions, explicit required governance inputs, and typed outcome semantics.
- Added protected and constitutional classification, source and derivation lineage, Governance Artifact Lineage projection, Constitutional Validation, Governance Omission Analysis, Governance Self-Protection, activation eligibility, Controlled Governance Activation, Governance Version, replay, provenance, and integrity structures.

## Traceability

DS-007 is directly mapped to CR-063 and contextually mapped to CR-110 through CR-114 and CR-117. The RTM dataset version is RTM-1.32 and the schema catalog version is 1.0.28.
