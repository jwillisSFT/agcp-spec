# Conformance

## Purpose

This directory contains the AGCP conformance framework used to verify
that an implementation satisfies the normative requirements defined by
the AGCP specifications.

The conformance artifacts provide human-readable documentation,
machine-readable mappings, executable harness checks, and deterministic
test vectors. Together they support repeatable, auditable, and
deterministic verification of AGCP implementations.

The governing relationship semantics among requirements, the RTM, Formal
Test Cases, Harness Checks, Harness Test Vectors, execution evidence, and
conformance determinations are defined in
`AGCP-Conformance-Traceability-and-Automation-Model.md`.

------------------------------------------------------------------------

# Conformance Architecture

The authoritative requirement and assessment path is:

``` text
Published CRs + AGCP Core + adopted normative Companion Specifications
        |
        | identified and mapped through Core-derived NS identifiers
        | in the authoritative RTM
        v
Formal Test Case (TC)
        |
        v
Objective evidence
        |
        v
PASS / FAIL / NOT APPLICABLE
```

Executable automation is a supporting branch of the Formal Test Case:

``` text
Executable TC propositions
        ↓
Harness Checks
        ↓
Harness Test Vectors and controlled setup
        ↓
Harness execution results
        ↓
Objective evidence evaluated under the Formal Test Case
```

Harness Checks and Harness Test Vectors SHALL NOT introduce independent
normative requirements or independently establish Test Case or profile
conformance. The complete relationship and cardinality rules are defined
in `AGCP-Conformance-Traceability-and-Automation-Model.md`.

------------------------------------------------------------------------

# Directory Contents

  -----------------------------------------------------------------------
  Artifact                              Purpose
  ------------------------------------- ---------------------------------
  AGCP-Conformance-Traceability-        Defines the normative relationship
  and-Automation-Model.md                semantics among CRs, NS identifiers,
                                        the RTM, Formal Test Cases, Harness
                                        Checks, Test Vectors, evidence, and
                                        conformance determinations.

  AGCP-Conformance.md                   Defines the AGCP conformance
                                        model, profiles, and verification
                                        requirements.

  Conformance Test Suite.md             Defines the authoritative Test Case
                                        methodology and assessment-result
                                        rules.

  AGCP-Test-Matrix.md                   Human-readable summary of
                                        validated capabilities and
                                        representative Harness Test
                                        Vectors.

  AGCP-Conformance-Test-Vectors.md      Deterministic execution scenarios
                                        covering governance behavior and
                                        observable outcomes.

  AGCP-Conformance-Harness-Spec.yml     Defines execution behavior for
                                        the automated conformance
                                        harness.

  AGCP-harness-request-parameter-       Controlled validation record proving
  validation.json                       that every primary request and HTTP
                                        setup prestep supplies required IF-001
                                        path, query, and header parameters.

  AGCP-harness-error-model-             Controlled validation record proving
  validation.json                       that every declared rejection-code and
                                        HTTP-status pair agrees with the
                                        normative Error Mapping and active
                                        rejection-code registry, and that every
                                        expected vector status is declared by
                                        the matched IF-001 OpenAPI operation.

  AGCP-if001-executable-operation-      Controlled validation record proving
  coverage-validation.json              that all ten mandatory IF-001 operations
                                        have schema-valid positive executable
                                        coverage and the applicable negative,
                                        tenant/domain-isolation, and idempotency
                                        scenarios defined by the coverage model.

  AGCP-governance-compilation-          Controlled validation record proving
  activation-executable-validation.json that every MUST Harness Check has substantive
                                        executable coverage and that Governance
                                        Configuration, compilation, constitutional
                                        validation, omission analysis, self-protection,
                                        atomic activation, rollback, evidence, and
                                        lineage behaviors are asserted.

  AGCP Harness Check Registry.md        Human-readable registry of
                                        executable Harness Checks.

  harness-checks.json                   Machine-readable Harness Check
                                        registry.

  fixture-mapping.json                  Exact schema-to-example fixture
                                        mapping and validation metadata.

  test-mapping.json                     Machine-readable mapping among NS,
                                        CR, TC, DS, IF, REG, fixtures,
                                        Harness Checks, and Harness Test
                                        Vectors, including explicit no-vector
                                        dispositions.

  agcp-conformance-manifest.yml         Index of the conformance package
                                        and execution metadata.

  tests/                                Controlled Formal Test Case batch
                                        documents for TC-001 through TC-122.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Scope

