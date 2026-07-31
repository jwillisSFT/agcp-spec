# DS-010 Governance Artifact View Update

## Summary

`governance_artifact_view.json` was comprehensively revised as the canonical externally observable, integrity-protected read model for governance-significant artifacts.

## Principal changes

- Added stable Governance Artifact View identity, view version, digest, signature, attribution, and provenance.
- Replaced unconstrained artifact summary and metadata objects with a bounded non-normative display summary and namespaced extensions.
- Added explicit Governance Configuration and Governance Version references.
- Added DS-042-backed compilation projection containing compilation status, Governance Artifact Lineage, Constitutional Validation, Governance Omission Analysis, Governance Self-Protection, and activation eligibility.
- Added DS-043-backed activation projection containing package identity, external approval basis, validation basis, atomicity, activation result, rollback basis, Governance Version establishment, and activation evidence.
- Added lifecycle history and governed re-evaluation basis.
- Added lifecycle-to-compilation and lifecycle-to-activation consistency rules.
- Added explicit assertions that the view is non-authoritative and cannot activate governance, establish authority at commitment, or authorize execution.

## Traceability

- ARM: ARM-502, ARM-506 through ARM-512
- Core: Sections 15.5, 15.6A, 15.6B
- NS: NS-15.5-01 through NS-15.5-03; NS-15.6A-01 through NS-15.6A-04; NS-15.6B-01 through NS-15.6B-02
- CR: CR-110 through CR-114; CR-117
