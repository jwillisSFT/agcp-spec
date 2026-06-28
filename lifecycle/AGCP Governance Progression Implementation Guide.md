# AGCP Governance Progression Implementation Guide

**Status:** Informational (Implementation Guide)  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This guide provides implementation guidance for realizing the AGCP governance progression while preserving conformance with the normative specifications.

It explains recommended implementation responsibilities, platform boundaries, deterministic processing, governance evidence generation, ordered ledger recording, Canonical State reconstruction, and implementation best practices.

This document is non-normative except where it explicitly restates normative requirements from the AGCP specifications.

---

# 2. Implementation Principles

Implementations SHOULD:

- preserve deterministic externally observable behavior;
- separate platform responsibilities from governance evaluation;
- generate Governance Evidence at governance-significant stages;
- record governance-significant events in the ordered Append-Only Governance Ledger;
- derive Canonical State from ordered ledger history (or a verifiable materialized state reproducible from that history).

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
10. Perform Human Review where required.
11. Generate Execution Authorization.
12. Determine current Canonical State.
13. Execute Commit Boundary validation.
14. Record Governance Evidence.
15. Append governance-significant events to the ordered Append-Only Governance Ledger.
16. Permit governed execution when Commit Boundary succeeds.

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
| Commit Boundary validation | Yes | No |
| Canonical State validation | Yes | No |

---

# 6. Governance Evidence

Governance Evidence SHOULD be generated for governance-significant processing including:

- Proposal Qualification
- Governance Decision
- Human Review
- Execution Authorization
- Commit Boundary
- Governed Execution

Evidence SHOULD include references to applicable ledger entries where available.

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

Canonical State SHALL be derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered Append-Only Governance Ledger can be deterministically reproduced.

Recommended reconstruction sequence:

1. Read ordered ledger entries.
2. Validate ledger integrity.
3. Reconstruct Governance Evidence relationships.
4. Reconstruct authoritative governance progression.
5. Derive Canonical State.

---

# 9. Commit Boundary Guidance

Immediately before governed execution, implementations SHOULD verify:

- Execution Authorization remains valid;
- required Human Review remains valid;
- tenant remains eligible;
- Governance Domain remains valid;
- Authority Lineage remains valid;
- current Canonical State satisfies authorization prerequisites.

Failure of any validation SHOULD prevent governed execution.

---

# 10. Deterministic Replay

Replay implementations SHOULD:

- replay ordered ledger history;
- validate provenance;
- reconstruct Governance Evidence;
- derive Canonical State;
- produce equivalent externally observable governance outcomes.

---

# 11. Error Handling

Internal implementation diagnostics MAY be more granular than externally reported rejection codes.

Externally visible rejection codes SHOULD conform to the published AGCP registries.

---

# 12. Implementation Checklist

A conformant implementation should ensure that:

- governance progression is deterministic;
- platform and governance evaluation responsibilities remain separated;
- Governance Evidence is generated consistently;
- governance-significant events are recorded in the ordered Append-Only Governance Ledger;
- Canonical State is reproducible from ordered ledger history;
- Commit Boundary determines current Canonical State immediately before governed execution;
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
