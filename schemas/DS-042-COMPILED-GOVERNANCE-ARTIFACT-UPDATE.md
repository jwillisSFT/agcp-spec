# DS-042 Compiled Governance Artifact Update

## Summary

Implemented `compiled_governance_artifact.json` as DS-042 and integrated it into the governance-artifact layer.

## Canonical responsibilities

DS-042 now owns:

- deterministic Compilation Context and build identity;
- complete source and validated dependency manifests;
- machine-evaluable representation and integrity digest;
- Domain Constraint Sets and Execution Constraint Sets;
- preservation of constraints, invariants, refusal paths, escalation semantics, evidence requirements, authority rules, and commit meaning;
- complete Governance Artifact Lineage and replay material;
- Constitutional Validation;
- Governance Omission Analysis;
- Governance Self-Protection assessment;
- eligibility for later DS-043 Controlled Governance Activation.

DS-042 does not establish authority at commitment, determine Commit-Bound Admissibility, authorize execution, or activate itself.

## Integrated schemas

The following schemas now reference DS-042 rather than independently representing compilation status:

- `policy_evaluation_module_artifact.json`
- `policy_artifact.json`
- `constraint_artifact.json`
- `invariant_definition.json`
- `exception_artifact.json`
- `governance_artifact_view.json`

## Traceability

DS-042 is mapped to CR-110 through CR-114 and ARM-501 through ARM-512.
