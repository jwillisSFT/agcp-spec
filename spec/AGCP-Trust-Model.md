# AGCP Trust Model

**Document status:** Architectural Trust Model  
**Scope:** Artificial Intelligence Governance Control Plane (AGCP)  
**Purpose:** Define the principal identities, trust boundaries, authority relationships, credential-separation requirements, human-governance semantics, governance-decision-to-realization-to-enforcement relationship, and implementation-profile obligations required to preserve governance from proposal through controlled execution.

---

## 1. Purpose

The AGCP Trust Model defines the security relationships required for a governed action to progress from proposal to operational consequence without collapsing reasoning, governance decision, authorization, commitment, enforcement, and execution into a single authority.

AGCP operates on the principle that:

- a proposal is not execution;
- a Governance Decision is not, by itself, commit-bound authority;
- an Execution Authorization is not, by itself, permission to execute;
- authentication alone does not establish governance authority;
- human approval is governance input, not direct execution authority;
- current execution eligibility must be established at commitment; and
- a governed consequence must cross the declared enforcement boundary.

The architecture therefore separates:

```text
proposal formation
        ↓
identity and context qualification
        ↓
governance evaluation
        ↓
Governance Decision
        ↓
human governance input / re-evaluation, when required
        ↓
Execution Authorization
        ↓
Governance Realization / commit-time revalidation
        ↓
policy enforcement
        ↓
governed target effect
        ↓
evidence and lifecycle recording
```

Within this model:

- the **Policy Decision Point (PDP)** is the policy-decision functional role realized by the AGCP **Governance Decision Function**;
- the **Governance Realization Function (GRF)** establishes whether an already-authorized transition remains eligible to proceed at commitment and prepares the enforcement-facing realization of that transition; and
- the **Policy Enforcement Point (PEP)** controls whether the governed transition can cross the enforcement boundary.

A Governance Decision alone does not establish commit-bound execution eligibility.

---

## 2. Scope and Architectural Level

This document is an **architectural trust model**.

It defines:

- principal classes;
- logical governance functions;
- authority boundaries;
- identity and credential separation;
- trust relationships;
- human-governance identity requirements;
- Governance Decision Function / PDP semantics;
- Governance Realization Function semantics;
- GRF-to-PEP trust semantics;
- PEP-to-target trust semantics;
- requirements for implementation-selected identity and enforcement profiles;
- credential non-substitution;
- fail-closed and non-bypassability expectations;
- management and test-control separation.

It does **not** prescribe:

- a particular identity provider;
- a particular credential technology;
- a particular secrets-management technology;
- a particular network topology;
- a particular programming language;
- a particular PEP product;
- a particular target system;
- concrete governed-action mappings;
- deployment-specific usernames, keys, tokens, paths, hostnames, or service names.

Those choices belong in Implementation Profiles and deployment-specific configuration.

AGCP is a reference control-plane realization within the broader Runtime Governance Architecture. The architecture deliberately separates general trust semantics from particular technical realizations.

Logical functions defined in this Trust Model may be implemented as separate services or co-located within one service. Co-location does not erase their logical responsibilities, sequencing, evidence, or testable trust relationships.

---

## 3. Core Trust Principles

### 3.1 Proposal is not authority

A proposer may state a requested action and supporting evidence, but the proposer does not determine that its own proposal is admissible, authorized, current, or executable.

A proposal remains untrusted until the required identity, provenance, schema, integrity, governance, state, evidence, authority, and lifecycle requirements have been established.

### 3.2 Authentication is not governance authorization

Authentication establishes the identity of a human or workload.

It does not, by itself, establish that:

- the actor is authorized for a particular governance role;
- the proposal is admissible;
- the requested target or action is allowed;
- required approvals exist;
- governance state remains current;
- commitment is allowed;
- execution may occur.

### 3.3 Governance Decision is distinct from commitment

The Governance Decision Function, acting in the PDP role, evaluates applicable governance and renders a decision.

A favorable Governance Decision is one input to later authorization and commitment processing. It does not, by itself, establish that the transition remains eligible when commitment is attempted.

### 3.4 Commitment is distinct from enforcement

The Governance Realization Function establishes whether the exact authorized transition is still eligible to proceed under current commitment-sensitive conditions.

The PEP then controls whether that transition crosses the enforcement boundary.

The GRF and PEP are therefore distinct logical functions even when they are deployed within the same product or service boundary.

### 3.5 Current authority is required at commitment

A prior favorable decision does not create permanent authority.

Before the governed transition is presented for enforcement, the GRF must establish that the conditions material to commitment remain valid, including as applicable:

- proposal identity and integrity;
- Governance Decision binding;
- authorization validity;
- governance version and authority basis;
- human approvals and delegations;
- target binding;
- required Canonical State;
- lifecycle eligibility;
- evidence validity;
- prior-use or single-use conditions;
- commitment-sensitive restrictions or revocations.

### 3.6 Human governance is governance input, not execution authority

A human reviewer contributes qualified governance input.

The human does not directly operate the PEP and does not acquire a portable execution credential by approving a proposal.

Human governance input may influence a Governance Decision, a re-evaluation, authorization conditions, or another defined governance outcome, but it remains distinct from commit-bound execution eligibility.

