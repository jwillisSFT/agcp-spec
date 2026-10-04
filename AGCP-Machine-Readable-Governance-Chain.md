# AGCP Machine-Readable Governance Chain

## Artifact Relationships and Runtime Progression

**Document status:** Informative architecture and implementation guidance  
**Scope:** Artificial Intelligence Governance Control Plane (AGCP)  
**Audience:** Implementers, integrators, reviewers, students, and instructors  
**Purpose:** Explain how AGCP architectural functions and machine-readable artifacts relate to one another from authenticated identity through governed execution, lifecycle, evidence, receipt, and ledger recording.

---

## 1. Purpose and Scope

This document explains the end-to-end machine-readable governance chain used by AGCP. It connects the architectural concepts defined by the AGCP Core, Architecture Reference Model, Trust Model, companion specifications, and Implementation Profile framework to the concrete Data Schema (DS) artifacts exchanged or produced during runtime governance.

This document is **informative**. It does not create new conformance requirements and does not supersede the AGCP Core, published Normative Statements, applicable Companion Specifications, Implementation Profiles, schemas, or interface contracts. If this document appears to conflict with a normative AGCP artifact, the applicable normative artifact controls.

The central design principle is that each stage answers a different governance question. An earlier result does not substitute for a later determination. In particular:

- authentication is not governance authority;
- identity-store authorization or entitlement is not AGCP Execution Authorization;
- a Governance Decision is not Execution Authorization;
- Execution Authorization is not current commit eligibility;
- the Governance Decision Function is not the Governance Realization Function;
- PEP enforcement is not policy decision-making;
- commitment is not always completed operational execution;
- evidence, receipts, lifecycle records, and ledger events record governance history but do not create new authority.

---

## 2. End-to-End Machine-Readable Chain

The corrected runtime progression is:

```text
Authenticated Principal
        |
        v
Identity and Authorization Store (IAS) Profile
        |
        v
DS-053 Identity and Authorization Qualification Result
        |
        v
Governance Decision Function (GDF) / Policy Decision Point (PDP)
        |
        v
DS-015 Governance Decision Result
        |
        v
DS-017 Execution Authorization
        |
        v
DS-018 Commit Boundary Request
        |
        v
Governance Realization Function (GRF)
   + DS-034 Authority Re-Derivation Result
   + current Canonical State
   + current qualified evidence
   + lifecycle / validity / binding checks
   + selected PEP Profile
        |
        v
DS-029 Enforcement Context
        |
        v
Policy Enforcement Point (PEP)
        |
        v
DS-019 Commit Boundary Result
        |
        | if operational execution is distinct from commitment
        v
DS-052 Governed Execution Outcome
        |
        v
DS-038 Governance Lifecycle Record
DS-020 Governance Evidence
DS-027 Governance Receipt
DS-040 Governance Ledger Event
```

A key sequencing point is that **DS-018 Commit Boundary Request initiates GRF processing**. The requester does not authoritatively supply DS-029 Enforcement Context. The GRF constructs DS-029 only after it independently re-establishes current commitment-sensitive conditions and applies the selected PEP Profile.

---

## 3. Runtime Progression

### Step 1 - Authenticated Principal

#### What it establishes

The authenticated principal establishes the verified identity of the human or workload interacting with AGCP. Authentication answers the question: **Who is this caller?**

Authentication is intentionally limited in what it proves. It does not establish that the principal possesses a particular governance role, entitlement, reviewer authority, delegation, or permission to cause a governed consequence. It also does not establish that a proposal is admissible, authorized for commitment, or executable.

The authenticated identity provides the trustworthy starting point from which AGCP can resolve additional authoritative information about the principal.

#### Relationship to prior steps

This is the first trust-establishing step in the governance chain. Before this point, AGCP may have received a request, proposal, or claimed identifier, but it does not yet have a trusted basis for attributing that interaction to a specific principal.

Any principal identifier, username, reviewer name, role, entitlement, or similar value supplied inside a request remains claimant-supplied information until it is bound to the authenticated principal and qualified through the applicable identity process.

