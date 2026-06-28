# Lifecycle

**Status:** Informational  
**Repository Versioning:** Repository Release Governed

## Purpose

This directory contains companion documents describing the AGCP governance progression model.

These documents explain how governance progresses from Proposal Qualification through Governed Execution. They are intended to assist architects, implementers, reviewers, and conformance engineers in understanding the governance processing model defined by the AGCP specifications.

Except where explicitly stated, these documents do not introduce independent normative requirements.

---

# Relationship to the Core Specification

The AGCP Core Specification is the authoritative definition of governance behavior.

The lifecycle documents in this directory:

- explain governance progression;
- summarize normative behavior;
- provide implementation guidance; and
- illustrate the relationship between governance stages.

Where any inconsistency exists, the Core Specification takes precedence.

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
Execution Authorization
    │
    ▼
Commit Boundary
    │
    ├──► Commit Rejected
    │
    ▼
Governed Execution
```

This progression represents governance processing rather than an application state machine.

---

# Canonical State

Canonical State is derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation can be deterministically reproduced from ordered ledger entries.

Ledger sequence order is authoritative.

Timestamp ordering is not authoritative.

---

# Governance Evidence

Governance Evidence documents governance-significant events throughout the governance progression.

The Append-Only Governance Ledger establishes the authoritative ordering and persistence of those events.

Together they enable deterministic replay, auditability, and Canonical State reconstruction.

---

# Relationship to Conformance

The behavior described by the lifecycle documents is verified by the AGCP Conformance framework.

The authoritative traceability model is:

```text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
        ↓
Harness Check
        ↓
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
