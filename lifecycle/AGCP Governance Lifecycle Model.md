# AGCP Governance Lifecycle Model

**Status:** Informational Companion  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This document describes the governance lifecycle defined by the Autonomous Governance Control Plane (AGCP).

Unlike traditional workflow specifications that define application state machines, this document explains how governance progresses through the deterministic AGCP governance pipeline described by the AGCP Core Specification.

The Governance Lifecycle Model illustrates:

- governance progression;
- governance decision points;
- Human Adjudication and Governance Approval integration;
- Execution Authorization;
- Commit Boundary enforcement;
- Governance Evidence generation;
- Append-Only Governance Ledger recording;
- Canonical State derivation; and
- deterministic replay.

This document is intended to provide an architectural understanding of AGCP lifecycle behavior.

Normative implementation requirements are established by the published CRs, the AGCP Core Specification, and any applicable normative Companion Specifications expressly adopted by the implementation profile. The ARM governs architectural terminology and concept meaning; Normative Statements support extraction and traceability and do not supersede those sources.

---

# 2. Scope

This document applies to governance-significant proposals processed by AGCP.

It describes governance processing from initial Proposal Qualification through the applicable pre-commit Continuation Integrity interval, Governance Realization, Commit Boundary processing, and governed execution.

The lifecycle model applies regardless of:

- implementation language;
- deployment architecture;
- storage technology;
- execution platform;
- orchestration framework; or
- cloud provider.

Implementations MAY differ internally provided that the externally observable governance behavior remains consistent with the normative specifications.

---

# 3. Relationship to Other Specifications

This document complements, but does not replace, the following controlled artifacts:

- the AGCP Core Specification (`../spec/AGCP-Core.docx`)
- the Policy Evaluation Contract (`../spec/AGCP-Policy-Evaluation-Contract.md`)
- the AGCP HTTP Interface Specification (`../spec/AGCP-HTTP-Interface-Specification.md`)
- the AGCP Multitenant Operational Specification (`../spec/AGCP-Multitenant-Operational-Specification.md`)
- the AGCP Provenance Wire Format Specification (`../spec/AGCP-Provenance-Wire-Format-Specification.md`)
- AGCP Error Mapping (`../spec/AGCP-Error-Mapping.md`)
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`)
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`)
- the AGCP Human Adjudication and Governance Approval Specification (`../spec/AGCP-Human-Review-Specification.md`)
- the Append-Only Governance Ledger Specification (`../spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`)
- the AGCP Conformance Specification (`../conformance/AGCP-Conformance.md`)

Where an inconsistency exists, it SHALL be resolved using the Core-defined precedence order: published CRs, Core Specification, applicable adopted normative Companion Specifications, Implementation Profiles, Conformance Test Suite, and Reference Implementations. This informational document does not supersede any of those sources.

---

# 4. Governance Lifecycle Overview

AGCP models governance as a deterministic progression through a series of governance stages rather than as a traditional application state machine.

Each stage evaluates authoritative governance information and produces governance outcomes that determine the next stage of processing.

A simplified lifecycle is illustrated below.

```text
Proposal
    │
    ▼
Proposal Qualification
    │
    ├──────────────► Structural Refusal
    │
    ▼
Governance Decision Function
    │
    ├──────────────► Denied
    │
    ├──────────────► Pending Human Review
    │                     │
    │                     ▼
    │              Human Adjudication and
    │              Governance Approval
    │                     │
    │                     ▼
    └──────────────► Governance Decision Resolved
                          │
                          ▼
        Execution Authorization / Eligible Nonterminal State
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
      Authorization Failure   Continuation Integrity,
                              where applicable while
                              the Proposal remains nonterminal
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
                    ▼                   ▼                   ▼
          Remains Eligible      Re-evaluation or      Governed Terminal
                                Recovery Required       Disposition
                    │                   │
                    └───────────┬───────┘
                                ▼
              Governance Realization and Commit Boundary
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
              Commit Failed          Commit Successful
                                            │
                                            ▼
                                   Governed Execution
```

Each governance-significant stage generates Governance Evidence where required and records governance-significant events in the ordered Append-Only Governance Ledger.

Canonical State is deterministically resolved from the applicable qualified authoritative governance sources. The ordered Append-Only Governance Ledger is authoritative for recorded governance events, event ordering, and Derived Lifecycle State incorporated into that resolution.