#### Relationship to the next step

The authenticated subject is passed into the identity-and-authorization qualification process governed by the **Identity and Authorization Store Profile**. The IAS Profile tells AGCP where authoritative information about that authenticated principal comes from and how that information must be resolved and qualified.

---

### Step 2 - Identity and Authorization Store Profile

#### What it establishes

The **Identity and Authorization Store Profile, or IAS Profile**, defines how a particular AGCP implementation resolves authoritative identity and identity-related authorization information.

It identifies the authoritative source or sources for information such as stable subject identity, account identity, account status, tenant and governance-domain membership, groups, roles, entitlements, governance permissions, reviewer classifications, delegated authority, applicable scope, validity periods, suspension or revocation state, and freshness requirements.

The IAS Profile is therefore not simply an authentication configuration. It defines the authoritative basis by which AGCP determines **what identity and authorization facts may be trusted about an authenticated principal**.

The authorization information held by the IAS remains distinct from **AGCP Execution Authorization**. For example, an IAS entitlement stating that a user may act as an incident reviewer is an authoritative fact about the user's organizational authority. It is not permission to execute a particular governed action.

#### Relationship to prior steps

The IAS Profile begins with the authenticated principal established in Step 1.

Instead of trusting role names, usernames, entitlements, or permissions supplied by the caller, AGCP resolves the authenticated subject according to the profile's declared authoritative sources, mappings, freshness rules, and failure behavior.

This prevents a caller from creating governance authority simply by asserting an identity or entitlement in a request.

#### Relationship to the next step

Applying the IAS Profile produces a machine-readable qualification result: **DS-053 Identity and Authorization Qualification Result**.

DS-053 carries the authoritative identity and authorization facts that downstream governance processing is permitted to consume.

---

### Step 3 - DS-053 Identity and Authorization Qualification Result

#### What it establishes

DS-053 records the result of authoritative identity and authorization qualification.

It establishes information such as stable subject identity, authoritative account identity, current account status, tenant and domain membership, roles, groups, entitlements, authorization attributes, reviewer classes, governance permissions, applicable scope, delegation or authority references, validity, freshness, and revocation state.

It also records the IAS Profile and authoritative source from which those facts were obtained, together with the evidence and integrity information necessary to understand how the qualification was performed.

DS-053 therefore answers: **What identity and authorization facts about this principal are sufficiently qualified for governance to rely upon?**

A successful qualification result still does not approve a proposal. It establishes trusted inputs for subsequent governance processing.

#### Relationship to prior steps

DS-053 is derived from the authenticated subject using the rules and authoritative sources declared by the IAS Profile.

It transforms authentication into a richer, governance-usable understanding of the principal without confusing authentication, organizational authorization, governance decision-making, or Execution Authorization.

#### Relationship to the next step

The qualified facts represented by DS-053 become inputs to the **Governance Decision Function**, where they may be combined with the proposal, governance policy, Canonical State, qualified evidence, constraints, invariants, approvals, delegation, lifecycle information, and other required governance inputs.

The GDF decides what those facts mean for the particular proposal under consideration.

---

### Step 4 - Governance Decision Function / Policy Decision Point

#### What it establishes

The **Governance Decision Function, or GDF**, realizes the **Policy Decision Point, or PDP, functional role** in AGCP.

Its responsibility is to evaluate a proposed governed transition against applicable governance requirements using qualified inputs. Those inputs can include DS-053 identity and authorization information, Canonical State, qualified evidence, policy artifacts, constraints, invariants, delegation, human governance artifacts, lifecycle information, and other required context.

The GDF answers: **Under the applicable governance rules and qualified information available at this evaluation point, what is the governance disposition of this proposal?**

The GDF makes a governance decision. It does not perform target execution, and a favorable decision does not itself establish current commit eligibility.

#### Relationship to prior steps

The GDF consumes qualified information rather than raw claims.

For identity-sensitive decisions, this means it relies on DS-053 rather than trusting a caller to claim that a person has a particular role or entitlement. For state-sensitive decisions, it similarly relies on qualified authoritative state and evidence.

