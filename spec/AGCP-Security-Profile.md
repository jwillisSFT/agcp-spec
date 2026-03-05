# AGCP Security Profile Specification v0.9.0

**Status:** Normative  
**Version:** 0.9.0  
**Series:** AGCP Core  
**Applies To:** All AGCP-conformant implementations

---

# 1. Purpose

This Security Profile defines the mandatory and recommended security requirements for AGCP implementations.

It specifies:

- Threat model
- Trust model
- Cryptographic requirements
- Multitenant isolation requirements
- Replay protection requirements
- Ledger integrity guarantees
- Policy module security
- HITL security controls
- Execution gating protections
- Denial-of-service considerations

All AGCP implementations **MUST** comply with this profile to claim Core conformance.

---

# 2. Threat Model

AGCP implementations **SHALL** assume the following threat actors:

- Malicious agent within a tenant
- Compromised agent identity
- Malicious tenant attempting cross-tenant escalation
- Insider with control-plane access
- Network adversary (MITM)
- Malicious or nondeterministic policy module author
- Execution adapter attempting bypass
- Replay attacker

AGCP implementations **MUST** design controls against the following threat classes:

- Envelope tampering
- Signature forgery
- Tenant boundary bypass
- Constraint injection
- Exception abuse
- Invariant bypass
- Replay attacks
- Ledger tampering
- HITL token replay/forgery
- Execution commit bypass
- Denial-of-service
- Timing-based tenant inference

Each requirement below mitigates one or more of these threats.

---

# 3. Trust Model

AGCP **SHALL** operate under the following trust assumptions:

- Agents are untrusted unless cryptographically verified.
- Tenants are mutually untrusted.
- Policy modules are untrusted until validated.
- Execution adapters are untrusted until ledger binding is verified.
- Network transport is untrusted without TLS protection.

Trust is established only through:

- Cryptographic verification
- Tenant scoping
- Deterministic PEC enforcement
- Ledger binding
- State validation

---

# 4. Cryptographic Requirements

## 4.1 Transport Security

All HTTP endpoints **MUST** be accessible only over HTTPS using TLS 1.2 or higher.

TLS 1.3 **SHOULD** be supported.

Plain HTTP **MUST NOT** be used in production.

---

## 4.2 Envelope Signatures

ActionEnvelope submissions **MUST** include cryptographic provenance signatures.

The implementation **MUST**:

- Verify signature prior to PEC evaluation.
- Verify signature binds to:
  - `tenant_id`
  - `action_id`
  - payload hash
  - timestamp

Reject invalid signatures with:

```
SIGNATURE_INVALID
```

---

## 4.3 Cosign Token Security

Cosign tokens **MUST**:

- Be cryptographically signed
- Include `tenant_id`
- Include `action_id`
- Include expiration timestamp
- Include signer identity
- Be non-reusable

Expired tokens **MUST** result in:

```
COSIGN_EXPIRED
```

Invalid tokens **MUST** result in:

```
COSIGN_INVALID
```

---

## 4.4 Cryptographic Profiles

AGCP implementations **SHALL** declare supported cryptographic profiles via `/meta`.

Profiles **MAY** include:

- LEGACY
- PQC
- HYBRID

Removal of cryptographic algorithms requires **MAJOR version increment**.

---

## 4.5 Key Management

Implementations **MUST**:

- Isolate cryptographic trust roots per tenant **OR**
- Enforce tenant-scoped key namespaces

Key revocation **SHOULD** be supported.

---

# 5. Replay Protection

## 5.1 Idempotency Enforcement

ActionEnvelope **MUST** include `idempotency_key`.

If the same `idempotency_key` is submitted with different payload:

```
MUST return HTTP 409
MUST return IDEMPOTENCY_CONFLICT
```

---

## 5.2 Replay of Authorized Execution

Execution commit **MUST**:

- Verify ledger authorization reference
- Verify action state is `AUTHORIZED`

Duplicate execution commit attempts **MUST** be rejected.

---

# 6. Ledger Integrity Requirements

AGCP ledger **MUST**:

- Be append-only
- Be immutable
- Preserve ordering
- Be tenant-scoped

