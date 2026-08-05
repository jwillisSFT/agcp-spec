# AGCP Semantic Fixture Test Vectors

This package provides implementation-independent semantic validation for controlled positive fixtures. JSON Schema validation remains necessary but is not sufficient: references that claim to describe the same Tenant, Governance Domain, Proposal, target, policy, approval, evidence, authorization, lifecycle state, or Canonical State must agree.

The package contains ten intentionally malformed semantic-mismatch vectors and binds the existing fifteen claimant-assertion negative vectors from `conformance/command-record/AGCP-Governance-Approval-Command-Record-Test-Vectors.json`.

Positive fixtures remain in `schemas/examples/`; negative vectors remain explicitly labeled and are not cataloged as successful examples.
