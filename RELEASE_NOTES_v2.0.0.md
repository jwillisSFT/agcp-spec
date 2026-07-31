# AGCP v2.0.0 Release Notes

**Release:** AGCP v2.0.0  
**Status:** Public Review — Controlled Baseline  
**Controlled baseline date:** 2026-07-30  
**Release-notes date:** 2026-07-31  
**Comparison source:** attached `agcp-spec-v.1.0.0.zip` archive  
**Compared v2 source:** F-17-corrected controlled repository

---

## 1. Release Summary

AGCP v2.0.0 is a major, intentionally breaking revision of the Artificial Intelligence Governance Control Plane specification ecosystem.

The release moves from the earlier action-centric, ledger-dominant model to a proposal-centric runtime-governance architecture in which:

- a structured Governed Action Proposal is qualified before governance evaluation;
- Canonical State is resolved from qualified authoritative governance sources rather than assumed to originate exclusively from recorded history;
- authority and final admissibility are re-derived immediately before commitment;
- Governance Realization coordinates state, evidence, authority, binding, resulting-state, and enforcement checks;
- a Policy Enforcement Point applies the decision at or immediately adjacent to the Commit Boundary;
- Governance Evidence, receipts, refusal records, and ordered Governance Ledger events make governance outcomes attributable and replayable;
- Continuation Integrity governs nonterminal proposals before commitment;
- governance compilation and controlled activation are explicit architectural and conformance concerns; and
- requirements, architecture, normative statements, implementation artifacts, tests, and executable automation are connected through a controlled traceability model.

AGCP v2.0.0 is not a drop-in replacement for the attached v1 comparison archive. Implementations require interface, schema, lifecycle, evidence, and conformance migration.

---

## 2. Comparison Basis

The attached comparison archive is named `agcp-spec-v.1.0.0.zip`. Its internal root README identifies the content as **v0.9.0 Public Review**, while its changelog also refers to a later **v1.0.3** release. These release notes therefore use the attached archive contents as the authoritative comparison input and refer to it as the **attached v1 comparison archive**, without attempting to resolve that internal labeling discrepancy.

The repository-level comparison, including this release-notes file, is:

| Measure | Attached v1 comparison archive | AGCP v2.0.0 repository |
|---|---:|---:|
| Total files | 59 | 267 |
| Files added in v2 | — | 230 |
| Files removed from the v1 layout | — | 22 |
| Common files materially modified | — | 35 |
| Common files unchanged | — | 2 |
| HTTP operations | 4 | 10 |
| OpenAPI component schemas | 14 | 96 |
| Root schema JSON files | 18 | 96, including schemas and validation records |
| Active cataloged DS schemas | Not cataloged | 43 |
| Retired DS identifiers | Not cataloged | 1 (`DS-016`) |
| Harness Test Vectors | 16 | 54 |
| Formal Test Cases | Not published as a controlled TC set | 122 |
| Harness Checks | Not published as a controlled registry | 17 |
| Controlled fixtures | Not published as a synchronized catalog | 29 |

Only `.github/CODEOWNERS` and `implementer/AGCP-Implementation-Decision-Record-Template.md` are byte-for-byte unchanged between the two repositories.

---

## 3. Compatibility and Upgrade Classification

AGCP v2.0.0 is a **MAJOR-version migration**.

### 3.1 No v1 HTTP compatibility surface

The active interface namespace is:

```text
/agcp/v2
```

No `/agcp/v1` compatibility paths are included in IF-001. A legacy adapter, if required, must sit outside the v2 normative interface and translate old requests into valid v2 objects and operations.

### 3.2 No schema compatibility aliases

The v2 schema package is a clean controlled set. Transitional compatibility aliases are not retained. In particular:

- the former flattened action submission representation is replaced by the DS-013 transport wrapper containing DS-021;
- the former Human Review Artifact identifier `DS-016` is retired;
- DS-026 Governance Approval Artifact is the sole active approval and adjudication representation; and
- obsolete top-level compatibility metadata in DS-013 is rejected.

### 3.3 Cross-major interoperability

Cross-major interoperability is not guaranteed. Clients and servers must negotiate or reject unsupported major versions in accordance with the v2 versioning and error model.

---

