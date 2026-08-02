# AGCP Full-Scope Multitenant Training and Client Demonstration Implementation Profile - Informational Example

Status: Informational Example (Non-Normative; Not an Operational Deployment)

Profile Version: 1.3.0

Base Template Version: 1.1.0

## 1. Purpose

This informational example shows how a completed Implementation Profile could define a full-scope AGCP implementation for an Internet-exposed, multitenant service used for:

- separate instructor-led training classes;
- separate client demonstrations and evaluation sessions;
- internal assurance, integration, and acceptance testing; and
- controlled demonstrations of all AGCP capability groups.

Each training class and each client demonstration is assigned a separate tenant. Every tenant supports multiple human users and service principals. The profile prioritizes security, tenant isolation, deterministic behavior, evidence integrity, and truthful conformance claims over convenience, cost, or implementation simplicity.

This document is not a controlling profile, deployment authorization, conformance claim, or representation of an existing service. It is a completed informational example. AGCP-specific requirements, identifiers, concepts, interface versions, and baseline references are drawn from the controlled AGCP source materials identified in this document. The implementation name `agcp-rs`; every AWS platform, service, region, account, and configuration selection; every hostname, domain, IP address, CIDR block, repository, container registry, resource limit, capacity, timeout, retention period, SLO, RTO/RPO value, date, role, approval, and other implementation- or deployment-specific value is illustrative unless expressly labeled `AGCP-CONTROLLED`.

## 2. Profile Interpretation

### 2.1 Value provenance and example status

This profile uses three value-provenance labels:

- **`AGCP-CONTROLLED`** - A real AGCP identifier, title, requirement range, architectural concept, normative statement reference, interface reference, registry reference, test reference, or baseline value taken from the controlled AGCP source materials. These values are not invented for the example.
- **`ILLUSTRATIVE`** - A concrete example implementation or deployment selection supplied to show how a completed profile should read. These values do not describe a live service and do not imply that the named endpoint, account, repository, cloud resource, identity tenant, key, approval, or operating process exists.
- **`PROPOSED-EXAMPLE`** - A profile-specific identifier or companion artifact used to illustrate what an implementation would create. It is not part of the AGCP controlled baseline unless and until separately approved and published through the AGCP specification-governance process.

Unless a value is expressly labeled `AGCP-CONTROLLED`, all implementation-specific and deployment-specific values in this document shall be interpreted as `ILLUSTRATIVE`. Reserved `.example` domain names and documentation-only private network values are used to prevent endpoint and network examples from being mistaken for deployed services.

The following are real AGCP-connected values in this example: AGCP v2.0.0, the 2026-07-30 Public Review Controlled Baseline designation, CR-001 through CR-122, the cited ARM and NS identifiers, the AGCP architectural and normative concepts, the controlled AGCP artifact names cited from the source materials, and the public interface version/path `/agcp/v2`. The example hostname combined with that path remains illustrative.

The implementation name `agcp-rs`, the service name `AGCP-DTS`, all AWS and third-party services, all resource and capacity values, all IP addresses and CIDR blocks, and all build/deployment repository paths are `ILLUSTRATIVE`. Profile-specific identifiers such as `AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0`, `ADR-PROF-*`, `RTM-2.0.0-PROFILE-EXT-1.0.0`, and `IF-002-AGCP-WASM-PEC-1.0.0` are `PROPOSED-EXAMPLE` identifiers unless an authoritative AGCP repository later publishes them.

### 2.2 Security posture

For this profile, maximum security means the strongest practical security posture supported by the selected architecture and operational model, including:

- fail-closed governance and security decisions;
- phishing-resistant multifactor authentication for all human users;
- short-lived asymmetric credentials;
- strict server-side tenant binding;
- no cross-tenant resource discovery or authority transfer;
- private, non-Internet-exposed management functions;
- TLS 1.3 on public connections and mutual TLS on internal service connections;
- per-tenant data isolation and encryption keys;
- hardware-backed key management for platform signing and encryption keys;
- immutable, integrity-protected Governance Evidence and release evidence;
- signed and content-addressed policy, schema, configuration, and release artifacts;
- least privilege, separation of duties, and dual authorization for high-impact administrative actions;
- continuous vulnerability, integrity, and configuration monitoring; and
- mandatory security review before external use.

No profile can guarantee absolute security. The phrase maximum security in this document means that security controls take precedence over operational convenience within the defined implementation and deployment scope.

### 2.3 Decision classification

This profile uses the following classifications:

- `FIXED_NORMATIVE_OBLIGATION`
- `PROFILE_SELECTION`
- `DEPLOYMENT_CONFIGURATION`
- `ADR_IDR_REQUIRED`
- `REPOSITORY_CORRECTION`

### 2.4 Profile authority

An adopted implementation profile would be lower precedence than the controlled AGCP Runtime Governance Conformance Requirements, AGCP Core Specification, and applicable normative companion specifications. If any statement in this profile conflicts with a higher-precedence source, the higher-precedence source governs and the conflict shall be treated as a profile defect or repository correction.

### 2.5 Repository boundary

The Implementation Profile and its optional machine-readable representation belong with the AGCP profile or specification artifacts. Build, deployment, and operations artifacts belong in the implementation build/deploy repository, not in the AGCP profile package. Accordingly:

- `deploy/` contains infrastructure as code, Helm or Kubernetes manifests, deployment overlays, network configuration, tenant-capacity configuration, and environment-specific resource values;
- `<build-deploy-repo>/runbooks/` contains operational, incident-response, key-management, backup, restoration, and disaster-recovery procedures;
- those directories are referenced by this example but are not packaged with it; and
- every path shown for those external artifacts is illustrative until a real build/deploy repository is created.

## 3. Profile Control Record

| Field | Profile value |
|---|---|
| Profile ID | `AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0` (`PROPOSED-EXAMPLE`) |
| Profile Name | AGCP Full-Scope Multitenant Training and Client Demonstration Profile - Informational Example |
| Profile Version | `1.3.0` |
| Repository Path | `profiles/examples/full-scope-multitenant-demo/AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0.md` (`ILLUSTRATIVE`) |
| Public Profile URI | `https://api.demo.agcp.example/agcp/v2/profiles/AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0` (hostname `ILLUSTRATIVE`; `/agcp/v2` is `AGCP-CONTROLLED`) |
| Profile SHA-256 Digest | The package includes a digest of this informational example for file-integrity checking only. It is not a release or conformance digest. |
| Publication Status | Informational Example - Non-Normative |
| Artifact Lifecycle State | Example |
| Profile Owner | Not assigned; illustrative role only |
| Technical Owner | Not assigned; illustrative role only |
| Approval Authority | Not applicable; this example is not approved for implementation or deployment |
| Approval Date | Not applicable |
| Effective Date | Not applicable |
| Review Date | Not applicable to the example; an adopted profile would define a controlled review date |
| Supersedes | None; revision history records the evolution of the example |
| Superseded By | None |

## 4. Implementation Identification

| Field | Profile value |
|---|---|
| Implementation Name | Example AGCP Full-Scope Training and Demonstration Service (`AGCP-DTS`) (`ILLUSTRATIVE`) |
| Implementing Organization | Example Operator Organization (`ILLUSTRATIVE`; not a real deployment operator) |
| Private Source Repository | `https://git.example/example-operator/agcp-rs` (`ILLUSTRATIVE`) |
| Initial Implementation Release | `agcp-rs v0.1.0` (`ILLUSTRATIVE`) |
| Release Tag Convention | `agcp-dts-v<semver>` (`ILLUSTRATIVE`) |
| Container Registry | `registry.example/example-operator/agcp-rs` (`ILLUSTRATIVE`) |
| Implementation Class | Illustrative production-capable training, demonstration, assurance, and reference implementation; pre-conformance until release evidence passes all applicable tests (`ILLUSTRATIVE`) |
| Primary Implementation Language | Rust, Edition 2024, stable toolchain pinned by `rust-toolchain.toml` and the signed release manifest (`ILLUSTRATIVE`) |
| Policy Source Language | Rego subset compiled into deterministic WebAssembly (`ILLUSTRATIVE`); direct WASM modules are an example option contingent on a separately published machine contract |
| Principal Runtime | AWS Elastic Kubernetes Service in private subnets, hardened Bottlerocket worker nodes, deterministic Wasmtime sandbox, and Amazon Aurora PostgreSQL-compatible version 16 (`ILLUSTRATIVE`) |
| Primary Region | AWS `us-east-1` (`ILLUSTRATIVE`) |
| Disaster-Recovery Region | AWS `us-west-2` (`ILLUSTRATIVE`) |
| Availability Zones | Three independent availability zones in each active region (`ILLUSTRATIVE`) |
| Deployment Environment | Internet-exposed authenticated public API with a private management plane, private Kubernetes control plane, and isolated tenant data domains (`ILLUSTRATIVE`) |
| Primary Architect | Example Chief Systems Architect role (`ILLUSTRATIVE`) |
| Security Authority | Example independent Security Authority role (`ILLUSTRATIVE`) |
| Operations Authority | Example Platform Operations Authority role (`ILLUSTRATIVE`) |

## 5. Controlled Baseline

### 5.1 Base AGCP release

| Field | Profile value |
|---|---|
| AGCP Specification Version | AGCP v2.0.0 Public Review Controlled Baseline (`AGCP-CONTROLLED`); Section 29 separately records repository findings supplied with this example |
| Publication Maturity | Public Review - Controlled Baseline (`AGCP-CONTROLLED`) |
| Controlled Baseline Date | 2026-07-30 (`AGCP-CONTROLLED`) |
| Baseline Bundle Name | `agcp-spec-v2.0.0-public-review-controlled-baseline.zip` (`ILLUSTRATIVE` filename for the controlled baseline) |
| Baseline Repository Location | `vendor/agcp-spec/2.0.0/` in the illustrative `agcp-rs` implementation repository (`ILLUSTRATIVE`) |
| Baseline Lock Record | `vendor/agcp-spec/2.0.0/baseline.lock.json` (`ILLUSTRATIVE`) |
| Baseline SHA-256 Binding | The exact bundle digest is recorded in `baseline.lock.json` and the signed release manifest. Build, startup, metadata generation, and conformance tooling fail closed if the digest is absent or mismatched. |
| Supported Baseline Count | One active AGCP baseline per deployed release |
| Baseline Migration Rule | No deployment follows a moving branch. Every change requires a new vendor directory, impact analysis, profile compatibility review, RTM review, full regression, signed migration approval, and new release manifest. |

### 5.2 Adopted controlled artifacts

| Artifact class | Identifier and version | Repository binding | Digest authority | Lifecycle state | Applicability |
|---|---|---|---|---|---|
| AGCP Core Specification | AGCP Core v2.0.0 | `baseline.lock.json` logical artifact entry `core` | Signed release manifest | Current | Mandatory |
| Architecture Reference Model | AGCP ARM v2.0.0 | `baseline.lock.json` entry `arm` | Signed release manifest | Current | Mandatory architectural vocabulary |
| Normative Statements | AGCP Normative Statements v2.0.0 | `baseline.lock.json` entry `normative_statements` | Signed release manifest | Current | Mandatory traceability source |
| Conformance Requirements | CR-001 through CR-122 (`AGCP-CONTROLLED`) | `baseline.lock.json` entry `conformance_requirements` | Signed release manifest | Current | All applicable |
| Requirements Traceability Matrix | RTM dataset applicable to v2.0.0 plus this profile extension | `traceability/rtm/` | Signed release manifest | Current after profile synchronization | Mandatory |
| Schema Catalog | Corrected v2.0.0 catalog | `baseline.lock.json` entry `schema_catalog` | Signed release manifest | Current after Section 29 corrections | Mandatory |
| Registry Catalog | Corrected v2.0.0 catalog | `baseline.lock.json` entry `registry_catalog` | Signed release manifest | Current after Section 29 corrections | Mandatory |
| Interface Specification | IF-001 v2.0.0 (`AGCP-CONTROLLED`) | Controlled baseline location | Controlled baseline integrity record | Current | Mandatory where applicable |
| Proposed profile companion | IF-002-AGCP-WASM-PEC-1.0.0 (`PROPOSED-EXAMPLE`) | `interfaces/if-002-wasm-pec/` (`ILLUSTRATIVE`) | Example signed release manifest | Not published | Required only if an adopted profile enables independently authored WASM modules |
| OpenAPI Contract | Corrected IF-001 OpenAPI v2.0.0 | `openapi/agcp-if-001-v2.0.0.yaml` | Signed release manifest | Current after Section 29 corrections | Mandatory |
| Conformance Test Suite | TC-001 through TC-122 plus profile extension 1.0.0 | `tests/conformance/` and `tests/profile/full-scope-multitenant-demo/` | Signed release manifest | Current | Mandatory |
| Assessment Procedures | Applicable AGCP assessment procedures | `assessment/` | Signed release manifest | Current | Mandatory for claims |
| Companion Specifications | Provenance, multitenancy, ledger, human review, implementation metadata, and profile-adopted companions | `baseline.lock.json` and `interfaces/` | Signed release manifest | Current after corrections | As mapped by RTM |

### 5.3 Artifact source and pinning

- **Authoritative artifact source:** The immutable vendored AGCP release bundle and its `baseline.lock.json`; embedded copies in binaries are read-only convenience copies and shall match the lock record.
- **Pinning strategy:** SHA-256 content digests plus exact specification version and source revision. Semantic version alone is insufficient.
- **Unknown-field policy:** Reject unknown fields unless the exact adopted schema expressly permits them.
- **Schema evolution policy:** No silent forward compatibility. New fields, enums, or semantics require a new controlled baseline or explicitly compatible profile revision.
- **Multiple-version support:** A running deployment serves one AGCP baseline and one profile version. Blue/green releases may coexist at infrastructure level, but a single tenant evaluation horizon never mixes semantic versions.

## 6. Conformance Posture

### 6.1 Conformance target

| Field | Profile value |
|---|---|
| Target Conformance Level | Full applicable AGCP capability scope, including the cumulative Level 1 through Level 5 capability set |
| Current Conformance Claim Status | `NOT_CLAIMED`; `agcp-rs v0.1.0` is an `ILLUSTRATIVE` implementation/release label and no claim evidence exists |
| Intended Claim Scope | AGCP-DTS public IF-001 surface, governance runtime, tenant persistence, Canonical State adapters, management-controlled activation, and owner-controlled PEP/executor paths |
| Excluded Claim Scope | Arbitrary client devices, student-owned code, customer systems not integrated through an owner-controlled adapter, and third-party actions initiated outside AGCP-DTS |
| Verification Threshold | 100 percent pass of all applicable official and profile-specific mandatory tests; no sampling |
| Conformance Claim Record | `release-evidence/<release>/conformance-claim.json`, created and signed only after the threshold is satisfied |
| Claim Signing Authority | Hardware-backed release key under dual authorization by the Release Manager and Security Authority |

### 6.2 Conformance statement

> This informational example illustrates an implementation targeting AGCP v2.0.0 under the proposed example profile identifier AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0. It is not implemented, approved, deployed, or conformant. A real AGCP conformance claim would require the exact implementation release, AGCP baseline digest, adopted profile digest, interface versions, schema and registry catalog digests, and objective evidence in a signed release-specific conformance claim record.

### 6.3 Objective evidence

Every conformance claim shall include:

- exact source commit and signed release tag;
- release manifest, SBOM, build provenance, and binary/image digests;
- baseline lock record and profile detached digest;
- schema, registry, OpenAPI, and interface validation reports;
- TC-001 through TC-122 results for every applicable test;
- profile-specific security, tenant-isolation, deterministic replay, concurrency, crash-recovery, and PEP-bypass test results;
- RTM validation and profile-extension mappings;
- signed metadata document; and
- approval records identified in Section 33.

## 7. Claimed Enforcement Scope

### 7.1 Enforcement boundary