The Governance Lifecycle therefore represents deterministic governance progression rather than mutable application state transitions.

---

# 5. Proposal Qualification

Proposal Qualification is the first governance stage of the AGCP lifecycle.

Its purpose is to determine whether an incoming Proposal is sufficiently complete, well-formed, and contextually valid to enter governance evaluation.

Proposal Qualification is intentionally limited to evaluating the Proposal itself. It does not perform governance authorization or policy decisions.

## 5.1 Responsibilities

Proposal Qualification evaluates, where applicable:

- structural validity;
- schema conformance;
- required metadata;
- tenant context;
- Governance Domain context;
- provenance;
- replay protection;
- idempotency;
- request admissibility.

Implementations MAY perform additional implementation-specific validation provided that externally observable behavior remains consistent with the normative specifications.

## 5.2 Outcomes

Proposal Qualification produces one of two outcomes.

### Qualified

The Proposal is accepted for governance evaluation.

Processing proceeds to the Governance Decision Function.

### Structural Refusal

The Proposal cannot be processed.

Examples include:

- malformed request;
- missing required information;
- invalid provenance;
- failed replay protection;
- invalid tenant context;
- unsupported request.

A structurally refused Proposal does not enter governance evaluation.

## 5.3 Governance Evidence

Proposal Qualification SHALL generate Governance Evidence describing:

- proposal identifier;
- qualification result;
- provenance verification;
- replay protection result;
- applicable rejection information.

Governance-significant Proposal Qualification events SHALL be recorded or referenced in the Append-Only Governance Ledger.

---

# 6. Governance Decision Function

The Governance Decision Function evaluates qualified proposals using the authoritative governance configuration applicable to the requesting tenant and Governance Domain.

This stage determines the governance disposition of the Proposal.

The Governance Decision Function is deterministic.

Identical authoritative inputs SHALL produce equivalent governance outcomes.

## 6.1 Inputs

Inputs may include:

- applicable governance policies;
- constraints;
- invariants;
- exceptions;
- Authority Lineage;
- Governance Domain configuration;
- Canonical State;
- tenant configuration;
- proposal attributes.

The exact evaluation model is defined by the AGCP Core Specification and the Policy Evaluation Contract.

## 6.2 Governance Outcomes

The Governance Decision Function may produce outcomes including:

### Authorized

The Proposal satisfies applicable governance requirements and may proceed toward Execution Authorization.

### Denied

The Proposal violates one or more applicable governance requirements.

Processing terminates unless subsequently resubmitted as a new Proposal.

### Pending Human Review

The Proposal requires one or more governed human-adjudication, approval, cosignature, risk-acceptance, cancellation, withdrawal, or quorum-participation actions before governance evaluation can continue.

The Proposal remains pending until the applicable DS-026 Governance Approval Artifact and quorum requirements have been satisfied or governance processing terminates. `Pending Human Review` is a governed lifecycle outcome; it is not an artifact type.

### Deferred

Implementations MAY support deferred governance processing where permitted by the applicable specifications.

Deferred processing SHALL preserve deterministic governance behavior.

### Governed Re-evaluation Required

Where authoritative governance conditions change before execution, governance processing may require re-evaluation.

Re-evaluation SHALL occur using the current authoritative governance configuration.

## 6.3 Determinism

The Governance Decision Function SHALL NOT depend upon:

- random values;
- non-authoritative timestamps;
- external mutable state;
- implementation-specific ordering.

Externally observable governance outcomes SHALL remain deterministic.

## 6.4 Governance Evidence

Governance Decision processing SHALL produce Governance Evidence describing:

- evaluated policies;
- evaluated constraints;
- evaluated invariants;
- evaluated exceptions;
- governance outcome;
- Authority Lineage;
- applicable Governance Domain;
- supporting provenance.

Governance-significant outcomes SHALL be recorded in the Append-Only Governance Ledger.

---

# 7. Human Adjudication and Governance Approval

Certain governance decisions require governed human adjudication, approval, negative adjudication, cosignature, risk acceptance, cancellation, withdrawal, or quorum participation before a Proposal may become eligible for Execution Authorization.

Human Adjudication and Governance Approval form a governance stage rather than an execution stage. `Pending Human Review` remains the controlled governance outcome used when required participation is incomplete; it does not identify a separate artifact representation.

All approval and adjudication evidence SHALL use the DS-026 Governance Approval Artifact.