The GDF therefore represents the first point at which the various qualified inputs are interpreted together under governance policy.

#### Relationship to the next step

The GDF produces **DS-015 Governance Decision Result**.

DS-015 makes the GDF/PDP decision explicit, attributable, integrity-protected, and available to subsequent authorization processing.

---

### Step 5 - DS-015 Governance Decision Result

#### What it establishes

DS-015 records the authoritative result of GDF/PDP evaluation.

It identifies the proposal that was evaluated, the governance outcome, the applicable policy and governance material, relevant qualified inputs, state and evidence basis, authority information, constraints and invariants, human governance inputs where applicable, and the evaluation basis used to reach the decision.

DS-015 therefore answers: **What did governance decide about this proposal, and on what qualified basis?**

A favorable DS-015 result means that the proposal satisfied the applicable governance-decision requirements at that evaluation point. It does **not** mean that the action may now be sent directly to the target.

#### Relationship to prior steps

DS-015 is the durable machine-readable representation of the GDF/PDP processing performed in Step 4.

Where identity or entitlement information influenced the decision, DS-015 can bind or reference the applicable DS-053 qualification result so that the decision can later be reconstructed from the same qualified inputs.

#### Relationship to the next step

A favorable Governance Decision can support creation of **DS-017 Execution Authorization**.

The next step changes the question from whether the proposal is governable to whether the governed proposal may progress toward final commitment processing.

---

### Step 6 - DS-017 Execution Authorization

#### What it establishes

DS-017 records that a successfully governed proposal is authorized to proceed toward the Commit Boundary, subject to the current-authority, current-state, binding, lifecycle, and Commit-Bound Admissibility checks that must still occur.

It binds the authorization to the specific proposal and relevant governance basis rather than creating a portable permission that can be applied to some other action, target, tenant, domain, or later set of conditions.

Execution Authorization answers: **Has this exact governed proposal satisfied the requirements necessary to proceed toward final commitment processing?**

It deliberately does **not** answer: **May this action execute right now?**

Conditions can change after authorization. An account can be disabled, an entitlement can be revoked, state can change, an approval can expire, or the intended target can change.

#### Relationship to prior steps

DS-017 depends upon favorable governance processing represented by DS-015 and any other required lifecycle, approval, or authority processing.

It preserves the relationship between the authorization and the exact proposal, governance decision, target, tenant/domain, scope, validity period, and other authorization-significant conditions.

#### Relationship to the next step

When a caller wants the authorized action to proceed toward operational realization, it submits a **DS-018 Commit Boundary Request**.

DS-017 is therefore an important input to the Commit Request, but it does not allow the caller to bypass the GRF or PEP.

---

### Step 7 - DS-018 Commit Boundary Request

#### What it establishes

DS-018 is the request to perform final commit-bound governance processing for an already governed and authorized proposal.

It identifies the proposal, action, target, relevant Governance Decision, Execution Authorization, caller, request integrity, and the information necessary for AGCP to locate and independently evaluate the applicable current governance context.

The Commit Request effectively asks: **Please determine whether this previously governed and authorized transition may now be committed.**

It does not allow the requester to declare that the authorization is still current, construct its own authoritative Enforcement Context, choose arbitrary enforcement semantics, or declare itself commit-eligible.

#### Relationship to prior steps

DS-018 refers back to the exact proposal, DS-015 Governance Decision, and DS-017 Execution Authorization that brought the proposal to this point.

The request is therefore not a new proposal and is not a second independent authorization request. It asks AGCP to realize the already-governed proposal under current conditions.

#### Relationship to the next step

Receipt of a valid DS-018 request invokes the **Governance Realization Function**.

The GRF independently re-establishes all commitment-sensitive conditions rather than simply trusting the state of affairs represented by the earlier authorization.

---

### Step 8 - Governance Realization Function

#### What it establishes

The **Governance Realization Function, or GRF**, is responsible for converting prior governance authorization into a determination of **current commit eligibility**.

It answers: **Given the authorization already issued and everything that is true now, may this exact transition be bound to the enforcement path and committed?**