Ledger entries **MUST** include:

- Validation stage
- Constraint results
- Invariant results
- HITL status
- Final decision
- Execution outcome (if applicable)

Ledger tampering attempts **MUST** be detectable.

If tampering is detected, the implementation **MUST** reject operations.

---

# 7. Multitenant Isolation Requirements

AGCP implementations **MUST**:

- Enforce tenant namespace isolation
- Prevent cross-tenant policy resolution
- Prevent cross-tenant constraint resolution
- Prevent cross-tenant invariant resolution
- Prevent cross-tenant exception resolution
- Prevent cross-tenant ledger reads
- Prevent cross-tenant execution commits

Cross-tenant access attempts **MUST** result in:

```
TENANT_SCOPE_VIOLATION
```

---

# 8. Policy Module Security

Policy Evaluation Modules (PEMs) **MUST**:

- Be integrity-validated before activation
- Be version-controlled
- Be tenant-scoped
- Be deterministic
- Be side-effect free

If module integrity fails:

```
POLICY_MODULE_INVALID
```

If module unavailable:

```
POLICY_MODULE_UNAVAILABLE
```

If module nondeterministic:

```
POLICY_MODULE_NONDETERMINISTIC
```

---

# 9. PEC Evaluation Security

PEC evaluation **MUST**:

- Not perform network calls
- Not mutate external state
- Not depend on system clock beyond envelope timestamp
- Not depend on random values
- Not access environment variables

Violation **MUST** result in module rejection.

---

# 10. Execution Gating Security

Execution adapters **MUST**:

- Verify ledger binding
- Verify tenant scope
- Verify action state is `AUTHORIZED`
- Record execution result in ledger

Execution **MUST NOT** occur based solely on envelope acceptance.

---

# 11. Exception Abuse Protection

Exceptions **MUST**:

- Be tenant-scoped
- Be time-bound
- Be approved via defined process
- Be recorded in ledger

Expired exceptions **MUST NOT** be honored.

---

# 12. Denial-of-Service Protections

AGCP implementations **MUST** support:

- Per-tenant rate limiting capability
- Envelope size limits
- Concurrent submission limits

Resource exhaustion in one tenant **MUST NOT** impact others.

---

# 13. Timing and Side-Channel Protection

Implementations **SHOULD**:

- Avoid exposing tenant existence via timing differences
- Avoid detailed error messages revealing internal state
- Normalize rejection timing where feasible

---

# 14. Administrative Access Controls

Administrative endpoints (tenant creation, policy registration, module registration) **MUST** require authentication and authorization.

Administrative operations **MUST** be ledger-recorded.

---

# 15. State Transition Protections

Tenant state transitions **MUST**:

- Be authorized
- Be validated
- Be ledger-recorded

Execution **MUST NOT** occur if tenant state is not `ACTIVE`.

---

# 16. Security Conformance Requirements

An implementation claiming Core conformance **MUST**:

- Enforce signature validation
- Enforce replay protection
- Enforce tenant isolation
- Enforce deterministic PEC evaluation
- Enforce execution gating
- Enforce ledger immutability

L5 conformance additionally requires verified cross-tenant negative tests.

---

# 17. Security Audit Requirements

Implementations **SHOULD** provide:

- Audit logging
- Tamper detection mechanisms
- Integrity verification tools
- Cryptographic key rotation mechanisms

These are recommended but not mandatory for Core.

---

# 18. Non-Goals

This profile does **not** mandate:

- Specific cryptographic libraries
- Specific key storage solutions
- Specific HSM integration
- Specific cloud provider security model
- Specific compliance frameworks

It defines **security behaviors only**.

---

# 19. Versioning

Security requirement changes that:

```
Remove protections → MAJOR version increment
Add optional protections → MINOR increment
Clarify wording → PATCH increment
```

---

# 20. Summary

The AGCP Security Profile guarantees:

- Cryptographic authenticity
- Deterministic policy enforcement
- Multitenant isolation
- Replay protection
- Execution integrity
- Ledger immutability
- Policy module safety

All AGCP implementations **MUST** conform to this profile to claim Core compliance.