### 3.7 Credentials are not interchangeable authority

Possession of a valid credential for one principal or interface does not authorize use of another principal's interface or authority.

In particular:

- proposer credentials are not human-governance credentials;
- proposer credentials are not protected control-plane credentials;
- human-review credentials are not protected workload credentials;
- management credentials are not governance-decision authority;
- management credentials are not Governance Realization authority;
- test-control credentials are not management credentials;
- control-plane credentials are not PEP target credentials;
- PEP credentials are not operator credentials.

Where the Governance Decision Function and Governance Realization Function are deployed as separate workloads across a trust boundary, their workload identities must be independently scoped. Where they are co-located within one protected control-plane service, an Implementation Profile may assign a shared service identity without collapsing their logical responsibilities.

### 3.8 No governed consequence without enforcement

Within an implementation's declared governance scope, a governed target effect must not be realizable through an alternate path that bypasses the intended enforcement point.

The assurance claim must be scoped to the actual reachable mutation paths.

---

## 4. Principal and Functional Model

AGCP distinguishes human principals, workload principals, logical governance functions, governance artifacts, and target authority.

A **principal** is an actor or workload that can be authenticated or attributed.

A **logical function** is a defined governance responsibility that may be implemented by one or more principals or co-located with other functions.

Co-location does not erase logical distinctions that are material to governance, evidence, testing, or assurance.

### 4.1 Developer

A Developer is a human principal who creates, tests, configures, or operates proposal-producing applications or agents.

A Developer may authenticate to development or proposal-facing interfaces according to the controlling Implementation Profile.

Developer authority does not include:

- asserting governance outcomes;
- fabricating authoritative state;
- creating authoritative human-governance approvals on behalf of another human;
- invoking protected realization or enforcement interfaces without the required authority;
- invoking governed targets using enforcement credentials;
- modifying protected governance state merely because the developer can submit proposals.

### 4.2 Agent or Proposal-Producing Workload

An Agent is a non-human workload principal that may create or manage permitted proposal-side objects.

Each independently operating agent or proposal-producing workload must have a workload identity appropriate to its trust boundary.

Agent identity establishes proposal provenance. It does not establish governance authority.

### 4.3 Human Governance Principal

A Human Governance Principal is an authenticated human whose judgment may become qualified governance input.

Examples include:

- approval;
- rejection;
- adjudication;
- risk acceptance;
- exception judgment;
- escalation decision;
- specialist review.

The human's authority must be qualified independently of the human's assertion.

### 4.4 Identity and Trust Service

An Identity and Trust Service is an authoritative or qualified source of identity information used by AGCP.

Its responsibilities may include:

- resolving authenticated subjects;
- establishing stable account identity;
- resolving workload identity;
- validating credential state;
- establishing tenant or organizational affiliation;
- resolving governance roles or eligibility;
- providing identity provenance.

An implementation must declare the authoritative identity source through its controlling Implementation Profile.

### 4.5 Canonical-State Source or Adapter

A Canonical-State Source supplies governance-relevant authoritative state.

Its authority is bounded to the facts for which it is declared authoritative.

A state provider trusted for one fact must not automatically be treated as authoritative for unrelated governance facts.

### 4.6 Governance Repository / Activation Authority

The Governance Repository or activation service supplies the governance artifacts that the AGCP control plane is authorized to evaluate.

Its trust responsibilities include, as applicable:

- package identity;
- version;
- integrity;
- provenance;
- activation status;
- supersession status;
- tenant/domain applicability.

### 4.7 Governance Decision Function / Policy Decision Point

The **Governance Decision Function (GDF)** is the AGCP logical function that performs policy and governance evaluation and renders a Governance Decision.

Within AGCP, the GDF realizes the **Policy Decision Point (PDP)** functional role.

The GDF/PDP may evaluate, as applicable:

- policy rules;
- constraints;
- invariants;
- identity attributes;
- authorization posture;
- qualified Canonical State;
- evidence;
- human-governance requirements;
- escalation conditions;
- applicable governance-package content.

The GDF/PDP may determine that a proposal is:

- authorized;
- denied;
- structurally refused;
- pending human review;
- deferred;
- subject to governed re-evaluation;
- or another outcome defined by the applicable specification and profile.

A Governance Decision produced by the GDF/PDP does **not** by itself establish commit-bound execution eligibility.

The GDF/PDP may be re-invoked during later governance processing when current conditions require governed re-evaluation. Re-invocation does not transform the GDF/PDP into the Governance Realization Function.

### 4.8 Governance Realization Function

The **Governance Realization Function (GRF)** is the AGCP logical function that establishes whether an already-authorized governed transition remains eligible to proceed at the commitment boundary.

The GRF does not replace or reinterpret the Governance Decision Function.

Its responsibilities include, as applicable:

- validating the applicable Execution Authorization;
- confirming proposal identity and content binding;
- confirming decision and authorization binding;
- re-establishing current authority;
- validating commitment-sensitive Canonical State;
- validating required human approval or delegation status;
- validating target binding;
- validating lifecycle eligibility;
- validating evidence freshness and applicability;
- validating prior-use, replay, or single-use conditions;
- determining whether governed re-evaluation is required;
- selecting the applicable PEP Profile;
- applying the PEP Profile to the exact commit-eligible transition;
- constructing or completing the Enforcement Context;
- invoking the selected PEP through the protected enforcement path.