- **Classification:** `ADR_IDR_REQUIRED`.
- **Claimed enforcement scope:** All governed actions submitted through the public AGCP endpoint and all owner-controlled execution adapters capable of producing a governed consequence for training, client demonstration, and internal assurance tenants.
- **Governed consequence classes within scope:** State mutation, service invocation, external API call, controlled file or object creation, workflow transition, approval-dependent action, policy/configuration activation, tenant lifecycle action, and profile-approved simulated physical or cyber action.
- **Owner-controlled services within scope:** API gateway integration, public governance service, governance decision service, Canonical State resolver, governance realization service, PEP/executor, tenant-specific action adapters, ledger/evidence service, approval service, re-evaluation service, and outbox dispatcher.
- **Governance runtime components within scope:** Proposal qualification, policy evaluation, authorization, authority re-derivation, binding validation, resulting-state validation, deterministic adjudication, Commit Boundary processing, Structural Refusal, and evidence production.
- **Persistence components within scope:** Platform control database, tenant databases, per-tenant ledger, idempotency store, approval store, outbox, immutable evidence archive, and signed release/configuration registry.
- **Policy Enforcement Point or executor within scope:** Owner-controlled PEP immediately adjacent to each execution adapter. The PEP is the only component permitted to invoke the governed adapter.
- **Commit Boundary placement:** Within the same transactional or cryptographically bound realization path that validates current governance conditions and issues the adapter-specific execution permit immediately before the governed consequence.
- **External systems within scope:** Only external services reached through owner-controlled adapters that require a current, single-use, proposal-bound execution permit.
- **External systems explicitly outside scope:** Arbitrary client devices, student-owned code, customer systems not integrated through an owner-controlled adapter, and third-party actions initiated outside the service.
- **Execution paths explicitly excluded from the non-bypassability claim:** Actions performed directly by external users or external systems without using the owner-controlled PEP/executor; administrative actions on external identity providers; underlying cloud-provider operations not mediated by an AGCP adapter.
- **Decision record:** `ADR-PROF-001 Enforcement Boundary and PEP Placement`.
- **Verification method:** Architecture review; network and call-graph analysis; adapter credential isolation; negative bypass testing; attempt to invoke adapters without a valid execution permit; review of cloud IAM and network policies.
- **Rationale:** A truthful claim must be limited to paths that the implementation can technically mediate.

### 7.2 Non-bypassability statement

> Every governed consequence included in this profile shall be produced only by an owner-controlled execution adapter invoked through the applicable PEP using a current, integrity-protected, proposal-specific, tenant-specific, target-specific, single-use execution permit created by Governance Realization immediately before commitment. Direct invocation credentials shall not be available to public clients, tenant users, policy modules, or governance-decision components. Actions initiated outside these owner-controlled paths are outside the non-bypassability claim.

### 7.3 Explicit non-goals

| Non-goal | Rationale | Effect on conformance claim |
|---|---|---|
| Control arbitrary code running on student or client devices | The operator does not control those execution environments. | Excluded from enforcement scope. |
| Permit cross-tenant authority or resource sharing | Training and client isolation has priority over convenience. | Cross-domain isolation is supported; transfer is prohibited. |
| Operate as a customer production control plane without a separate customer-specific profile and assessment | Client demos are not equivalent to production integration. | No customer production conformance claim. |
| Store unrestricted real customer secrets or regulated production data in demo tenants | Reduces exposure and legal risk. | Synthetic or approved sanitized data only unless separately authorized. |
| Expose public administrative mutation endpoints | Internet exposure materially increases risk. | Management plane is private and outside IF-001. |

## 8. Capability and Applicability Profile

| Capability or requirement group | Applicability | Controlling source | Implementation mapping | Verification evidence |
|---|---|---|---|---|
| Proposal Qualification | Mandatory / Supported | Core, NS, applicable CRs | Strict parsing, schema, asserted formats, identity, provenance, context, and binding qualification | Official tests, negative fixtures, qualification evidence |
| Governance Decision Function | Mandatory / Supported | Core, NS, applicable CRs | Deterministic WASM policy evaluation over qualified inputs | Official tests, cross-platform vectors, replay evidence |
| Execution Authorization | Mandatory / Supported | Core, NS, applicable CRs | Immutable authorization outcome subject to commit-time re-derivation | Official tests and lifecycle evidence |
| Governance Realization and Commit Boundary | Mandatory / Supported | Core, NS, applicable CRs | Transactionally bound realization plus owner-controlled PEP/executor | PEP bypass tests and commit evidence |
| Governance Evidence | Mandatory / Supported | Core, NS, ledger companion | Per-tenant append-only ledger, signed evidence export, immutable archive | Ledger validation, export verification, replay |
| Canonical State Resolution and Qualification | Mandatory / Supported | Core, ARM, applicable CRs | Qualified adapters, immutable snapshots, deterministic precedence, fail closed | Conflict, stale-source, and outage tests |
| Authority Re-Derivation | Mandatory / Supported | Core, ARM, applicable CRs | Re-derived at commit from current tenant, subject, delegation, approval, revocation, and policy state | Revocation and expiry tests |
| Governance Binding Validation | Mandatory / Supported | Core, ARM, applicable CRs | Proposal, tenant, target, evidence, policy, state, scope, and lifecycle binding | Mismatch fixtures and negative tests |
| Tenant and Governance Domain Isolation | Mandatory / Supported | Core, multitenant companion | Dedicated tenant database, tenant-specific keys, server-side binding, network and application isolation | Tenant isolation and cross-tenant disclosure tests |
| Delegation and Authority Lineage | Mandatory / Supported | Core, applicable CRs | Typed delegation records, bounded depth, revocation propagation, complete lineage | Lineage and revocation tests |
| Human Review and Approval Artifacts | Mandatory / Supported | Core, human review companion | Submission-to-artifact qualification, FIDO2-authenticated approvers, partial quorum | Quorum, eligibility, replay, and binding tests |
| Continuation Integrity | Mandatory / Supported | Core, ARM, applicable CRs | Nonterminal proposal monitoring, expiry, cancellation, degradation, dependency checks | Lifecycle and continuation tests |
| Risk-Based Re-Evaluation | Mandatory / Supported | Core, CR-122 | Typed change events, dependency graph, deterministic affected-proposal traversal | TC-122 and profile extension |
| Composite Proposal Governance | Mandatory / Supported | Core, ARM, applicable CRs | Bind sets, dependency graphs, coupling semantics, resulting-state validation | Composite and partial-bind tests |
| Cross-Domain Authority Isolation | Mandatory / Supported | Core, applicable CRs | Cross-tenant and cross-domain authority transfer prohibited | Negative transfer tests |
| Governance Self-Protection | Mandatory / Supported | Core, applicable CRs | Private management plane, dual control, signed config, protected keys, tamper detection | Management and tamper tests |
| Autonomous Coordination | Mandatory / Supported | Core, applicable CRs | Bounded coordinator proposals, no direct execution authority, deterministic adjudication | Coordination and conflict tests |
| Tenant-class lifecycle automation | Profile-specific / Supported | This profile | Class and demo tenant templates, scheduled expiry, archival, and secure reset | Tenant lifecycle tests |

## 9. Runtime Architecture and Service Boundaries

> **Value classification:** All technologies, products, topology, service names, repository paths, and deployment choices in this section are `ILLUSTRATIVE`.

### 9.1 Deployment mode

- **Classification:** `PROFILE_SELECTION`.
- **Single-tenant, multi-tenant, or both:** Multitenant service; each logical tenant is isolated and may have multiple users and service principals.
- **Tenant isolation boundary:** Dedicated tenant database, dedicated database role, dedicated encryption data key, tenant-specific ledger chain, tenant-specific object-storage prefix protected by policy, tenant-specific policy/configuration namespace, and exact tenant binding in every request and record.
- **Governance-domain isolation boundary:** One governance domain per tenant. Cross-domain authority transfer is prohibited.
- **Tenant classes:** `TRAINING_CLASS`, `CLIENT_DEMO`, and `INTERNAL_ASSURANCE`.
- **Multiple-user requirement:** Every tenant supports at least one tenant administrator and multiple concurrent users. There is no single-user tenant mode.
- **Verification method:** Tenant-provisioning tests; cross-tenant access attempts; database role and key inspection; object-store policy tests; concurrent multi-user tests.
- **Rationale:** Separate tenants prevent one class or client demo from observing or affecting another.

### 9.2 Service decomposition

- **Classification:** `ADR_IDR_REQUIRED`.
- **Single-process, multi-process, or distributed model:** Distributed services with minimal privilege and narrowly defined interfaces.
- **Public governance service:** Stateless Rust service behind an API gateway and WAF.
- **Governance decision component:** Isolated Rust service hosting the deterministic WASM runtime; no direct Internet exposure.
- **Governance realization component:** Rust service that performs current-state revalidation, binding validation, commit-time authorization, and PEP coordination.
- **Policy Enforcement Point or executor:** Separate privileged service with exclusive credentials to governed adapters.
- **Ledger component:** Append-only per-tenant ledger writer with exclusive write authority.
- **Canonical State adapters:** Read-only or narrowly scoped adapters to tenant, identity, entitlement, policy, configuration, key, and ledger sources.
- **Private management plane:** Separate service accessible only through a private network, device-bound identity, mTLS, and phishing-resistant MFA.
- **Operations interface:** Tenant-scoped read-only `/ops/v1` service; no direct Canonical State mutation.
- **Background workers:** Re-evaluation, evidence archival, outbox dispatch, tenant expiry, backup verification, and integrity monitoring workers.
- **Decision record:** `ADR-PROF-002 Service and Trust-Boundary Decomposition`.
- **Verification method:** Network-policy review, service-account review, credential-path analysis, interface tests, and privilege escalation tests.
- **Rationale:** Separation limits blast radius and prevents public or policy-evaluation components from directly executing actions.

### 9.3 Development and production relationship

- **Classification:** `PROFILE_SELECTION` and `DEPLOYMENT_CONFIGURATION`.
- **Base profile shared across environments:** Yes. Governance semantics, authentication requirements, tenant isolation, cryptographic verification, evidence generation, and fail-closed behavior are identical.
- **Development overlay:** `<build-deploy-repo>/deploy/overlays/development.yaml` (`ILLUSTRATIVE` external reference).
- **Test overlay:** `<build-deploy-repo>/deploy/overlays/test.yaml` (`ILLUSTRATIVE` external reference).
- **Staging overlay:** `<build-deploy-repo>/deploy/overlays/staging.yaml` (`ILLUSTRATIVE` external reference).
- **Production overlay:** `<build-deploy-repo>/deploy/overlays/production.yaml` (`ILLUSTRATIVE` external reference).
- **Development public hostname:** `api.dev.demo.agcp.example` (`ILLUSTRATIVE`).
- **Test public hostname:** `api.test.demo.agcp.example` (`ILLUSTRATIVE`).
- **Staging public hostname:** `api.staging.demo.agcp.example` (`ILLUSTRATIVE`).
- **Production public hostname:** `api.demo.agcp.example` (`ILLUSTRATIVE`).
- **Environment-specific deviations permitted:** Capacity, replica counts, rate limits within profile bounds, telemetry destinations, hostnames, and shortened retention in local development only.
- **Environment-specific deviations prohibited:** Disabling authentication, WebAuthn MFA, tenant binding, mTLS, evidence generation, signature verification, Commit Boundary checks, fail-closed behavior, signed artifact verification, or profile-required tests.
- **Promotion rule:** The same signed image and artifact digests are promoted from staging to production; production rebuilds are prohibited.
- **Verification method:** Overlay schema validation, policy-as-code checks, and signed promotion record.
- **Rationale:** Environment convenience shall not create a weaker governance model.

### 9.4 Stack constraints

- **Classification:** `PROFILE_SELECTION`.
- **Cloud platform:** AWS commercial partition.
- **Edge and DDoS controls:** Amazon Route 53, CloudFront, AWS WAF, and AWS Shield Advanced.
- **Container platform:** Amazon EKS with private-only Kubernetes API endpoint, three availability zones, Bottlerocket worker nodes, no SSH, and signed image admission.
- **Service mesh and workload identity:** Istio in strict mTLS mode; workload certificates issued from AWS Private CA with 24-hour validity and automatic rotation at 12 hours.
- **Persistence:** One Aurora PostgreSQL-compatible version 16 cluster per tenant, plus a separate platform-control cluster; serializable transactions are mandatory.
- **Immutable evidence archive:** One S3 bucket per tenant with Object Lock Compliance mode, versioning, cross-region replication, and a dedicated KMS key.
- **Key and secret services:** AWS KMS asymmetric keys, AWS CloudHSM-backed custom key store for release/metadata signing, and AWS Secrets Manager for non-key secrets.
- **Identity broker:** Auth0 Enterprise with custom domain `auth.demo.agcp.example`; one Auth0 Organization per AGCP tenant. A separate administrative identity tenant uses `auth-admin.demo.agcp.example`.
- **Telemetry:** OpenTelemetry Collector to CloudWatch Logs/Metrics, Amazon OpenSearch Service for protected audit search, GuardDuty, Security Hub, and immutable S3 log archive.
- **Required language/runtime constraints:** Memory-safe Rust; maintained cryptographic libraries; Wasmtime sandbox; PostgreSQL; OpenTelemetry.
- **Prohibited implementation patterns:** Custom cryptographic primitives, unpinned dependencies, runtime code download, shell execution in request paths, unsafe deserialization, shared tenant credentials, privileged containers, public node IPs, and direct database access by public clients.
- **Rust unsafe-code rule:** `#![forbid(unsafe_code)]` for public API, governance decision, authorization, realization, and ledger crates. Any exception requires a separate security-reviewed crate and ADR.
- **Operating-system controls:** Read-only root filesystem, non-root UID, seccomp `RuntimeDefault`, AppArmor, dropped Linux capabilities, default-deny egress, and no package manager or shell in production images.
- **Compliance posture:** FIPS certification and FedRAMP authorization are not claimed. The architecture uses managed hardware-backed keys and strong modern cryptography; a future FIPS-specific profile may substitute approved algorithms and providers.
- **Verification method:** IaC policy tests, image scan, admission test, dependency audit, runtime inspection, and external origin-reachability test.
- **Rationale:** A specific, hardened platform removes ambiguity from the implementation profile.

## 10. Interface Profile

> **Value classification:** `/agcp/v2` is the real AGCP-connected public interface version/path used by this profile. Hostnames, domains, internal protocols, management paths, and operations paths are `ILLUSTRATIVE` unless expressly marked otherwise.

### 10.1 Public AGCP interface adoption

- **Classification:** `FIXED_NORMATIVE_OBLIGATION` where required by IF-001.
- **Adopted interface identifier and version:** IF-001 v2.0.0 corrected binding.
- **Public base URI:** `https://api.demo.agcp.example/agcp/v2` (hostname `ILLUSTRATIVE`; `/agcp/v2` `AGCP-CONTROLLED`).
- **Required operations:** All mandatory IF-001 operations plus read-only status retrieval required for Pending Human Review, Deferred, and governed re-evaluation workflows.
- **Required request and response schemas:** Exact corrected v2.0.0 schema catalog entries identified in the signed release manifest.
- **Required `Idempotency-Key` behavior:** Required on every state-creating or state-transitioning operation designated by IF-001; enforced as described in Section 15.
- **Required implementation metadata operation and path:** `GET /agcp/v2/meta` (`AGCP-CONTROLLED` public interface version/path).
- **Required error model:** Controlled public error envelope; no stack traces, database identifiers, tenant-specific existence information, or internal policy details.
- **Synchronous or asynchronous behavior permitted by the adopted interface:** The public conformance surface is synchronous for submission and authoritative outcome production. Pending Human Review and Deferred are authoritative governance outcomes, not transient asynchronous implementation states.
- **Verification method:** OpenAPI validation, contract tests, negative tests, idempotency tests, and metadata continuity tests.
- **Evidence location:** Signed interface conformance results and per-request Governance Evidence.

### 10.2 Internal RPC and transport

- **Classification:** `PROFILE_SELECTION`.
- **Internal RPC protocol:** gRPC over HTTP/2 or HTTP/3 where supported and approved.
- **Serialization format:** Protobuf for internal transport; canonical JSON/JCS only at defined signature and evidence boundaries.
- **Remote-call authentication:** Workload identity with short-lived certificates issued by the platform trust domain.
- **Remote-call encryption:** Mandatory TLS 1.3.
- **mTLS requirement:** Mandatory for every service-to-service connection.
- **Host-isolation reliance:** Host isolation is defense in depth and shall not replace mTLS, authentication, or authorization.
- **Retry behavior:** Only idempotent internal operations may be automatically retried. Retry inputs and outcome identity shall be preserved.
- **Timeout governance:** Bounded, overlay-controlled timeouts; timeout shall not be interpreted as authorization or success.
- **Deployment-overlay references:** `<build-deploy-repo>/deploy/overlays/*` and `<build-deploy-repo>/runbooks/network-security.md`.
- **Verification method:** Certificate-rotation tests, service identity tests, network capture, and denied plaintext connection tests.
- **Rationale:** Internet exposure requires zero-trust treatment of internal networks.