## 4. Controlled Normative and Traceability Baseline

The attached v1 comparison archive did not contain a controlled CR catalog, Architecture Reference Model, extracted Normative Statements collection, or authoritative RTM workbook. AGCP v2.0.0 introduces a complete controlled engineering baseline:

| Controlled artifact | AGCP v2.0.0 state |
|---|---|
| Runtime Governance Conformance Requirements | `CR-001` through `CR-122` |
| Core Specification | Normative runtime behavior in `spec/AGCP-Core.docx` |
| Architecture Reference Model | 90 ARM identifiers and domain anchors |
| Normative Statements | 358 Core-derived atomic statements |
| Requirements Traceability Matrix | `RTM-1.45` |
| Schema Catalog | Version `1.0.44` |
| Active schemas | 43 (`DS-001` through `DS-044`, excluding retired `DS-016`) |
| Interface Catalog | 2 active interfaces: IF-001 and IF-002 |
| Registry Entry Catalog | 92 controlled entries |
| Formal Test Cases | 122 |
| Harness Checks | 17 |
| Harness Test Vectors | 54 |
| Controlled fixtures | 29 |

### 4.1 Normative precedence

AGCP v2.0.0 establishes the following order where normative interpretation must be resolved:

1. Published Runtime Governance Conformance Requirements
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile
4. Implementation Profiles
5. AGCP Conformance Test Suite
6. Reference Implementations

The ARM governs architectural terminology and concept meaning but does not independently create conformance obligations. Normative Statement identifiers are Core-derived extraction and traceability artifacts. The RTM is the authoritative traceability artifact. Neither traceability nor executable automation reverses the CR-first normative precedence model.

### 4.2 Traceability model

The controlled relationship is:

```text
CR <-> Core-derived NS identifiers <-> Formal TC
                              |
                              +-> Harness Checks -> Test Vectors -> execution evidence
```

Formal Test Cases remain the authoritative assessment procedures. Harness results provide objective evidence but do not independently establish conformance.

---

## 5. Major Architecture Changes

### 5.1 Action-centric submission replaced by proposal-centric governance

The v1 `ActionEnvelope` model is replaced by a layered representation:

- **DS-013 Proposal Submit Request** — transport wrapper;
- **DS-021 Governed Action Proposal** — canonical proposal domain object;
- **DS-022 Governance Context Envelope** — attributable governance context and lineage; and
- **Proposal Identity** — stable identity for retry, replay, lifecycle, authorization binding, and duplicate-effect prevention.

A proposal declares intent, target, requested effect, action representation, validity, identity, tenant, Governance Domain, context, and provenance. Submission is not execution and does not confer authority at commitment.

### 5.2 Canonical State source-resolution model

The earlier repository emphasized lifecycle and authorization derivation from the append-only ledger. In v2:

- Canonical State is resolved from one or more qualified authoritative governance sources;
- state is qualified for freshness, provenance, completeness, consistency, integrity, availability, and ordering suitability;
- the ordered Governance Ledger is authoritative for recorded governance events, event ordering, and Derived Lifecycle State;
- the ledger need not originate every governance-relevant fact; and
- replay reproduces Canonical State resolution from recorded qualified source versions and applicable ordered ledger records.

This removes the implication that all Canonical State is reconstructed exclusively from ledger history.

### 5.3 Commit-Bound Admissibility and Governance Realization

V2 separates earlier authorization from final authority and admissibility at commitment.

Immediately before commitment, Governance Realization coordinates:

- Canonical State Resolution;
- State Qualification;
- Evidence Qualification;
- Authority Re-Derivation;
- Governance Binding Validation;
- Resulting-State Validation;
- Commit-Bound Admissibility;
- Enforcement Context generation; and
- Policy Enforcement Point enforcement.

Prior authorization, approval, identity, delegation, or standing permission may contribute evidence but does not by itself constitute authority at commitment or permission to execute.

### 5.4 Governance Enforcement Binding

The enforced decision must remain bound to the same proposal, target, tenant, Governance Domain, authorization, evidence, policy, Canonical State basis, scope, lifecycle state, validity window, Governance Version, and bind conditions evaluated by governance.

V2 explicitly prevents substitution, detachment, stale reuse, cross-tenant transfer, and enforcement bypass.