The GRF may be implemented in the same service as the GDF/PDP or as a separate protected service.

When co-located, their logical responsibilities must remain distinguishable in implementation behavior, evidence, and testing.

### 4.9 Policy Enforcement Point

The **PEP** is the non-human enforcement function that controls the governed execution boundary.

The PEP:

- accepts enforcement requests only through the authorized governance path;
- authenticates or otherwise verifies the authorized control-plane caller according to the controlling profile;
- validates the execution-relevant authorization and bindings required by its interface and PEP Profile;
- rejects unsupported, invalid, stale, replayed, mismatched, or otherwise ineligible invocations;
- applies or mediates the allowed target operation defined by the selected PEP Profile;
- invokes the governed target using authority unavailable to proposal-side principals;
- records or returns execution evidence as required by the profile.

The PEP does not independently reinterpret the policy basis for the Governance Decision.

### 4.10 Governed Target or Execution Adapter

The Governed Target is the system whose authoritative state or external behavior can be changed.

A target-specific adapter may stand between the PEP and the underlying target.

Within the declared governance scope, the target or adapter must accept governed mutations only through the authorized PEP path.

### 4.11 Ledger / Evidence Service

Where implemented as an independent workload, the Ledger or Evidence Service is a non-human principal authorized to record or preserve governance lifecycle and execution evidence.

Ledger-writing authority must remain distinct from ordinary proposer authority.

### 4.12 Management-Plane Workload

A Management-Plane Workload is a non-human service supporting governance observation or authorized administrative actuation.

The existence of management interfaces in AGCP does not require every implementation to deploy a management plane.

A management-plane workload:

- possesses its own service identity where it crosses an independent trust boundary;
- may act only within its declared management authority;
- must not manufacture human governance authority;
- must not substitute its credential for GDF/PDP, GRF, PEP, or target authority.

### 4.13 Test-Control Principal

A Test-Control Principal is a non-human principal authorized to invoke explicitly declared test and injection mechanisms.

Test-control authority is distinct from:

- developer authority;
- production management authority;
- governance-decision authority;
- Governance Realization authority;
- PEP authority.

A deployment may omit test-control capability entirely.

Where present, test-control mechanisms must remain explicitly scoped and isolated from production governance authority.

### 4.14 Operator / Provisioning Authority

The Operator or Provisioning Authority controls protected deployment functions such as:

- identity bootstrap;
- workload credentials;
- profile activation;
- trust anchors;
- cryptographic keys;
- tenant provisioning;
- service configuration;
- credential rotation and revocation.

Operator authority must not be implicitly granted to proposer workloads.

---

## 5. Principal and Credential Separation

Each non-human principal that independently crosses a trust boundary must use an independently scoped workload identity unless an Implementation Profile explicitly demonstrates that co-location removes that independent authentication boundary.

At minimum, an implementation must distinguish authority for:

```text
proposal-producing workloads

protected AGCP control-plane workload(s), including:
  - Governance Decision Function / PDP
  - Governance Realization Function
    when separately deployed

PEP

test control, when present

management, when present

operator/provisioning
```

Other independently deployed services, including identity, Canonical State, governance repository, and ledger/evidence services, should likewise possess service identities appropriate to their interfaces and authority.

Credential separation provides two different forms of protection:

1. **caller authentication** - establishes which workload is invoking an interface;
2. **governance binding** - establishes what exact governed transition is eligible.

Neither substitutes for the other.

A shared service identity for co-located GDF/PDP and GRF functions may be permitted by an Implementation Profile. Such co-location must not permit an earlier Governance Decision to bypass the GRF's current-authority and commitment checks.

---

## 6. Primary Governance Flow

The principal governance path is:

```text
Developer / Agent
      |
      | proposal identity / provenance
      v
Governed Action Proposal
      |
      v
Governance Decision Function / PDP
      |
      +-------------------------------+
      |                               |
      | automated progression         | human governance required
      |                               v
      |                       Human Governance Principal
      |                               |
      |                        authenticated identity
      |                               |
      |                               v
      |                        IAS Profile
      |                               |
      |                         qualified identity
      |                         and authority
      |                               |
      |                               v
      |                       proposal-bound human
      |                       governance artifact
      |                               |
      +-------------------------------+
      |
      v
Governance Decision / re-evaluation
      |
      v
Execution Authorization
      |
      v
Governance Realization Function
      |
      | current authority
      | current state/evidence
      | proposal/action/target binding
      | lifecycle/prior-use validation
      | selected PEP Profile
      | Enforcement Context
      v
Policy Enforcement Point
      |
      | PEP workload identity
      | +
      | profile-defined target operation
      v
Governed Target / Adapter
      |
      v
Execution outcome / evidence
      |
      v
Governance lifecycle / evidence record
```

---

## 7. Human-in-the-Loop Trust Model

### 7.1 Human identity

The human reviewer must be authenticated as a human principal.

A client-supplied name alone is not authoritative identity.

The implementation must qualify the authenticated subject against the authoritative identity source selected by its Implementation Profile.

### 7.2 Human authority

Authentication does not by itself establish governance eligibility.

The system must establish, as required by governance:

- stable human subject identity;
- current account status;
- tenant or organizational binding;
- governance domain;
- reviewer class or role;
- roles, groups, entitlements, governance permissions, and applicable scopes;
- delegation or authority;
- separation-of-duty requirements;
- quorum requirements;
- conflict constraints;
- validity conditions.

### 7.3 Proposal binding

A human governance artifact must be bound to the proposal or bounded sub-transition to which the human judgment applies.

The binding should carry sufficient information to prevent reuse of an approval for a different proposal, action, target, scope, tenant, or material proposal version.

Conceptually, human governance information may include:

```text
human_subject_id
authoritative_account_id
tenant_id
governance_domain
reviewer_role / reviewer_class
proposal_id or proposal_digest
approval / adjudication type
scope
conditions
issued_at
valid_until
authentication assurance
authority basis
provenance / issuer evidence
integrity protection
```

Where applicable:

```text
required_quorum
approval_sequence
separation-of-duty constraints
conflict-of-interest constraints
reason / justification
```

### 7.4 Human approval does not directly execute

Submitting or recording an approval does not invoke the PEP.

It creates a governance input.

The GDF/PDP must evaluate or re-evaluate the proposal with that input and all other applicable governance conditions.

If the resulting Governance Decision permits progression, authorization and Governance Realization still occur before the governed transition may reach the PEP.

---

## 8. Identity and Authorization Store Profile (IAS Profile)

An AGCP implementation that accepts governance-significant human or workload identity input must declare how authoritative identity and identity-system authorization/entitlement information is established through an **Identity and Authorization Store Profile (IAS Profile)** or equivalent implementation-profile section.

The IAS Profile is deployment-specific and is not part of the generic AGCP trust model.

It must define, at minimum:

- identity/authorization store identity and version where applicable;
- source/store type;
- authenticated-subject source;
- stable subject/account identifier;
- account-name or display attributes where relevant;
- lookup/resolution mechanism;
- tenant/domain relationship;
- account-validity semantics;
- roles, groups, entitlements, governance permissions, reviewer classes, scopes, and delegation/authority attributes where governance-significant;
- subject-to-governance-principal binding rules;
- authoritative fact scope and source precedence when multiple sources are used;
- freshness and cache behavior;
- failure behavior;
- service identity used for protected resolution; and
- required audit and provenance information.

IAS authorization/entitlement information is governance input. It is not AGCP Execution Authorization and does not itself produce a Governance Decision.

The IAS Profile must not permit a claimant to establish authoritative identity, role, entitlement, reviewer class, or governance authority merely by assertion.

Failure to resolve a required authoritative identity or authorization/entitlement fact must fail closed for governance actions that require that fact.

## 9. Governance Decision Function / PDP Trust and Authority

### 9.1 GDF/PDP role

The GDF/PDP is the AGCP function responsible for policy and governance evaluation.

It renders the Governance Decision.

It is not, by virtue of that role alone, the commit service or enforcement point.

### 9.2 GDF/PDP identity

Where the GDF/PDP is deployed as an independently authenticated workload, it must possess a workload identity appropriate to its protected control-plane authority.

That identity must be distinct from proposal-producing, human-review, management, test-control, and PEP target credentials.

Where the GDF/PDP and GRF are co-located in one protected service, the controlling Implementation Profile may define one control-plane service identity for both functions.

### 9.3 GDF/PDP authority

The GDF/PDP is trusted to evaluate the qualified governance inputs required by the applicable governance model and to render the resulting Governance Decision.

Its decision may participate in creation or qualification of an Execution Authorization.

The decision does not, by itself, establish that the transition is still eligible at commitment.

### 9.4 Re-evaluation

The GDF/PDP may be re-invoked when:

- human governance input is received;
- required state changes;
- authority changes;
- governance changes;
- evidence becomes stale;
- a prior decision requires re-evaluation;
- or another defined governance condition requires a new decision.

Re-evaluation must remain bound to the applicable proposal and governance context.

---

## 10. Governance Realization Function Trust and Authority

### 10.1 GRF role

The GRF is the AGCP function responsible for establishing current commit eligibility and realizing the authorized transition into an enforcement-ready form.

### 10.2 GRF identity

Where the GRF crosses an independent authentication boundary, it must possess a workload identity appropriate to its authority.

Where the GRF is co-located with the GDF/PDP, the controlling Implementation Profile may use a shared protected control-plane service identity.

Where the GRF is separately deployed, its credential must not be interchangeable with proposer, human-review, management, test-control, or PEP target credentials.

### 10.3 Commitment-time responsibility

Immediately before enforcement, the GRF must establish that the authorization remains applicable to the exact transition under current commitment-sensitive conditions.

A previously favorable Governance Decision or Execution Authorization must not be treated as permanently executable.

### 10.4 GRF use of the PEP Profile

The GRF is the AGCP function that applies the controlling **PEP Profile** to the commit-eligible governed transition.

The GRF uses the PEP Profile to:

- identify the appropriate PEP interface;
- identify the PEP-supported operation corresponding to the governed action;
- map canonical proposal and target fields into the enforcement representation;
- preserve required governance-significant bindings;
- determine required Enforcement Context fields;
- determine required caller-authentication properties;
- determine validity, replay, idempotency, and single-use requirements;
- determine profile-defined failure behavior;
- interpret PEP outcomes into AGCP execution and evidence semantics.