### 10.3 Private management plane

- **Classification:** `ADR_IDR_REQUIRED`.
- **Management-plane URI and boundary:** `https://mgmt.demo.agcp.example/mgmt/v1`, resolvable only inside the management VPC. Access requires AWS Verified Access, a managed device, FIDO2 authentication through `auth-admin.demo.agcp.example`, and client-certificate mTLS.
- **Authorized operator classes:** Platform Security Administrator, Platform Operations Administrator, Specification Release Manager, and Tenant Provisioning Administrator. High-impact functions require two distinct authorized persons.
- **Tenant management functions:** Create, configure, suspend, reactivate, expire, archive, and destroy tenant metadata subject to retention rules.
- **Principal management functions:** Invite, bind, suspend, revoke, and remove tenant memberships; platform operators cannot impersonate tenant users.
- **Key-management functions:** Register, rotate, revoke, and recover platform or tenant keys through KMS/HSM workflows.
- **Configuration-management functions:** Validate, sign, stage, activate, and roll back immutable configuration bundles.
- **Governance compilation functions:** Submit, validate, compile, sign, and stage policy modules.
- **Activation and rollback functions:** Atomic activation by digest with dual authorization; rollback only to a previously approved artifact set.
- **Suspension functions:** Immediate tenant, user, service principal, key, policy, adapter, or global service suspension.
- **Quota-management functions:** Configure profile-bounded tenant quotas in deployment overlays.
- **Export functions:** Authorized evidence and tenant export with approval, encryption, and audit.
- **Separation from the public conformance interface:** Separate service, DNS name, network route, identity audience, authorization model, and deployment account.
- **Canonical State mutation authority:** Only specific management commands may propose mutations. Mutations themselves are governed, attributable, evidence-producing, and subject to dual control where high impact.
- **Decision record:** `ADR-PROF-003 Private Management Plane and Dual Control`.
- **Verification method:** External network tests, role separation tests, dual-control tests, and direct mutation attempts.
- **Rationale:** Administrative compromise is a primary threat to a governance control plane.

### 10.4 Operations interface

- **Classification:** `PROFILE_SELECTION`.
- **Operations URI:** `https://ops.demo.agcp.example/ops/v1`, exposed through the same edge security layer as IF-001 but with a separate OAuth audience and authorization policy; anonymous access is prohibited.
- **Query functions:** Proposal, decision, authorization, lifecycle, evidence summary, and current tenant capability queries.
- **List functions:** Tenant-scoped proposal and evidence listings with bounded pagination and disclosure controls.
- **Audit functions:** Tenant-scoped audit search and integrity-verified evidence export.
- **Export functions:** Encrypted, signed tenant evidence package export.
- **Tenant scoping:** Exact server-side binding to the authenticated tenant.
- **Authentication and authorization:** Same strong authentication as IF-001 plus tenant roles and fine-grained permissions.
- **Direct Canonical State mutation prohibited:** Yes.
- **Verification method:** Mutation attempts, cross-tenant query tests, and export-signature validation.
- **Rationale:** Operators, instructors, and client participants require visibility without an alternate mutation path.

## 11. Ingress Trust Boundary and Authoritative Records

### 11.1 Command-versus-record distinction

- **Classification:** `ADR_IDR_REQUIRED`.
- **Untrusted command or submission object types:** GovernedActionProposalSubmission, GovernanceApprovalSubmission, EvidenceSubmission, DelegationSubmission, TenantConfigurationChangeCommand, PolicyActivationCommand, and AdapterInvocationRequest.
- **Authoritative AGCP-created record types:** QualifiedProposal, GovernanceDecision, ExecutionAuthorization, GovernanceApprovalArtifact, RefusalRecord, GovernanceReceipt, LedgerEvent, CanonicalStateSnapshotRecord, and ReEvaluationRecord.
- **AGCP-qualified external record types:** Identity assertion, entitlement assertion, external evidence artifact, and delegated authority artifact after qualification.
- **Server-derived fields that claimants may not assert authoritatively:** signature_verified, identity_verified, eligibility_verified, replay_unique, quorum_complete, evidence_qualified, canonical_state_resolved, authority_at_commitment, lifecycle_state, commit_status, and ledger_sequence.
- **Qualification process:** Structural validation, identity and provenance verification, tenant and semantic binding, authority and eligibility checks, replay checks, Canonical State qualification, and evidence sufficiency checks.
- **Conversion from submission to authoritative record:** A new immutable server-generated record is created with server attribution, qualification evidence, source reference, and content digest. The submission is retained as evidence but is not rewritten into an authoritative record.
- **Rejection behavior:** Invalid submissions produce a controlled transport rejection or Structural Refusal according to the stage reached. No claimant field can bypass qualification.
- **Decision record:** `ADR-PROF-004 Ingress Commands and Authoritative Records`.
- **Verification method:** Schema tests preventing server-derived fields in submission objects; attempts to submit verified flags; evidence-chain inspection.
- **Rationale:** Claimants cannot be trusted to assert the control plane's own verification results.

### 11.2 Governance Approval Artifacts

- **Classification:** `PROFILE_SELECTION` and `FIXED_NORMATIVE_OBLIGATION` where defined by adopted artifacts.
- **Approval submission object:** GovernanceApprovalSubmission containing proposal identity, decision intent, approver identity reference, reason, validity, and detached signature.
- **Authoritative Governance Approval Artifact:** Immutable AGCP-created record containing verified approver attribution, eligibility result, proposal and tenant binding, lifecycle binding, scope, validity, quorum contribution, nonce result, and source submission digest.
- **Approver attribution requirements:** Unique subject, tenant membership, role/attribute eligibility, authenticated session, and cryptographic signature.
- **Cryptographic verification requirements:** Hardware-backed or device-bound signing where available; profile-approved signature algorithm; key status checked at qualification and commit-time revalidation where required.
- **Eligibility verification:** Current tenant role, approval policy, conflict-of-interest constraints, and quorum membership from Canonical State.
- **Scope and validity binding:** Exact proposal, requested effect, target, tenant, policy version, and time window.
- **Proposal Identity binding:** Mandatory exact match.
- **Lifecycle-state binding:** Approval accepted only for eligible nonterminal states.
- **Partial quorum representation:** Each qualified approval is an independent immutable contribution; partial quorum is an authoritative lifecycle condition.
- **Completed quorum representation:** Deterministically derived from the set of currently valid, eligible, unique approval artifacts.
- **Replay-prevention rule:** Unique tuple of tenant, proposal, approver, approval purpose, and nonce; no contribution may count twice.
- **Storage and retrieval model:** Per-tenant approval store plus immutable ledger reference; tenant-scoped retrieval.
- **Verification method:** Ineligible approver, duplicate approval, stale approval, cross-tenant approval, revoked key, and lifecycle mismatch tests.
- **Rationale:** Human approval is evidence, not portable execution authority.

## 12. Authentication, Authorization, and Tenant Binding

> **Value classification:** AGCP tenant-binding and isolation obligations are real AGCP-connected requirements. Identity providers, token formats, claim names, lifetimes, roles, and authentication products are `ILLUSTRATIVE` profile selections.

### 12.1 Authentication profile

- **Classification:** `PROFILE_SELECTION`.
- **Public identity broker:** Auth0 Enterprise custom domain `https://auth.demo.agcp.example/`.
- **Administrative identity broker:** Separate Auth0 Enterprise custom domain `https://auth-admin.demo.agcp.example/`, accessible only through the management access path.
- **Tenant representation:** One Auth0 Organization per AGCP tenant; the Auth0 Organization identifier is mapped one-to-one to the AGCP tenant identifier.
- **Human authentication:** WebAuthn/passkey is mandatory. Password-only and SMS OTP authentication are prohibited. TOTP is prohibited for privileged roles and may be enabled only as a temporary recovery factor for nonprivileged users with security approval.
- **Service-principal authentication:** OAuth 2.0 client credentials using `private_key_jwt` and mTLS-bound access tokens; client secrets and public API keys are prohibited.
- **API token type:** Broker-issued JWT access token using `ES384` only.
- **External IdP federation:** Client-demo tenants may federate SAML or OIDC to Auth0. The AGCP API trusts only the broker-issued internal token, never an external IdP token directly.
- **Public issuer:** `https://auth.demo.agcp.example/`.
- **Administrative issuer:** `https://auth-admin.demo.agcp.example/`.
- **Required IF-001 audience:** `https://api.demo.agcp.example/agcp/v2` (`ILLUSTRATIVE` audience URI using the `AGCP-CONTROLLED` `/agcp/v2` path).
- **Required operations audience:** `https://ops.demo.agcp.example/ops/v1`.
- **Required management audience:** `https://mgmt.demo.agcp.example/mgmt/v1`.
- **Human access-token lifetime:** 300 seconds.
- **Service-principal access-token lifetime:** 300 seconds.
- **Management access-token lifetime:** 180 seconds.
- **Refresh-token absolute lifetime:** 8 hours with rotation and reuse detection.
- **Interactive-session idle timeout:** 30 minutes.
- **Interactive-session absolute lifetime:** 8 hours; management session absolute lifetime is 60 minutes.
- **Device requirement for management:** Managed and attested device, encrypted storage, current endpoint protection, and client certificate.
- **Revocation target:** Broker session revocation plus Canonical State update reaches commit-time checks within 30 seconds; tenant suspension is effective immediately at the platform control source.
- **Break-glass access:** Two offline FIDO2 hardware keys held under separate custody. Break-glass use requires dual authorization, a 15-minute session, mandatory incident record, and post-use credential rotation.
- **Verification method:** Issuer, audience, algorithm, expiry, token replay, refresh-token reuse, wrong organization, suspended subject, unmanaged device, and factor-downgrade tests.
- **Rationale:** The API has one strict token contract while tenants retain federation flexibility.

### 12.2 Identity and tenant claims

- **Classification:** `PROFILE_SELECTION`.
- **Subject claim:** `sub`, immutable within the broker tenant.
- **Tenant claim:** `tid`, containing the AGCP tenant URN.
- **Organization claim:** `org_id`, required and mapped to `tid` in Canonical State.
- **Role claim:** `roles`, containing only broker-issued role identifiers.
- **Permission claim:** `permissions`, containing endpoint scopes.
- **Authentication-method claim:** `amr`, required to contain `webauthn` for human users.
- **Token identifier claim:** `jti`, required and replay-monitored for privileged operations.
- **Authentication-time claim:** `auth_time`, maximum age 15 minutes for approval operations and 5 minutes for management operations.
- **Tenant identifier format:** `urn:agcp:tenant:<uuidv7>`.
- **Principal identifier format:** `urn:agcp:principal:<tenant-uuidv7>:<uuidv7>`.
- **Route, body, query, reference, token, and Canonical State binding:** Every tenant identifier shall exactly equal the authenticated `tid`; no default tenant and no client-selected tenant override are permitted.
- **Tenant mismatch behavior:** Public 404 `RESOURCE_NOT_FOUND`; protected evidence records `TENANT_BINDING_MISMATCH`.
- **Missing tenant behavior:** 401 when the token lacks `tid`; 400 only when a required request field is structurally absent before resource resolution.
- **Cross-tenant lookup behavior:** Always 404 with response-size normalization and a target timing variance of no more than 25 milliseconds at p95 between missing and inaccessible resources.
- **Verification method:** Exhaustive mismatch matrix across token, route, body, referenced artifacts, policy, evidence, approval, target, and snapshot.
- **Rationale:** Tenant binding is explicit, redundant, and server enforced.

### 12.3 Authorization profile

- **Classification:** `PROFILE_SELECTION`.
- **Authorization engine:** Server-side RBAC plus ABAC evaluated from current Canonical State; token roles are hints and are revalidated against current membership.
- **Tenant roles:** `tenant_admin`, `instructor`, `student`, `client_demo_operator`, `client_participant`, `auditor`, `observer`, and `service_principal`.
- **Platform roles:** `platform_security_admin`, `platform_ops_admin`, `tenant_provisioning_admin`, `release_manager`, and `platform_auditor`.
- **Approval separation:** A user cannot approve a proposal they submitted when the active policy requires separation of duties. Platform release and high-impact management changes require two distinct authorized humans.
- **Required scopes:** `proposal:submit`, `proposal:read`, `approval:submit`, `evidence:read`, `evidence:export`, `ops:read`, `tenant:admin`, `policy:stage`, `policy:activate`, `release:approve`, and `platform:audit` as applicable.
- **Management-plane restrictions:** Separate issuer and audience, FIDO2, managed device, mTLS, private network, just-in-time elevation, and dual authorization.
- **Operations-interface restrictions:** Read and export only; no Canonical State mutation.
- **Commit-time revalidation:** Tenant status, subject status, membership, roles, delegation, approval eligibility, key status, and policy/configuration version are re-derived immediately before commitment.
- **Maximum standing privileged membership:** Two platform security administrators, two release managers, and two platform auditors. Additional privileges are time-bounded elevation only.
- **Verification method:** Role/permission matrix, stale token, stale role, self-approval, privilege escalation, confused deputy, and dual-control tests.
- **Rationale:** Current server-side authority, not token possession alone, controls execution.

### 12.4 Disclosure policy

- **Classification:** `PROFILE_SELECTION`.
- **Resource lookup disclosure mode:** `HIDE_404`.
- **Conditions for HTTP 404:** Missing resource, inaccessible resource, cross-tenant resource, or resource whose existence the caller is not authorized to know.
- **Conditions for HTTP 403:** The caller is authenticated, the resource existence is already legitimately known within the same tenant, and the denied operation does not expose protected information.
- **Cross-tenant disclosure behavior:** Always 404 with response timing normalization where practical.
- **Internal evidence or telemetry detail:** Exact denial reason retained in protected tenant-bound or platform-security evidence.
- **Verification method:** Enumeration and timing tests.
- **Rationale:** Training and client demo tenants must not discover each other.

### 12.5 Cross-domain authority scope

- **Classification:** `PROFILE_SELECTION`.
- **Cross-tenant authority transfer:** Prohibited.
- **Cross-domain authority transfer:** Prohibited in this profile.
- **Required trust artifacts:** Not applicable because transfer is prohibited.
- **Initial restrictions:** Delegations, approvals, keys, policies, evidence, and execution permits are tenant-bound and cannot be imported as authority into another tenant.
- **Future-profile extension rule:** Any future cross-domain profile requires explicit trust artifacts, reciprocal policy, namespace rules, revocation propagation, new threat model, RTM updates, and conformance tests.
- **Verification method:** Cross-tenant artifact substitution tests.
- **Rationale:** Full capability coverage does not require permitting cross-tenant authority transfer; it requires enforcing isolation correctly.

## 13. Cryptography and Key Management

> **Value classification:** AGCP integrity, attribution, verification, and replay-protection obligations are real AGCP-connected requirements. Algorithms, key services, rotation windows, cache values, and key-storage products are `ILLUSTRATIVE` profile selections.

### 13.1 Provenance and signature profile

