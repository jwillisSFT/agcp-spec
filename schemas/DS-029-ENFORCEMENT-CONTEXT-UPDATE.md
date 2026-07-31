# DS-029 Enforcement Context Update

DS-029 externalizes the integrity-protected enforcement-facing projection assembled immediately before Policy Enforcement Point mediation. It consumes the qualified and validated results from DS-030 through DS-037 and preserves Proposal Identity, decision, authorization, authority, evidence, target, Tenant, policy, Canonical State, lifecycle, scope, validity, Governance Version, resulting-state, and composite bind conditions.

## Integration changes

- DS-018 now carries the canonical DS-029 Enforcement Context rather than an unconstrained execution context.
- DS-019 records the DS-029 Enforcement Context reference and PEP enforcement result.
- DS-020 may preserve DS-029 references as Governance Evidence.
- DS-027 and DS-028 use the DS-029 enforcement-result definition.
- Superseded Enforcement Context and enforcement-result definitions were removed from `common.json`.

## Normative mapping

- CR-119 Enforcement Context Availability
- CR-120 Enforcement Decision Integrity
- CR-121 Governance Enforcement Binding
