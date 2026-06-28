# AGCP Harness Check Registry

**Status:** Informational  
**Repository Versioning:** Repository Release Governed  
**Canonical Machine-Readable Source:** `/conformance/harness-checks.json` (or `assertions.json` until renamed)

---

# 1. Purpose

This document provides a human-readable registry of the executable Harness Checks used by the AGCP Conformance Harness.

Harness Checks define the executable verification behavior used to realize published Conformance Test Cases (TCs). They are **not** an independent normative layer.

The authoritative normative traceability chain is:

```text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

Harness Checks and Harness Test Vectors provide the executable realization of Test Cases and SHALL remain synchronized with the Requirements Traceability Matrix (RTM).

The canonical machine-readable registry is maintained in:

```text
/conformance/harness-checks.json
```

(or `assertions.json` until the repository rename is completed.)

---

# 2. Harness Check Model

Harness Checks verify that an implementation exhibits the behaviors required by the published specifications.

Each Harness Check defines:

- Harness Check identifier
- Validated capability
- Applicable pipeline stages
- Applicable schemas and registries
- Expected behavior
- Required evidence
- Representative Harness Test Vectors

Harness Checks SHALL NOT introduce independent normative requirements.

---

# 3. Harness Check Registry

| Harness Check ID | Validated Capability |
|------------------|----------------------|
| CHECK-PROPOSAL-QUALIFICATION | Proposal Qualification validation and refusal behavior |
| CHECK-GOVERNANCE-DECISION | Deterministic Governance Decision Function behavior |
| CHECK-HUMAN-REVIEW | Human Review quorum, authorization, replay protection, and validation |
| CHECK-EXECUTION-AUTHORIZATION | Execution Authorization generation and validation |
| CHECK-COMMIT-BOUNDARY | Commit Boundary authorization and governance revalidation |
| CHECK-GOVERNANCE-EVIDENCE | Governance Evidence generation, linkage, integrity, and auditability |
| CHECK-APPEND-ONLY-GOVERNANCE-LEDGER | Ordered Append-Only Governance Ledger behavior |
| CHECK-CANONICAL-STATE | Canonical State reconstruction from ordered ledger history |
| CHECK-IDEMPOTENCY | Idempotent proposal replay behavior |
| CHECK-TENANT-STATE-GATING | Tenant lifecycle state enforcement |
| CHECK-TENANT-AND-DOMAIN-ISOLATION | Tenant and Governance Domain isolation |
| CHECK-PROVENANCE | Provenance verification and replay protection |
| CHECK-REGISTRIES | Registry validation for published governance registries |

---

# 4. Conformance Relationship

Harness Checks are executed as part of the AGCP Conformance Harness.

The complete relationship is:

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

The authoritative NS→CR→TC mappings are maintained by the Requirements Traceability Matrix and `test-mapping.json`.

---

# 5. Scope of Verification

Collectively, the Harness Checks verify:

- Proposal Qualification
- Governance Decision Function
- Human Review
- Execution Authorization
- Commit Boundary
- Governance Evidence
- Ordered Append-Only Governance Ledger
- Canonical State derivation
- Deterministic replay
- Idempotency
- Provenance validation
- Tenant lifecycle enforcement
- Tenant and Governance Domain isolation
- Published governance registries

---

# 6. Relationship to Test Cases

Each Harness Check is exercised through one or more representative Harness Test Vectors.

Representative examples include:

| Harness Check | Representative Harness Test Vectors |
|---------------|-------------------------------------|
| CHECK-PROPOSAL-QUALIFICATION | TV-PROP-001, TV-PROP-002 |
| CHECK-GOVERNANCE-DECISION | TV-GOV-001, TV-GOV-002, TV-GOV-003 |
| CHECK-HUMAN-REVIEW | TV-HR-001, TV-HR-002, TV-HR-003 |
| CHECK-EXECUTION-AUTHORIZATION | TV-AUTH-001, TV-AUTH-002 |
| CHECK-COMMIT-BOUNDARY | TV-CB-001, TV-CB-002, TV-CB-003 |
| CHECK-APPEND-ONLY-GOVERNANCE-LEDGER | TV-LEDGER-001, TV-LEDGER-002, TV-LEDGER-003 |
| CHECK-CANONICAL-STATE | TV-LEDGER-001, TV-LEDGER-002, TV-META-003 |

---

# 7. Canonical Registry

The canonical machine-readable Harness Check Registry contains, for each Harness Check:

- identifier
- validated capability
- applicable pipeline stages
- applicable schemas
- applicable registries (where applicable)
- expected behavior
- required evidence
- representative Harness Test Vectors

The Markdown registry exists solely as a human-readable companion to the machine-readable registry.

---

# 8. Change Control

Harness Check identifiers SHOULD remain stable across repository releases.

New Harness Checks SHOULD be additive.

Harness Checks SHALL remain synchronized with:

- Requirements Traceability Matrix
- Conformance Test Cases
- Harness Test Vectors
- Published specifications

---

# 9. Conformance Claims

An implementation may claim AGCP Conformance only when:

1. Applicable Normative Statements are satisfied.
2. Applicable Conformance Requirements are satisfied.
3. Applicable Test Cases pass.
4. Applicable Harness Checks pass.
5. Applicable Harness Test Vectors execute successfully.

---

# 10. Guidance for Reviewers

When reviewing AGCP conformance:

- Review normative behavior in the published specifications.
- Confirm NS→CR→TC traceability.
- Verify Harness Checks correctly implement published Test Cases.
- Confirm Harness Test Vectors exercise each applicable Harness Check.
- Verify Canonical State reconstruction from the ordered Append-Only Governance Ledger.

---

# 11. Future Expansion

Future repository releases may introduce additional Harness Check domains including:

- Distributed replay verification
- Multi-ledger federation
- Cross-jurisdiction governance
- Distributed Canonical State validation
- Advanced governance analytics

Future additions SHOULD preserve backward compatibility and remain synchronized with the Requirements Traceability Matrix.

---

# Relationship to Other Artifacts

| Artifact | Purpose |
|----------|---------|
| Requirements Traceability Matrix | Authoritative NS → CR → TC mapping |
| Harness Check Registry (JSON) | Machine-readable executable harness definitions |
| AGCP Conformance Test Matrix | Human-readable capability mapping |
| AGCP Conformance Test Vectors | Representative executable scenarios |
| AGCP Conformance Harness Specification | Harness execution behavior |

