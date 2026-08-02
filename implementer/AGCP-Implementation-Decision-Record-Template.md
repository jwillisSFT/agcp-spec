# AGCP Implementation Profile Template

Status: Informational (Non-Normative)

Template Version: 1.2.0

## 1. Purpose

This template is used to create a controlled AGCP Implementation Profile for a specific implementation class, deployment model, or product realization.

A completed document produced from this template is the Implementation Profile itself. It is not merely a questionnaire or an Implementation Decision Record.

The template supports two completion modes:

- **Controlled implementation profile** - a profile bound to a real implementation and its controlled build, deployment, and assurance artifacts.
- **Informational example profile** - a complete worked example that uses real AGCP-connected values and clearly labeled illustrative implementation and deployment values. It is non-normative, non-operational, and makes no implementation or conformance claim.

An Implementation Profile may define:

- supported capabilities;
- optional behavior expressly permitted by AGCP;
- deployment constraints;
- interface mappings;
- implementation-specific technology selections; and
- implementation guidance.

An Implementation Profile shall not redefine, weaken, disable, replace, bypass, or contradict mandatory behavior established by higher-precedence AGCP sources.

## 2. Completion Rules

### 2.1 Required completion state

Before approval and publication:

- every required field shall contain a definitive value;
- every non-applicable field shall state `Not Applicable` and include a rationale;
- unresolved items shall be recorded as controlled dependencies and shall not be silently resolved in implementation code;
- all referenced artifacts shall identify a version, repository path or URI, lifecycle state, and integrity digest where applicable;
- all significant architectural or security decisions shall reference an approved ADR or IDR;
- mutable environment-specific values shall be routed to a deployment overlay or operations runbook; and
- the profile shall identify the objective evidence required to support any conformance claim.

A profile containing unresolved `TBD`, `TBC`, or equivalent placeholders shall not be assigned an approved or production-ready lifecycle state.

An informational example may use concrete illustrative values instead of unresolved placeholders, but every such value shall be explicitly identified as illustrative and shall not be represented as an actual endpoint, account, implementation, deployment, approval, or conformance result.

### 2.2 Decision classification

Every profile entry shall be assigned one of the following classifications.

| Classification | Meaning | Required disposition |
|---|---|---|
| `FIXED_NORMATIVE_OBLIGATION` | Behavior is already required or prohibited by a higher-precedence AGCP artifact. | Record the controlling source, implementation mapping, and verification evidence. Do not present the behavior as optional. |
| `PROFILE_SELECTION` | Stable implementation choice or permitted alternative selected for this profile. | Record the selected value, rationale, compatibility effect, and verification method in this profile. |
| `DEPLOYMENT_CONFIGURATION` | Mutable environment-specific value. | Record the controlling rule in this profile and route the concrete value to a deployment overlay or runbook. |
| `ADR_IDR_REQUIRED` | Significant architectural, security, trust-boundary, or lifecycle decision. | Reference a separate approved ADR or IDR containing context, alternatives, decision, consequences, and affected artifacts. |
| `REPOSITORY_CORRECTION` | Defect, contradiction, stale reference, or inconsistency in controlled AGCP artifacts. | Resolve through the AGCP specification change process. Do not create a private implementation interpretation. |

### 2.3 Value authority and provenance classification

Decision classification and value authority are separate. A decision may be a `PROFILE_SELECTION` while its example value is still `ILLUSTRATIVE_EXAMPLE`.

Every concrete value shall be attributable to one of the following value-authority classes.

| Value-authority class | Meaning | Required treatment |
|---|---|---|
| `AGCP_CONTROLLED` | The value is established by an applicable controlled AGCP artifact, such as an AGCP version, identifier, capability, normative path, schema, interface, registry, CR, NS, ARM, or TC reference. | Preserve the exact controlled value and cite its authoritative AGCP source. Do not label it illustrative. |
| `PROFILE_DEFINED` | The value is an approved stable implementation-profile selection for a real implementation. | Record the approving authority, rationale, verification method, and versioning consequences. |
| `ILLUSTRATIVE_EXAMPLE` | The value is concrete but not real and is supplied only to demonstrate how a profile could be completed. | Label it illustrative wherever a reader could mistake it for an actual implementation or deployment value. Use reserved example domains and documentation-only network ranges. |
| `EXTERNAL_DEPLOYMENT_VALUE` | The value is mutable and controlled in the implementation build/deploy repository, such as a hostname, IP address, resource limit, rate limit, timeout, replica count, region, account, secret reference, SLO, RTO, or RPO. | Reference the build/deploy artifact and do not embed the current operational value in the profile unless interoperability or conformance requires a profile-versioned constant. |
| `COMPUTED_ARTIFACT_VALUE` | The value is calculated from a final artifact, such as a SHA-256 digest. | Calculate it only after the artifact is final; identify the calculation and verification process. |
| `CONTROLLED_DEPENDENCY` | The value cannot be finalized until a separate controlled correction, decision, or artifact exists. | Identify the dependency, owner, blocking scope, and acceptance evidence. Do not invent a value. |

For an informational example profile:

- AGCP-connected values shall be real, source-derived, and marked `AGCP_CONTROLLED` where classification is shown;
- implementation names such as `agcp-rs`, cloud providers and services, identity providers, hostnames, IP addresses, resource limits, quotas, timeouts, capacities, retention periods, and operational targets shall be marked `ILLUSTRATIVE_EXAMPLE` unless they are genuinely adopted values of a real implementation;
- no illustrative hostname or address shall be presented as reachable or operational; and
- no illustrative approval, evidence, digest, deployment, or conformance status shall be represented as real.

### 2.4 Precedence and interpretation

The profile shall apply the AGCP specification precedence established by the applicable controlled baseline.

Where a profile entry conflicts with a higher-precedence AGCP source, the higher-precedence source governs and the conflict shall be recorded as a profile defect or repository correction.

### 2.5 Repository and artifact routing rule

The completed profile shall contain stable profile selections and mappings. It shall reference, but not duplicate, separately controlled artifacts.

The AGCP specification/profile repository may contain:

- the human-readable implementation profile;
- the machine-readable profile record;
- an informational-example notice where applicable;
- the final profile digest;
- profile-specific interface specifications that are part of the AGCP-controlled profile definition;
- profile-specific traceability and conformance-extension artifacts; and
- references to associated ADRs, IDRs, and release evidence.

The implementation build/deploy repository shall contain operational implementation artifacts, including:

- development, test, staging, and production deployment overlays;
- infrastructure definitions and manifests;
- tenant-class and environment configuration;
- operations, security, incident-response, backup, restoration, and disaster-recovery runbooks;
- release manifests, SBOMs, binary provenance, and build attestations; and
- release-specific deployment and conformance evidence.

The profile shall reference those external artifacts using stable repository paths, versions, revisions, and digests where applicable. `deploy/` and `runbooks/` directories shall not be placed inside the AGCP profile package.

### 2.6 How to use the completion guidance

Appendix C provides field-level explanations, classification examples, model answers, and common failure patterns. The examples are illustrative and non-normative. They demonstrate the expected degree of specificity but do not prescribe a universal implementation choice.

When creating a profile from this template:

1. copy the template to a new file named for the intended profile;
2. retain the section structure and replace every blank field with a definitive value, `Not Applicable`, or an explicitly controlled dependency;
3. use Appendix C to determine the appropriate level of detail and artifact routing;
4. replace illustrative identifiers, paths, digests, values, and technologies with approved implementation-specific values;
5. delete all bracketed instructional placeholders;
6. remove Appendix C from the completed profile unless the publication policy expressly retains authoring guidance; and
7. calculate the final profile digest only after content approval and final formatting.

#### 2.6.1 Field completion convention

Use the following pattern for narrative profile entries whenever the section does not already provide a table:

- **Classification:** one of the classifications in Section 2.2.
- **Decision or Rule:** the definitive profile requirement or selection.
- **Controlling Source:** the applicable AGCP artifact and section, interface, schema, registry, ADR, or deployment overlay.
- **Rationale:** why the profile selected or mapped the behavior.
- **Verification Method:** how an assessor or test can determine that the implementation follows the profile.
- **Evidence Location:** the controlled artifact, test output, configuration record, ledger evidence, or release evidence containing the result.

#### 2.6.2 Required writing style

Profile language shall be concrete, testable, and implementation-specific. Avoid vague responses such as `supported`, `standard security`, `as needed`, `industry best practice`, or `configured in production` without identifying the controlling rule and evidence.

Prefer statements such as:

> The service SHALL reject a request when the tenant identifier in the authenticated credential does not exactly match every tenant identifier present in the route, request body, and referenced resource. Public responses SHALL use HTTP 404 with `RESOURCE_NOT_FOUND`; the tenant-specific mismatch reason SHALL be retained only in protected Governance Evidence.

Do not use statements such as:

> Tenant isolation is supported.

## 3. Profile Control Record

**Completion guidance:** See Appendix C.4 for a completed control-record example.

| Field | Profile value |
|---|---|
| Artifact Mode | Controlled Implementation Profile / Informational Example Profile |
| Operational Deployment | Yes / No |
| Profile ID | |
| Profile Name | |
| Profile Version | |
| Repository Path or URI | |
| Profile SHA-256 Digest | |
| Publication Status | |
| Artifact Lifecycle State | |
| Profile Owner | |
| Technical Owner | |
| Approval Authority | |
| Approval Date | |
| Effective Date | |
| Review Date | |
| Supersedes | |
| Superseded By | |

## 4. Implementation Identification