The GRF must not use the PEP Profile to change the Governance Decision or widen the authorized transition.

### 10.5 GRF credential is not unrestricted target authority

A GRF or control-plane workload credential authenticates the authorized governance caller to the PEP where required by the profile.

It does not by itself authorize an arbitrary target effect.

The enforcement request must additionally carry or reference the current proposal-bound authorization and Enforcement Context required by the applicable PEP Profile.

---

## 11. GRF-to-PEP Trust Boundary

The GRF-to-PEP boundary combines, as applicable:

```text
authorized control-plane / GRF caller authentication
        +
current governance authorization
        +
commit result / current eligibility
        +
proposal binding
        +
target/action binding
        +
required validity/state/lifecycle information
        +
PEP Profile binding
        +
Enforcement Context
```

The PEP must reject an invocation when any required property cannot be established.

The PEP must not accept:

- a Developer or Agent credential as protected control-plane authority;
- a Human Reviewer credential as protected control-plane authority;
- a Management credential as protected control-plane authority;
- a Test-Control credential as protected control-plane authority;
- an authorization bound to another proposal;
- an authorization bound to another target;
- expired or revoked authority;
- replay of a single-use authorization;
- an invalid or mismatched Enforcement Context;
- an operation unsupported by the selected PEP Profile;
- a request whose profile identity, version, or integrity binding is invalid where the profile requires such binding.

An implementation may co-locate the GRF and PEP, but co-location must not remove the logical requirement that current commit eligibility and enforcement bindings be validated before the target effect occurs.

---

## 12. PEP Profile

An implementation that connects a Governance Realization Function to a concrete PEP must declare an **implementation-specific PEP Profile**.

The PEP Profile defines how a canonical, commit-eligible governed transition and its authorization bindings map onto operations supported by the selected enforcement technology.

The PEP Profile must be separately identifiable and versioned or otherwise integrity-bound.

It should define, as applicable:

```text
PEP profile identity
profile version
profile digest

PEP implementation/interface identity

authorized GRF/control-plane caller requirements
PEP endpoint/interface binding

supported governed action types
supported target types

proposal-field to PEP-input mappings
required proposal fields
allowed deterministic transformations
target-identifier mappings

required authorization bindings
required commit/result bindings
required state/lifecycle bindings
required Enforcement Context fields
validity requirements
single-use/idempotency semantics

PEP response mappings
execution outcome mappings
evidence/receipt requirements

failure behavior
unsupported-action behavior

credential references
```

### 12.1 Binding preservation

A PEP Profile may transform representation, but must not change governance meaning.

It must preserve the bindings needed to establish:

- proposal identity;
- Governance Decision reference where required;
- Execution Authorization;
- governed action;
- target;
- tenant/domain;
- current commit eligibility;
- required current-state conditions;
- validity;
- execution constraints.

### 12.2 No approximate enforcement

If no valid mapping exists between the commit-eligible governed transition and a PEP-supported operation, the system must not:

- substitute a "similar" action;
- widen the target set;
- discard governance-significant fields;
- silently reduce restrictions;
- infer unsupported execution semantics.

The result must be non-execution through the profile-defined refusal, failure, or governed re-evaluation path.

### 12.3 No governance reinterpretation

The PEP Profile maps a governance-authorized, commit-eligible transition into an enforcement operation.

It does not perform a second independent policy interpretation and must not override the Governance Decision or GRF commitment result.

### 12.4 Profile selection

The implementation must define how the applicable PEP Profile is selected.

Profile selection must be deterministic for the governed action and target context within the controlling Implementation Profile.

A proposer must not be able to select an arbitrary PEP Profile in order to obtain a broader or weaker enforcement path.

---

## 13. PEP-to-Target Trust Boundary

The PEP must possess a workload identity or target credential distinct from ordinary proposal-side and control-plane credentials when the governed target exposes an independent authentication boundary.

The PEP credential answers:

> Is the caller an authorized enforcement workload?

The governance authorization and current commitment result answer:

> Is this exact consequence authorized and eligible now?

These are separate questions.

Within the declared governance scope:

- a Developer/Agent must not possess the PEP target credential;
- a Human Reviewer must not possess the PEP target credential;
- a Management workload must not possess the PEP target credential merely because it can administer governance;
- the GDF/PDP must not bypass the GRF/PEP path and use the target credential directly;
- the GRF must not bypass the PEP and use the target credential directly unless the implementation explicitly co-locates GRF and PEP while preserving equivalent enforcement semantics;
- Test Control must not substitute for PEP target authority.

---

## 14. Management-Plane Trust Model

A management plane is an optional implementation capability.

The Trust Model does not require that every deployment implement one.

Where present, the management plane may provide interfaces for:

- governance observation;
- controlled administrative actuation;
- profile/configuration management;
- key or trust management;
- human-review workflow;
- operational control.

A management-plane backend must possess its own service identity where it crosses an independent trust boundary.

A human operating through a management interface remains the human governance principal for governance-significant actions. The backend service identity must not replace the human identity in the resulting governance evidence.

Management authority does not itself authorize a governed operational effect.

Management authority must not substitute for GDF/PDP, GRF, PEP, or target authority.

