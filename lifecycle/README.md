# Lifecycle

**Status:** Informational  
**Repository Versioning:** Repository Release Governed

## Purpose

This directory contains companion documents describing the AGCP governance progression model.

These documents explain how governance progresses from Proposal Qualification through applicable pre-commit Continuation Integrity, Governance Realization, Commit Boundary processing, and Governed Execution. They are intended to assist architects, implementers, reviewers, and conformance engineers in understanding the governance processing model defined by the AGCP specifications.

Except where explicitly stated, these documents do not introduce independent normative requirements.

---

# Relationship to the Authoritative Sources

The published CRs are the highest-precedence normative capability requirements, followed by the AGCP Core Specification and any applicable normative Companion Specifications expressly adopted by the implementation profile. The ARM governs architectural terminology and concept meaning without independently creating conformance obligations.

The lifecycle documents in this directory:

- explain governance progression;
- summarize behavior established by the authoritative normative sources;
- provide implementation guidance; and
- illustrate the relationship between governance stages.

Normative Statements are Core-derived extraction and traceability artifacts. Where an inconsistency exists, it SHALL be resolved using the complete Core-defined precedence order rather than treating this lifecycle material or the Normative Statements as an independent normative authority.

---

# Directory Contents

| Document | Purpose |
|----------|---------|
| AGCP Governance Lifecycle Model.md | Conceptual description of governance progression and governance-stage interactions. |
| AGCP Normative Governance Progression Table.md | Concise tabular summary of governance stages, guards, governance evidence, and progression outcomes. |
| AGCP Governance Progression Implementation Guide.md | Recommended implementation practices for realizing the governance progression while preserving conformance. |

---

# Governance Progression Overview

```text
Proposal
    │
    ▼
Proposal Qualification
    │
    ├──► Structural Refusal
    │
    ▼
Governance Decision Function
    │
    ├──► Denied
    │
    ├──► Pending Human Review
    │           │
    │           ▼
    │     Human Review
    │
    ▼
Execution Authorization / Eligible Nonterminal State
    │
    ├──► Continuation Integrity, where applicable before commitment
    │           ├──► Re-evaluation, Degraded State, Recovery, or Terminal Disposition
    │           └──► Remains Eligible
    │
    ▼
Governance Realization and Commit Boundary
    │
    ├──► Commit Rejected
    │
    ▼
Governed Execution
```

This progression represents governance processing rather than an application state machine. Continuation Integrity ends at successful commitment or another governed terminal lifecycle state; post-commit operational controls are separately defined and are not Continuation Integrity.

---

# Canonical State

Canonical State is deterministically resolved from the applicable qualified authoritative governance sources. The ordered Append-Only Governance Ledger is authoritative for recorded governance events, event ordering, and Derived Lifecycle State incorporated into Canonical State, but need not originate every governance-relevant fact.

Ledger sequence order is authoritative for ledger-governed events and Derived Lifecycle State.

Timestamp ordering and implementation-specific storage ordering are not authoritative substitutes for ledger sequence order.

---

# Governance Evidence

Governance Evidence documents governance-significant events throughout the governance progression.

The Append-Only Governance Ledger establishes the authoritative ordering and persistence of those events.

Together with the applicable qualified authoritative governance sources, they enable deterministic replay, auditability, and Canonical State resolution.

---

# Relationship to Conformance

The behavior described by the lifecycle documents is verified by the AGCP Conformance framework.

The authoritative traceability model is:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
        |
        v
Harness Check
        |
        v
Harness Test Vector
```

The lifecycle documents explain this behavior but do not replace the normative specifications or conformance artifacts.

---

# Intended Audience

This directory is intended for:

- architects
- implementers
- governance engine developers
- platform developers
- reviewers
- conformance engineers
- auditors

---

# Repository Versioning

Lifecycle documentation follows repository-release versioning and evolves with the AGCP architecture while remaining consistent with the authoritative specifications.

---

# Canonical Evidence and Companion References

Lifecycle documents use DS-020 Governance Evidence (`../schemas/governance_evidence.json`) and DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`) as the canonical machine-readable evidence artifacts. Canonical companion-reference dispositions are maintained in `../governance/AGCP-Normative-Companion-Reference-Dispositions.md`.
