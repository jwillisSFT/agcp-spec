# AGCP Architecture Overview

Status: Informational  
Version: 0.9.0  
Category: Architectural Overview  

This document provides a high-level description of the Governance Control Plane (AGCP) architecture.  
It is intended to orient readers and implementers before they review the normative specification documents.

Normative requirements are defined in the specifications located under the `spec/` directory.

---

# 1. Architectural Model

AGCP defines a **deterministic governance control plane** for automated systems.

The core principle of AGCP is that **execution eligibility is derived from canonical system state rather than mutable authorization flags**.

Execution authority is therefore determined by evaluating:

1. Governance policy
2. Deterministic constraints and invariants
3. Human-in-the-loop authorization when required
4. Canonical ledger state

This evaluation occurs **before an action is permitted to commit**.

---

# 2. Control Plane Responsibilities

The AGCP control plane is responsible for:

- validating governance envelopes
- verifying provenance
- resolving applicable policy modules
- evaluating policy constraints
- enforcing invariants
- coordinating human-in-the-loop approval
- deriving lifecycle state
- recording all governance decisions in an append-only ledger

The control plane does **not perform execution itself**.  
Instead it determines whether execution is permitted.

---

# 3. Deterministic Evaluation Pipeline

All actions submitted to AGCP pass through a fixed evaluation pipeline:


SCHEMA_VALIDATION
PROVENANCE_VERIFICATION
TENANT_STATE_VALIDATION
POLICY_RESOLUTION
PEC_CONSTRAINTS
PEC_INVARIANTS
PEC_HITL
DECISION
EXECUTION_AUTHORIZED
EXECUTION_COMMITTED


The ordering of these stages is deterministic and MUST NOT be altered.

---

# 4. Ledger Model

AGCP uses an append-only governance ledger.

Each evaluation stage produces a ledger entry that records:

- stage identifier
- evaluation result
- supporting metadata

Lifecycle state is derived from ledger history rather than stored as mutable state.

This ensures that system behavior is:

- deterministic
- replayable
- auditable

---

# 5. Lifecycle Model

The externally observable action states are:


REJECTED
PENDING_HITL
AUTHORIZED
EXECUTED


The internal state `SUBMITTED` is transient and MUST NOT be returned by canonical retrieval endpoints.

Lifecycle state transitions are defined in:


lifecycle/


---

# 6. Human-in-the-Loop Authorization

Certain actions may require explicit human authorization.

In these cases AGCP enters the state:


PENDING_HITL


Authorized principals may submit **cosign tokens**.

Once the required quorum is satisfied the system records:


EXECUTION_AUTHORIZED


---

# 7. Execution Commit

Execution of an action is permitted only if:

1. the action is in state `AUTHORIZED`
2. the authorization reference matches the ledger
3. provenance validation succeeds
4. tenant state is valid

Successful execution produces the ledger stage:


EXECUTION_COMMITTED


---

# 8. Multitenant Isolation

AGCP supports multi-tenant deployments.

All operations are tenant-scoped and implementations MUST enforce:

- tenant-scoped policy resolution
- tenant-scoped key lookup
- tenant-scoped ledger queries

Cross-tenant access MUST be rejected.

---

# 9. Repository Structure


agcp-spec/


The repository is organized into the following primary directories.

| Directory | Purpose |
|---|---|
| `spec/` | Normative specification documents |
| `lifecycle/` | Action lifecycle model |
| `schemas/` | JSON schema definitions |
| `registries/` | Enumerated registries |
| `conformance/` | Conformance testing artifacts |
| `api/` | OpenAPI interface specification |
| `reference/` | Informational reference materials |
| `governance/` | Specification governance process |
| `diagrams/` | Architecture diagrams |

---

# 10. Specification Documents

The normative AGCP specification consists of the documents under:


spec/


These define the authoritative protocol requirements for AGCP implementations.
