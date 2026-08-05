# AGCP Provenance Wire Format Specification

**Status:** Normative
**Specification Version:** 2.0.4  
**Artifact Lifecycle:** Current  
**Repository Release Target:** AGCP v2.0.4  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.4 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-05  
**AGCP Release Series:** v2

## 1. Purpose

This specification defines the canonical provenance wire envelope, deterministic canonicalization procedure, detached-signature encoding, verification process, and replay-protection requirements for AGCP-conformant implementations.

It establishes one interoperable, implementation-independent provenance representation for governance requests and governance artifacts. `schemas/common.json#/$defs/provenance` is the authoritative machine-readable schema for this envelope and SHALL remain structurally identical to this specification.

## 2. Scope

This specification applies to every AGCP request or governance artifact containing a top-level `provenance` member, including:

- Proposal submission requests;
- Commit Boundary requests;
- Governance Approval submission envelopes;
- governance artifacts;
- Governance Evidence;
- Governance Ledger Events; and
- metadata or lifecycle artifacts that declare provenance.

A schema that references `common.json#/$defs/provenance` inherits this wire contract without redefining it.

## 3. Canonical Provenance Wire Envelope

Every signed object SHALL contain one top-level `provenance` object with the following fields and no undeclared fields.

| Field | Required | Wire type | Description |
|---|---:|---|---|
| `signer` | Yes | string | Stable signer identity within the applicable tenant and governance scope. |
| `kid` | Yes | string | Verification-key identifier. |
| `alg` | Yes | string | Signature algorithm identifier. |
| `signed_at` | Yes | RFC 3339 string | Time at which the signature was produced. |
| `expires_at` | No | RFC 3339 string | Optional signature-expiration time. |
| `nonce` | Yes | string | Replay-protection nonce. |
| `scope` | Yes | string | Signature-scope identifier. |
| `signature` | Yes | string | Detached compact JWS-style value in `protected_header_b64..signature_b64` form. |

The wire envelope SHALL NOT use a nested signature object. In particular, `alg`, `kid`, and the detached signature value SHALL be direct properties of `provenance`.

The provenance object, except for `provenance.signature`, SHALL be included in the signed payload. Fields such as `source_system`, `source_artifact_ref`, `payload_digest`, or `predecessor_evidence_refs` are not members of this wire envelope. Where those concepts are required, they SHALL be represented in their owning governance schema.

### 3.1 Example

```json
{
  "provenance": {
    "signer": "client:test",
    "kid": "kid-test",
    "alg": "Ed25519",
    "signed_at": "2026-08-03T11:00:00Z",
    "nonce": "nonce-0000000000000001",
    "scope": "agcp.http.request.body",
    "signature": "eyJhbGciOiJFZDI1NTE5Iiwia2lkIjoia2lkLXRlc3QiLCJ0eXAiOiJBR0NQK1BST1YifQ..U0lHTkFUVVJF"
  }
}
```

## 4. Signature Scope

Implementations SHALL support at least:

`agcp.http.request.body`

Additional scopes MAY include:

- `agcp.proposal`;
- `agcp.governance-approval`;
- `agcp.commit-boundary`; and
- `agcp.governance-evidence`.

New scope identifiers SHALL use the `agcp.` namespace and preserve backward compatibility. A verifier SHALL reject a signature presented for a different operation or artifact scope.

## 5. Governance Binding

Where applicable, signed content SHALL bind:

- `tenant_id`;
- `governance_domain_id`;
- `proposal_id`;
- `action_id`;
- Governance Context;
- Canonical State; and
- Authority Lineage.

Modification of bound content SHALL invalidate the signature.

## 6. Canonicalization

To produce canonical payload bytes:

1. parse the complete JSON object containing `provenance`;
2. make a deep copy;
3. remove only `provenance.signature` from the copy;
4. canonicalize the remaining JSON data model using RFC 8785 JSON Canonicalization Scheme;
5. encode the canonical representation as UTF-8; and
6. use the resulting bytes as the detached-signature payload.

Array order SHALL be preserved. Implementations SHALL NOT remove `signer`, `kid`, `alg`, `signed_at`, `expires_at`, `nonce`, or `scope` during canonicalization.

