# AGCP Normative Governance Progression Table

**Status:** Normative lifecycle companion table  
**Artifact Lifecycle:** Current  
**Repository Release Target:** AGCP v2.1.x

# 1. Purpose

This table restates the controlled progression from proposal through decision, authorization, current Governance Realization, enforcement, commitment, and operational outcome. It does not create obligations beyond the published CRs, Core, and adopted normative companions.

# 2. Governance Progression

| Stage | Primary function | Required basis | Principal output | Non-progression behavior |
|---|---|---|---|---|
| Proposal Qualification | Qualification pipeline | proposal integrity, identity/provenance, schema, Tenant/Domain, required state/evidence | Qualified Proposal or Structural Refusal | no Governance Decision / no effect |
| Governance Decision | Governance Decision Function / PDP | Qualified Proposal, Canonical State, governance, evidence, qualified human/identity-authorization context where applicable | Governance Decision | deny, refuse, review, defer, or re-evaluate as defined |
| Human Adjudication | Human governance path | authenticated subject + IAS-resolved current identity/authorization/entitlement + proposal binding | authoritative Governance Approval Artifact / quorum state | no contribution when identity/authority is unresolved or invalid |
| Execution Authorization | Authorization function | favorable decision and required authority/bindings for the authorization horizon | proposal-bound Execution Authorization | authorization failure / re-evaluation |
| Continuation Integrity | continuation processing | nonterminal lifecycle, current proposal/bindings, material-change triggers | continued viability or governed re-evaluation | suspension / terminal governed outcome |
| Governance Realization | GRF | Execution Authorization, current authority/state/evidence/lifecycle, binding validation, PEP Profile | current Commit-Bound Admissibility + Enforcement Context / protected PEP request | fail closed or governed re-evaluation |
| Enforcement / Commitment | PEP at Commit Boundary | authorized GRF path + valid Enforcement Context + profile-defined bindings | acceptance/refusal of exact transition at commitment | no governed consequence |
| Governed Execution | target / execution adapter | accepted transition and protected target authority | actual operational outcome | execution failure/recovery as defined |
| Evidence / Lifecycle | ledger and evidence functions | all governance-significant milestones | reconstructable evidence and lifecycle state | integrity failure is non-conformance within claimed scope |

# 3. Governance Progression Diagram

```text
Proposal
  -> Qualification
  -> GDF / PDP
  -> Governance Decision
  -> Human Review / re-evaluation when required
  -> Execution Authorization
  -> Continuation Integrity as applicable
  -> GRF / Commit-Bound Admissibility
  -> PEP Profile application + Enforcement Context
  -> PEP / Commit Boundary
  -> Governed Execution
  -> Evidence / Lifecycle
```

# 4. Commit Boundary Decision Matrix

| Condition at commitment | Required result |
|---|---|
| authorization valid, current authority/state/bindings valid, exact PEP mapping available, PEP accepts | transition may commit |
| required identity/entitlement/authority no longer current | no commit; re-evaluate/refuse as defined |
| authorization stale/revoked/consumed | no commit |
| target/action/profile binding mismatch | no commit |
| no faithful supported PEP mapping | no approximate enforcement; no commit |
| PEP unavailable/refuses | no governed target effect |
| commit accepted but target completes asynchronously | record commitment now; record later execution outcome separately |

# 5. Canonical State

Canonical State remains the authoritative governance state selected and qualified under the Core. Identity-system authorization/entitlement data resolved through an IAS Profile may be qualified governance input without becoming Canonical State unless the controlling profile explicitly assigns that fact class to a Canonical State source.

# 6. Governance Evidence

Evidence shall preserve the proposal, decision, authorization, human authority basis when applicable, GRF current-eligibility result, selected PEP Profile reference, Enforcement Context, PEP result, commitment event, and actual target outcome when distinct.

# 7. Relationship to Conformance

Conformance tests may observe each stage separately. A favorable result at an earlier stage does not satisfy a later-stage requirement.

# 8. Relationship to Other Specifications

This table is interpreted with the AGCP Core, Architecture Reference Model, AGCP Trust Model, Human Adjudication and Governance Approval Specification, Policy Evaluation Contract, HTTP Interface Specification, Append-Only Governance Ledger Specification, and the controlling Implementation Profile.

Canonical companion bindings: `../schemas/governance_evidence.json` (DS-020 Governance Evidence), `../schemas/evidence_qualification_result.json` (DS-033 Evidence Qualification Result), and `../spec/AGCP-Human-Review-Specification.md` (Human Adjudication and Governance Approval Specification).
