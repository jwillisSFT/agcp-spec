# AGCP Conformance Test Matrix

**Status:** Informational, regenerated from the synchronized Formal Test Case set

This document is the human-readable Test Matrix derived from the controlled Formal Test Cases under `conformance/tests/`. It does not create requirements and does not replace the published Conformance Requirements, Core Specification, Normative Statements, Formal Test Cases, or the final Requirements Traceability Matrix (RTM).

This matrix uses the current **TC-001 through TC-122** files as its source. The machine-readable test mapping, test-control mappings, and Harness Test Vector/Check layer are synchronized. Aggregate conformance-layer validation has passed. Final RTM synchronization is complete at `RTM-1.47`.

---

# Regeneration basis

- Formal Test Case set: `TC-001` through `TC-122`
- Published Conformance Requirement set: `CR-001` through `CR-122`
- One-to-one top-level CR/TC model preserved: yes
- New top-level Formal Test Cases introduced: none
- Formal assertion/traceability changes: 42 TCs
- Additional regression/scenario changes: 22 TCs
- Total affected Formal Test Cases: 64
- New Core-derived NS relationships assigned: 36
- Retired NS identifiers remain reserved and are not active test targets: `NS-8.6A-01`, `NS-8.6A-03`, `NS-9.1-01`
- Final RTM synchronization: complete — `RTM-1.47`

---

# Formal Test Case summary

| Classification | Count |
|---|---:|
| Formal assertion/traceability | 42 |
| Regression/scenario | 22 |
| Unchanged | 58 |

## Conformance-level distribution

| Conformance level | TCs |
|---|---:|
| L1 — Schema & Envelope Validation | 11 |
| L2 — Ordered Governance Mediation | 26 |
| L3 — Deterministic Governance | 30 |
| L4 — Execution Authorization Control | 46 |
| L5 — Multitenant Governance Isolation | 9 |

## Requirement-group distribution

| Requirement group | TCs |
|---|---:|
| RG-1 — Lifecycle Governance | 18 |
| RG-10 — Continuation Integrity Governance | 8 |
| RG-11 — Multitenancy & Governance Isolation | 6 |
| RG-12 — Governance Compilation & Control Plane Integrity | 6 |
| RG-2 — Execution Governance | 24 |
| RG-3 — Governance Object Integrity | 12 |
| RG-4 — Canonical-State Governance | 7 |
| RG-5 — Refusal and Escalation Governance | 9 |
| RG-6 — Governance Evidence and Receipts | 9 |
| RG-7 — Multi-Agent Runtime Governance | 3 |
| RG-8 — Delegation & Authority Lineage | 4 |
| RG-9 — Governance Continuity & Multi-Agent Coordination | 16 |

## Active NS relationship counts represented by the Formal TCs

| Relationship | Count |
|---|---:|
| Direct test-generating | 283 |
| Conditional | 15 |
| Supporting/contextual | 162 |

---

# Complete Formal Test Case matrix

The matrix below is generated from the `Authoritative Traceability` block in each Formal Test Case. `Direct`, `Conditional`, and `Supporting` columns report the number of active NS relationships represented by that TC.

