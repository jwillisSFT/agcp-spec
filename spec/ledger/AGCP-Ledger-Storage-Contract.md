# AGCP Ledger Storage Contract Specification v0.9.0

## 1. Purpose

This document defines the storage-layer contract required for the Append-Only Ledger used by the Governance Control Plane Architecture (AGCP).

The ledger is the authoritative record of governance stage entries. All lifecycle state derivation and ordering guarantees depend on the properties defined in this specification.

This contract specifies:

- Stage entry persistence semantics
- Ordering guarantees
- Immutability requirements
- Concurrency behavior
- Sequence assignment enforcement
- Integrity constraints required for deterministic lifecycle derivation

This specification is normative for any implementation claiming AGCP conformance.

---

## 2. Ledger Responsibilities

The append-only ledger MUST provide the following guarantees:

1. Append-only semantics
2. Per-action total ordering
3. Immutable stage entries
4. Deterministic retrieval
5. Tenant isolation
6. Sequence enforcement

The ledger does not derive lifecycle state. Lifecycle state is derived by the Lifecycle Derivation Engine using stage entries retrieved from the ledger.

---

## 3. Stage Entry Structure

Each recorded entry MUST contain the following fields.

### StageEntry


tenant_id
action_id
sequence_value
stage_identifier
evaluation_result
configuration_version
timestamp_metadata (optional)
stage_payload (optional)


### Required Fields

**tenant_id**  
Logical tenant identifier.

**action_id**  
Identifier representing a single governed action instance.

**sequence_value**  
Monotonically increasing ordering value scoped to a specific action_id.

**stage_identifier**  
Identifier representing the stage within the deterministic evaluation pipeline.

**evaluation_result**  
Result produced by execution of the stage.

**configuration_version**  
Identifier representing the configuration version under which evaluation occurred.

---

## 4. Append-Only Guarantee

Once written, a stage entry MUST NOT be:

- modified
- deleted
- reordered

Permitted operations are limited to:

- append
- read
- integrity verification

Updates to historical entries are prohibited.

---

## 5. Ordering Guarantees

Ordering is determined exclusively by sequence_value.

For each action_id:


sequence_value(N+1) > sequence_value(N)


Implementations MAY additionally enforce:


sequence_value(N+1) = sequence_value(N) + 1


This optional rule is known as gapless sequencing.

Timestamp fields MUST NOT be used as authoritative ordering signals.

---

## 6. Sequence Assignment Requirements

Sequence assignment MUST guarantee single total ordering per action identifier.

The sequence assignment mechanism MUST ensure:


For any action_id:
only one entry may exist with sequence_value = N


Attempts to insert entries that violate ordering MUST be rejected.

Possible implementations include:

- atomic counters
- database sequence primitives
- distributed consensus counters
- monotonic counters
- serialized write pipelines

---

## 7. Concurrency Constraints

Concurrent writes affecting the same action_id MUST NOT produce:

- duplicate sequence values
- skipped sequence values (if gapless mode enabled)
- non-deterministic ordering

The storage system MUST enforce write serialization per action identifier.

---

## 8. Tenant Isolation

Ledger entries MUST be logically partitioned by tenant_id.

Isolation guarantees include:

- read isolation
- write isolation
- lifecycle derivation isolation

Cross-tenant access is permitted only if validated through a Cross-Tenant Trust Artifact.

---

## 9. Retrieval Semantics

The ledger MUST support deterministic retrieval using the following query pattern:


SELECT *
FROM ledger
WHERE tenant_id = ?
AND action_id = ?
ORDER BY sequence_value ASC


The returned result MUST represent the complete ordered stage history for the action.

No additional filtering or ordering may alter lifecycle derivation semantics.

---

## 10. Immutability Enforcement Mechanisms

Implementations MAY enforce immutability using any of the following mechanisms:

- database append-only tables
- write-once storage
- cryptographic chaining of stage entries
- storage-layer immutability flags
- blockchain-style ledger systems
- event stores

The implementation mechanism is not mandated provided immutability is preserved.

---

## 11. Deterministic Replay Support

Deterministic replay requires that the ledger preserve:

- exact sequence ordering
- original configuration version
- evaluation outcomes

Replay MUST produce identical lifecycle state when executed under the same configuration version.

---

## 12. Failure and Retry Handling

If a stage evaluation fails after a stage entry has been written:

- the entry remains immutable
- retries must append new stage entries
- lifecycle state remains derived from ordered stage history

Rollback of stage entries is prohibited.

---

## 13. Storage Technology Independence

The ledger contract is implementation agnostic.

Permitted implementations include:

- relational databases
- distributed logs
- event sourcing systems
- blockchain-style ledgers
- append-only object stores

The required behavior is defined by the contract, not the storage engine.

---

## 14. Conformance Requirements

An implementation claiming AGCP conformance MUST satisfy all of the following:

- append-only stage entry storage
- deterministic ordering using sequence values
- per-action total ordering guarantees
- immutable stage entries
- deterministic retrieval
- tenant isolation enforcement

Violation of these guarantees invalidates lifecycle derivation correctness.

---

## 15. Relationship to Other Specifications

This document defines storage requirements for the following AGCP components:

- Deterministic Evaluation Pipeline
- Lifecycle Derivation Engine
- Execution Authorization Generator
- Deterministic Replay Mechanisms

The ledger storage contract operates as a foundational control-plane component.

---

## Version

AGCP Ledger Storage Contract Specification  
Version 0.9.0

---

## Status

Normative specification.

---

## Change History

Version 0.9.0  
Initial release — Ledger storage contract specification.

---

## References

- AGCP Core Specification
- AGCP Lifecycle Derivation Model
- AGCP Control-Plane Invariant Registry
