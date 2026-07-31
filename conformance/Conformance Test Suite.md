# AGCP Conformance Test Suite

## Purpose

The AGCP Conformance Test Suite defines the normative conformance methodology used to verify implementations of the Artificial Intelligence Governance Control Plane (AGCP).

This document specifies how conformance tests are organized, traced, executed, and evaluated. Detailed test procedures are maintained in controlled Test Case batch documents under the `tests/` directory. The governing relationship among requirements, the RTM, Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, and conformance determinations is defined in `AGCP-Conformance-Traceability-and-Automation-Model.md`.

## Scope

The Conformance Test Suite verifies implementation conformance to the published CRs, the AGCP Core Specification, and any applicable normative Companion Specifications expressly adopted by the implementation profile. Core-derived Normative Statement identifiers support traceability and test construction but do not supersede those normative sources.

## Conformance Model

The AGCP conformance model separates the authoritative assessment procedure from supporting automation:

```text
Published Runtime Governance Conformance Requirement (CR)
            +
Applicable AGCP Core behavior and adopted Companion obligations
            |
            | mapped in the RTM using Core-derived NS identifiers
            v
Formal Test Case (TC)
       /                         \
      v                           v
Non-automated evidence       Harness Checks
                                  |
                                  v
                           Harness Test Vectors
                                  |
                                  v
                           Execution evidence
       \                         /
        v                       v
           Objective TC Evidence
                    |
                    v
        PASS / FAIL / NOT APPLICABLE
```

Harness Checks and Harness Test Vectors automate portions of Formal Test Cases. They do not replace Formal Test Cases, create independent normative requirements, or independently establish conformance.

## CR-to-TC Mapping Rule

Each Runtime Governance Requirement (CR) SHALL be verified by exactly one Conformance Test Case (TC).

Each Conformance Test Case SHALL verify every Normative Statement mapped to its corresponding CR in the Requirements Traceability Matrix (RTM).

A Test Case MAY contain multiple assertions where necessary to verify all mapped Normative Statements.

## Test Organization

```text
conformance/
├── AGCP-Conformance-Traceability-and-Automation-Model.md
├── AGCP-Conformance.md
├── Conformance Test Suite.md
├── AGCP-Test-Matrix.md
├── AGCP Harness Check Registry.md
├── harness-checks.json
├── AGCP-Conformance-Harness-Spec.yml
├── AGCP-Conformance-Test-Vectors.md
├── test-mapping.json
├── fixture-mapping.json
└── tests/
    ├── TC001-TC010.md
    ├── ...
    └── TC121-TC122.md
```

## Test Case Structure

Each Test Case SHALL include:

- Requirement Under Test (CR)
- Normative Statements Covered
- Conformance Level
- Test Objective
- Preconditions
- Request / Scenario
- Simulated Execution Trace
- Ledger Delta
- Derived State
- Expected Result
- Pass Criteria
- Fail Criteria

## Evidence Requirements

Each successful conformance test SHALL produce objective evidence sufficient to demonstrate:

- Proposal Qualification and Governance Decision Function outcomes
- Execution Authorization outcome where applicable
- applicable pre-commit Continuation Integrity outcome for a nonterminal Proposal
- Governance Realization and final Commit-Bound Admissibility outcome where applicable
- Policy Enforcement Point and Commit Boundary behavior where applicable
- Governance Evidence generated and bound throughout every applicable governance-significant stage as a cross-cutting supporting service
- Lifecycle outcome
- Applicable tenant and governance domain context

## Conformance Result

Each Test Case SHALL result in one of the following outcomes:

- PASS
- FAIL
- NOT APPLICABLE

## Relationship to the RTM

The Requirements Traceability Matrix is the authoritative mapping between:

- Runtime Governance Requirements (CR)
- Normative Statements (NS)
- Conformance Test Cases (TC)

The Conformance Test Suite SHALL remain synchronized with the RTM.

## Relationship to Individual Test Cases

This document defines the conformance methodology.

Detailed execution procedures are maintained in the controlled Test Case batch documents located in the `tests/` directory. Each TC remains individually identified and assessed even when several TCs are stored in one Markdown file.

## Versioning

This document is governed by the AGCP repository release. The authoritative Test Suite is the version included in the controlled repository release and SHALL remain synchronized with the RTM, Formal Test Cases, relationship model, and machine-readable conformance mappings.