The GRF coordinates the commitment-sensitive checks that occur immediately before enforcement. These include current Authority Re-Derivation, current Canonical State and evidence, lifecycle status, validity, binding validation, prior-use or replay conditions, target and action identity, tenant/domain binding, current governance configuration, and the applicable PEP Profile.

Where a material change requires policy to be evaluated again, the GRF may cause governed re-evaluation through the GDF/PDP rather than attempting to reinterpret policy itself.

#### Relationship to prior steps

The GRF starts from the DS-018 Commit Boundary Request and the prior governance chain represented by DS-015 and DS-017.

It does not discard those earlier results. Instead, it determines whether the assumptions, bindings, and authorities upon which they depend remain sufficient for commitment now.

This is what prevents an old favorable decision or authorization from becoming permanent execution authority.

#### Relationship to the next step

The GRF uses several important commitment-time inputs and sub-results. Chief among them is **DS-034 Authority Re-Derivation Result**, together with current Canonical State, current qualified evidence, lifecycle and validity information, binding validation, and the selected PEP Profile.

Those elements collectively allow the GRF to construct the authoritative **DS-029 Enforcement Context**.

---

### Step 9 - DS-034 Authority Re-Derivation Result

#### What it establishes

DS-034 records the current determination of authority applicable to the exact proposal and proposed transition at commitment time.

It can include current subject and account status, IAS-qualified roles and entitlements, delegation, authority lineage, human approval authority, applicable scope, tenant/domain, validity, revocation status, and other facts material to current authority.

It answers: **Does the necessary authority still exist, right now, for this exact proposal, target, action, and scope?**

This is intentionally stronger than merely checking whether an earlier authorization artifact still exists.

#### Relationship to prior steps

Earlier stages may have established authority sufficiently for GDF evaluation and Execution Authorization.

DS-034 revisits authority at the later commitment horizon. For example, a reviewer may have been authorized when an approval was accepted, but the associated account or entitlement may have been revoked before commitment. DS-034 provides the machine-readable basis for recognizing that change.

#### Relationship to the next step

The GRF combines DS-034 with current state, current evidence, lifecycle, binding information, and the PEP Profile.

If required authority can no longer be established, the chain does not proceed to enforcement.

---

### Step 10 - Current Canonical State and Qualified Evidence

#### What it establishes

Current Canonical State and qualified evidence establish the authoritative runtime facts that are material to commitment.

Canonical State answers questions about what the governed environment currently contains or represents. Qualified evidence establishes which observations or supporting facts are trustworthy enough to participate in governance.

The important property at this stage is **currency**. The GRF cannot simply assume that state and evidence used during the original Governance Decision remain valid indefinitely.

#### Relationship to prior steps

State and evidence may already have participated in the original Governance Decision and Execution Authorization.

At commitment, the GRF determines whether the commitment-sensitive portions remain valid and sufficiently current. Material changes can invalidate the prior basis or require governed re-evaluation.

#### Relationship to the next step

Together with DS-034 and the existing authorization, current state and evidence establish the factual basis for Commit-Bound Admissibility.

The GRF must then determine how the resulting commit-eligible transition maps onto an actual enforcement mechanism. That mapping is controlled by the **PEP Profile**.

---

### Step 11 - PEP Profile

#### What it establishes

The **PEP Profile** defines how an AGCP governed transition is realized through a particular enforcement mechanism.

It specifies the supported governed action and target types, exact operation mappings, required fields, permitted deterministic transformations, target identifier mappings, GRF-to-PEP authentication, required Enforcement Context bindings, idempotency and replay rules, PEP response mappings, evidence requirements, failure behavior, and PEP-to-target authority.

It answers: **How can this exact AGCP-governed transition be represented faithfully to this particular enforcement technology?**

The profile may transform representation, but it may not change governance meaning. If the PEP cannot faithfully represent the authorized transition, the correct result is non-execution rather than approximation.

#### Relationship to prior steps

The GRF reaches the PEP Profile only after it has the prior Governance Decision, Execution Authorization, current Authority Re-Derivation, current state and evidence, and other commitment-sensitive information.

