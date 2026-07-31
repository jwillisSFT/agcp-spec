# DS-004 Tenant Governance Record Update

Date: 2026-07-30

## Result

Updated `tenant.json` as the canonical, attributable, versioned, integrity-protected Tenant governance record for AGCP v2.0.

## Authoritative Tenant state

DS-004 now records a stable Tenant record identity and version, authoritative Tenant operational state, authoritative Tenant-state version, current state-transition reference, operational eligibility, and a complete attributable state history.

State history entries include transition identity and sequence, prior and resulting state and versions, transition kind, governance basis, effective and recorded times, Governance Ledger reference, Governance Evidence, attribution, predecessor-chain integrity, and transition digest. History is explicitly append-only and replayable.

## Governance Configuration history

The schema preserves the current active DS-041 Governance Configuration where applicable and a complete configuration-version history. Each history entry records configuration identity, version and digest, Governance Version, DS-043 Controlled Governance Activation, effective interval, status, Governance Ledger reference, Governance Evidence, predecessor-chain integrity, and entry digest.

## Tenant and Governance Domain Isolation

DS-004 now explicitly records Tenant and governance-domain isolation for governance configuration, Canonical State, Authority Lineage, Governance Evidence, ledger access, policy resolution, visibility, authority propagation, execution, and evidence commingling. Cross-domain interaction is either prohibited or permitted only through an explicit governed and validated relationship.

## Governance Evidence and integrity

Every Tenant record includes Tenant Governance Evidence, accountable attribution, provenance, complete record digest, cryptographic integrity signature, and deterministic replay material. Unrestricted `metadata` was removed and replaced with bounded namespaced extensions that cannot change canonical governance meaning.

## State-specific validation

Only `ACTIVE` may be operationally eligible. An active Tenant requires an active Governance Configuration, an active configuration-history entry, and verified isolation. `INACTIVE`, `SUSPENDED`, `PROVISIONED`, and `DECOMMISSIONED` are ineligible. A decommissioned Tenant cannot retain a current active configuration reference.

## Clean migration

DS-004 now owns the Tenant state vocabulary. The superseded `common.json#/$defs/tenant_state_enum` definition was removed. No backward-compatibility alias remains.

## Traceability

Schema Catalog version: 1.0.39.
RTM dataset version: RTM-1.42.

DS-004 is mapped to CR-006 and CR-024 through CR-030, covering Tenant operational status and cross-Tenant visibility, authority, commitment, policy-resolution, and Governance Evidence isolation.
