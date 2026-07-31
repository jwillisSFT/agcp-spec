# DS-031 Resulting-State Validation Result Update

## Implementation

- DS identifier: `DS-031`
- Canonical filename: `resulting_state_validation_result.json`
- Catalog version: `1.0.17`
- RTM version: `RTM-1.21`

DS-031 records deterministic pre-commit validation that the state projected from a single governed transition, a complete DS-035 Bind Set, or an explicitly governed executable subset satisfies applicable governance requirements.

## Normative semantics

The schema requires qualified current Canonical State, an explicit evaluation horizon, deterministic projection and ordering, target and proposal binding, policy references, projected state components, governance-requirement evaluations, aggregate validation, qualified evidence, attribution, integrity, and replay material.

A `VALID` result is eligible to continue into Commit-Bound Admissibility. An `INVALID` result requires Structural Refusal. An `INDETERMINATE` result blocks evaluation. No DS-031 outcome establishes authority, authorizes execution, selects an executable subset, or commits a transition.

## Related changes

- Removed the superseded Resulting-State Validation identifier, outcome, and reference definitions from `common.json`.
- Updated `governance_receipt.json` to use the canonical DS-031 reference.
- Added DS-031 and its reference to the OpenAPI components.
- Mapped DS-031 to CR-102 and CR-109 in RTM-1.21.