- **Classification:** `PROFILE_SELECTION` plus `REPOSITORY_CORRECTION` until the provenance contradiction is resolved.
- **Applicable provenance specification:** Corrected AGCP Provenance Wire Format adopted by the controlled baseline.
- **Signature algorithm:** Ed25519 for AGCP provenance and evidence signatures. Platform release and metadata signing may additionally use ECDSA P-384 where required by the deployment KMS/HSM.
- **Canonicalization method:** RFC 8785 JSON Canonicalization Scheme for JSON signature inputs.
- **Character encoding:** UTF-8 without byte-order mark.
- **Base64url padding rule:** Unpadded base64url.
- **Protected-header contract:** Fixed profile-defined fields including algorithm, key identifier, content type, profile identifier, and signature purpose. Unknown protected fields are rejected.
- **Signature input construction:** Exact profile-defined protected header bytes plus exact canonical payload bytes and explicit domain-separation label.
- **Signer representation:** Stable tenant-bound or platform-bound principal/key reference.
- **Key identifier representation:** Tenant-scoped JWK `kid` for tenant keys; globally unique URN for platform release keys.
- **Signing-time rule:** `signed_at` is required and evaluated against authoritative time; it does not establish ledger ordering.
- **Clock-skew allowance:** Maximum 5 minutes; production overlay may reduce but not increase.
- **Nonce rule:** Cryptographically random 128-bit minimum nonce supplied by signer and enforced for durable uniqueness within its tenant and signature purpose.
- **Replay-retention rule:** At least 24 hours for provenance signatures; longer where the signed artifact validity exceeds 24 hours.
- **Scope binding:** Tenant, proposal identity, target, operation, policy version, validity window, and signature purpose as applicable.
- **Verification-failure mapping:** Invalid provenance before governance entry returns controlled 422 or authentication failure as appropriate; protected evidence records the exact cause.
- **Verification method:** Cross-language vectors, altered canonical bytes, wrong tenant, wrong purpose, duplicate nonce, stale time, revoked key, and header confusion tests.
- **Rationale:** Explicit domain separation and canonicalization prevent substitution and cross-protocol replay.

### 13.2 Key identifiers and purposes

- **Classification:** `PROFILE_SELECTION`.
- **`kid` format:** `urn:agcp:key:<tenant-id>:<purpose>:<uuid>` for tenant keys; `urn:agcp:key:platform:<purpose>:<uuid>` for platform keys.
- **`kid` uniqueness scope:** Globally unique by full URN and independently unique within tenant and purpose.
- **JWK or equivalent representation:** Public keys represented as pinned JWK records with algorithm, use, status, creation, activation, expiry, revocation, and provenance metadata.
- **Key purposes:** `provenance`, `approval`, `metadata`, `release`, `evidence-export`, `service-identity`, and `data-encryption`.
- **Tenant binding:** Tenant keys cannot validate artifacts for another tenant.
- **Key registration authority:** Private management plane using dual authorization for platform keys and tenant administrator plus platform security approval for tenant signing keys.
- **Key-use constraints:** Algorithm, purpose, tenant, validity, status, and allowed operations are enforced server side.
- **Verification method:** Wrong-purpose, wrong-tenant, expired, future, revoked, and duplicate-key tests.
- **Rationale:** Purpose-specific keys reduce cross-protocol and cross-tenant misuse.

### 13.3 Key storage, caching, rotation, and revocation

- **Classification:** `PROFILE_SELECTION` and `DEPLOYMENT_CONFIGURATION`.
- **Platform release and metadata keys:** ECDSA P-384 keys in AWS CloudHSM-backed KMS custom key store; private keys are non-exportable.
- **AGCP provenance and approval keys:** Ed25519; tenant private keys remain tenant controlled unless the tenant explicitly selects the hosted-signing option.
- **Data-encryption keys:** One AWS KMS symmetric key per tenant; envelope data keys are generated per object or record batch using AES-256-GCM.
- **Service identity keys:** 24-hour X.509 workload certificates from AWS Private CA, rotated after 12 hours.
- **Database credentials:** Dynamic credentials with 24-hour maximum validity; applications receive them through workload identity and Secrets Manager.
- **Public-key/status cache TTL:** 30 seconds maximum, with immediate event-driven invalidation.
- **JWKS cache TTL:** 300 seconds maximum with ETag validation; unknown `kid` causes one forced refresh and then fail closed.
- **Tenant signing-key rotation:** Every 90 days, or immediately after suspected compromise.
- **Platform metadata-key rotation:** Every 180 days.
- **Platform release-key rotation:** Every 365 days, with dual authorization.
- **Tenant data-encryption-key rotation:** Every 90 days; historical ciphertext is rewrapped during the following maintenance window.
- **Service-certificate rotation:** Every 12 hours.
- **Rotation overlap:** 24 hours for new signing use; old keys remain verification-only for the evidence-retention period unless revoked.
- **Revocation propagation target:** 30 seconds to all online authorization and commit-time checks; immediate at the authoritative key registry.
- **KMS/HSM unavailability:** Fail closed for signing, decryption needed for governance, and commit authorization; return 503 without exposing key details.
- **Verification method:** Rotation continuity, unknown key, forced refresh, stale cache, revocation latency, HSM failover, and compromise exercise.
- **Rationale:** Short validity and non-exportable hardware-backed keys limit compromise duration and blast radius.

### 13.4 Digest profile

- **Classification:** `PROFILE_SELECTION`.
- **Allowed digest algorithms:** SHA-256 and SHA-384 where the governing schema and interface explicitly identify the algorithm.
- **Required default algorithm:** SHA-256 for AGCP schema and catalog compatibility; SHA-384 may be used for release artifacts where explicitly declared.
- **Encoding:** Lowercase hexadecimal.
- **Canonical case:** Lowercase only.
- **Algorithm-specific length rule:** SHA-256 exactly 64 hex characters; SHA-384 exactly 96 hex characters.
- **Declared-algorithm consistency validation:** Mandatory before any digest comparison.
- **BLAKE2B or variable-length algorithm treatment:** Prohibited in this profile until explicit fixed-output variants and validation rules are controlled.
- **Verification method:** Wrong length, uppercase, invalid characters, algorithm mismatch, and truncated digest tests.
- **Rationale:** Strict algorithm/length coupling avoids ambiguous digest objects.

## 14. Persistence, Ledger, and Atomicity

### 14.1 Database topology

- **Classification:** `ADR_IDR_REQUIRED`.
- **One database, multiple schemas, or multiple databases:** Separate platform control database plus a dedicated PostgreSQL database for each tenant.
- **Tenant partitioning:** Physical logical-database isolation by tenant; tables within a tenant database remain tenant-tagged for defense in depth.
- **Tenant isolation mechanism:** Dedicated database credentials, dedicated connection pool, network policy, KMS-wrapped tenant data key, tenant-specific backup, and no cross-tenant SQL role.
- **Row-level security, if applicable:** Enabled within each tenant database for user/resource-level restrictions even though the database is tenant dedicated.
- **Data ownership:** Tenant data is logically owned by the tenant; platform control metadata is owned by the operator and minimized.
- **Verification method:** Credential substitution tests, cross-database connection tests, backup isolation tests, and row-level security tests.
- **Rationale:** Dedicated tenant databases provide stronger isolation for unrelated classes and client organizations.

### 14.2 Atomic governance transaction

- **Classification:** `ADR_IDR_REQUIRED`.
- **Proposal-state changes included:** Yes.
- **Governance Evidence included:** Yes.
- **Ledger event included:** Yes.
- **Idempotency result included:** Yes.
- **Outbox record included:** Yes.
- **Approval artifact changes included:** When the operation creates or consumes an approval artifact.
- **Canonical State projection changes included:** When the authoritative tenant store is changed by the governed action.
- **Transaction boundary:** One serializable tenant-database transaction for the governance result and all local authoritative records.
- **External effects after commit:** Only an outbox dispatcher with a single-use execution permit may publish an external effect after the local transaction commits.
- **Crash-recovery behavior:** Reprocess committed outbox records idempotently; never infer success from a missing response; reconcile adapter receipt before terminal lifecycle update.
- **Decision record:** `ADR-PROF-005 Atomic Persistence, Outbox, and External Effects`.
- **Verification method:** Fault injection at every transaction and dispatch boundary.
- **Rationale:** Atomic local evidence plus idempotent external dispatch avoids split-brain governance outcomes.

### 14.3 Governance Ledger storage and sequencing

- **Classification:** `PROFILE_SELECTION`.
- **Ledger backend:** Append-only tenant ledger tables plus immutable object-storage archive and periodic signed checkpoints.
- **Structured-field storage:** Required for query and validation.
- **Canonical-byte storage:** Required for deterministic replay and independent verification.
- **Hash-chain use:** Yes, one chain per tenant governance domain.
- **Hash-chain algorithm and formula:** `event_hash = SHA-256(domain_separator || previous_event_hash || uint64_be(sequence) || canonical_event_bytes)`.
- **Sequence-allocation strategy:** Locked per-tenant counter row allocated inside the same serializable transaction as the ledger event.
- **Per-tenant, per-domain, or global ordering:** Per-tenant governance-domain total order. Platform security events use a separate platform ledger.
- **Timestamp role:** Evidence of observed time and validity evaluation only.
- **Timestamp non-authority rule:** Timestamps shall not define ledger order.
- **Replay reconstruction rule:** Replay uses sequence, canonical bytes, artifact digests, Canonical State snapshot references, policy module digest, and profile/version metadata.
- **Verification method:** Chain verification, sequence-gap tests, reordered timestamp tests, restore-and-replay tests, and signed checkpoint validation.
- **Rationale:** Per-tenant ordering preserves isolation and deterministic lifecycle derivation.

### 14.4 Action-state projection

- **Classification:** `PROFILE_SELECTION`.
- **Separate action-state store:** Yes, within each tenant database.
- **Projection updated on write or derived on read:** Updated transactionally on write and independently rebuildable from ledger and authoritative records.
- **Projection reproducibility:** Mandatory; projection is not more authoritative than the source records.
- **Indexed lookup keys:** Proposal identity, action identity, lifecycle state, target, actor, policy digest, Canonical State snapshot, authorization identity, and time window.
- **Rebuild procedure:** Offline or controlled online rebuild to a new projection, verify digest/count invariants, then atomic swap.
- **Verification method:** Projection deletion and rebuild, divergent projection detection, and replay comparison.
- **Rationale:** Query performance must not compromise replayability.

## 15. Idempotency and Replay Protection

### 15.1 Idempotency state machine

- **Classification:** `FIXED_NORMATIVE_OBLIGATION` where required by IF-001 and `PROFILE_SELECTION` for implementation details.
- **Required interface operations:** Every state-creating or state-transitioning public operation identified by IF-001.
- **Uniqueness key:** `(tenant_id, operation_id, idempotency_key)`.
- **Request canonicalization:** RFC 8785 JCS after strict schema and semantic normalization.
- **Request digest algorithm:** SHA-256.
- **Atomic reservation rule:** First request atomically creates a reservation before governance processing.
- **In-progress behavior:** Same-body concurrent request receives a controlled in-progress response or waits within a bounded server timeout; different-body request receives 409.
- **Same-key, same-body behavior:** Replays the authoritative completed response without repeating the governed consequence.
- **Same-key, different-body behavior:** HTTP 409 `IDEMPOTENCY_CONFLICT` and protected evidence.
- **Completed-response replay behavior:** Exact status, public body, and relevant headers are replayed from encrypted storage; fresh transport metadata may be added without changing the authoritative outcome.
- **Retention period rule:** Minimum 24 hours. Production default is 7 days and is defined in the production overlay.
- **Stored response representation:** Encrypted response body, response digest, status, operation identity, completion state, and authoritative record references.
- **Encryption requirement:** Per-tenant envelope encryption.
- **Cleanup behavior:** Expiry creates an auditable tombstone digest sufficient to detect prohibited reuse during any longer replay window required by the operation.
- **Verification method:** Concurrent same-body, concurrent different-body, crash, retry, expiry, and cross-tenant key tests.
- **Rationale:** Idempotency must prevent duplicate consequence, not merely duplicate database rows.

### 15.2 Approval and provenance replay protection

- **Classification:** `PROFILE_SELECTION`.
- **Durable nonce uniqueness scope:** Tenant, key, signature purpose, and nonce.
- **Approval replay-prevention key:** Tenant, proposal identity, approver identity, approval purpose, and nonce.
- **Signature replay-prevention key:** Tenant, signer key, signature purpose, payload digest, and nonce.
- **Retention window:** At least the longer of 24 hours, artifact validity, or proposal nonterminal lifetime.
- **Expiration behavior:** Expired artifacts remain evidentiary but cannot contribute to current authority.
- **Cross-tenant replay prevention:** Tenant binding is part of signature input and uniqueness key.
- **Verification method:** Replay within same tenant, replay across tenants, replay after expiry, and replay after key rotation.
- **Rationale:** A valid signature does not imply valid context or unique use.

## 16. Determinism Controls

### 16.1 Authoritative time

- **Classification:** `PROFILE_SELECTION`.
- **Authoritative time source:** Platform time service synchronized to at least three authenticated upstream sources, with monotonic clock used for local duration measurement.
- **Clock synchronization requirement:** Nodes exceeding the production skew threshold are removed from service.
- **Validity-window evaluation rule:** One authoritative evaluation timestamp is captured and included in the qualified input set.
- **Clock-skew rule:** Maximum 5 minutes for external signatures; stricter internal threshold defined in production overlay.
- **Failure behavior when time suitability cannot be established:** Fail closed; do not issue authorization or commit permit. Return 503 where processing cannot begin or Structural Refusal where a qualified proposal fails a required validity condition.
- **Replay treatment of time:** Replay uses recorded authoritative evaluation time and time-source evidence, not current wall clock.
- **Verification method:** Clock drift, rollback, leap, unavailable source, and replay tests.
- **Rationale:** Time is a qualified input, not an implicit ambient dependency.

### 16.2 Randomness

- **Classification:** `PROFILE_SELECTION`.
- **Randomness permitted in governance evaluation:** No.
- **Permitted deterministic pseudo-random use, if any:** None in governance decisions. Cryptographic randomness is permitted only outside decision semantics for nonce/key generation and is recorded where needed for evidence.
- **Seed derivation rule:** Not applicable to policy evaluation.
- **Recorded replay inputs:** All nonce and generated identifier values that affect evidence identity.
- **Prohibited uses:** Tie-breaking, policy outcomes, approval selection, ordering, and resource allocation decisions.
- **Verification method:** Static analysis, runtime import restrictions, and repeated evaluation tests.
- **Rationale:** Random decision behavior is incompatible with equivalent-outcome replay.

### 16.3 Floating-point processing

- **Classification:** `PROFILE_SELECTION`.
- **Floating-point permitted in governance evaluation:** No.
- **Permitted operations:** None inside policy decision semantics.
- **Required precision and rounding:** Use bounded integers, fixed-point decimal with explicit scale, or rational representations.
- **Integer or fixed-point alternatives:** Mandatory for risk scores, quotas, thresholds, and resource values.
- **Cross-platform equivalence rule:** Canonical integer/fixed-point representation and overflow checks.
- **Verification method:** Static policy validation and cross-runtime vectors.
- **Rationale:** Floating-point variability can break deterministic equivalence.

### 16.4 Canonicalization boundaries

- **Classification:** `PROFILE_SELECTION`.
- **Objects canonicalized:** Proposals, approval submissions, evidence submissions, policy inputs/outputs, Canonical State snapshots, ledger events, metadata documents, and release manifests where JSON is used.
- **Exact bytes hashed:** UTF-8 RFC 8785 canonical bytes after schema validation and before storage.
- **Exact bytes signed:** Domain-separation label, protected header canonical bytes, and canonical payload bytes as defined by the applicable signature contract.
- **Canonical serialization version:** RFC 8785 JCS plus profile-specific version label `agcp-jcs-1`.
- **Protected and unprotected fields:** Security-significant fields are protected. Transport-only diagnostics may be unprotected and shall not affect authority.
- **Excluded fields:** Server receipt time, trace identifier, and non-authoritative display text unless explicitly included by the relevant artifact contract.
- **Verification method:** Golden vectors across Rust, Python, JavaScript, and Java or another independent implementation.
- **Rationale:** Every digest and signature boundary must be unambiguous.

## 17. Canonical State Profile

### 17.1 Canonical State source classes