| Field | Profile value |
|---|---|
| Implementation Name | |
| Implementing Organization | |
| Implementation Release or Build | |
| Implementation Source Repository | |
| Build and Deploy Repository | |
| Runbook Location | |
| Implementation Class | Reference Implementation / Production Implementation / Both / Other |
| Primary Implementation Language(s) | |
| Principal Runtime(s) | |
| Target Platform Class | |
| Deployment Environment Class | |
| Primary Architects | |
| Security Authority | |
| Operations Authority | |

## 5. Controlled Baseline

**Completion guidance:** See Appendix C.5 for baseline identification, artifact pinning, and digest examples.

### 5.1 Base AGCP release

| Field | Profile value |
|---|---|
| AGCP Specification Version | |
| Publication Maturity | |
| Controlled Baseline Date | |
| Baseline Bundle Name | |
| Baseline Bundle Repository Path or URI | |
| Baseline Bundle SHA-256 Digest | |
| Supported Baseline Count | One / Multiple |
| Baseline Migration Rule | |

### 5.2 Adopted controlled artifacts

| Artifact class | Identifier and version | Repository path or URI | SHA-256 digest | Lifecycle state | Applicability |
|---|---|---|---|---|---|
| AGCP Core Specification | | | | | |
| Architecture Reference Model | | | | | |
| Normative Statements | | | | | |
| Conformance Requirements | | | | | |
| Requirements Traceability Matrix | | | | | |
| Schema Catalog | | | | | |
| Registry Catalog | | | | | |
| Interface Specifications | | | | | |
| OpenAPI Contract | | | | | |
| Conformance Test Suite | | | | | |
| Assessment Procedures | | | | | |
| Other Companion Specifications | | | | | |

### 5.3 Artifact source and pinning

- Classification:
- Authoritative artifact source:
- Extracted machine-readable artifact policy:
- Embedded-document artifact policy:
- Hash-pinning rule:
- Semantic-version role:
- Multi-version support rule:
- Change-detection mechanism:
- Migration approval requirement:
- Verification method:
- Rationale:

## 6. Conformance Posture

**Completion guidance:** See Appendix C.6. Separate the target conformance scope from the current verified claim.

### 6.1 Conformance target

| Field | Profile value |
|---|---|
| Target AGCP Conformance Level or Scope | |
| Current Conformance Claim Status | Not Claimed / Partially Verified / Verified / Other |
| Applicable Mandatory Requirements | |
| Supported Optional Capabilities | |
| Unsupported Optional Capabilities | |
| Applicable Companion Specifications | |
| Applicable Profile-Specific Conformance Extension | |
| Conformance Claim Record | |

### 6.2 Conformance statement

Provide the exact statement that may be used in implementation metadata and release documentation.

Profile Statement:

> [Insert the approved conformance posture statement.]

### 6.3 Objective evidence

| Evidence class | Required | Evidence location | Acceptance criterion |
|---|---|---|---|
| Official AGCP conformance test results | | | |
| Governance Evidence | | | |
| Implementation documentation | | | |
| Assessment results | | | |
| Independent technical evidence | | | |
| Profile-specific test results | | | |
| Release manifest and attestations | | | |

## 7. Claimed Enforcement Scope

**Completion guidance:** See Appendix C.7. Describe the real technical mediation boundary, not the intended business scope.

### 7.1 Enforcement boundary

- Classification: `ADR_IDR_REQUIRED`
- Claimed enforcement scope:
- Governed consequence classes within scope:
- Owner-controlled services within scope:
- Governance runtime components within scope:
- Persistence components within scope:
- Policy Enforcement Point or executor within scope:
- Commit Boundary placement:
- External systems within scope:
- External systems explicitly outside scope:
- Execution paths explicitly excluded from the non-bypassability claim:
- Decision record:
- Verification method:
- Rationale:

### 7.2 Non-bypassability statement

> [State precisely which execution paths are mediated by the applicable governance decision and Policy Enforcement Point mechanisms, and which paths are not included in the claim.]

### 7.3 Explicit non-goals

| Non-goal | Rationale | Effect on conformance claim |
|---|---|---|
| | | |

## 8. Capability and Applicability Profile

**Completion guidance:** See Appendix C.8 for the meaning of applicability values and a completed mapping row.

For each capability, identify whether it is mandatory, supported, unsupported, or not applicable. Unsupported optional capabilities shall not weaken mandatory behavior.

| Capability or requirement group | Applicability | Controlling source | Implementation mapping | Verification evidence |
|---|---|---|---|---|
| Proposal Qualification | | | | |
| Governance Decision Function | | | | |
| Execution Authorization | | | | |
| Governance Realization and Commit Boundary | | | | |
| Governance Evidence | | | | |
| Canonical State Resolution and Qualification | | | | |
| Authority Re-Derivation | | | | |
| Governance Binding Validation | | | | |
| Tenant and Governance Domain Isolation | | | | |
| Delegation and Authority Lineage | | | | |
| Human Review and Approval Artifacts | | | | |
| Continuation Integrity | | | | |
| Risk-Based Re-Evaluation | | | | |
| Composite Proposal Governance | | | | |
| Cross-Domain Authority Isolation | | | | |
| Governance Self-Protection | | | | |
| Autonomous Coordination | | | | |
| Profile-specific optional capability | | | | |

## 9. Runtime Architecture and Service Boundaries

### 9.1 Deployment mode

- Classification:
- Single-tenant, multi-tenant, or both:
- Tenant isolation boundary:
- Governance-domain isolation boundary:
- Verification method:
- Rationale:

### 9.2 Service decomposition

- Classification: `ADR_IDR_REQUIRED`
- Single-process, multi-process, or distributed model:
- Public governance service:
- Governance decision component:
- Governance realization component:
- Policy Enforcement Point or executor:
- Ledger component:
- Canonical State adapters:
- Private management plane:
- Operations interface:
- Background workers:
- Decision record:
- Verification method:
- Rationale:

### 9.3 Development and production relationship

- Classification:
- Base profile shared across environments:
- Development overlay:
- Test overlay:
- Staging overlay:
- Production overlay:
- Environment-specific deviations permitted:
- Environment-specific deviations prohibited:
- Promotion rule:
- Verification method:
- Rationale:

### 9.4 Stack constraints

- Classification:
- Required libraries or providers:
- Prohibited libraries or providers:
- Foreign-function or native-code constraints:
- Operating-system constraints:
- Containerization constraints:
- Compliance constraints:
- Verification method:
- Rationale:

## 10. Interface Profile

**Completion guidance:** See Appendix C.9. Record mandatory adopted-interface behavior as fixed obligations, not optional selections.

### 10.1 Public AGCP interface adoption

- Classification: `FIXED_NORMATIVE_OBLIGATION` where required by the adopted interface
- Adopted interface identifier and version:
- Public endpoint origin or hostname: [profile-defined or external deployment value; illustrative in an example profile]
- AGCP public base path: `/agcp/v2`
- Implementation metadata operation and path: `GET /agcp/v2/meta`
- Required operations:
- Required request and response schemas:
- Required `Idempotency-Key` behavior:
- Required error model:
- Synchronous or asynchronous behavior permitted by the adopted interface:
- Verification method:
- Evidence location:

### 10.2 Internal RPC and transport

- Classification:
- Internal RPC protocol:
- Serialization format:
- Remote-call authentication:
- Remote-call encryption:
- mTLS requirement:
- Host-isolation reliance:
- Retry behavior:
- Timeout governance:
- Deployment-overlay references:
- Verification method:
- Rationale:

### 10.3 Private management plane

- Classification: `ADR_IDR_REQUIRED`
- Management-plane path, binding, or network boundary:
- Authorized operator classes:
- Tenant management functions:
- Principal management functions:
- Key-management functions:
- Configuration-management functions:
- Governance compilation functions:
- Activation and rollback functions:
- Suspension functions:
- Quota-management functions:
- Export functions:
- Separation from the public conformance interface:
- Canonical State mutation authority:
- Decision record:
- Verification method:
- Rationale:

### 10.4 Operations interface

- Classification:
- Operations path or binding:
- Query functions:
- List functions:
- Audit functions:
- Export functions:
- Tenant scoping:
- Authentication and authorization:
- Direct Canonical State mutation prohibited: Yes / No
- Verification method:
- Rationale:

## 11. Ingress Trust Boundary and Authoritative Records

**Completion guidance:** See Appendix C.10 for a command-versus-authoritative-record example.

### 11.1 Command-versus-record distinction

- Classification: `ADR_IDR_REQUIRED`
- Untrusted command or submission object types:
- Authoritative AGCP-created record types:
- AGCP-qualified external record types:
- Server-derived fields that claimants may not assert authoritatively:
- Qualification process:
- Conversion from submission to authoritative record:
- Rejection behavior:
- Decision record:
- Verification method:
- Rationale:

### 11.2 Governance Approval Artifacts

- Classification:
- Approval submission object:
- Authoritative Governance Approval Artifact:
- Approver attribution requirements:
- Cryptographic verification requirements:
- Eligibility verification:
- Scope and validity binding:
- Proposal Identity binding:
- Lifecycle-state binding:
- Partial quorum representation:
- Completed quorum representation:
- Replay-prevention rule:
- Storage and retrieval model:
- Verification method:
- Rationale:

## 12. Authentication, Authorization, and Tenant Binding

**Completion guidance:** See Appendix C.11 for an authentication and tenant-binding example.

### 12.1 Authentication profile

- Classification:
- Authentication mechanism:
- Identity provider model:
- Token or credential type:
- Asymmetric algorithm allowlist:
- Issuer allowlist rule:
- Required audience:
- Token lifetime rule:
- Credential revocation rule:
- Verification method:
- Rationale:

### 12.2 Identity and tenant claims

