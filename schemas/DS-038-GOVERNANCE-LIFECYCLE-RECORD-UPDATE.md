# DS-038 - Governance Lifecycle Record Update

**Status:** Updated for the AGCP v2.1.x GDF/PDP -> Execution Authorization -> Governance Realization -> PEP architecture synchronization.  
**Date:** 2026-10-03  
**Schema:** `governance_lifecycle_record.json`

## Changes in this update

- Adds COMMITTED lifecycle state and separates COMMITMENT_ACCEPTED from EXECUTION_COMPLETION.

## Compatibility and authority

The frozen CR set is unchanged. This schema update realizes obligations already expressed by the revised Core and Normative Statements; it does not create a new CR. Deployment-specific identity-store or PEP product details remain controlled by Implementation Profiles and referenced IAS/PEP Profiles.
## v2.1.x commitment/execution lifecycle clarification

The lifecycle now distinguishes commitment acceptance from later operational execution completion. `COMMITMENT_ACCEPTED` transitions to nonterminal `COMMITTED` with `commitment_eligibility=COMMITTED_AWAITING_EXECUTION_OUTCOME` and consumed execution authorization. A later `EXECUTION_COMPLETION` transitions `COMMITTED` to terminal `EXECUTED`; `EXECUTION_FAILURE` transitions to terminal `EXECUTION_FAILED`. `COMMITMENT_AND_EXECUTION` remains available for implementations where commitment and execution complete atomically.