- **Classification:** `ADR_IDR_REQUIRED`.
- **Tenant authoritative source:** The platform-control Aurora PostgreSQL cluster table `tenant_registry` plus the platform tenant-lifecycle ledger.
- **Identity and entitlement authoritative source:** Auth0 Organization membership synchronized into the platform `principal_membership` registry by signed event; commit-time checks require the synchronized version to be no older than 30 seconds.
- **Configuration authoritative source:** Signed immutable configuration bundles in S3 Object Lock, activated by digest in the platform control database.
- **Policy authoritative source:** Signed WASM policy modules in the private artifact registry plus the atomic activation record in the tenant database and tenant ledger.
- **Key authoritative source:** AWS KMS/CloudHSM status plus the qualified `key_registry` record in the platform control database.
- **Governance Ledger source:** Ordered per-tenant ledger for recorded governance events, event ordering, and Derived Lifecycle State.
- **Additional authoritative sources:** Tenant-specific governed resource adapter where the resource system is authoritative for target existence or state.
- **Non-authoritative context sources:** Client-supplied context, telemetry, agent memory, browser state, and unqualified external claims.
- **Decision record:** `ADR-PROF-006 Canonical State Sources, Precedence, and Qualification`.
- **Rationale:** Canonical State must reflect qualified operational reality without treating client context as authoritative.

### 17.2 Snapshot construction

- **Classification:** `PROFILE_SELECTION`.
- **Snapshot identity:** `urn:agcp:canonical-state:<tenant-id>:<uuid>`.
- **Snapshot digest:** SHA-256 over canonical snapshot descriptor and source-version manifest.
- **Included source versions:** Tenant record, membership/entitlement version, configuration digest, policy digest, key-status version, ledger sequence/checkpoint, target adapter version, and relevant approval/evidence versions.
- **Freshness requirements:** Tenant status 0 seconds from the platform control source; identity/membership 30 seconds; key status 30 seconds; active policy/configuration by immutable digest with live activation check; target state 5 seconds for read-only evaluation and live optimistic-version check at commit; approval/evidence status 30 seconds; ledger sequence live within the transaction.
- **Completeness requirements:** Every source required by the proposal's dependency declaration and active policy shall be present.
- **Consistency requirements:** Source identities, tenant, target, lifecycle, and version dependencies shall agree.
- **Integrity requirements:** Signature, digest, authenticated channel, and source authority validation.
- **Ordering suitability:** Ledger sequence and explicit source versions; never timestamp sorting alone.
- **Snapshot storage or reference:** Immutable snapshot descriptor stored with the decision and commit evidence; large source objects may be referenced by immutable digest.
- **Replay reconstruction:** Resolve exact source versions or archived canonical bytes by digest.
- **Verification method:** Missing source, stale source, inconsistent source, altered source, and replay tests.
- **Rationale:** Snapshot identity makes the exact governance basis independently verifiable.

### 17.3 Resolution and conflict policy

- **Classification:** `PROFILE_SELECTION`.
- **Deterministic source priority:** Profile-defined by fact type. Tenant status comes from tenant control; identity and membership from the broker registry; policy/configuration from active signed bundles; key status from key registry/KMS; lifecycle ordering from the ledger; target state from the qualified target adapter.
- **Conflict-detection rule:** Two qualified sources assert incompatible values for the same authoritative fact and evaluation horizon.
- **Conflict-resolution rule:** Use the designated source for the fact type. If two sources are both designated authoritative and no deterministic precedence is defined, fail closed.
- **Fail-closed conditions:** Missing mandatory source, stale source beyond limit, invalid signature/digest, conflicting equal-priority sources, unavailable commit-critical source, or inability to reconstruct the snapshot.
- **Source-unavailable behavior:** HTTP 503 when governance processing cannot start; Structural Refusal or Governed Re-evaluation Required when a qualified proposal loses required suitability.
- **HTTP or interface mapping for unavailable authoritative sources:** 503 `AUTHORITATIVE_SOURCE_UNAVAILABLE` with no sensitive detail.
- **Structural Refusal conditions:** Source is present but fails qualification or demonstrates inadmissibility.
- **Verification method:** Source priority matrix, equal-priority conflict tests, outage tests, and stale cache tests.
- **Rationale:** Silent conflict resolution would make outcomes dependent on implementation accident.

## 18. Risk-Based Re-Evaluation

- **Classification:** `PROFILE_SELECTION` implementing fixed AGCP obligations.
- **Material-change representation:** Signed typed Canonical State Change Event with tenant, source type, old/new digest, effective sequence, and affected fact keys.
- **Typed authoritative-input digest changes:** Mandatory for policy, configuration, tenant status, subject status, key status, delegation, approval, target state, evidence status, and dependency graph changes.
- **Dependency-edge model:** Explicit edges from each nonterminal proposal to authoritative fact keys, policy modules, approvals, evidence, targets, and composite dependencies.
- **Proposal-selection rule:** Select only nonterminal proposals whose dependency set intersects the typed change set and whose active risk configuration requires re-evaluation.
- **Deterministic affected-proposal traversal:** Sorted by tenant ledger sequence and Proposal Identity; no arrival-time ordering.
- **Proposal re-evaluation serialization:** Proposal-scoped lock and serializable transaction.
- **Unaffected-proposal treatment:** Lifecycle unchanged; no implicit refresh.
- **Recorded no-op outcomes:** Required when a proposal is evaluated and remains unchanged.
- **Re-evaluation outcome representation:** Immutable ReEvaluationRecord plus ledger event and updated Derived Lifecycle State where applicable.
- **Interface response behavior:** Public operation returns 200 for an authoritative re-evaluation outcome; background re-evaluation is visible through tenant-scoped operations queries.
- **Verification method:** CR-122/TC-122 plus change-selection, no-op, ordering, and concurrent-change tests.
- **Rationale:** Re-evaluation must be selective, deterministic, and attributable.

## 19. Policy Evaluation Module and Policy Evaluation Contract

### 19.1 Execution environment

- **Classification:** `PROFILE_SELECTION`.
- **Runtime format:** WebAssembly.
- **Isolation model:** Wasmtime-compatible sandbox with no WASI and a minimal deterministic host interface.
- **In-process, process-isolated, or sandboxed:** Separate policy-evaluation process or pod with seccomp, no network egress, read-only filesystem, and strict resource limits.
- **Module identity:** Stable policy module URN.
- **Module version:** Semantic version plus immutable digest.
- **Module digest:** SHA-256 of exact module bytes.
- **Module pinning rule:** Decision and evidence record the exact module digest; active module set is atomically activated by signed configuration.
- **Activation and rollback rule:** Dual-authorized atomic activation; rollback only to previously approved signed module set.
- **Verification method:** Module substitution, unsigned module, altered digest, prohibited import, and rollback tests.
- **Rationale:** Independently authored modules require a controlled deterministic machine boundary.

### 19.2 Profile-specific machine contract

- **Classification:** `FIXED_NORMATIVE_OBLIGATION` after adoption.
- **Companion interface identifier and version:** `IF-002-AGCP-WASM-PEC-1.0.0`.
- **ABI version:** `agcp_pec_abi_v1`.
- **Input envelope:** Canonical bytes containing profile/version, Proposal Identity, qualified proposal digest, Canonical State snapshot descriptor, policy/configuration digests, authoritative evaluation time, and applicable evidence/authority references.
- **Output envelope:** Canonical decision result containing outcome, constraints/invariants, reasons, required approvals, dependency declarations, and deterministic diagnostics safe for protected evidence.
- **Exported function name:** `agcp_evaluate_v1`.
- **Memory convention:** Host allocates bounded input/output buffers using profile-defined ABI functions; no arbitrary host memory access.
- **Deterministic host functions:** Read bounded input, emit bounded output, deterministic fixed-point helpers, and explicit structured error reporting.
- **Prohibited imports:** Network, filesystem, clock, randomness, environment variables, threads, dynamic linking, process creation, and unbounded memory growth.
- **External I/O restrictions:** No external I/O.
- **Fuel behavior:** Fuel limit supplied by signed deployment overlay within profile bounds; exhaustion maps to a controlled evaluation failure and no authorization.
- **Memory behavior:** Hard maximum, zeroed memory on reuse where supported, and deterministic out-of-memory mapping.
- **Timeout behavior:** Host terminates evaluation; no partial decision is accepted.
- **Trap mapping:** Stable profile registry codes; traps never map to Authorized.
- **Module-digest binding:** Mandatory in input, output evidence, authorization, and commit-time binding.
- **Activation semantics:** New module set becomes active atomically with policy/configuration version and effective ledger event.
- **Verification method:** ABI vectors, prohibited import tests, fuel/memory/timeout tests, and cross-runtime replay.
- **Evidence location:** Policy activation evidence and per-decision records.

### 19.3 Resource limits - Illustrative examples

All module, memory, CPU, timeout, fuel, call-depth, replica, and autoscaling values in this subsection are `ILLUSTRATIVE`; they are not AGCP normative values.

- **Classification:** `DEPLOYMENT_CONFIGURATION`.
- **Maximum WASM module size:** 8 MiB.
- **Maximum input envelope:** 256 KiB canonical bytes.
- **Maximum output envelope:** 256 KiB canonical bytes.
- **Fuel budget:** 25,000,000 Wasmtime fuel units per evaluation.
- **Linear-memory maximum:** 64 MiB per module instance.
- **Policy-evaluator pod memory:** 1 GiB request and 2 GiB limit.
- **Policy-evaluator pod CPU:** 1 vCPU request and 2 vCPU limit.
- **Hard wall-clock timeout:** 500 milliseconds per evaluation.
- **Maximum nested policy-call depth:** 32.
- **Maximum result constraints/invariants:** 1,024 entries.
- **Maximum concurrent evaluations per policy-evaluator pod:** 8.
- **Autoscaling:** 3 minimum and 24 maximum policy-evaluator pods in production, based on CPU, queue depth, and p95 latency.
- **Failure mapping:** Fuel, memory, timeout, trap, or output-limit failure never maps to Authorized. The request produces a controlled evaluation failure; 503 is used only when the evaluation service cannot safely start processing.
- **Verification method:** Exact-boundary, one-over-boundary, exhaustion, malicious module, and recovery tests.

### 19.4 Replay purity

- **Classification:** `PROFILE_SELECTION`.
- **State-snapshot input rule:** Only the qualified immutable snapshot descriptor and referenced canonical bytes may influence the decision.
- **Host-input rule:** Host inputs are explicit, typed, bounded, and evidence-recorded.
- **External I/O rule:** Prohibited.
- **Time-input rule:** Authoritative time is explicit input.
- **Randomness rule:** Prohibited.
- **Side-effect prohibition:** Policy module cannot mutate state, issue network calls, write files, or invoke an adapter.
- **Replay evidence:** Input envelope bytes, module bytes/digest, output bytes, ABI version, runtime version, and fuel limit.
- **Verification method:** Repeat evaluation across nodes and supported runtime versions.
- **Rationale:** Policy evaluation is a pure deterministic function over qualified inputs.

## 20. Concurrency and Processing Model

### 20.1 Concurrency control

- **Classification:** `ADR_IDR_REQUIRED`.
- **Production replicas:** Public API 3-12; Governance Decision 3-24; Governance Realization 3-12; PEP/executor 3-12; Ledger Writer 3-9; background workers 2-10.
- **Worker model:** Horizontally scalable workers partitioned by tenant; every proposal has a proposal-scoped serialization key.
- **Per-tenant active governance limit:** `TRAINING_CLASS` 100, `CLIENT_DEMO` 150, `INTERNAL_ASSURANCE` 300 concurrent nonterminal proposals.
- **Per-user active governance limit:** `TRAINING_CLASS` 20, `CLIENT_DEMO` 25, `INTERNAL_ASSURANCE` 50.
- **Transaction isolation:** PostgreSQL serializable.
- **Proposal advisory lock:** 64-bit key derived from SHA-256 of tenant ID plus Proposal Identity.
- **Target advisory lock:** Used when the active policy declares target exclusivity or deterministic contention.
- **Database statement timeout:** 3 seconds.
- **Database lock timeout:** 500 milliseconds.
- **Maximum transaction duration:** 5 seconds for the local governance transaction.
- **Deadlock/serialization retry:** Maximum two retries with fixed 100 ms and 300 ms backoff; a third conflict returns 409 or causes governed re-evaluation as appropriate.
- **Optimistic-version checks:** Proposal lifecycle, Canonical State snapshot, target version, active policy/configuration, authorization, approval set, and tenant status.
- **Sequence allocation:** Locked per-tenant counter row in the same transaction as the ledger event.
- **Deterministic ordering:** Tenant ledger sequence, policy-defined priority, conflict/dependency rules, and Proposal Identity; worker arrival time is never sufficient.
- **Decision record:** `ADR-PROF-007 Concurrency, Locking, and Sequence Allocation`.
- **Verification method:** 10,000-request concurrency stress per tenant class, serialization anomaly tests, deadlock injection, duplicate commit attempts, and cross-node replay.
- **Rationale:** Explicit limits and ordering preserve determinism under scale.

### 20.2 Public processing model

- **Classification:** `PROFILE_SELECTION`.
- **Synchronous or asynchronous public conformance surface:** Synchronous acceptance and authoritative governance outcome.
- **Pending Human Review representation:** Authoritative outcome with proposal lifecycle and required approval information.
- **Deferred representation:** Authoritative outcome with deterministic reason and dependencies.
- **Governed Re-evaluation Required representation:** Authoritative outcome; no execution until re-evaluation completes.
- **Transient internal state exposure prohibited:** Yes. Queueing, lock wait, retry, and worker state are not canonical governance lifecycle states.
- **Polling or callback behavior, if applicable:** Authenticated tenant-scoped polling through `/ops/v1`; optional signed callback may be added only through a separately controlled interface profile.
- **Verification method:** State-transition tests and internal-state leakage tests.
- **Rationale:** Internal processing state shall not become external governance truth.

## 21. HTTP and Service Outcome Mapping

| Condition | Profile mapping | Classification | Governing rationale | Verification |
|---|---|---|---|---|
| Invalid transport syntax | 400 `INVALID_REQUEST` | Profile selection | Request cannot be parsed | Parser tests |
| Invalid schema or asserted format | 422 `INVALID_CONTENT` | Profile selection | Parsed representation is invalid | Schema/format tests |
| Invalid authoritative content | 422 `INVALID_AUTHORITATIVE_CONTENT` | Profile selection | Content cannot be qualified | Semantic tests |
| Semantic binding failure | 422 or Structural Refusal according to processing stage | Fixed/profile mapping | Prevents mismatched authority/evidence | Mismatch fixtures |
| Authentication failure | 401 with standards-compliant challenge | Profile selection | Credential invalid or absent | Auth tests |
| Authorization failure where existence is known | 403 `FORBIDDEN` | Profile selection | Same-tenant known resource | Role tests |
| Resource not found | 404 `RESOURCE_NOT_FOUND` | Profile selection | Hide resource detail | Lookup tests |
| Cross-tenant resource lookup | 404 `RESOURCE_NOT_FOUND` | Profile selection | Prevent tenant enumeration | Isolation tests |
| Command or precondition conflict | 409 `CONFLICT` | Profile selection | State/idempotency/version conflict | Conflict tests |
| Authoritative source unavailable | 503 `AUTHORITATIVE_SOURCE_UNAVAILABLE` | Profile selection | Governance cannot safely proceed | Outage tests |
| Pre-governance tenant throttling | 429 with `Retry-After` | Deployment configuration | Transport protection before governance | Rate tests |
| Pre-governance global throttling | 429 with `Retry-After` | Deployment configuration | Platform protection | Rate tests |
| System-wide unavailable capacity | 503 `SERVICE_UNAVAILABLE` | Deployment configuration | Processing cannot begin | Capacity tests |
| Governance policy quota denial | 200 or interface-defined governance outcome containing Denied/Structural Refusal | Fixed/profile mapping | Policy denial is governance, not transport throttling | Policy tests |
| Authoritative re-evaluation outcome | 200 with authoritative outcome | Profile selection | Re-evaluation completed | Re-evaluation tests |
| Structural Refusal | Interface-defined governance outcome, not generic 500 | Fixed normative obligation | Refusal is a governance result | Official tests |

### 21.1 Rate limiting and service exhaustion