## 7.1 Purpose

Human Adjudication and Governance Approval provide controlled, attributable governance participation where required by governance policy.

They SHALL NOT bypass requirements established by the Governance Decision Function and SHALL NOT by themselves constitute authority at commitment or permission to execute.

## 7.2 Human Adjudication and Governance Approval Processing

Processing verifies, where applicable:

- approver authorization and current eligibility;
- required governance roles;
- quorum requirements and valid partial-quorum accumulation;
- approval kind, decision, status, and lifecycle effect;
- Proposal Identity and eligible lifecycle-state binding;
- target and governance scope;
- Tenant identity and Governance Domain;
- applicable policy and Governance Version;
- Canonical State basis at adjudication;
- validity, revocation, cancellation, withdrawal, and supersession conditions;
- Authority Lineage and provenance;
- cryptographic verification; and
- replay protection.

Human adjudication, approval, negative adjudication, cosignature, risk acceptance, cancellation, withdrawal, and quorum participation SHALL be represented by cryptographically attributable and verifiable DS-026 Governance Approval Artifacts bound to the eligible Proposal Identity, lifecycle state, scope, Tenant, Governance Domain, target, applicable policy and Governance Version, Canonical State basis, Authority Lineage, and validity conditions.

## 7.3 Outcomes

Human Adjudication and Governance Approval processing may produce outcomes including:

### Pending

Required approval or quorum conditions have not yet been completed. Valid partial quorum MAY accumulate through one or more ACTIVE Governance Approval Artifacts.

### Satisfied

All required approval or quorum conditions have been satisfied by valid, ACTIVE Governance Approval Artifacts.

Governance processing may proceed toward Execution Authorization, subject to all other applicable governance conditions and current-state re-evaluation.

### Failed

Required approval, adjudication, or quorum conditions cannot be satisfied, or an applicable Governance Approval Artifact is invalid, expired, cancelled, withdrawn, revoked, or superseded.

Governance processing terminates or enters governed re-evaluation according to applicable governance policy.

## 7.4 Governance Approval Artifacts — DS-026

Each human or governed approval, negative adjudication, cosignature, risk acceptance, cancellation, withdrawal, and quorum-participation action SHALL be represented by one or more DS-026 Governance Approval Artifacts conforming to `schemas/governance_approval_artifact.json`.

Each Governance Approval Artifact SHALL include the applicable DS-026 content, including:

- approval artifact identity and version;
- artifact role, approval kind, decision, and status;
- Proposal Identity, Tenant, Governance Domain, target, lifecycle-state binding, and scope;
- validity window, policy references, Governance Version, and Canonical State reference at adjudication;
- approver identity, approver-eligibility basis, and Authority Lineage reference;
- lifecycle effect and any applicable quorum contribution;
- Governance Evidence references and issuance time;
- attribution, cryptographic verification, replay protection, artifact digest, and semantic assertions; and
- applicable termination, supersession, or related-artifact references.

DS-016 and `human_review_artifact.json` are retired and SHALL NOT be used as active approval or adjudication representations.

Completion of approval or quorum makes the Proposal eligible for the applicable lifecycle transition only. It does not itself constitute authority at commitment, final admissibility, or permission to execute.

## 7.5 Governance Evidence

Human Adjudication and Governance Approval processing SHALL generate Governance Evidence documenting:

- Governance Approval Artifact identity and version;
- approver participation and eligibility;
- decision, approval kind, status, and lifecycle effect;
- validity and cryptographic-verification results;
- partial or completed quorum state;
- replay-protection validation;
- cancellation, withdrawal, revocation, expiration, or supersession where applicable; and
- the resulting governance-continuation decision.

Governance-significant Governance Approval events SHALL be recorded or referenced through DS-040 Governance Ledger Events.

Completion of Human Adjudication or Governance Approval does not itself authorize execution.

Execution remains subject to Execution Authorization, Authority Re-Derivation, Governance Realization, final Commit-Bound Admissibility, and Policy Enforcement Point/Commit Boundary processing.

---

# 8. Execution Authorization

Execution Authorization is the governance stage that determines whether a Proposal is authorized to proceed to the Commit Boundary.

Execution Authorization does not perform execution.

Instead, it establishes that all applicable governance requirements have been satisfied immediately prior to execution authorization.

Execution Authorization SHALL be based upon the current authoritative governance context.

## 8.1 Purpose

