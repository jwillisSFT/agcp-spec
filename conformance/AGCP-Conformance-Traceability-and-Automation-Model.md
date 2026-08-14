# AGCP Conformance Traceability and Automation Model

**Status:** Normative for conformance-artifact relationship semantics  
**Implementation Behavior:** Does not create or modify AGCP implementation requirements  
**Applies To:** Requirements traceability, Formal Test Cases, Harness Checks, Harness Test Vectors, execution evidence, assessment results, and conformance claims  
**Versioning:** Governed by the AGCP repository release

---

# 1. Purpose

This document defines how AGCP requirements, traceability artifacts, assessment procedures, executable checks, test vectors, and conformance results relate to one another.

It establishes a single relationship model for:

- Runtime Governance Conformance Requirements (CRs);
- the AGCP Core Specification and adopted normative Companion Specifications;
- Core-derived Normative Statement (NS) identifiers;
- the Requirements Traceability Matrix (RTM);
- Formal Test Cases (TCs);
- Harness Checks;
- Harness Test Vectors;
- schema fixtures and execution setup;
- execution results and objective evidence; and
- Test Case and conformance-profile determinations.

This document SHALL NOT create an independent implementation obligation, alter a CR, change normative precedence, or replace an RTM mapping or Formal Test Case. It governs the interpretation and synchronization of conformance artifacts only.

---

# 2. Governing Principles

The AGCP conformance system is governed by the following principles:

1. **Normative obligations originate in the governing specifications.** CRs, the AGCP Core Specification, and expressly adopted normative Companion Specifications define implementation obligations in the applicable precedence order.
2. **Normative Statements support identification and traceability.** NS identifiers represent atomic obligations extracted from the Core. They do not supersede the CRs, Core, or applicable Companion Specifications.
3. **The RTM is the authoritative traceability artifact.** It controls the mappings among CRs, NS identifiers, Formal Test Cases, conformance levels, implementation artifacts, and required evidence.
4. **Formal Test Cases are the authoritative assessment procedures.** A Test Case defines how the corresponding requirement is evaluated and how PASS, FAIL, or NOT APPLICABLE is determined.
5. **Harness Checks automate executable portions of Test Cases.** A Harness Check is a reusable machine-executable capability check. It does not replace the Test Case and does not create an independent normative requirement.
6. **Harness Test Vectors instantiate executable scenarios.** A Test Vector supplies concrete setup, inputs, operations, expected outputs, and evidence expectations. It is not an independent conformance requirement.
7. **Automation produces evidence; the assessment determines conformance.** A harness run can satisfy part or all of the objective evidence needed by a Test Case, but the harness does not independently grant a Test Case or profile-level conformance result.
8. **Conformance levels classify obligation scope.** L1 through L5 are cumulative conformance profiles. They are not separate harnesses and do not determine whether evidence must be obtained manually or automatically.

---

# 3. Authority and Precedence

Normative implementation behavior is governed by the precedence order established by the AGCP Core Specification and the AGCP Conformance Specification:

```text
1. Published AGCP Runtime Governance Conformance Requirements (CRs)
2. AGCP Core Specification
3. Applicable normative Companion Specifications expressly adopted by the implementation profile
4. Implementation Profiles
5. AGCP Conformance Test Suite
6. Reference Implementations
```

The Architecture Reference Model governs architectural terminology and concept meaning where an ARM-defined concept is used, but it does not independently create conformance obligations.

Within the conformance framework:

- the RTM is authoritative for controlled traceability mappings;
- the Formal Test Case is authoritative for the assessment procedure and its pass/fail criteria;
- `conformance/test-mapping.json` is the authoritative machine-readable extension of TC traceability to DS, IF, REG, fixtures, Harness Checks, and Harness Test Vectors;
- `conformance/harness-checks.json` is the machine-readable Harness Check registry;
- `conformance/AGCP-Conformance-Harness-Spec.yml` is the authoritative executable Harness Test Vector catalog;
- `conformance/AGCP-Conformance-Test-Vectors.md` is the required human-readable mirror of that vector catalog; and
- `conformance/fixture-mapping.json` is the authoritative mapping between conformance fixtures and their exact active schemas.