---

## 15. Test and Injection Control

Test-control and injection mechanisms are a distinct trust domain.

They may exist to establish:

- authoritative test fixtures;
- simulated state;
- synthetic evidence;
- virtual time;
- controlled failure states;
- test authority or delegation conditions;
- test-only enforcement outcomes;
- other conformance or implementation-test conditions.

A Test-Control Principal must possess a distinct credential and scope where it crosses an independent trust boundary.

Test mechanisms must not be treated as production management authority.

An implementation may internally reuse adapters or source interfaces between management and test capabilities, but the authorization surfaces must remain distinct.

Test injection must not silently convert directly into a Governance Decision, Execution Authorization, commit result, or governed target effect where normal governance is required to consume and evaluate the injected condition.

---

## 16. Governance Artifacts Are Not Credentials

AGCP governance artifacts and workload credentials serve different purposes.

Examples of governance artifacts include:

- Governed Action Proposal;
- Governance Decision;
- human approval/adjudication artifact;
- Execution Authorization;
- Enforcement Context;
- commitment result;
- governance evidence;
- execution receipt.

A cryptographically valid governance artifact does not by itself prove that its presenter is an authorized workload.

Similarly, possession of a service credential does not prove that a particular governed transition is authorized or commit-eligible.

Secure operation requires both the appropriate **principal identity** and the appropriate **governance binding** where the interface requires them.

---

## 17. Non-Substitution Rules

The following authority substitutions are prohibited:

```text
Developer/Agent credential
    != Human Governance identity

Developer/Agent credential
    != protected AGCP control-plane authority

Human Governance identity
    != GDF/PDP workload authority

Human Governance identity
    != GRF workload authority

Management identity
    != Human Governance identity

Management identity
    != GDF/PDP authority

Management identity
    != GRF authority

Test-Control identity
    != Management identity

Test-Control identity
    != GDF/PDP authority

Test-Control identity
    != GRF authority

GDF/PDP decision
    != commit-bound execution eligibility

Execution Authorization
    != final execution permission by itself

GRF/control-plane identity
    != PEP target identity

Governance artifact
    != workload credential

Authentication
    != governance authorization

Human approval
    != execution authorization
```

An implementation must fail closed when a credential or artifact is presented outside its authorized trust domain.

Co-location may permit one protected workload identity to perform multiple AGCP logical functions, but it must not permit one function's result to substitute for the checks assigned to another logical stage.

---

## 18. Trust Boundaries

The principal AGCP trust boundaries are:

### 18.1 Proposer -> control plane

The proposal is untrusted until required identity, provenance, schema, integrity, and governance qualification occurs.

### 18.2 Identity service -> control plane

AGCP relies on qualified identity sources for human and workload identity assertions.

### 18.3 Canonical State -> control plane

Authoritative-state providers are trusted only for explicitly declared facts.

### 18.4 Governance repository -> control plane

The AGCP control plane relies on the repository or activation service for the correct active governance material.

### 18.5 Human Governance Principal -> control plane

Human judgments require verifiable identity, authority, scope, timing, and proposal binding.

### 18.6 Governance Decision Function -> Governance Realization Function

Where these functions are separated by an implementation boundary, the GRF must receive an integrity-protected Governance Decision and associated authorization/binding information sufficient to preserve the exact governed transition.

Where they are co-located, the implementation must preserve equivalent logical binding and evidence.

### 18.7 Governance Realization Function -> PEP

The PEP trusts the protected governance path to present a valid, current, profile-conformant enforcement request.

The governance path trusts the PEP to enforce refusal, binding, validity, and commitment conditions.

### 18.8 PEP -> governed target

The target trusts the PEP as the authorized enforcement principal for governed effects within the declared scope.

### 18.9 Target -> evidence/lifecycle system

Execution receipts and resulting-state evidence must be sufficiently trustworthy to establish the resulting operational outcome.

---

## 19. Security Boundaries

Security controls must protect, as applicable:

- proposer/governance separation;
- administrative interfaces;
- human identity resolution;
- Canonical State adapters;
- governance package activation;
- protected GDF/PDP functions;
- protected GRF functions;
- service credentials;
- authorization artifacts;
- GDF-to-GRF bindings where independently deployed;
- GRF-to-PEP channels;
- PEP Profile integrity and selection;
- Enforcement Context integrity;
- PEP credentials;
- target mutation paths;
- ledger/evidence writers;
- tenant/domain boundaries;
- test-control interfaces.

A proposal-producing principal must not automatically be able to:

- alter its own governance package;
- replace authoritative identity;
- replace Canonical State;
- write authoritative governance evidence;
- configure the GRF;
- configure or replace the selected PEP Profile;
- configure the PEP;
- obtain protected control-plane credentials;
- obtain PEP target credentials;
- invoke an alternate ungoverned target path.

---

## 20. Fail-Closed Requirements

AGCP must fail closed when a fact required to establish governance authority or execution eligibility cannot be qualified.

Examples include inability to establish:

- proposal integrity;
- authenticated workload identity;
- authenticated human identity;
- human authority;
- tenant/domain binding;
- active governance package;
- required Canonical State;
- required evidence;
- valid Governance Decision;
- valid Execution Authorization;
- target binding;
- current commit eligibility;
- authorized GRF/control-plane identity at the PEP;
- valid PEP Profile selection or mapping;
- valid Enforcement Context;
- PEP identity at the governed target;
- required validity/freshness;
- replay/single-use status.

