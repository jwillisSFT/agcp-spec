# AGCP Versioning and Governance Specification v0.9.0

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  
**Applies To:** All AGCP-conformant implementations

---

# 1. Purpose

This document defines:

- The versioning model for AGCP
- Backward and forward compatibility rules
- Schema and registry version alignment
- Change control requirements
- Governance process for specification evolution
- Namespace management rules
- Conformance impact rules
- Release lifecycle model

This specification ensures that AGCP remains:

- Deterministic
- Interoperable
- Stable across implementations
- Safe for multi-vendor adoption
- Suitable for formal standards governance

---

# 2. Versioning Model

AGCP uses **Semantic Versioning**:

`MAJOR.MINOR.PATCH`

Example:

`0.9.0`

---

## 2.1 MAJOR Version

A **MAJOR version increment** is REQUIRED when:

- A breaking change is introduced
- Required fields are removed
- Required fields are modified
- Behavioral guarantees change
- Determinism guarantees change
- Security guarantees are weakened
- Multitenant isolation semantics change
- PEC input/output contract changes
- Conformance assertion semantics change

MAJOR versions are **NOT required for additive extensions**.

---

## 2.2 MINOR Version

A **MINOR version increment** is REQUIRED when:

- Optional fields are added
- Registry entries are added (non-breaking)
- New endpoints are added (optional)
- Conformance profiles are extended
- New constraint or invariant types are added
- Clarifications that do not alter normative meaning are introduced

MINOR updates **MUST preserve backward compatibility within the same MAJOR series**.

---

## 2.3 PATCH Version

A **PATCH version increment** is REQUIRED when:

- Editorial corrections are made
- Typographical errors are corrected
- Examples are clarified
- Non-normative explanatory content is updated

PATCH updates **MUST NOT alter normative behavior**.

---

# 3. Specification Scope Versioning

The following artifacts **MUST share the same MAJOR.MINOR version**:

- AGCP-Core
- AGCP-HTTP-Interface
- AGCP-PEC
- AGCP-Security-Profile
- AGCP-Multitenant-Profile
- AGCP-Conformance
- AGCP-Versioning-and-Governance

Schemas and registries **MUST align with the same MAJOR.MINOR version**.

PATCH alignment is recommended but **not strictly required if behavior unchanged**.

---

# 4. Schema Version Alignment

All JSON schemas **MUST include**:

`"schema_version": "0.9.0"`

Schema changes:

| Change | Version Impact |
|------|------|
Removing required property | MAJOR increment |
Adding required property | MAJOR increment |
Adding optional property | MINOR increment |
Tightening validation rules | MAJOR increment |
Expanding enum values | MINOR increment (if non-breaking) |

---

# 5. Registry Governance

Registries are **normative artifacts**.

The following registries are Core-managed:

- Rejection Code Registry
- Constraint Type Registry
- Invariant Type Registry

---

## 5.1 Registry Entry Rules

Each registry entry **MUST include**:

- name
- status (ACTIVE \| DEPRECATED \| RETIRED)
- description
- version introduced

Optional:

- parameters_schema (for constraint types)
- http_status (for rejection codes)

---

## 5.2 Registry Status Semantics

**ACTIVE**

Entry may be used in conformance implementations.

**DEPRECATED**

Entry remains valid but **SHOULD NOT be used in new implementations**.

**RETIRED**

Entry **MUST NOT be used in new implementations**.

Implementations **MAY still process legacy artifacts referencing it**.

---

## 5.3 Registry Namespace Rules

Core namespace prefix:

`core.`

Experimental namespace prefix:

`x.`

Vendor namespace prefix:

`vendor.<vendor_name>.`

Core namespace modifications require governance approval.

Vendor namespace entries **do NOT modify Core conformance guarantees**.

---

# 6. Compatibility Rules

## 6.1 Within Same MAJOR

Implementations claiming conformance to MAJOR version **X MUST interoperate with**:

- All MINOR versions within X
- All PATCH versions within X

---

## 6.2 Cross-MAJOR Behavior

An implementation **MUST reject requests specifying unsupported MAJOR version**.

Rejection code:

`UNSUPPORTED_SPEC_VERSION`

---

# 7. Change Control Process

All normative changes **MUST include**:

- Problem statement
- Proposed modification
- Impact analysis
- Schema impact
- Registry impact
- Conformance impact
- Security impact
- Multitenant impact
- Compatibility classification (MAJOR/MINOR/PATCH)
- Migration guidance

Changes **MUST be tracked via versioned release snapshots**.

---

# 8. Conformance Impact Rules

| Change | Version Impact |
|------|------|
Add new rejection codes | MINOR |
Change rejection semantics | MAJOR |
Add new conformance assertions | MINOR |
Remove conformance assertions | MAJOR |
Modify ordering guarantees | MAJOR |

---

# 9. Governance Structure (Standards Process Context)

AGCP governance **SHALL include**:

- Public review process
- Documented ballot mechanism
- Version tagging
- Public issue tracking
- Change logs

Governance model **MUST ensure**:

- Vendor neutrality
- Deterministic stability
- Security-first evolution
- Backward compatibility discipline

---

# 10. Release Lifecycle

Each release **MUST include**:

- Version number
- Release date
- Changelog
- Normative specification set
- Schema bundle
- Registry bundle
- Conformance assertion mapping
- Audit report (recommended)

Release states:

`Draft → Committee Specification → Final Standard`

---

# 11. Experimental Features

Experimental features **MUST**:

- Use `x.` namespace
- Be clearly labeled non-normative
- Not impact Core conformance

Experimental features **MAY be promoted to core namespace via governance vote**.

---

# 12. Deprecation Policy

Deprecation **MUST**:

- Be announced in MINOR release
- Remain valid for at least one additional MINOR cycle
- Provide migration guidance

Removal **requires MAJOR increment**.

---

# 13. Determinism Stability Rule

Any change that impacts:

- PEC input contract
- PEC output contract
- Evaluation ordering
- Invariant enforcement logic
- Multitenant isolation guarantees

**MUST be classified as MAJOR.**

---

# 14. Security Stability Rule

Any change that:

- Weakens signature validation requirements
- Weakens tenant isolation
- Weakens replay protection
- Weakens execution gating
- Weakens ledger immutability

**MUST be classified as MAJOR.**

---

# 15. Documentation Versioning Requirements

Each specification document **MUST include**:

- Version
- Status
- Publication date
- Change history section

Each schema and registry file **MUST include a version identifier**.

---

# 16. Interoperability Guarantees

AGCP guarantees that:

- Conformant implementations of the same MAJOR version can exchange ActionEnvelopes
- Deterministic PEC behavior is preserved across implementations
- Registry semantics remain stable within MAJOR version
- Conformance assertions remain stable within MAJOR version

---

# 17. Non-Goals

This document does **not**:

- Define OASIS procedural mechanics
- Define organizational governance beyond technical version control
- Mandate specific voting thresholds
- Mandate specific repository hosting platforms

---

# 18. Summary

The AGCP Versioning and Governance Specification ensures:

- Predictable evolution
- Interoperability across vendors
- Deterministic stability
- Multitenant safety continuity
- Security guarantee preservation

All AGCP implementations **MUST adhere to this versioning and governance model to claim conformance**.
