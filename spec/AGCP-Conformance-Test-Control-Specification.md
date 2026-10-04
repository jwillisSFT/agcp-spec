# AGCP Conformance Test Control Specification

**Artifact Lifecycle:** CURRENT  
**Baseline Status:** Public Review Controlled Baseline  
**Document status:** Normative Companion Specification for optional test control  
**Specification Version:** 2.1.0  
**Repository Release Target:** AGCP v2.1.0  
**Baseline Date:** 2026-08-15  
**Interface ID:** IF-005

## 1. Purpose

This specification defines an optional, isolated Conformance Test Control Plane for establishing deterministic Formal Test Case preconditions that cannot reliably be established through the ordinary public runtime or production Management Plane.

IF-005 exists to improve executable metrology. It SHALL NOT be required merely to claim an AGCP conformance level unless an adopted profile expressly requires it. Lack of IF-005 SHALL NOT convert an otherwise unobservable requirement into Pass; assessment disposition remains governed by the Formal Test Case and assessment methodology.

## 2. Test-only separation

IF-005 SHALL be disabled by default in production deployments. An implementation exposing IF-005 SHALL:

- require an explicit isolated test scope;
- require dedicated test-control authority;
- identify all resulting control records as test-originated;
- prevent test controls from silently entering a production Governance Domain;
- preserve evidence sufficient to distinguish setup from target behavior;
- provide deterministic cleanup or scope reset; and
- prevent test-scoped inputs from leaking into requests that do not carry the same authorized test scope.

Production distributions MAY compile IF-005 out entirely.

## 3. Standard test controls and typed payloads

The controlled operation vocabulary is:

- `VIRTUAL_TIME_SET`
- `VIRTUAL_TIME_ADVANCE`
- `AUTHORITATIVE_SOURCE_FIXTURE`
- `AUTHORITATIVE_SOURCE_FAILURE`
- `CANONICAL_STATE_FIXTURE`
- `EVIDENCE_FIXTURE`
- `AUTHORITY_FIXTURE`
- `DELEGATION_FIXTURE`
- `HUMAN_REVIEW_FIXTURE`
- `TENANT_STATE_FIXTURE`
- `GOVERNANCE_DOMAIN_FIXTURE`
- `DEGRADATION_FIXTURE`
- `COMPOSITE_GOVERNANCE_FIXTURE`
- `GOVERNANCE_CONFIGURATION_FIXTURE`
- `PEP_OUTCOME_FIXTURE`
- `TARGET_EXECUTION_FIXTURE`
- `ENFORCEMENT_PATH_FAULT_FIXTURE`
- `RESET_TEST_SCOPE`

Every non-reset operation SHALL carry the type-specific fixture defined by DS-050. A generic untyped object is not sufficient for an implementation to claim interoperable support for the control.

Implementations MAY support a subset and SHALL advertise the supported subset through IF-003 capability discovery.

## 4. Scoped runtime binding model

Applying a test-control record SHALL NOT be implemented as a disconnected metadata operation when the capability is advertised as runtime-bound.

For each advertised `runtime_binding_status: BOUND` control type, the implementation SHALL connect the isolated Test Control Store to the corresponding authoritative-source adapter, external-dependency adapter, or controlled boundary-fault adapter used by ordinary governed processing.

The required processing model is:

```text
IF-005 Test Control
        |
        v
Isolated Test Control Store
        |
        v
Test-Scope Source Adapter / Overlay
        |
        v
Ordinary AGCP Authoritative Source Resolution
        |
        v
Normal Qualification / Evaluation / Commit Pipeline
```

The adapter SHALL alter only the input/source condition being controlled. It SHALL NOT skip the normal governance stage that consumes that source.

### 4.1 Test-scope propagation

A governed IF-001 request that is intended to consume an isolated test condition SHALL carry the same `X-AGCP-Test-Scope` value used when the condition was created.

The implementation SHALL propagate that test scope through all internal calls necessary to resolve the affected source or dependency.

If the request does not carry the authorized matching scope, ordinary production sources SHALL be used and the isolated fixture SHALL have no effect.

### 4.2 Overlay precedence

Within an authorized isolated test scope, a matching effective test fixture MAY replace or simulate the specific authoritative-source/dependency input identified by the control.