- **Classification:** `DEPLOYMENT_CONFIGURATION`.
- **Global authenticated limit:** 500 requests/second sustained, 1,000-request burst.
- **Global unauthenticated limit:** 20 requests/second sustained, 40-request burst, limited to health and public metadata routes.
- **Per-source-IP limit:** 50 requests/second authenticated and 5 requests/second unauthenticated; IPv6 is normalized to /64 for rate accounting.
- **Training tenant limit:** 20 requests/second sustained, 40-request burst, and 10,000 governance submissions/day.
- **Client-demo tenant limit:** 30 requests/second sustained, 60-request burst, and 25,000 governance submissions/day.
- **Internal-assurance tenant limit:** 100 requests/second sustained, 200-request burst, and 100,000 governance submissions/day.
- **Per-user limit:** 10 requests/second sustained and 20-request burst for human users.
- **Per-service-principal limit:** 25 requests/second sustained and 50-request burst unless a narrower scope is assigned.
- **Maximum request body:** 1 MiB compressed and 4 MiB after decompression.
- **Maximum header size:** 16 KiB total.
- **Maximum JSON nesting:** 64 levels.
- **Maximum array items:** 10,000 unless a stricter schema limit applies.
- **HTTP 429:** Used only for pre-governance throttling and always includes `Retry-After` between 1 and 60 seconds.
- **HTTP 503:** Used when capacity or a required dependency prevents safe processing from starting.
- **Governance quota denial:** Tenant entitlement or policy quota produces an authoritative Denied or Structural Refusal outcome and Governance Evidence, not transport 429.
- **WAF action:** Block known malicious patterns; challenge suspicious automated traffic; no WAF bypass path to the origin.
- **Verification method:** Per-tenant fairness, per-user isolation, global saturation, distributed-source testing, retry behavior, and quota-policy tests.
- **Rationale:** Concrete layered limits protect shared capacity without confusing transport throttling with governance decisions.

## 22. Validation Pipeline

| Validation stage | Required behavior | Failure outcome | Evidence | Verification |
|---|---|---|---|---|
| Transport and size limits | Enforce method, content type, header, body, nesting, and decompression limits | 400, 413, 415, or 429 | Security log | Boundary tests |
| Strict serialization parsing | Reject duplicate keys, invalid UTF-8, non-canonical numeric forms where prohibited, and trailing data | 400 | Security log | Parser corpus |
| Schema validation | Validate against exact pinned schema and reject unknown fields unless schema expressly permits them | 422 | Validation record | Schema tests |
| Asserted-format validation | Validate identifiers, timestamps, digests, signatures, URIs, and enums | 422 | Validation record | Format tests |
| Semantic binding validation | Validate tenant, proposal, target, evidence, policy, lifecycle, and reference equality | 422 or Structural Refusal | Protected evidence | Mismatch fixtures |
| Provenance verification | Verify signature, key status, time, nonce, purpose, scope, and canonical bytes | 401/422 or Structural Refusal | Protected evidence | Crypto vectors |
| Authentication verification | Validate broker token, audience, issuer, binding, and status | 401 | Security log | Auth tests |
| Authorization and tenant binding | Validate current membership, scopes, roles, attributes, and exact tenant binding | 403/404 or Structural Refusal | Protected evidence | Authorization matrix |
| Canonical State suitability | Resolve and qualify required authoritative sources | 503 or Structural Refusal | Governance Evidence | Source tests |
| Governance-processing entry | Create qualified immutable input identity and begin deterministic evaluation | Qualified Proposal or Structural Refusal | Ledger/evidence | Official tests |

- **Classification:** `PROFILE_SELECTION` implementing fixed obligations.
- **Unknown-field policy:** Reject unless the exact schema explicitly permits extension fields and defines their semantics.
- **Duplicate-key policy:** Reject.
- **Numeric-format policy:** Integers or fixed-point strings according to schema; no NaN, Infinity, exponent ambiguity, or unbounded values.
- **String-normalization policy:** No implicit Unicode normalization after signature creation. Identifiers use schema-defined restricted character sets; display strings are not authority-bearing unless explicitly canonicalized.
- **Validation ordering rule:** Exactly the order shown above, with safe early rejection before expensive cryptography or policy evaluation.
- **Failure short-circuit rule:** Stop at the first stage whose failure prevents safe continuation; record only protected details appropriate to that stage.
- **Verification method:** End-to-end stage-order tests and malicious parser corpus.
- **Rationale:** Deterministic ordering prevents inconsistent error and trust-boundary behavior.

## 23. Retention, Archival, and Deletion

> **Value classification:** AGCP evidence-preservation and replay obligations are real AGCP-connected requirements. Every duration, deletion period, archival period, and retention value in this section is `ILLUSTRATIVE`.

### 23.1 Governance Evidence and Ledger

- **Classification:** `PROFILE_SELECTION` and `DEPLOYMENT_CONFIGURATION`.
- **Governance Evidence retention:** Seven years after tenant closure.
- **Governance Ledger retention:** Seven years after tenant closure; no in-place deletion or mutation.
- **Online searchable period:** 365 days after event creation.
- **Immutable archive period:** Remainder of the seven-year period in S3 Object Lock Compliance mode.
- **Public deletion support:** None.
- **Tenant-user deletion authority:** None for Governance Evidence or ledger records.
- **Archival authority:** Platform Security Administrator and Platform Auditor dual authorization.
- **Legal hold:** Suspends expiry and cryptographic erasure until released by the profile owner or authorized legal authority.
- **End-of-retention disposition:** Verify no legal hold, create a signed disposition record, destroy the tenant KMS key under dual authorization, retain only nonidentifying release/conformance summaries, and ledger the destruction event in the platform security domain.
- **Training/class personal data:** Identity/contact data not required for evidence is deleted 90 days after tenant closure; evidence retains immutable principal identifiers and minimum attribution.
- **Client-demo personal data:** Same 90-day minimization rule unless a written client agreement specifies a shorter period.
- **Verification method:** Delete denial, archive restore, legal-hold, key-destruction rehearsal, and digest-chain verification.
- **Rationale:** Seven years provides durable assurance evidence while defining an explicit privacy-preserving end state.

### 23.2 Idempotency, nonce, and operational records

| Record class | Concrete retention | Deletion or expiry behavior | Verification |
|---|---:|---|---|
| Idempotency records | 7 days | Encrypted response purged; tombstone digest retained 30 days | Retry/expiry tests |
| Provenance nonces | 30 days or artifact validity, whichever is longer | Removed from active index after expiry; evidentiary reference remains | Replay tests |
| Approval replay index | Proposal nonterminal lifetime plus 30 days | Active uniqueness index may compact; approval evidence remains seven years | Quorum replay tests |
| Security/audit logs | 90 days hot plus 365 days immutable archive | Signed deletion record after expiry | Retention audit |
| Application logs | 30 days hot plus 90 days archive | Secure deletion; no raw tokens or secrets | Logging audit |
| High-resolution telemetry | 30 days | Aggregated, tenant-minimized metrics retained 365 days | Privacy audit |
| Signed metadata | Current document plus prior two release documents; release bundle retained seven years | Never replaced by an unverified document | Outage/rollover tests |
| Vulnerability scan results | Seven years with release evidence | Immutable archive | Supply-chain audit |

## 24. Implementation Metadata

- **Classification:** `FIXED_NORMATIVE_OBLIGATION` where required by adopted interface.
- **Metadata operation and path:** `GET /agcp/v2/meta` (`AGCP-CONTROLLED` public interface version/path).
- **Profile ID field:** `profile_id`.
- **Profile version field:** `profile_version`.
- **Profile URI field:** `profile_uri`.
- **Profile digest field:** `profile_sha256`.
- **Base AGCP version field:** `agcp_version`.
- **Baseline digest field:** `baseline_sha256`.
- **Capability representation:** Explicit supported capability identifiers and status; no inference from marketing labels.
- **Interface version representation:** Exact IF-001 and IF-002 identifiers/versions.
- **Schema and registry version representation:** Catalog version and digest.
- **Conformance claim-status representation:** `NOT_CLAIMED`, `PARTIALLY_VERIFIED`, or `VERIFIED`, with claim-record URI/digest only when applicable.
- **Public-information limitation:** No tenant list, internal topology, private endpoint, vulnerability, key material, internal version, or operational contact data.
- **Metadata signing rule:** Signed by hardware-backed platform metadata key; signature and key status publicly verifiable.
- **Generation point:** Release time and startup verification.
- **Cache rule:** Immutable per release, cached by digest.
- **Dependency-outage behavior:** Serve the last valid signed metadata document if the service remains safe to operate; otherwise return 503.
- **Last-valid-document behavior:** Document remains available with accurate release identity; no fabricated freshness.
- **Verification method:** Signature, altered document, stale key, missing dependency, and release rollover tests.
- **Evidence location:** Signed release evidence bundle and metadata service ledger.

## 25. Illustrative Deployment Configuration

Every AWS service, account, region, VPC, IP address, CIDR block, endpoint hostname, capacity, quota, timeout, cache value, replica count, CPU value, memory value, backup interval, SLO, RTO, and RPO in this section is `ILLUSTRATIVE` and non-operational. The `/agcp/v2` path is the only public-endpoint element treated as AGCP-connected.

The following values are part of this profile. Overlays may reduce capacity or shorten local-development retention, but production values shall not be weakened without a profile revision.

### 25.1 Network and platform topology

| Configuration | Production value |
|---|---|
| Primary AWS account | Dedicated production account for AGCP-DTS (`ILLUSTRATIVE`) |
| Primary region | `us-east-1` |
| DR region | `us-west-2` |
| Primary VPC CIDR | `10.40.0.0/16` (`ILLUSTRATIVE`) |
| DR VPC CIDR | `10.41.0.0/16` (`ILLUSTRATIVE`) |
| Availability zones | Three per region |
| Public DNS | Route 53 hosted zone for `demo.agcp.ai` |
| Public edge | CloudFront + AWS WAF + Shield Advanced |
| Public origin | Internet-facing ALB restricted to CloudFront origin-facing addresses and a secret origin header; no direct application origin route |
| Kubernetes cluster | `agcp-demo-prod-use1`; private EKS API endpoint only |
| DR cluster | `agcp-demo-dr-usw2`; normally scaled to warm-standby minimum |
| Worker OS | Bottlerocket, no SSH, IMDSv2 only |
| Service mesh | Istio strict mTLS |
| Egress | Default deny; per-service FQDN/IP allowlists through controlled egress gateways |
| Management access | AWS Verified Access plus private DNS, FIDO2, managed device, and client-certificate mTLS |

### 25.2 Public endpoints

| Function | URI | Exposure |
|---|---|---|
| IF-001 v2 public API | `https://api.demo.agcp.example/agcp/v2` | Hostname `ILLUSTRATIVE`; `/agcp/v2` `AGCP-CONTROLLED`; Internet/authenticated posture `ILLUSTRATIVE` |
| Implementation metadata | `https://api.demo.agcp.example/agcp/v2/meta` | Hostname `ILLUSTRATIVE`; `/agcp/v2/meta` AGCP-connected; exposure posture `ILLUSTRATIVE` |
| Profile publication | `https://api.demo.agcp.example/agcp/v2/profiles/AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0` | Hostname and profile publication route `ILLUSTRATIVE`; `/agcp/v2` `AGCP-CONTROLLED` |
| Tenant operations | `https://ops.demo.agcp.example/ops/v1` | Internet, authenticated and tenant scoped |
| Identity | `https://auth.demo.agcp.example/` | Internet, Auth0 custom domain |
| Management API | `https://mgmt.demo.agcp.example/mgmt/v1` | Private only |
| Administrative identity | `https://auth-admin.demo.agcp.example/` | Reachable only through management access path |

### 25.3 Tenant-class capacities

| Value | Training class | Client demo | Internal assurance |
|---|---:|---:|---:|
| Maximum active tenants | 20 | 10 | 3 |
| Maximum human users per tenant | 50 | 25 | 20 |
| Maximum service principals per tenant | 10 | 10 | 25 |
| Sustained requests/second | 20 | 30 | 100 |
| Burst requests | 40 | 60 | 200 |
| Governance submissions/day | 10,000 | 25,000 | 100,000 |
| Concurrent nonterminal proposals | 100 | 150 | 300 |
| Default tenant lifetime | 45 days | 30 days | Indefinite |
| Automatic suspension | 7 days after scheduled class end | At scheduled engagement end | Manual |
| Non-evidentiary PII deletion | 90 days after closure | 90 days after closure | 90 days after record becomes unnecessary |

### 25.4 Runtime, timeout, and cache values

| Configuration | Production value |
|---|---:|
| Public request timeout | 15 seconds |
| Internal gRPC deadline | 2 seconds |
| Canonical State source timeout | 1 second per source; 2.5 seconds aggregate |
| KMS/HSM call timeout | 750 milliseconds |
| Local governance transaction timeout | 5 seconds |
| External governed-adapter timeout | 10 seconds |
| Policy evaluation timeout | 500 milliseconds |
| Policy fuel | 25,000,000 units |
| Policy linear memory | 64 MiB |
| Policy module/input/output limits | 8 MiB / 256 KiB / 256 KiB |
| Public key/status cache TTL | 30 seconds |
| JWKS cache TTL | 300 seconds |
| Membership cache TTL | 30 seconds |
| Immutable policy/config cache | 15 minutes by digest; activation checked live at commit |
| In-process cache maximum | 256 MiB per pod; tenant-keyed and never shared across tenant IDs |
| DB connections per tenant cluster | 30 maximum |
| Platform-wide DB connections | 300 maximum |

### 25.5 Pod replicas and resources

| Service | Min replicas | Max replicas | CPU request/limit | Memory request/limit |
|---|---:|---:|---|---|
| Public API | 3 | 12 | 500m / 2 | 512 MiB / 2 GiB |
| Governance Decision | 3 | 24 | 1 / 2 | 1 GiB / 2 GiB |
| Governance Realization | 3 | 12 | 1 / 2 | 1 GiB / 2 GiB |
| PEP/Executor | 3 | 12 | 1 / 2 | 512 MiB / 1 GiB |
| Ledger Writer | 3 | 9 | 500m / 1 | 512 MiB / 1 GiB |
| Operations API | 2 | 6 | 250m / 1 | 256 MiB / 1 GiB |
| Re-evaluation workers | 2 | 10 | 500m / 2 | 512 MiB / 2 GiB |
| Outbox dispatchers | 2 | 10 | 500m / 2 | 512 MiB / 1 GiB |

### 25.6 Security rotation values

| Security object | Rotation or validity |
|---|---|
| Human access token | 5 minutes |
| Management access token | 3 minutes |
| Refresh token/session | 8 hours absolute, 30 minutes idle |
| Workload certificate | 24-hour validity, rotate at 12 hours |
| Dynamic database credential | 24-hour maximum |
| Tenant provenance/approval key | 90 days |
| Tenant data-encryption key | 90 days |
| Platform metadata key | 180 days |
| Platform release key | 365 days |
| Revocation propagation | 30 seconds maximum |
| External signature clock skew | 5 minutes maximum |
| Internal node clock offset | 100 milliseconds maximum; node removed from service when exceeded |

### 25.7 Backup, recovery, and observability values

| Configuration | Production value |
|---|---|
| Aurora point-in-time recovery | 35 days |
| Daily snapshots | 35 days |
| Weekly snapshots | 13 weeks |
| Monthly snapshots | 84 months |
| Cross-region replication | Required for tenant DB snapshots, S3 evidence, and release evidence |
| RPO | 1 minute for tenant database/ledger; zero-loss expectation for immutable release artifacts |
| RTO | 60 minutes for platform service; 120 minutes for full tenant restoration |
| Restore testing | Monthly single-tenant restore and quarterly full-environment exercise |
| Availability SLO | 99.95 percent monthly, excluding approved maintenance |
| IF-001 latency SLO | p95 <= 750 ms and p99 <= 2 s for operations not requiring human review or external governed execution |
| Commit-local latency SLO | p95 <= 1 s before external adapter time |
| Security alert acknowledgement | 15 minutes, 24x7 |
| Critical incident containment target | 30 minutes |
| Audit-log retention | 90 days hot plus 365 days immutable archive |
| Evidence/ledger retention | Seven years after tenant closure |
| SIEM | Amazon OpenSearch Service with GuardDuty and Security Hub integration |

### 25.8 Configuration files

In a real implementation, the illustrative values above would be maintained as environment-specific configuration in the external build/deploy repository, for example:

- `<build-deploy-repo>/deploy/overlays/production.yaml`;
- `<build-deploy-repo>/deploy/overlays/staging.yaml`;
- `<build-deploy-repo>/deploy/overlays/test.yaml`;
- `<build-deploy-repo>/deploy/overlays/development.yaml`; and
- `<build-deploy-repo>/deploy/tenant-classes.yaml`.