- Classification:
- Subject identifier source:
- Tenant identifier source:
- Tenant claim name:
- Subject claim name:
- Route, body, query, and credential tenant-binding rule:
- Tenant mismatch behavior:
- Missing-tenant behavior:
- Cross-tenant lookup behavior:
- Verification method:
- Rationale:

### 12.3 Authorization profile

- Classification:
- Scope or permission model:
- Role model, if used:
- Minimum roles:
- Endpoint restrictions:
- Management-plane restrictions:
- Operations-interface restrictions:
- Server-side authorization revalidation:
- Verification method:
- Rationale:

### 12.4 Disclosure policy

- Classification:
- Resource lookup disclosure mode:
- Conditions for HTTP 404:
- Conditions for HTTP 403:
- Cross-tenant disclosure behavior:
- Internal evidence or telemetry detail:
- Verification method:
- Rationale:

### 12.5 Cross-domain authority scope

- Classification:
- Cross-tenant authority transfer:
- Cross-domain authority transfer:
- Required trust artifacts:
- Initial restrictions:
- Future-profile extension rule:
- Verification method:
- Rationale:

## 13. Cryptography and Key Management

**Completion guidance:** See Appendix C.12. Every algorithm, encoding, key scope, nonce rule, and failure mapping must be explicit.

### 13.1 Provenance and signature profile

- Classification: `PROFILE_SELECTION` plus any applicable `REPOSITORY_CORRECTION`
- Applicable provenance specification:
- Signature algorithm:
- Canonicalization method:
- Character encoding:
- Base64url padding rule:
- Protected-header contract:
- Signature input construction:
- Signer representation:
- Key identifier representation:
- Signing-time rule:
- Clock-skew allowance:
- Nonce rule:
- Replay-retention rule:
- Scope binding:
- Verification-failure mapping:
- Verification method:
- Rationale:

### 13.2 Key identifiers and purposes

- Classification:
- `kid` format:
- `kid` uniqueness scope:
- JWK or equivalent representation:
- Key purposes:
- Tenant binding:
- Key registration authority:
- Key-use constraints:
- Verification method:
- Rationale:

### 13.3 Key storage, caching, rotation, and revocation

- Classification:
- Key management mode:
- Storage backend class:
- Tenant-upload support:
- Server-managed support:
- In-memory cache policy:
- Cache invalidation:
- Rotation model:
- Rotation overlap rule:
- Revocation mechanism:
- Revocation propagation requirement:
- Concrete operational values routed to:
- Verification method:
- Rationale:

### 13.4 Digest profile

- Classification:
- Allowed digest algorithms:
- Required default algorithm:
- Encoding:
- Canonical case:
- Algorithm-specific length rule:
- Declared-algorithm consistency validation:
- BLAKE2B or variable-length algorithm treatment:
- Verification method:
- Rationale:

## 14. Persistence, Ledger, and Atomicity

**Completion guidance:** See Appendix C.13 for a transaction-boundary and ledger-sequencing example.

### 14.1 Database topology

- Classification:
- One database, multiple schemas, or multiple databases:
- Tenant partitioning:
- Tenant isolation mechanism:
- Row-level security, if applicable:
- Data ownership:
- Verification method:
- Rationale:

### 14.2 Atomic governance transaction

- Classification: `ADR_IDR_REQUIRED`
- Proposal-state changes included:
- Governance Evidence included:
- Ledger event included:
- Idempotency result included:
- Outbox record included:
- Approval artifact changes included:
- Canonical State projection changes included:
- Transaction boundary:
- External effects after commit:
- Crash-recovery behavior:
- Decision record:
- Verification method:
- Rationale:

### 14.3 Governance Ledger storage and sequencing

- Classification:
- Ledger backend:
- Structured-field storage:
- Canonical-byte storage:
- Hash-chain use:
- Hash-chain algorithm and formula:
- Sequence-allocation strategy:
- Per-tenant, per-domain, or global ordering:
- Timestamp role:
- Timestamp non-authority rule:
- Replay reconstruction rule:
- Verification method:
- Rationale:

### 14.4 Action-state projection

- Classification:
- Separate action-state store:
- Projection updated on write or derived on read:
- Projection reproducibility:
- Indexed lookup keys:
- Rebuild procedure:
- Verification method:
- Rationale:

## 15. Idempotency and Replay Protection

**Completion guidance:** See Appendix C.14. Define the full state machine, not only the uniqueness key.

### 15.1 Idempotency state machine

- Classification:
- Required interface operations:
- Uniqueness key:
- Request canonicalization:
- Request digest algorithm:
- Atomic reservation rule:
- In-progress behavior:
- Same-key, same-body behavior:
- Same-key, different-body behavior:
- Completed-response replay behavior:
- Retention period rule:
- Stored response representation:
- Encryption requirement:
- Cleanup behavior:
- Verification method:
- Rationale:

### 15.2 Approval and provenance replay protection

- Classification:
- Durable nonce uniqueness scope:
- Approval replay-prevention key:
- Signature replay-prevention key:
- Retention window:
- Expiration behavior:
- Cross-tenant replay prevention:
- Verification method:
- Rationale:

## 16. Determinism Controls

### 16.1 Authoritative time

- Classification:
- Authoritative time source:
- Clock synchronization requirement:
- Validity-window evaluation rule:
- Clock-skew rule:
- Failure behavior when time suitability cannot be established:
- Replay treatment of time:
- Verification method:
- Rationale:

### 16.2 Randomness

- Classification:
- Randomness permitted in governance evaluation: Yes / No
- Permitted deterministic pseudo-random use, if any:
- Seed derivation rule:
- Recorded replay inputs:
- Prohibited uses:
- Verification method:
- Rationale:

### 16.3 Floating-point processing

- Classification:
- Floating-point permitted in governance evaluation: Yes / No
- Permitted operations:
- Required precision and rounding:
- Integer or fixed-point alternatives:
- Cross-platform equivalence rule:
- Verification method:
- Rationale:

### 16.4 Canonicalization boundaries

- Classification:
- Objects canonicalized:
- Exact bytes hashed:
- Exact bytes signed:
- Canonical serialization version:
- Protected and unprotected fields:
- Excluded fields:
- Verification method:
- Rationale:

## 17. Canonical State Profile

**Completion guidance:** See Appendix C.15 for source qualification, snapshot, precedence, conflict, and fail-closed examples.

### 17.1 Canonical State source classes

- Classification: `ADR_IDR_REQUIRED`
- Tenant authoritative source:
- Identity and entitlement authoritative source:
- Configuration authoritative source:
- Policy authoritative source:
- Key authoritative source:
- Governance Ledger source:
- Additional authoritative sources:
- Non-authoritative context sources:
- Decision record:
- Rationale:

### 17.2 Snapshot construction

- Classification:
- Snapshot identity:
- Snapshot digest:
- Included source versions:
- Freshness requirements:
- Completeness requirements:
- Consistency requirements:
- Integrity requirements:
- Ordering suitability:
- Snapshot storage or reference:
- Replay reconstruction:
- Verification method:
- Rationale:

### 17.3 Resolution and conflict policy

- Classification:
- Deterministic source priority:
- Conflict-detection rule:
- Conflict-resolution rule:
- Fail-closed conditions:
- Source-unavailable behavior:
- HTTP or interface mapping for unavailable authoritative sources:
- Structural Refusal conditions:
- Verification method:
- Rationale:

## 18. Risk-Based Re-Evaluation

- Classification:
- Material-change representation:
- Typed authoritative-input digest changes:
- Dependency-edge model:
- Proposal-selection rule:
- Deterministic affected-proposal traversal:
- Proposal re-evaluation serialization:
- Unaffected-proposal treatment:
- Recorded no-op outcomes:
- Re-evaluation outcome representation:
- Interface response behavior:
- Verification method:
- Rationale:

## 19. Policy Evaluation Module and Policy Evaluation Contract

**Completion guidance:** See Appendix C.16. Technology selection belongs in the profile; the complete machine contract belongs in a controlled interface specification.

### 19.1 Execution environment

- Classification:
- Runtime format:
- Isolation model:
- In-process, process-isolated, or sandboxed:
- Module identity:
- Module version:
- Module digest:
- Module pinning rule:
- Activation and rollback rule:
- Verification method:
- Rationale:

### 19.2 Profile-specific machine contract

- Classification: `FIXED_NORMATIVE_OBLIGATION` after adoption of the profile-specific interface specification
- Companion interface identifier and version:
- ABI version:
- Input envelope:
- Output envelope:
- Exported function name:
- Memory convention:
- Deterministic host functions:
- Prohibited imports:
- External I/O restrictions:
- Fuel behavior:
- Memory behavior:
- Timeout behavior:
- Trap mapping:
- Module-digest binding:
- Activation semantics:
- Verification method:
- Evidence location:

### 19.3 Resource limits

- Classification: `DEPLOYMENT_CONFIGURATION`
- Value authority: `EXTERNAL_DEPLOYMENT_VALUE`; use `ILLUSTRATIVE_EXAMPLE` values in an informational example profile
- CPU or fuel policy:
- Memory policy:
- Timeout policy:
- Limit source in build/deploy repository:
- Failure mapping:
- Development overlay:
- Production overlay:
- Verification method:

### 19.4 Replay purity

- Classification:
- State-snapshot input rule:
- Host-input rule:
- External I/O rule:
- Time-input rule:
- Randomness rule:
- Side-effect prohibition:
- Replay evidence:
- Verification method:
- Rationale:

## 20. Concurrency and Processing Model

### 20.1 Concurrency control

- Classification: `ADR_IDR_REQUIRED`
- Worker model:
- Per-tenant concurrency:
- Proposal-scoped serialization:
- Transaction-isolation level:
- Advisory-lock use:
- Optimistic-version checks:
- Sequence allocation within transaction:
- Deadlock handling:
- Retry behavior:
- Deterministic ordering guarantee:
- Decision record:
- Verification method:
- Rationale:

### 20.2 Public processing model

- Classification:
- Synchronous or asynchronous public conformance surface:
- Pending Human Review representation:
- Deferred representation:
- Governed Re-evaluation Required representation:
- Transient internal state exposure prohibited:
- Polling or callback behavior, if applicable:
- Verification method:
- Rationale:

## 21. HTTP and Service Outcome Mapping

**Completion guidance:** See Appendix C.17. Distinguish transport rejection, service unavailability, governance outcomes, and protected internal detail.

Complete this section only where HTTP is adopted. Otherwise identify the applicable transport-specific mapping.

| Condition | Profile mapping | Classification | Governing rationale | Verification |
|---|---|---|---|---|
| Invalid transport syntax | | | | |
| Invalid schema or asserted format | | | | |
| Invalid authoritative content | | | | |
| Semantic binding failure | | | | |
| Authentication failure | | | | |
| Authorization failure where existence is known | | | | |
| Resource not found | | | | |
| Cross-tenant resource lookup | | | | |
| Command or precondition conflict | | | | |
| Authoritative source unavailable | | | | |
| Pre-governance tenant throttling | | | | |
| Pre-governance global throttling | | | | |
| System-wide unavailable capacity | | | | |
| Governance policy quota denial | | | | |
| Authoritative re-evaluation outcome | | | | |
| Structural Refusal | | | | |

### 21.1 Rate limiting and service exhaustion

- Classification:
- Tenant-specific limits:
- Global limits:
- Concrete values routed to:
- HTTP 429 use:
- `Retry-After` rule:
- HTTP 503 use:
- Governance quota-denial distinction:
- Governance Evidence generation rule:
- Verification method:
- Rationale:

## 22. Validation Pipeline

**Completion guidance:** See Appendix C.18. The order must be deterministic and must identify which failures occur before governance processing begins.

The profile shall define the ordered validation pipeline and the conditions required to enter governance processing.

| Validation stage | Required behavior | Failure outcome | Evidence | Verification |
|---|---|---|---|---|
| Transport and size limits | | | | |
| Strict serialization parsing | | | | |
| Schema validation | | | | |
| Asserted-format validation | | | | |
| Semantic binding validation | | | | |
| Provenance verification | | | | |
| Authentication verification | | | | |
| Authorization and tenant binding | | | | |
| Canonical State suitability | | | | |
| Governance-processing entry | | | | |

- Classification:
- Unknown-field policy:
- Duplicate-key policy:
- Numeric-format policy:
- String-normalization policy:
- Validation ordering rule:
- Failure short-circuit rule:
- Verification method:
- Rationale:

## 23. Retention, Archival, and Deletion

### 23.1 Governance Evidence and Ledger

- Classification:
- Evidence retention rule:
- Ledger retention rule:
- Public deletion support:
- Destructive deletion prohibition:
- Archival authority:
- Archive immutability:
- Archive retrieval:
- Legal or compliance constraints:
- Concrete schedules routed to:
- Verification method:
- Rationale:

### 23.2 Idempotency, nonce, and operational records

| Record class | Profile retention rule | Concrete value location | Deletion or expiry behavior | Verification |
|---|---|---|---|---|
| Idempotency records | | | | |
| Provenance nonces | | | | |
| Approval replay records | | | | |
| Operational logs | | | | |
| Telemetry | | | | |
| Cached metadata | | | | |

## 24. Implementation Metadata

- Classification: `FIXED_NORMATIVE_OBLIGATION` where required by the adopted interface
- AGCP public base path: `/agcp/v2`
- Metadata operation and path: `GET /agcp/v2/meta`
- Endpoint origin or hostname: [profile-defined or external deployment value; illustrative in an example profile]
- Profile ID field:
- Profile version field:
- Profile URI field:
- Profile digest field:
- Base AGCP version field:
- Baseline digest field:
- Capability representation:
- Interface version representation:
- Schema and registry version representation:
- Conformance claim-status representation:
- Public-information limitation:
- Metadata signing rule:
- Generation point:
- Cache rule:
- Dependency-outage behavior:
- Last-valid-document behavior:
- Verification method:
- Evidence location:

## 25. External Build and Deployment Configuration Routing

**Completion guidance:** See Appendix C.19. Record stable limits and approval rules here; store concrete mutable values in overlays or runbooks.

The base profile shall define controlling rules. Concrete mutable values shall be maintained in approved artifacts in the implementation build/deploy repository. Deployment overlays and runbooks are external references and are not part of the AGCP profile package.

| Configuration class | Controlling profile rule | Development build/deploy path | Production build/deploy or runbook path | Approval authority |
|---|---|---|---|---|
| Tenant rate limits | | | | |
| Global rate limits | | | | |
| CPU and fuel limits | | | | |
| Memory limits | | | | |
| Timeouts | | | | |
| Cache sizes | | | | |
| Cache refresh intervals | | | | |
| Database connection limits | | | | |
| Worker counts | | | | |
| Telemetry sinks | | | | |
| Log levels | | | | |
| Backup schedules | | | | |
| Restore-test schedules | | | | |
| RTO | | | | |
| RPO | | | | |
| Secret-rotation cadence | | | | |
| Key-rotation cadence | | | | |
| Incident-response contacts | | | | |
| Host and network topology | | | | |
| Internal mTLS configuration | | | | |

## 26. Operational Hardening and Lifecycle

### 26.1 Backup and disaster recovery

- Classification: `DEPLOYMENT_CONFIGURATION`
- Data classes included:
- Key-material backup rule:
- Backup integrity protection:
- Restore-test requirement:
- RTO rule:
- RPO rule:
- Development runbook in build/deploy repository:
- Production runbook in build/deploy repository:
- Verification evidence:

### 26.2 Database migration

- Classification:
- Migration tooling:
- Forward-only or reversible policy:
- Pre-migration validation:
- Data compatibility rule:
- Rollback rule:
- Evidence preservation:
- Verification method:
- Rationale:

### 26.3 Upgrade, rollout, activation, and rollback

- Classification:
- Release-candidate process:
- Configuration immutability rule:
- Startup validation:
- Atomic activation rule:
- Rollout strategy:
- Rollback strategy:
- Tenant suspension strategy:
- Emergency disablement boundaries:
- Prohibited bypass behavior:
- Verification method:
- Rationale:

### 26.4 Observability and incident readiness

- Classification: `DEPLOYMENT_CONFIGURATION`
- Required telemetry classes:
- Required audit fields:
- SLO rule:
- Alerting rule:
- Incident-response requirement:
- External beta readiness criteria:
- Runbook references:
- Verification evidence:

## 27. Release Engineering and Supply-Chain Evidence

- Classification:
- Whole-release signed manifest required:
- SBOM required:
- Binary provenance required:
- Build attestation required:
- Source revision binding:
- Dependency lockfile binding:
- Reproducible build requirement:
- Artifact-signing authority:
- Release metadata location:
- Verification method:
- Rationale:

## 28. Profile-Specific Verification and Conformance Extension

The official AGCP conformance suite establishes the minimum conformance basis. This section identifies additional tests required by the profile.

| Test class | Required | Scope | Test artifact | Acceptance criterion |
|---|---|---|---|---|
| Official conformance tests | | | | |
| Semantic binding tests | | | | |
| Positive controlled fixtures | | | | |
| Negative mismatch fixtures | | | | |
| Property tests | | | | |
| Mutation tests | | | | |
| Concurrency tests | | | | |
| Crash-recovery tests | | | | |
| Malicious-input tests | | | | |
| Cross-language cryptographic vectors | | | | |
| Canonicalization vectors | | | | |
| Tenant-isolation tests | | | | |
| Cross-domain authority tests | | | | |
| Key-rotation tests | | | | |
| Key-revocation tests | | | | |
| Tenant-suspension tests | | | | |
| PEP-bypass tests | | | | |
| Canonical State conflict tests | | | | |
| Risk-Based Re-Evaluation tests | | | | |
| Backup restoration tests | | | | |
| Metadata continuity tests | | | | |

## 29. Repository Correction Dependencies

**Completion guidance:** See Appendix C.20. Do not convert a repository defect into a local implementation choice.

Repository defects shall be resolved outside the profile through controlled specification change. The profile may identify and depend upon those corrections but shall not privately reinterpret them.

| Finding ID | Classification | Description | Required ruling or correction | Affected artifacts | Blocking scope | Status | Verification evidence |
|---|---|---|---|---|---|---|---|
| | `REPOSITORY_CORRECTION` | | | | | | |

## 30. Associated Decision Records

| Decision record | Subject | Status | Repository path or URI | Affected profile sections |
|---|---|---|---|---|
| | | | | |

At minimum, determine whether separate decision records are required for:

- enforcement-boundary placement;
- service and trust-boundary decomposition;
- command-versus-authoritative-record separation;
- private management-plane separation;
- cryptographic profile selection;
- authentication and tenant-binding architecture;
- Canonical State source precedence and fail-closed behavior;
- atomic persistence and outbox architecture;
- concurrency and sequence allocation; and
- policy-module isolation and ABI selection.

## 31. Traceability Record

**Completion guidance:** See Appendix C.21 for an example traceability row and relationship rationale.

### 31.1 Required traceability

| Profile section or decision | ARM reference(s) | NS reference(s) | CR reference(s) | DS reference(s) | IF reference(s) | REG reference(s) | TC reference(s) | ADR/IDR reference(s) | Repository artifact(s) |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

### 31.2 RTM update

- RTM dataset version:
- New or modified RTM records:
- Relationship types:
- Architectural rationale:
- Semantic review status:
- Verification status:
- Approval authority:
- Validation report:

## 32. Controlled Artifact Inventory and Repository Boundary

### 32.1 AGCP specification/profile repository artifacts

| Artifact | Identifier and version | Repository path or URI | SHA-256 digest | Lifecycle state | Approval status |
|---|---|---|---|---|---|
| Base AGCP release reference | | | | | |
| Implementation Profile | | | | | |
| Machine-readable profile record | | | | | |
| Informational-example notice, if applicable | | | | | |
| Profile digest record | | | | | |
| Profile-specific interface specification | | | | | |
| Profile-specific RTM extension | | | | | |
| Profile-specific conformance extension | | | | | |

### 32.2 External implementation build/deploy repository references

The following artifacts are referenced by the profile but belong in the implementation build/deploy repository. They shall not be packaged inside the AGCP profile directory.

| External artifact | Identifier and version | Build/deploy repository path or URI | Revision or digest | Environment or release | Approval status |
|---|---|---|---|---|---|
| Implementation source and build configuration | | | | | |
| Infrastructure definitions | | | | | |
| Development deployment overlay | | | | | |
| Test deployment overlay | | | | | |
| Staging deployment overlay | | | | | |
| Production deployment overlay | | | | | |
| Tenant-class configuration | | | | | |
| Operations runbooks | | | | | |
| Security and incident-response runbooks | | | | | |
| Backup, restoration, and disaster-recovery runbooks | | | | | |
| Release manifest | | | | | |
| SBOM | | | | | |
| Build provenance and attestations | | | | | |
| Release-specific conformance claim record | | | | | |

### 32.3 Repository-boundary verification

- Profile repository contains no `deploy/` directory: Yes / No
- Profile repository contains no `runbooks/` directory: Yes / No
- All external paths resolve to the identified build/deploy repository revision: Yes / No
- External artifacts are versioned or content-addressed where required: Yes / No
- Verification method:
- Evidence location:

## 33. Approval Record

| Review or approval | Required | Reviewer or authority | Date | Result | Evidence or record |
|---|---|---|---|---|---|
| Architecture Review | | | | | |
| Security Review | | | | | |
| Traceability Review | | | | | |
| Normative Review | | | | | |
| Schema Review | | | | | |
| Interface Review | | | | | |
| Registry Review | | | | | |
| Conformance Review | | | | | |
| Operations Review | | | | | |
| Specification Owner Approval | | | | | |
| Implementation Owner Approval | | | | | |
| Publication Approval | | | | | |

## 34. Publication Readiness Checklist

**Completion guidance:** See Appendix C.22 for the expected completion sequence and approval gate.

A profile is ready for controlled publication only when all applicable checks are complete.

- [ ] Profile ID and version are unique and stable.
- [ ] Profile status and lifecycle state are defined.
- [ ] Exact AGCP baseline and digest are recorded.
- [ ] Artifact mode is identified as controlled implementation profile or informational example profile.
- [ ] AGCP-connected values are source-derived and identified as controlled rather than illustrative.
- [ ] Informational-example implementation and deployment values are explicitly labeled illustrative.
- [ ] The AGCP public base path is `/agcp/v2`, and the metadata path is `GET /agcp/v2/meta`.
- [ ] All adopted companion specifications are identified.
- [ ] Claimed enforcement scope and exclusions are explicit.
- [ ] Conformance target and current claim status are separate and accurate.
- [ ] Mandatory obligations are not presented as optional selections.
- [ ] Every profile selection has a rationale and verification method.
- [ ] Every deployment-specific value is routed to an overlay or runbook.
- [ ] Deployment overlays and runbooks are referenced from the implementation build/deploy repository and are not included in the profile package.
- [ ] Hostnames, IP addresses, cloud services, resource limits, quotas, capacities, and operational targets in an informational example are marked illustrative.
- [ ] Every significant architectural decision references an approved ADR or IDR.
- [ ] Repository corrections are dispositioned or recorded as explicit blockers.
- [ ] Public and private interfaces are separated as required.
- [ ] Command and submission objects are distinct from authoritative AGCP records.
- [ ] Canonical State sources, freshness, priority, and fail-closed behavior are defined.
- [ ] PEP placement and non-bypassability scope are testable.
- [ ] Cryptographic, digest, nonce, and replay rules are internally consistent.
- [ ] Idempotency behavior is complete and testable.
- [ ] Atomic persistence and external-effect publication rules are defined.
- [ ] Policy-module ABI and deterministic execution contract are controlled.
- [ ] Validation order and failure mappings are defined.
- [ ] Metadata publication includes profile and baseline identity.
- [ ] Profile-specific verification requirements are defined.
- [ ] RTM updates are complete and approved.
- [ ] Associated artifacts are versioned, content-addressed, and inventoried.
- [ ] No unresolved `TBD` or `TBC` values remain for the assigned lifecycle state.
- [ ] Profile digest is calculated after final approval.

## 35. Revision History

| Profile version | Date | Change summary | Change classification | Affected sections | Approval authority |
|---|---|---|---|---|---|
| | | | | | |

## Appendix A - Repeatable Decision Entry

Use this structure when a profile decision requires more detail than the section-specific fields provide.

### Decision [Profile Decision ID] - [Title]

- Classification:
- Status:
- Controlling AGCP source(s):
- Related finding or requirement IDs:
- Decision:
- Profile statement:
- Rationale:
- Alternatives considered:
- Security consequences:
- Interoperability consequences:
- Conformance consequences:
- Deployment consequences:
- Affected schemas:
- Affected interfaces:
- Affected registries:
- Affected tests:
- Affected RTM records:
- Required ADR or IDR:
- Required deployment overlay or runbook:
- Verification method:
- Evidence location:
- Approval authority:
- Approval date:

## Appendix B - Prohibited Template Outcomes

A completed profile shall not:

- treat a mandatory AGCP behavior as optional;
- state or imply conformance before all applicable mandatory requirements are satisfied;
- resolve a controlled repository contradiction through undocumented local code behavior;
- allow claimant-supplied assertions to become authoritative AGCP facts without qualification;
- claim non-bypassability outside the actual enforcement boundary;
- use a moving repository branch as an unidentified normative baseline;
- omit version or digest bindings needed for deterministic reproduction;
- embed mutable production values in the base profile without an explicit versioning rationale;
- leave a profile-specific machine contract as undocumented implementation behavior; or
- permit lower-precedence profile language to override a higher-precedence AGCP source.

## Appendix C - Completion Guidance and Worked Examples

### C.1 Purpose and status of this appendix

This appendix explains how to complete the template. It is authoring guidance only. Its examples do not establish AGCP requirements, select technologies for every profile, or resolve conflicts in controlled AGCP artifacts.

A completed controlled implementation profile should normally remove this appendix so that the published artifact contains only approved profile content. An informational example may retain selected explanatory notes, provided they remain clearly non-normative. A template maintained for repeated use should retain the appendix.

Throughout the examples below, AGCP identifiers and interface paths are real only where they are identified as AGCP-controlled. Implementation names, product names, cloud platforms and services, identity providers, hostnames, IP addresses, resource limits, timing values, capacities, repository names, and approval identities are illustrative unless explicitly stated otherwise.

### C.2 Choosing the correct classification

Use the classification that describes the source of authority for the entry, not merely the importance of the decision.

| Situation | Correct classification | Example disposition |
|---|---|---|
| The adopted public interface requires an `Idempotency-Key` header. | `FIXED_NORMATIVE_OBLIGATION` | Record the interface identifier, operation applicability, implementation mapping, tests, and evidence. Do not ask whether the header is required. |
| The profile selects Ed25519 from algorithms permitted by the governing specifications. | `PROFILE_SELECTION` | State Ed25519, the encoding and canonicalization rules, compatibility effects, and test vectors. |
| Production rate limits may change without changing the implementation architecture. | `DEPLOYMENT_CONFIGURATION` | State the controlling rate-limit model in the profile and place exact values in the production overlay. |
| The placement of the PEP determines the actual non-bypassability boundary. | `ADR_IDR_REQUIRED` | Summarize the approved decision in the profile and reference the decision record. |
| A schema contradicts a higher-precedence wire-format specification. | `REPOSITORY_CORRECTION` | Record the dependency and block affected structure finalization until the controlled repository is corrected. |

A single topic may require more than one classification. For example, Section 13.1 may contain a `PROFILE_SELECTION` for the chosen signature algorithm and a `REPOSITORY_CORRECTION` dependency for an unresolved provenance representation conflict.

### C.3 Writing definitive and testable entries

A complete entry answers five questions:

1. What exactly is required, selected, prohibited, or routed elsewhere?
2. Which controlled source authorizes or requires it?
3. Why is this value appropriate for the profile?
4. How is compliance verified?
5. Where is the verification evidence retained?

#### Inadequate

> Authentication: OIDC.

#### Adequate

> **Classification:** `PROFILE_SELECTION`  
> **Decision or Rule:** Public IF-001 requests SHALL use asymmetric OIDC access tokens validated against an issuer-allowlisted JWKS. Tokens SHALL contain the required audience, subject, and tenant claims. Symmetric JWT algorithms and unsigned tokens are prohibited.  
> **Controlling Source:** [Profile-specific authentication ADR], [adopted IF-001 version].  
> **Rationale:** The selection supports tenant-bound external authentication without making OIDC a universal AGCP requirement.  
> **Verification Method:** Execute positive and negative token-validation vectors covering issuer, audience, signature, expiry, tenant, and algorithm restrictions.  
> **Evidence Location:** `conformance/profile/authentication/` and the release assessment record.

### C.4 Profile Control Record example

The example below demonstrates format only. Every non-AGCP implementation value is `ILLUSTRATIVE_EXAMPLE`.

