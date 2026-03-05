# AGCP Implementation Decision Record Template

Status: Informational (Non-Normative)

## Purpose

This document provides a structured questionnaire for organizations implementing the Governance Control Plane Architecture (AGCP).

The questions identify key architectural, operational, and security decisions that must be resolved when designing an AGCP implementation.

The answers form an **Implementation Decision Record (IDR)** documenting how a specific deployment satisfies AGCP requirements.

This document is **informational** and does not modify or extend the AGCP normative specifications.

---

# Implementation Record

Implementation Name:

Organization:

Target AGCP Specification Version:

Implementation Conformance Target:
- Reference Implementation
- Production Implementation
- Both

Deployment Environment:

Primary Architects:

Date:

---

# Section 1 – Scope & Conformance Posture

## Decision 1.1 – Conformance Level

Question  
Target conformance level: Reference Implementation, Production Implementation, or both?

Implementation Decision

Rationale

---

## Decision 1.2 – Deployment Mode

Question  
Deployment mode: single-tenant, multi-tenant, or both?

Implementation Decision

Rationale

---

## Decision 1.3 – Target Platform

Question  
Target platform: Kubernetes, VM/service, Docker, serverless, other?

Implementation Decision

Rationale

---

## Decision 1.4 – Compliance Constraints

Question  
Any hard compliance constraints (FIPS, FedRAMP-like, air-gapped, etc.)?

Implementation Decision

Rationale

---

## Decision 1.5 – Implementation Language

Question  
Primary implementation language(s)?

Implementation Decision

Rationale

---

## Decision 1.6 – Service Architecture

Question  
Single service or split services?

Implementation Decision

Rationale

---

## Decision 1.7 – Stack Constraints

Question  
Any stack/library constraints (e.g., OpenSSL required, no CGO, etc.)?

Implementation Decision

Rationale

---

## Decision 1.8 – Authoritative Artifact Source

Question  
Authoritative artifact source: extracted machine-readable files, embedded docx, or both?

Implementation Decision

Rationale

---

## Decision 1.9 – Artifact Pinning Strategy

Question  
Artifact pinning strategy: semver-only or hash-pinned?

Implementation Decision

Rationale

---

## Decision 1.10 – Spec Version Support

Question  
Support one AGCP spec version or multiple simultaneously?

Implementation Decision

Rationale

---

## Decision 1.11 – Schema Evolution Policy

Question  
Schema evolution stance: reject unknown fields or allow/ignore?

Implementation Decision

Rationale

---

## Decision 1.12 – Explicit Non-Goals

Question  
List implementation elements explicitly out of scope.

Implementation Decision

Rationale

---

# Section 2 – Runtime Architecture & Service Boundaries

## Decision 2.1 – Service Decomposition

Question  
Service decomposition model: single process, multi-process, distributed?

Implementation Decision

Rationale

---

## Decision 2.2 – Development vs Production Profiles

Question  
Separate development profile from production profile?

Implementation Decision

Rationale

---

## Decision 2.3 – Internal RPC Protocol

Question  
Internal RPC protocol (HTTP+JSON, gRPC, etc.)?

Implementation Decision

Rationale

---

## Decision 2.4 – Internal Transport Security

Question  
Require mTLS for internal calls or rely on host isolation?

Implementation Decision

Rationale

---

## Decision 2.5 – Ledger Backend

Question  
Ledger backend technology?

Implementation Decision

Rationale

---

## Decision 2.6 – Action State Store

Question  
Separate action state store?

Implementation Decision

Rationale

---

## Decision 2.7 – Cosign Token Store

Question  
Separate cosign token store?

Implementation Decision

Rationale

---

## Decision 2.8 – Concurrency Model

Question  
Concurrency model: one worker per tenant or many?

Implementation Decision

Rationale

---

## Decision 2.9 – Rate Limiting

Question  
Per-tenant rate limiting required?

Implementation Decision

Rationale

---

## Decision 2.10 – Idempotency Support

Question  
Require Idempotency-Key header?

Implementation Decision

