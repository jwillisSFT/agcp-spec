# DS-021 Governed Action Proposal Implementation Report

## Artifacts

- Canonical domain schema: `DS-021 governed_action_proposal.json`
- Transport wrapper: `DS-013 proposal_submit_request.json`
- Catalog version: `1.0.3`
- RTM dataset version: `RTM-1.8`
- Date: 2026-07-29

## Architectural separation

DS-021 now owns the governance-domain representation of a proposed transition: Proposal Identity, originating Tenant and governance domain, operational intent, target, requested effect, validity, policy inputs, canonical Action Representation, Governance Context, provenance, and composite-proposal semantics.

DS-013 now contains only the required `proposal` reference plus optional submission time, client correlation, and namespace-qualified transport extensions. The previous flattened DS-013 shape is intentionally no longer normative.

## Composite governance

DS-021 preserves the existing conditional rules:

- `COMPOSITE` proposals require the composite structure.
- `SIMPLE` proposals prohibit the composite structure.
- Composite proposals contain governed sub-transition identities, dependency graph, coupling semantics, partial-binding policy, and aggregate-effect digest.

## Canonical context dependency

DS-022 `governance_context_envelope.json` is now implemented as the authoritative context domain object. DS-021 references DS-022 directly and no longer embeds a duplicate Governance Context Envelope definition.

## Semantic validation obligations

Standard JSON Schema cannot compare arbitrary values across object locations. Proposal Qualification must therefore verify equality and binding among top-level Tenant/domain values, Proposal Identity, Governance Context, targets, digests, and parent/sub-transition identities.

## Traceability

DS-021 inherits the semantically reviewed proposal mappings formerly represented solely by DS-013. RTM-1.8 adds DS-021 to those 18 records and adds the new repository path while retaining DS-013 for the transport contract.

## HTTP contract synchronization

The OpenAPI 3.1 contract now references the authoritative DS-013 and DS-021 files rather than retaining a conflicting embedded flattened ProposalSubmitRequest definition. Its pipeline summary was also aligned so Continuation Integrity precedes final Governance Realization and Commit Boundary processing for applicable nonterminal proposals.

## Validation summary

- JSON Schema Draft 2020-12 structural validation: PASS
- Cross-schema reference resolution: PASS
- Simple proposal positive vector: PASS
- Composite proposal positive vector: PASS
- DS-013 transport-wrapper positive vector: PASS
- Negative structural and extension tests: PASS
- OpenAPI 3.1 external schema references: PASS
- RTM-1.8 DS/path synchronization across 18 records: PASS
- RTM workbook formatting preservation: PASS
## DS-035 extraction

Composite proposals now reference `bind_set.json#/$defs/bind_set_ref` and `bind_set.json#/$defs/partial_binding_policy`. The transitional local `partial_binding_policy` definition was removed from DS-021.