Execution Authorization confirms that:

- Proposal Qualification has completed successfully;
- Governance Decision processing has completed successfully;
- all required DS-026 Governance Approval Artifacts have been accepted and any required quorum has been completed;
- applicable governance policies remain satisfied;
- applicable constraints remain satisfied;
- applicable invariants remain satisfied;
- applicable exceptions remain valid;
- tenant state permits execution authorization;
- Governance Domain requirements are satisfied;
- authoritative governance information has not changed in a manner requiring re-evaluation.

Execution Authorization represents the final governance authorization prior to Commit Boundary processing.

## 8.2 Authorization Outcomes

Execution Authorization may produce one of the following outcomes.

### Authorized

All governance prerequisites have been satisfied.

The Proposal may proceed to Commit Boundary processing.

Authorization alone SHALL NOT permit execution.

Execution remains contingent upon successful Commit Boundary validation.

### Authorization Failure

One or more governance requirements cannot be satisfied.

Execution SHALL NOT proceed.

### Governed Re-evaluation Required

Changes in authoritative governance information require governance processing to be repeated before execution may be authorized.

Examples include:

- policy changes;
- tenant suspension;
- Governance Domain changes;
- revoked authority;
- expired, cancelled, withdrawn, revoked, or superseded Governance Approval Artifact;
- expired exception;
- invalidated provenance.

Implementations SHALL ensure that stale authorizations are not reused.

## 8.3 Authorization Validity

Execution Authorization represents a governed authorization decision rather than an execution command.

Execution Authorization SHOULD include sufficient information to permit independent verification, including:

- Proposal reference;
- tenant identifier;
- Governance Domain;
- Authority Lineage reference;
- governance configuration reference;
- Canonical State reference;
- provenance;
- validity information.

Implementations MAY impose additional operational controls provided externally observable behavior remains consistent with the normative specifications.

## 8.4 Governance Evidence

Execution Authorization SHALL generate Governance Evidence documenting:

- authorization outcome;
- applicable governance configuration;
- Authority Lineage;
- Canonical State reference;
- provenance;
- authorization validity.

Governance-significant authorization events SHALL be recorded in the Append-Only Governance Ledger.

---

# 9. Continuation Integrity

Continuation Integrity applies while a Governed Action Proposal remains nonterminal before commitment. It preserves the governance legitimacy, verified continuation basis, and admissible-path viability of the Proposal from evaluation or authorization until final Commit-Bound Admissibility is resolved.

Continuation Integrity ends when the Proposal reaches a governed terminal lifecycle state or successfully completes Commit Boundary processing. Post-commit operational monitoring, intervention, suspension, or termination controls may be established by an applicable Conformance Requirement or implementation profile, but those controls are distinct from Continuation Integrity.

## 9.1 Purpose

Continuation Integrity provides assurance that:

- the nonterminal Proposal continues to satisfy the governance conditions required for potential commitment;
- authority, evidence, Canonical State, lifecycle, dependency, policy, validity, tenant, target, and configuration conditions remain sufficiently verified;
- material governance-condition changes are detected before commitment;
- at least one admissible path toward binding remains viable; and
- a Proposal that lacks a verified continuation basis cannot proceed to commitment.

## 9.2 Pre-Commit Continuation Processing

While a Proposal remains nonterminal, implementations evaluate applicable changes to:

- tenant and Governance Domain state;
- authority, delegation, approval, and Authority Lineage;
- applicable governance policy and configuration;
- Canonical State and qualified evidence;
- lifecycle, validity, target, dependency, coupling, and cross-domain conditions; and
- other governance-significant conditions identified by active risk-based governance configuration.

Affected Proposals are deterministically re-evaluated where required. Unaffected Proposals retain their current lifecycle state and are not unnecessarily re-evaluated.

## 9.3 Integrity Outcomes

Continuation Integrity evaluation may produce the following pre-commit outcomes, consistent with DS-039:

### Proposal Remains Authorized or Viable

The Proposal retains a verified continuation basis and may continue toward final Commit-Bound Admissibility.

### Governed Re-evaluation Required

The Proposal requires renewed governance evaluation before commitment may proceed.

### Degraded or Commitment Suspended

The Proposal enters a policy-defined non-executable lifecycle state, or commitment is suspended, until governed recovery or another policy-defined disposition occurs.

### Proposal Restored to Eligible State

