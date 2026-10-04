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

## Test and Injection Point Development Status

The conformance test-control, fixture-injection, and Governance Observation Point inventory is under active development. The IF-005 controls, fixture types, observation points, mappings, and related harness capabilities currently enumerated in this directory represent the capabilities identified to date and are not a declaration that every useful test or injection point has already been identified, frozen, or implemented.

Additional controls or observation points may be identified as the reference implementation, negative-test corpus, integration testing, and Formal Test Case automation mature. Some enumerated capabilities may also be only partially implemented by a particular reference implementation until the corresponding source-code adapters, hooks, isolation mechanisms, and evidence paths are completed and qualified.

The specifications define the external semantics, scope, isolation, and prohibited outcome-injection behavior for standardized controls. The exact internal source-code hooks used to realize those controls are implementation details and may evolve while preserving the specified externally observable behavior.

The conformance mapping files may therefore identify planned control or observation capabilities before reference-implementation support is complete. Such entries are development targets until validated by the corresponding implementation and objective conformance evidence. A Formal Test Case remains authoritative for the required assessment; successful setup, fixture injection, observation, or management actuation does not independently constitute a Test Case Pass.

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

  AGCP-Test-Mapping.md                  Human-readable informational mirror of
                                        test-mapping.json for TC-001 through
                                        TC-122.

  agcp-conformance-manifest.yml         Index of the conformance package
                                        and execution metadata.

  tests/                                Controlled Formal Test Case batch
                                        documents for TC-001 through TC-122.
  -----------------------------------------------------------------------

------------------------------------------------------------------------


## v2.1.x Test Mapping Regeneration Status

`test-mapping.json` has been completely regenerated for `TC-001` through `TC-122` and synchronized to 21 Harness Checks and 135 Harness Test Vectors. The downstream test-control mapping, Harness Vector/Check synchronization, and aggregate conformance-layer validation steps are complete. Final RTM synchronization is complete at `RTM-1.47`.

## v2.1.x Aggregate Conformance-Layer Validation Status

The synchronized Formal Test Cases, Test Matrix, test mappings, test-control mappings, 21 Harness Checks, 135 Harness Test Vectors, controlled fixtures, DS-050 control vocabulary, and DS-046 Governance Observation Point vocabulary have passed aggregate pre-RTM validation. The validation also corrected a stale machine-readable Harness Check count and removed obsolete semantic-fixture assumptions that DS-018 carries GRF-derived authority/evidence or DS-029 Enforcement Context. See `AGCP-v2.1.x-AGGREGATE-CONFORMANCE-LAYER-VALIDATION.md` and `AGCP-v2.1.x-aggregate-conformance-layer-validation.json`. Final RTM synchronization is complete at `RTM-1.47`.

## v2.1.x Test-Control Mapping Regeneration Status

`test-control-mapping.json` and `AGCP-Test-Control-Mapping.md` have been completely regenerated for `TC-001` through `TC-122`. All standardized control references validate against DS-050 and all Governance Observation Point references validate against DS-046. The mapping explicitly distinguishes standardized control recommendations from implementation-specific or future-standardization harness injection needs. Those needs are represented in the synchronized Harness Vector/Check layer without claiming universal implementation support. Aggregate conformance-layer validation has passed.

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

`fixture-mapping.json` maps every conformance example to its exact active DS schema and expected validation result. The examples are maintained in `../schemas/examples/`. The 36 controlled fixtures include the existing governance, ledger, approval, commit, and registry examples plus the DS-052 Governed Execution Outcome and DS-053 Identity and Authorization Qualification Result fixtures added for v2.1.x harness synchronization.

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

The synchronized v2.1.x change set is closed at `RTM-1.47`. The full overlaid repository state used for closure validation is indexed by `../governance/AGCP-v2.1.x-repository-closure-manifest.json` and validated by `../governance/AGCP-v2.1.x-repository-closure-validation.json`. The currently published baseline remains v2.1.0 until a separate controlled release designation is made.


## Repository-wide integrity gate

## v2.1.0 observation and test control

`test-control-mapping.json` maps all controlled Formal TCs to recommended IF-003 observations, optional IF-005 precondition controls, or explicit external dependencies. The mapping is an execution aid only; the Formal TC remains authoritative. Successful setup or actuation never constitutes a TC Pass.


- [AGCP Management Plane Harness Spec](AGCP-Management-Plane-Harness-Spec.yml) — supporting executable checks for runtime binding, actuation realization, test-scope isolation, and consumption evidence.
## v2.1.0 server implementation closure aids

- `AGCP-Management-Plane-Harness-Spec.yml` provides supporting checks for truthful GOP/GAP/Test-Control runtime coupling, including the omission-safe optional `correlation_id` case.
- `AGCP-v2.1.0-Executable-Regression-Requirements.json` is the machine-readable known-defect regression matrix intended for server implementation and pre-conformance CI. It does not create new CRs or replace Formal Test Cases.
- `../reference/AGCP-v2.1.0-Server-Implementation-Blueprint.md` gives concrete server module boundaries, authoritative-source resolution, Commit Boundary processing order, atomic lifecycle persistence, generated-artifact validation, test-control adapter design, and Rust-oriented implementation notes.



## v2.1.x Conformance Closure Status

The conformance synchronization sequence is complete: 122 Formal Test Cases, the regenerated Test Matrix, 122 test mappings, 122 test-control mappings, 21 Harness Checks, 135 Harness Test Vectors, 36 controlled fixtures, and aggregate conformance-layer validation are synchronized to final `RTM-1.47`. This closes the specification/conformance synchronization step; later source-code implementation and runtime evidence do not retroactively redefine the Formal Test Cases.

## Formal Test Case synchronization status

The formal Test Cases under `tests/` are now synchronized to the current v2.1.x Core and Normative Statements. The suite remains `TC-001` through `TC-122`; no `TC-123` is introduced. The synchronization updates 42 TCs at the assertion/traceability level and 22 additional TCs at the regression/scenario level. Final RTM synchronization is complete at `RTM-1.47`. See `AGCP-v2.1.x-FORMAL-TEST-CASE-SYNCHRONIZATION-UPDATE.md`, `v2.1.x-formal-test-sync.json`, and `../spec/AGCP-v2.1.x-RTM-SYNCHRONIZATION-UPDATE.md`.
