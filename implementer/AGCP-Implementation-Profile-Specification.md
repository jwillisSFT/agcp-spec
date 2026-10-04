# AGCP Implementation Profile Specification

**Status:** Controlled implementer specification  
**Profile Format Version:** 2.0.0  
**Repository Release Target:** AGCP v2.1.x

## 1. Purpose

An AGCP Implementation Profile declares how one implementation realizes the implementation-selectable portions of the AGCP architecture and normative specification. It binds a concrete runtime to controlled choices without weakening higher-precedence CR, Core, or adopted companion requirements.

The profile is generic with respect to customer, course, hosting provider, product, and deployment name. Deployment-specific profiles may be distributed separately.

## 2. Authority and precedence

An Implementation Profile is subordinate to published CRs, AGCP Core, and applicable adopted normative Companion Specifications. It SHALL NOT create an interpretation that weakens or contradicts those sources.

The Architecture Reference Model and AGCP Trust Model define architectural vocabulary and trust relationships. They do not independently create conformance obligations.

## 3. Required package

A controlled implementation profile package SHALL contain:

- authoritative YAML data conforming to `AGCP-Implementation-Profile-Schema.json`;
- a human-readable Markdown rendering carrying the same decisions;
- profile identity and semantic version;
- AGCP baseline identity;
- canonical digest; and
- references to controlled subordinate profiles required by the implementation.

Subordinate profile types standardized by this repository are:

1. Identity and Authorization Store (IAS) Profile; and
2. PEP Profile.

## 4. Artifact responsibilities

### 4.1 Format specification

This document defines the profile-format semantics.

### 4.2 JSON Schema

`AGCP-Implementation-Profile-Schema.json` defines machine-validatable structure for format 2.0.0.

### 4.3 YAML profile

YAML is the authoritative human-editable representation for controlled deployment profiles unless a published profile states another controlled representation.

### 4.4 Markdown profile

Markdown is the human-readable rendering and SHALL NOT contradict the authoritative data representation.

## 5. Data-model rules

Profiles SHALL:

- use stable field names;
- set explicit values for security- and conformance-significant choices;
- reference secrets rather than embed them;
- identify external controlled artifacts by identity/version/digest where integrity matters;
- distinguish normative AGCP requirements from implementation choices; and
- declare failure behavior for unavailable or unverifiable required dependencies.

## 6. Required top-level sections

Format 2.0.0 requires:

- document;
- profile;
- baseline;
- conformance;
- intended_use;
- implementation;
- deployment_topology;
- assurance_boundary;
- interfaces;
- trust_boundaries;
- governance_functions;
- identity_and_authorization;
- cryptography;
- canonical_state;
- schema_validation;
- compilation_and_activation;
- pem_runtime;
- enforcement;
- persistence;
- background_processing;
- idempotency;
- validation_pipeline;
- http;
- reevaluation;
- metadata;
- backup_and_recovery;
- performance_qualification;
- operational_values;
- repository_corrections;
- observed_evidence;
- profile_specific_tests;
- required_decision_records;
- approval; and
- revision_history.

## 7. Stable decisions and deployment overlays

The base profile SHALL contain stable implementation decisions. Environment-specific addresses, capacity values, secret references, and deployment overlays MAY be separated provided the controlling profile identifies their authority and precedence.

An overlay SHALL NOT change the semantic identity of the profile without the change-control process required by Section 16.

## 8. Canonicalization and profile digest

The profile SHALL define its canonicalization and content-digest rules. Format 2.0.0 uses RFC 8785 JCS over the authoritative normalized profile representation unless a future profile-format version states otherwise.

The digest SHALL bind every security- or conformance-significant profile decision except the digest value itself.

## 9. Deployment and runtime boundary

The profile SHALL identify:

- deployment pattern and runtime units;
- process/service placement relevant to AGCP functions;
- network or IPC trust boundaries relevant to the claim;
- persistent-state boundaries;
- operator-managed and external-provider-managed responsibilities; and
- explicit exclusions from the assurance claim.

AGCP does not require a particular host, cloud, container platform, IDE, workspace product, or orchestration technology.

## 10. Governance function placement

The profile SHALL declare the placement of:

- Proposal Qualification;
- Governance Decision Function / PDP;
- Execution Authorization;
- Governance Realization Function (GRF);
- PEP; and
- governed target/adapter.

The profile SHALL state whether GDF/PDP and GRF are co-located or independently deployed. If they cross an authentication boundary, the profile SHALL identify the protected interface and workload-identity requirements.

Co-location SHALL NOT collapse their logical responsibilities.

## 11. Identity and authorization rules

The profile SHALL identify authentication mechanisms for relevant human and workload principals and SHALL reference an IAS Profile when governance-significant identity-system authorization or entitlement information is used.

The IAS Profile may resolve identity, account state, Tenant/Domain membership, roles, groups, entitlements, reviewer classes, governance permissions, scopes, delegation/authority attributes, and validity.

IAS authorization/entitlement data is governance input. It is not AGCP Execution Authorization and does not itself produce a Governance Decision.

The profile SHALL define where IAS resolution occurs, required freshness, failure behavior, and which functions consume the qualified result.

## 12. Canonical State locality

The profile SHALL identify authoritative Canonical State source classes, qualification boundaries, freshness rules, conflict policy, and locality/remote-resolution assumptions relevant to deterministic governance.

## 13. Whole-schema-set and runtime validation

The profile SHALL identify the schema set and validator set used by the implementation and any integrity bindings exposed through runtime metadata.

## 14. Lifecycle and approval

The profile SHALL declare supported lifecycle capabilities, human-review behavior, commitment semantics, and whether commitment and target execution are atomic or distinct.

When human approval is supported, the profile SHALL bind approval identity/eligibility to the IAS Profile and the Human Adjudication and Governance Approval Specification.

## 15. Enforcement realization and PEP Profiles

For every governed consequence in claimed enforcement scope, the profile SHALL identify the applicable PEP and reference one or more controlled PEP Profiles.

The profile SHALL define deterministic PEP Profile selection using governance-controlled information. A proposer SHALL NOT be able to select a broader/weaker PEP Profile arbitrarily.

The profile SHALL define:

- GRF-to-PEP authentication/trust requirements;
- PEP endpoint/interface binding;
- PEP-to-target authority boundary;
- target credential references;
- non-bypassability scope;
- commitment versus asynchronous execution semantics; and
- evidence/receipt expectations.

The GRF applies the PEP Profile. The PEP Profile SHALL NOT reinterpret or widen the Governance Decision or commit-eligible transition.

## 16. Change control

A profile version change is required when a security-, conformance-, or interoperability-significant decision changes, including:

- IAS Profile identity/version/digest;
- authoritative identity/entitlement source or mapping;
- GDF/PDP or GRF placement/trust boundary;
- PEP Profile identity/version/digest or selection logic;
- action/target enforcement mapping;
- PEP-to-target authority;
- canonical-state source or conflict rules;
- policy/PEM execution contract;
- cryptographic trust anchors or required algorithms;
- commitment semantics; or
- claimed enforcement/conformance scope.

Backward-compatible editorial changes may use a patch increment. Changes to required data-model structure require a profile-format version change.
