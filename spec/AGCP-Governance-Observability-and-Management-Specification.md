# AGCP Governance Observability and Management Specification

**Artifact Lifecycle:** CURRENT  
**Baseline Status:** Public Review Controlled Baseline  
**Document status:** Normative Companion Specification  
**Specification Version:** 2.1.0  
**Repository Release Target:** AGCP v2.1.0  
**Baseline Date:** 2026-08-15  
**Interface IDs:** IF-003, IF-004

## 1. Purpose

This specification defines the AGCP Governance Observability and Management Plane. It standardizes read-only Governance Observation Points (GOPs), controlled Governance Actuation Points (GAPs), machine-readable capability discovery, authoritative actuation realization/readback, and the security and evidence rules that permit operational management tooling without creating a governance bypass.

This companion specification does not create an independent Conformance Requirement merely because an implementation does or does not expose IF-003 or IF-004. Where an adopted Implementation Profile requires these interfaces, applicability SHALL be explicit. Existing CR and Formal Test Case obligations remain authoritative.

## 2. Architectural model

The AGCP runtime MAY expose three logically distinct interface classes:

1. governed-action/data-plane interfaces such as IF-001;
2. the production-capable Management Plane defined by IF-003 and IF-004; and
3. the optional Conformance Test Control Plane defined separately by IF-005.

Management-plane operations SHALL NOT be interpreted as ordinary governed-action proposals unless the controlling operation explicitly enters the Proposal lifecycle.

A management-plane request record is not itself an authoritative state transition. The implementation SHALL distinguish request acceptance from authoritative realization.

## 3. Governance Observation Points (GOPs)

A **Governance Observation Point (GOP)** is a read-only interface that exposes attributable information about governance state, transitions, evaluations, decisions, evidence, enforcement, or lifecycle realization.

A GOP:

- SHALL NOT mutate authoritative governance state;
- SHALL identify the implementation and observation time;
- SHALL identify the observed subject or artifact where applicable;
- SHALL preserve Tenant and Governance Domain scope;
- SHALL distinguish authoritative artifacts from telemetry or derived views;
- SHALL NOT cause a governance decision merely because it was observed;
- SHALL support integrity protection for observation records intended as assessment or operational evidence; and
- when used to demonstrate management/test-control consumption, SHALL correlate the observation to the responsible actuation/test-control condition and the authoritative source or artifact actually consumed.

Standard observation classes are:

- `PROPOSAL_INGRESS`
- `PROPOSAL_QUALIFICATION`
- `CANONICAL_STATE_RESOLUTION`
- `STATE_QUALIFICATION`
- `EVIDENCE_QUALIFICATION`
- `GOVERNANCE_DECISION`
- `HUMAN_REVIEW`
- `AUTHORITY_REDERIVATION`
- `EXECUTION_AUTHORIZATION`
- `CONTINUATION_INTEGRITY`
- `GOVERNANCE_DEGRADATION`
- `COMMIT_BOUND_ADMISSIBILITY`
- `GOVERNANCE_BINDING_VALIDATION`
- `GOVERNANCE_REALIZATION`
- `PEP_ENFORCEMENT`
- `RESULTING_STATE_VALIDATION`
- `GOVERNANCE_EVIDENCE`
- `LEDGER_APPEND`
- `DERIVED_LIFECYCLE_STATE`

### 3.1 Five-stage observation alignment

GOPs SHOULD be attributable to the AGCP control-plane stage in which the observation occurred:

1. identity/context attributes;
2. action schema/representation;
3. rule evaluation;
4. commit semantics; and
5. audit/lifecycle records.

### 3.2 Observation correlation

Where a governed request is affected by a management actuation or isolated test control, applicable GOP records SHALL preserve correlation sufficient to establish:

- the governed request or Proposal that was processed;
- the management/test operation that established the condition;
- the authoritative or test-scoped source selected by the runtime;
- the stage at which the condition was consumed; and
- the resulting authoritative artifact or outcome, without treating the observation itself as authority.

DS-046 provides `test_scope`, `correlation_id`, `caused_by_refs`, `condition_refs`, and `source_refs` for this purpose.

### 3A. Decision, Realization, Enforcement, and Outcome Distinction

Observation data SHALL preserve the distinction among:

- GDF/PDP Governance Decision;
- Execution Authorization;
- GRF current-authority and Commit-Bound Admissibility result;
- selected PEP Profile / enforcement mapping reference where applicable;
- PEP invocation, refusal, or acceptance;
- commitment event; and
- downstream target/execution outcome when distinct from commitment.

An observability implementation SHALL NOT collapse those milestones into one generic `authorized` or `executed` event when the implementation exposes the underlying distinctions.

## 4. Governance Actuation Points (GAPs)