The conformance suite verifies, where applicable:

-   Proposal Qualification
-   Governance Decision Function
-   Governance Approval and Adjudication
-   Execution Authorization or another eligible nonterminal state
-   applicable pre-commit Continuation Integrity until final Commit-Bound Admissibility is resolved
-   Governance Realization, including current-state, evidence, authority, binding, and resulting-state validation
-   Policy Enforcement Point and Commit Boundary processing
-   Provenance validation
-   Ordered Append-Only Governance Ledger behavior
-   Canonical State resolution and deterministic replay
-   Idempotency
-   Tenant lifecycle enforcement
-   Tenant and Governance Domain isolation
-   Published registries
-   all ten mandatory IF-001 HTTP operations, including metadata discovery,
    Proposal and authorization retrieval, governance-artifact registration and
    retrieval, and the applicable negative, isolation, and idempotency behavior

Governance Evidence is a cross-cutting supporting service generated during every applicable governance-significant stage. It is not a terminal pipeline stage.

------------------------------------------------------------------------

# Canonical State

Canonical State SHALL be deterministically resolved from qualified authoritative governance sources. The ordered Governance Ledger is authoritative for recorded governance events, authoritative event ordering, and Derived Lifecycle State. Materialized governance state used for replay must be verifiably derived from the applicable authoritative sources and ledger records.

Ledger sequence order is authoritative. Timestamp order is not.

------------------------------------------------------------------------

# Canonical Fixture Catalog

`fixture-mapping.json` maps every conformance example to its exact active DS schema and expected validation result. The examples are maintained in `../schemas/examples/`. The 29 controlled fixtures include the existing governance, ledger, approval, commit, and registry examples plus schema-valid IF-001 response examples for DS-003, DS-005, DS-006, DS-010, and DS-017.

Fixture resolution occurs before IF-001 request validation. Commit Boundary tests use the current DS-018 representation and the `/agcp/v2` namespace exclusively.

------------------------------------------------------------------------

# Relationship to the Requirements Traceability Matrix

The Requirements Traceability Matrix (RTM) is the authoritative mapping
between:

-   Normative Statements (NS)
-   Conformance Requirements (CR)
-   Test Cases (TC)

The Formal Test Cases provide the authoritative assessment procedures.
Harness Checks and Harness Test Vectors provide executable support for
portions of those procedures and SHALL remain synchronized with the RTM,
the Test Cases, and `test-mapping.json`. Automation produces evidence; it
does not independently determine conformance.

------------------------------------------------------------------------

# Normative vs. Informational Artifacts

Normative specifications define required implementation behavior.
`AGCP-Conformance-Traceability-and-Automation-Model.md` is normative only
for conformance-artifact relationship semantics and does not create new
implementation obligations.

Informational and executable artifacts explain, summarize, map, or
execute the normative model without creating new requirements.

Machine-readable artifacts support automation but do not supersede the
normative specifications.

------------------------------------------------------------------------

# Repository Versioning

This directory follows repository-release versioning.

Individual artifacts generally do not embed specification version
numbers unless required for interoperability.

------------------------------------------------------------------------

# Future Evolution

Future repository releases may expand the conformance suite with
additional Harness Checks, Test Vectors, or execution capabilities while
preserving the controlled CR ↔ Core-derived NS ↔ TC traceability relationship maintained by the RTM, without altering normative precedence.