Rationale

---

## Decision 2.11 – Idempotency Scope

Question  
Idempotency scope: endpoint-specific or global per action?

Implementation Decision

Rationale

---

## Decision 2.12 – Metadata Endpoint

Question  
Metadata endpoint required? If yes, what path?

Implementation Decision

Rationale

---

# Section 3 – Authentication, Authorization & Tenant Binding

## Decision 3.1 – Authentication Mechanism

Question  
Authentication mechanism (JWT, mTLS, API keys, etc.)?

Implementation Decision

Rationale

---

## Decision 3.2 – Identity Provider Model

Question  
Identity provider model: single IdP, per-tenant IdP, hybrid?

Implementation Decision

Rationale

---

## Decision 3.3 – Tenant Identifier Source

Question  
Source of tenant_id (JWT claim, header, hostname, etc.)?

Implementation Decision

Rationale

---

## Decision 3.4 – Tenant Mismatch Policy

Question  
Policy for mismatched tenant identifiers?

Implementation Decision

Rationale

---

## Decision 3.5 – Role-Based Access Control

Question  
Is RBAC required?

Implementation Decision

Rationale

---

## Decision 3.6 – Minimum Roles

Question  
Minimum roles supported?

Implementation Decision

Rationale

---

## Decision 3.7 – Endpoint Role Restrictions

Question  
Any endpoints restricted to specific roles?

Implementation Decision

Rationale

---

## Decision 3.8 – Key Management Mode

Question  
Key management mode: server-managed or tenant-upload?

Implementation Decision

Rationale

---

## Decision 3.9 – Key Rotation and Revocation

Question  
Support key rotation and revocation?

Implementation Decision

Rationale

---

## Decision 3.10 – Audit Logging

Question  
Required audit log fields?

Implementation Decision

Rationale

---

## Decision 3.11 – Telemetry Sink

Question  
Logging/telemetry sink (stdout, file, OpenTelemetry, etc.)?

Implementation Decision

Rationale

---

# Section 4 – Key Management & Cryptography

## Decision 4.1 – JWT Algorithm Allowlist

Question  
JWT algorithm allowlist?

Implementation Decision

Rationale

---

## Decision 4.2 – JWKS Acquisition Model

Question  
JWKS acquisition model: static pinned bundle or fetched?

Implementation Decision

Rationale

---

## Decision 4.3 – JWT Tenant Claim

Question  
JWT claim name used for tenant_id?

Implementation Decision

Rationale

---

## Decision 4.4 – AGCP Key Identifier Format

Question  
AGCP kid format?

Implementation Decision

Rationale

---

## Decision 4.5 – Key Identifier Scope

Question  
Are kid values globally unique or tenant-scoped?

Implementation Decision

Rationale

---

## Decision 4.6 – Key Purpose Definitions

Question  
Key purposes defined (provenance, HITL, etc.)?

Implementation Decision

Rationale

---

## Decision 4.7 – Key Storage Backend

Question  
Key storage backend?

Implementation Decision

Rationale

---

## Decision 4.8 – In-Memory Key Cache

Question  
In-memory key cache required?

Implementation Decision

Rationale

---

## Decision 4.9 – Revocation Mechanism

Question  
Revocation mechanism?

Implementation Decision

Rationale

---

## Decision 4.10 – Rotation Overlap Window

Question  
Rotation overlap duration?

Implementation Decision

Rationale

---

## Decision 4.11 – Verification Failure Mapping

Question  
Verification failure HTTP mapping strategy?

Implementation Decision

Rationale

---

# Section 5 – Persistence Schemas & Sequencing

## Decision 5.1 – Database Topology

Question  
One database with schemas or multiple databases?

Implementation Decision

Rationale

---

## Decision 5.2 – Tenant Partitioning

Question  
Table partitioning by tenant_id required?

Implementation Decision

Rationale

---

## Decision 5.3 – Ledger Storage Model

Question  
Ledger storage model: structured + canonical bytes, or bytes only?

Implementation Decision

Rationale

---

