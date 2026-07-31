# DS-006 Governance Policy Artifact Update

## Summary

`policy_artifact.json` was comprehensively revised as the canonical v2.0 Governance Policy artifact. It now represents attributable policy intent and deterministic policy semantics, binds those semantics to DS-041 Governance Configuration, and references DS-042 compilation and DS-043 activation records rather than duplicating their authoritative state.

## Clean migration changes

- Removed `common.json#/$defs/policy_ref`.
- Added `policy_artifact.json#/$defs/policy_artifact_ref`.
- Updated 22 active schemas to reference DS-006 directly.
- Removed unrestricted `metadata` from the policy artifact.
- Replaced the thin `policy_module_ref` string with an integrity-bound module binding.
- Added explicit source governance intent, policy source representation, rule semantics, deterministic conflict resolution, authority, evidence, Canonical State, lifecycle, commit, composite-governance, refusal-path, escalation, protected-property, replay, provenance, and integrity structures.

## Lifecycle integration

Status-specific validation now enforces compilation and activation consistency for Registered, Compiled, Validation Pending, Validated, Accepted, Validation Failed, Rejected, Activation Pending, Active, Activation Failed, Superseded, Deprecated, Retired, and Governed Re-evaluation Required policy artifacts.

## Traceability

DS-006 is directly mapped to CR-007 and contextually mapped to CR-110 through CR-114 and CR-117. The RTM dataset version is RTM-1.30 and the schema catalog version is 1.0.26.
