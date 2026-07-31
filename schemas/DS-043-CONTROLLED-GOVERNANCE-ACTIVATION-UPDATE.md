# DS-043 Controlled Governance Activation Update

## Status

Implemented as the canonical AGCP v2.0 Controlled Governance Activation schema.

## Normative role

DS-043 records the governed atomic operation through which an externally approved, constitutionally validated, omission-analysis-passed, self-protection-passed governance package becomes authoritative for runtime evaluation. It establishes package identity, Governance Version, provenance, effective scope, approval, activation evidence, prior-version preservation, and rollback basis while remaining distinct from execution authorization, authority at commitment, Commit-Bound Admissibility, and transition commitment.

## Clean migration changes

- Replaced the transitional DS-041 activation object with the DS-043 canonical reference.
- Added a DS-041 candidate-configuration reference for activation packages.
- Removed independent `activated_at` fields from policy, module, constraint, invariant, exception, and artifact-view schemas.
- Required those artifact schemas to reference DS-043 for pending, successful, failed, and historical activation states.
- Replaced the generic Governance Version activation-evidence reference with the DS-043 activation reference.

## Traceability

ARM-506 through ARM-512; Core Sections 15.6A and 15.6B; NS-15.6A-03, NS-15.6A-04, and NS-15.6B-02; CR-111 through CR-114 and CR-117.