### 5.5 Governance Evidence and refusal semantics

Governance Evidence becomes a cross-cutting mandatory service rather than a limited audit output.

V2 adds or formalizes:

- Governance Receipts for non-refusal outcomes;
- Refusal Records for Structural Refusal;
- evidence qualification and continuity;
- provenance chains;
- deterministic replay of governance interpretation without re-executing the historical action;
- cryptographic attribution and integrity; and
- Governance Ledger event coverage for submissions, decisions, approvals, refusals, commitments, enforcement outcomes, lifecycle transitions, continuation events, and evidence references.

Governance-significant artifact-validation failures must produce Governance Evidence where the implementation has sufficient attribution context.

### 5.6 Lifecycle and Continuation Integrity

The v1 action-state documents are replaced by a governance-progression model.

V2 distinguishes:

- governance lifecycle state from transient internal processing state;
- Pending Human Review as a controlled governance outcome;
- approval artifacts from executable authority;
- nonterminal continuation from post-commit operational control;
- Degraded State, admissible-path viability, recovery, expiration, cancellation, and supersession; and
- risk-based re-evaluation of affected nonterminal proposals.

Continuation Integrity applies before commitment and ends at successful commitment or another governed terminal disposition.

### 5.7 Composite governance and deterministic adjudication

V2 introduces explicit support for:

- composite proposals;
- Bind Sets;
- Governance Dependency Graphs;
- weakly and strongly coupled sub-transitions;
- Partial-Bind Admissibility;
- aggregate Resulting-State Validation;
- Admissible Sets; and
- Deterministic Adjudication when multiple admissible transitions contend.

### 5.8 Governance compilation and controlled activation

Governance configuration is no longer treated only as static policy input. V2 defines:

- Governance Configuration;
- deterministic Governance Compilation;
- Compiled Governance Artifacts;
- Governance Versions;
- Constitutional Validation;
- Governance Omission Analysis;
- Governance Self-Protection and self-modification isolation;
- atomic Controlled Governance Activation;
- prior-version preservation; and
- governed rollback with evidence and lineage.

### 5.9 Tenant and Governance Domain isolation

V2 expands tenant isolation into explicit tenant and Governance Domain semantics throughout proposals, state, evidence, authority, artifacts, retrieval, evaluation, and commitment. Cross-domain authority is governed, bounded, and attributable rather than implied by identity or transport context.

---

## 6. HTTP Interface Migration

### 6.1 Replaced operations

| Attached v1 operation | AGCP v2.0.0 operation | Migration impact |
|---|---|---|
| `POST /agcp/v1/actions/submit` (`submitAction`) | `POST /agcp/v2/proposals/submit` (`submitProposal`) | Replace ActionEnvelope payload with DS-013 wrapper and DS-021 proposal. |
| `GET /agcp/v1/actions/{action_id}` (`getAction`) | `GET /agcp/v2/proposals/{proposal_id}` (`getProposal`) | Use Proposal Identity and mandatory tenant/Governance-Domain query scope. |
| `POST /agcp/v1/actions/{action_id}/cosign` (`cosignAction`) | `POST /agcp/v2/proposals/{proposal_id}/governance-approvals` (`submitGovernanceApproval`) | Replace cosign token semantics with DS-026 Governance Approval Artifact submission. |
| `POST /agcp/v1/executions/commit` (`commitExecution`) | `POST /agcp/v2/commit-boundary/commit` (`commitBoundaryProcessing`) | Supply complete commit-time authority, qualification, binding, resulting-state, enforcement, and integrity references. |

### 6.2 New mandatory operations

V2 adds six operations that had no equivalent in the attached v1 contract:

- `GET /agcp/v2/meta`
- `GET /agcp/v2/execution-authorizations/{authorization_id}`
- `GET /agcp/v2/governance-evidence/{evidence_id}`
- `POST /agcp/v2/governance-artifacts/policy-modules`
- `POST /agcp/v2/governance-artifacts/policies`
- `GET /agcp/v2/governance-artifacts/{artifact_id}`

All ten IF-001 operations have schema-valid positive executable coverage, with applicable negative, isolation, and idempotency scenarios.

### 6.3 Required request scope