| TC | Primary CR | Test Case | Group | Level | Direct | Conditional | Supporting | v2.1.x change |
|---|---|---|---|---|---:|---:|---:|---|
| `TC-001` | `CR-001` | Submit -> Authorized | RG-1 — Lifecycle Governance | L2 — Ordered Governance Mediation | 2 | 0 | 6 | Formal assertion/traceability |
| `TC-002` | `CR-002` | Submit -> Pending HITL | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 2 | 0 | 0 | Formal assertion/traceability |
| `TC-003` | `CR-003` | Submit -> Rejected (Hard Invariant Failure) | RG-1 — Lifecycle Governance | L2 — Ordered Governance Mediation | 1 | 0 | 2 | Formal assertion/traceability |
| `TC-004` | `CR-004` | Schema Validation Failure | RG-1 — Lifecycle Governance | L1 — Schema & Envelope Validation | 9 | 0 | 7 | Formal assertion/traceability |
| `TC-005` | `CR-005` | Provenance Validation Failure | RG-1 — Lifecycle Governance | L1 — Schema & Envelope Validation | 2 | 0 | 0 | Unchanged |
| `TC-006` | `CR-006` | Tenant Inactive on Submit | RG-1 — Lifecycle Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Unchanged |
| `TC-007` | `CR-007` | Policy Not Found | RG-1 — Lifecycle Governance | L2 — Ordered Governance Mediation | 1 | 0 | 1 | Unchanged |
| `TC-008` | `CR-008` | Idempotent Replay (Identical Payload) | RG-1 — Lifecycle Governance | L3 — Deterministic Governance | 2 | 0 | 0 | Unchanged |
| `TC-009` | `CR-009` | Idempotency Conflict | RG-1 — Lifecycle Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-010` | `CR-010` | GET Authorized Action | RG-1 — Lifecycle Governance | L1 — Schema & Envelope Validation | 1 | 0 | 0 | Unchanged |
| `TC-011` | `CR-011` | Transient State Not Externally Observable | RG-1 — Lifecycle Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Regression/scenario |
| `TC-012` | `CR-012` | Valid Cosign, Quorum Not Yet Met | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-013` | `CR-013` | Valid Cosign Completes Quorum | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-014` | `CR-014` | Cosign Wrong State | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-015` | `CR-015` | Cosign Expired | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 2 | 0 | 0 | Formal assertion/traceability |
| `TC-016` | `CR-016` | Cosign Invalid Signature | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-017` | `CR-017` | HITL Expiration -> Rejected | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-018` | `CR-018` | Governance Cancellation -> Rejected | RG-1 — Lifecycle Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-019` | `CR-019` | Commit Authorized Action | RG-2 — Execution Governance | L4 — Execution Authorization Control | 5 | 0 | 4 | Formal assertion/traceability |
| `TC-020` | `CR-020` | Commit While Pending HITL | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-021` | `CR-021` | Commit While Rejected | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-022` | `CR-022` | Authorization Reference Mismatch | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-023` | `CR-023` | Replay Commit After Executed | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-024` | `CR-024` | Tenant Suspended Before Commit | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-025` | `CR-025` | Tenant Decommissioned Before Commit | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-026` | `CR-026` | Cross-Tenant GET | RG-2 — Execution Governance | L5 — Multitenant Governance Isolation | 6 | 0 | 7 | Formal assertion/traceability |
| `TC-027` | `CR-027` | Cross-Tenant Cosign | RG-2 — Execution Governance | L5 — Multitenant Governance Isolation | 1 | 0 | 0 | Regression/scenario |
| `TC-028` | `CR-028` | Cross-Tenant Commit | RG-2 — Execution Governance | L5 — Multitenant Governance Isolation | 1 | 0 | 0 | Regression/scenario |
| `TC-029` | `CR-029` | Cross-Tenant Policy Resolution | RG-2 — Execution Governance | L5 — Multitenant Governance Isolation | 1 | 0 | 0 | Unchanged |
| `TC-030` | `CR-030` | Cross-Tenant Ledger Access | RG-2 — Execution Governance | L5 — Multitenant Governance Isolation | 1 | 0 | 1 | Unchanged |
| `TC-031` | `CR-031` | Dual Authorized Conflicting Actions | RG-2 — Execution Governance | L4 — Execution Authorization Control | 13 | 0 | 8 | Formal assertion/traceability |
| `TC-032` | `CR-032` | Stale Authorization After Prior Commit | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-033` | `CR-033` | Divergent State Assumption Conflict | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-034` | `CR-034` | Concurrent Authorization Race | RG-2 — Execution Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-035` | `CR-035` | Canonical State Changes During HITL | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-036` | `CR-036` | Missing Intent | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 1 | Unchanged |
| `TC-037` | `CR-037` | Missing Target Resource | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 1 | Unchanged |
| `TC-038` | `CR-038` | Missing Requested Effect | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 1 | Unchanged |
| `TC-039` | `CR-039` | Expired Proposal | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 0 | Unchanged |
| `TC-040` | `CR-040` | Malformed Delegation References | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 3 | 0 | 2 | Formal assertion/traceability |
| `TC-041` | `CR-041` | Malformed Evidence References | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 0 | Unchanged |
| `TC-042` | `CR-042` | Canonical Hash Mismatch | RG-3 — Governance Object Integrity | L3 — Deterministic Governance | 1 | 0 | 1 | Unchanged |
| `TC-043` | `CR-043` | Missing Mission/Task Lineage | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 1 | 0 | 0 | Unchanged |
| `TC-044` | `CR-044` | Broken Delegation Chain | RG-3 — Governance Object Integrity | L2 — Ordered Governance Mediation | 3 | 0 | 3 | Unchanged |
| `TC-045` | `CR-045` | Conflicting Originating Actor | RG-3 — Governance Object Integrity | L1 — Schema & Envelope Validation | 6 | 0 | 1 | Formal assertion/traceability |
| `TC-046` | `CR-046` | Context Attempts to Override Canonical State | RG-3 — Governance Object Integrity | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Unchanged |
| `TC-047` | `CR-047` | Provenance Continuity Gap | RG-3 — Governance Object Integrity | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-048` | `CR-048` | Canonical State Unavailable | RG-4 — Canonical-State Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-049` | `CR-049` | Stale Canonical State | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 1 | 0 | 1 | Unchanged |
| `TC-050` | `CR-050` | Conflicting Canonical-State Sources | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-051` | `CR-051` | Telemetry Conflicts With Canonical State | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-052` | `CR-052` | Canonical-State Hash Mismatch | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-053` | `CR-053` | Structural Refusal Due to Invariant Violation | RG-5 — Refusal and Escalation Governance | L2 — Ordered Governance Mediation | 4 | 0 | 0 | Unchanged |
| `TC-054` | `CR-054` | Structural Refusal Due to Missing Evidence | RG-5 — Refusal and Escalation Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Unchanged |
| `TC-055` | `CR-055` | Structural Refusal Due to Canonical-State Conflict | RG-5 — Refusal and Escalation Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-056` | `CR-056` | Refusal Record Missing Attribution | RG-5 — Refusal and Escalation Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Unchanged |
| `TC-057` | `CR-057` | Refusal Record Not Replayable | RG-5 — Refusal and Escalation Governance | L3 — Deterministic Governance | 1 | 0 | 1 | Unchanged |
| `TC-058` | `CR-058` | Escalation Required but Missing Artifact | RG-5 — Refusal and Escalation Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-059` | `CR-059` | Escalation Resolved to Commit | RG-5 — Refusal and Escalation Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-060` | `CR-060` | Escalation Resolved to Refusal | RG-5 — Refusal and Escalation Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-061` | `CR-061` | Deferred Authorization Expires | RG-5 — Refusal and Escalation Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-062` | `CR-062` | Missing Canonical-State Reference | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 1 | 0 | 1 | Formal assertion/traceability |
| `TC-063` | `CR-063` | Missing Invariant References | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 3 | 0 | 0 | Unchanged |
| `TC-064` | `CR-064` | Missing Evidence Hashes | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 1 | 0 | 1 | Unchanged |
| `TC-065` | `CR-065` | Invalid Signer Identity | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 2 | 2 | 1 | Formal assertion/traceability |
| `TC-066` | `CR-066` | Receipt Replay Hash Mismatch | RG-6 — Governance Evidence and Receipts | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-067` | `CR-067` | Evidence Changes Between Proposal and Commit | RG-6 — Governance Evidence and Receipts | L3 — Deterministic Governance | 9 | 0 | 7 | Formal assertion/traceability |
| `TC-068` | `CR-068` | Evidence Unavailable at Commit | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 2 | 0 | 2 | Formal assertion/traceability |
| `TC-069` | `CR-069` | Evidence Lineage Gap Across Agents | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Regression/scenario |
| `TC-070` | `CR-070` | Governance Context Preserved Across Handoff | RG-7 — Multi-Agent Runtime Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Regression/scenario |
| `TC-071` | `CR-071` | Downstream Agent Drops Context | RG-7 — Multi-Agent Runtime Governance | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Regression/scenario |
| `TC-072` | `CR-072` | Cross-Domain Delegation Requires Escalation | RG-7 — Multi-Agent Runtime Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-073` | `CR-073` | REST vs Message Bus Same Result | RG-8 — Delegation & Authority Lineage | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-074` | `CR-074` | Canonically Equivalent Payloads Same Result | RG-8 — Delegation & Authority Lineage | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-075` | `CR-075` | Different Implementations Produce Same Decision | RG-8 — Delegation & Authority Lineage | L3 — Deterministic Governance | 1 | 0 | 1 | Unchanged |
| `TC-076` | `CR-076` | Same Proposal + Same State + Same Invariants = Same Decision | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 2 | 0 | 2 | Unchanged |
| `TC-077` | `CR-077` | Same Proposal Across Distributed Nodes | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-078` | `CR-078` | Determinism Under Non-Deterministic Agent Inputs | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-079` | `CR-079` | Authorized Actions Successfully Commit | RG-9 — Governance Continuity & Multi-Agent Coordination | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-080` | `CR-080` | Unauthorized Actions Never Commit | RG-9 — Governance Continuity & Multi-Agent Coordination | L4 — Execution Authorization Control | 2 | 0 | 0 | Formal assertion/traceability |
| `TC-081` | `CR-081` | Every Action Follows Valid Lifecycle Transitions | RG-9 — Governance Continuity & Multi-Agent Coordination | L2 — Ordered Governance Mediation | 1 | 1 | 1 | Formal assertion/traceability |
| `TC-082` | `CR-082` | Derived State Matches Ledger Reconstruction | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 3 | 0 | 3 | Formal assertion/traceability |
| `TC-083` | `CR-083` | Canonical State and Decision Remain Synchronized | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-084` | `CR-084` | Commit Uses Latest Canonical State | RG-9 — Governance Continuity & Multi-Agent Coordination | L4 — Execution Authorization Control | 2 | 0 | 1 | Formal assertion/traceability |
| `TC-085` | `CR-085` | Decision Fully Reconstructable from Ledger | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 1 | 0 | 2 | Formal assertion/traceability |
| `TC-086` | `CR-086` | Receipt Reproduces Original Decision | RG-9 — Governance Continuity & Multi-Agent Coordination | L3 — Deterministic Governance | 1 | 0 | 0 | Regression/scenario |
| `TC-087` | `CR-087` | Inadmissible Actions Produce Structural Refusal | RG-9 — Governance Continuity & Multi-Agent Coordination | L2 — Ordered Governance Mediation | 2 | 0 | 1 | Formal assertion/traceability |
| `TC-088` | `CR-088` | Refused Actions Never Execute | RG-9 — Governance Continuity & Multi-Agent Coordination | L4 — Execution Authorization Control | 1 | 0 | 0 | Formal assertion/traceability |
| `TC-089` | `CR-089` | Implementation Passes AGCP Conformance Suite | RG-9 — Governance Continuity & Multi-Agent Coordination | L5 — Multitenant Governance Isolation | 25 | 2 | 35 | Formal assertion/traceability |
| `TC-090` | `CR-090` | Independent Implementations Produce Equivalent Outcomes | RG-9 — Governance Continuity & Multi-Agent Coordination | L5 — Multitenant Governance Isolation | 1 | 0 | 1 | Regression/scenario |
| `TC-091` | `CR-091` | Degraded Governance State | RG-10 — Continuation Integrity Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-092` | `CR-092` | DEGRADED as Non-Terminal State | RG-10 — Continuation Integrity Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-093` | `CR-093` | Re-Evaluation Required from DEGRADED State | RG-10 — Continuation Integrity Governance | L4 — Execution Authorization Control | 3 | 0 | 0 | Regression/scenario |
| `TC-094` | `CR-094` | Admissible Set Determination | RG-2 — Execution Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-095` | `CR-095` | Deterministic Adjudication of Competing Futures | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-096` | `CR-096` | Authority Re-Derivation at Commit | RG-2 — Execution Governance | L4 — Execution Authorization Control | 12 | 3 | 2 | Formal assertion/traceability |
| `TC-097` | `CR-097` | Evidence Qualification Before Admissibility | RG-6 — Governance Evidence and Receipts | L2 — Ordered Governance Mediation | 1 | 0 | 0 | Unchanged |
| `TC-098` | `CR-098` | Continuation Integrity Preservation | RG-10 — Continuation Integrity Governance | L4 — Execution Authorization Control | 5 | 0 | 5 | Regression/scenario |
| `TC-099` | `CR-099` | Admissible Path Viability Tracking | RG-10 — Continuation Integrity Governance | L2 — Ordered Governance Mediation | 2 | 0 | 2 | Unchanged |
| `TC-100` | `CR-100` | Degraded Continuation Detection | RG-10 — Continuation Integrity Governance | L2 — Ordered Governance Mediation | 2 | 0 | 1 | Regression/scenario |
| `TC-101` | `CR-101` | Continuation Recovery Support | RG-10 — Continuation Integrity Governance | L4 — Execution Authorization Control | 2 | 0 | 0 | Regression/scenario |
| `TC-102` | `CR-102` | Governance Realization Layer | RG-2 — Execution Governance | L4 — Execution Authorization Control | 3 | 1 | 3 | Formal assertion/traceability |
| `TC-103` | `CR-103` | State Qualification Prior to Admissibility | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 2 | 0 | 2 | Formal assertion/traceability |
| `TC-104` | `CR-104` | Governance Decision State Suitability | RG-4 — Canonical-State Governance | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-105` | `CR-105` | Composite Proposal Representation | RG-11 — Multitenancy & Governance Isolation | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-106` | `CR-106` | Governance Dependency Graph Evaluation | RG-11 — Multitenancy & Governance Isolation | L4 — Execution Authorization Control | 1 | 0 | 0 | Unchanged |
| `TC-107` | `CR-107` | Composite Admissibility Re-Evaluation | RG-11 — Multitenancy & Governance Isolation | L4 — Execution Authorization Control | 1 | 0 | 0 | Regression/scenario |
| `TC-108` | `CR-108` | Coupling Classification | RG-11 — Multitenancy & Governance Isolation | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-109` | `CR-109` | Partial Bind Governance | RG-11 — Multitenancy & Governance Isolation | L4 — Execution Authorization Control | 2 | 0 | 0 | Regression/scenario |
| `TC-110` | `CR-110` | Governance Compilation | RG-12 — Governance Compilation & Control Plane Integrity | L2 — Ordered Governance Mediation | 1 | 0 | 1 | Unchanged |
| `TC-111` | `CR-111` | Constitutional Validation | RG-12 — Governance Compilation & Control Plane Integrity | L3 — Deterministic Governance | 2 | 0 | 1 | Unchanged |
| `TC-112` | `CR-112` | Constitutional Constraint Preservation | RG-12 — Governance Compilation & Control Plane Integrity | L3 — Deterministic Governance | 3 | 0 | 0 | Unchanged |
| `TC-113` | `CR-113` | Governance Self-Protection | RG-12 — Governance Compilation & Control Plane Integrity | L4 — Execution Authorization Control | 9 | 0 | 7 | Formal assertion/traceability |
| `TC-114` | `CR-114` | Governance Omission Analysis | RG-12 — Governance Compilation & Control Plane Integrity | L3 — Deterministic Governance | 1 | 0 | 0 | Unchanged |
| `TC-115` | `CR-115` | Recursive Authority Containment | RG-8 — Delegation & Authority Lineage | L4 — Execution Authorization Control | 2 | 0 | 1 | Unchanged |
| `TC-116` | `CR-116` | Cross-Domain Authority Isolation | RG-11 — Multitenancy & Governance Isolation | L5 — Multitenant Governance Isolation | 8 | 0 | 13 | Regression/scenario |
| `TC-117` | `CR-117` | Governance Self-Modification Isolation | RG-12 — Governance Compilation & Control Plane Integrity | L4 — Execution Authorization Control | 2 | 0 | 0 | Formal assertion/traceability |
| `TC-118` | `CR-118` | Autonomous Coordination Bounds | RG-9 — Governance Continuity & Multi-Agent Coordination | L4 — Execution Authorization Control | 12 | 0 | 8 | Formal assertion/traceability |
| `TC-119` | `CR-119` | Enforcement Context Availability | RG-2 — Execution Governance | L4 — Execution Authorization Control | 1 | 0 | 2 | Formal assertion/traceability |
| `TC-120` | `CR-120` | Enforcement Decision Integrity | RG-2 — Execution Governance | L4 — Execution Authorization Control | 8 | 3 | 1 | Formal assertion/traceability |
| `TC-121` | `CR-121` | Governance Enforcement Binding | RG-2 — Execution Governance | L4 — Execution Authorization Control | 6 | 2 | 4 | Formal assertion/traceability |
| `TC-122` | `CR-122` | Risk-Based Re-Evaluation | RG-10 — Continuation Integrity Governance | L5 — Multitenant Governance Isolation | 7 | 1 | 2 | Formal assertion/traceability |

