# AGCP DS-025 Delegation Artifact Implementation Report

## Result

`schemas/delegation_artifact.json` has been implemented as `DS-025`, the canonical domain schema for independently verifiable delegated-authority artifacts.

## Architectural boundary

DS-025 is immutable evidence of bounded delegation. It does not constitute unconditional authority at commitment or permission to execute. Current authority, revocation, expiration, subject eligibility, target eligibility, and commit-time admissibility remain re-derived from current qualified Canonical State and other qualified governance inputs.

## Required semantics

DS-025 requires:

- originating, delegating, and receiving principals;
- source and target governance-domain binding;
- source-authority provenance and parent-delegation reference where applicable;
- source and delegated scopes;
- an attributable scope-containment assertion;
- proposal-specific or bounded-standing binding;
- validity constraints;
- authoritative revocation lookup controls;
- recursive-delegation depth and attenuation controls;
- Governance Version and policy references;
- Canonical State reference at issuance;
- attributable issuance evidence;
- cryptographic or equivalent independent verification material;
- evidence references and an artifact digest.

Cross-domain delegation requires an approved escalation artifact, qualified trust relationship, transition policy, and transition evidence. Same-domain artifacts cannot carry the cross-domain governance block.

## DS-022 integration

The transitional Delegation Artifact reference definition was removed from `governance_context_envelope.json`. DS-022 now references:

`delegation_artifact.json#/$defs/delegation_artifact_ref`

## Relationship-specific RTM synchronization

RTM-1.11 maps DS-025 to:

- CR-040 — Malformed Delegation References;
- CR-042 — Canonical Hash Mismatch;
- CR-044 — Broken Delegation Chain;
- CR-045 — Conflicting Originating Actor;
- CR-047 — Provenance Continuity Gap;
- CR-072 — Cross-Domain Delegation Requires Escalation;
- CR-115 — Recursive Authority Containment.

## Validation

- Draft 2020-12 metaschema validation: PASS
- Cross-schema reference resolution: PASS
- Same-domain delegation positive test: PASS
- Cross-domain approved escalation positive test: PASS
- Missing verification material rejection: PASS
- Artifact-as-execution-authority rejection: PASS
- Invalid recursive depth rejection: PASS
- Delegated source without parent rejection: PASS
- Proposal-specific binding without Proposal Identity rejection: PASS
- Cross-domain delegation without governed escalation rejection: PASS
- Same-domain artifact with cross-domain block rejection: PASS
- Disabled revocation checking rejection: PASS
- Catalog, OpenAPI, RTM, DS-022 dependency, and archive synchronization: PASS
