# DS-030 Governance Binding Validation Result Update

## Status

Implemented on 2026-07-29.

## Canonical artifact

- DS ID: `DS-030`
- Filename: `governance_binding_validation_result.json`
- Canonical URI: `https://agcp.ai/schemas/governance_binding_validation_result.json`

## Purpose

DS-030 records whether the governance binding originally evaluated remains intact immediately before enforcement and commitment. The result compares proposal identity, decision, authorization, current authority, evidence, target, Tenant, governance domain, policy, qualified Canonical State, Derived Lifecycle State, scope, validity, Governance Version, and applicable composite bind conditions.

## Outcome semantics

- `VALID`: Enforcement Context assembly may proceed.
- `INVALID`: Structural Refusal is required.
- `RE_EVALUATION_REQUIRED`: affected governance determinations must be renewed.
- `INDETERMINATE`: required inputs cannot be resolved and processing is blocked.

DS-030 does not itself establish authority, authorize execution, apply enforcement, or commit a transition.