A lower-precedence or automation-layer artifact SHALL NOT weaken, expand, or contradict a higher-precedence obligation or an authoritative RTM/Test Case mapping.

---

# 4. Artifact Roles

| Artifact | Primary role | Authority boundary |
|---|---|---|
| Runtime Governance Conformance Requirement (CR) | Defines a controlled capability requirement. | Normative implementation obligation. |
| AGCP Core Specification | Defines normative runtime behavior and semantics. | Normative implementation obligation. |
| Adopted normative Companion Specification | Defines additional obligations for an adopted interface, profile, or technical domain. | Normative only when expressly adopted and subject to precedence. |
| Architecture Reference Model | Defines architectural terminology, concepts, and relationships. | Interpretive; does not independently create a conformance obligation. |
| Normative Statement (NS) identifier | Provides a stable identifier for an atomic Core obligation used in traceability. | Traceability support; not an independently superior normative source. |
| Requirements Traceability Matrix (RTM) | Controls mappings among CRs, NS identifiers, TCs, levels, evidence, and related artifacts. | Authoritative traceability artifact. |
| Formal Test Case (TC) | Defines the complete assessment procedure, evidence requirements, and PASS/FAIL/NOT APPLICABLE criteria for its requirement. | Authoritative assessment procedure. |
| Test assertion | Expresses a proposition that must be demonstrated within a TC or conformance procedure. | Derives authority from the governing requirement and TC. |
| Harness Check (`CHECK-*`) | Implements a reusable executable capability check supporting one or more TCs. | Harness-local automation identifier; not an independent normative requirement or assessment authority. |
| Harness Test Vector (`TV-*`) | Instantiates a concrete executable scenario, setup sequence, expected result, and evidence expectation. | Execution artifact; not an independent requirement or conformance determination. |
| Fixture | Supplies schema-bound example data used for setup, validation, or execution. | Test input; not sufficient evidence by itself. |
| Harness execution result | Records observed requests, responses, state transitions, evidence, ledger effects, and assertion outcomes for a vector run. | Objective evidence candidate; must be attributable to the applicable release and environment. |
| Assessment record | Combines automated and non-automated evidence and records the TC disposition. | Authoritative record of the Test Case result. |
| Conformance declaration | Aggregates all applicable TC results for the claimed cumulative profile. | Conformance claim; valid only when all applicable requirements are satisfied. |

`AGCP-A-*` assertion identifiers, where used by the AGCP Conformance Specification, are conformance abstractions derived from normative sources. `CHECK-*` identifiers are executable Harness Check identifiers and SHALL NOT be treated as independent `AGCP-A-*` normative assertions.

---

# 5. Relationship Model

## 5.1 End-to-End Model

```text
Normative obligation sources
  CRs + Core + adopted normative Companion Specifications
                         |
                         | atomic identification and controlled mapping
                         v
              NS identifiers + authoritative RTM
                         |
                         v
              Formal Test Case and its criteria
                    /                         \
                   /                           \
                  v                             v
 Manual, documentary, architectural,     Executable portions
 operational, and observational evidence       |
                                                v
                                         Harness Checks
                                                |
                                                v
                                      Harness Test Vectors
                                                |
                                                v
                                      Harness execution results
                   \                           /
                    \                         /
                     v                       v
                       Objective TC evidence
                               |
                               v
                  PASS / FAIL / NOT APPLICABLE
                               |
                               v
                   Cumulative profile claim
```

The branches are complementary. A Test Case may require only non-automated evidence, only executable evidence, or a combination of both. The existence of a Harness Check does not imply that the complete Test Case is automated.

## 5.2 Formal Test Case to Harness Check

