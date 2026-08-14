# AGCP Versioning and Governance Specification

**Status:** Normative  
**Repository Versioning:** Repository Release Governed  
**Applies To:** All AGCP-conformant implementations

---

# 1. Purpose

This specification defines the versioning, compatibility, and governance model for the Autonomous Governance Control Plane (AGCP).

It establishes the rules governing:

- specification versioning;
- repository releases;
- compatibility;
- schema evolution;
- registry management;
- change control;
- conformance impact;
- governance processes; and
- interoperability across implementations.

The objectives of this specification are to ensure that AGCP remains:

- deterministic;
- interoperable;
- implementation independent;
- stable across repository releases;
- suitable for multi-vendor adoption; and
- suitable for long-term standards governance.

---

# 2. Repository Versioning

AGCP is published as a versioned repository.

A repository release represents the authoritative collection of:

- normative specifications;
- schemas;
- registries;
- conformance artifacts;
- reference documentation;
- lifecycle documentation; and
- supporting implementation guidance.

Repository releases define the complete set of artifacts applicable to a particular AGCP release.

Individual informative documents MAY evolve independently provided they remain consistent with the repository release in which they are published.

---

# 3. Semantic Versioning Model

Repository releases use Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

Example:

```text
0.9.0
```

The version number applies to the repository release as a whole rather than requiring identical embedded version numbers within every document.

## 3.1 Authoritative repository release-number source

The root `VERSION` file SHALL be the sole maintained source of the current AGCP repository release number. It contains bare Semantic Versioning form (`MAJOR.MINOR.PATCH`). Build and validation tooling SHALL derive release-tag form (`vMAJOR.MINOR.PATCH`), RTM specification-version form (`v.MAJOR.MINOR.PATCH`), release identifiers, and generated release-specific report filenames from that value.

Historical release records SHALL retain the release identity under which they were published and SHALL NOT be rewritten solely because the current `VERSION` value changes.


---

# 4. Version Classification

## 4.1 MAJOR Version

A MAJOR version increment is REQUIRED whenever one or more of the following occur:

- breaking specification changes;
- removal of required schema properties;
- modification of required schema semantics;
- changes to deterministic governance behavior;
- changes to Proposal Qualification semantics;
- changes to Governance Decision semantics;
- changes to Human Review semantics;
- changes to Execution Authorization semantics;
- changes to Commit Boundary semantics;
- changes to Canonical State derivation;
- changes to Governance Evidence semantics;
- changes to ordered Append-Only Governance Ledger semantics;
- weakening of security guarantees;
- weakening of multitenant isolation guarantees;
- incompatible changes to conformance requirements.

MAJOR version increments are not required for purely additive, backward-compatible extensions.

---

## 4.2 MINOR Version

A MINOR version increment is REQUIRED when:

- optional schema properties are added;
- new registries are introduced;
- registry entries are added without breaking compatibility;
- optional endpoints are introduced;
- new governance capabilities are added without altering existing behavior;
- new conformance profiles are introduced;
- clarifications are added that do not change normative meaning.

MINOR releases SHALL preserve backward compatibility within the same MAJOR version.

---

## 4.3 PATCH Version

A PATCH version increment is REQUIRED for:

- editorial corrections;
- typographical corrections;
- documentation improvements;
- clarification of examples;
- non-normative explanatory updates.

PATCH releases SHALL NOT alter normative implementation behavior.

---

# 5. Compatibility Model

## 5.1 Repository Compatibility

Artifacts within a repository release are intended to operate together as a coherent specification set.

Implementations claiming conformance SHOULD implement artifacts from a single repository release whenever practical.

---

## 5.2 Same-Major Compatibility

Implementations conforming to a particular MAJOR version SHALL interoperate with:

- all MINOR releases of that MAJOR version; and
- all PATCH releases of that MAJOR version,

subject to optional capability negotiation where applicable.

---

## 5.3 Cross-Major Compatibility

Implementations SHALL reject requests requiring unsupported MAJOR versions.

The appropriate rejection code SHALL be defined by the published rejection-code registry.

Cross-major interoperability is not guaranteed.

---

# 6. Specification Alignment

The following controlled artifact families SHALL remain aligned within the same repository release:

- AGCP Core Specification
- AGCP HTTP Interface Specification
- Policy Evaluation Contract and applicable controlled machine-contract companions
- AGCP Provenance Wire Format Specification
- AGCP Multitenant Operational Specification
- AGCP Error Mapping
- Append-Only Governance Ledger Specification
- AGCP Human Adjudication and Governance Approval Specification
- active governance schemas, including DS-020 Governance Evidence and DS-033 Evidence Qualification Result
- Conformance Specifications and executable conformance assets

