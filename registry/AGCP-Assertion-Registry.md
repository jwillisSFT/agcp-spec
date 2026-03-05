# AGCP Assertion Registry
Version: 0.9.0

This document provides a human-readable index of normative assertions.

The canonical machine-readable registry is:

/conformance/assertions.json

---

## Core Assertions

| Assertion ID | Description |
|---------------|-------------|
| A-COMMIT-GATING | Commit allowed only when state=AUTHORIZED and ledger_authorization_ref matches |
| A-COSIGN-GATING | Cosign allowed only when state=PENDING_HITL and token valid |
| A-DERIVATION | Returned state must equal state derived from ledger history |
| A-IDEMPOTENCY-NO-MUTATION | Idempotency conflicts must not mutate ledger |
| A-ORDERING | Ledger stages must be appended in deterministic order |
| A-STATE-NO-SUBMITTED | Canonical responses must not expose SUBMITTED |
| A-TENANT-ACTIVE-GATING | Operations must enforce tenant ACTIVE gating |
| A-TERMINAL-NO-TRANSITION | Terminal states must reject further transitions |

---

## Traceability

Assertions are referenced by:

/conformance/test-mapping.json  
/conformance/AGCP Conformance Harness Spec.yml
