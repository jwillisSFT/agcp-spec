# AGCP v2.1.x Test-Control Mapping Regeneration Update

**Regeneration identifier:** `AGCP-v2.1.x-TEST-CONTROL-MAPPING-REGENERATION-2026-10-03`  
**Status:** Complete  
**Formal Test Case coverage:** `TC-001` through `TC-122`

## Scope

This controlled step regenerates the test-control/observation mapping after Formal Test Case synchronization, complete Test Matrix regeneration, and complete test-mapping regeneration. It does not modify the frozen CR set or create new Formal Test Case identifiers.

## Regenerated artifacts

- `conformance/test-control-mapping.json`
- `conformance/AGCP-Test-Control-Mapping.md`
- `conformance/AGCP-v2.1.x-test-control-mapping-validation.json`
- `conformance/test-control-mapping-validation.json`

## Result

- 122 Formal Test Cases mapped exactly once.
- All mapped IF-005 control names validate against DS-050.
- All mapped Governance Observation Points validate against DS-046.
- Runtime binding/effect/consumption gates are carried explicitly.
- Standardized control support is treated as implementation-dependent and discoverable at runtime; the mapping does not claim that every enumerated injection point is already implemented.
- Additional non-standardized harness injection needs are recorded for the asynchronous execution and enforcement-boundary negative paths where current DS-050 controls do not fully express the needed mutation.
- IF-005 controls remain precondition controls only and may not inject expected governance or conformance outcomes.

## v2.1.x-specific control additions

The regenerated mapping adds or clarifies control support for IAS source failure and authority changes, commitment-distinct/asynchronous execution outcomes, per-participant current authority in coordinated actions, and GRF-to-PEP caller/binding negative paths. These additions are derived from the synchronized Formal TCs and do not broaden the frozen CRs.

## Downstream work intentionally not performed in this step

This step does **not** regenerate Harness Test Vector content, Harness Check definitions, the final aggregate conformance validation, or the RTM.

## Next controlled step

Synchronize and regenerate the Harness Test Vectors and Harness Checks against the current Formal TCs, Test Matrix, test mappings, and test-control mappings.
