# AGCP HITL Token Structure Specification v0.9.0

**Status:** Normative  
**Scope:** Defines the exact Human-In-The-Loop (HITL) cosign token wire format, required fields, cryptographic binding rules, canonicalization procedure, signature encoding, and replay protection semantics.

This artifact complements the PEC semantic definition by specifying bit-level token encoding.

---

# 1. Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in **RFC 2119** and **RFC 8174**.

---

# 2. Token Model Overview

A HITL token represents a cryptographically signed cosign assertion by an authorized principal.

It **MUST** be bound to a specific `tenant_id` and `action_id` and **MUST NOT** be reusable across actions or tenants.

The token **MUST** be self-contained and verifiable without external mutable state.

---

# 3. HITL Token Payload Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "tenant_id",
    "action_id",
    "role",
    "signer",
    "kid",
    "alg",
    "issued_at",
    "nonce",
    "scope",
    "signature"
  ],
  "properties": {
    "tenant_id": { "type": "string" },
    "action_id": { "type": "string" },

    "role": {
      "type": "string",
      "description": "Role being satisfied (e.g., RISK_OFFICER)."
    },

    "signer": {
      "type": "string",
      "description": "Identity of the human or principal providing cosign."
    },

    "kid": {
      "type": "string",
      "description": "Key identifier for signature verification."
    },

    "alg": {
      "type": "string",
      "description": "Signature algorithm identifier."
    },

    "issued_at": {
      "type": "string",
      "format": "date-time"
    },

    "expires_at": {
      "type": "string",
      "format": "date-time"
    },

    "nonce": {
      "type": "string",
      "description": "Unique nonce for replay protection."
    },

    "scope": {
      "type": "string",
      "description": "Must equal 'agcp.hitl.cosign'."
    },

    "signature": {
      "type": "string",
      "description": "Detached JWS-style signature encoding (Section 6)."
    }
  }
}
```

---

## 3.1 Required scope value

The `scope` field **MUST** equal the literal string:

```
agcp.hitl.cosign
```

---

# 4. Cryptographic Binding Rules

A valid token **MUST** cryptographically bind the following fields:

- `tenant_id`
- `action_id`
- `role`
- `signer`
- `issued_at`
- `nonce`
- `scope`

Any alteration of these fields **MUST** invalidate the signature.

The token **MUST NOT** be valid for a different `action_id` or `tenant_id` than those embedded in the signed payload.

---

# 5. Canonicalization Procedure

To produce `canonical_bytes` for signing:

1. Create a deep copy of the token JSON object.
2. Remove the `signature` field entirely.
3. Sort all object keys lexicographically by Unicode code point order.
4. **Do NOT** reorder arrays (if any).
5. Serialize as minimal JSON (no extra whitespace) using UTF-8 encoding.
6. The resulting UTF-8 byte sequence is `canonical_bytes`.

---

# 6. Signature Encoding

The `signature` field **MUST** use detached JWS-style encoding.

## 6.1 Protected header JSON (canonical, sorted keys)

```json
{"alg": <alg>, "kid": <kid>, "typ": "AGCP+HITL"}
```

## 6.2 Encoding steps

```
protected_header_b64 = base64url(protected_header_json_bytes) (no padding)

payload_b64 = base64url(canonical_bytes) (no padding)

signing_input = protected_header_b64 + "." + payload_b64

sig_bytes = SIGN(signing_input, private_key, alg)

sig_b64 = base64url(sig_bytes) (no padding)

signature = protected_header_b64 + ".." + sig_b64
```

Verification **MUST** recompute `canonical_bytes` and `signing_input` exactly as above.

---

# 7. Supported Algorithms

Implementations **MUST** support at least one of:

- EdDSA-Ed25519 (**RECOMMENDED baseline**)
- ES256
- RS256

Public key lookup **MUST** be tenant-scoped using:

```
(tenant_id, kid)
```

---

# 8. Replay Protection and Expiry

## 8.1 Time window validation

- Default allowed clock skew: **300 seconds**
- Token **MUST** be rejected if:

```
now < issued_at - skew
```

- If `expires_at` is present, token **MUST** be rejected if:

```
now > expires_at + skew
```

---

## 8.2 Nonce uniqueness

The tuple:

```
(tenant_id, action_id, signer, nonce)
```

**MUST** be unique within the replay window.

If seen again within the window, the token **MUST** be rejected as replay.

---

## 8.3 One-time-use enforcement

Even if nonce uniqueness is enforced, a token **MUST NOT** transition state more than once.

If quorum has already been satisfied or the action is not in `PENDING_HITL`, the token **MUST** be rejected.

---

# 9. Error Mapping Guidance

If signature verification fails:

```
rejection_code = COSIGN_INVALID
HTTP 409 recommended
```

If token expired:

```
rejection_code = COSIGN_EXPIRED
HTTP 409 recommended
```

If wrong tenant/action binding:

```
rejection_code = TENANT_SCOPE_VIOLATION
or ACTION_NOT_AUTHORIZED
```

If replay detected:

Implementations **SHOULD** indicate replay explicitly; otherwise `COSIGN_INVALID` may be used conservatively.

---

# 10. Versioning and Compatibility

Any change to the following **constitutes a breaking change**:

- canonicalization rules
- required fields
- signature encoding
- binding semantics

Such changes **SHALL** require either:

- a **MAJOR version increment**, or  
- a **distinct scope identifier**.
