# DS-008 Governance Invariant Definition Update

## Summary

`invariant_definition.json` has been comprehensively updated as the canonical DS-008 Governance Invariant Definition for AGCP v2.0. The prior thin registry-oriented object has been replaced with an attributable, versioned, integrity-protected governance artifact that preserves deterministic invariant semantics, source specification and governance lineage, effective scope, protected or constitutional classification, enforcement level, non-weakening controls, Governance Configuration binding, DS-042 compilation and validation evidence, DS-043 Controlled Governance Activation, Governance Version, Governance Evidence, and replay material.

## Clean migration changes

The shared `common.json` definitions `invariant_id`, `invariant_enforcement_enum`, and `invariant_ref` were removed. Canonical invariant identity, enforcement, and reference definitions are now owned by DS-008. All active references were migrated to `invariant_definition.json#/$defs/...`; no backward-compatibility alias remains.

## Updated dependent schemas

- `common.json`
- `compiled_governance_artifact.json`
- `governance_dependency_graph.json`
- `invariant_evaluation.json`
- `policy_artifact.json`
- `refusal_record.json`

## Traceability

DS-008 is mapped to CR-003, CR-053, CR-063, CR-076, CR-110 through CR-114, and CR-117. The Schema Catalog is version 1.0.29 and the RTM is version RTM-1.33.

## Validation

All 40 implemented schemas validate under JSON Schema Draft 2020-12. All 2,743 schema references and JSON Pointer fragments resolve. Registered, protected, constitutional, and active invariant definitions pass. Invalid soft-protected, exceptionable-constitutional, unactivated-active, invalid-compilation, arrival-timing, weakening, arbitrary-metadata, premature-compilation, execution-authority, and unhashed-reference cases are rejected. The RTM workbook structure and formatting are preserved.