| Field | Example profile value | Value authority |
|---|---|---|
| Artifact Mode | `Informational Example Profile` | Template-defined classification |
| Operational Deployment | `No` | `ILLUSTRATIVE_EXAMPLE` status |
| Profile ID | `AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-2.0.0` | `ILLUSTRATIVE_EXAMPLE` |
| Profile Name | `AGCP Full-Scope Multitenant Example Profile` | `ILLUSTRATIVE_EXAMPLE` |
| Profile Version | `1.0.0` | `ILLUSTRATIVE_EXAMPLE` |
| Repository Path or URI | `implementer/AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-PROFILE.md` | `ILLUSTRATIVE_EXAMPLE` repository path |
| Profile SHA-256 Digest | `Calculated after final example content is fixed` | `COMPUTED_ARTIFACT_VALUE` |
| Publication Status | `INFORMATIONAL_EXAMPLE_NON_NORMATIVE` | Example status |
| Artifact Lifecycle State | `EXAMPLE` | Example status |
| Profile Owner | `Example profile maintainer` | `ILLUSTRATIVE_EXAMPLE` |
| Technical Owner | `Example technical authority` | `ILLUSTRATIVE_EXAMPLE` |
| Approval Authority | `Not Applicable - informational example` | Example status |
| Approval Date | `Not Applicable` | Example status |
| Effective Date | `Not Applicable` | Example status |
| Review Date | `Not Applicable` | Example status |
| Supersedes | `None` | Example status |
| Superseded By | `None` | Example status |

For a real controlled implementation profile, replace illustrative values with approved `PROFILE_DEFINED`, `EXTERNAL_DEPLOYMENT_VALUE`, or `COMPUTED_ARTIFACT_VALUE` values and record their controlling evidence.

### C.5 Controlled Baseline example

#### Example base-release record

| Field | Example profile value | Value authority |
|---|---|---|
| AGCP Specification Version | `2.0.0` | `AGCP_CONTROLLED` |
| Publication Maturity | `PUBLIC_REVIEW_CONTROLLED_BASELINE` | `AGCP_CONTROLLED` |
| Controlled Baseline Date | `2026-07-30` | `AGCP_CONTROLLED` |
| Baseline Bundle Name | `<exact controlled release bundle name>` | `AGCP_CONTROLLED` when copied from the release; otherwise a placeholder |
| Baseline Bundle Repository Path or URI | `<exact controlled release location>` | `AGCP_CONTROLLED` when resolved |
| Baseline Bundle SHA-256 Digest | `<computed 64-character lowercase SHA-256 digest>` | `COMPUTED_ARTIFACT_VALUE` |
| Supported Baseline Count | `One` | `PROFILE_DEFINED` |
| Baseline Migration Rule | `A different bundle digest requires an approved profile migration record and re-execution of affected verification.` | `PROFILE_DEFINED` |

#### Example artifact-pinning entry

- **Classification:** `PROFILE_SELECTION`
- **Authoritative artifact source:** Extracted machine-readable files in the hash-pinned baseline bundle.
- **Extracted machine-readable artifact policy:** Runtime loading is permitted only from files whose path and digest match the signed release manifest.
- **Embedded-document artifact policy:** Embedded copies are informative unless their digest is explicitly listed as authoritative by the manifest.
- **Hash-pinning rule:** Every normative or executable artifact consumed by the implementation is bound by SHA-256 digest.
- **Semantic-version role:** Semantic versions identify compatibility intent but do not replace content-addressed pinning.
- **Multi-version support rule:** Only the active baseline is loaded by a running instance.
- **Change-detection mechanism:** Startup manifest validation and continuous configuration-integrity checks.
- **Migration approval requirement:** Architecture, traceability, and conformance impact review.
- **Verification method:** Alter one pinned artifact and verify startup refusal; execute manifest-validation tests.
- **Rationale:** This prevents a moving repository branch or reused version label from silently changing the normative basis.

### C.6 Conformance Posture example

Conformance target and claim status are different fields.

| Field | Example profile value |
|---|---|
| Target AGCP Conformance Level or Scope | `All mandatory requirements applicable to the multitenant L5 target and the adopted companion specifications` |
| Current Conformance Claim Status | `Not Claimed` |
| Applicable Mandatory Requirements | `CR-001 through CR-122, subject to profile applicability mapping` |
| Supported Optional Capabilities | `Human approval, deterministic WASM PEM, tenant-scoped operations export` |
| Unsupported Optional Capabilities | `Cross-domain authority transfer` |
| Applicable Companion Specifications | `[exact identifiers and versions]` |
| Applicable Profile-Specific Conformance Extension | `AGCP-EXAMPLE-TEST-EXT-2.0.0` (`ILLUSTRATIVE_EXAMPLE`) |
| Conformance Claim Record | `Not Applicable until all mandatory tests pass` |

#### Example conformance statement

> This implementation is built against the AGCP v2.0.0 controlled baseline identified by the recorded bundle digest and targets the capability scope defined by the identified profile (`ILLUSTRATIVE_EXAMPLE` identifier in an example profile). No AGCP production-conformance claim is made until all applicable mandatory requirements and profile-specific verification criteria have been satisfied and an approved conformance claim record has been published.

Do not state `conformant`, `certified`, or `verified` merely because the profile is complete.

### C.7 Claimed Enforcement Scope example

#### Example enforcement-boundary entry

- **Classification:** `ADR_IDR_REQUIRED`
- **Claimed enforcement scope:** The owner-controlled public governance service, governance runtime, persistence layer, and owner-controlled PEP/executor that performs the governed consequence.
- **Governed consequence classes within scope:** Mutations executed by the owner-controlled executor after successful Commit Boundary processing.
- **Owner-controlled services within scope:** Public IF-001 service, decision service, realization service, ledger writer, Canonical State adapters, and executor.
- **External systems explicitly outside scope:** Arbitrary student applications, external user devices, and independently operated executors that can act without invoking the owner-controlled PEP.
- **Execution paths explicitly excluded from the non-bypassability claim:** Any path not technically mediated by the owner-controlled PEP/executor.
- **Decision record:** `ADR-PEP-001`.
- **Verification method:** Architecture inspection, route-to-executor tests, direct-database-write denial tests, and PEP-bypass attempts.
- **Rationale:** Non-bypassability is claimed only where the implementation has actual technical authority to prevent the governed consequence.

#### Example non-bypassability statement

> Every governed state mutation performed by the owner-controlled executor within this profile's enforcement scope SHALL require a current, proposal-bound governance decision and integrity-protected Enforcement Context applied by the owner-controlled PEP at or immediately adjacent to the Commit Boundary. The profile does not claim to prevent independent external software from producing consequences outside that boundary.

### C.8 Capability and Applicability example

Use these applicability values consistently:

- `Mandatory - Implemented`
- `Mandatory - Not Yet Implemented`
- `Optional - Supported`
- `Optional - Unsupported`
- `Not Applicable` with rationale

| Capability or requirement group | Example applicability | Example controlling source | Example implementation mapping | Example verification evidence |
|---|---|---|---|---|
| Risk-Based Re-Evaluation | `Mandatory - Implemented` | `CR-122; Core Section [x]; NS-[x]` | `src/reevaluation/selector.rs`, dependency-index schema, and ledger event mapping | `TC-122`, selector property tests, and recorded no-op outcome fixtures |

Do not use `Supported` without indicating whether the capability is mandatory or optional and whether implementation is complete.

### C.9 Interface Profile example

- **Classification:** `FIXED_NORMATIVE_OBLIGATION`
- **Adopted interface identifier and version:** `IF-001 v2.0.0`.
- **Required operations:** List every adopted operation by operation identifier, not merely `all endpoints`.
- **Required request and response schemas:** List exact schema identifiers and versions.
- **Required `Idempotency-Key` behavior:** Required on the operations identified by IF-001; absence is rejected before governance processing.
- **AGCP public base path:** `/agcp/v2` (`AGCP_CONTROLLED`).
- **Required implementation metadata operation and path:** `GET /agcp/v2/meta` (`AGCP_CONTROLLED`).
- **Endpoint origin or hostname:** `EXTERNAL_DEPLOYMENT_VALUE`; use a reserved `.example` hostname in an informational example.
- **Required error model:** Reference the adopted public error schema and Section 21 mappings.
- **Synchronous or asynchronous behavior permitted by the adopted interface:** State the actual profile selection and how Pending Human Review or Deferred outcomes are represented.
- **Verification method:** OpenAPI validation, contract tests, required-header tests, and controlled examples.
- **Evidence location:** Published interface-test report.

If the governing interface has not yet established a required behavior, classify the unresolved question correctly rather than marking it as a fixed obligation.

### C.10 Ingress trust-boundary example

- **Classification:** `ADR_IDR_REQUIRED`
- **Untrusted command or submission object types:** `GovernanceApprovalSubmission`, `ProposalSubmission`, and `KeyRegistrationRequest`.
- **Authoritative AGCP-created record types:** `GovernanceApprovalArtifact`, `QualifiedProposalRecord`, and `RegisteredKeyRecord`.
- **Server-derived fields that claimants may not assert authoritatively:** `signature_verified`, `eligibility_verified`, `nonce_unique`, `qualified_at`, `derived_lifecycle_effect`, and authoritative evidence relationships.
- **Qualification process:** Parse, schema-validate, bind to tenant and proposal, verify provenance and identity, consult current Canonical State, and produce either Structural Refusal or an attributable authoritative record.
- **Conversion from submission to authoritative record:** Performed only by the governance service in the same controlled transaction that records qualification evidence.
- **Rejection behavior:** Invalid claimant assertions are ignored only where the schema expressly treats them as non-authoritative; otherwise the request is rejected.
- **Decision record:** `ADR-TRUST-BOUNDARY-001`.
- **Verification method:** Attempt to submit each server-derived field and verify rejection or non-authoritative treatment; verify authoritative records are created only after qualification.