V2 makes tenant and Governance Domain scope explicit:

- proposal, authorization, evidence, and artifact retrieval require `tenant_id` and `governance_domain_id` query parameters;
- approval, commit, policy-module registration, and policy registration require `Idempotency-Key`; and
- idempotency is scoped to the endpoint and the tenant represented by the canonical request body.

Authenticated identity, a path identifier, or another request context may not silently replace the declared tenant and Governance Domain scope.

### 6.4 Error model

The v2 normative Error Mapping, OpenAPI response sets, rejection-code registry, YAML vectors, and Markdown vector mirror are synchronized.

Notable additions include:

- HTTP 422 for semantic validation and qualification failures;
- HTTP 503 for unavailable governance dependencies;
- `RESOURCE_NOT_FOUND` for hidden 404 outcomes;
- operation-specific 404 support under the selected cross-scope disclosure strategy; and
- evidence generation for attributable governance-significant failures.

---

## 7. Schema and Data-Model Migration

### 7.1 Cataloged schema architecture

V2 introduces a controlled Schema Catalog with stable DS identifiers, canonical URIs, lifecycle state, hashes, forward dependencies, reverse dependencies, RTM mappings, CR mappings, and validation records.

The active catalog contains 43 schemas across these domains:

- common infrastructure;
- governance artifacts;
- evaluation results;
- governance workflow;
- canonical governance objects;
- authority and delegation;
- approval and adjudication;
- evidence and provenance;
- commit and enforcement;
- qualification;
- composite governance;
- lifecycle and continuation;
- governance compilation; and
- registry validation.

### 7.2 Key v1-to-v2 representation changes

| Attached v1 schema | V2 replacement or successor |
|---|---|
| `action_envelope.json` | DS-013 `proposal_submit_request.json` plus DS-021 `governed_action_proposal.json` and DS-022 `governance_context_envelope.json` |
| `action_status_response.json` | DS-014 Proposal View, DS-017 Execution Authorization View, and DS-038 Governance Lifecycle Record, as applicable |
| `cosign_token.json` | DS-026 Governance Approval Artifact |
| `execution_commit_request.json` | DS-018 Commit Boundary Request |
| `execution_commit_result.json` | DS-019 Commit Boundary Result |
| `ledger_entry.json` | DS-040 Governance Ledger Event |
| `policy_module.json` | DS-005 Policy Evaluation Module Artifact |
| `validation_result.json` | Specialized constraint, invariant, state, evidence, authority, binding, and resulting-state result schemas |

The v1 `policy_artifact.json`, constraint, invariant, exception, tenant, error, and common schemas remain recognizable in purpose but are materially expanded and cataloged under v2 DS identifiers.

### 7.3 Human review representation retirement

`DS-016 Human Review Artifact` is permanently retired and may not be reused. `DS-026 Governance Approval Artifact` is the sole active representation for approval, adjudication, cosignature, quorum participation, risk acceptance, cancellation, withdrawal, and related governed decisions.

`Pending Human Review` remains a governance outcome; it is not an active artifact type.

### 7.4 Canonical schema URIs and release versioning

V2 schemas use the `https://agcp.ai/schemas/` canonical namespace and repository-release governance rather than embedding the old `0.9.0` schema identity pattern throughout payloads.

---

## 8. Conformance Model Changes

### 8.1 Profile names and meanings

The cumulative L1-L5 model remains, but two names and several obligations are materially revised:

| Level | Attached v1 name | AGCP v2.0.0 name |
|---|---|---|
| L1 | Schema & Envelope Validation | Schema & Envelope Validation |
| L2 | Ordered Validation Pipeline | Ordered Governance Mediation |
| L3 | Deterministic Governance | Deterministic Governance |
| L4 | HITL & Execution Gating | Execution Authorization Control |
| L5 | Multitenant Isolation | Multitenant Governance Isolation |

Implementations must update conformance declarations to use the v2 names and satisfy the expanded governance semantics.

### 8.2 Formal assessment and executable support

The earlier assertion-oriented conformance package is replaced by:

