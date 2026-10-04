# DS-018 - Commit Boundary Request Update

**Status:** Updated for the AGCP v2.1.x GDF/PDP -> Execution Authorization -> Governance Realization -> PEP architecture synchronization.  
**Date:** 2026-10-03  
**Schema:** `commit_boundary_request.json`

## Changes in this update

- Recasts the public commit request as an invocation of Governance Realization. Removes caller-supplied authoritative commitment-time state, authority, binding validation, Enforcement Context, PEP selection, and PEP identity.

## Compatibility and authority

The frozen CR set is unchanged. This schema update realizes obligations already expressed by the revised Core and Normative Statements; it does not create a new CR. Deployment-specific identity-store or PEP product details remain controlled by Implementation Profiles and referenced IAS/PEP Profiles.
