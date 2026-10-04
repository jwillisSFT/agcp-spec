# AGCP Governance Progression Implementation Guide

**Status:** Informational (Implementation Guide)  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This guide provides implementation guidance for realizing the AGCP governance progression while preserving conformance with the normative specifications.

It explains recommended implementation responsibilities, platform boundaries, deterministic processing, governance evidence generation, ordered ledger recording, Canonical State source resolution and replay, and implementation best practices.

This document is non-normative except where it explicitly restates normative requirements from the AGCP specifications.

---

# 2. Implementation Principles

Implementations SHOULD:

- preserve deterministic externally observable behavior;
- separate platform responsibilities from governance evaluation;
- generate Governance Evidence at governance-significant stages;
- record governance-significant events in the ordered Append-Only Governance Ledger;
- resolve Canonical State from the applicable qualified authoritative governance sources and preserve authoritative ledger ordering for recorded governance events and Derived Lifecycle State.

---

# 3. Platform Responsibilities vs. Governance Evaluation

## Platform Responsibilities (Outside Governance Evaluation)

Recommended responsibilities include:

1. Request parsing
2. Schema validation
3. Provenance verification
4. Replay protection
5. Idempotency validation
6. Tenant validation
7. Governance Domain validation
8. Governance configuration resolution
9. Governance Evidence persistence
10. Ordered Append-Only Governance Ledger recording

These responsibilities SHOULD remain outside governance evaluation.

## Governance Evaluation Responsibilities

The governance evaluation engine SHOULD perform:

- policy evaluation
- constraint evaluation
- invariant evaluation
- Authority Lineage evaluation
- Human Review determination
- governance decision computation

The evaluation engine SHOULD NOT:

- mutate platform state;
- perform transport validation;
- append directly to the governance ledger;
- bypass platform validation.

---

# 4. Recommended Internal Processing Sequence

A conforming implementation should preserve the following logical sequence even when multiple functions are co-located in one service:

1. receive and qualify the proposal;
2. resolve Canonical State and other qualified governance inputs;
3. resolve qualified identity/authorization context through the IAS Profile when applicable;
4. execute the Governance Decision Function / PDP and persist the Governance Decision;
5. complete human adjudication or governed re-evaluation as required;
6. produce proposal-bound Execution Authorization when eligible;
7. maintain Continuation Integrity for nonterminal proposals;
8. invoke the Governance Realization Function;
9. re-derive current authority and commitment-sensitive state/evidence;
10. perform Governance Binding Validation and Commit-Bound Admissibility;
11. deterministically select and apply the controlling PEP Profile;
12. construct the required Enforcement Context and exact PEP request;
13. invoke the PEP through the protected path;
14. record the commitment event if the exact transition is accepted;
15. execute or observe the target operation; and
16. record execution outcome, lifecycle, and evidence.

Co-location does not permit an earlier stage result to substitute for a later-stage check.

# 5. Guard Enforcement Matrix

| Guard / responsibility | GDF / PDP | GRF | PEP | Target/adapter |
|---|---:|---:|---:|---:|
| policy/constraint/invariant evaluation | Primary | Re-invoke if required | No | No |
| authoritative human identity/entitlement as governance input | Consume qualified result | Revalidate when commitment-sensitive | No | No |
| Governance Decision | Primary | Consume | No reinterpretation | No |
| Execution Authorization | No | Validate/consume | Validate reference as profile requires | No |
| current authority/state/lifecycle/prior-use | No | Primary | Verify enforcement-facing subset | No |
| PEP Profile selection/application | No | Primary | Enforce declared mapping contract | No |
| Enforcement Context creation | No | Primary | Validate/consume | No |
| prevention of unauthorized crossing | No | Coordinate | Primary | Honor protected interface |
| target credential | No | No direct use unless GRF+PEP co-located by profile | Primary holder | Validate caller |
| actual operational mutation | No | No | Mediate/invoke | Perform |

The PEP is not a second general-purpose policy engine. It may validate the integrity and applicability of the enforcement-facing bindings required to prevent an ineligible transition.

# 6. Governance Evidence

Governance Evidence SHALL be generated as part of governance-significant processing, including:

- Proposal Qualification
- Governance Decision
- governed approval or adjudication where required
- Execution Authorization
- Continuation Integrity for applicable nonterminal Proposals
- Governance Realization and Commit Boundary processing
- Governed Execution and execution-outcome evidence where applicable

Governance Evidence SHALL include or reference the applicable DS-040 Governance Ledger Event references where a ledger relationship applies.

---

# 7. Ordered Append-Only Governance Ledger

Implementations SHOULD:

- append governance-significant events only;
- preserve ledger sequence ordering;
- prevent modification of historical entries;
- prevent reordering;
- preserve tenant isolation.

Ledger sequence order is authoritative.

Timestamp ordering is not authoritative.

---

# 8. Canonical State

Canonical State SHALL be deterministically resolved from one or more qualified authoritative governance sources. The ordered Append-Only Governance Ledger SHALL be authoritative for recorded governance events, event ordering, and Derived Lifecycle State, but need not originate every governance-relevant fact incorporated into Canonical State.

Recommended resolution sequence:

1. Identify the authoritative governance sources applicable to the evaluation horizon.
2. Qualify each source for freshness, provenance, completeness, consistency, integrity, availability, and ordering suitability.
3. Retrieve applicable Governance Ledger records in authoritative sequence order.
4. Validate Governance Ledger integrity and Governance Evidence relationships.
5. Resolve one authoritative Canonical State or produce Structural Refusal when source suitability or conflict resolution fails.
6. Record or reference the source identities, source versions, ledger positions, provenance, and integrity basis required for deterministic replay.

---

# 9. Continuation Integrity, Governance Realization, and Commit Boundary Normative Restatements

Continuation Integrity preserves the validity of nonterminal governed processing between earlier evaluation and the later commitment attempt.

Governance Realization is the logical function that determines whether an authorized transition is still usable now. It consumes current qualified governance inputs, performs Authority Re-Derivation, Governance Binding Validation, and Commit-Bound Admissibility, and prepares the transition for enforcement.

Where human identity/authorization is commitment-sensitive, GRF resolution uses the controlling IAS Profile. Where a concrete PEP is used, the GRF applies the controlling PEP Profile to map the exact commit-eligible transition into the PEP-supported representation and Enforcement Context.

A PEP Profile may transform representation but may not widen targets, substitute a similar action, discard governance-significant fields, weaken conditions, or reinterpret the Governance Decision. If no faithful mapping exists, the operation fails closed.

The Commit Boundary is the protected boundary at which the PEP permits the exact eligible transition to cross into consequence or prevents it. A successful commitment is not necessarily completed target execution when the target is asynchronous.

# 10. Deterministic Replay

Replay implementations SHOULD:

- replay ordered ledger history;
- validate provenance;
- reconstruct Governance Evidence;
- resolve Canonical State from the recorded qualified authoritative source versions and applicable ordered Governance Ledger records;
- produce equivalent externally observable governance outcomes.

---

# 11. Error Handling

Internal implementation diagnostics MAY be more granular than externally reported rejection codes.

Externally visible rejection codes SHOULD conform to the published AGCP registries.

---

# 12. Implementation Checklist

For the mandatory behaviors summarized by this checklist, a conformant implementation SHALL ensure that:

- governance progression is deterministic;
- platform and governance evaluation responsibilities remain separated;
- Continuation Integrity applies only while a Proposal remains nonterminal before commitment;
- affected nonterminal Proposals are deterministically re-evaluated when material governance conditions change;
- Proposals lacking a verified continuation basis or viable admissible path cannot proceed to commitment;
- Governance Evidence is generated as part of every applicable governance-significant processing stage and satisfies the content, integrity, availability, continuity, and deterministic-replay requirements of Core Section 10;
- governance-significant events are recorded in the ordered Append-Only Governance Ledger;
- Canonical State is reproducible from the applicable qualified authoritative source versions and ordered Governance Ledger records;
- Governance Realization resolves current qualified governance inputs and final Commit-Bound Admissibility immediately before commitment;
- Commit Boundary enforcement prevents any governed consequence unless the current decision and binding remain valid; and
- replay produces equivalent governance outcomes.

---

# 13. Relationship to Other Specifications

Read this guide together with:

- the AGCP Core Specification (`../spec/AGCP-Core.docx`)
- the AGCP Governance Lifecycle Model (`AGCP Governance Lifecycle Model.md`)
- the AGCP Normative Governance Progression Table (`AGCP Normative Governance Progression Table.md`)
- the Append-Only Governance Ledger Specification (`../spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`)
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`)
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`)
- the AGCP Human Adjudication and Governance Approval Specification (`../spec/AGCP-Human-Review-Specification.md`)
- the AGCP Provenance Wire Format Specification (`../spec/AGCP-Provenance-Wire-Format-Specification.md`)
- the AGCP Multitenant Operational Specification (`../spec/AGCP-Multitenant-Operational-Specification.md`)
- AGCP Error Mapping (`../spec/AGCP-Error-Mapping.md`)
- the AGCP Conformance Specification (`../conformance/AGCP-Conformance.md`)