Governed recovery re-establishes the continuation basis and admissible-path viability. Restoration does not bypass renewed Commit-Bound Admissibility.

### Governed Terminal Outcome

The Proposal is escalated, refused, expired, cancelled, or otherwise transitioned according to applicable governance policy when its continuation basis cannot be restored before commitment.

## 9.4 Governance Evidence

Continuation Integrity SHALL generate Governance Evidence documenting:

- Proposal Identity and current Derived Lifecycle State;
- continuation-basis and admissible-path-viability evaluation;
- material governance-condition changes;
- re-evaluation or recovery activity;
- resulting pre-commit lifecycle outcome; and
- applicable source, evidence, policy, configuration, authority, and provenance references.

Governance-significant Continuation Integrity events SHALL be recorded in the Append-Only Governance Ledger.

---

# 10. Commit Boundary

The Commit Boundary is the final governance control point immediately preceding governance-significant execution.

Its purpose is to ensure that execution occurs only after successful governance authorization and immediately validated governance conditions.

The Commit Boundary is distinct from Execution Authorization.

Execution Authorization determines whether execution is permitted.

Commit Boundary determines whether execution may actually proceed at that moment.

## 10.1 Purpose

Commit Boundary validates that:

- a valid Execution Authorization exists;
- the authorization remains valid;
- required DS-026 Governance Approval Artifacts remain ACTIVE, valid, and applicable;
- tenant state remains eligible;
- Governance Domain requirements remain satisfied;
- Canonical State remains valid;
- authoritative governance conditions have not changed since authorization.

If any required condition is no longer satisfied, execution SHALL NOT proceed.

## 10.2 Commit Outcomes

Commit Boundary processing may produce the following outcomes.

### Commit Successful

Execution may proceed.

Governance-significant execution begins only after successful Commit Boundary processing.

### Commit Failed

Execution is denied.

No governance-significant execution occurs.

### Governed Re-evaluation Required

Execution is deferred until governance processing has been repeated.

Implementations SHALL NOT rely upon previously issued Execution Authorizations after authoritative governance changes requiring re-evaluation.

## 10.3 Commit Validation

Commit Boundary validation SHOULD be performed immediately prior to execution.

Implementations SHOULD minimize the interval between successful Commit Boundary validation and execution to reduce exposure to changing governance conditions.

Where execution cannot begin immediately following validation, implementations MAY require Commit Boundary validation to be repeated.

## 10.4 Governance Evidence

Commit Boundary processing SHALL generate Governance Evidence describing:

- Commit Boundary request;
- validation outcome;
- Execution Authorization reference;
- Canonical State reference;
- provenance;
- execution decision.

Successful Commit Boundary processing SHALL be recorded in the Append-Only Governance Ledger.

---

# 11. Governed Execution

Governed Execution begins only after successful Commit Boundary processing.

Execution is outside the governance decision process itself but remains subject to governance accountability and evidence generation.

## 11.1 Purpose

Governed Execution performs the authorized activity while preserving governance accountability.

Execution implementations MAY differ internally provided they preserve the externally observable governance behavior defined by the AGCP specifications.

## 11.2 Governance Responsibilities During Execution

During execution, implementations SHOULD:

- preserve execution provenance;
- preserve Governance Evidence;
- preserve execution accountability;
- detect execution failures where applicable;
- support deterministic audit and replay.

Execution implementations SHALL NOT invalidate the governance guarantees established by earlier lifecycle stages.

## 11.3 Execution Outcomes

Execution may result in outcomes including:

### Successful Completion

Execution completes successfully.

### Execution Failure

Execution terminates unsuccessfully.

Execution failure does not invalidate the governance processing that preceded execution.

Instead, Governance Evidence records the observed execution outcome.

### Governed Recovery

Implementations MAY perform governed recovery procedures where permitted by applicable governance policy.

Recovery behavior SHALL remain consistent with the normative specifications.

## 11.4 Governance Evidence

Where post-commit execution-outcome evidence is required by an applicable Conformance Requirement or implementation profile, Governed Execution SHALL generate or preserve Governance Evidence describing:

- execution initiation;
- execution completion;
- execution outcome;
- execution failure information (where applicable);
- provenance;
- Commit Boundary reference.

Governance-significant execution events SHALL be recorded in the Append-Only Governance Ledger.

---

# 12. Governance Evidence Throughout the Lifecycle

