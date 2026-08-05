# AGCP Conformance Fixture, Mapping, and Example Synchronization

**Applicable AGCP release:** v2.0.0
**Interface:** IF-001 v2 (`/agcp/v2`)
**Schema Catalog:** 1.0.50
**RTM dataset:** RTM-1.46
**Date:** 2026-08-03

## 1. Purpose

This update synchronizes the conformance harness, reference implementation, test mapping, Harness Check Registry, and canonical examples with the completed AGCP v2.0 schema and interface migrations.

## 2. Conformance harness corrections

The harness now:

- uses `/agcp/v2` for every HTTP operation;
- contains no `/human-review` operation or DS-016 compatibility property;
- uses Governance Approval Artifact fixtures from DS-026;
- resolves DS-018 Commit Boundary request fixtures before request validation;
- supplies canonical Enforcement Context rather than transitional commit-request content;
- identifies IF-001 and the v2 interface namespace explicitly; and
- validates the complete fixture catalog before executing HTTP scenarios.

## 3. Canonical fixture catalog

`conformance/fixture-mapping.json` maps 29 valid examples to exact active schema paths. The fixture set covers:

- DS-011 Governance Constraint Evaluation;
- DS-012 Governance Invariant Evaluation;
- DS-018 Commit Boundary Request;
- DS-019 Commit Boundary Result;
- DS-026 Governance Approval Artifact and quorum accumulation;
- DS-029 Enforcement Context;
- DS-032 State Qualification Result;
- DS-033 Evidence Qualification Result;
- DS-038 Governance Lifecycle Record;
- DS-039 Continuation Integrity Result;
- DS-040 Governance Ledger Event;
- DS-041 Governance Configuration;
- DS-042 Compiled Governance Artifact;
- DS-043 Controlled Governance Activation; and
- DS-044 Registry Document.

The DS-044 example is synthetic and informative. The three authoritative registry payloads remain exclusively under `registries/`.

## 4. Test mapping synchronization

`conformance/test-mapping.json` derives NS, CR, TC, DS, schema-file, IF, REG, and fixture mappings from RTM-1.46 and now extends each TC record to the executable conformance layer. Each of the 122 TC records identifies:

- current NS and CR identifiers;
- current DS identifiers and exact active schema repository paths;
- applicable IF and REG identifiers;
- relevant validated fixture files;
- one or more applicable Harness Check identifiers;
- direct Harness Test Vector identifiers where a dedicated executable scenario exists;
- supporting Harness Test Vector identifiers where they provide partial executable coverage; and
- an explicit disposition when no dedicated executable vector exists.

Retired DS-016 is absent from active mappings. All 16 Harness Checks and all 28 current Harness Test Vectors are referenced by the controlled TC mapping.

## 5. Harness Check Registry synchronization

The machine-readable registry now contains 16 checks. It uses exact repository paths and adds explicit checks for:

- qualified governance inputs;
- lifecycle and Continuation Integrity; and
- Governance Configuration, compilation, and controlled activation.

All test-vector references resolve to current harness vector identifiers.

The executable YAML catalog and the human-readable Markdown catalog now contain the same 28 unique vector identifiers. The YAML file is the authoritative executable source, and the Markdown file is its exact human-readable mirror. The Conformance Test Matrix references only identifiers in this synchronized set.

## 6. Reference implementation correction

The Commit Boundary reference flow now validates DS-018, reads Proposal Identity and Execution Authorization from their canonical nested references, verifies qualification, re-derivation, binding, resulting-state, and continuation inputs, and passes DS-029 Enforcement Context to commitment binding.

## 7. Validation summary

The integrated validation passed:

- 44 active Draft 2020-12 schemas metaschema-valid;
- 3,579 cross-schema references and JSON Pointer fragments resolved;
- 29 of 29 schema examples valid;
- four registry documents structurally and cryptographically verified, including the synthetic DS-044 example;
- 28 executable harness vectors parsed and matched to 28 human-readable vector definitions;
- 29 HTTP operations or presteps use `/agcp/v2`;
- 16 Harness Checks reference existing schemas, fixtures, registries, and current test-vector identifiers;
- 122 test mappings match RTM-1.46 and contain valid Harness Check and Test Vector mappings or explicit vector dispositions;
- 142 OpenAPI references resolved;
- 44 active Schema Catalog hashes matched;
- all 44 active Schema Catalog RTM/CR mappings matched the authoritative RTM-1.46 DS assignments;
- all 44 active Schema Catalog reverse dependency lists matched the inverse of the active forward dependency graph;
- RTM-1.46 contains the controlled IF mappings used by the current test mapping; and
- no active runtime compatibility reference to `/agcp/v1`, `/human-review`, DS-016, or the transitional Commit Boundary field remains.

The detailed machine-readable results are in `AGCP-conformance-fixture-synchronization-validation.json`.
## 8. P0-02 provenance synchronization

The fixture and test mappings now reference Schema Catalog 1.0.50. TC-005 explicitly maps DS-001, `schemas/common.json`, IF-001, and the controlled cross-language provenance vector package. All 30 controlled fixtures validate against the synchronized provenance wire schema.

## P0-06 fixture addition

Added `FX-DS045-GOVERNANCE-APPROVAL-SUBMISSION` for the untrusted approval ingress schema. The fixture contains claimant content and provenance only and validates independently from DS-026 authoritative records.

## P1-12 digest synchronization

All controlled fixtures continue to validate after DS-001 began enforcing exact algorithm/output-length and lowercase-hexadecimal digest semantics. Dedicated valid examples and negative vectors are maintained separately under `schemas/examples/` and `conformance/digests/`.

## P0-10 semantic correction - 2026-08-03

Fourteen positive fixtures contained internally inconsistent placeholder identifiers despite passing JSON Schema validation. The fixtures were normalized to the common example namespace (`tenant-1`, `domain-1`, `proposal-1`, `target-1`, `policy-1` version `2.0.0`, and `canonical-state-1` where applicable). The fixture catalog now requires semantic equality validation for those files. Ten intentionally invalid semantic-mismatch vectors and the existing fifteen claimant-assertion vectors are validated separately.
