# AGCP Normative Governance Progression Table

**Status:** Informational Companion  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This document provides a concise, tabular representation of the normative governance progression defined by the AGCP Core Specification.

Rather than defining an application state machine, it summarizes the governance stages, decision points, governance evidence, ledger interactions, and progression conditions that together constitute the AGCP governance lifecycle.

Normative implementation behavior is established by the published CRs, the AGCP Core Specification, and any applicable normative Companion Specifications expressly adopted by the implementation profile. The ARM governs architectural terminology and concept meaning. This document summarizes that behavior for readability and implementation consistency and does not create or supersede normative obligations.

---

# 2. Governance Progression

| Governance Stage | Entry Condition | Governance Activities | Decision / Guard | Governance Evidence | Ledger Recording | Next Progression |
|------------------|-----------------|-----------------------|------------------|---------------------|------------------|------------------|
| Proposal Qualification | Proposal received | Validate schema, provenance, tenant, Governance Domain, replay protection, idempotency | Qualified or Structurally Refused | Proposal Qualification Evidence | Yes, where required | Governance Decision Function |
| Governance Decision Function | Qualified Proposal | Evaluate policies, constraints, invariants, exceptions, Authority Lineage | Authorized, Denied, Pending Human Review, or Governed Re-evaluation Required | Governance Decision Evidence | Yes | Human Review or Execution Authorization |
| Human Review | Human Review required | Validate reviewers, roles, quorum, provenance | Satisfied or Failed | Human Review Evidence | Yes | Execution Authorization |
| Execution Authorization | Governance prerequisites satisfied | Verify authorization prerequisites using current authoritative governance information | Authorized, Authorization Failure, or Governed Re-evaluation Required | Execution Authorization Evidence | Yes | Continuation Integrity where applicable, otherwise Governance Realization and Commit Boundary |
| Continuation Integrity | Authorized or otherwise eligible nonterminal Proposal before commitment | Preserve or re-establish the continuation basis; detect material governance-condition changes; evaluate admissible-path viability; perform governed re-evaluation or recovery where required | Proposal Remains Authorized or Viable, Governed Re-evaluation Required, Degraded, Commitment Suspended, Proposal Restored to Eligible State, Non-Executable Lifecycle State, or Governed Terminal Outcome | Continuation Integrity Evidence | Yes | Governance Realization and Commit Boundary, renewed governance processing, recovery, or policy-defined terminal disposition |
| Governance Realization and Commit Boundary | Valid current governance basis and eligible nonterminal Proposal | Resolve current Canonical State, re-derive authority, qualify evidence and state, validate governance binding and resulting state, resolve final Commit-Bound Admissibility, and enforce the result | Commit Successful, Commit Failed, or Governed Re-evaluation Required | Governance Realization and Commit Boundary Evidence | Yes | Governed Execution or renewed governance processing |
| Governed Execution | Successful Commit Boundary | Perform governed execution and record governance-significant outcomes | Execution Complete or Execution Failure | Execution Evidence | Yes, where applicable | Complete or separately defined post-commit operational controls |

---

# 3. Governance Progression Diagram

```text
Proposal
    |
    v
Proposal Qualification
    |
    +--> Structural Refusal
    |
    v
Governance Decision Function
    |
    +--> Denied
    |
    +--> Pending Human Review
    |          |
    |          v
    |    Human Review
    |          |
    v          v
Execution Authorization / Eligible Nonterminal State
    |
    +--> Continuation Integrity, where applicable before commitment
    |          |
    |          +--> Re-evaluation / Degraded / Recovery / Terminal Disposition
    |          |
    |          v
    |     Remains Eligible
    |
    v
Governance Realization and Commit Boundary
    |
    +--> Commit Rejected or Governed Re-evaluation Required
    |
    v
Governed Execution
```

---

# 4. Commit Boundary Decision Matrix

| Condition | Result |
|-----------|--------|
| Execution Authorization valid and current Canonical State satisfies authorization prerequisites | Commit Allowed |
| Authorization expired or invalid | Commit Rejected |
| Tenant inactive | Commit Rejected |
| Required Human Review invalid or expired | Commit Rejected |
| Authority Lineage invalid | Commit Rejected |
| Governance configuration changed requiring re-evaluation | Governed Re-evaluation Required |
| Current Canonical State no longer satisfies authorization prerequisites | Governed Re-evaluation Required |

---

# 5. Canonical State

Canonical State SHALL be deterministically resolved from one or more qualified authoritative governance sources.

The ordered Append-Only Governance Ledger SHALL be authoritative for recorded governance events, event ordering, and Derived Lifecycle State. Where Canonical State incorporates those elements, ledger sequence order SHALL be authoritative.

Timestamp ordering and implementation-specific storage ordering SHALL NOT substitute for authoritative ledger ordering.

Materialized Canonical State views SHALL remain reproducible from the applicable qualified authoritative source versions and ordered Governance Ledger records and SHALL NOT supersede those sources.

---

# 6. Governance Evidence

Each governance-significant processing stage SHALL generate Governance Evidence appropriate to that stage and sufficient to satisfy the applicable requirements of Core Section 10.

Governance Evidence SHALL accurately represent the governance processing that occurred and SHALL preserve the attributable, integrity-protected basis required for audit, conformance assessment, assurance assessment, forensic analysis, and deterministic replay.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

---

# 7. Relationship to Conformance

The governance progression summarized in this document is verified through the AGCP Conformance framework using the authoritative traceability model:

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

---

# 8. Relationship to Other Specifications

This document should be read together with:

- the AGCP Core Specification (`../spec/AGCP-Core.docx`)
- the AGCP Governance Lifecycle Model (`AGCP Governance Lifecycle Model.md`)
- the Append-Only Governance Ledger Specification (`../spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`)
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`)
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`)
- the AGCP Human Adjudication and Governance Approval Specification (`../spec/AGCP-Human-Review-Specification.md`)
- the AGCP Conformance Specification (`../conformance/AGCP-Conformance.md`)