The PEP Profile therefore does not decide whether the proposal is permitted. It tells the GRF how an already-governed and currently eligible transition can be represented to the selected PEP.

#### Relationship to the next step

The GRF applies the PEP Profile when assembling **DS-029 Enforcement Context**.

The profile identity, version or digest, selected operation mapping, and other enforcement-significant information become part of the binding presented to the PEP.

---

### Step 12 - DS-029 Enforcement Context

#### What it establishes

DS-029 is the authoritative enforcement-facing context assembled by the GRF.

It brings together the information the PEP needs to determine whether the exact operation presented at the enforcement boundary is the same operation that was governed, authorized, and found commit-eligible.

This can include bindings to the proposal, Governance Decision, Execution Authorization, Authority Re-Derivation result, current state and evidence, action, target, tenant/domain, lifecycle, validity, selected PEP Profile and operation mapping, GRF identity, and Governance Enforcement Binding.

DS-029 answers: **What exact transition has AGCP established as eligible for enforcement, under what current governance basis, and through what declared enforcement mapping?**

#### Relationship to prior steps

DS-029 is not supplied authoritatively by the external requester.

It is constructed by the GRF from the earlier governance artifacts plus current commitment-time facts. That distinction protects the enforcement boundary from a caller manufacturing its own "approved" execution context.

#### Relationship to the next step

DS-029 is presented to the **Policy Enforcement Point** through the protected GRF-to-PEP path.

The PEP uses the context and selected profile to determine whether to permit the exact transition across the enforcement boundary.

---

### Step 13 - Policy Enforcement Point

#### What it establishes

The **Policy Enforcement Point, or PEP**, is the component or function that controls the path by which the governed consequence can occur.

The PEP verifies the enforcement-facing bindings required by the applicable PEP Profile and Enforcement Context. It can prevent operations that are stale, mismatched, replayed, unsupported, improperly bound, or otherwise inadmissible.

The PEP answers: **Will this exact commit-eligible transition be allowed across the protected enforcement boundary?**

It does not make a new general policy decision and does not reinterpret a favorable GDF result into a broader action.

#### Relationship to prior steps

The PEP receives an enforcement operation from the GRF together with DS-029.

That request represents the culmination of the earlier identity qualification, governance decision, authorization, current Authority Re-Derivation, Commit-Bound Admissibility, and PEP Profile mapping.

The PEP is therefore the enforcement terminus of the governance control chain rather than another decision engine parallel to the GDF.

#### Relationship to the next step

The outcome of GRF and PEP processing is recorded in **DS-019 Commit Boundary Result**.

If the PEP refuses the transition, the governed consequence does not cross the protected boundary.

---

### Step 14 - DS-019 Commit Boundary Result

#### What it establishes

DS-019 records the authoritative outcome of final commit processing.

A successful result establishes that the exact governed transition satisfied current commitment requirements and was accepted through the protected enforcement path for application to the intended target.

A failed result records that commitment did not occur for that attempt.

The important semantic distinction is that **Commit Successful does not universally mean operational execution has already completed**. Commitment and execution may be atomic in one implementation and separate in another.

#### Relationship to prior steps

DS-019 represents the result of the GRF's current eligibility determination and the PEP's enforcement-boundary processing.

It therefore depends on the integrity of the entire earlier chain, including DS-017, DS-034, DS-029, and the applicable PEP Profile.

#### Relationship to the next step

If commitment and target execution are atomic, the operational outcome may be known immediately.

If the target executes asynchronously or otherwise separates acceptance from completion, AGCP uses **DS-052 Governed Execution Outcome** to represent what happens after commitment.

---

### Step 15 - DS-052 Governed Execution Outcome

#### What it establishes

DS-052 represents the actual operational result of a governed transition after commitment when execution is distinct from the commitment event.

It can represent states such as pending, in progress, succeeded, partially succeeded, failed, cancelled, or indeterminate.

It binds the operational outcome back to the applicable proposal, DS-019 Commit Result, DS-029 Enforcement Context, PEP Profile, PEP, target, resulting state, and supporting evidence.

