# AGCP Multitenant Operational Profile v0.9.0

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  
**Applies To:** All AGCP-conformant implementations

---

# 1. Purpose

This document defines the multitenant operational requirements for AGCP implementations.

It specifies:

- Tenant lifecycle model
- Namespace isolation guarantees
- Cross-tenant trust artifact model
- Resource isolation requirements
- Artifact scoping rules
- Tenant deletion and archival semantics
- Conformance expectations for L5

Multitenancy in AGCP is **not an implementation detail**. It is a **normative behavioral guarantee**.

---

# 2. Tenant Definition

A tenant is a logically isolated governance namespace containing its own:

- Policy registry
- Constraint registry
- Invariant registry
- Exception registry
- Policy modules
- Ledger namespace
- Execution authorization boundary
- Trust root or trust namespace

Each tenant **MUST** be uniquely identified by:

```
tenant_id (string)
```

---

# 3. Tenant Lifecycle Model

## 3.1 Tenant States

A tenant **SHALL** exist in one of the following states:

- PROVISIONED
- ACTIVE
- SUSPENDED
- DECOMMISSIONED

---

## 3.2 State Semantics

### PROVISIONED

- Namespace created
- Registries empty or uninitialized
- Action submission **MUST** be rejected

---

### ACTIVE

- Policy modules may be registered
- Policies may be activated
- Actions may be submitted
- Execution commits permitted

---

### SUSPENDED

- Action submission **MUST** be rejected
- Execution commits **MUST** be rejected
- Ledger read permitted

---

### DECOMMISSIONED

- Action submission **MUST** be rejected
- Execution commits **MUST** be rejected
- Registry mutation **MUST** be rejected
- Ledger **MUST** remain readable
- Ledger **MUST NOT** be deleted

---

## 3.3 State Transition Requirements

State transitions **MUST**:

- Be authorized
- Be validated
- Be ledger-recorded

Invalid transitions **MUST** return:

```
TENANT_STATE_INVALID
```

---

# 4. Namespace Isolation Requirements

## 4.1 Artifact Scoping

The following objects **MUST** include `tenant_id`:

- ActionEnvelope
- PolicyArtifact
- ConstraintArtifact
- InvariantDefinition
- ExceptionArtifact
- LedgerEntry
- CosignToken
- PolicyModule

---

## 4.2 Resolution Isolation

An AGCP implementation **MUST** ensure:

- Policy resolution is tenant-scoped
- Constraint resolution is tenant-scoped
- Invariant resolution is tenant-scoped
- Exception resolution is tenant-scoped
- Policy module resolution is tenant-scoped
- Ledger reads are tenant-scoped

---

## 4.3 Cross-Tenant Access Prohibition

Absent a valid trust artifact (Section 6), any cross-tenant reference **MUST** result in:

```
HTTP 403
TENANT_SCOPE_VIOLATION
```

Cross-tenant inference via error messages **MUST NOT** reveal tenant existence.

---

# 5. Identifier Uniqueness

Within a tenant namespace:

- `action_id` **MUST** be unique
- `policy_id` **MUST** be unique
- `constraint_id` **MUST** be unique
- `invariant_id` **MUST** be unique
- `exception_id` **MUST** be unique
- `ledger_entry_ref` **MUST** be unique

Global uniqueness across tenants is **NOT** required.

---

# 6. Cross-Tenant Trust Artifact Model

Cross-tenant operations are **prohibited by default**.

They are permitted only via a **Cross-Tenant Trust Artifact**.

---

## 6.1 Trust Artifact Structure

A Cross-Tenant Trust Artifact **MUST** include:

- `artifact_id`
- `source_tenant_id`
- `target_tenant_id`
- `allowed_operations` (array)
- `allowed_surfaces` (array)
- `authority_limits`
- `expiration`
- `signature`
- `timestamp`

---

## 6.2 Trust Artifact Validation

An implementation **MUST** verify:

- Signature validity
- Expiration not exceeded
- Operation permitted
- Surface permitted
- Tenant scope matches

Invalid trust artifact **MUST** result in:

```
TENANT_SCOPE_VIOLATION
```

---

## 6.3 Ledger Recording

All cross-tenant operations **MUST**:

- Be explicitly recorded in both tenants’ ledgers
- Include trust artifact reference

---

# 7. Resource Isolation Requirements

AGCP implementations **MUST** support capability for:

- Per-tenant submission rate limiting
- Per-tenant concurrent action limits
- Per-tenant storage partitioning
- Per-tenant policy module isolation
- Per-tenant ledger storage partitioning

Resource exhaustion in one tenant **MUST NOT** affect others.

---

# 8. Data Residency & Encryption

Implementations **SHOULD**:

- Support per-tenant encryption keys
- Support tenant-partitioned encryption domains

Encryption domain sharing across tenants **MUST NOT** enable cross-tenant data access.

---

# 9. Tenant Deletion & Archival

Deletion **SHALL** be logical, not physical.

When a tenant transitions to **DECOMMISSIONED**:

- All registries become immutable
- Execution disabled
- Ledger preserved
- Policy modules preserved
- Trust artifacts preserved

Hard deletion of ledger entries **MUST NOT** occur under Core conformance.

---

# 10. Cross-Tenant Attack Mitigations

Implementations **MUST** prevent:

- Tenant enumeration via response timing
- Tenant enumeration via error messaging
- Cross-tenant replay
- Cross-tenant policy injection
- Cross-tenant ledger reads

---

# 11. Conformance Requirements for L5

To claim **L5 conformance**, implementation **MUST** demonstrate:

- Strict namespace isolation
- Cross-tenant negative test pass
- Trust artifact enforcement
- Resource isolation capability
- Ledger namespace partitioning

Failure of any cross-tenant negative test **invalidates L5 claim**.

---

# 12. Administrative Isolation

Administrative operations **MUST**:

- Be tenant-scoped
- Be authenticated
- Be authorized
- Be ledger-recorded

Global administrative controls **MUST NOT** bypass tenant isolation guarantees.

---

# 13. Multi-Region and Deployment Models

AGCP does **not** mandate:

- Separate physical infrastructure per tenant
- Separate database per tenant
- Separate process per tenant

However, logical isolation requirements **MUST hold regardless of deployment model**.

---

# 14. Side-Channel Considerations

Implementations **SHOULD**:

- Avoid response time discrepancies based on tenant existence
- Avoid exposing tenant identifiers in error messages
- Avoid shared cache leakage across tenants

---

# 15. Versioning Impact

Changes to multitenant isolation semantics require:

```
MAJOR version increment
```

Additions of optional isolation mechanisms require:

```
MINOR version increment
```

---

# 16. Summary

The AGCP Multitenant Operational Profile guarantees:

- Strong logical isolation
- Deterministic tenant scoping
- Trust artifact–controlled cross-tenant operations
- Resource containment
- Immutable tenant ledger preservation

These guarantees are required for secure multitenant AI governance.