### C.11 Authentication and tenant-binding example

- **Classification:** `PROFILE_SELECTION`
- **Authentication mechanism:** OIDC access tokens verified through an issuer-allowlisted JWKS (`ILLUSTRATIVE_EXAMPLE` unless adopted by a real profile).
- **Identity provider model:** One approved issuer for the initial profile; a later profile may add per-tenant issuers.
- **Token or credential type:** Asymmetric signed JWT access token.
- **Asymmetric algorithm allowlist:** `EdDSA` with Ed25519 (`ILLUSTRATIVE_EXAMPLE`), or the exact approved selection for a real profile.
- **Required audience:** Exact service audience identifier.
- **Subject identifier source:** `sub` claim.
- **Tenant identifier source:** `tenant_id` claim.
- **Route, body, query, and credential tenant-binding rule:** All tenant identifiers SHALL match exactly after schema-defined normalization; absence or mismatch is fail-closed.
- **Tenant mismatch behavior:** Public `404 RESOURCE_NOT_FOUND`; protected evidence records the mismatch category.
- **Server-side authorization revalidation:** Required for every operation; token scopes are inputs and are not treated as authority at commitment.
- **Verification method:** Positive and negative JWT vectors, cross-tenant lookup tests, and tenant-suspension tests.

Replace claim names and algorithms if the actual profile selects different permitted values.

### C.12 Cryptography example

- **Classification:** `PROFILE_SELECTION`
- **Signature algorithm:** Ed25519.
- **Canonicalization method:** RFC 8785 JSON Canonicalization Scheme.
- **Character encoding:** UTF-8.
- **Base64url padding rule:** Unpadded.
- **Protected-header contract:** Exact allowed members, required values, and ordering-independent canonicalization are defined by the adopted provenance interface.
- **Key identifier representation:** Tenant-scoped JWK `kid`.
- **Signing-time rule:** `signed_at` is evaluated against the authoritative time source and recorded in replay evidence.
- **Clock-skew allowance:** Maximum five minutes, with exact value maintained as a stable profile rule or routed to an overlay only if variability is expressly permitted.
- **Nonce rule:** Nonce uniqueness is durable within the tenant, signer, key, and defined scope.
- **Replay-retention rule:** At least 24 hours for the initial profile.
- **Verification-failure mapping:** Public response follows Section 21; detailed cryptographic reason is retained in protected evidence.
- **Verification method:** Cross-language signing vectors, modified-byte tests, wrong-tenant key tests, expiry tests, and replay tests.

#### Digest example

- **Allowed digest algorithms:** `SHA-256`.
- **Encoding:** Lowercase hexadecimal.
- **Algorithm-specific length rule:** Exactly 64 hexadecimal characters.
- **Declared-algorithm consistency validation:** The value is rejected unless its syntax and length match the declared algorithm.

Do not write `SHA-256 or similar` or accept variable digest lengths without a defined algorithm relationship.

### C.13 Atomic persistence and ledger example

- **Classification:** `ADR_IDR_REQUIRED`
- **Transaction boundary:** One database transaction atomically persists proposal state, Governance Evidence, the ledger event, the idempotency result, and the outbox record.
- **Approval artifact changes included:** Included when the operation qualifies or consumes approval evidence.
- **Canonical State projection changes included:** Included only for projections owned by the transaction; external authoritative sources remain referenced by immutable snapshot identity.
- **External effects after commit:** The outbox publisher may emit external effects only after the transaction commits successfully.
- **Crash-recovery behavior:** A crash before commit produces no authoritative partial result; a crash after commit is recovered through idempotent outbox publication.
- **Decision record:** `ADR-PERSISTENCE-001`.
- **Verification method:** Fault injection before and after each persistence step, transaction rollback checks, duplicate-delivery tests, and ledger/state consistency queries.

#### Ledger sequencing example

- **Sequence-allocation strategy:** Allocate the tenant-scoped ledger sequence inside the same serializable transaction as the ledger write.
- **Timestamp role:** Timestamps provide attributable temporal evidence but do not establish authoritative event order.
- **Replay reconstruction rule:** Replay uses the authoritative sequence and stored canonical bytes or integrity-bound structured representation.

### C.14 Idempotency example

- **Classification:** `PROFILE_SELECTION` and `FIXED_NORMATIVE_OBLIGATION` where required by IF-001.
- **Uniqueness key:** `(tenant_id, operation_id, idempotency_key)`.
- **Request canonicalization:** RFC 8785 JCS over the complete governance-significant request body plus operation identity and tenant binding.
- **Request digest algorithm:** SHA-256.
- **Atomic reservation rule:** The key and request digest are reserved in the same transaction that begins authoritative processing.
- **In-progress behavior:** A duplicate matching request receives the defined in-progress response and cannot initiate duplicate governance processing.
- **Same-key, same-body behavior:** Return the stored authoritative response when complete.
- **Same-key, different-body behavior:** Reject with HTTP 409 and the public conflict code.
- **Completed-response replay behavior:** Return the same authoritative status and body, subject to protected-header regeneration rules expressly defined by the interface.
- **Retention period rule:** At least 24 hours for the initial profile.
- **Stored response representation:** Full response body encrypted at rest, or another exact approved choice.
- **Verification method:** Concurrent duplicate tests, crash-recovery tests, changed-body tests, and expiry-boundary tests.

### C.15 Canonical State example

#### Source classes

- **Classification:** `ADR_IDR_REQUIRED`
- **Tenant authoritative source:** Owner-controlled tenant registry.
- **Identity and entitlement authoritative source:** Approved identity and entitlement adapter.
- **Configuration authoritative source:** Active, integrity-verified configuration release.
- **Policy authoritative source:** Atomically activated policy bundle.
- **Key authoritative source:** Tenant-scoped key registry and revocation state.
- **Governance Ledger source:** Authoritative for recorded governance events, event ordering, and Derived Lifecycle State.
- **Non-authoritative context sources:** Request context, telemetry, and agent assertions unless separately qualified.

#### Snapshot

- **Snapshot identity:** Stable identifier generated from the ordered set of source identifiers and versions.
- **Snapshot digest:** SHA-256 over the profile-defined canonical snapshot manifest.
- **Freshness requirements:** Define a maximum age or event-driven invalidation rule for each source class.
- **Completeness requirements:** Every source required by the proposal's dependency set must be present.
- **Conflict-resolution rule:** Apply the approved deterministic source precedence only where the sources are authorized to overlap.
- **Fail-closed conditions:** Missing, stale, unverifiable, inconsistent, or unresolved conflicting authoritative inputs prevent admissibility processing.
- **Source-unavailable behavior:** Map service unavailability separately from a governance Structural Refusal as established by Section 21.
- **Verification method:** Stale-source, conflicting-source, unavailable-source, altered-snapshot, and replay tests.

Do not describe the ledger as the originating system of record for every governance-relevant fact unless the implementation actually makes that design choice and it remains consistent with the controlled Core.

### C.16 PEM and machine-contract example

#### Profile selection

- **Classification:** `PROFILE_SELECTION`
- **Runtime format:** WebAssembly.
- **Isolation model:** Deterministic sandbox with no ambient network, filesystem, clock, randomness, or process access.
- **Module identity:** Stable module identifier plus version and digest.
- **Module pinning rule:** Evaluation uses the module digest recorded in the active governance configuration and evidence.
- **Activation and rollback rule:** Activation is atomic; rollback activates a previously approved digest and produces governance evidence.

#### Controlled IF-002 companion

The profile should reference, rather than duplicate, the complete ABI specification. The companion should define at least:

- ABI version;
- input and output envelopes;
- exported function name;
- memory ownership and allocation conventions;
- deterministic host functions;
- prohibited imports;
- fuel, memory, timeout, and trap behavior;
- module-digest binding; and
- activation semantics.

The profile may summarize the selection, but undocumented Rust function signatures or runtime behavior are not a controlled machine contract.

### C.17 HTTP and service-outcome example

| Condition | Example profile mapping | Example classification | Example rationale |
|---|---|---|---|
| Invalid transport syntax | `400 BAD_REQUEST` | `PROFILE_SELECTION` or fixed by adopted interface | Request cannot be parsed as the adopted transport. |
| Invalid authoritative content | `422 UNPROCESSABLE_CONTENT` | `PROFILE_SELECTION` | Syntax is valid, but authoritative semantic content is invalid. |
| Resource not found | `404 RESOURCE_NOT_FOUND` | `PROFILE_SELECTION` plus repository reconciliation if needed | Public response does not disclose protected resource type. |
| Cross-tenant resource lookup | `404 RESOURCE_NOT_FOUND` | `PROFILE_SELECTION` | Implements the HIDE_404 disclosure policy. |
| Command or precondition conflict | `409 CONFLICT` | `PROFILE_SELECTION` | The command conflicts with an existing idempotency reservation or state precondition. |
| Authoritative source unavailable | `503 SERVICE_UNAVAILABLE` | `PROFILE_SELECTION` | Processing cannot establish the required authoritative basis. |
| Pre-governance tenant throttling | `429 TOO_MANY_REQUESTS` with `Retry-After` | `PROFILE_SELECTION` plus `DEPLOYMENT_CONFIGURATION` for values | Transport/service throttling occurs before governance evaluation. |
| Governance policy quota denial | Authoritative governance outcome | `FIXED_NORMATIVE_OBLIGATION` or profile mapping | A governance denial is not reduced to transport throttling. |
| Authoritative re-evaluation outcome | `200` with the authoritative outcome representation | `PROFILE_SELECTION` | Re-evaluation completed and produced a governance result. |