Governance Evidence provides the authoritative record describing governance-significant processing throughout the governance lifecycle.

Each governance-significant processing stage SHALL generate Governance Evidence sufficient to support:

- audit;
- accountability;
- deterministic replay;
- compliance verification;
- forensic analysis;
- Canonical State resolution and deterministic replay.

Governance Evidence records governance events.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

## 12.1 Typical Governance Evidence

Governance Evidence SHALL contain sufficient information to establish, where applicable:

- proposal identifier;
- tenant identifier;
- Governance Domain;
- governance stage;
- governance outcome;
- Authority Lineage;
- provenance;
- policy references;
- constraint results;
- invariant results;
- Governance Approval Artifact references;
- Execution Authorization references;
- Commit Boundary references;
- execution outcomes;
- Canonical State reference;
- ledger reference.

The exact contents are defined by the applicable schemas and specifications.

## 12.2 Integrity

Governance Evidence SHALL be authoritative, attributable, complete, deterministic, verifiable, and tamper-evident.

Governance Evidence SHALL remain tenant scoped and Governance Domain scoped where applicable and SHALL preserve authenticity, integrity, traceability, chronological ordering, and logical association with the governed Proposal, Action, and resulting outcome.

Governance Evidence SHALL support deterministic reconstruction of governance processing and outcome.

---

# 13. Append-Only Governance Ledger

The Append-Only Governance Ledger is the authoritative persistent record of governance-significant events.

It establishes:

- authoritative ordering;
- persistence;
- governance accountability;
- deterministic replay support;
- Canonical State resolution and deterministic replay.

The ledger records governance-significant events.

It does not itself determine governance policy.

## 13.1 Ordered Recording

Governance-significant events SHALL be recorded in deterministic ledger sequence order.

Ledger sequence ordering is authoritative.

Timestamp ordering SHALL NOT be used to determine authoritative governance ordering.

## 13.2 Immutability

Governance Ledger Events SHALL conform to DS-040 and SHALL be append-only.

Historical governance events SHALL NOT be modified, reordered, or removed.

Implementations MAY choose any storage technology provided these externally observable properties are preserved.

## 13.3 Governance Ledger Event References

Governance artifacts SHOULD use the DS-040 Governance Ledger Event reference representation where a ledger relationship applies. The reference includes:

- `ledger_event_id`;
- `event_version`;
- `event_type`;
- `event_category`;
- `ledger_position`, including `ledger_id`, `stream_id`, `sequence`, event identity, and integrity digests;
- `tenant_id`;
- `governance_domain_id`;
- `proposal_id`, where applicable;
- `event_digest`;
- `event_uri`, where applicable; and
- `appended_at`.

Governance Ledger Events themselves SHALL preserve the current DS-040 `event_artifact_refs`, `governance_basis`, `evidence_binding`, `causality`, `integrity_protection`, `attribution`, `provenance`, `replay_material`, and `semantic_assertions` structures.

These references and event structures support traceability, integrity verification, authoritative ordering, and deterministic reconstruction.

## 13.4 Relationship to Governance Evidence

Governance Evidence describes governance events.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

Together they provide deterministic governance accountability.

---

# 14. Canonical State Resolution

Canonical State is the qualified and authoritative governance representation of operational reality used for a defined evaluation horizon.

Canonical State SHALL be deterministically resolved from one or more qualified authoritative governance sources. The Append-Only Governance Ledger need not be the originating system of record for every governance-relevant fact incorporated into Canonical State.

## 14.1 Source Qualification and Resolution

The applicable source set SHALL be qualified for freshness, provenance, completeness, consistency, integrity, availability, and ordering suitability for the evaluation horizon.

Where candidate authoritative governance sources conflict, the implementation SHALL resolve one authoritative Canonical State or produce Structural Refusal.

The Canonical State basis used for an evaluation SHALL preserve or reference the applicable source identities, versions, provenance, and integrity information required for deterministic replay.

## 14.2 Governance Ledger Authority and Ordering

The ordered Append-Only Governance Ledger SHALL be authoritative for recorded governance events, event ordering, and Derived Lifecycle State.

Where Canonical State incorporates those ledger-governed elements, ledger sequence order SHALL determine their authoritative order. Timestamp order and implementation-specific storage order SHALL NOT substitute for ledger sequence order.

Non-ledger Canonical State facts SHALL remain bound to their applicable qualified authoritative governance sources.