- 122 Formal Test Cases mapped to CR-001 through CR-122;
- 17 MUST Harness Checks;
- 54 synchronized Harness Test Vectors;
- 29 controlled schema fixtures;
- complete TC-to-check and TC-to-vector mappings or explicit no-dedicated-vector dispositions; and
- controlled validation records for request parameters, response sets, error mappings, fixtures, IF-001 coverage, compilation/activation coverage, and mapping completeness.

The former `AGCP-Assertion-Registry.md` and `assertions.json` are no longer the governing conformance structure.

### 8.3 New executable coverage

V2 executable coverage includes:

- all ten mandatory IF-001 operations;
- proposal qualification and governance outcomes;
- governance approval and quorum behavior;
- commit-time authority, binding, and refusal;
- tenant and Governance Domain isolation;
- Governance Evidence retrieval;
- governance-artifact registration and retrieval;
- idempotency replay and conflict behavior;
- governance configuration and deterministic compilation;
- Constitutional Validation and omission analysis;
- self-modification refusal;
- atomic activation and injected activation failure; and
- governed rollback with evidence and lineage.

---

## 9. Specification and Repository Packaging Changes

### 9.1 New authoritative engineering documents

V2 adds:

- Architecture Reference Model;
- Runtime Governance Conformance Requirements catalog;
- extracted Normative Statements;
- Requirements Traceability Framework;
- RTM Specification;
- authoritative RTM workbook;
- Interface Catalog;
- Schema Catalog;
- Registry Entry Catalog;
- formal Conformance Test Suite; and
- Conformance Traceability and Automation Model.

### 9.2 Lifecycle package reorganization

The former action lifecycle diagram, normative state-transition table, and transition implementer annex are replaced by:

- `AGCP Governance Lifecycle Model.md`;
- `AGCP Normative Governance Progression Table.md`; and
- `AGCP Governance Progression Implementation Guide.md`.

The obsolete `transitions/` directory is removed.

### 9.3 Reference and research material

The HTTP reference pseudocode is renamed and expanded as `AGCP-HTTP-Reference-Implementation-Pseudocode.md`.

A `research/` package is added for supporting papers and terminology references. Research publications are informative unless expressly adopted by a normative source. The current v2.0.0 research package intentionally includes `Runtime Governance Body of Knowledge - Glossary - DRAFT For Discussion Purposes Only.pdf` in place of the earlier `AI Runtime Governance - Vocabulary – Walkthrough Style - v.1.3.pdf` reference.

### 9.4 Licensing and patent notice

The documentation remains licensed under CC BY 4.0. The license file is simplified, and the patent disclosure is moved into the separate root `NOTICE.md`.

---

## 10. Removed or Replaced v1 Files

The following files from the attached v1 comparison archive do not appear under the same path in v2:

| Removed v1 path | V2 disposition |
|---|---|
| `conformance/AGCP-Assertion-Registry.md` | Replaced by Formal TCs, Harness Check Registry, Test Matrix, and traceability/automation model. |
| `conformance/assertions.json` | Replaced by `harness-checks.json`, Formal TC mappings, and controlled validation records. |
| `lifecycle/AGCP-Action-Lifecycle-State-Diagram.md` | Replaced by Governance Lifecycle Model and progression documents. |
| `lifecycle/AGCP-Normative-State-Transition-Table.md` | Replaced by Normative Governance Progression Table. |
| `lifecycle/AGCP-Transition-Implementer-Annex.md` | Replaced by Governance Progression Implementation Guide. |
| `reference/AGCP-HTTP-Reference-Pseudocode.md` | Replaced by `AGCP-HTTP-Reference-Implementation-Pseudocode.md`. |
| `schemas/action_envelope.json` | Replaced by DS-013, DS-021, and DS-022. |
| `schemas/action_status_response.json` | Replaced by specialized proposal, authorization, and lifecycle views. |
| `schemas/cosign_token.json` | Replaced by DS-026 Governance Approval Artifact. |
| `schemas/execution_commit_request.json` | Replaced by DS-018 Commit Boundary Request. |
| `schemas/execution_commit_result.json` | Replaced by DS-019 Commit Boundary Result. |
| `schemas/ledger_entry.json` | Replaced by DS-040 Governance Ledger Event. |
| `schemas/policy_module.json` | Replaced by DS-005 Policy Evaluation Module Artifact. |
| `schemas/validation_result.json` | Replaced by specialized v2 evaluation and qualification result schemas. |
| `spec/AGCP-Core.md` | Replaced by controlled `AGCP-Core.docx`. |
| `spec/AGCP-HITL-Token.md` | Replaced by Human Review Specification and DS-026 approval artifacts. |
| `spec/AGCP-HTTP-Interface.md` | Replaced by HTTP Interface Specification and IF-001 OpenAPI contract. |
| `spec/AGCP-Multitenant-Operational-Profile.md` | Replaced by Multitenant Operational Specification. |
| `spec/AGCP-Provenance-Wire-Format.md` | Replaced by Provenance Wire Format Specification. |
| `spec/AGCP-Security-Profile.md` | Standalone file not retained; applicable security and integrity obligations are distributed across the Core, companion specifications, schemas, registries, and conformance assets. |
| `spec/ledger/AGCP-Ledger-Storage-Contract.md` | Replaced by Append-Only Governance Ledger Specification. |
| `transitions/README.md` | Directory retired; lifecycle documentation is consolidated under `lifecycle/`. |

