# DS-050 - AGCP Test Control Request Update

**Status:** Updated for Management Control Plane-safe conformance control operation.  
**Date:** 2026-10-04  
**Schema:** `test_control_request.json`  
**Wire contract version:** `1.2`

## Changes in this update

- Requires a finite `expires_at` lease for every non-`RESET_TEST_SCOPE` control.
- Preserves typed fixture requirements for every non-reset control.
- Retains `RESET_TEST_SCOPE` as the explicit deterministic cleanup operation without requiring an expiry on the reset command itself.
- Keeps all fixture semantics input-only: test controls establish source/dependency conditions and never inject the expected governance or conformance result.

## Management Control Plane usability

The finite lease is a fail-safe for abandoned or disconnected test-control clients. Runtime implementations SHALL deactivate an expired test condition without deleting its historical evidence. The Management Control Plane can still issue `RESET_TEST_SCOPE` for deterministic cleanup before the lease expires.

## Compatibility and authority

The root `VERSION` file remains the sole AGCP repository release-version source. `control_version: 1.2` is the DS-050 wire-format revision and is not an independent AGCP repository release number. The frozen CR set is unchanged; this update refines the interoperable test-control contract needed to exercise existing Formal Test Cases.