Normative schemas and registries SHALL remain consistent with the repository release in which they are published.

### 6.1 Normative reference integrity

Every normative reference SHALL identify an existing controlled repository artifact by canonical title and path or an explicitly identified external normative source. A subject-area label SHALL NOT be written as though it were a standalone companion when no such artifact is published. Distributed obligations SHALL reference the applicable controlling artifacts identified in `AGCP-Normative-Companion-Reference-Dispositions.md`.

PATCH-level editorial updates MAY occur independently provided normative behavior remains unchanged.

---

# 7. Registry Governance

Normative registries are authoritative components of the AGCP repository.

Registries provide stable identifiers, controlled vocabularies, and machine-readable metadata that support interoperability and deterministic governance behavior.

Core-managed registries include, where applicable:

- Rejection Code Registry
- Constraint Type Registry
- Invariant Type Registry
- Governance Stage Registry
- Governance Evidence Type Registry
- Human Review Role Registry

Additional registries MAY be introduced in future repository releases provided they comply with the compatibility rules defined by this specification.

---

## 7.1 Registry Entry Requirements

Each registry entry SHALL include, at a minimum:

- identifier;
- name;
- status;
- description;
- repository release introduced.

Additional metadata MAY include:

- parameters schema;
- associated specification;
- applicable interfaces;
- associated Governance Domains;
- associated conformance requirements.

Registry entries SHALL remain uniquely identifiable across repository releases.

---

## 7.2 Registry Status

Registry entries SHALL use one of the following lifecycle states.

### ACTIVE

The entry is approved for use by conformant implementations.

### DEPRECATED

The entry remains valid for compatibility purposes but SHOULD NOT be used in new implementations.

Migration guidance SHOULD be provided.

### RETIRED

The entry SHALL NOT be used in new implementations.

Implementations MAY continue to recognize retired entries when processing historical artifacts or maintaining backward compatibility.

---

## 7.3 Registry Namespace Rules

Core-managed registry identifiers SHALL occupy the core namespace.

Experimental identifiers SHALL use the `x.` namespace.

Vendor-specific identifiers SHALL use a vendor-qualified namespace.

Example:

```text
vendor.example.constraint.example_constraint
```

Vendor namespaces SHALL NOT modify or redefine Core registry semantics.

---

# 8. Schema Governance

Normative schemas SHALL evolve in a manner consistent with the compatibility guarantees defined by this specification.

Schema evolution SHALL preserve deterministic interoperability across conformant implementations.

## 8.1 Version Alignment

Normative schemas SHALL remain aligned with the repository release in which they are published.

Schemas MAY include explicit schema version metadata where appropriate.

## 8.2 Compatibility Rules

Typical compatibility classifications include:

| Schema Change | Version Impact |
|---------------|----------------|
| Remove required property | MAJOR |
| Add required property | MAJOR |
| Add optional property | MINOR |
| Tighten validation constraints | MAJOR |
| Expand enumerated values without breaking compatibility | MINOR |
| Editorial clarification | PATCH |

Implementations SHOULD reject schema versions that are incompatible with their supported repository release.

---

# 9. Change Control Process

Normative changes SHALL follow a documented governance process.

Each proposed normative change SHOULD include:

- problem statement;
- proposed modification;
- rationale;
- specification impact;
- schema impact;
- registry impact;
- conformance impact;
- security impact;
- multitenant impact;
- compatibility classification;
- migration guidance.

Repository releases SHALL preserve an auditable history of normative changes.

---

## 9.1 Change Classification

Each approved change SHALL be classified as:

- MAJOR;
- MINOR; or
- PATCH,

consistent with the Semantic Versioning model defined by this specification.

---

## 9.2 Repository Snapshots

Each repository release SHOULD preserve an immutable snapshot of:

- normative specifications;
- schemas;
- registries;
- conformance artifacts;
- reference documentation.

Repository snapshots support reproducibility, deterministic conformance testing, and long-term interoperability.

---

# 10. Conformance Impact Rules

Changes affecting conformance SHALL be evaluated for compatibility impact.

Typical classifications include:

| Change | Version Impact |
|--------|----------------|
| Add new Normative Statements | MINOR |
| Remove or modify Normative Statements | MAJOR |
| Add new Conformance Requirements | MINOR |
| Remove or modify Conformance Requirements | MAJOR |
| Add new Test Cases without changing existing behavior | MINOR |
| Modify Test Case behavior affecting normative verification | MAJOR |
| Add new Harness Checks | MINOR |
| Modify Harness Checks affecting normative verification | MAJOR |
| Modify deterministic governance ordering | MAJOR |
| Modify Canonical State derivation semantics | MAJOR |
| Modify Governance Evidence semantics | MAJOR |
| Modify ordered Append-Only Governance Ledger semantics | MAJOR |

Conformance artifacts SHALL remain traceable through the normative conformance model:

```text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
        |
        v
Harness Check
        |
        v
Harness Test Vector
```

---

# 11. Governance Process

The AGCP governance process SHALL support the orderly evolution of the specifications while preserving interoperability and deterministic behavior.

Repository governance SHOULD include:

- public review;
- documented issue tracking;
- repository release tagging;
- published change history;
- documented approval process.

The governance process SHALL preserve:

- vendor neutrality;
- deterministic behavior;
- backward compatibility discipline;
- security-first evolution;
- transparent technical decision making.

Repository governance defines how specifications evolve.

It does not prescribe the governance structure of any particular standards organization.

---

# 12. Release Lifecycle

Each repository release SHALL include, at a minimum:

- repository release identifier;
- publication date;
- release notes;
- normative specification set;
- schema bundle;
- registry bundle;
- conformance artifact bundle;
- reference documentation;
- lifecycle documentation.

Where applicable, a repository release SHOULD also include:

- implementation guidance;
- audit report;
- migration guidance;
- known compatibility considerations.

Repository releases represent immutable snapshots of the AGCP specification.

---

## 12.1 Release States

Repository releases MAY progress through lifecycle states including:

```text
Draft
    ↓
Public Review
    ↓
Committee Specification
    ↓
Release Candidate
    ↓
Final Standard
```

Alternative release processes MAY be used by adopting organizations provided that published repository releases remain stable and reproducible.

---

# 13. Experimental Features

Experimental capabilities enable architectural innovation while preserving normative interoperability.

Experimental features SHALL:

- be clearly identified as experimental;
- remain outside normative conformance requirements;
- avoid modifying normative Core semantics;
- preserve deterministic externally observable behavior.

Experimental features SHOULD use the `x.` namespace.

Experimental features MAY be promoted into the Core through the documented repository governance process.

Promotion of an experimental capability into the Core SHALL follow the compatibility rules defined by this specification.

---

# 14. Deprecation Policy

Normative specifications, schemas, registries, interfaces, and conformance artifacts MAY be deprecated.

Deprecation SHALL:

- be announced in a MINOR repository release;
- include migration guidance;
- remain supported for at least one subsequent MINOR release unless an exceptional security issue requires earlier removal.

Removal of normative behavior SHALL require a MAJOR repository release.

Historical repository releases SHALL remain available for interoperability and audit purposes where practical.

---

# 15. Determinism Stability Rule

Deterministic governance behavior is a foundational architectural guarantee of AGCP.

Any change affecting one or more of the following SHALL be classified as a MAJOR change:

- Proposal Qualification semantics;
- Governance Decision Function semantics;
- Human Review semantics;
- Execution Authorization semantics;
- Commit Boundary semantics;
- governance progression ordering;
- Canonical State derivation;
- Governance Evidence semantics;
- ordered Append-Only Governance Ledger semantics;
- deterministic replay behavior;
- multitenant isolation guarantees;
- Governance Domain isolation semantics.

Repository evolution SHALL preserve deterministic externally observable governance behavior across conformant implementations within the same MAJOR version.

---

# 16. Security Stability Rule

Security guarantees are normative architectural guarantees.

Changes that weaken one or more of the following SHALL require a MAJOR repository release:

- provenance validation;
- cryptographic verification;
- replay protection;
- tenant isolation;
- Governance Domain isolation;
- Human Review integrity;
- Execution Authorization integrity;
- Commit Boundary validation;
- Governance Evidence integrity;
- ordered Append-Only Governance Ledger integrity;
- Canonical State integrity.

Security enhancements that strengthen existing guarantees without breaking compatibility MAY be introduced in MINOR releases.

---

# 17. Documentation Requirements

Normative specifications SHALL include, where applicable:

- document title;
- status;
- repository versioning information;
- purpose;
- scope;
- normative content.

Publication metadata MAY additionally include:

- publication date;
- document history;
- repository release reference.

Normative schemas and registries SHOULD include sufficient metadata to identify the repository release with which they are associated.

Informative documentation MAY evolve independently provided that it remains consistent with the repository release in which it is published.

---

# 18. Repository Documentation