A Harness Check automates one or more executable propositions within one or more Formal Test Cases.

The following rules apply:

- A Formal Test Case SHALL remain complete and assessable independently of whether a dedicated Harness Test Vector exists.
- A Formal Test Case MAY map to multiple Harness Checks when several executable capabilities are involved.
- A Harness Check MAY support multiple Formal Test Cases when the same executable capability is reused.
- A Harness Check SHALL identify the capability, expected behavior, applicable execution scope, and evidence it evaluates.
- A Harness Check SHALL NOT replace documentary, architectural, organizational, or other non-executable steps required by the Formal Test Case.
- A Harness Check SHALL NOT introduce an expectation that cannot be traced to the governing CR, Core/Companion obligation, RTM mapping, or Formal Test Case.

The current machine-readable mapping requires every TC record to identify one or more applicable `harness_check_ids`. This identifies applicable executable capability families; it does not assert that every TC has complete executable coverage.

## 5.3 Harness Check to Harness Test Vector

A Harness Test Vector is a concrete instantiation used to exercise one or more Harness Checks or to provide required setup and supporting observability.

The following rules apply:

- A Harness Check MAY be exercised by zero, one, or multiple Test Vectors in a particular repository release.
- A Harness Check with no current Test Vector represents an executable-coverage gap; it does not invalidate the governing Formal Test Case.
- A Test Vector MAY exercise multiple Harness Checks.
- A Test Vector MAY support multiple Formal Test Cases.
- A setup or retrieval vector MAY provide supporting evidence without representing a standalone Harness Check.
- Every current Test Vector SHALL be referenced by at least one TC mapping or be explicitly classified as a controlled setup/support vector in the machine-readable mapping.
- The YAML vector catalog and Markdown vector mirror SHALL contain the same controlled vector identifier set and substantively equivalent scenarios.

## 5.4 Formal Test Case to Harness Test Vector

A Test Case may have:

- one or more **direct** Test Vectors that execute the principal TC scenario;
- one or more **supporting** Test Vectors that provide partial, shared, setup, retrieval, or cross-cutting evidence; or
- no dedicated Test Vector, provided the mapping records an explicit controlled disposition.

A missing dedicated vector SHALL NOT invalidate a Formal Test Case. It means the Test Case remains manual, documentary, architectural, operational, observational, or otherwise not directly instantiated by the current harness catalog.

## 5.5 Fixtures and Setup

Fixtures are resolved and validated before they are used by a vector.

- A fixture SHALL be mapped to its exact active schema through `conformance/fixture-mapping.json`.
- Fixture validity establishes that the input conforms to its schema; it does not establish implementation conformance.
- Vector setup and presteps are part of the executable scenario and SHALL satisfy the same applicable interface and schema requirements as the primary request unless the vector explicitly tests rejection of an invalid setup request.
- A failed setup step prevents the vector from producing valid evidence for its intended primary scenario.

---

# 6. Controlled Cardinalities and Mapping Rules

The controlled relationships for the current AGCP v2.0.8 model are:

| Relationship | Controlled rule |
|---|---|
| CR to primary TC | Exactly one TC per CR in the current release. |
| TC to primary CR | Exactly one primary CR per TC. |
| CR/TC to NS identifiers | One or more direct, conditional, or contextual NS mappings as controlled by the RTM. An NS identifier may support multiple CRs/TCs. |
| TC to Harness Checks | One or more applicable Harness Check identifiers in the current `test-mapping.json`; this does not imply complete automation. |
| Harness Check to TCs | One or more TCs; reusable many-to-many mapping is permitted. |
| TC to direct Test Vectors | Zero or more. Zero requires a controlled no-dedicated-vector disposition. |
| TC to supporting Test Vectors | Zero or more. |
| Harness Check to Test Vectors | Zero or more. Zero identifies an executable-coverage gap for that release. |
| Test Vector to Harness Checks | Zero or more; setup/support vectors may not embody a standalone check. |
| Test Vector to TCs | One or more controlled direct or supporting mappings. |
| Fixture to Test Vectors | Zero or more; each referenced fixture must resolve through the fixture catalog. |
| Vector execution to execution result | One attributable result set per vector run. |
| TC to assessment result | Exactly one recorded disposition for the assessment instance: PASS, FAIL, or NOT APPLICABLE. |

