# AGCP Implementation Profile Specification

Status: Controlled Implementer Specification

Version: `1.1.0`

Schema: [`AGCP-Implementation-Profile-Schema.json`](./AGCP-Implementation-Profile-Schema.json)

## 1. Purpose

This specification defines the controlled file format, validation rules, lifecycle rules, and cross-artifact consistency requirements for an AGCP Implementation Profile.

An Implementation Profile records stable implementation selections, supported capabilities, deployment constraints, interface mappings, trust boundaries, assurance limitations, and profile-specific verification obligations for one identified implementation. It does not replace the AGCP Core, create an alternate conformance model, or permit an implementation to weaken a higher-precedence AGCP obligation.

Validation against the profile schema establishes **profile-format validity only**. It does not establish that the described implementation conforms to AGCP.

## 2. Authority and precedence

For files declaring profile format version `1.1.0`:

1. the YAML profile is the authoritative machine-readable representation;
2. the Markdown profile is its human-readable companion rendering;
3. the JSON Schema is authoritative for profile serialization structure and data types;
4. this specification is authoritative for serialization semantics, canonicalization, lifecycle, and cross-file consistency; and
5. higher-precedence AGCP requirements remain controlling.

When a profile conflicts with a published AGCP requirement, the profile is invalid to the extent of the conflict. The conflict shall be resolved through the controlled specification or profile change process and shall not be resolved by silently changing implementation behavior.

## 3. Required package

A controlled profile package shall contain:

```text
implementer/
├── AGCP-Implementation-Profile-Specification.md
├── AGCP-Implementation-Profile-Schema.json
├── <PROFILE-ID>.yaml
└── <PROFILE-ID>.md
```

The YAML profile shall validate before the Markdown companion is approved or published.

## 4. Artifact responsibilities

### 4.1 Format specification

The format specification defines authority, precedence, serialization, canonicalization, lifecycle, extension handling, Markdown consistency, and controlled change procedures.

### 4.2 JSON Schema

The JSON Schema uses JSON Schema Draft 2020-12, rejects undeclared properties except under the controlled `extensions` namespace, and constrains mandatory sections, identifiers, versions, dates, digests, lifecycle values, and data types.

### 4.3 YAML profile

The YAML profile is the source of truth for machine processing and shall contain only JSON-compatible data.

### 4.4 Markdown profile

The Markdown profile may add rationale, explanation, diagrams, and review guidance, but it shall not add, remove, or contradict a machine-readable profile decision.

## 5. YAML data-model rules

A conforming profile YAML file shall:

- decode to one JSON object;
- use UTF-8 and string object keys;
- prohibit duplicate keys, custom tags, aliases, and merge keys;
- prohibit non-finite numeric values;
- quote date values so they remain JSON strings;
- represent unresolved optional values as `null`;
- contain no secrets, credentials, tokens, or private keys; and
- validate after conversion to the JSON data model.

Optional implementation-specific data may appear only in the top-level `extensions` object. Each extension key shall begin with `x-`.

## 6. Required top-level sections

Format version `1.1.0` requires the following sections:

| Section | Purpose |
|---|---|
| `$schema` | Identifies the controlling JSON Schema. |
| `document` | Declares artifact type, format version, companion rendering, canonicalization, and digest. |
| `profile` | Identifies owner, lifecycle, version, and approval authority. |
| `baseline` | Pins the AGCP release and schema namespace. |
| `conformance` | Declares target level, claim posture, enforcement scope, and exclusions. |
| `intended_use` | States approved and prohibited uses. |
| `implementation` | Defines the stable runtime and deployment architecture. |
| `platform_topology` | Defines development, class-delivery, and scale-out node roles. |
| `workspace_model` | Defines team workspaces, access, persistence, and privilege boundaries. |
| `hosting_assurance_boundary` | Separates provider, operator, student, and unclaimed responsibilities. |
| `interfaces` | Defines IF-001, routing, management, operations, and PEM interfaces. |
| `trust_boundaries` | Defines command/record separation and authoritative-boundary rules. |
| `identity` | Defines platform, workspace, runtime actor, and agent identity. |
| `cryptography` | Defines signatures, canonicalization, digesting, replay, and key limits. |
| `canonical_state` | Defines source locality, qualification, snapshotting, and resolution behavior. |
| `schema_validation` | Defines whole-release build checks and route-specific runtime validation. |
| `compilation_and_activation` | Separates validator generation from Governance Compilation and Controlled Activation. |
| `pem_runtime` | Defines deterministic Policy Evaluation Module execution. |
| `persistence` | Defines platform and governance stores, partitioning, atomicity, and concurrency. |
| `background_processing` | Defines persistent or scheduled deferred work. |
| `idempotency` | Defines key scope, request digesting, replay, and conflict behavior. |
| `validation_pipeline` | Declares ordered request-validation stages. |
| `http` | Declares HTTP, disclosure, throttling, and capacity behavior. |
| `reevaluation` | Defines dependency-driven re-evaluation. |
| `metadata` | Defines metadata generation and advertised state. |
| `backup_and_recovery` | Defines integrity, off-provider copies, and restoration testing. |
| `performance_qualification` | Defines class-capacity and failure-mode qualification. |
| `operational_values` | Identifies mutable values delegated to deployment overlays and runbooks. |
| `repository_corrections` | Records specification defects that are not implementation choices. |
| `observed_evidence` | Records dated observations without upgrading them into conformance claims. |
| `profile_specific_tests` | Declares additional verification imposed by the profile. |
| `required_decision_records` | Declares ADR/IDR dependencies. |
| `approval` | Records independent review gates. |
| `revision_history` | Records controlled profile evolution. |