The adopted Implementation Profile would control AGCP semantic constraints and permitted profile selections. The external build/deploy configuration would control environment-specific operational values and would be required to conform to the adopted profile. These external files are not included in this informational example package.

## 26. Operational Hardening and Lifecycle

> **Repository boundary:** The procedures and environment-specific values described here would be implemented in the build/deploy repository under `<build-deploy-repo>/runbooks/` and `<build-deploy-repo>/deploy/`. The paths and values below are `ILLUSTRATIVE` references and are not included in this profile package.

### 26.1 Backup and disaster recovery

- **Classification:** `DEPLOYMENT_CONFIGURATION`.
- **Aurora point-in-time recovery:** 35 days.
- **Daily tenant and platform snapshots:** 35-day retention.
- **Weekly snapshots:** 13-week retention.
- **Monthly snapshots:** 84-month retention.
- **Cross-region copy:** Required to `us-west-2` with a distinct DR KMS key.
- **S3 Governance Evidence:** Versioning, Object Lock Compliance mode, cross-region replication, and seven-year retention after tenant closure.
- **Key-material recovery:** Non-exportable KMS/HSM keys use multi-region or provider-supported resilient replication. Exported private keys are prohibited.
- **Backup encryption:** AES-256 using a backup-specific KMS key separated from active tenant data keys.
- **Backup manifest:** SHA-384 digest, ECDSA P-384 signature, source release/profile/baseline identity, and object inventory.
- **Restore testing:** Monthly restore of one randomly selected tenant; quarterly complete platform exercise; mandatory successful exercise before a conformance claim.
- **RPO:** One minute for tenant database and ledger; zero-loss expectation for immutable release artifacts.
- **RTO:** 60 minutes for platform availability and 120 minutes for complete tenant restoration.
- **Runbooks:** `<build-deploy-repo>/runbooks/dr-development.md` and `<build-deploy-repo>/runbooks/dr-production.md`.
- **Verification evidence:** Signed restore report, ledger-chain verification, Canonical State reconstruction, and application smoke tests.

### 26.2 Database migration

- **Classification:** `ADR_IDR_REQUIRED`.
- **Migration tooling:** Signed versioned Rust/SQL migration package executed by a dedicated migration identity.
- **Forward-only or reversible policy:** Forward-only for authoritative ledger history; reversible application/schema changes only when proven not to discard or reinterpret evidence.
- **Pre-migration validation:** Backup, integrity check, capacity check, schema compatibility, dry run, and RTM impact review.
- **Data compatibility rule:** Existing records retain original schema/profile/version identity and remain replayable.
- **Rollback rule:** Roll back application release or restore to a verified pre-migration state; never edit historical ledger records.
- **Evidence preservation:** Migration start/end events, tool digest, operator identities, affected versions, and validation results are ledgered in the platform security domain.
- **Verification method:** Migration rehearsal, rollback test, historical replay, and downgrade-denial test.
- **Rationale:** Schema evolution cannot rewrite governance history.

### 26.3 Upgrade, rollout, activation, and rollback

- **Classification:** `PROFILE_SELECTION` and `ADR_IDR_REQUIRED`.
- **Release-candidate process:** Build once, sign, scan, test, stage, assess, and promote exact digests.
- **Configuration immutability rule:** Active configuration is immutable and content-addressed.
- **Startup validation:** Verify release signature, manifest, SBOM reference, profile/baseline digests, schema catalog, registry catalog, policy modules, configuration, database compatibility, KMS, and required authoritative sources.
- **Atomic activation rule:** Policy/configuration/schema-compatible release set activates atomically with a ledger event.
- **Rollout strategy:** Canary in internal assurance tenant, then training tenants, then client-demo tenants. No mixed semantic version within one tenant evaluation horizon.
- **Rollback strategy:** Return to previously approved signed release/configuration set; preserve evidence and migration records.
- **Tenant suspension strategy:** Immediate fail-closed suspension prevents new governance processing and commits while preserving read-only evidence access for authorized users.
- **Emergency disablement boundaries:** May stop new traffic, suspend tenants, revoke keys, or disable adapters. Shall not create an execution bypass or delete evidence.
- **Prohibited bypass behavior:** No debug flag, emergency permit, operator override, or direct adapter credential may authorize execution outside Governance Realization and PEP.
- **Verification method:** Startup failure tests, canary rollback, partial activation, suspension, and emergency procedure exercises.
- **Rationale:** The governance system must protect itself during change and incident response.

### 26.4 Observability and incident readiness

- **Classification:** `DEPLOYMENT_CONFIGURATION`.
- **Availability SLO:** 99.95 percent per calendar month, excluding approved maintenance.
- **IF-001 latency SLO:** p95 no more than 750 ms and p99 no more than 2 seconds for requests not requiring human review or external governed execution.
- **Commit-local latency SLO:** p95 no more than 1 second before external-adapter time.
- **Security-event delivery:** Critical events reach the SIEM within 60 seconds.
- **Critical alert acknowledgement:** 15 minutes, 24x7.
- **Critical incident containment target:** 30 minutes.
- **Required telemetry:** Availability, latency, error class, throttling, authentication, authorization, Canonical State suitability, policy limits, ledger integrity, key events, admin actions, tenant lifecycle, adapter outcomes, and PEP permit use.
- **Required audit fields:** Time, actor, tenant, operation, proposal/resource, outcome, source IP or workload identity, credential ID, profile/baseline/release, correlation ID, and evidence reference. Raw tokens, secrets, and private keys are prohibited.
- **Immediate alerts:** Ledger-chain failure, signature/digest mismatch, unauthorized management attempt, cross-tenant access attempt, signing-key event, policy/configuration tamper, PEP bypass attempt, repeated Canonical State failure, and direct-origin traffic.
- **External-beta gates:** Successful monthly restore, incident tabletop, independent penetration test, threat-model review, load test at 2x configured sustained rate, and all critical profile tests.
- **Runbooks:** `<build-deploy-repo>/runbooks/observability.md`, `<build-deploy-repo>/runbooks/incident-response.md`, and `<build-deploy-repo>/runbooks/security-operations.md`.
- **Verification evidence:** Alert drills, SIEM rule tests, incident tabletop, penetration report, and remediation record.

## 27. Release Engineering and Supply-Chain Evidence

- **Classification:** `PROFILE_SELECTION`.
- **Whole-release signed manifest required:** Yes.
- **SBOM required:** Yes, SPDX or CycloneDX, signed and bound to release digest.
- **Binary provenance required:** Yes.
- **Build attestation required:** Yes, including source revision, builder identity, workflow, dependencies, toolchain, and artifact digests.
- **Source revision binding:** Exact immutable Git commit and clean-tree assertion.
- **Dependency lockfile binding:** Required and included in attestation.
- **Reproducible build requirement:** Required where technically practical; otherwise independent rebuild comparison and documented non-reproducible inputs.
- **Artifact-signing authority:** Hardware-backed release key controlled by Release Manager and Security Authority dual workflow.
- **Release metadata location:** Immutable release evidence bundle and metadata endpoint reference.
- **Verification method:** Fresh-environment rebuild, signature verification, altered dependency test, and admission control.
- **Rationale:** A secure runtime cannot rely on an unverifiable software supply chain.

## 28. Profile-Specific Verification and Conformance Extension

| Test class | Required | Scope | Test artifact | Acceptance criterion |
|---|---|---|---|---|
| Official conformance tests | Yes | All applicable CRs | Official suite | 100 percent applicable pass |
| Semantic binding tests | Yes | Proposal, tenant, target, policy, evidence, approval, lifecycle | Profile extension | All positive and negative cases pass |
| Positive controlled fixtures | Yes | Every success/admissible/activated path | Controlled fixtures | Internally consistent and schema/semantic valid |
| Negative mismatch fixtures | Yes | Every binding class | Controlled fixtures | Correct refusal/rejection and evidence |
| Property tests | Yes | Canonicalization, idempotency, lifecycle, isolation | Rust property tests | No invariant violation in configured run |
| Mutation tests | Yes | Validation and authorization logic | Mutation framework | Required mutation score and no surviving critical mutation |
| Concurrency tests | Yes | Adjudication, commit, sequence, idempotency | Stress harness | No duplicate consequence or nondeterministic outcome |
| Crash-recovery tests | Yes | Transaction/outbox/adapter boundaries | Fault injection harness | Correct recovery with no lost/duplicate evidence |
| Malicious-input tests | Yes | Parser, schema, crypto, decompression, resource limits | Fuzz and corpus tests | No crash, bypass, or unbounded resource use |
| Cross-language cryptographic vectors | Yes | JCS, signatures, digests | Vector package | Byte-for-byte agreement |
| Canonicalization vectors | Yes | All signed/hashed JSON objects | Vector package | Exact canonical bytes/digests |
| Tenant-isolation tests | Yes | DB, API, cache, object store, logs, exports | Isolation suite | Zero cross-tenant disclosure or mutation |
| Cross-domain authority tests | Yes | Delegation, approval, evidence substitution | Negative suite | All transfer attempts fail closed |
| Key-rotation tests | Yes | Platform and tenant keys | Security suite | Continuous verification without unauthorized overlap |
| Key-revocation tests | Yes | Cache and commit-time revalidation | Security suite | Revoked authority cannot commit |
| Tenant-suspension tests | Yes | All public/ops/adapter paths | Lifecycle suite | No new commit after effective suspension |
| PEP-bypass tests | Yes | Every governed adapter | Red-team suite | No alternate execution path |
| Canonical State conflict tests | Yes | Every source class | State suite | Deterministic precedence or fail closed |
| Risk-Based Re-Evaluation tests | Yes | CR-122 and profile dependencies | Re-evaluation suite | Deterministic affected set and outcomes |
| Backup restoration tests | Yes | Tenant and platform | DR suite | RTO/RPO met and ledger verifies |
| Metadata continuity tests | Yes | Startup/outage/rollover | Interface suite | Last valid signed metadata served correctly |
| MFA and session security tests | Yes | All human roles | Identity suite | No password-only access; revocation works |
| Management dual-control tests | Yes | High-impact admin operations | Management suite | Single operator cannot complete operation |
| Internet exposure tests | Yes | WAF, TLS, headers, DDoS controls, origin isolation | External security suite | No direct origin access; only approved TLS and routes |

## 29. Repository Correction Dependencies

| Finding ID | Classification | Description | Required ruling or correction | Affected artifacts | Blocking scope | Status | Verification evidence |
|---|---|---|---|---|---|---|---|
| P0-02 | `REPOSITORY_CORRECTION` | Provenance wire/schema contradiction | Make wire-format envelope authoritative and synchronize schemas, examples, OpenAPI, tests, catalog, and reports | Provenance spec and dependents | Freezing provenance structs and interoperability claim | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Corrected validation and test report |
| P0-10 | `REPOSITORY_CORRECTION` | Semantically inconsistent positive fixtures | Correct tenant/proposal/domain/policy/artifact bindings and add negative vectors | Controlled examples and tests | Conformance evidence quality | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Semantic fixture validation |
| P2-01 | `REPOSITORY_CORRECTION` | Inconsistent publication/lifecycle labels | Separate release status, artifact lifecycle, version, and baseline date | Catalogs and artifacts | Controlled publication metadata | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Repository metadata audit |
| P1-01 | `REPOSITORY_CORRECTION` | References to absent normative companions | Remove, supersede, or resolve controlled references | Specifications and catalogs | Normative reference integrity | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Link/reference validation |
| P0-06 | `REPOSITORY_CORRECTION` plus profile ADR | Ingress combines claimant facts and server-derived assertions | Add submission and authoritative record schemas | Schemas, OpenAPI, examples, RTM, tests | Public trust boundary | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Schema and trust-boundary tests |
| P1-03 | `REPOSITORY_CORRECTION` plus profile mapping | Inconsistent public not-found codes | Public `RESOURCE_NOT_FOUND`; retain specific codes only in protected evidence | OpenAPI, vectors, pseudocode | Public error interoperability | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Contract tests |
| P1-12 | `REPOSITORY_CORRECTION` | Digest length/case not coupled to algorithm | Enforce exact algorithm lengths and lowercase | Schemas and vectors | Digest validation | Open in the v2.0.0 baseline; mandatory before interoperability or conformance claim | Schema tests |
| P0-05 | `REPOSITORY_CORRECTION` / companion creation | IF-002 machine contract absent | Publish controlled WASM PEC interface | IF-002, RTM, tests | Independent policy modules | Mandatory before independently authored policy modules are enabled | ABI validation |

## 30. Associated Decision Records