The replacement SHALL be explicit and attributable. GOP evidence SHALL make the selected test-scoped source identifiable.

Test fixtures SHALL NOT alter unrelated source classes, Tenants, Governance Domains, Proposals, or test scopes.

## 5. Acceptance, effect, and consumption are separate

A test-control operation has three separate dimensions:

1. **Acceptance** — whether the control request was admitted;
2. **Effect** — whether the scoped runtime source adapter is ready to supply the condition to matching governed requests; and
3. **Consumption** — whether a governed runtime processing attempt actually consumed the condition.

DS-051 SHALL represent these dimensions separately.

An HTTP 2xx response or `acceptance_status: ACCEPTED` SHALL NOT establish the precondition.

A control may be used as a Formal Test Case precondition only after readback reports:

```text
runtime_binding_status = BOUND
effect_status = EFFECTIVE
```

For a Formal Test Case whose determination depends on proving that the condition was used, the evidence package SHALL additionally establish:

```text
consumption_status = OBSERVED
```

with a consumed-by reference and correlated GOP observation.

`effect_status: EFFECTIVE` SHALL NOT be returned if the implementation has only stored or logged the control and ordinary governed processing will ignore it.


## 5A. Optional correlation identifier serialization

`correlation_id` is optional on DS-050 requests and DS-051 results. Absence and JSON `null` are not equivalent.

When a request omits `correlation_id`, an implementation SHALL:

- accept the otherwise valid request without requiring an invented correlation value;
- preserve the field as absent in internal option/nullable-language representations;
- omit `correlation_id` from DS-051 serialization unless a non-empty string value exists; and
- SHALL NOT serialize `correlation_id: null`, because DS-051 does not admit JSON null for that property.

An omitted optional correlation identifier SHALL NOT cause HTTP 500, internal schema-validation failure, or rejection of an otherwise valid control. Harness check `MP-TC-008` verifies this behavior.

## 6. Status/readback

IF-005 SHALL provide control status/readback through:

`GET /agcp/test/v1/controls/{operation_id}`

The readback operation SHALL require the same isolated test scope and test-control authority rules as the original control.

A conformance harness SHALL poll or otherwise observe the result until the control becomes EFFECTIVE, fails, expires, or reaches another terminal control state. A harness SHALL NOT infer effectiveness from elapsed time.

## 7. No outcome injection

A test control MAY establish an input condition, dependency condition, simulated authoritative source, time condition, identity/authorization condition, or external enforcement result where the Formal Test Case requires such a controllable dependency.

A test control SHALL NOT directly inject:

- `Pass`, `Partial`, `Fail`, or `Not Assessed`;
- a desired Governance Decision;
- a desired Execution Authorization;
- a desired GRF current-eligibility or Commit-Bound Admissibility conclusion;
- a selected PEP Profile or profile-mapping success result;
- a constructed Enforcement Context intended to bypass normal GRF processing;
- a desired Structural Refusal;
- a desired Derived Lifecycle State;
- a desired Commit Boundary outcome; or
- any other expected governance conclusion whose derivation is the behavior under test.

The target runtime SHALL still perform the applicable qualification, GDF/PDP, authorization, Governance Realization, and PEP processing.


### 7.1 Controlled boundary-fault injection

`ENFORCEMENT_PATH_FAULT_FIXTURE` MAY perturb an implementation-generated artifact or authenticated boundary condition only after the ordinary producing stage has completed and only at the declared isolated injection point. The control SHALL NOT replace the producing stage, construct the entire artifact under test, skip GRF processing, or directly establish the consuming stage's refusal, commitment, or governance result.

The harness SHALL preserve mutation evidence sufficient to identify the injection point, fault target, affected field when applicable, and pre-/post-mutation digests. Ordinary PEP or logical-boundary validation SHALL remain responsible for detecting the fault and determining the enforcement result.

## 8. Virtual time

Virtual time controls SHALL be scoped to the declared isolated test scope, deterministic, observable, and reversible. They SHALL NOT alter the host clock or unrelated Tenant/Governance Domain processing.

All temporal validity logic exercised by a scoped governed request SHALL use the scoped time adapter consistently for that request.

## 9. Fixture controls

