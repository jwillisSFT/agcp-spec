# AGCP Append-Only Governance Ledger Specification

**Status:** Normative

## 1. Purpose

This specification defines the mandatory storage contract for the AGCP
Append-Only Governance Ledger.

Every AGCP-conformant implementation SHALL provide an append-only
governance ledger satisfying this specification.

The ledger is the authoritative, immutable record of
governance-significant events and provides the foundation for governance
integrity, deterministic replay, auditability, and evidence
preservation.

The ledger records governance events including, but not limited to:

-   Proposal submission
-   Governance Decision
-   Human Review
-   Execution Authorization
-   Commit Boundary
-   Governance Evidence
-   Administrative governance operations

## 2. Responsibilities

The ledger SHALL provide:

1.  Append-only persistence
2.  Immutable records
3.  Deterministic ordering
4.  Deterministic retrieval
5.  Tenant isolation
6.  Governance Domain isolation (where applicable)
7.  Cryptographic integrity support
8.  Deterministic replay support

## 3. Canonical State Authority

The ordered Append-Only Governance Ledger SHALL be the authoritative source for Canonical State derivation.

Canonical State SHALL be derived exclusively from ledger entries in sequence order, or from a verifiable materialized state whose derivation from the ordered Append-Only Governance Ledger can be deterministically reproduced.

Sequence order, not timestamp order, SHALL determine the authoritative order of governance state transitions.

Materialized state views, caches, indexes, and other derived representations SHALL NOT supersede the ordered Append-Only Governance Ledger as the authoritative governance record.

Implementations SHALL be capable of reproducing the Canonical State from the ordered ledger for deterministic replay, audit, and conformance verification.

## 4. Ledger Entry

Every ledger entry SHALL contain at least:

-   ledger_entry_id
-   tenant_id
-   governance_domain_id (if applicable)
-   sequence_value
-   artifact_type
-   artifact_reference
-   timestamp
-   provenance_reference
-   governance_evidence_reference

Entries MAY additionally include:

-   proposal_id
-   action_id
-   previous_entry_hash
-   implementation metadata

## 5. Append-Only Guarantee

Once committed, a ledger entry SHALL NOT be:

-   modified
-   deleted
-   reordered

Permitted operations are limited to:

-   append
-   read
-   integrity verification

Historical updates are prohibited.

## 6. Ordering

Ordering SHALL be determined exclusively by `sequence_value`.

For a given ledger partition:

    sequence_value(N+1) > sequence_value(N)

Gapless sequencing MAY be implemented but is not required.

Timestamps SHALL NOT be authoritative ordering signals.

## 7. Sequence Assignment

Sequence assignment SHALL guarantee a single deterministic ordering.

No two entries within the same ledger partition SHALL share the same
sequence value.

## 8. Concurrency

Concurrent writes SHALL NOT produce:

-   duplicate sequence values
-   non-deterministic ordering

Implementations SHALL serialize ledger appends for a given partition.

## 9. Isolation

Ledger records SHALL be isolated by tenant.

Where Governance Domains exist, implementations SHALL additionally
isolate records by Governance Domain.

Cross-boundary access SHALL require explicit authorization defined by
applicable governance policy.

## 10. Retrieval

Implementations SHALL support deterministic retrieval preserving append
order.

Retrieval SHALL return the complete ordered governance history for the
requested scope.

## 11. Integrity

Implementations SHALL provide mechanisms to detect unauthorized
modification.

Examples include:

-   cryptographic hashes
-   chained hashes
-   digital signatures
-   write-once storage
-   immutable database features

The specific mechanism is implementation-defined provided integrity is
preserved.

## 12. Governance Evidence

Every governance-significant operation SHALL result in Governance
Evidence.

Ledger entries SHALL reference the associated Governance Evidence.

The Governance Evidence remains the canonical description of the
governance event, while the ledger provides immutable ordering and
preservation.

## 13. Replay

The ledger SHALL preserve sufficient information to support
deterministic replay and governance audit.

Replay SHALL produce identical governance outcomes when evaluated using
the same governance configuration and policy artifacts.

## 14. Failure Handling

Failed governance processing SHALL NOT modify existing ledger entries.

Subsequent retries SHALL append new entries rather than altering
history.

Rollback of committed ledger entries is prohibited.

## 15. Storage Independence

The required behavior is normative; the storage technology is not.

Permissible implementations include:

-   relational databases
-   append-only logs
-   event stores
-   immutable object stores
-   blockchain-style ledgers
-   write-once storage

## 16. Conformance

Conformant implementations SHALL provide:

-   append-only semantics
-   immutable records
-   deterministic ordering
-   deterministic retrieval
-   tenant isolation
-   governance evidence linkage
-   integrity verification
-   deterministic replay support

## 17. Relationship to Other Specifications

This specification complements:

-   AGCP Core Specification
-   AGCP Security Specification
-   AGCP Provenance Wire Format Specification
-   AGCP Human Review Specification
-   Policy Evaluation Contract (PEC)
-   AGCP HTTP Interface Specification

## 18. Repository Versioning

Repository releases govern versioning of this specification.
