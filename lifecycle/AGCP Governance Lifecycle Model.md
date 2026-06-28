# AGCP Governance Lifecycle Model

**Status:** Informational (Normative Companion)  
**Repository Versioning:** Repository Release Governed

---

# 1. Purpose

This document describes the governance lifecycle defined by the Autonomous Governance Control Plane (AGCP).

Unlike traditional workflow specifications that define application state machines, this document explains how governance progresses through the deterministic AGCP governance pipeline described by the AGCP Core Specification.

The Governance Lifecycle Model illustrates:

- governance progression;
- governance decision points;
- Human Review integration;
- Execution Authorization;
- Commit Boundary enforcement;
- Governance Evidence generation;
- Append-Only Governance Ledger recording;
- Canonical State derivation; and
- deterministic replay.

This document is intended to provide an architectural understanding of AGCP lifecycle behavior.

Normative implementation requirements are defined by the AGCP Core Specification and associated normative specifications.

---

# 2. Scope

This document applies to governance-significant proposals processed by AGCP.

It describes the progression of governance processing from initial Proposal Qualification through governed execution and Continuation Integrity.

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

This document complements, but does not replace, the following specifications:

- AGCP Core Specification
- AGCP Policy Evaluation Contract
- AGCP HTTP Interface Specification
- AGCP Security Specification
- AGCP Multitenant Operational Specification
- AGCP Provenance Wire Format Specification
- AGCP Human Review Specification
- AGCP Append-Only Governance Ledger Specification
- AGCP Conformance Specification

Where any inconsistency exists between this document and a normative specification, the normative specification takes precedence.

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
    │              Human Review
    │                     │
    │                     ▼
    └──────────────► Governance Decision Resolved
                          │
                          ▼
                 Execution Authorization
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
      Authorization Failure   Authorized
                                        │
                                        ▼
                                Commit Boundary
                                        │
                        ┌───────────────┴───────────────┐
                        │                               │
                        ▼                               ▼
                 Commit Failed                 Commit Successful
                                                        │
                                                        ▼
                                               Governed Execution
                                                        │
                                                        ▼
                                             Continuation Integrity