These cardinalities describe the conformance relationship model. They do not require every Test Case to be fully automated.

---

# 7. Conformance-Level Semantics

The five AGCP conformance profiles are cumulative:

| Level | Name |
|---|---|
| L1 | Schema & Envelope Validation |
| L2 | Ordered Governance Mediation |
| L3 | Deterministic Governance |
| L4 | Execution Authorization Control |
| L5 | Multitenant Governance Isolation |

Conformance-level metadata SHALL be interpreted as follows:

- A CR and its TC are assigned to the applicable requirement level through the RTM.
- A claim at a level includes all applicable obligations at that level and every preceding level.
- A Harness Check or Test Vector may carry profile metadata indicating the levels whose behaviors it exercises.
- Harness or vector profile metadata does not create a separate profile test suite and does not independently establish profile conformance.
- There is no independent “L1 harness,” “L2 harness,” or equivalent assessment authority. A harness runner MAY filter executable scenarios by profile for convenience, but the resulting run is only the automated evidence subset for that profile.
- A profile claim is valid only when every applicable Formal Test Case across the cumulative level set has the required disposition and evidence.

---

# 8. Pass, Fail, and Evidence Authority

## 8.1 Formal Test Case Authority

The Formal Test Case controls the assessment disposition.

A TC may be recorded as:

- **PASS** only when every mandatory pass criterion and required evidence element is satisfied;
- **FAIL** when observed behavior or missing required evidence violates a mandatory criterion; or
- **NOT APPLICABLE** only when the TC applicability conditions are not met and the basis is documented.

## 8.2 Harness Result Authority

A Harness Check or Test Vector produces assertion outcomes and objective evidence. It does not independently issue the TC disposition.

- A passing vector demonstrates only the behaviors and evidence expectations exercised by that vector.
- Passing all vectors mapped to a TC does not automatically establish TC PASS when the TC also requires non-automated evidence or procedures.
- A failed mandatory executable expectation is evidence of nonconformance for the affected TC criterion, unless the failure is demonstrated to be a harness, environment, or setup defect rather than implementation behavior.
- A harness infrastructure or setup failure does not establish implementation PASS or FAIL; the run is invalid for the intended evidence purpose and must be corrected and repeated.
- Raw counts of passed vectors, failed vectors, or executed Harness Checks SHALL NOT be used as a substitute for TC-level assessment.

## 8.3 Evidence Attribution

Harness-produced evidence used in an assessment SHALL be attributable to:

- the AGCP repository release;
- the implementation and build under test;
- the harness and vector identifiers;
- the execution environment and applicable configuration;
- the exact inputs, presteps, and authoritative source versions used;
- observed responses, artifacts, state transitions, Governance Evidence, and Governance Ledger effects; and
- the execution time and result disposition.

The assessor SHALL relate each accepted evidence item to the applicable TC criterion. Evidence generated for one vector may support multiple TCs only where the controlled mappings and observed behavior justify that reuse.

---

# 9. Machine-Readable Synchronization Rules

The conformance artifacts SHALL remain synchronized according to the following rules:

