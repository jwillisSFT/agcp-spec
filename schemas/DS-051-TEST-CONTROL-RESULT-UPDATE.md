# DS-051 - AGCP Test Control Result Update

**Status:** Updated for Management Control Plane-safe conformance control readback and recovery.  
**Date:** 2026-10-04  
**Schema:** `test_control_result.json`  
**Wire contract version:** `1.2`

## Changes in this update

- Adds required per-operation `runtime_binding_status`.
- Enforces `effect_status: EFFECTIVE` only when `runtime_binding_status: BOUND`.
- Adds required applying-principal readback through `requested_by`.
- Adds Tenant, Governance Domain, and finite lease expiry context needed for attributable recovery and active-control inventory.
- Requires admitted non-reset controls to preserve `expires_at`.
- Retains consumption evidence and enforcement-path mutation evidence introduced by the v2.1.0 testability closure.

## Management Control Plane usability

Capability advertisement alone is not sufficient to establish a Formal Test Case precondition. The Management Control Plane must read the individual DS-051 result and require `runtime_binding_status: BOUND` together with `effect_status: EFFECTIVE`, and must require `consumption_status: OBSERVED` when the Formal Test Case depends on proof that the controlled condition was consumed.

The additional attribution and lease fields allow a restarted Management Control Plane to enumerate active or historical controls, identify who applied them, determine their scope and expiry, and verify cleanup without retaining only local client state.

## Compatibility and authority

The root `VERSION` file remains the sole AGCP repository release-version source. `result_version: 1.2` is the DS-051 wire-format revision and is not an independent AGCP repository release number. The frozen CR set is unchanged.