Fixture controls SHALL identify whether the fixture models an authoritative source, qualified evidence source, identity/authorization/entitlement source, authority/delegation source, human-review condition, Tenant or Governance Domain state, composite dependency, Governance Configuration, degradation condition, or PEP/external effect.

`AUTHORITY_FIXTURE` MAY represent test-scoped source conditions such as active/disabled subject status, role, group, entitlement, reviewer class, governance permission, scope, delegation, effective period, or revocation state when those are inputs to the behavior under test. Such a fixture represents the source condition only; it does not directly create a Governance Approval Artifact, Governance Decision, Execution Authorization, or commit result.

The fixture SHALL be attributable to the test controller and SHALL be distinguishable from target-generated Governance Evidence.

A fixture that is intended to behave as a source used by governance evaluation or realization SHALL be selected by the same source-resolution path used in the corresponding production behavior, except for the explicit isolated source substitution.

## 10. PEP outcome control

`PEP_OUTCOME_FIXTURE` MAY emulate an external enforcement target only where the behavior under test is the AGCP governance reaction to that external result. It SHALL NOT be used to claim that a real external PEP is implemented or non-bypassable.

`PEP_OUTCOME_FIXTURE` SHALL NOT substitute for GRF application of the controlling PEP Profile, Governance Binding Validation, Enforcement Context construction, or any other normal commitment processing whose behavior is under test.


## 10A. Post-commit target execution control

`TARGET_EXECUTION_FIXTURE` MAY emulate a post-commit asynchronous target dependency where the assessed profile separates commitment from completed target execution. The fixture SHALL control only the external target condition and its deterministic release. It SHALL NOT directly create DS-052, a Derived Lifecycle State, or any governance result.

Where deterministic delay is required, `VIRTUAL_TIME_ADVANCE` SHOULD be used to release the target condition. The target/runtime SHALL generate the resulting DS-052 Governed Execution Outcome and any subsequent lifecycle derivation through the ordinary execution-outcome path.

## 11. Reset semantics

`RESET_TEST_SCOPE` SHALL remove or deactivate every test-originated condition in the named isolated scope and restore future requests in that scope to the ordinary source-selection baseline unless new controls are applied.

Reset SHALL NOT delete or rewrite historical evidence showing that a test control previously existed or was consumed.

## 12. External-dependency limitation

IF-005 cannot replace an independent implementation, alternate transport, or independent deployment when the Formal Test Case explicitly requires one. Such requirements remain external dependencies.

## 13. Evidence preservation

Every admitted test control SHALL produce a Test Control Result recording:

- control operation identity;
- test scope;
- control type;
- applying principal;
- acceptance status;
- current effect status;
- effective condition and digest when effective;
- source adapter identity when effective;
- consumption status and consuming request/artifact references when observed;
- application/effect/consumption times as applicable;
- cleanup/reset requirement; and
- integrity digest.

Applicable GOP observations SHALL link the governed runtime processing attempt to the test condition and selected source.

Formal Test Case evidence packages SHOULD preserve the control request/result separately from target request/response, observation, ledger, and restart artifacts.

## 14. Controlled mapping

`conformance/test-control-mapping.json` provides a non-normative execution aid mapping each controlled TC to recommended observation/test-control surfaces or explicit external dependencies.

The mapping SHALL NOT treat `RECORD_ONLY`, `UNBOUND`, `PENDING`, or merely accepted test controls as established preconditions. Formal TCs remain the authoritative assessment procedures.

The machine-readable interface contract is `api/AGCP-Management-Contract.yaml` and the controlled request/result schemas are DS-050 and DS-051.

## Machine-readable v2.1.0 synchronization

DS-050 AUTHORITY_FIXTURE can emulate authoritative account status, roles, groups, entitlements, authorization attributes, permissions, revocation, and freshness. PEP_OUTCOME_FIXTURE is consumed only at enforcement. TARGET_EXECUTION_FIXTURE is consumed only by the post-commit target/execution dependency path. ENFORCEMENT_PATH_FAULT_FIXTURE may perturb only the declared post-production enforcement boundary condition. None may inject a Governance Decision, Execution Authorization, GRF commit result, DS-052 outcome, or conformance result.