---

# Affected Test Case traceability detail

The following 64 TCs changed in this v2.1.x synchronization. This section exposes their current NS relationships directly from the Formal Test Case files so the next machine-readable mapping regeneration can be checked against the same source.

| TC | Change class | Direct NS IDs | Conditional NS IDs | Supporting/contextual NS IDs |
|---|---|---|---|---|
| `TC-001` | Formal assertion/traceability | `NS-7.5-04`, `NS-7.6-01` | None | `NS-7.1-01`, `NS-7.2-03`, `NS-7.3-01`, `NS-7.3-02`, `NS-7.4-02`, `NS-7.6-02` |
| `TC-002` | Formal assertion/traceability | `NS-7.5-01`, `NS-13.6B-01` | None | None |
| `TC-003` | Formal assertion/traceability | `NS-7.4-05` | None | `NS-5.5-01`, `NS-5.5-02` |
| `TC-004` | Formal assertion/traceability | `NS-4.15-01`, `NS-6.1-01`, `NS-6.1-02`, `NS-6.2-02`, `NS-6.3-02`, `NS-6.5-01`, `NS-6.6-01`, `NS-6.7-02`, `NS-7.2-01` | None | `NS-6.3-01`, `NS-6.4-01`, `NS-6.4-03`, `NS-6.6-02`, `NS-6.6-03`, `NS-6.7-01`, `NS-6.7-03` |
| `TC-011` | Regression/scenario | `NS-13.6A-03` | None | None |
| `TC-012` | Regression/scenario | `NS-13.6B-02` | None | None |
| `TC-013` | Regression/scenario | `NS-13.6B-03` | None | None |
| `TC-014` | Formal assertion/traceability | `NS-13.6B-01` | None | None |
| `TC-015` | Formal assertion/traceability | `NS-13.6B-01`, `NS-13.6B-06` | None | None |
| `TC-016` | Formal assertion/traceability | `NS-13.6B-01` | None | None |
| `TC-018` | Regression/scenario | `NS-13.6B-04` | None | None |
| `TC-019` | Formal assertion/traceability | `NS-5.1-01`, `NS-8.6-02`, `NS-9.2-01`, `NS-9.5-01`, `NS-9.6-01` | None | `NS-8.1-01`, `NS-9.2-02`, `NS-9.6-03`, `NS-5.2.3-01` |
| `TC-022` | Formal assertion/traceability | `NS-9.6A-02` | None | None |
| `TC-023` | Regression/scenario | `NS-13.6A-05` | None | None |
| `TC-024` | Formal assertion/traceability | `NS-9.6A-01` | None | None |
| `TC-026` | Formal assertion/traceability | `NS-11.1-02`, `NS-11.2-01`, `NS-11.4-02`, `NS-11.5-01`, `NS-11.5-03`, `NS-11.7-02` | None | `NS-11.2-02`, `NS-11.3-01`, `NS-11.3-02`, `NS-11.5-02`, `NS-11.6-04`, `NS-11.7-01`, `NS-11.7-03` |
| `TC-027` | Regression/scenario | `NS-11.1-02` | None | None |
| `TC-028` | Regression/scenario | `NS-11.1-02` | None | None |
| `TC-031` | Formal assertion/traceability | `NS-4.5-01`, `NS-4.11-01`, `NS-8.1-02`, `NS-8.2-01`, `NS-8.2-02`, `NS-8.4-01`, `NS-8.5-01`, `NS-8.5-02`, `NS-8.5-03`, `NS-8.6-01`, `NS-8.7-02`, `NS-13.6-05`, `NS-7.1-03` | None | `NS-8.2-03`, `NS-8.2-04`, `NS-8.3-01`, `NS-8.3-02`, `NS-8.6-03`, `NS-8.7-01`, `NS-8.7-03`, `NS-13.6-06` |
| `TC-032` | Formal assertion/traceability | `NS-8.1-03` | None | None |
| `TC-035` | Regression/scenario | `NS-13.4-04` | None | None |
| `TC-040` | Formal assertion/traceability | `NS-12.2-02`, `NS-12.4-01`, `NS-12.7-02` | None | `NS-12.3-01`, `NS-12.7-01` |
| `TC-045` | Formal assertion/traceability | `NS-12.3-02`, `NS-4.12-01`, `NS-4.12A-02`, `NS-6.4-04`, `NS-6.4-05`, `NS-6.6A-03` | None | `NS-6.6A-02` |
| `TC-047` | Formal assertion/traceability | `NS-10.8A-03` | None | None |
| `TC-048` | Formal assertion/traceability | `NS-9.6A-01` | None | None |
| `TC-058` | Formal assertion/traceability | `NS-13.6B-01` | None | None |
| `TC-059` | Regression/scenario | `NS-13.6B-03` | None | None |
| `TC-060` | Formal assertion/traceability | `NS-13.6B-01` | None | None |
| `TC-062` | Formal assertion/traceability | `NS-10.4-01` | None | `NS-10.4-02` |
| `TC-065` | Formal assertion/traceability | `NS-13.6B-01`, `NS-13.6B-07` | `NS-13.6B-08`, `NS-13.6B-09` | `NS-12.6-04` |
| `TC-067` | Formal assertion/traceability | `NS-10.1-02`, `NS-10.2-01`, `NS-10.2-03`, `NS-10.3-01`, `NS-10.3-02`, `NS-10.8-01`, `NS-10.8-03`, `NS-10.8A-03`, `NS-10.9-01` | None | `NS-7.6-03`, `NS-8.6-04`, `NS-10.2-02`, `NS-10.8-02`, `NS-10.9-02`, `NS-10.9-03`, `NS-13.6-03` |
| `TC-068` | Formal assertion/traceability | `NS-9.6A-01`, `NS-9.6A-02` | None | `NS-10.6-01`, `NS-10.6-02` |
| `TC-069` | Regression/scenario | `NS-16.6A-03` | None | None |
| `TC-070` | Regression/scenario | `NS-16.6A-03` | None | None |
| `TC-071` | Regression/scenario | `NS-16.6A-03` | None | None |
| `TC-079` | Formal assertion/traceability | `NS-9.5-02` | None | None |
| `TC-080` | Formal assertion/traceability | `NS-9.5-03`, `NS-9.6A-03` | None | None |
| `TC-081` | Formal assertion/traceability | `NS-13.6A-04` | `NS-9.5-05` | `NS-4.7-02` |
| `TC-082` | Formal assertion/traceability | `NS-4.6-03`, `NS-4.6-05`, `NS-10.8A-02` | None | `NS-13.6A-01`, `NS-5.2.5-01`, `NS-5.2.5-02` |
| `TC-084` | Formal assertion/traceability | `NS-9.5-04`, `NS-9.1-03` | None | `NS-13.6-07` |
| `TC-085` | Formal assertion/traceability | `NS-10.7-03` | None | `NS-10.7-01`, `NS-10.7-02` |
| `TC-086` | Regression/scenario | `NS-10.1-01` | None | None |
| `TC-087` | Formal assertion/traceability | `NS-7.5-01`, `NS-9.4-07` | None | `NS-7.4-01` |
| `TC-088` | Formal assertion/traceability | `NS-9.6A-03` | None | None |
| `TC-089` | Formal assertion/traceability | `NS-1.5-01`, `NS-1.5-02`, `NS-2.7-01`, `NS-2.7-03`, `NS-3.4-05`, `NS-5.9-01`, `NS-5.9-03`, `NS-17.1-01`, `NS-17.2-03`, `NS-17.3-01`, `NS-17.4-01`, `NS-17.4-02`, `NS-17.5-01`, `NS-17.5-02`, `NS-17.6-01`, `NS-17.6-02`, `NS-17.6-03`, `NS-17.7-01`, `NS-17.7-02`, `NS-17.8-01`, `NS-17.8-02`, `NS-17.9-01`, `NS-17.9-02`, `NS-17.10-01`, `NS-17.10-02` | `NS-4.12A-01`, `NS-17.5-04` | `NS-1.2-01`, `NS-2.1-01`, `NS-2.4-01`, `NS-2.6-01`, `NS-2.7-02`, `NS-3.3-01`, `NS-3.3-02`, `NS-3.4-01`, `NS-3.4-02`, `NS-3.4-03`, `NS-3.4-04`, `NS-3.5-01`, `NS-3.6-01`, `NS-3.6-02`, `NS-3.6-03`, `NS-3.6-04`, `NS-3.7-01`, `NS-4.1-01`, `NS-4.1-02`, `NS-4.8-01`, `NS-4.19-01`, `NS-4.19-02`, `NS-5.2-01`, `NS-5.3-01`, `NS-5.3-02`, `NS-5.3-03`, `NS-5.4-01`, `NS-5.7-01`, `NS-5.7-02`, `NS-5.8-01`, `NS-17.2-02`, `NS-17.5-03`, `NS-17.7-03`, `NS-17.8-03`, `NS-3.3-03` |
| `TC-090` | Regression/scenario | `NS-5.2.1-01` | None | `NS-5.9-02` |
| `TC-091` | Regression/scenario | `NS-13.6C-01` | None | None |
| `TC-093` | Regression/scenario | `NS-13.5-02`, `NS-13.5-03`, `NS-13.5-04` | None | None |
| `TC-096` | Formal assertion/traceability | `NS-8.4-02`, `NS-8.6A-02`, `NS-12.1-01`, `NS-12.1-02`, `NS-12.2-01`, `NS-12.5-01`, `NS-12.5-02`, `NS-12.6-02`, `NS-8.4-03`, `NS-8.6A-04`, `NS-8.6A-05`, `NS-12.6-06` | `NS-8.6A-06`, `NS-12.2-03`, `NS-13.6B-10` | `NS-8.6-05`, `NS-13.6-01` |
| `TC-098` | Regression/scenario | `NS-13.1-01`, `NS-13.2-01`, `NS-13.3-01`, `NS-13.4-05`, `NS-13.5-01` | None | `NS-13.2-04`, `NS-13.3-02`, `NS-13.6-04`, `NS-13.7-01`, `NS-13.7-03` |
| `TC-100` | Regression/scenario | `NS-13.4-02`, `NS-13.6C-01` | None | `NS-13.4-01` |
| `TC-101` | Regression/scenario | `NS-13.4-06`, `NS-13.6C-04` | None | None |
| `TC-102` | Formal assertion/traceability | `NS-7.1-02`, `NS-9.6A-01`, `NS-9.1-03` | `NS-5.6-01` | `NS-5.2.2-01`, `NS-5.2.2-02`, `NS-5.2.4-01` |
| `TC-103` | Formal assertion/traceability | `NS-4.6-01`, `NS-7.6A-01` | None | `NS-4.6-02`, `NS-5.2.5-03` |
| `TC-107` | Regression/scenario | `NS-9.6B-04` | None | None |
| `TC-109` | Regression/scenario | `NS-9.6B-01`, `NS-9.6B-05` | None | None |
| `TC-113` | Formal assertion/traceability | `NS-15.1-01`, `NS-15.1-02`, `NS-15.2-02`, `NS-15.4-01`, `NS-15.4-02`, `NS-15.5-01`, `NS-15.6-01`, `NS-15.6A-03`, `NS-15.7-02` | None | `NS-15.2-01`, `NS-15.3-01`, `NS-15.3-02`, `NS-15.6-02`, `NS-15.6-03`, `NS-15.7-01`, `NS-15.7-03` |
| `TC-116` | Regression/scenario | `NS-12.6-03`, `NS-14.1-01`, `NS-14.2-01`, `NS-14.4-02`, `NS-14.5-01`, `NS-14.5-02`, `NS-14.6-03`, `NS-14.7-02` | None | `NS-11.6-01`, `NS-11.6-02`, `NS-13.6-02`, `NS-14.2-02`, `NS-14.3-01`, `NS-14.3-02`, `NS-14.4-01`, `NS-14.6-01`, `NS-14.6-04`, `NS-14.6-05`, `NS-14.7-01`, `NS-14.7-03`, `NS-16.6-04` |
| `TC-117` | Formal assertion/traceability | `NS-15.6B-01`, `NS-15.6B-02` | None | None |
| `TC-118` | Formal assertion/traceability | `NS-16.1-02`, `NS-16.2-02`, `NS-16.4-01`, `NS-16.4-02`, `NS-16.4-03`, `NS-16.5-01`, `NS-16.5-02`, `NS-16.6-01`, `NS-16.6-02`, `NS-16.6A-01`, `NS-16.7-02`, `NS-16.6-07` | None | `NS-16.1-01`, `NS-16.2-01`, `NS-16.3-01`, `NS-16.3-02`, `NS-16.6-05`, `NS-16.6-06`, `NS-16.7-01`, `NS-16.7-03` |
| `TC-119` | Formal assertion/traceability | `NS-9.6A-03` | None | `NS-9.3-01`, `NS-9.3-02` |
| `TC-120` | Formal assertion/traceability | `NS-9.4-01`, `NS-9.4-02`, `NS-9.4-04`, `NS-9.6A-03`, `NS-4.13B-01`, `NS-9.4-06`, `NS-9.4-08`, `NS-9.4-09` | `NS-4.13E-01`, `NS-4.13E-02`, `NS-9.4-05` | `NS-9.4-03` |
| `TC-121` | Formal assertion/traceability | `NS-4.7-01`, `NS-9.1-02`, `NS-9.6-04`, `NS-9.6A-04`, `NS-5.2.3-02`, `NS-13.6-08` | `NS-9.6A-05`, `NS-9.6A-06` | `NS-9.6-02`, `NS-9.7-01`, `NS-9.7-02`, `NS-9.7-03` |
| `TC-122` | Formal assertion/traceability | `NS-13.2-04`, `NS-13.3-01`, `NS-13.4-01`, `NS-13.4-03`, `NS-13.4-04`, `NS-13.4-05`, `NS-13.7-02` | `NS-7.6-05` | `NS-13.3-02`, `NS-13.7-03` |

