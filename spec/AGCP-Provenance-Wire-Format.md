# AGCP Concrete Provenance Wire Format Specification

Version: 0.9.0  
Status: Normative  
Scope: Defines the exact provenance wire format, canonicalization procedure for signing/verifying, signature encoding, and replay-window rules for AGCP requests and tokens. This artifact removes bit-level ambiguity for interoperable implementations.

---

# 1. Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in:

- RFC 2119
- RFC 8174

---

# 2. Applicability

This specification applies to all AGCP HTTP requests that include a provenance envelope and to any bearer artifacts derived from the same signing scheme, including:

- HITL cosign tokens
- execution commit attestations

---

# 3. Provenance Envelope

Each signed request **MUST** include a JSON object field named `provenance` at the top level of the request body.

The `provenance` object SHALL contain the following fields:

| Field | Type | Required | Description |
|------|------|---------|-------------|
| signer | string | YES | Signer identity (e.g., key ID, subject, or DID) |
| kid | string | YES | Key identifier. MUST uniquely identify the verification key within the tenant trust domain |
| alg | string | YES | Signing algorithm identifier |
| signed_at | string (RFC3339) | YES | Time the signature was created |
| expires_at | string (RFC3339) | NO | Optional expiry timestamp |
| nonce | string | YES | Client-generated nonce for replay protection |
| scope | string | YES | Signature scope label |
| signature | string | YES | Signature encoding |

The provenance object **MUST** be included in the request body itself to ensure the signed payload is self-contained and auditable.

---

# 4. Signed Content (Signature Scope)

The signature **MUST** cover a canonical representation of the request body with the field:

```
provenance.signature
```

excluded.

The `scope` field indicates what portion of the envelope was signed.

Implementations **MUST support**:

```
agcp.http.request.body
```

which represents canonicalized JSON of the request body excluding `provenance.signature`.

Headers are **not signed by default** in this profile.

If a deployment signs headers, it **MUST introduce a new scope value** and MUST NOT break verification for the required scope.

---

# 5. Canonicalization Procedure for Signing / Verification

Canonicalization **MUST be deterministic across implementations**.

### Input

The full JSON request body object.

### Procedure

1. Create a deep copy of the JSON object.
2. Within the `provenance` object remove the field:

```
signature
```

3. Do not reorder arrays. Array element order MUST remain unchanged.
4. For all JSON objects:
   - Sort keys lexicographically by Unicode code point order.
5. Serialize the JSON with the following rules:

- UTF-8 encoding
- No insignificant whitespace
- Minimal JSON formatting
- Strings escaped according to JSON rules

The resulting byte sequence is called:

```
canonical_bytes
```

---

# 6. Algorithms and Key Requirements

The `alg` field identifies the signing algorithm.

Implementations **MUST support at least one** of the following:

| Algorithm | Requirement |
|-----------|-------------|
| EdDSA-Ed25519 | RECOMMENDED |
| ES256 | OPTIONAL |
| RS256 | OPTIONAL |

Key requirements:

- Public keys MUST be retrievable by `(tenant_id, kid)`
- Key lookup MUST be tenant scoped
- Cross-tenant key use MUST be rejected

---

# 7. Signature Encoding

This specification uses a deterministic **Detached JWS-like encoding**.

---

## 7.1 Protected Header

The protected header contains:

```
{
  "alg": "...",
  "kid": "...",
  "typ": "AGCP+PROV"
}
```

Keys MUST be sorted and serialized in minimal JSON form.

---

## 7.2 Signing Input

Let:

```
protected_header_json
protected_header_b64
payload_b64
```

Where:

```
protected_header_b64 = base64url(protected_header_json)
payload_b64 = base64url(canonical_bytes)
```

The signing input is:

```
signing_input = protected_header_b64 + "." + payload_b64
```

---

## 7.3 Signature Value

```
sig_bytes = SIGN(signing_input, private_key, alg)
sig_b64   = base64url(sig_bytes)
```

---

## 7.4 Wire Encoding

The `provenance.signature` field MUST contain:

```
signature = protected_header_b64 + ".." + sig_b64
```

The double period indicates a **detached payload**.

---

## 7.5 Verification

Verification requires:

1. Recompute canonical bytes.
2. Reconstruct `signing_input`.
3. Verify signature using `(tenant_id, kid)` key.

---

# 8. Replay Protection and Time Window Rules

## 8.1 Time Validation

`signed_at` MUST be validated with clock skew tolerance.

Default tolerance:

```
300 seconds (5 minutes)
```

---

## 8.2 Replay Window

A request MUST be rejected if:

```
now < signed_at - skew_tolerance
```

or

```
now > signed_at + replay_window
```

Default replay window:

```
600 seconds (10 minutes)
```

---

## 8.3 Nonce Uniqueness

Nonce uniqueness MUST be enforced for the tuple:

```
(tenant_id, signer, scope, nonce)
```

If the same tuple appears within the replay window the request MUST be rejected.

---

## 8.4 Storage Requirements

Replay tuples MUST be stored for at least:

```
replay_window + skew_tolerance
```

Storage MAY be:

- memory cache
- distributed cache
- database

provided it is consistent with the deployment threat model.

---

# 9. Error Mapping

If provenance verification fails:

```
HTTP 400
rejection_code = PROVENANCE_INVALID
```

If key lookup violates tenant scope:

```
HTTP 403
rejection_code = TENANT_SCOPE_VIOLATION
```

Replay detection SHOULD return:

```
HTTP 409
rejection_code = PROVENANCE_INVALID
```

or a dedicated replay code if defined.

---

# 10. Minimal Test Vectors

Implementations SHOULD include automated tests verifying:

- canonicalization consistency across languages
- signature generation and verification round-trip
- replay detection for duplicate nonce
- rejection outside allowed time windows

---

# 11. Versioning and Compatibility

Changes to any of the following require a **MAJOR version increment**:

- canonicalization rules
- signature encoding
- signing input structure
- replay window semantics

Alternatively a new scope profile identifier may be introduced.
