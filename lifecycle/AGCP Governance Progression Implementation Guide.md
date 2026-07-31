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

1. Receive Proposal.
2. Validate schema.
3. Verify provenance.
4. Validate replay protection.
5. Validate idempotency.
6. Validate tenant and Governance Domain.
7. Resolve applicable governance configuration.
8. Perform Proposal Qualification.
9. Execute Governance Decision Function.
10. Perform governed approval or adjudication where required.
11. Generate Execution Authorization or establish another eligible nonterminal lifecycle state.
12. While the Proposal remains nonterminal before commitment, maintain Continuation Integrity where applicable.
13. Detect material governance-condition changes and identify affected Proposals using active risk-based governance configuration.
14. Re-evaluate affected Proposals, assess Admissible Path Viability, and perform governed recovery or policy-defined disposition where required.
15. Immediately before commitment, perform Governance Realization: resolve current Canonical State, qualify state and evidence, re-derive authority, validate governance binding and resulting state, and resolve final Commit-Bound Admissibility.
16. Execute non-bypassable Commit Boundary enforcement.
17. Record Governance Evidence throughout each applicable governance-significant stage.
18. Append governance-significant events to the ordered Append-Only Governance Ledger.
19. Permit governed execution only when Commit Boundary processing succeeds.

---

# 5. Guard Enforcement Matrix

| Guard | Platform | Governance Evaluation |
|-------|:-------:|:---------------------:|
| Schema validation | Yes | No |
| Provenance validation | Yes | No |
| Replay protection | Yes | No |
| Idempotency | Yes | No |
| Tenant validation | Yes | No |
| Governance Domain validation | Yes | No |
| Policy evaluation | No | Yes |
| Constraint evaluation | No | Yes |
| Invariant evaluation | No | Yes |
| Human Review determination | No | Yes |
| Execution Authorization validation | Yes | No |
| Continuation Integrity lifecycle control | Shared | Shared |
| Governance Realization and binding validation | Shared | Shared |
| Commit Boundary enforcement | Yes | No |
| Canonical State validation | Yes | No |

---

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

**Normative restatement.** The requirements in this section restate mandatory obligations from AGCP Core Sections 9.4, 9.6A, 9.6B, 13.1, 13.2, 13.4, 13.6, and 13.6A and the corresponding Normative Statements. They do not create or modify an obligation; the controlling Core and Normative Statement text governs interpretation.

While a Proposal remains nonterminal before commitment, Continuation Integrity SHALL ensure that the Proposal retains a verified continuation basis and at least one admissible path toward binding until it reaches a terminal lifecycle state or successfully completes Commit Boundary processing. Continuation Integrity SHALL preserve and re-establish, where required, the governance basis supporting the Proposal throughout its pre-commit lifecycle.

Continuation Integrity SHALL apply active risk-based governance configuration to determine when material changes to authority, evidence, Canonical State, policy, configuration, lifecycle, validity, tenant, target, dependency, coupling, or cross-domain conditions require re-evaluation of affected nonterminal Proposals. The governance control plane SHALL deterministically re-evaluate affected nonterminal Proposals when such material changes may affect continued execution admissibility, in accordance with active risk-based governance configuration.

Immediately before commitment, the Governance Realization Function SHALL coordinate current Canonical State Resolution, State Qualification, Evidence Qualification, Authority Re-Derivation, Governance Binding Validation, Commit-Bound Admissibility, and enforcement. Governance Realization and Commit Boundary processing SHALL perform the applicable validations required by the Core, including verification that:

- the Proposal remains nonterminal and eligible for commitment;
- applicable Continuation Integrity requirements are satisfied;
- Execution Authorization remains valid;
- required governed approval or adjudication remains valid where applicable;
- tenant and Governance Domain remain eligible;
- Authority Lineage remains valid;
- current Canonical State and qualified evidence support authority and admissibility;
- governance binding and resulting-state requirements remain satisfied; and
- final Commit-Bound Admissibility is established.

Failure of any required validation SHALL prevent commitment and governed execution or SHALL require renewed governance processing, as applicable. An authorized nonterminal Proposal SHALL NOT proceed to commitment when mandatory governance conditions are no longer satisfied. A Proposal SHALL NOT proceed to commitment when its verified continuation basis or at least one admissible path to binding can no longer be established. Pending, rejected, refused, expired, cancelled, superseded, or degraded Proposals SHALL NOT commit unless governance establishes an eligible transition. Post-commit monitoring, intervention, or termination controls are distinct from Continuation Integrity unless separately established by an applicable requirement or implementation profile.

---

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

- AGCP Core Specification
- AGCP Governance Lifecycle Model
- AGCP Normative Governance Progression Table
- AGCP Append-Only Governance Ledger Specification
- AGCP Governance Evidence Specification
- AGCP Human Review Specification
- AGCP Security Specification
- AGCP Conformance Specification