| Decision record | Subject | Status | Repository path or URI | Affected profile sections |
|---|---|---|---|---|
| ADR-PROF-001 | Enforcement Boundary and PEP Placement | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-001.md` | 7, 14, 20, 28 |
| ADR-PROF-002 | Service and Trust-Boundary Decomposition | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-002.md` | 9, 10, 19 |
| ADR-PROF-003 | Private Management Plane and Dual Control | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-003.md` | 10, 12, 26 |
| ADR-PROF-004 | Ingress Commands and Authoritative Records | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-004.md` | 11, 22 |
| ADR-PROF-005 | Atomic Persistence, Outbox, and External Effects | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-005.md` | 14, 20, 26 |
| ADR-PROF-006 | Canonical State Sources, Precedence, and Qualification | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-006.md` | 17, 18 |
| ADR-PROF-007 | Concurrency, Locking, and Sequence Allocation | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-007.md` | 14, 20 |
| ADR-PROF-008 | Cryptographic and Key-Management Profile | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-008.md` | 12, 13, 24, 27 |
| ADR-PROF-009 | Tenant Classes, Identity Federation, and Multi-User Roles | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-009.md` | 9, 12, 23 |
| ADR-PROF-010 | WASM PEC Isolation and ABI | Illustrative example decision; no ADR has been approved or published | `adr/ADR-PROF-010.md` | 19, 28 |

## 31. Traceability Record

### 31.1 Required traceability

The RTM profile extension shall add relationship-specific rows rather than one generic row. The following is an illustrative minimum mapping set for an adopted version of this profile.

| Profile section or decision | ARM reference(s) | NS reference(s) | CR reference(s) | DS reference(s) | IF reference(s) | REG reference(s) | TC reference(s) | ADR/IDR reference(s) | Repository artifact(s) |
|---|---|---|---|---|---|---|---|---|---|
| Claimed enforcement scope and PEP | ARM-201, ARM-210 through ARM-213 | NS-9.1-01, NS-9.4-03, NS-9.6-04 and applicable mappings | Applicable commit/enforcement CRs | Enforcement context schemas | IF-001 and adapter contract | Error/outcome registries | Applicable official and bypass tests | ADR-PROF-001 | Profile, adapter specs, tests |
| Tenant isolation and multi-user binding | ARM-102, ARM-103, ARM-203, ARM-213 | Applicable tenant, binding, and isolation NS | Applicable multitenant CRs | Tenant, identity, context schemas | IF-001 | Role and tenant-status registries | Tenant-isolation tests | ADR-PROF-009 | Profile, identity config, tests |
| Canonical State resolution | ARM-103, ARM-202, ARM-209 | NS-4.6-01 through NS-4.6-05, NS-7.4-01 | Applicable Canonical State CRs | Snapshot and source descriptors | Resolver interface | Source-type registry | State suitability tests | ADR-PROF-006 | Resolver spec and tests |
| Approval artifacts | ARM-107 | Applicable approval and authority NS | Applicable human review CRs | Approval submission/artifact schemas | Approval interface | Approval status/reason registries | Quorum/replay tests | ADR-PROF-004, ADR-PROF-008 | Approval service artifacts |
| Risk-Based Re-Evaluation | ARM-209 | Applicable re-evaluation NS | CR-122 | Change/dependency/re-evaluation schemas | Re-evaluation interface | Change-type registry | TC-122 and extensions | ADR-PROF-006 | Re-evaluation service/tests |
| Deterministic WASM PEC | ARM-204 and applicable compilation concepts | Determinism and decision NS | Applicable decision/compilation CRs | PEC input/output schemas | IF-002 | Trap/outcome registries | ABI and replay tests | ADR-PROF-010 | IF-002 and runtime tests |
| Atomic persistence and ledger | ARM-104, ARM-108 and evidence/lifecycle concepts | Applicable evidence, ledger, lifecycle NS | Applicable evidence/ledger CRs | Ledger/event schemas | Internal ledger interface | Event-type registry | Crash/replay tests | ADR-PROF-005, ADR-PROF-007 | DB migrations, ledger tests |

### 31.2 RTM update

- **RTM dataset version:** `RTM-2.0.0-PROFILE-EXT-1.0.0`.
- **New or modified RTM records:** Profile, IF-002, tenant-class, management-plane, operations-interface, and profile-test mappings.
- **Relationship types:** `IMP`, `MAP`, `LOC`, `VER`, `VAL`, `DEP`, `CNS`, and `ADR` as appropriate.
- **Architectural rationale:** Full-scope public demonstration requires explicit implementation mappings while preserving Core technology independence.
- **Semantic review status:** Informational example only; not reviewed, approved, or incorporated into the authoritative RTM.
- **Verification status:** Profile mapping defined; implementation verification occurs per release.
- **Approval authority:** Not applicable to the example; an adopted profile would require the RTM Owner, Specification Owner, and Conformance Authority.
- **Validation report:** `release-evidence/<release>/rtm-validation.json`.

## 32. Controlled Artifact Inventory

| Artifact | Identifier and version | Repository path or URI | Digest binding | Lifecycle state | Approval status |
|---|---|---|---|---|---|
| Base AGCP release | AGCP v2.0.0 Public Review Controlled Baseline (`AGCP-CONTROLLED`) | Controlled baseline source location | Controlled baseline integrity record | Controlled baseline | Referenced by the example; not adopted by this document |
| Implementation Profile | This informational example v1.2.0 | `profiles/full-scope-multitenant-demo/AGCP-FULL-SCOPE-MULTITENANT-DEMO-2.0.0.md` | Detached `.sha256` file | Example | Not approved; informational only |
| Machine-readable profile | v1.2.0 | `profiles/full-scope-multitenant-demo/profile.yaml` | Signed release manifest | Example | Not approved; informational only |
| Public interface | IF-001 v2.0.0 (`AGCP-CONTROLLED`) | Controlled baseline location | Controlled baseline integrity record | Current | Referenced; any correction remains subject to repository governance |
| WASM PEC interface | IF-002-AGCP-WASM-PEC-1.0.0 | `interfaces/if-002-wasm-pec/` | Signed release manifest | Proposed example companion | Not part of the controlled baseline |
| Schema catalog | AGCP v2.0.0 catalog (`AGCP-CONTROLLED`) | Controlled baseline location | Controlled baseline integrity record | Current baseline artifact | Repository findings in Section 29 remain separate |
| Registry catalog | AGCP v2.0.0 catalog (`AGCP-CONTROLLED`) | Controlled baseline location | Controlled baseline integrity record | Current baseline artifact | Repository findings in Section 29 remain separate |
| RTM profile extension | RTM-2.0.0-PROFILE-EXT-1.0.0 | `traceability/rtm/` | Signed release manifest | Illustrative mapping plan | Not incorporated into the authoritative RTM |
| Official tests | TC-001 through TC-122 (`AGCP-CONTROLLED`) | Controlled baseline location | Controlled baseline integrity record | Current | Referenced by the example |
| Profile test extension | v1.0.0 | `tests/profile/full-scope-multitenant-demo/` | Signed release manifest | Illustrative test plan | Not implemented or approved |
| Development overlay | Illustrative | `<build-deploy-repo>/deploy/overlays/development.yaml` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Test overlay | Illustrative | `<build-deploy-repo>/deploy/overlays/test.yaml` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Staging overlay | Illustrative | `<build-deploy-repo>/deploy/overlays/staging.yaml` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Production overlay | Illustrative | `<build-deploy-repo>/deploy/overlays/production.yaml` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Tenant-class configuration | Illustrative | `<build-deploy-repo>/deploy/tenant-classes.yaml` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Operations runbooks | Illustrative | `<build-deploy-repo>/runbooks/` | External build/deploy repository | `ILLUSTRATIVE` | Not packaged with profile |
| Release manifest/SBOM/attestations | Per release (`PROPOSED-EXAMPLE`) | `release-evidence/<release>/` (`ILLUSTRATIVE`) | Example hardware-backed signature | Not generated | Would be required per release |
| Conformance claim record | Per verified release (`PROPOSED-EXAMPLE`) | `release-evidence/<release>/conformance-claim.json` (`ILLUSTRATIVE`) | Example hardware-backed signature | Not created | Could exist only after verification |

## 33. Approval Record

No approval is granted or represented by this informational example. The table shows the review and approval roles that a real implementation profile would require before adoption, deployment, or a conformance claim.

| Review or approval | Authority | Date | Result | Required follow-on evidence |
|---|---|---|---|---|
| Architecture Review | Not performed | Not applicable | Informational example only | Required before adoption |
| Security Design Review | Not performed | Not applicable | Informational example only | Independent review required before adoption |
| Traceability Plan Review | Not performed | Not applicable | Informational example only | RTM review required before adoption |
| Normative/Profile Review | Not performed | Not applicable | Informational example only | Specification-owner review required before adoption |
| Interface/Profile Review | Not performed | Not applicable | Informational example only | Interface review required before adoption |
| Operations Design Review | Not performed | Not applicable | Informational example only | Operations review required before adoption |
| Implementation Owner Approval | Not performed | Not applicable | Informational example only | Formal owner approval required before adoption |
| Conformance Review | Example AGCP Conformance Authority role | Not applicable | Not performed | Full official and adopted-profile test results would be required |
| External Production Security Review | Example independent assessor role | Not applicable | Not performed | Penetration and remediation evidence would be required before external use |

## 34. Profile Completion and Release Readiness

### 34.1 Profile completion

- [x] Profile ID, version, example status, lifecycle state, and non-applicable ownership/approval fields are explicitly populated.
- [x] Public, operations, identity, and private management endpoints are defined.
- [x] Hosting platform, regions, network boundaries, database topology, identity broker, key services, and telemetry stack are selected.
- [x] Tenant classes, user capacities, service-principal capacities, tenant lifetimes, and quotas are defined.
- [x] Authentication factors, algorithms, token lifetimes, claims, session limits, and break-glass controls are defined.
- [x] Cryptographic algorithms, key stores, rotation periods, cache TTLs, and revocation targets are defined.
- [x] Illustrative rate limits, payload limits, timeouts, policy limits, database limits, replicas, and resource requests are provided as completion examples; a real build/deploy repository would supply adopted values.
- [x] Backup schedules, retention, RTO, RPO, SLOs, alert targets, and incident targets are defined.
- [x] Claimed enforcement scope and explicit exclusions are defined.
- [x] Conformance target and current claim status are separate and accurate.
- [x] No field remains `TBD` or `TBC`; non-AGCP implementation values are intentionally concrete but explicitly `ILLUSTRATIVE`.

### 34.2 Release and conformance gates

The informational example is complete as a worked example, but it is not approved for implementation. A real adopted profile would have to complete the following engineering, governance, release, and conformance gates:

- [ ] Vendor the exact AGCP baseline and generate `baseline.lock.json` with real artifact digests.
- [ ] Apply and validate the Section 29 repository corrections.
- [ ] Publish IF-002 and synchronize OpenAPI, schemas, registries, RTM, and controlled fixtures.
- [ ] Generate detached profile digest and signed release manifest.
- [ ] Generate SBOM, build provenance, binary/image signatures, and deployment attestations.
- [ ] Complete standalone ADR extraction and RTM synchronization.
- [ ] Execute all applicable official and profile-specific tests.
- [ ] Complete independent penetration testing, restoration exercise, and incident exercise.
- [ ] Create a signed conformance claim record only if every mandatory gate passes.

## 35. Revision History

| Profile version | Date | Change summary | Change classification | Affected sections | Approval authority |
|---|---|---|---|---|---|
| 1.0.0 | 2026-08-02 | Initial full-scope multitenant profile example | Initial draft | All | Informational only |
| 1.1.0 | 2026-08-02 | Added concrete platform, endpoint, tenant, identity, cryptographic, capacity, timeout, retention, recovery, and operational values | Example completion | All | Informational draft |
| 1.2.0 | 2026-08-02 | Restored informational-example status; distinguished real AGCP-controlled references from illustrative deployment values; removed implied approvals and live-service representations | Corrective clarification | All | Informational only |
| 1.3.0 | 2026-08-02 | Classified `agcp-rs`, AWS services, resource limits, IP/CIDR values, and operational values as illustrative; moved deploy/runbook artifacts to the external build/deploy repository boundary; corrected the public interface to `/agcp/v2` | Corrective clarification | 1-5, 9-13, 19, 23, 25-26, 32-35, appendices | Informational only |


> **Example-use notice:** Sections 9 through Appendix C contain concrete implementation values to demonstrate completeness. `agcp-rs`, AWS and third-party services, hostnames, IP/CIDR values, resource limits, capacities, timing values, retention values, SLOs, RTO/RPO values, deploy paths, and runbook paths are illustrative and non-operational. Only values expressly marked `AGCP-CONTROLLED` are treated as real AGCP-connected values. The deploy and runbook artifacts referenced by this profile belong in an external build/deploy repository and are not part of this profile package.

## Appendix A - Tenant Classes and User Model

### A.1 Training class tenant

- **Tenant class:** `TRAINING_CLASS`.
- **Purpose:** One isolated tenant per course delivery, cohort, workshop, or class.
- **User capacity:** Up to 50 human users and 10 service principals; minimum one instructor and two students.
- **Permitted roles:** tenant_admin, instructor, student, auditor, observer, and service_principal.
- **Identity model:** Platform IdP by default; no shared accounts.
- **Data rule:** Synthetic training data and course artifacts only. Personal data is minimized to identity and course administration data.
- **Lifecycle:** Default 45 days. Automatically suspended seven days after the scheduled class end; non-evidentiary PII is deleted 90 days after closure and Governance Evidence is retained seven years.
- **Isolation:** No visibility into any other class or client-demo tenant.

### A.2 Client demonstration tenant

- **Tenant class:** `CLIENT_DEMO`.
- **Purpose:** One isolated tenant per client organization or confidential demonstration engagement.
- **User capacity:** Up to 25 human users and 10 service principals; minimum one client_demo_operator and one client_participant.
- **Permitted roles:** tenant_admin, client_demo_operator, client_participant, auditor, observer, and service_principal.
- **Identity model:** Approved client IdP federation or platform IdP guest identity through the broker; all users require FIDO2 MFA.
- **Data rule:** Synthetic or approved sanitized data by default. Real client production credentials, unrestricted secrets, and regulated datasets are prohibited without a separate data-protection approval and deployment overlay.
- **Lifecycle:** Default 30 days and automatically suspended at the scheduled engagement end. Non-evidentiary PII is deleted 90 days after closure and Governance Evidence is retained seven years.
- **Isolation:** No visibility into other clients or training tenants.

### A.3 Internal assurance tenant

- **Tenant class:** `INTERNAL_ASSURANCE`.
- **Purpose:** Regression, security, conformance, integration, and red-team testing.
- **User capacity and roles:** Up to 20 human users and 25 service principals; restricted internal roles only.
- **Data rule:** Synthetic test data and malicious-input corpora; never reused as a client tenant.
- **Lifecycle:** Long-lived but separately isolated from public tenant classes.

### A.4 Multi-user guarantees

Every tenant shall:

- support multiple simultaneously active human users;
- assign unique user identities and prohibit shared credentials;
- support multiple service principals with separately scoped credentials;
- permit immediate suspension and revocation of individual users without suspending the tenant;
- record every governance-significant user action with subject and tenant attribution;
- prevent one user from approving an action where the active policy requires separation of duties or quorum; and
- preserve tenant membership and role changes as qualified Canonical State inputs.

## Appendix B - Internet Exposure Security Baseline

The Internet-exposed endpoint shall use the following minimum controls:

1. Public traffic terminates at a managed DDoS protection and WAF layer.
2. The application origin is not directly reachable from the public Internet.
3. TLS 1.3 is required; deprecated protocols and weak cipher suites are disabled.
4. HSTS, secure response headers, request-size limits, connection limits, and decompression limits are enforced.
5. Authentication is required for every functional endpoint except health checks designed for public availability and public metadata expressly permitted by the profile.
6. Human users use phishing-resistant WebAuthn/FIDO2 MFA; password-only access is prohibited.
7. The public API accepts only short-lived broker-issued asymmetric tokens.
8. Public API keys, long-lived bearer tokens, and shared user accounts are prohibited.
9. The management plane is private and uses a separate identity audience, network path, mTLS, managed-device policy, and dual control.
10. Internal services use workload identity and mTLS with automatic short-lived certificate rotation.
11. Egress is default denied and allowlisted per service.
12. Tenant data is isolated by dedicated database, credentials, encryption key, ledger, and storage namespace.
13. Secrets and private keys are held in KMS/HSM and are not stored in source, images, environment-variable dumps, logs, or configuration files.
14. Containers run non-root with read-only filesystems, dropped capabilities, runtime confinement, and signed image admission.
15. Release artifacts, policy modules, schemas, configuration, and metadata are signed and digest pinned.
16. Security telemetry is sent to a protected SIEM with alerts for cross-tenant attempts, key events, tamper, bypass, and privileged operations.
17. External penetration testing and restoration testing are required before an external beta or conformance claim.
18. No production claim is made solely because these controls are documented; objective evidence is required.

## Appendix C - Controlling Profile Decision Statement

### Decision PROF-SEC-001 - Maximum-Security Multitenant Internet Deployment

- **Classification:** `ADR_IDR_REQUIRED`.
- **Status:** Informational example only; not approved, controlling, or adopted. A real implementation would require a separately reviewed and published ADR.
- **Controlling AGCP source(s):** AGCP Core v2.0.0, applicable multitenancy, provenance, interface, evidence, and conformance artifacts.
- **Decision:** Deploy a full-scope AGCP service with an Internet-exposed authenticated public interface, private management plane, dedicated tenant databases and keys, phishing-resistant MFA, short-lived asymmetric credentials, internal mTLS, owner-controlled PEP/executor, deterministic WASM policy evaluation, immutable evidence, and signed release artifacts.
- **Profile statement:** Security controls are mandatory across all tenant classes and cannot be disabled by a tenant or development overlay.
- **Rationale:** Unrelated students and clients share platform infrastructure; therefore tenant compromise, credential theft, administrative misuse, and cross-tenant disclosure are primary threats.
- **Alternatives considered:** Single shared database with tenant rows; public management endpoint; password-plus-TOTP; long-lived API keys; in-process policy plug-ins; client-controlled execution. These alternatives were rejected because they create larger blast radius, weaker phishing resistance, greater bypass risk, or reduced determinism.
- **Security consequences:** Increased operational complexity, cost, and onboarding friction; materially stronger isolation, attribution, and compromise resistance.
- **Interoperability consequences:** Client IdPs are supported through the broker, while the API retains one internal token contract.
- **Conformance consequences:** Supports truthful full-scope implementation mapping but does not create a conformance claim without evidence.
- **Deployment consequences:** Requires private network access for management, KMS/HSM, workload PKI, dedicated tenant databases, signed supply-chain evidence, and continuous security operations.
- **Affected schemas:** Identity, tenant, approval, provenance, metadata, Canonical State, and evidence schemas.
- **Affected interfaces:** IF-001, IF-002, `/ops/v1`, `/mgmt/v1`, and adapter contracts.
- **Affected registries:** Roles, tenant classes, key purposes, outcomes, errors, lifecycle states, source types, and trap codes.
- **Affected tests:** All tenant-isolation, authentication, authorization, key, management, PEP-bypass, supply-chain, and Internet exposure tests.
- **Affected RTM records:** Profile-specific implementation and verification mappings.
- **Required ADR or IDR:** ADR-PROF-001 through ADR-PROF-010.
- **Required deployment overlay or runbook:** Production overlay, security operations, key management, incident response, and disaster recovery runbooks.
- **Verification method:** Architecture/security review, automated profile tests, penetration test, conformance suite, release attestation verification, and evidence replay.
- **Evidence location:** Signed release and assessment evidence bundle.
- **Approval authority:** Not applicable to this example; shown only as the roles a real adoption would require.
- **Approval date:** Not applicable to this example.