A **Governance Actuation Point (GAP)** is an authenticated, authorized, scoped administrative ingress through which management tooling can introduce a controlled governance input or request an administrative transition.

A GAP SHALL exercise the normal authoritative governance mechanisms applicable to the change. A GAP SHALL NOT directly overwrite or fabricate a downstream governance result merely to obtain a desired state.

Standard production actuation types are:

- `TENANT_STATE_TRANSITION`
- `GOVERNANCE_DOMAIN_TRANSITION`
- `GOVERNANCE_CONFIGURATION_ACTIVATION`
- `GOVERNANCE_CONFIGURATION_ROLLBACK`
- `AUTHORITY_EVENT`
- `DELEGATION_EVENT`
- `EVIDENCE_SOURCE_ADMINISTRATION`
- `HUMAN_REVIEW_ADMINISTRATION`
- `DEGRADATION_TRANSITION`
- `CONTINUATION_REEVALUATION_REQUEST`
- `POLICY_LIFECYCLE_ACTION`

### 4.1 Type-bound actuation payloads

Each actuation type SHALL use the corresponding type-specific `requested_condition` defined by DS-048. An implementation SHALL reject a condition payload that does not match its declared `actuation_type`.

The typed condition is an input to the applicable authoritative governance mechanism. It is not permission to synthesize the downstream result.

### 4.2 Acceptance is not realization

An HTTP 2xx response or `acceptance_status: ACCEPTED` means only that the actuation request was authenticated, authorized, structurally valid, and admitted for processing.

It SHALL NOT be interpreted as evidence that the requested condition is authoritative or effective.

DS-049 SHALL represent realization separately with one of:

- `PENDING`
- `EFFECTIVE`
- `NO_OP`
- `FAILED`
- `CANCELLED`
- `EXPIRED`
- `NOT_APPLICABLE`

`realization_status: EFFECTIVE` SHALL be emitted only after the ordinary authoritative management mechanism has realized the requested condition. An EFFECTIVE result SHALL identify the effective condition, authoritative artifact references, Governance Evidence, and correlated observation records. Where the controlling baseline requires a Governance Ledger event, the corresponding ledger reference SHALL also be present.

### 4.3 Readback and asynchronous processing

IF-004 SHALL provide status/readback through:

`GET /agcp/management/v1/actuations/{actuation_id}`

A client SHALL be able to distinguish a request that remains pending from one that became effective, failed, expired, was cancelled, or was a governed no-op.

A management tool or conformance harness SHALL NOT assume eventual effectiveness merely because an earlier response returned `PENDING`.

### 4.4 Prohibited direct mutation

A Governance Actuation Point SHALL NOT directly mutate a governed target merely because the caller has management authority.

A GAP SHALL NOT directly manufacture, replace, or inject:

- a Governance Decision;
- an Execution Authorization;
- a GRF current-eligibility or Commit-Bound Admissibility conclusion;
- a selected PEP Profile result;
- an Enforcement Context;
- a PEP acceptance/refusal result;
- an authoritative human identity/authorization/entitlement result; or
- an execution receipt.

Where management changes an authoritative source, entitlement, profile, governance package, configuration, or enforcement mapping, ordinary governed processing SHALL subsequently consume the changed authoritative condition through the normal qualification, GDF/PDP, authorization, GRF, and PEP path.

Management may administer the controlled artifacts that determine later behavior only when the caller is authorized for that administrative operation and the change is attributable, integrity-protected, and evidence-producing.

## 5. Management capability discovery

IF-003 SHALL provide machine-readable discovery of management and test-control capabilities.

Capability discovery SHALL distinguish availability from runtime binding.

Availability `status` SHALL use the controlled values in DS-047. `runtime_binding_status` SHALL use:

- `BOUND` — the advertised surface is connected to the runtime stage or authoritative source it claims to observe or control;
- `RECORD_ONLY` — the surface can accept/record requests or produce records but does not affect or originate from the claimed governed runtime path;
- `UNBOUND` — the implementation knows the surface is not connected to the claimed runtime path;
- `NOT_APPLICABLE`; or
- `UNKNOWN`.

An actuation/test-control surface advertised as `RECORD_ONLY`, `UNBOUND`, or `UNKNOWN` SHALL NOT be treated as capable of establishing a Formal Test Case precondition.

Actuation and test-control capability records SHALL also identify whether status readback is supported.

For `TARGET_EXECUTION_FIXTURE`, capability discovery SHALL identify supported execution modes, terminal outcomes, and whether deterministic virtual-time release is supported. For `ENFORCEMENT_PATH_FAULT_FIXTURE`, capability discovery SHALL identify supported fault targets, fault modes, and injection points. A controller SHALL NOT infer support for a variant merely because the parent `control_type` is advertised.

