# AGCP v2.1.x DS / Interface / API Change Set

**Date:** 2026-10-03

This package integrates the previously updated Trust Model, ARM, Core, companion/profile layer, and Normative Statements with the DS/interface/API synchronization.

## New schemas

- DS-052 Governed Execution Outcome
- DS-053 Identity and Authorization Qualification Result

## Structural schema revisions

DS-001, DS-003, DS-006, DS-007, DS-008, DS-011, DS-012, DS-014, DS-015, DS-017, DS-018, DS-019, DS-020, DS-022, DS-024, DS-026, DS-027, DS-028, DS-029, DS-030, DS-034, DS-038, DS-040, DS-041, DS-045, DS-046, DS-050, DS-051, DS-052, DS-053

The regression review moved DS-006, DS-007, DS-008, DS-011, and DS-012 into the structural-change set because their closed input contracts could not express DS-053 identity/authorization qualification. DS-004, DS-005, DS-009, DS-010, DS-013, DS-021, DS-023, DS-025, DS-031, DS-032, DS-033, DS-035, DS-036, DS-037, DS-039, DS-042, DS-043, DS-044, DS-047, DS-048, and DS-049 remain structurally unchanged apart from targeted descriptive synchronization where noted.

No new public IF identifier is introduced. IAS lookup and GRF-to-PEP transport remain controlled by the Implementation Profile, IAS Profile, and PEP Profile.

The final RTM and conformance-test synchronization are intentionally deferred to their subsequent controlled steps.
