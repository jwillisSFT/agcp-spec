# DS-022 Governance Context Envelope Update

DS-022 is the authoritative canonical Governance Context Envelope schema for AGCP v2.0.

## Separation from DS-021

- DS-021 owns the Governed Action Proposal.
- DS-022 owns the proposal-associated Governance Context Envelope.
- DS-021 references DS-022 directly and no longer embeds a duplicate context definition.

## Principal controls

DS-022 provides stable Proposal Identity binding, Tenant and governance-domain attribution, versioning, digest protection, context qualification, attributable updates, operational and governance lineage, handoff records, evidence and delegation references, Canonical State reference-only semantics, lifecycle and outcome relationships, and bounded coordination context. Context entries are explicitly classified as `NON_AUTHORITATIVE_CONTEXT`.

Cross-object equality and binding checks that JSON Schema cannot express remain semantic Proposal Qualification obligations.