## 14.3 Materialized State

Implementations MAY maintain materialized Canonical State for operational efficiency.

A materialized view SHALL remain deterministically reproducible from the applicable qualified authoritative source versions and ordered Governance Ledger records used to produce it.

A materialized view SHALL NOT supersede those sources as the authoritative governance basis.

## 14.4 Replay and Reproduction

Deterministic replay using the same qualified authoritative source versions, applicable ordered Governance Ledger records, governance configuration, and policy artifacts SHALL reproduce an equivalent Canonical State basis and governance outcome.

Failure to reproduce the Canonical State basis may indicate:

- source-version mismatch;
- unavailable, incomplete, or unqualified authoritative source data;
- Governance Ledger corruption or ordering failure;
- incomplete Governance Evidence or provenance; or
- non-conformant behavior.

## 14.5 Lifecycle Significance

Governance-significant lifecycle events contribute to Derived Lifecycle State through the ordered Append-Only Governance Ledger.

Derived Lifecycle State may form part of Canonical State, but no lifecycle stage or ledger record independently defines the complete Canonical State unless the complete applicable authoritative source set for that evaluation consists solely of ledger-governed information.

---

# 15. Deterministic Replay

Deterministic replay enables independent verification that governance processing produces equivalent externally observable outcomes when supplied with equivalent authoritative inputs.

Deterministic replay supports:

- audit;
- compliance verification;
- forensic investigation;
- implementation validation;
- conformance testing;
- Canonical State verification.

Replay is performed using recorded Governance Evidence together with the ordered Append-Only Governance Ledger.

## 15.1 Replay Inputs

Replay SHOULD use the authoritative governance artifacts applicable to the original governance decision, including:

- Proposal;
- provenance;
- applicable governance configuration;
- policy references;
- constraint definitions;
- invariant definitions;
- DS-026 Governance Approval Artifacts;
- Execution Authorization artifacts;
- Commit Boundary records;
- Governance Evidence;
- ordered DS-040 Governance Ledger Events.

Replay implementations MAY use additional implementation-specific information provided that externally observable replay behavior remains consistent with the AGCP specifications.

## 15.2 Replay Expectations

Given equivalent authoritative inputs, deterministic replay SHOULD produce equivalent:

- Proposal Qualification outcomes;
- Governance Decision outcomes;
- Governance Approval Artifact validation and human-adjudication or quorum outcomes;
- Execution Authorization decisions;
- Commit Boundary decisions;
- Governance Evidence relationships;
- Canonical State.

Replay implementations SHALL preserve authoritative ledger ordering.

## 15.3 Canonical State Replay

Replay SHALL resolve Canonical State using the same qualified authoritative source versions and applicable Governance Ledger records used for the original evaluation.

For incorporated Governance Ledger records and Derived Lifecycle State, replay SHALL preserve authoritative ledger sequence order and SHALL NOT substitute timestamp or implementation-specific storage ordering.

Equivalent Canonical State resolution demonstrates that governance processing remains deterministic.

## 15.4 Replay Failures

Replay SHOULD fail when authoritative governance history cannot be reconstructed.

Examples include:

- missing Governance Evidence;
- missing DS-040 Governance Ledger Events;
- reordered ledger history;
- corrupted provenance;
- invalid, expired, cancelled, withdrawn, revoked, or superseded DS-026 Governance Approval Artifacts;
- invalid Execution Authorization;
- inconsistent governance configuration.

Such failures indicate that governance reconstruction cannot be verified.

---

# 16. Exceptional Conditions

Not every Proposal progresses successfully through the governance lifecycle.

Implementations SHALL manage exceptional conditions while preserving deterministic governance behavior and accountability.

## 16.1 Structural Refusal

Proposal Qualification MAY refuse processing before governance evaluation begins.

Examples include:

- malformed Proposal;
- schema violations;
- missing required information;
- invalid provenance;
- replay protection failure;
- unsupported request.

Structural refusal terminates processing before governance evaluation.

## 16.2 Governance Denial

The Governance Decision Function MAY deny a Proposal when governance requirements are not satisfied.

Governance denial records the applicable governance outcome and supporting Governance Evidence.

## 16.3 Human Adjudication or Governance Approval Failure

Human Adjudication or Governance Approval MAY fail because required approvers, valid Governance Approval Artifacts, quorum, or other governed approval conditions cannot be satisfied.