## 7. Stable decisions and deployment overlays

The base profile shall contain stable decisions that affect interoperability, trust boundaries, conformance scope, persistence semantics, validation behavior, identity binding, Canonical State locality, or assurance claims.

Mutable environment-specific values belong in controlled deployment overlays or runbooks. Examples include provider account, region, product name, hostnames, IP addresses, certificates, exact software versions, absolute paths, quotas, resource limits, backup schedules, telemetry sinks, service-level objectives, and incident contacts.

A profile may name a current provider product as a deployment overlay, but the profile shall also state the minimum node class and shall not treat provider branding as an AGCP requirement.

## 8. Canonicalization and profile digest

The profile content digest is calculated as follows:

1. parse the YAML into the JSON data model;
2. make a deep copy;
3. remove `document.digest.value` from the copy;
4. serialize the remaining object using RFC 8785 JSON Canonicalization Scheme;
5. hash the canonical UTF-8 bytes with SHA-256; and
6. store the lowercase hexadecimal result in `document.digest.value`.

The digest scope identifier shall be `PROFILE_DOCUMENT_EXCLUDING_DOCUMENT_DIGEST_VALUE`.

## 9. Team workspace and local-runtime rules

A profile that places AGCP in a team workspace shall explicitly identify:

- the workspace platform and provisioning mechanism;
- whether the workspace is individual or shared;
- how individually authenticated students receive access;
- whether the workspace operating-system identity is sufficient for AGCP actor attribution;
- which paths are student-writable and which are operator-protected;
- whether students receive host root, `sudo`, privileged containers, or the host container socket;
- where the governance runtime, Canonical State sources, PEP, governed targets, ledger, and evidence reside; and
- whether a central control node is required for synchronous governance.

A shared shell or shared operating-system account shall not be treated as an authoritative individual actor identity unless an approved identity-binding mechanism establishes the individual subject for each governed operation.

## 10. Scale-out rules

A multi-node profile shall distinguish vertical scale-up from horizontal scale-out. It shall identify stable team-to-node assignment, stateful workspace placement, migration behavior, control-plane dependencies, and whether adding a node interrupts existing workspaces.

Planning capacity is not a conformance claim. Published class capacity requires representative load evidence using the complete workspace image and realistic simultaneous build and multi-agent execution workloads.

## 11. Identity rules

Platform login, workspace access, human runtime identity, and agent identity are separate concerns and shall be represented separately.

Individual student accounts are required. Shared credentials are prohibited. A platform login alone does not prove the human actor represented in an AGCP proposal, approval, activation, or other governed record. The runtime actor token or signature shall bind the subject, team, workspace, audience, issuer, and applicable scopes.

Agent instances shall use distinct registered identities and shall not inherit authority solely from the human account that launched them.

## 12. Canonical State locality

A profile shall state where synchronous Canonical State is resolved. Central reporting, assessment, backup, or administration copies shall not become authoritative merely because they are centralized.

Student submissions and agent reports are commands, claims, or observations until qualified. External sources may be used only through approved adapters that create provenance-bound, freshness-bounded, replayable snapshots.

## 13. Whole-schema-set and runtime validation

A profile that uses AGCP JSON Schemas shall distinguish controlled build processing of the complete pinned schema graph from request-time validation of the operation-specific entry schema and reachable dependencies.

Schema-validator generation is not AGCP Governance Compilation. Governance Compilation and Controlled Governance Activation remain separate processes.

## 14. Lifecycle and approval

Profile lifecycle values are `PROPOSED`, `APPROVED`, `ACTIVE`, `SUPERSEDED`, and `RETIRED`. Profile status values are `DEVELOPMENT_PRE_CONFORMANCE`, `CANDIDATE`, `APPROVED`, and `RETIRED`.

A profile may be structurally valid while remaining proposed or pre-conformance. Approval requires resolution of applicable repository corrections, completion of required decision records, objective verification evidence, and approval of all required review gates.

## 15. Markdown consistency

The Markdown companion shall reproduce, at minimum:

- profile ID, version, lifecycle, and status;
- authoritative YAML filename, schema filename, format version, and canonical digest;
- pinned AGCP baseline and digest;
- conformance posture, scope, exclusions, and intended use;
- node topology and scale-out model;
- team workspace, student access, and privilege model;
- runtime locality and Canonical State model;
- identity and agent-binding model;
- schema validation, persistence, backup, performance, and assurance limitations;
- unresolved decision records and approval gates; and
- revision history.

## 16. Change control

A new profile revision is required for a material change to the execution model, node topology, workspace isolation, identity contract, persistence model, cryptographic contract, public interface mapping, PEM runtime, enforcement boundary, Canonical State model, or production-use authorization.
