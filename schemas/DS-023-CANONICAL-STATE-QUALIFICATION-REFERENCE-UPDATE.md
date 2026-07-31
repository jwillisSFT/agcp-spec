# DS-023 Canonical State Qualification Reference Update

## Change

`canonical_state.json` now requires `qualification_result`, which references `state_qualification_result.json#/$defs/state_qualification_result_ref` and is constrained to `outcome = QUALIFIED`.

The former top-level `qualification` property that embedded the complete DS-032 result is removed. Per-source observation qualification remains a separate local structure because it qualifies individual source observations rather than the resolved Canonical State.

## Compatibility

No backward-compatibility alias is retained. Instances using the former `qualification` property must migrate to `qualification_result`.

## Traceability

DS-023 continues to depend on DS-032. RTM mappings are unchanged because this is a representation correction, not a change in normative coverage.
