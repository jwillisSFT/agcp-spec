# AGCP Normative Governance Progression Table

**Status:** Informational (Normative Companion)  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This document provides a concise, tabular representation of the normative governance progression defined by the AGCP Core Specification.

Rather than defining an application state machine, it summarizes the governance stages, decision points, governance evidence, ledger interactions, and progression conditions that together constitute the AGCP governance lifecycle.

Normative implementation behavior is defined by the AGCP specifications. This document is intended to improve readability and implementation consistency.

---

# 2. Governance Progression

| Governance Stage | Entry Condition | Governance Activities | Decision / Guard | Governance Evidence | Ledger Recording | Next Progression |
|------------------|-----------------|-----------------------|------------------|---------------------|------------------|------------------|
| Proposal Qualification | Proposal received | Validate schema, provenance, tenant, Governance Domain, replay protection, idempotency | Qualified or Structurally Refused | Proposal Qualification Evidence | Yes, where required | Governance Decision Function |
| Governance Decision Function | Qualified Proposal | Evaluate policies, constraints, invariants, exceptions, Authority Lineage | Authorized, Denied, Pending Human Review, or Governed Re-evaluation Required | Governance Decision Evidence | Yes | Human Review or Execution Authorization |
| Human Review | Human Review required | Validate reviewers, roles, quorum, provenance | Satisfied or Failed | Human Review Evidence | Yes | Execution Authorization |
| Execution Authorization | Governance prerequisites satisfied | Verify authorization prerequisites using current authoritative governance information | Authorized, Authorization Failure, or Governed Re-evaluation Required | Execution Authorization Evidence | Yes | Commit Boundary |
| Commit Boundary | Valid Execution Authorization | Determine current Canonical State and validate authorization remains applicable | Commit Allowed, Commit Rejected, or Governed Re-evaluation Required | Commit Boundary Evidence | Yes | Governed Execution |
| Governed Execution | Successful Commit Boundary | Perform governed execution and record governance-significant outcomes | Execution Complete or Execution Failure | Execution Evidence | Yes, where applicable | Complete |

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
Execution Authorization
    |
    v
Commit Boundary
    |
    +--> Commit Rejected
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

Canonical State SHALL be derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered Append-Only Governance Ledger can be deterministically reproduced.

Ledger sequence order is authoritative.

Timestamp ordering SHALL NOT determine Canonical State.

---

# 6. Governance Evidence

Each governance stage SHOULD generate Governance Evidence appropriate to that stage.

Governance Evidence documents governance events.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

---

# 7. Relationship to Conformance

The governance progression summarized in this document is verified through the AGCP Conformance framework using the authoritative traceability model:

```text
Normative Specification
        |
        v
Normative Statement (NS)
        |
        v
Conformance Requirement (CR)
        |
        v
Test Case (TC)
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

- AGCP Core Specification
- AGCP Governance Lifecycle Model
- AGCP Append-Only Governance Ledger Specification
- AGCP Governance Evidence Specification
- AGCP Human Review Specification
- AGCP Conformance Specification