---

# New Core-derived NS disposition

The 36 newly introduced Core-derived NS relationships are allocated to existing CR-linked Formal Test Cases; no TC-123 is created.

| NS | Formal TC | Relationship |
|---|---|---|
| `NS-7.1-03` | `TC-031` | Direct |
| `NS-4.12-01` | `TC-045` | Direct |
| `NS-4.12A-02` | `TC-045` | Direct |
| `NS-6.4-04` | `TC-045` | Direct |
| `NS-6.4-05` | `TC-045` | Direct |
| `NS-6.6A-03` | `TC-045` | Direct |
| `NS-13.6B-07` | `TC-065` | Direct |
| `NS-13.6B-08` | `TC-065` | Conditional |
| `NS-13.6B-09` | `TC-065` | Conditional |
| `NS-4.7-02` | `TC-081` | Support |
| `NS-9.5-05` | `TC-081` | Conditional |
| `NS-9.1-03` | `TC-102` | Direct |
| `NS-9.4-07` | `TC-087` | Direct |
| `NS-3.3-03` | `TC-089` | Support |
| `NS-4.12A-01` | `TC-089` | Conditional |
| `NS-17.5-04` | `TC-089` | Conditional |
| `NS-8.4-03` | `TC-096` | Direct |
| `NS-8.6A-04` | `TC-096` | Direct |
| `NS-8.6A-05` | `TC-096` | Direct |
| `NS-12.6-06` | `TC-096` | Direct |
| `NS-8.6A-06` | `TC-096` | Conditional |
| `NS-12.2-03` | `TC-096` | Conditional |
| `NS-13.6B-10` | `TC-096` | Conditional |
| `NS-5.6-01` | `TC-102` | Conditional |
| `NS-16.6-07` | `TC-118` | Direct |
| `NS-4.13B-01` | `TC-120` | Direct |
| `NS-9.4-06` | `TC-120` | Direct |
| `NS-9.4-08` | `TC-120` | Direct |
| `NS-9.4-09` | `TC-120` | Direct |
| `NS-4.13E-01` | `TC-120` | Conditional |
| `NS-4.13E-02` | `TC-120` | Conditional |
| `NS-9.4-05` | `TC-120` | Conditional |
| `NS-13.6-08` | `TC-121` | Direct |
| `NS-9.6A-05` | `TC-121` | Conditional |
| `NS-9.6A-06` | `TC-121` | Conditional |
| `NS-7.6-05` | `TC-122` | Conditional |