## Decision 5.4 – Ledger Hash Chain

Question  
Maintain hash chain in ledger? If yes, which algorithm and formula?

Implementation Decision

Rationale

---

## Decision 5.5 – Sequence Allocation Strategy

Question  
Sequence allocation strategy (counter row, per-tenant sequence, global sequence)?

Implementation Decision

Rationale

---

## Decision 5.6 – Action Store Projection

Question  
Action store projection updated on write or derived on read?

Implementation Decision

Rationale

---

## Decision 5.7 – Indexed Lookup Keys

Question  
Indexed lookup keys required?

Implementation Decision

Rationale

---

## Decision 5.8 – Cosign Replay Protection

Question  
Cosign replay-prevention uniqueness constraint?

Implementation Decision

Rationale

---

## Decision 5.9 – Idempotency TTL

Question  
Idempotency TTL duration?

Implementation Decision

Rationale

---

## Decision 5.10 – Idempotency Storage

Question  
Store full response body, encrypted body, or response hash only?

Implementation Decision

Rationale

---

# Section 6 – Determinism Controls

## Decision 6.1 – Authoritative Time Source

Question  
Authoritative time source policy?

Implementation Decision

Rationale

---

## Decision 6.2 – Randomness Policy

Question  
Randomness policy (allowed or prohibited in evaluation pipeline)?

Implementation Decision

Rationale

---

## Decision 6.3 – Floating Point Restrictions

Question  
Floating-point usage restrictions?

Implementation Decision

Rationale

---

## Decision 6.4 – Canonicalization Boundaries

Question  
Exactly which bytes are hashed or signed?

Implementation Decision

Rationale

---

## Decision 6.5 – Concurrency Ordering Guarantees

Question  
Concurrency ordering guarantees across workers?

Implementation Decision

Rationale

---

## Decision 6.6 – Replay Purity Guarantees

Question  
Replay and purity guarantees for PEC evaluation?

Implementation Decision

Rationale

---

# Section 7 – Policy Evaluation Module (PEM / PEC)

## Decision 7.1 – Execution Environment

Question  
PEM execution environment (WASM, process isolation, in-process)?

Implementation Decision

Rationale

---

## Decision 7.2 – Resource Limits

Question  
Resource limits (CPU, memory, timeouts)?

Implementation Decision

Rationale

---

## Decision 7.3 – Deterministic Execution Enforcement

Question  
Deterministic execution enforcement mechanisms?

Implementation Decision

Rationale

---

## Decision 7.4 – PEM Version Pinning

Question  
PEM version pinning strategy?

Implementation Decision

Rationale

---

## Decision 7.5 – State Snapshot Construction

Question  
State snapshot construction rules?

Implementation Decision

Rationale

---

# Section 8 – Operational Hardening & Lifecycle

## Decision 8.1 – Backup Strategy

Question  
Backup strategy for Postgres and key material?

Implementation Decision

Rationale

---

## Decision 8.2 – Disaster Recovery

Question  
Disaster recovery RTO/RPO targets?

Implementation Decision

Rationale

---

## Decision 8.3 – Database Migration Strategy

Question  
Database migration strategy?

Implementation Decision

Rationale

---

## Decision 8.4 – Observability SLOs

Question  
Observability SLOs defined?

Implementation Decision

Rationale

---

## Decision 8.5 – Rate Limiting and DoS Mitigation

Question  
Rate limiting and DoS mitigation strategy?

Implementation Decision

Rationale

---

## Decision 8.6 – Upgrade and Rollout Strategy

Question  
Upgrade and rollout strategy?

Implementation Decision

Rationale

---

## Decision 8.7 – Configuration Immutability

Question  
Configuration immutability and startup validation rules?

Implementation Decision

Rationale

---

# Relationship to AGCP Conformance

Completion of this questionnaire does **not** by itself establish AGCP conformance.

Implementations must satisfy the normative requirements defined in:

- AGCP Core Specification  
- AGCP Conformance Specification  
- AGCP Ledger Storage Contract  
- AGCP Policy Evaluation Contract
