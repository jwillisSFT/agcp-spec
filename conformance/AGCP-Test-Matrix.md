# AGCP Conformance Test Matrix

Version: 0.9.0

This document provides a human-readable mapping between:

Requirements → Assertions → Conformance Tests

The canonical machine-readable mapping is:

/conformance/test-mapping.json

---

# Conformance Traceability Model

AGCP conformance verification uses the following structure:

Specification  
↓  
Assertion  
↓  
Requirement  
↓  
Test Vector

All normative requirements MUST be covered by at least one conformance test.

---

# Test Matrix

| Requirement ID | Assertion | Test Vectors |
|----------------|-----------|--------------|
| REQ-COMMIT-APPENDS-COMMITTED | A-COMMIT-GATING | TV-COM-001 |
| REQ-COMMIT-AUTH-REF-MATCH | A-COMMIT-GATING | TV-COM-004 |
| REQ-COMMIT-ONLY-AUTHORIZED | A-COMMIT-GATING | TV-COM-002, TV-COM-003 |
| REQ-COMMIT-REPLAY-REJECT | A-TERMINAL-NO-TRANSITION | TV-COM-005 |
| REQ-COMMIT-TENANT-INACTIVE | A-TENANT-ACTIVE-GATING | TV-COM-006 |
| REQ-COSIGN-ONLY-PENDING | A-COSIGN-GATING | TV-COS-003, TV-COS-006 |
| REQ-COSIGN-QUORUM-AUTH | A-COSIGN-GATING | TV-COS-002 |
| REQ-COSIGN-VALIDITY | A-COSIGN-GATING | TV-COS-004, TV-COS-005 |
| REQ-CROSS-TENANT-PROFILE | A-TENANT-ACTIVE-GATING | TV-XTEN-SETUP, TV-XTEN-001, TV-XTEN-002, TV-XTEN-003 |
| REQ-STATE-DERIVED-FROM-LEDGER | A-DERIVATION | Multiple tests |
| REQ-STATE-NO-SUBMITTED | A-STATE-NO-SUBMITTED | Multiple tests |
| REQ-LEDGER-ORDERING | A-ORDERING | TV-COS-002, TV-COM-001 |

---

# Notes

Some assertions are enforced by many tests. These are listed as "Multiple tests" for readability.

The authoritative coverage information is maintained in:

/conformance/test-mapping.json