DS-052 answers: **After the governed transition was accepted for application, what actually happened operationally?**

#### Relationship to prior steps

DS-052 only makes sense in relation to a valid commitment event.

It cannot retroactively manufacture a Governance Decision or Execution Authorization, nor does a target claiming success establish that the required governance chain occurred. Its provenance must connect the operational result back to DS-019 and the governed enforcement path.

#### Relationship to the next step

The operational result affects the authoritative lifecycle state and becomes evidence that must be durably recorded.

That leads to the final set of persistent governance representations: DS-038, DS-020, DS-027, and DS-040.

---

### Step 16 - DS-038 Governance Lifecycle Record

#### What it establishes

DS-038 establishes the authoritative lifecycle status of the governed proposal.

It represents where the proposal currently stands as a consequence of the governance events that have occurred.

The model allows commitment and execution to remain distinct. A proposal can therefore progress through states such as:

```text
AUTHORIZED -> COMMITTED -> EXECUTED
```

rather than requiring successful commitment to mean immediate execution. Where execution later fails, the lifecycle can represent that result without denying that commitment previously occurred.

#### Relationship to prior steps

DS-038 reflects the accumulated consequences of proposal processing, decision, authorization, review, GRF processing, commitment, enforcement, and execution outcome.

It is not an independent source of authority that allows software to arbitrarily set the proposal's state.

#### Relationship to the next step

The lifecycle state must be supported by reconstructable evidence and authoritative event history.

DS-020, DS-027, and DS-040 provide complementary views of that same governance history.

---

### Step 17 - DS-020 Governance Evidence

#### What it establishes

DS-020 preserves the evidence necessary to reconstruct and substantiate the governance process.

It can link the original proposal, identity qualification, Governance Decision, Execution Authorization, Authority Re-Derivation, current state and evidence qualifications, GRF processing, PEP Profile, Enforcement Context, PEP processing, Commit Result, execution outcome, and lifecycle consequences.

It answers: **Can an assessor reconstruct what governance did, what information it relied upon, why the result occurred, and what happened afterward?**

#### Relationship to prior steps

Every significant stage of the chain may contribute evidence.

DS-020 brings those pieces together without collapsing the distinctions among identity, decision, authorization, commitment, enforcement, and execution.

#### Relationship to the next step

Particular governance results may also be represented as attributable Governance Receipts, while the ordered history of governance-significant events is preserved in the Governance Ledger.

---

### Step 18 - DS-027 Governance Receipt

#### What it establishes

DS-027 provides an attributable, integrity-protected receipt for a particular successful or otherwise non-refusal governance result.

A receipt may attest to an approval, decision, authorization, commitment, enforcement result, execution result, or another supported governance outcome.

The receipt provides a compact proof that a particular governed result occurred under a particular governance basis.

A receipt is **evidence of a result**, not a new source of authority.

#### Relationship to prior steps

A receipt is derived from an actual governance result already established by the corresponding stage.

For example, a commitment receipt refers back to the actual DS-019 result rather than independently asserting that commitment occurred.

#### Relationship to the next step

The receipt can itself be referenced by Governance Evidence and Governance Ledger records.

The ultimate authoritative ordering of governance history belongs to the Governance Ledger.

---

### Step 19 - DS-040 Governance Ledger Event

#### What it establishes

DS-040 records an individual event in the append-only, integrity-protected governance history.

Ledger events can represent or reference proposal submission, qualification, identity and authorization qualification, GDF decisions, human governance activity, Execution Authorization, Authority Re-Derivation, Governance Realization, PEP enforcement, commitment, execution outcomes, receipts, and lifecycle transitions.

The ledger answers: **What governance-significant events occurred, in what authoritative order, and with what integrity relationships?**

This makes the governance process reconstructable rather than dependent on mutable application state or ordinary operational logs.

#### Relationship to prior steps

Each significant artifact or transition in the preceding chain may generate one or more ledger events.

