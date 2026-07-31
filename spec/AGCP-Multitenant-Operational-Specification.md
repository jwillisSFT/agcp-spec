# AGCP Multitenant Operational Specification

**Status:** Normative

## 1. Purpose

This specification defines the mandatory multitenant operational
requirements for AGCP-conformant implementations.

It establishes normative requirements for:

-   Tenant lifecycle management
-   Governance Domain isolation
-   Namespace isolation
-   Governance artifact scoping
-   Cross-domain trust
-   Resource isolation
-   Governance Evidence preservation
-   Administrative isolation
-   Multitenant conformance

Multitenancy is a normative behavioral guarantee and SHALL NOT depend on
deployment architecture.

## 2. Tenant Definition

A tenant is an isolated governance namespace containing its own:

-   Governance Policy registry
-   Constraint registry
-   Invariant registry
-   Exception registry
-   Policy Evaluation Modules
-   Governance Configuration
-   Authority Lineage
-   Governance Evidence namespace
-   Execution Authorization boundary
-   Governance Domain configuration

Each tenant SHALL be uniquely identified by `tenant_id`.

## 3. Tenant Lifecycle

### States

-   PROVISIONED
-   ACTIVE
-   SUSPENDED
-   DECOMMISSIONED

### PROVISIONED

-   Namespace created
-   Governance artifacts may be initialized
-   Proposal submission SHALL be rejected

### ACTIVE

-   Governance artifacts may be managed
-   Proposals may be submitted
-   Governed human adjudication and Governance Approval may occur
-   Execution Authorization and Commit Boundary processing are permitted

### SUSPENDED

-   Proposal submission SHALL be rejected
-   Execution Authorization SHALL be rejected
-   Commit Boundary processing SHALL be rejected
-   Governance Evidence remains readable

### DECOMMISSIONED

-   Governance artifacts become immutable
-   Proposal submission SHALL be rejected
-   Execution Authorization SHALL be rejected
-   Commit Boundary processing SHALL be rejected
-   Governance Evidence SHALL remain available

State transitions SHALL be authorized, validated, and produce Governance
Evidence.

## 4. Namespace Isolation

Every governance artifact SHALL be tenant-scoped, including:

-   Proposal
-   Governance Policy
-   Policy Evaluation Module
-   Constraint Artifact
-   Invariant Definition
-   Exception Artifact
-   Governance Approval Artifact
-   Execution Authorization
-   Commit Boundary Result
-   Governance Evidence

Resolution of governance artifacts, Governance Configuration, Authority
Lineage, and Governance Evidence SHALL remain tenant scoped.

Cross-tenant access SHALL be rejected unless explicitly authorized by a
valid Governance Trust Artifact.

## 5. Identifier Uniqueness

Within a tenant namespace, identifiers such as `proposal_id`,
`policy_id`, `constraint_id`, `invariant_id`, `exception_id`,
`authorization_id`, `artifact_id`, and `governance_evidence_id` SHALL be
unique.

Global uniqueness across tenants is not required.

## 6. Governance Trust Artifacts

Cross-tenant or cross-Governance Domain operations are prohibited by
default.

Such operations SHALL require a Governance Trust Artifact defining:

-   source tenant and Governance Domain
-   target tenant and Governance Domain
-   authorized operations
-   authorized governance surfaces
-   authority limits
-   expiration
-   provenance
-   signature

Validation SHALL verify authorization, scope, provenance, signature, and
expiration.

Authorized cross-boundary operations SHALL produce Governance Evidence
in each participating governance domain.

## 7. Resource Isolation

Implementations SHALL support:

-   per-tenant rate limiting
-   concurrent proposal processing limits
-   storage partitioning
-   Policy Evaluation Module isolation
-   Governance Evidence isolation

Resource exhaustion in one tenant SHALL NOT compromise another.

## 8. Data Protection

Implementations SHOULD support tenant-specific encryption keys and
governance-domain isolation of cryptographic material.

## 9. Preservation and Archival

Transition to DECOMMISSIONED SHALL preserve Governance Evidence and
governance artifacts.

Implementations using append-only ledgers SHALL preserve corresponding
ledger records.

## 10. Cross-Tenant Attack Mitigation

Implementations SHALL prevent:

-   tenant enumeration
-   cross-tenant replay
-   governance artifact injection
-   Authority Lineage spoofing
-   Governance Context substitution
-   Governance Evidence forgery

## 11. Administrative Isolation

Administrative operations SHALL be authenticated, authorized, tenant
scoped, and generate Governance Evidence.

Global administration SHALL NOT bypass tenant isolation guarantees.

## 12. Deployment Independence

Logical isolation requirements SHALL hold regardless of infrastructure,
database, process, or regional deployment model.

## 13. Side-Channel Protection

Implementations SHOULD minimize information leakage through timing
differences, cache sharing, and error reporting.

## 14. Conformance

Conformant implementations SHALL demonstrate:

-   tenant isolation
-   Governance Domain isolation
-   governance artifact isolation
-   Governance Evidence isolation
-   Governance Trust Artifact enforcement
-   resource isolation
-   cross-tenant negative testing appropriate to the claimed conformance
    profile

## 15. Repository Versioning

Repository releases govern versioning of this specification.

## 16. Summary

This specification guarantees:

-   deterministic tenant scoping
-   Governance Domain isolation
-   governance artifact isolation
-   controlled cross-boundary governance
-   Governance Evidence preservation
-   implementation-independent multitenant behavior