---

## 11. Migration Checklist for Implementers

1. **Treat the upgrade as cross-major.** Do not send v1 requests directly to IF-001.
2. **Regenerate HTTP clients and validators** from `api/AGCP-HTTP-Contract.yaml`.
3. **Replace ActionEnvelope submission** with DS-013 containing a complete DS-021 proposal.
4. **Create and preserve Proposal Identity** independently of transport retries and action execution.
5. **Populate tenant and Governance Domain scope** in canonical objects and required retrieval query parameters.
6. **Replace cosign-token/HITL artifact handling** with DS-026 Governance Approval Artifacts and the governance-approval endpoint.
7. **Implement current-source Canonical State resolution** and record the qualified source versions needed for replay.
8. **Implement State Qualification, Evidence Qualification, and Authority Re-Derivation** before commitment.
9. **Implement Governance Binding Validation and Resulting-State Validation** for every governed commitment.
10. **Place an authoritative Policy Enforcement Point** at or immediately adjacent to every governed consequence within the claimed enforcement scope.
11. **Replace v1 commit payloads** with DS-018 and produce DS-019 outcomes.
12. **Replace ledger-entry handling** with ordered DS-040 Governance Ledger Events and Derived Lifecycle State semantics.
13. **Generate Governance Receipts or Refusal Records** and preserve Governance Evidence throughout applicable processing.
14. **Implement Continuation Integrity** for nonterminal proposals and risk-based re-evaluation where material conditions change.
15. **Add governance-artifact registration and retrieval** for policy modules and policies.
16. **Implement endpoint-and-tenant-scoped idempotency** and return the v2 normative conflict behavior.
17. **Adopt the active Schema and Registry catalogs** rather than relying on v1 filenames or embedded version assumptions.
18. **Update conformance declarations** to the v2 profile names.
19. **Run the 122 Formal Test Cases** and use Harness Checks/Test Vectors as supporting executable evidence.
20. **Document any legacy translation layer** as non-normative implementation infrastructure outside the v2 interface contract.

---

## 12. Known Baseline Dispositions

### 12.1 Proposed companion specifications

The RTM contains 55 references across 47 rows to ten proposed or expanded companion paths. Each is explicitly classified as **Planned / Non-Baseline** and is not required for AGCP v2.0.0 conformance:

- `spec/AGCP-Continuation-Integrity.md`
- `spec/AGCP-Audit-Model.md`
- `spec/AGCP-State-Qualification.md`
- `spec/AGCP-Action-Representation.md`
- `spec/AGCP-Governance-Compilation-Interface.md`
- `spec/AGCP-Composite-Governance.md`
- `spec/AGCP-Enforcement-Model.md`
- `spec/AGCP-Governance-Context.md`
- `spec/AGCP-Evidence-Qualification.md`
- `spec/AGCP-Delegation-Model.md`

Their absence does not make accepted RTM rows incomplete.

### 12.2 Public-review status

This is a controlled Public Review baseline. Review feedback does not modify the baseline unless incorporated into a later versioned revision and recorded in the changelog.

### 12.3 Specification repository only