Failing closed does not necessarily require a single universal lifecycle outcome. The applicable specification and Implementation Profile determine whether the result is denial, structural refusal, pending review, governed re-evaluation, deferred processing, execution failure, or another defined non-execution state.

---

## 21. Non-Bypassability

An implementation may claim non-bypassability only for the scope in which all relevant governed target mutation paths are mediated by the declared enforcement boundary.

The claim must identify:

- governed consequences;
- relevant GRF-to-PEP enforcement paths;
- selected PEPs;
- applicable PEP Profiles;
- protected targets/adapters;
- alternate administrative interfaces;
- recovery paths;
- privileged APIs;
- database or storage mutation paths;
- automation paths;
- operator exceptions, if any.

An unmanaged alternate path capable of producing the same governed consequence weakens or invalidates a full non-bypassability claim for that consequence.

A direct GRF-to-target path that bypasses the declared PEP also weakens or invalidates the non-bypassability claim unless the Implementation Profile explicitly defines the same component as both GRF and PEP and demonstrates equivalent enforcement semantics at the target boundary.

---

## 22. Implementation Profile Responsibilities

The generic AGCP Trust Model establishes required security semantics.

A controlling Implementation Profile specifies how a particular implementation realizes those semantics.

An Implementation Profile should identify, as applicable:

- implemented principal classes;
- logical GDF/PDP placement;
- logical GRF placement;
- whether GDF/PDP and GRF are co-located or independently deployed;
- process/service placement;
- trust-boundary placement;
- workload identity mechanisms;
- credential issuer;
- intended audience;
- scope/role model;
- tenant/domain binding;
- credential lifetime;
- credential storage/protection;
- rotation/revocation;
- interface acceptance rules;
- interface rejection rules;
- identity-and-authorization-store selection;
- IAS Profile;
- PEP selection;
- PEP Profile;
- GRF-to-PEP authentication and interface binding;
- PEP-to-target authentication and interface binding;
- governance-package source;
- Canonical-State sources;
- ledger/evidence realization;
- management capabilities;
- test-control capabilities;
- metadata and profile identities;
- claimed security and conformance scope.

An implementation-specific profile may narrow optional features, but must not silently weaken a mandatory trust invariant within the scope it claims to implement.

---

## 23. Metadata and Trust Representation

Runtime metadata should allow a client or assessor to determine which implementation and governing profile are actually active.

Where applicable, metadata should identify or bind:

- implementation identity and release;
- AGCP specification release;
- controlling Implementation Profile;
- profile version and digest;
- selected IAS Profile;
- selected PEP Profile or profiles;
- schema set;
- validator set;
- active governance;
- declared capabilities;
- interface contracts;
- conformance status;
- deployment binding when publicly safe.

Metadata is evidence about the running implementation. It must not substitute for enforcement of the trust model.

Development or example metadata must not be represented as a production or deployment-specific identity unless it accurately describes the running implementation.

---

## 24. Evidence and Attribution

Governance evidence should permit reconstruction of:

```text
who or what proposed the action
what exact transition was proposed
which identity and context were qualified
which governance material applied
which authoritative state was used
which human governance inputs were qualified
what the GDF/PDP decided
which Execution Authorization applied
what remained valid at commitment
what the GRF established
which PEP Profile was applied
which Enforcement Context was presented
which PEP accepted or refused the request
what target/effect was attempted
what actually occurred
what lifecycle state resulted
```

Evidence should record identifiers and integrity relationships without exposing raw secrets.

Where GDF/PDP, GRF, and PEP functions are co-located, evidence should still preserve the logical milestones necessary to distinguish decision, authorization, commitment, enforcement, and outcome.

---

## 25. Credential Protection

Credential protection must reflect the authority of the principal.

Implementation Profiles should define appropriate controls for:

- generation;
- issuance;
- provisioning;
- storage;
- access;
- rotation;
- expiration;
- revocation;
- compromise response;
- logging prohibition;
- disposal.

Secrets must not be embedded in governance evidence or metadata.

Where a credential must be accessible to a workload, its protection mechanism must prevent unrelated principals from acquiring or using it.

A developer-accessible credential is therefore not an appropriate substitute for a protected control-plane, GRF, PEP, test-control, or operator credential.

---

## 26. Architectural Invariants

The following invariants summarize this Trust Model.

**TM-01 - Proposal separation**  
A proposal does not establish its own admissibility or execution authority.

**TM-02 - Identity qualification**  
Governance-significant human and workload identities must be qualified through an authoritative or explicitly trusted identity mechanism.

**TM-03 - Human attribution**  
Human governance input must be attributable to the qualified human principal and bound to the governed proposal and applicable scope.

**TM-04 - Human non-execution**  
Human approval contributes governance input; it does not directly invoke enforcement.

**TM-05 - Governance Decision authority**  
The Governance Decision Function, acting in the PDP role, evaluates applicable governance and renders the Governance Decision; that decision alone does not establish commit-bound execution eligibility.