---

# Retired NS test-target disposition

Retired identifiers remain permanently reserved but are not current test targets.

| Retired NS | Former Formal TC reference | Current disposition |
|---|---|---|
| `NS-9.1-01` | `TC-084` | Removed from active direct/conditional/supporting TC metadata; replacement coverage is represented by current v2.1.x NS relationships. |
| `NS-8.6A-01` | `TC-096` | Removed from active direct/conditional/supporting TC metadata; replacement coverage is represented by current v2.1.x NS relationships. |
| `NS-8.6A-03` | `TC-096` | Removed from active direct/conditional/supporting TC metadata; replacement coverage is represented by current v2.1.x NS relationships. |

---

# Primary v2.1.x coverage areas

| Area | Primary Formal TC coverage |
|---|---|
| Authoritative identity/authorization qualification and claimant-conflict handling | `TC-045`, `TC-065`, `TC-096` |
| Decision/authorization versus current commit eligibility | `TC-031`, `TC-084`, `TC-096`, `TC-102` |
| PEP Profile mapping, Enforcement Context, and non-widening | `TC-087`, `TC-119`, `TC-120` |
| GRF-to-PEP trust/binding and co-location equivalence | `TC-121` |
| Commitment versus later execution outcome | `TC-079`, `TC-081`, `TC-082`, `TC-085`, `TC-086` |
| Composite current Commit-Bound Admissibility | `TC-107`, `TC-109`, `TC-118` |
| Governed GDF re-evaluation without GDF/GRF collapse | `TC-093`, `TC-101`, `TC-122` |

---

# Downstream conformance-artifact status

The downstream conformance artifacts derived from this Test Matrix have now been regenerated and aggregate-validated. Their current status is:

| Downstream artifact | Status after this step |
|---|---|
| `conformance/test-mapping.json` | **COMPLETE - regenerated for TC-001 through TC-122** |
| `conformance/test-control-mapping.json` and `AGCP-Test-Control-Mapping.md` | **Regenerated for TC-001 through TC-122** |
| `AGCP-Conformance-Test-Vectors.md` and executable vector catalog | **COMPLETE - 71 synchronized vectors** |
| `AGCP Harness Check Registry.md` / harness checks | **COMPLETE - 21 synchronized checks** |
| Final conformance-layer validation | **COMPLETE - PASS** |
| Final RTM synchronization | **COMPLETE — RTM-1.47** |

The current test mapping, test-control mappings, Harness Checks, and Harness Test Vectors are synchronized to the Formal TCs, and aggregate conformance-layer validation has passed. Final RTM synchronization is complete at `RTM-1.47`.