The repository contains specifications, schemas, traceability, tests, evidence definitions, validation records, and supporting publications. It does not contain a production AGCP implementation, deployment artifacts, operational keys, or customer-specific configuration.

---

## 13. Baseline Hardening Completed Before Release Notes

The F-17-controlled repository incorporates the following audit closures:

- mandatory IF-001 parameters added to all affected harness requests;
- schema-valid Governance Approval setup and semantic cryptographic-failure testing;
- harness rejection codes and HTTP statuses synchronized with the normative error model;
- hidden 404 outcomes declared by OpenAPI;
- complete OpenAPI/Error Mapping response-set parity;
- complete human-readable Interface Specification/OpenAPI parity;
- executable coverage for all ten mandatory IF-001 operations;
- substantive executable vectors for Governance Compilation and Controlled Activation;
- mandatory Continuation Integrity and commit controls preserved in downstream restatements;
- mandatory Governance Evidence language preserved in Error Mapping;
- Markdown fence structure repaired in the normative Conformance Specification;
- active validation records aligned to RTM-1.45;
- schema-specific validation JSON records placed under `schemas/`, with catalog metadata and catalog validation retained under `schemas/catalog/`;
- retired Human Review Artifact terminology removed from active representations;
- traceability wording separated from normative precedence;
- Canonical State resolution terminology corrected; and
- all proposed Companion_Spec references explicitly dispositioned as non-baseline.

---

## 14. Validation Summary

The controlled v2 repository used for these notes passed the following consistency checks before release-note integration:

- all JSON and YAML control files parsed without duplicate-key failures;
- all 43 active schemas passed Draft 2020-12 metaschema validation;
- `schemas/common.json` contained 62 reachable shared definitions, with no unused definitions and no obsolete `pass_fail_enum`;
- Schema Catalog hashes and forward/reverse dependencies were synchronized;
- all OpenAPI references resolved;
- Interface Specification and OpenAPI method/path/operationId, required-parameter, request-schema, and response-set parity passed for all ten operations;
- Error Mapping and OpenAPI non-success response-set parity passed;
- all HTTP primary and setup requests supplied mandatory parameters;
- every expected vector status was declared by the matched operation;
- every MUST Harness Check had substantive executable coverage;
- all 29 controlled fixtures validated against their assigned schemas;
- all 122 Formal Test Cases had complete Harness Check mappings and vector mappings or explicit controlled dispositions;
- no Harness Check or Test Vector was unreferenced; and
- the internal ZIP passed duplicate-entry, CRC-integrity, and fresh-extraction byte comparison checks.

---

## 15. Recommended Review Path

1. [`spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv`](spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv)
2. [`spec/AGCP-Core.docx`](spec/AGCP-Core.docx)
3. [`spec/Architecture Reference Model.docx`](spec/Architecture%20Reference%20Model.docx)
4. [`spec/AGCP Normative Statements.docx`](spec/AGCP%20Normative%20Statements.docx)
5. [`spec/AGCP_Requirements_Traceability_Matrix_(RTM).xlsx`](spec/AGCP_Requirements_Traceability_Matrix_%28RTM%29.xlsx)
6. [`spec/AGCP-HTTP-Interface-Specification.md`](spec/AGCP-HTTP-Interface-Specification.md)
7. [`api/AGCP-HTTP-Contract.yaml`](api/AGCP-HTTP-Contract.yaml)
8. [`schemas/SCHEMA-CATALOG.md`](schemas/SCHEMA-CATALOG.md)
9. [`conformance/AGCP-Conformance-Traceability-and-Automation-Model.md`](conformance/AGCP-Conformance-Traceability-and-Automation-Model.md)
10. [`conformance/AGCP-Conformance.md`](conformance/AGCP-Conformance.md)
11. [`conformance/Conformance Test Suite.md`](conformance/Conformance%20Test%20Suite.md)
12. [`conformance/AGCP-Test-Matrix.md`](conformance/AGCP-Test-Matrix.md)
13. [`governance/CHANGELOG.md`](governance/CHANGELOG.md)

---

## 16. Attribution and Notices

AGCP documentation is licensed under CC BY 4.0. See [`LICENSE`](LICENSE).

Patent and implementation-rights disclosures are provided in [`NOTICE.md`](NOTICE.md).
