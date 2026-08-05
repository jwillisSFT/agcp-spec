# DS-045 Governance Approval Submission Update

**Finding:** P0-06  
**Schema Catalog:** 1.0.50  
**Date:** 2026-08-03

DS-045 is the untrusted IF-001 governance-approval ingress command. It carries claimant content and provenance but cannot carry AGCP-derived verification, eligibility, Canonical State, authority, replay, quorum, lifecycle, evidence, digest, or ledger results. DS-026 remains the authoritative AGCP-created or AGCP-qualified Governance Approval Artifact and now requires `artifact_origin = AGCP_CREATED_OR_QUALIFIED`.