DS-040 therefore does not replace DS-015, DS-017, DS-019, DS-052, or the other substantive artifacts. It records their occurrence and relationships in an ordered governance history.

#### Relationship to the next step

DS-040 is the durable end of this machine-readable chain.

Its history supports reconstruction of DS-038 lifecycle state, retrieval and verification of DS-020 evidence, validation of DS-027 receipts, deterministic replay, audit, incident investigation, and conformance assessment.

---

## 4. Key Architectural Distinctions

### 4.1 Authentication is not authorization

Authentication establishes who a principal is. IAS qualification establishes which identity and authorization facts about that principal are authoritative. Neither one independently decides whether a proposal is permitted.

### 4.2 IAS authorization is not AGCP Execution Authorization

An IAS role, group, entitlement, or governance permission is an authoritative fact about a subject. AGCP Execution Authorization is a proposal-bound governance artifact that permits a successfully governed proposal to continue toward commitment processing.

These are different concepts and must not be represented by the same artifact or treated as interchangeable.

### 4.3 Governance Decision is not Execution Authorization

DS-015 states the result of GDF/PDP governance evaluation. DS-017 states that the governed proposal may proceed toward final commitment processing. Neither artifact independently permits immediate target execution.

### 4.4 Execution Authorization is not current commit eligibility

DS-017 represents prior authorization. The GRF must independently re-establish current commitment-sensitive conditions. This prevents stale authorization from becoming permanent execution authority.

### 4.5 GDF/PDP is not GRF

The GDF/PDP evaluates governance policy and produces a Governance Decision. The GRF determines whether a previously governed and authorized transition may bind under current conditions and be presented to enforcement.

These functions may be co-located in one implementation, but their logical responsibilities remain distinct.

### 4.6 GRF is not PEP

The GRF establishes current commit eligibility and constructs the enforcement-facing context. The PEP controls the enforcement boundary and prevents ineligible or mismatched operations from crossing it.

### 4.7 Commitment is not always execution completion

DS-019 establishes the commitment event. DS-052 establishes the later operational outcome where target realization is distinct or asynchronous.

This distinction allows AGCP to model both atomic and asynchronous target systems without changing governance semantics.

### 4.8 Evidence, receipts, lifecycle, and ledger do not create authority

DS-020, DS-027, DS-038, and DS-040 record, reconstruct, summarize, or order governance history. They do not replace the GDF, Execution Authorization, GRF, or PEP.

---

## 5. Artifact Relationship Summary

| Function or Stage | Primary Machine-Readable Artifact | Primary Meaning |
|---|---|---|
| Identity and authorization qualification | DS-053 | Qualified authoritative subject/account/role/entitlement/authorization facts |
| Governance decision | DS-015 | GDF/PDP decision and decision basis |
| Pre-commit authorization | DS-017 | Proposal may proceed toward commitment processing |
| Commit invocation | DS-018 | Request to perform current GRF/commit processing |
| Current authority | DS-034 | Commitment-time authority re-derived from current qualified facts |
| Enforcement realization | DS-029 | Exact enforcement-facing context constructed by the GRF |
| Commitment result | DS-019 | Exact transition accepted or refused at the protected commitment/enforcement path |
| Operational execution result | DS-052 | What happened after commitment when target realization is distinct |
| Lifecycle | DS-038 | Current authoritative lifecycle state derived from governance history |
| Evidence | DS-020 | Reconstructable evidence supporting governance results |
| Receipt | DS-027 | Attributable integrity-protected receipt for a specific governance result |
| Ledger | DS-040 | Ordered append-only governance-event history |

---

## 6. Atomic and Asynchronous Execution

AGCP permits implementations in which commitment and execution completion occur together, as well as implementations in which commitment accepts work that completes later.

### 6.1 Atomic realization

```text
DS-019 Commit Successful
        |
        v
Target transition completes as part of the same protected operation
        |
        v
DS-052 may record the completed result immediately
        |
        v
DS-038 reflects EXECUTED
```

### 6.2 Asynchronous realization

