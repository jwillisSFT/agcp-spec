# AGCP Implementation Profile Template

**Profile format:** 2.0.0  
**Use:** Copy this template to create a controlled implementation-specific profile. Do not place secrets in the profile.

## 1. Profile Control Record

- Profile ID:
- Name:
- Profile version:
- Status:
- Owner:
- Authoritative YAML/JSON artifact:
- Human-readable rendering:
- Canonical digest:

## 2. Controlled Baseline

- AGCP release:
- Controlled CR/Core/Companion artifacts:
- Schema catalog / validator-set identities:
- Adopted optional companion specifications:

## 3. Conformance and Intended Use

- Claim status:
- Claimed conformance scope:
- Claimed enforcement scope:
- Intended use:
- Explicit limitations / non-goals:

## 4. Implementation Identification

- Implementation ID/version:
- Runtime language/platform:
- Distribution model:

## 5. Deployment Topology and Assurance Boundary

Describe runtime units, process/service boundaries, network/IPC trust boundaries, persistence boundaries, external-provider dependencies, operator-managed responsibilities, and excluded assurance surfaces.

Do not use customer-, course-, workspace-, or hosting-product-specific terminology in a generic/public profile unless that profile is explicitly deployment-specific.

## 6. Interface Profile

### 6.1 IF-001

- Base path:
- Exposure:
- Authentication:
- Idempotency:

### 6.2 Management

- Implemented:
- Interface/transport:
- Authority separation:

### 6.3 Test Control

- Implemented:
- Interface/transport:
- Isolation model:

### 6.4 PEC / PEM

- Interface ID:
- Runtime:
- Determinism constraints:

## 7. Trust Boundaries

Document:

- proposer -> control plane;
- identity/authorization source -> control plane;
- Canonical State -> control plane;
- governance repository -> control plane;
- human governance principal -> control plane;
- GDF/PDP -> GRF;
- GRF -> PEP;
- PEP -> target; and
- target -> evidence/lifecycle.

List any alternate mutation/admin/recovery paths relevant to the non-bypassability claim.

## 8. Governance Function Placement

| Function | Placement | Workload identity / authority | Notes |
|---|---|---|---|
| Proposal Qualification | | | |
| GDF / PDP | | | |
| Execution Authorization | | | |
| GRF | | | |
| PEP | | | |
| Governed target/adapter | | | |

State whether GDF/PDP and GRF are co-located. If separated, document the protected interface and integrity/authentication requirements.

## 9. Identity and Authorization Profile

### 9.1 Authentication model

Describe human and workload authentication.

### 9.2 IAS Profile reference

- IAS Profile ID:
- IAS Profile version:
- IAS Profile SHA-256:
- Artifact path/URI:

### 9.3 Qualified identity/authorization context

Describe which identity-system facts are governance-significant, such as:

- stable subject/account identity;
- active/disabled/revoked state;
- Tenant/Domain membership;
- roles and groups;
- entitlements;
- governance permissions and reviewer classes;
- scopes;
- delegation/authority attributes;
- validity/effective periods.

State where resolution occurs, freshness/cache rules, consumers, and fail-closed behavior.

**Important:** IAS authorization/entitlement information is not AGCP Execution Authorization and does not itself produce a Governance Decision.

## 10. Cryptography and Key Management

Document algorithms, trust anchors, key purposes, rotation/revocation, and secret references. Do not embed secret key material.

## 11. Canonical State Profile

Document authoritative source classes, qualification, freshness, conflict policy, snapshot semantics, and failure behavior.

## 12. Governance Compilation and PEM Runtime

Document governance package source/activation, PEM runtime, profile-specific machine contract if any, resource limits, side-effect/network restrictions, and replay purity.

## 13. Lifecycle and Human Review

Document supported outcomes, human-review workflow, authoritative approval creation, quorum behavior, current authority revalidation, and relationship to the IAS Profile.

## 14. Governance Realization and Enforcement

### 14.1 GRF

Describe current-authority/state/evidence revalidation, binding validation, prior-use/single-use handling, and Commit-Bound Admissibility.

### 14.2 PEP Profile references

For each PEP Profile:

- Profile ID/version/digest:
- Supported governed action/target scope:
- Selection rule:

### 14.3 GRF -> PEP

- Authentication / workload identity:
- Protected transport or in-process boundary:
- Required Enforcement Context:

### 14.4 PEP -> target

- Target authority / credential reference:
- Alternate paths and non-bypassability controls:

### 14.5 Mapping and failure semantics

State that unsupported or non-faithful mappings fail closed and cannot widen/substitute the governed action.

### 14.6 Commitment versus execution

Select and explain: atomic; asynchronous/distinct; or mixed by operation.

## 15. Persistence, Ledger, Idempotency, and Replay

Document authoritative stores, transaction/atomicity model, ledger sequencing, idempotency state, replay protection, and deterministic replay.

## 16. HTTP and Error Mapping

Document not-found/disclosure policy, rate limiting/capacity, application errors, and governance-outcome separation.

## 17. Re-evaluation

List material-change triggers and the required path back through GDF/PDP and GRF.

## 18. Metadata

Document public-safe metadata fields and how implementation, AGCP release, controlling profile, IAS Profile, PEP Profile(s), schema/validator set, and active governance are bound/exposed.

## 19. Backup, Recovery, and Operational Controls

Document protected state, recovery integrity, operator-only functions, and evidence continuity.

## 20. Performance Qualification

Document the evidence-backed method used to publish limits or service objectives.

## 21. Profile-Specific Tests

Include negative tests for at least:

- claimant identity/entitlement substitution;
- stale/disabled/revoked human authority;
- GDF/PDP result treated as direct execution authority;
- stale Execution Authorization;
- unsupported PEP mapping;
- PEP Profile substitution;
- direct target bypass;
- cross-Tenant/Domain identity or enforcement substitution; and
- duplicate/replay effects.

## 22. Required Decision Records

List all deployment decisions that remain controlled outside the profile and identify their owner/source.

## 23. Approval and Revision History

Record approval status, owner, version, date, summary, and affected subordinate profile digests.