Record detailed internal cause information in protected evidence rather than exposing tenant or resource existence publicly.

### C.18 Validation Pipeline example

| Validation stage | Example required behavior | Example failure outcome |
|---|---|---|
| Transport and size limits | Reject a body exceeding the operation-specific maximum before parsing. | Transport rejection; no governance processing. |
| Strict serialization parsing | Reject duplicate object keys and malformed UTF-8. | `400 BAD_REQUEST`. |
| Schema validation | Validate against the exact hash-pinned schema and asserted formats. | `422` or adopted interface mapping. |
| Semantic binding validation | Verify proposal, tenant, target, policy, artifact, and evidence identifiers agree. | Public semantic rejection; protected mismatch evidence. |
| Provenance verification | Verify canonical bytes, signature, key purpose, tenant scope, validity, and nonce. | Verification rejection. |
| Authentication verification | Validate issuer, audience, signature, time, subject, and tenant claims. | `401` or adopted interface mapping. |
| Authorization and tenant binding | Revalidate endpoint scope and all tenant relationships. | `403` where existence is known; otherwise `404`. |
| Canonical State suitability | Establish qualified authoritative sources and immutable snapshot identity. | Structural Refusal or `503`, according to the cause and adopted mapping. |
| Governance-processing entry | Create the authoritative qualification record and enter the governance pipeline. | Only possible after all prior required stages succeed. |

- **Unknown-field policy:** Reject unknown fields where schemas set `additionalProperties: false` or equivalent strictness.
- **Duplicate-key policy:** Reject duplicate keys during parsing.
- **Failure short-circuit rule:** Stop at the first stage whose failure prevents later stages; still generate the evidence required for that failure class.

### C.19 Deployment-configuration routing example

| Configuration class | Example controlling profile rule | Example development location | Example production location | Example approval authority |
|---|---|---|---|---|
| Tenant rate limits | Limits SHALL be tenant-scoped, fail predictably, and use the Section 21 overload mapping. | `<build-deploy-repo>/deploy/development/limits.yaml` | `<build-deploy-repo>/deploy/production/limits.yaml` | Operations Authority |
| PEM memory limits | Every module execution SHALL have a finite approved memory ceiling; exceeding it produces the IF-002 resource-limit outcome. | `<build-deploy-repo>/deploy/development/pem.yaml` | `<build-deploy-repo>/deploy/production/pem.yaml` | Security and Operations Authorities |
| RTO | A tested recovery objective SHALL be defined before external beta. | `<build-deploy-repo>/runbooks/development-disaster-recovery.md` | `<build-deploy-repo>/runbooks/production-disaster-recovery.md` | Operations Authority |

The profile states what must remain true across environments. The external build/deploy overlay or runbook states the current number, endpoint, cadence, address, or host-specific value. These files belong in the implementation build/deploy repository, not in the AGCP profile package.

A concrete value belongs in the base profile only when interoperability or conformance depends on it and changing it requires a profile version change.

### C.20 Repository-correction dependency example

| Finding ID | Classification | Description | Required ruling or correction | Affected artifacts | Blocking scope | Status | Verification evidence |
|---|---|---|---|---|---|---|---|
| `P0-02` | `REPOSITORY_CORRECTION` | Provenance wire-format fields conflict with the common provenance schema. | Select the authoritative representation and synchronize schemas, examples, OpenAPI, vectors, catalogs, hashes, and validation reports. | Provenance specification, common schema, dependent schemas, examples, OpenAPI, tests, catalog | Freezing public provenance structs and interoperability claims | `Open` | Corrected artifacts validate and all dependent tests pass |

A profile may state that it depends on the corrected representation. It shall not silently choose one incompatible representation in code and describe that private interpretation as AGCP behavior.

### C.21 Traceability example

| Profile section or decision | ARM reference(s) | NS reference(s) | CR reference(s) | DS reference(s) | IF reference(s) | REG reference(s) | TC reference(s) | ADR/IDR reference(s) | Repository artifact(s) |
|---|---|---|---|---|---|---|---|---|---|
| Claimed enforcement scope and PEP placement | `ARM-201`, `ARM-211`, `ARM-213` | `NS-9.1-01`, `NS-9.4-03`, `NS-9.6-04` | `[applicable CR identifiers]` | `[Enforcement Context schema]` | `[IF-001 operation(s)]` | `[applicable registry entries]` | `[PEP and bypass TCs]` | `ADR-PEP-001` | `profiles/...`, `src/pep/...`, `conformance/profile/pep/...` |

The architectural rationale should explain why the mapping is semantically correct, not merely state `complete coverage`.

### C.22 Recommended completion and approval sequence

Complete and review the profile in this order:

1. **Identify the baseline.** Record the exact bundle, version, date, manifest, and digest.
2. **Resolve classification.** Mark each entry as fixed, selected, deployment-controlled, ADR-controlled, or a repository correction.
3. **Define conformance posture.** State the target and current claim separately.
4. **Define the enforcement boundary.** Complete the scope and non-bypassability statement before making detailed service decisions.
5. **Map mandatory capabilities.** Identify applicable CR, NS, interface, schema, registry, and test relationships.
6. **Complete stable profile selections.** Identity, cryptography, ingress trust boundary, persistence, Canonical State, PEM, concurrency, and error behavior.
7. **Route mutable values.** Create or identify deployment overlays and runbooks in the implementation build/deploy repository; do not place them in the profile package.
8. **Create required ADRs or IDRs.** Do not leave major architecture decisions embedded only as unexplained profile fields.
9. **Resolve repository dependencies.** Block affected structures or claims until objective defects are corrected.
10. **Define verification.** Every decision must have an observable acceptance method and evidence location.
11. **Update traceability.** Add or revise RTM records and validate identifiers and relationships.
12. **Perform reviews.** Architecture, security, traceability, interface, schema, registry, conformance, and operations reviews as applicable.
13. **Remove authoring material.** Delete placeholders, unused alternatives, and normally Appendix C.
14. **Approve and hash.** Approve the final content, calculate the digest, update metadata and inventories, and publish immutable artifacts.

### C.23 Distinguishing AGCP-controlled and illustrative values

The following distinctions apply to every informational example produced from this template.

| Value | Treatment in an informational example |
|---|---|
| `AGCP v2.0.0` | Real AGCP-connected value; classify as `AGCP_CONTROLLED`. |
| `CR-001` through `CR-122` | Real AGCP identifiers; classify as `AGCP_CONTROLLED`. |
| ARM, NS, DS, IF, REG, and TC identifiers copied from the controlled baseline | Real AGCP identifiers; classify as `AGCP_CONTROLLED`. |
| Public AGCP base path `/agcp/v2` | Real AGCP-connected interface value; classify as `AGCP_CONTROLLED`. |
| Metadata path `GET /agcp/v2/meta` | Real AGCP-connected interface value; classify as `AGCP_CONTROLLED`. |
| `agcp-rs` or any other implementation/product name | Illustrative unless it identifies a real controlled implementation; classify as `ILLUSTRATIVE_EXAMPLE` in an example profile. |
| AWS, Azure, Google Cloud, Kubernetes services, managed databases, KMS/HSM products, identity providers, WAFs, or DDoS services | Illustrative technology examples unless actually adopted; classify as `ILLUSTRATIVE_EXAMPLE` in an example profile. |
| Hostnames, origins, IP addresses, CIDR blocks, accounts, regions, zones, clusters, and tenant counts | Illustrative or external deployment values. Use reserved `.example` domains and documentation-only address ranges in an informational example. |
| CPU, memory, fuel, timeout, replica, connection, cache, rate-limit, quota, capacity, SLO, RTO, RPO, and retention values | Illustrative in an example profile and externally controlled in a real deployment unless a specific value is required for interoperability or conformance. |
| Final profile, baseline, release, or artifact digest | `COMPUTED_ARTIFACT_VALUE`; never invent it. |

An example profile may be complete as an example while remaining non-operational. Completeness means that every field has a classified, coherent, and testable example value; it does not convert illustrative values into real deployment facts.

### C.24 Common failure patterns

| Inadequate entry | Why it is inadequate | Acceptable direction |
|---|---|---|
| `Database: PostgreSQL` | Does not define authority, tenancy, transaction, ordering, recovery, or verification. | Identify topology, isolation, transaction boundary, sequence allocation, replay behavior, ADR, and tests. |
| `mTLS: Yes` | Does not state where it applies, identity semantics, trust anchors, or failure behavior. | Define which internal calls require mTLS, certificate identity mapping, rotation, validation, and overlay references. |
| `Retention: 24 hours` | Does not identify the record class or whether the value is stable or mutable. | State the rule separately for idempotency, nonces, approval replay, evidence, ledger, logs, and telemetry. |
| `Unknown fields ignored` | May conflict with strict schemas or weaken controlled behavior. | Identify the governing schema rule and whether rejection is required for each interface object. |
| `Conformance: L5` | Confuses target scope with verified status. | State `L5 target; Not Claimed` until evidence and approval exist. |
| `All execution is non-bypassable` | May exceed the actual technical enforcement boundary. | Identify the exact owner-controlled executor paths and explicitly exclude external paths. |
| `Use the latest spec` | Creates a moving and irreproducible normative baseline. | Record the exact baseline version, bundle name, digest, and migration rule. |
| `WASM policy engine` | Does not define an interoperable machine contract. | Reference a controlled IF-002 profile containing ABI, envelopes, imports, resource behavior, traps, digest, and activation semantics. |
| `See code` | Code alone does not provide controlled rationale or stable traceability. | Reference the code mapping plus the governing source, decision record, verification method, and evidence. |