**TM-06 - Current authority**  
The Governance Realization Function must re-establish the commitment-sensitive conditions required for the exact governed transition before enforcement.

**TM-07 - Protected Governance Realization-to-enforcement path**  
Only the authorized Governance Realization / control-plane path may present a governed transition to the PEP within the claimed governance path.

**TM-08 - Authorization and commitment binding**  
Caller authentication alone is insufficient; enforcement must also be bound to the exact authorized and currently commit-eligible transition.

**TM-09 - PEP mediation**  
The PEP controls whether the governed transition crosses the enforcement boundary.

**TM-10 - PEP target authority**  
Only the PEP-controlled execution path may possess the authority required to produce the governed target effect within the claimed scope.

**TM-11 - Credential non-substitution**  
Credentials belonging to one trust principal or authority domain must not be accepted as authority belonging to another.

**TM-12 - PEP Profile fidelity**  
The Governance Realization Function must apply the selected PEP Profile in a manner that preserves the governed transition's authorization-significant and commitment-significant semantics.

**TM-13 - Unsupported enforcement refusal**  
If the configured PEP cannot safely realize the commit-eligible transition, no approximate or substituted effect may occur.

**TM-14 - Identity and authorization-store authority**  
A claimed human identity and any governance-significant role, group, entitlement, reviewer class, governance permission, scope, or delegation attribute must be resolved through the implementation-selected authoritative identity and authorization source before becoming governance-significant.

**TM-15 - Management separation**  
Management service authority does not itself constitute human governance, GDF/PDP, GRF, PEP, or target authority.

**TM-16 - Test-control separation**  
Test/injection authority must remain distinct from production governance and management authority.

**TM-17 - Evidence integrity**  
Governance and execution evidence must preserve attribution and binding sufficient for later reconstruction.

**TM-18 - Non-bypassability**  
Non-bypassability may be claimed only where all relevant paths to the governed consequence traverse the protected enforcement boundary.

**TM-19 - Fail closed**  
Missing, unverifiable, stale, conflicting, unsupported, or invalid authority required for decision, commitment, or execution results in non-execution.

**TM-20 - Profile-controlled realization**  
Deployment-specific identity, credential, PEP, PEP Profile, target, management, test-control, and metadata choices must be declared through controlled implementation-profile artifacts rather than implicitly embedded in generic AGCP semantics.

---

## 27. Reference Trust Flow

```text
                         HUMAN GOVERNANCE PATH

                    Authenticated Human
                            |
                            v
                    IAS Profile
                            |
                  qualified identity/authority
                            |
                            v
                 Proposal-bound HITL Artifact
                            |
                            |
                            v
+----------------+       +-----------------------------+
| Developer /    |       |                             |
| Agent          |------>| Governed Action Proposal    |
+----------------+       +-----------------------------+
                                  |
                                  v
                         +-------------------+
                         | Governance        |
                         | Decision Function |
                         |      / PDP        |
                         |                   |
                         | - policy          |
                         | - constraints     |
                         | - state/evidence  |
                         | - HITL            |
                         | - decision        |
                         +-------------------+
                                  |
                                  v
                         Governance Decision
                                  |
                                  v
                       Execution Authorization
                                  |
                                  v
                         +-------------------+
                         | Governance        |
                         | Realization       |
                         | Function          |
                         |                   |
                         | - current auth    |
                         | - current state   |
                         | - lifecycle       |
                         | - target binding  |
                         | - prior-use       |
                         | - PEP Profile     |
                         | - Enforcement     |
                         |   Context         |
                         +-------------------+
                                  |
                       protected control-plane
                         enforcement request
                                  |
                                  v
                         +-------------------+
                         |       PEP         |
                         |                   |
                         | validate bindings |
                         | control crossing  |
                         | of enforcement    |
                         | boundary          |
                         +-------------------+
                                  |
                       PEP workload identity
                                  |
                                  v
                         +-------------------+
                         | Governed Target / |
                         | Execution Adapter |
                         +-------------------+
                                  |
                                  v
                         Outcome / Evidence
                                  |
                                  v
                       Governance Lifecycle
```

---

## 28. Summary

The AGCP trust relationship is:

> **A proposer proposes. Qualified human authority may contribute bounded governance input. The Governance Decision Function, acting in the PDP role, evaluates the applicable governance basis and renders a Governance Decision. A favorable decision may support an Execution Authorization, but neither the decision nor the authorization alone establishes commitment. The Governance Realization Function re-establishes current execution eligibility, applies the selected PEP Profile, and constructs the enforcement-facing bindings and Enforcement Context for the exact governed transition. The PEP controls whether that transition crosses the enforcement boundary and uses protected enforcement authority to reach the governed target. The resulting decision, authorization, commitment, enforcement, outcome, and lifecycle remain attributable and reconstructable.**

No single credential represents that entire chain.

No human approval is a direct execution command.

No Governance Decision is commit-bound authority by itself.

No Execution Authorization is unconditional future permission to execute.

No GRF or control-plane credential is unrestricted authority to mutate targets.

No PEP credential creates governance authority by itself.

No PEP Profile may reinterpret or widen the governed transition.

No management or test-control identity substitutes for normal governance.

No implementation may claim a governed execution path is non-bypassable when the same consequence remains reachable outside the protected enforcement boundary.
