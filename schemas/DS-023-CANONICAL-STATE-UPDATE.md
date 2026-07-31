# AGCP DS-023 Canonical State Implementation Report

## Result

`schemas/canonical_state.json` has been implemented as `DS-023`, the canonical domain schema for qualified and resolved Canonical State.

## Architectural boundaries

DS-023 represents one authoritative governance-state basis for a defined evaluation horizon. It explicitly distinguishes Canonical State from Governance Context, telemetry, runtime observations, local application state, inferred state, and agent belief.

The schema does not assume that the Governance Ledger originates every governance-relevant fact. It treats the ledger as authoritative for recorded governance events, event ordering, and Derived Lifecycle State, while permitting other qualified authoritative sources such as identity systems, entitlement systems, policy registries, asset repositories, application systems of record, evidence repositories, and lifecycle registries.

## Required structure

DS-023 requires:

- stable Canonical State identity and version;
- Tenant and governance-domain binding;
- a defined evaluation horizon;
- at least one qualified authoritative source observation;
- deterministic single-state resolution;
- typed state components and integrity digests;
- successful State Qualification for freshness, provenance, completeness, consistency, integrity, availability, and ordering suitability;
- a non-timestamp-only ordering basis;
- attribution and replay-support material.

## State Qualification

The State Qualification result previously embedded in DS-023 has been extracted into implemented `DS-032 state_qualification_result.json`. DS-023 now references DS-032 and permits only the `QUALIFIED` outcome.

## Relationship-specific RTM synchronization

RTM-1.10 maps DS-023 to:

- CR-048 — Canonical State Unavailable;
- CR-049 — Stale Canonical State;
- CR-050 — Conflicting Canonical-State Sources;
- CR-051 — Telemetry Conflicts With Canonical State;
- CR-103 — State Qualification Prior to Admissibility.

Broader requirements that merely consume Canonical State at decision, authorization, continuation, or commitment were not mapped prematurely; those mappings should be added when their consuming schemas are updated to reference DS-023.

## OpenAPI synchronization

The OpenAPI 3.1 component catalog now exposes:

- `CanonicalState` -> `../schemas/canonical_state.json`;
- `CanonicalStateRef` -> `../schemas/common.json#/$defs/canonical_state_ref`.

No interface endpoint was changed to transmit the full object where the current contract only requires a reference.

## Validation

- Draft 2020-12 metaschema validation: PASS
- Cross-schema reference resolution: PASS
- Qualified Canonical State positive test: PASS
- Missing source rejection: PASS
- Unqualified state rejection: PASS
- Timestamp-only ordering rejection: PASS
- Unresolved state rejection: PASS
- Derived Lifecycle State without ledger position rejection: PASS
- Non-authoritative observation authority escalation rejection: PASS
- Resolved conflict without a conflict record rejection: PASS
- Catalog, OpenAPI, RTM, and archive synchronization: PASS
