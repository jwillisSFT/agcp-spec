# DS-005 Policy Evaluation Module Artifact Update

## Summary

`policy_evaluation_module_artifact.json` was comprehensively refactored as the canonical AGCP v2.0 Policy Evaluation Module artifact. The schema now binds deterministic runtime representation and interface behavior to source policy artifacts, Governance Configuration, controlled registries, DS-042 compilation context and deterministic build identity, validated dependencies, Governance Artifact Lineage, Constitutional Validation, Governance Omission Analysis, Governance Self-Protection, DS-043 Controlled Governance Activation, Governance Version, evidence, integrity, and replay material.

## Clean migration changes

- DS-005 now owns `policy_evaluation_module_artifact_ref`.
- DS-006 `policy_module_binding` now references DS-005 directly.
- The former unconstrained `metadata` object and legacy `determinism_verified` flag were removed.
- Independent compilation and activation status is not duplicated; DS-005 carries integrity-bound projections and references to DS-042 and DS-043.
- Active modules require validated compilation, successful constitutional and omission analysis, Governance Self-Protection, activated DS-043 evidence, active DS-041 configuration, Governance Version, and effective time.
- Module evaluation is side-effect-free and cannot establish authority, authorize execution, activate governance, or commit transitions.

## Traceability

DS-005 is mapped to CR-110 through CR-114 and CR-117 and to the corresponding ARM-500 series and NS-15.6A/15.6B statements.


## Informational machine-contract example

The registered-module example uses an explicitly implementation-defined IF-002 machine-contract identifier and example.invalid URIs. DS-005 remains technology-independent; an operational implementation binds its selected machine contract through the existing runtime-representation and interface-contract fields under its separately controlled Implementation Profile.