1. Every CR and TC identifier in `conformance/test-mapping.json` SHALL resolve to the authoritative RTM and Test Case set.
2. Every Harness Check identifier referenced by a TC SHALL exist in `conformance/harness-checks.json`.
3. Every Test Vector identifier referenced by a TC, Harness Check, or supporting mapping SHALL exist in the authoritative YAML vector catalog.
4. The YAML vector catalog and Markdown mirror SHALL maintain identifier-set equality and substantive scenario parity.
5. Every fixture referenced by a vector SHALL resolve through `conformance/fixture-mapping.json` to an existing active schema and fixture file.
6. A TC without a dedicated executable vector SHALL retain an explicit controlled mapping status and disposition.
7. Every current Harness Check and every current Test Vector SHALL be referenced by the controlled mapping set or carry an explicit controlled disposition.
8. Changes to CR, NS, TC, Harness Check, Test Vector, fixture, DS, IF, or REG relationships SHALL be reflected in the RTM and machine-readable mapping artifacts as applicable.
9. Automation-layer changes SHALL NOT silently alter Formal Test Case pass/fail criteria.
10. Conflicts SHALL be resolved according to normative precedence, with the RTM controlling traceability and the Formal Test Case controlling assessment procedure.

---

# 10. Assessment Workflow

A conforming assessment workflow is:

1. Identify the claimed cumulative conformance profile and applicable implementation scope.
2. Resolve the applicable CRs, Core and adopted Companion obligations, NS identifiers, and TCs from the controlled baseline.
3. Determine the required manual, documentary, architectural, operational, observational, and executable evidence for each TC.
4. Validate applicable schemas, fixtures, interface contracts, registries, harness configuration, and vector setup.
5. Execute the mapped Harness Test Vectors and Harness Checks where executable coverage exists.
6. Preserve attributable execution results and relate them to the applicable TC criteria.
7. Complete all remaining non-automated TC procedures.
8. Record PASS, FAIL, or NOT APPLICABLE for each TC with the required evidence basis.
9. Determine the profile result from the complete cumulative TC set, not from harness results alone.
10. Issue a conformance declaration only when all applicable requirements for the claimed profile are satisfied.

---

# 11. Current-Baseline Example

The current mapping for `TC-001` illustrates the relationship model:

```text
CR-001
  |
  | RTM and Core-derived NS mappings
  v
TC-001 — Submit -> Authorized
  |
  | applicable executable capability checks
  +--> CHECK-PROPOSAL-QUALIFICATION
  +--> CHECK-GOVERNANCE-DECISION
  +--> CHECK-EXECUTION-AUTHORIZATION
  +--> CHECK-GOVERNANCE-EVIDENCE
  +--> CHECK-APPEND-ONLY-GOVERNANCE-LEDGER
  |
  | direct executable scenario
  v
TV-PROP-001
  |
  v
requests, responses, lifecycle outcome, Governance Evidence,
and Governance Ledger observations
  |
  v
objective evidence evaluated under the complete TC-001 procedure
```

`TV-PROP-001` can automate substantial portions of `TC-001`, but TC-001 remains the authoritative assessment procedure. The vector result is accepted only for the criteria it actually demonstrates.

At the controlled AGCP v2.0.8 baseline, the mapping set contains 122 Formal Test Cases, 17 Harness Checks, and 54 Harness Test Vectors. These counts are release metadata, not permanent relationship constraints.

---

# 12. Change Control

Changes to this relationship model are repository-level conformance changes and SHALL be recorded in `governance/CHANGELOG.md`.

A change that only clarifies artifact roles, mapping semantics, or reporting behavior without altering implementation obligations may be issued as a documentation or patch-level correction under the AGCP versioning rules.

A change that alters normative implementation behavior, required TC outcomes, profile scope, or conformance eligibility SHALL be processed under the applicable normative and semantic-versioning rules and synchronized across all affected specifications, RTM mappings, Test Cases, machine-readable catalogs, and assessment guidance.

---

# 13. Summary

The AGCP conformance system separates three functions:

```text
Normative specifications define what an implementation must do.
Formal Test Cases define how conformance is assessed.
Harness Checks and Test Vectors automate portions of that assessment and produce evidence.
```

Conformance levels classify the cumulative scope of obligations. They do not create separate harness authorities. Complete conformance is determined at the Formal Test Case and profile levels using all required automated and non-automated evidence.
