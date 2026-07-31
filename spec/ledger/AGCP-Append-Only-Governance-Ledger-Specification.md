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

Governance Evidence provides the attributable description and integrity basis for each governance event, while the ordered Append-Only Governance Ledger provides authoritative persistence and ordering for recorded governance events and Derived Lifecycle State. Canonical State may incorporate those ledger-governed elements together with facts resolved from other qualified authoritative governance sources.

The ledger records governance events including, but not limited to:

-   Proposal submission
-   Governance Decision
-   Governance Approval and human adjudication
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

## 3. Governance Ledger Authority and Canonical State Use

The ordered Append-Only Governance Ledger SHALL be authoritative for recorded governance events, event ordering, and Derived Lifecycle State.

Canonical State SHALL be deterministically resolved from one or more qualified authoritative governance sources. The Governance Ledger need not be the originating system of record for every governance-relevant fact incorporated into Canonical State.

Where Canonical State incorporates recorded governance events or Derived Lifecycle State, those ledger-derived elements SHALL be interpreted using authoritative ledger sequence order. Timestamps and implementation-specific storage order SHALL NOT establish authoritative event ordering.

Materialized state views, caches, indexes, and other derived representations MAY be used provided they are deterministically reproducible from the applicable qualified authoritative governance sources and do not supersede those sources as the authoritative governance basis.

Implementations SHALL record or reference the qualified authoritative source versions, ledger positions, provenance, and integrity information sufficient to reproduce the Canonical State basis used for an evaluation.

## 4. Governance Ledger Event Representation

Every appended governance record SHALL conform to DS-040, `schemas/governance_ledger_event.json`.

Each Governance Ledger Event SHALL contain the following required top-level properties:

-   `ledger_event_id`
-   `event_version`
-   `record_type`, with value `GOVERNANCE_LEDGER_EVENT`
-   `event_type`
-   `event_category`
-   `ledger_id`
-   `ordering_scope`
-   `ledger_position`
-   `tenant_id`
-   `governance_domain_id`
-   `event_subject`
-   `event_artifact_refs`
-   `governance_basis`
-   `evidence_binding`
-   `causality`
-   `event_time`
-   `append_status`, with value `APPENDED`
-   `append_only_controls`
-   `integrity_protection`
-   `attribution`
-   `provenance`
-   `replay_material`
-   `semantic_assertions`
-   `event_uri`

Conditional correction and retention information SHALL be represented only through the DS-040 `correction_record` and `retention_record` structures. Extension content SHALL be confined to `namespaced_extensions` as permitted by DS-040.

Legacy pre-DS-040 scalar ledger-entry fields SHALL NOT be used as substitutes for the DS-040 Governance Ledger Event representation.

## 5. Event Subject and Artifact Binding

The governance-significant subject of an event SHALL be identified through `event_subject`.

Referenced governance artifacts SHALL be represented through `event_artifact_refs`, including the required primary artifact URI and digest and the applicable typed artifact reference defined by DS-040.

A generic artifact type plus untyped artifact reference SHALL NOT replace the typed DS-040 artifact-binding structure.

## 6. Append-Only Guarantee

After a Governance Ledger Event has been appended, the event SHALL NOT be modified, deleted during its applicable retention period, silently replaced, or reordered.

The event's `append_only_controls` SHALL assert the required append-only and immutability properties. A correction SHALL be recorded by appending a subsequent `LEDGER_CORRECTION_RECORDED` event that preserves the original event and satisfies the DS-040 correction conditions.

Permitted operations are limited to append, deterministic retrieval, integrity verification, and governed retention processing represented through DS-040.

## 7. Ordering Scope and Ledger Position

Authoritative ordering SHALL be established within the explicit stream identified by `ordering_scope` and `ledger_position`.

Within the same `ledger_id` and `stream_id`:

    ledger_position.sequence(N+1) > ledger_position.sequence(N)

A genesis event SHALL use sequence `0` and SHALL NOT claim a predecessor event or previous event digest.

A non-genesis event SHALL use sequence `1` or greater and SHALL identify both `predecessor_event_id` and `previous_event_digest` in `ledger_position`.

The `ledger_position.event_id` SHALL identify the same event as `ledger_event_id`. Event, chain, and predecessor digests SHALL be represented through the DS-040 digest structures.

Timestamps, arrival order, storage order, node identity, transport behavior, and implementation scheduling SHALL NOT be authoritative ordering signals.

## 8. Append and Sequence Assignment

Sequence assignment SHALL guarantee one deterministic total order within each declared ordering scope.

No two Governance Ledger Events within the same `ledger_id` and `stream_id` SHALL share the same `ledger_position.sequence`.

Sequence reuse and unauthorized reordering SHALL be prohibited. A successfully appended event SHALL carry `append_status: APPENDED` and a `ledger_position` representing the event's authoritative stream position.

## 9. Concurrency

Concurrent appends SHALL NOT produce duplicate sequence positions, duplicate event identities, broken predecessor bindings, or non-deterministic ordering within the same declared ordering scope.

Implementations SHALL serialize or equivalently coordinate appends for a given `ledger_id` and `stream_id` while preserving any explicit cross-stream causality represented by DS-040.

