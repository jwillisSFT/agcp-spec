# DS-035 Bind Set Update

**Schema:** `bind_set.json`  
**DS identifier:** DS-035  
**Catalog version:** 1.0.16  
**RTM version:** RTM-1.20  

## Purpose

DS-035 defines the complete candidate collection of governed sub-transitions evaluated as a coordinated governance unit. It preserves parent and sub-transition identity, targets, Tenant and governance-domain binding, authority domains, explicit coupling semantics, DS-036 dependency-graph binding, aggregate-effect basis, and partial-binding policy.

## Separation of concerns

A Bind Set does not establish authority, authorize execution, determine Partial-Bind Admissibility, or identify an approved executable subset. Those determinations require their own governance results.

## Integration changes

- DS-021 now uses DS-035 for `candidate_bind_set_ref` and `partial_binding_policy`.
- DS-036 now uses the canonical DS-035 Bind Set reference.
- DS-001 delegates the Bind Set reference in Governance Binding to DS-035 and no longer contains duplicate `bind_set_id` or `bind_set_ref` definitions.
- OpenAPI exposes `BindSet` and `BindSetRef`.
- RTM mappings were added for CR-105, CR-108, and CR-109.
