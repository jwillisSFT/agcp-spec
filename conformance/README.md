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

## Informative Implementation and Traceability References

- [AGCP v2.0.0 Requirement Traceability Annex](reference/agcp-v2.0.0-requirement-traceability-annex.pdf) — consolidated implementation and validation references for CR-001 through CR-122. Informative; does not alter normative precedence.

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

## Provenance wire-format vectors

Cross-language canonicalization, detached-signature, schema-rejection, protected-header, algorithm, payload-modification, and replay vectors are provided in `provenance/AGCP-Provenance-Wire-Format-Test-Vectors.json`. They are validated by `../governance/validate_provenance_wire_format.py`.


## IF-002 deterministic WASM companion

The controlled Rust Student Service profile companion is specified by `spec/AGCP-WASM-Policy-Evaluation-Machine-Contract.md`. Machine-readable ABI and envelope schemas are under `api/if-002/`, and reusable ABI, import, failure, digest-binding, and replay vectors are under `conformance/if-002/`. These supplement rather than replace the Formal Test Cases.

## Governance Approval command/record separation

P0-06 vectors are under `conformance/command-record/`. They verify DS-045 untrusted ingress and DS-026 authoritative-record separation.

## Algorithm-explicit content digest vectors

P1-12 vectors are under `conformance/digests/`. They verify exact SHA-256, SHA-384, SHA-512, BLAKE2B-256, and BLAKE2B-512 output lengths, lowercase hexadecimal, required fields, closed-object behavior, and rejection of ambiguous or inconsistent digest representations. They are validated by `../governance/validate_content_digest_contract.py`.

## IF-001 Error and Metadata Vectors

`conformance/http/AGCP-HTTP-Error-Metadata-Test-Vectors.json` verifies P1-03, P1-09, P1-14, and P1-17 across public 404 normalization, 429/Retry-After, 503 capacity, transport-vs-governance separation, and integrity-bound metadata advertisements.

## Semantic fixture validation

The controlled positive-fixture catalog is subject to both JSON Schema validation and semantic equality validation. The semantic validator checks declared bindings for Tenant, Governance Domain, Proposal, target, policy, approval, evidence, authorization, lifecycle state, and Canonical State.

- Positive fixture rules and mismatch vectors: `conformance/semantic-fixtures/AGCP-Semantic-Fixture-Test-Vectors.json`
- Claimant-assertion negatives: `conformance/command-record/AGCP-Governance-Approval-Command-Record-Test-Vectors.json`
- Validator: `governance/validate_semantic_fixtures.py`
- Controlled result: `governance/AGCP-semantic-fixture-validation.json`


## Repository Synchronization

The cumulative v2.0.1 correction set is indexed by `../governance/AGCP-v2.0.1-repository-synchronization-manifest.json` and validated by `../governance/validate_repository_synchronization.py` against `RTM-1.46` and the current catalogs.


## Repository-wide integrity gate

The final accumulated correction-set gate is `governance/validate_repository_integrity.py`. Its controlled report is `governance/AGCP-v2.0.1-repository-integrity-validation.json`, and its CI workflow is `.github/workflows/validate-repository-integrity.yml`. The public correction summary is `AGCP-v2.0.1-CORRECTION-SUMMARY.md`. This gate aggregates the finding-specific validators and repository synchronization controls; it does not establish implementation conformance.