## 10. Isolation

Governance Ledger Events SHALL remain isolated by `tenant_id` and `governance_domain_id`.

The declared `ordering_scope`, event subject, artifact references, governance basis, evidence binding, attribution, and provenance SHALL preserve the applicable tenant and governance-domain bindings.

Cross-boundary access or causality SHALL require explicit governed authorization and SHALL NOT weaken tenant or governance-domain isolation.

## 11. Deterministic Retrieval

Implementations SHALL support deterministic retrieval of Governance Ledger Events by applicable ledger, stream, ordering scope, event identity, proposal identity, tenant, governance domain, and other supported DS-040 reference attributes.

Retrieval SHALL preserve authoritative `ledger_position.sequence` ordering within the requested scope and SHALL return the DS-040 event representation or a verifiable projection that preserves its semantics.

## 12. Governance Basis, Evidence Binding, and Causality

Each Governance Ledger Event SHALL preserve the governance basis applicable to that event through `governance_basis`.

Associated Governance Evidence SHALL be bound through `evidence_binding.governance_evidence_refs`. Evidence references SHALL remain resolvable and integrity-verifiable, and Evidence Continuity SHALL be preserved.

Causal, parent, and dependency relationships among Governance Ledger Events SHALL be represented through the DS-040 `causality` structure using DS-040 Governance Ledger Event references.

A Governance Ledger Event reference SHALL use the DS-040 reference representation, including `ledger_event_id`, `event_version`, `event_type`, `event_category`, `ledger_position`, tenant and governance-domain identity, `event_digest`, and `appended_at`, together with `proposal_id` and `event_uri` where applicable.

## 13. Integrity and Provenance

Every Governance Ledger Event SHALL carry `integrity_protection`, `attribution`, and `provenance` structures conforming to DS-040.

Integrity protection SHALL cover event content, ledger position, artifact references, and evidence references and SHALL preserve predecessor binding for non-genesis events.

Implementations SHALL support detection of unauthorized mutation, substitution, deletion, predecessor detachment, reference substitution, and reordering.

The specific cryptographic algorithms and storage technologies remain implementation-defined where not otherwise constrained, but the externally observable DS-040 integrity semantics SHALL be preserved.

## 14. Replay Material and Semantic Assertions

Every Governance Ledger Event SHALL contain the DS-040 `replay_material` and `semantic_assertions` required to support deterministic reconstruction of governance reasoning and verification.

Replay material SHALL preserve or bind the ordered event content, governance basis, artifact-reference set, evidence-reference set, causality, and ledger-chain digests.

Replay SHALL reconstruct governance reasoning and verification; it SHALL NOT re-execute the historical operational action.

Semantic assertions SHALL preserve, at minimum, append-only behavior, authoritative ordering within the declared scope, tenant and domain isolation, reference resolvability, provenance-chain continuity, non-authorizing event semantics, and correction by subsequent event rather than mutation.

## 15. Relationship to Canonical State

Where Canonical State incorporates recorded governance events or Derived Lifecycle State, those elements SHALL be interpreted from applicable DS-040 Governance Ledger Events in authoritative `ledger_position.sequence` order together with their evidence bindings and qualified governance basis.

Other Canonical State facts SHALL continue to be resolved from their applicable qualified authoritative governance sources. A Governance Ledger Event SHALL NOT replace those sources, independently establish authority at commitment, authorize execution, or commit a referenced transition merely by recording or referencing it.

## 16. Failure and Correction Handling

Failed governance processing SHALL NOT modify previously appended Governance Ledger Events.

A retry or later governance event SHALL be represented by a new DS-040 event with its own `ledger_event_id`, ledger position, governance basis, evidence binding, causality, integrity protection, attribution, and provenance.

An error in an appended event SHALL be corrected only through a subsequent DS-040 correction event. Rollback, in-place mutation, identifier reuse, sequence reuse, and silent replacement of an appended event are prohibited.

## 17. Storage Independence

The DS-040 representation and externally observable ledger behavior are normative; the storage technology is not.

Permissible implementations include relational databases, append-only logs, event stores, immutable object stores, blockchain-style ledgers, and write-once storage, provided they preserve the complete DS-040 semantics.

## 18. Conformance

A conformant implementation SHALL demonstrate:

-   DS-040-valid Governance Ledger Events;
-   append-only and immutable event history;
-   deterministic ordering by `ordering_scope` and `ledger_position.sequence`;
-   valid genesis and predecessor-binding behavior;
-   deterministic retrieval;
-   tenant and governance-domain isolation;
-   typed event-subject and artifact binding;
-   governance-basis and evidence binding;
-   causality preservation;
-   integrity protection, attribution, and provenance;
-   replay-material completeness; and
-   correction by subsequent event rather than mutation.

## 19. Relationship to Other Specifications

This specification complements:

-   AGCP Core Specification
-   DS-040 Governance Ledger Event schema
-   AGCP Security Specification
-   AGCP Provenance Wire Format Specification
-   AGCP Human Review Specification
-   Policy Evaluation Contract (PEC)
-   AGCP HTTP Interface Specification

## 20. Repository Versioning

Repository releases govern versioning of this specification.