## 7. Algorithms

Implementations SHALL support at least one of:

- Ed25519, represented as `Ed25519` in the AGCP wire envelope;
- ES256; or
- RS256.

An implementation profile MAY restrict the permitted set. Verification keys SHALL be resolved within the applicable tenant and governance scope. Digest algorithm names, such as `SHA-256`, SHALL NOT be used as signature-algorithm identifiers.

## 8. Detached Signature Encoding

Detached compact JWS-style encoding SHALL be used.

Protected header:

```json
{
  "alg": "...",
  "kid": "...",
  "typ": "AGCP+PROV"
}
```

The protected header SHALL be serialized as minimal UTF-8 JSON and base64url encoded without padding. Its `alg` and `kid` values SHALL equal the corresponding top-level provenance fields, and `typ` SHALL equal `AGCP+PROV`.

Signing input:

```text
protected_header_b64 + "." + payload_b64
```

Wire value stored in `provenance.signature`:

```text
protected_header_b64 + ".." + signature_b64
```

`payload_b64` is the unpadded base64url encoding of the canonical payload bytes produced by Section 6. Verification SHALL reconstruct the canonical representation and signing input exactly.

## 9. Verification Procedure

A verifier SHALL, in order:

1. validate the complete object against its applicable JSON Schema;
2. validate `provenance` against `common.json#/$defs/provenance`;
3. parse the detached signature into exactly two non-empty base64url segments separated by `..`;
4. decode and validate the protected header;
5. require protected `typ`, `alg`, and `kid` to match this specification and the envelope;
6. resolve the key identified by `kid` within the applicable tenant and governance scope;
7. enforce algorithm allowlisting;
8. enforce `signed_at`, optional `expires_at`, clock-skew, replay-window, scope, and nonce rules;
9. reconstruct the canonical payload and signing input;
10. verify the cryptographic signature; and
11. record the verification result as Governance Evidence.

Schema validity alone SHALL NOT establish signature validity, key authority, freshness, scope validity, or replay uniqueness.

## 10. Replay Protection

Replay protection SHALL enforce:

- configurable clock-skew tolerance;
- configurable replay window;
- optional expiration; and
- durable nonce uniqueness.

The tuple:

```text
tenant_id
signer
scope
nonce
```

SHALL be unique for the replay window. Previously accepted signed content SHALL NOT be replayed.

## 11. Governance Evidence

Successful or failed provenance verification SHALL produce or support Governance Evidence recording, as applicable:

- verification outcome;
- signer;
- key identifier;
- signature algorithm;
- signing time;
- scope;
- nonce or a protected nonce reference;
- applicable governance stage; and
- rejection reason when verification fails.

## 12. Error Handling

Failed provenance verification SHALL use the applicable rejection code from the Rejection Code Registry. Tenant or governance-domain scope violations SHALL be rejected before governance processing continues.

## 13. Conformance

Conformant implementations SHALL:

- implement the exact envelope in Section 3;
- implement deterministic canonicalization in Section 6;
- generate and verify the detached representation in Section 8;
- enforce replay protection;
- enforce tenant-scoped and governance-domain-scoped key resolution; and
- pass the controlled cross-language vectors in `conformance/provenance/AGCP-Provenance-Wire-Format-Test-Vectors.json`.

## 14. Security Considerations

Implementations SHALL:

- protect signing keys;
- validate certificate or key trust chains where applicable;
- reject cross-tenant or cross-domain key use;
- prevent algorithm substitution;
- compare protected-header values with the wire envelope;
- preserve immutable verification evidence; and
- avoid logging private key material or unprotected sensitive payloads.

## 15. Repository Versioning

This specification follows repository release versioning. Canonicalization rules, signature encoding, signing-input structure, envelope fields, or replay semantics SHALL NOT change incompatibly within a repository release series.

Changes to this wire contract require synchronized updates to `schemas/common.json`, dependent schemas, IF-001/OpenAPI, examples, conformance vectors, schema catalogs, hashes, validation reports, and RTM mappings.