A repository release SHOULD include documentation sufficient to support:

- implementation;
- conformance testing;
- interoperability;
- governance review;
- security assessment;
- architectural understanding.

Typical documentation includes:

- normative specifications;
- lifecycle documentation;
- conformance documentation;
- implementation guidance;
- reference documentation;
- research publications.

Only the normative specifications define implementation requirements.

All other documentation is informative unless explicitly stated otherwise.

---

# 19. Interoperability Guarantees

AGCP is designed to support interoperable governance processing across conformant implementations.

Conformant implementations of the same MAJOR repository release SHALL preserve equivalent externally observable governance behavior.

Interoperability guarantees include:

- consistent Proposal processing;
- deterministic governance progression;
- consistent Proposal Qualification behavior;
- consistent Governance Decision Function behavior;
- consistent Human Review behavior;
- consistent Execution Authorization behavior;
- consistent Commit Boundary behavior;
- equivalent Canonical State derivation;
- equivalent Governance Evidence semantics;
- equivalent ordered Append-Only Governance Ledger semantics;
- deterministic replay using equivalent authoritative inputs.

Implementation architecture, programming language, storage technology, deployment model, and execution platform MAY differ provided these externally observable guarantees are preserved.

---

# 20. Repository Governance

The AGCP repository is the authoritative publication mechanism for the specification.

Repository governance SHALL ensure that:

- normative specifications remain internally consistent;
- schemas remain aligned with normative behavior;
- registries remain authoritative and version controlled;
- conformance artifacts remain traceable to the normative specifications;
- informative documentation remains consistent with the published architecture.

Normative specifications define implementation requirements.

Schemas define normative data structures.

Registries define controlled vocabularies and stable identifiers.

Conformance artifacts verify implementation behavior.

Reference, lifecycle, implementation guidance, and research documents provide informative architectural support and SHALL NOT introduce additional normative requirements unless explicitly designated as normative.

---

# 21. Relationship to Other Specifications

This specification defines the governance model for repository evolution.

It complements, but does not replace, the following controlled artifacts:

- the AGCP Core Specification (`../spec/AGCP-Core.docx`)
- the AGCP HTTP Interface Specification (`../spec/AGCP-HTTP-Interface-Specification.md`)
- the Policy Evaluation Contract (`../spec/AGCP-Policy-Evaluation-Contract.md`)
- the AGCP Provenance Wire Format Specification (`../spec/AGCP-Provenance-Wire-Format-Specification.md`)
- the AGCP Multitenant Operational Specification (`../spec/AGCP-Multitenant-Operational-Specification.md`)
- AGCP Error Mapping (`../spec/AGCP-Error-Mapping.md`)
- DS-020 Governance Evidence (`../schemas/governance_evidence.json`)
- DS-033 Evidence Qualification Result (`../schemas/evidence_qualification_result.json`)
- the Append-Only Governance Ledger Specification (`../spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`)
- the AGCP Human Adjudication and Governance Approval Specification (`../spec/AGCP-Human-Review-Specification.md`)
- the AGCP Conformance Specification (`../conformance/AGCP-Conformance.md`)

All specifications within a repository release SHALL be interpreted as a coherent specification set.

Where inconsistencies exist, they SHALL be resolved using the Core-defined precedence order: published CRs; Core Specification; applicable normative Companion Specifications expressly adopted by the implementation profile; Implementation Profiles; Conformance Test Suite; and Reference Implementations. The ARM SHALL govern architectural terminology and concept meaning where an ARM-defined concept is used, without independently creating a conformance obligation. Normative Statements and the RTM support extraction and traceability and do not supersede the normative sources.

---

# 22. Non-Goals

This specification does not:

- define the governance structure of any particular standards organization;
- prescribe organizational voting procedures;
- require a particular repository hosting platform;
- mandate a specific software development workflow;
- require a particular release cadence;
- define implementation-specific deployment architectures.

These matters remain the responsibility of the organizations adopting, publishing, or implementing AGCP.

---

# 23. Summary

This specification establishes the versioning and governance model for the Autonomous Governance Control Plane.

It defines:

- repository versioning;
- Semantic Versioning rules;
- compatibility classifications;
- registry governance;
- schema governance;
- change control;
- repository governance;
- conformance impact classification;
- interoperability guarantees; and
- long-term specification stability.

Together with the other normative AGCP specifications, this specification provides a stable foundation for deterministic governance processing, interoperable implementations, and long-term evolution of the AGCP standard.

Conformant implementations SHALL adhere to this versioning and governance model when claiming conformance to an AGCP repository release.