Execution SHALL NOT proceed when required DS-026 Governance Approval Artifact or quorum conditions remain incomplete, invalid, or unsuccessful.

## 16.4 Authorization Failure

Execution Authorization MAY fail when governance prerequisites are no longer satisfied.

Examples include:

- governance policy changes;
- expired, cancelled, withdrawn, revoked, or superseded Governance Approval Artifact;
- revoked authority;
- tenant suspension;
- Governance Domain changes;
- Canonical State inconsistency.

Authorization failure prevents progression to the Commit Boundary.

## 16.5 Commit Boundary Failure

Commit Boundary processing MAY fail immediately before execution.

Failure SHALL prevent governance-significant execution.

Where appropriate, implementations MAY require renewed governance evaluation before another Commit Boundary attempt.

## 16.6 Execution Failure

Execution itself MAY fail after successful Commit Boundary validation.

Execution failure does not invalidate the governance decisions that authorized execution.

Instead, execution outcomes become part of the Governance Evidence and ordered Append-Only Governance Ledger.

## 16.7 Recovery

Implementations MAY support governed recovery procedures.

Recovery behavior SHALL:

- preserve governance accountability;
- preserve deterministic behavior;
- preserve ordered ledger history;
- preserve Canonical State integrity.

---

# 17. Relationship to Conformance

This lifecycle model provides architectural guidance for understanding governance progression.

Normative implementation behavior is verified through the AGCP Conformance framework.

The authoritative conformance traceability model is:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
```

Executable verification is provided through:

```text
Test Case (TC)
        ↓
Harness Check
        ↓
Harness Test Vector
```

The lifecycle described by this document is exercised by the Conformance Test Suite through representative governance scenarios covering:

- Proposal Qualification;
- Governance Decision Function;
- Human Adjudication and Governance Approval;
- Execution Authorization;
- Commit Boundary;
- Governance Evidence;
- Append-Only Governance Ledger;
- Canonical State resolution and, for replay, reproduction of Canonical State resolution from recorded qualified source versions and applicable ordered Governance Ledger records;
- deterministic replay;
- tenant isolation;
- Governance Domain isolation.

Successful conformance demonstrates that an implementation preserves the externally observable governance behavior defined by the AGCP specifications.

---

# 18. References

This document should be read together with the following controlled AGCP artifacts:

- the AGCP Core Specification (`../spec/AGCP-Core.docx`)
- the Policy Evaluation Contract (`../spec/AGCP-Policy-Evaluation-Contract.md`)
- the AGCP HTTP Interface Specification (`../spec/AGCP-HTTP-Interface-Specification.md`)
- the AGCP Multitenant Operational Specification (`../spec/AGCP-Multitenant-Operational-Specification.md`)
- the AGCP Human Adjudication and Governance Approval Specification (`../spec/AGCP-Human-Review-Specification.md`)
- the AGCP Provenance Wire Format Specification (`../spec/AGCP-Provenance-Wire-Format-Specification.md`)
- AGCP Error Mapping (`../spec/AGCP-Error-Mapping.md`)
- the Append-Only Governance Ledger Specification (`../spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`)
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`)
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`)
- the AGCP Conformance Specification (`../conformance/AGCP-Conformance.md`)
- the AGCP Conformance Test Matrix (`../conformance/AGCP-Test-Matrix.md`)
- the AGCP Conformance Test Vectors (`../conformance/AGCP-Conformance-Test-Vectors.md`)
- the AGCP Harness Check Registry (`../conformance/AGCP Harness Check Registry.md`)

---

# Summary

The AGCP Governance Lifecycle describes deterministic governance progression rather than a traditional application state machine.

Governance progresses through Proposal Qualification, Governance Decision, Human Adjudication and Governance Approval (where required), Execution Authorization or another eligible nonterminal state, applicable pre-commit Continuation Integrity, Governance Realization and Commit Boundary processing, and governed execution.

Throughout this progression:

- Governance Evidence documents governance-significant events.
- The Append-Only Governance Ledger establishes authoritative ordering and persistence.
- Canonical State is deterministically resolved from the applicable qualified authoritative governance sources, with authoritative ledger ordering applied to incorporated governance events and Derived Lifecycle State.
- Deterministic replay enables independent verification of governance behavior.
- Conformance verifies that implementations preserve the externally observable behavior defined by the AGCP specifications while allowing implementation flexibility for internal architecture.