Capability discovery SHALL identify whether test-scope propagation, management/test correlation, and authorized IF-005 control enumeration/recovery are supported.

Discovery SHALL NOT claim that presence of an interface establishes conformance with any CR or TC.

## 6. Security and authority

Every protected management operation SHALL require authentication and authorization appropriate to its effect.

Actuation SHALL enforce:

- principal attribution;
- Tenant scope;
- Governance Domain scope where applicable;
- operation-specific administrative authority;
- replay protection;
- idempotency for retriable state-changing operations;
- validity/expiry where applicable; and
- least-privilege separation between observe, production actuation, test-control, and cross-scope test-control recovery authority.

Management credentials and management authorization SHALL NOT substitute for:

- an authoritative Human Governance Principal or IAS-resolved human entitlement;
- GDF/PDP workload authority;
- GRF workload authority;
- PEP authority; or
- target-mutation authority.

Changes to IAS Profiles, identity/entitlement source bindings, PEP Profiles, PEP selection rules, GRF-to-PEP trust bindings, or target-authority configuration are governance-significant administrative changes and SHALL receive the same attribution, authorization, integrity, and evidence controls applicable to comparable governance configuration changes.

Cross-tenant and cross-domain management access SHALL be denied unless explicitly authorized by controlling governance policy and any applicable AGCP isolation requirements.

## 7. Evidence and ledger requirements

A governance-significant actuation SHALL produce attributable Governance Evidence. Where the actuation changes an authoritative governance condition, the resulting authoritative event SHALL be recorded through the normal Governance Ledger mechanism where required by the controlling AGCP baseline.

Observation telemetry MAY be recorded separately from the Governance Ledger. Telemetry SHALL NOT be treated as authoritative merely because it is emitted by a GOP.

An EFFECTIVE actuation result SHALL be reproducibly traceable to the authoritative change it represents.

## 8. Relationship to isolated test scope

Production management actuation and IF-005 test actuation are distinct.

When IF-005 is implemented, IF-001 requests MAY carry the optional `X-AGCP-Test-Scope` header defined by the IF-001 contract. The header SHALL be honored only when the caller and scope are authorized for isolated test control. Unauthorized production requests SHALL NOT silently receive test-scoped governance inputs.

The detailed source-overlay, finite-lease, readback, consumption, reset, and recovery rules are defined by the AGCP Conformance Test Control Specification.

Where IF-005 control enumeration is implemented, ordinary test controllers SHALL be limited to their authorized test scopes. Cross-scope enumeration used to recover orphaned active controls after controller restart SHALL require explicit recovery/administrative authority and SHALL remain attributable and auditable.

## 9. Conformance and assessment use

A conformance harness MAY use GOPs to observe Formal Test Case behavior and MAY use GAPs to establish legitimate preconditions that a production administrator could establish.

A successful management request is setup evidence only. The harness SHALL wait for authoritative realization when the Formal Test Case depends on the changed condition.

The target runtime's behavior after the precondition is effective determines the CR/TC result.

The optional IF-005 test-control interface is governed by `AGCP-Conformance-Test-Control-Specification.md` and SHALL remain logically distinguishable from production management actuation.

## 10. Machine-readable contracts

The machine-readable interface contract is `api/AGCP-Management-Contract.yaml`.

Controlled schemas:

- DS-046 Governance Observation Event;
- DS-047 Management Capabilities Response;
- DS-048 Governance Actuation Request;
- DS-049 Governance Actuation Result; and
- DS-050/DS-051 test-control records as defined by the companion test-control specification, including per-operation runtime binding, finite-lease readback, variant discovery, and authorized active-control recovery.
## Runtime-coupling truthfulness

A Management Plane capability SHALL advertise `runtime_binding_status: BOUND` only after the implementation can demonstrate that the corresponding operation is consumed by the same authoritative source-resolution, qualification, lifecycle, or enforcement path used by ordinary governed processing. A record-only handler, queue-only handler, disconnected metadata store, or handler that changes only a management readback SHALL report `RECORD_ONLY` or `UNBOUND`, not `BOUND`.

For an actuation to become `EFFECTIVE`, the implementation SHALL persist or realize the authoritative governance condition through the normal governed administrative path, and its readback SHALL identify authoritative artifacts, Governance Evidence, and correlated observations sufficient to prove the effect.

Management-generated authoritative records SHALL validate against their controlled DS schemas before they are persisted, exposed as authoritative, or referenced by the Governance Ledger.

## Machine-readable v2.1.0 synchronization

DS-046 observations distinguish Identity and Authorization Qualification, GDF/PDP decision, Authority Re-Derivation, Governance Realization, PEP enforcement, commitment, and post-commit execution. IF-004 management authority remains separate from those governance authorities.
