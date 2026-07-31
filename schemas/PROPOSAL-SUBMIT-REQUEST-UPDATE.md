# Proposal Submit Request Schema Update

## Artifact

- DS identifier: `DS-013`
- Filename: `proposal_submit_request.json`
- Catalog version: `1.0.42`
- SHA-256: `b4d125ca8bf2569b30b020fc304b145a0d20fc0253d52bb5818768b2c3e18883`
- Date: 2026-07-30

## Current normative model

DS-013 is the transport-only submission wrapper for one canonical DS-021 Governed Action Proposal. The required `proposal` member carries the domain object. Optional transport-envelope members are limited to `submitted_at`, `client_request_id`, and `extensions`.

The `extensions` member is the sole namespace-qualified extension container. Extension members SHALL NOT alter, replace, or weaken the canonical Governed Action Proposal carried in `proposal`.

## Obsolete-field removal

The deprecated top-level `metadata` compatibility member has been removed from the active schema. Because the schema sets `additionalProperties` to `false`, payloads that continue to submit a top-level `metadata` member are invalid and must migrate that content to `extensions`.

No active OpenAPI operation, conformance fixture, or harness mapping depends upon the removed member.

## DS-021 relationship

The authoritative proposal domain object remains DS-021 `governed_action_proposal.json`. DS-013 does not duplicate or redefine DS-021 governance-domain fields and does not confer authority at commitment.