```text
DS-019 Commit Successful
        |
        v
DS-038 reflects COMMITTED
        |
        v
DS-052 = PENDING / IN_PROGRESS
        |
        +------> DS-052 = SUCCEEDED ------> DS-038 = EXECUTED
        |
        +------> DS-052 = FAILED ---------> DS-038 = execution-failure state
```

A successful commitment therefore means that the exact governed transition was accepted through the controlled enforcement path. It does not universally assert that all downstream operational work has completed.

---

## 7. Trust-Boundary Interpretation

The machine-readable chain crosses several distinct trust boundaries.

### 7.1 Principal to IAS qualification

The authenticated principal is trusted as the authenticated subject. Claimed roles, entitlements, reviewer status, or authority are not yet authoritative.

### 7.2 IAS source to AGCP governance

DS-053 establishes which identity and authorization facts are qualified according to the selected IAS Profile. Governance consumes those facts but still decides their relevance under policy.

### 7.3 Qualified inputs to GDF/PDP

The GDF/PDP receives qualified governance inputs and produces DS-015. The GDF/PDP is trusted to decide governance disposition but not to cause the target consequence directly.

### 7.4 Authorization to GRF

DS-017 authorizes progression toward commitment. The GRF independently verifies current commitment-sensitive conditions before enforcement.

### 7.5 GRF to PEP

The GRF applies the PEP Profile and produces DS-029. The PEP trusts the protected GRF path and the bound Enforcement Context rather than a caller's unverified execution request.

### 7.6 PEP to target

The target trusts the PEP as the enforcement principal for the declared governed scope. PEP-to-target credentials answer whether the caller is an authorized enforcement workload; the governance chain answers whether the exact consequence is authorized now.

### 7.7 Target outcome to evidence and ledger

Execution evidence must be sufficiently trustworthy to establish what happened operationally. DS-052, DS-020, and DS-040 preserve that result without allowing the target to retroactively create governance authority.

---

## 8. Replay, Audit, and Reconstruction

The final four persistent artifact families serve different purposes and should not be treated as duplicates.

**DS-038 Governance Lifecycle Record** answers: *Where is this proposal now in the governance lifecycle?*

**DS-020 Governance Evidence** answers: *What evidence supports the decisions, authorizations, commitment, enforcement, and execution results?*

**DS-027 Governance Receipt** answers: *What attributable, integrity-protected governance result was issued for this specific event or outcome?*

**DS-040 Governance Ledger Event** answers: *What governance-significant events occurred, and in what authoritative order?*

Together, they support deterministic reconstruction of the governance path without replaying the governed target action itself.

---

## 9. Student and Implementer Interpretation

For students and implementers, the most important operational lesson is that **no single intermediate artifact means "execute now."**

A proposal is a request. DS-053 establishes qualified identity and authorization facts. DS-015 records a governance decision. DS-017 allows the governed proposal to proceed toward commitment. DS-018 requests final commitment processing. The GRF then re-establishes current authority and current governance reality, applies the PEP Profile, and constructs DS-029. The PEP controls the enforcement boundary. DS-019 records whether commitment occurred. DS-052 records what happened operationally where execution is distinct.

This separation is what prevents proposal generation, authentication, prior approval, or earlier authorization from becoming unrestricted execution authority.

---

## 10. Related AGCP Artifacts

This document should be read together with the current AGCP repository artifacts, including:

- AGCP Core Specification;
- AGCP Normative Statements;
- Architecture Reference Model;
- AGCP Trust Model;
- AGCP Human Review Specification;
- AGCP Policy Evaluation Contract;
- AGCP HTTP Interface Specification;
- AGCP Implementation Profile Specification;
- AGCP Identity and Authorization Store Profile Specification;
- AGCP PEP Profile Specification;
- AGCP Governance Lifecycle Model;
- AGCP Normative Governance Progression Table;
- AGCP Governance Progression Implementation Guide;
- machine-readable Data Schemas DS-001 through DS-053, as applicable;
- AGCP HTTP and Management OpenAPI contracts;
- AGCP conformance and traceability artifacts.

Where any explanatory text in this document differs from a controlling normative artifact, the controlling normative artifact governs.