```

Each governance-significant stage generates Governance Evidence where required and records governance-significant events in the ordered Append-Only Governance Ledger.

Canonical State is derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation can be deterministically reproduced from the ordered ledger history.

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

Proposal Qualification SHOULD generate Governance Evidence describing:

- proposal identifier;
- qualification result;
- provenance verification;
- replay protection result;
- applicable rejection information.

Where Governance Evidence is produced, governance-significant events SHALL be recorded in the Append-Only Governance Ledger.

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

The Proposal requires one or more Human Reviews before governance evaluation can continue.

The Proposal remains pending until Human Review requirements have been satisfied or governance processing terminates.

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

Governance Decision processing SHOULD produce Governance Evidence describing:

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

# 7. Human Review

Certain governance decisions require explicit Human Review before execution may be authorized.

Human Review is a governance stage rather than an execution stage.

It provides governed human participation within an otherwise deterministic governance process.

## 7.1 Purpose

Human Review provides controlled human authorization where required by governance policy.

Human Review SHALL NOT bypass governance requirements established by the Governance Decision Function.

## 7.2 Human Review Processing

Human Review verifies, where applicable:

- reviewer authorization;
- required review roles;
- quorum requirements;
- review scope;
- proposal identity;
- tenant identity;
- Governance Domain;
- provenance;
- replay protection.

Human Review artifacts SHALL be cryptographically attributable to the reviewer.

## 7.3 Outcomes

Human Review may produce outcomes including:

### Pending

Required reviews have not yet been completed.

### Satisfied

All required reviews have been successfully completed.

Governance processing proceeds toward Execution Authorization.

### Failed

Human Review requirements cannot be satisfied.

Governance processing terminates unless subsequently re-initiated according to applicable governance policy.

## 7.4 Human Review Artifacts

Each completed Human Review SHOULD produce a Human Review Artifact describing:

- reviewer identity;
- reviewer role;
- review decision;
- review timestamp;
- provenance;
- applicable proposal;
- Authority Lineage reference.

## 7.5 Governance Evidence

Human Review processing SHOULD generate Governance Evidence documenting:

- Human Review participation;
- quorum status;
- review completion;
- replay validation;
- governance continuation decision.

Governance-significant Human Review events SHALL be recorded in the Append-Only Governance Ledger.

Completion of Human Review does not itself authorize execution.

Execution remains subject to Execution Authorization and Commit Boundary validation.

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
- all required Human Reviews have been completed;
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
- expired Human Review;
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

Execution Authorization SHOULD generate Governance Evidence documenting:

- authorization outcome;
- applicable governance configuration;
- Authority Lineage;
- Canonical State reference;
- provenance;
- authorization validity.

Governance-significant authorization events SHALL be recorded in the Append-Only Governance Ledger.

---

# 9. Commit Boundary

The Commit Boundary is the final governance control point immediately preceding governance-significant execution.

Its purpose is to ensure that execution occurs only after successful governance authorization and immediately validated governance conditions.

The Commit Boundary is distinct from Execution Authorization.

Execution Authorization determines whether execution is permitted.

Commit Boundary determines whether execution may actually proceed at that moment.

## 9.1 Purpose

Commit Boundary validates that:

- a valid Execution Authorization exists;
- the authorization remains valid;
- required Human Reviews remain valid;
- tenant state remains eligible;
- Governance Domain requirements remain satisfied;
- Canonical State remains valid;
- authoritative governance conditions have not changed since authorization.

If any required condition is no longer satisfied, execution SHALL NOT proceed.

## 9.2 Commit Outcomes

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

## 9.3 Commit Validation

Commit Boundary validation SHOULD be performed immediately prior to execution.

Implementations SHOULD minimize the interval between successful Commit Boundary validation and execution to reduce exposure to changing governance conditions.

Where execution cannot begin immediately following validation, implementations MAY require Commit Boundary validation to be repeated.

## 9.4 Governance Evidence

Commit Boundary SHOULD generate Governance Evidence describing:

- Commit Boundary request;
- validation outcome;
- Execution Authorization reference;
- Canonical State reference;
- provenance;
- execution decision.

Successful Commit Boundary processing SHALL be recorded in the Append-Only Governance Ledger.

---

# 10. Governed Execution

Governed Execution begins only after successful Commit Boundary processing.

Execution is outside the governance decision process itself but remains subject to governance accountability and evidence generation.

## 10.1 Purpose

Governed Execution performs the authorized activity while preserving governance accountability.

Execution implementations MAY differ internally provided they preserve the externally observable governance behavior defined by the AGCP specifications.

## 10.2 Governance Responsibilities During Execution

During execution, implementations SHOULD:

- preserve execution provenance;
- preserve Governance Evidence;
- preserve execution accountability;
- detect execution failures where applicable;
- support deterministic audit and replay.

Execution implementations SHALL NOT invalidate the governance guarantees established by earlier lifecycle stages.

## 10.3 Execution Outcomes

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

## 10.4 Governance Evidence

Governed Execution SHOULD generate Governance Evidence describing:

- execution initiation;
- execution completion;
- execution outcome;
- execution failure information (where applicable);
- provenance;
- Commit Boundary reference.

Governance-significant execution events SHALL be recorded in the Append-Only Governance Ledger.

---

# 11. Continuation Integrity

Certain governance-significant activities continue beyond the initial execution event.

Continuation Integrity ensures that ongoing execution remains consistent with the governance conditions under which execution was authorized.

Continuation Integrity applies only where required by the applicable governance policy or implementation profile.

## 11.1 Purpose

Continuation Integrity provides assurance that:

- execution continues within authorized governance boundaries;
- governance assumptions remain valid throughout execution;
- significant governance changes are detected;
- continued execution remains authorized.

Continuation Integrity extends governance accountability beyond the initial Commit Boundary.

## 11.2 Continuous Governance

Implementations MAY periodically evaluate:

- tenant state;
- Governance Domain state;
- applicable governance policies;
- Authority Lineage;
- execution environment;
- provenance validity;
- operational constraints.

The frequency and implementation mechanism are implementation-specific unless otherwise defined by a normative specification.

## 11.3 Integrity Outcomes

Continuation Integrity evaluation may produce outcomes including:

### Continue

Execution continues under the existing governance authorization.

### Re-evaluation Required

Execution SHOULD pause or enter a governed state pending renewed governance evaluation.

### Terminate

Execution terminates because governance requirements can no longer be satisfied.

Implementations MAY define additional operational responses provided externally observable governance behavior remains consistent with the AGCP specifications.

## 11.4 Governance Evidence

Continuation Integrity SHOULD generate Governance Evidence documenting:

- integrity evaluation;
- governance changes;
- continuation decision;
- provenance;
- execution status.

Governance-significant Continuation Integrity events SHALL be recorded in the Append-Only Governance Ledger.

---

# 12. Governance Evidence Throughout the Lifecycle

Governance Evidence provides the authoritative record describing governance-significant processing throughout the governance lifecycle.

Each lifecycle stage SHOULD generate Governance Evidence sufficient to support:

- audit;
- accountability;
- deterministic replay;
- compliance verification;
- forensic analysis;
- Canonical State reconstruction.

Governance Evidence records governance events.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

## 12.1 Typical Governance Evidence

Governance Evidence may include:

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
- Human Review references;
- Execution Authorization references;
- Commit Boundary references;
- execution outcomes;
- Canonical State reference;
- ledger reference.

The exact contents are defined by the applicable schemas and specifications.

## 12.2 Integrity

Governance Evidence SHOULD be:

- attributable;
- integrity protected;
- tenant scoped;
- Governance Domain scoped where applicable;
- independently verifiable.

Governance Evidence SHOULD support deterministic reconstruction of governance processing.

---

# 13. Append-Only Governance Ledger

The Append-Only Governance Ledger is the authoritative persistent record of governance-significant events.

It establishes:

- authoritative ordering;
- persistence;
- governance accountability;
- deterministic replay support;
- Canonical State reconstruction.

The ledger records governance-significant events.

It does not itself determine governance policy.

## 13.1 Ordered Recording

Governance-significant events SHALL be recorded in deterministic ledger sequence order.

Ledger sequence ordering is authoritative.

Timestamp ordering SHALL NOT be used to determine authoritative governance ordering.

## 13.2 Immutability

Ledger entries SHALL be append-only.

Historical governance events SHALL NOT be modified, reordered, or removed.

Implementations MAY choose any storage technology provided these externally observable properties are preserved.

## 13.3 Ledger References

Governance artifacts SHOULD include ledger references where applicable, including:

- ledger_entry_id;
- ledger_sequence_value;
- previous_ledger_entry_hash (where implemented).

These references improve traceability and deterministic reconstruction.

## 13.4 Relationship to Governance Evidence

Governance Evidence describes governance events.

The Append-Only Governance Ledger establishes their authoritative ordering and persistence.

Together they provide deterministic governance accountability.

---

# 14. Canonical State Derivation

Canonical State represents the authoritative governance state of a Proposal at a particular point in governance processing.

Canonical State is not independently stored by architectural requirement.

Instead:

> Canonical State SHALL be derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation from the ordered Append-Only Governance Ledger can be deterministically reproduced.

## 14.1 Authoritative Ordering

Canonical State SHALL be derived using ledger sequence order.

Timestamp order SHALL NOT determine authoritative governance state.

If ledger ordering differs from timestamp ordering, ledger ordering takes precedence.

## 14.2 Materialized State

Implementations MAY maintain materialized Canonical State for operational efficiency.

Such materialized state SHALL remain verifiable against the ordered Append-Only Governance Ledger.

Materialized state SHALL NOT become the authoritative governance record.

## 14.3 Reconstruction

Deterministic replay of ordered ledger history SHALL produce equivalent Canonical State.

Failure to reproduce Canonical State from ordered ledger history indicates:

- implementation error;
- ledger corruption;
- incomplete governance history; or
- non-conformant behavior.

## 14.4 Lifecycle Significance

Every governance stage contributes evidence toward Canonical State.

No individual governance stage independently defines Canonical State.

Rather, Canonical State emerges from the complete ordered governance history recorded in the Append-Only Governance Ledger.

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
- Human Review artifacts;
- Execution Authorization artifacts;
- Commit Boundary records;
- Governance Evidence;
- ordered Append-Only Governance Ledger entries.

Replay implementations MAY use additional implementation-specific information provided that externally observable replay behavior remains consistent with the AGCP specifications.

## 15.2 Replay Expectations

Given equivalent authoritative inputs, deterministic replay SHOULD produce equivalent:

- Proposal Qualification outcomes;
- Governance Decision outcomes;
- Human Review validation results;
- Execution Authorization decisions;
- Commit Boundary decisions;
- Governance Evidence relationships;
- Canonical State.

Replay implementations SHALL preserve authoritative ledger ordering.

## 15.3 Canonical Replay

Replay SHALL reconstruct Canonical State using the ordered Append-Only Governance Ledger.

Replay SHALL NOT derive Canonical State using timestamp ordering or any other non-authoritative ordering mechanism.

Equivalent Canonical State reconstruction demonstrates that governance processing remains deterministic.

## 15.4 Replay Failures

Replay SHOULD fail when authoritative governance history cannot be reconstructed.

Examples include:

- missing Governance Evidence;
- missing ledger entries;
- reordered ledger history;
- corrupted provenance;
- invalid Human Review artifacts;
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

## 16.3 Human Review Failure

Human Review MAY fail because required reviewers, approvals, or authorization conditions cannot be satisfied.

Execution SHALL NOT proceed when required Human Review remains incomplete or unsuccessful.

## 16.4 Authorization Failure

Execution Authorization MAY fail when governance prerequisites are no longer satisfied.

Examples include:

- governance policy changes;
- expired Human Review;
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
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
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
- Human Review;
- Execution Authorization;
- Commit Boundary;
- Governance Evidence;
- Append-Only Governance Ledger;
- Canonical State reconstruction;
- deterministic replay;
- tenant isolation;
- Governance Domain isolation.

Successful conformance demonstrates that an implementation preserves the externally observable governance behavior defined by the AGCP specifications.

---

# 18. References

This document should be read together with the following AGCP specifications:

- AGCP Core Specification
- AGCP Policy Evaluation Contract
- AGCP HTTP Interface Specification
- AGCP Security Specification
- AGCP Multitenant Operational Specification
- AGCP Human Review Specification
- AGCP Provenance Wire Format Specification
- AGCP Append-Only Governance Ledger Specification
- AGCP Governance Evidence Specification
- AGCP Conformance Specification
- AGCP Conformance Test Matrix
- AGCP Conformance Test Vectors
- AGCP Harness Check Registry

---

# Summary

The AGCP Governance Lifecycle describes deterministic governance progression rather than a traditional application state machine.

Governance progresses through Proposal Qualification, Governance Decision, Human Review (where required), Execution Authorization, Commit Boundary, Governed Execution, and Continuation Integrity.

Throughout this progression:

- Governance Evidence documents governance-significant events.
- The Append-Only Governance Ledger establishes authoritative ordering and persistence.
- Canonical State is derived from the ordered Append-Only Governance Ledger, or from a verifiable materialized state whose derivation can be deterministically reproduced from the ordered ledger.
- Deterministic replay enables independent verification of governance behavior.
- Conformance verifies that implementations preserve the externally observable behavior defined by the AGCP specifications while allowing implementation flexibility for internal architecture.

