# AGCP Conformance Framework

Version: 0.9.0

This directory contains the artifacts used to define and verify AGCP conformance.

AGCP conformance is verified through a layered traceability model:

Specification  
→ Assertions  
→ Requirements  
→ Conformance Tests

Each layer is represented by files in this directory.

---

# Conformance Artifacts

## assertions.json

Canonical machine-readable registry of normative assertions.

Assertions represent behavioral guarantees derived from the AGCP specifications.

Example assertions include:

- Deterministic ledger ordering
- Lifecycle derivability from ledger state
- Authorization gating for execution commits
- Idempotency safety
- Terminal state safety

All conformance tests ultimately verify one or more assertions.

---

## AGCP-Assertion-Registry.md

Human-readable index of assertions.

This file exists to assist reviewers and implementers during specification review.

The canonical registry remains `assertions.json`.

---

## test-mapping.json

Defines traceability between:

tests → requirements → assertions

This layer allows the conformance harness to validate that every assertion is enforced by one or more tests.

---

## AGCP Conformance Harness Spec.yml

Executable definition of the AGCP conformance harness.

The harness defines:

- Test suites
- Test vectors
- Endpoint behavior checks
- Assertion enforcement rules

Implementations claiming AGCP conformance must pass the harness.

---

# Conformance Model

The AGCP conformance framework uses the following verification chain:

Specification  
↓  
Assertion  
↓  
Requirement  
↓  
Test

This structure ensures that all normative guarantees in the specification are verifiable through automated testing.

---

# Conformance Claim

An implementation may claim AGCP conformance only if:

1. All conformance tests pass.
2. No registered assertion is violated.
3. Observed behavior matches the normative specification.

---

# Review Guidance

During public review, issues related to behavioral guarantees should reference the relevant **Assertion ID**.

Example:

Assertion: `A-ORDERING`  
Issue: Deterministic evaluation ordering clarification.

Assertion identifiers provide stable references for discussing specification behavior.

---

# Future Conformance Extensions

Future versions of AGCP may introduce additional conformance domains, including:

- Deterministic replay verification
- Distributed ledger consistency validation
- Cross-node lifecycle reconstruction
- Multi-ledger federation safety

These additions will extend the assertion registry and conformance harness.

---
