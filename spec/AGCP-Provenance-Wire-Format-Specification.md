# AGCP Provenance Wire Format Specification

**Status:** Normative

## 1. Purpose

This specification defines the canonical provenance wire format,
deterministic canonicalization procedure, signature encoding,
verification process, and replay protection requirements for
AGCP-conformant implementations.

It establishes interoperable, implementation-independent provenance
semantics for governance requests and governance artifacts.

## 2. Scope

This specification applies to all AGCP requests and governance artifacts
containing a `provenance` object, including:

-   Proposal submission requests
-   Commit Boundary requests
-   Human Review artifacts
-   Governance artifacts
-   Governance Evidence

## 3. Provenance Object

Every signed object SHALL contain a top-level `provenance` object.

  Field        Required   Description
  ------------ ---------- -----------------------------
  signer       Yes        Signer identity
  kid          Yes        Verification key identifier
  alg          Yes        Signature algorithm
  signed_at    Yes        RFC3339 timestamp
  expires_at   Optional   Expiration timestamp
  nonce        Yes        Replay-protection nonce
  scope        Yes        Signature scope identifier
  signature    Yes        Detached signature

The provenance object SHALL be part of the signed payload.

## 4. Signature Scope

Implementations SHALL support at least:

`agcp.http.request.body`

Additional scopes MAY include:

-   `agcp.proposal`
-   `agcp.human-review`
-   `agcp.commit-boundary`
-   `agcp.governance-evidence`

New scope identifiers SHALL preserve backward compatibility.

## 5. Governance Binding

Where applicable, signed content SHALL bind:

-   tenant_id
-   governance_domain_id
-   proposal_id
-   action_id
-   Governance Context
-   Canonical State
-   Authority Lineage

Modification of bound content SHALL invalidate the signature.

## 6. Canonicalization

To produce canonical bytes:

1.  Deep-copy the JSON object.
2.  Remove `provenance.signature`.
3.  Preserve array order.
4.  Sort object keys lexicographically.
5.  Serialize as minimal UTF-8 JSON.

The resulting UTF-8 byte sequence is the canonical representation.

## 7. Algorithms

Implementations SHALL support at least one of:

-   Ed25519 (recommended baseline)
-   ES256
-   RS256

Verification keys SHALL be resolved within the applicable tenant
governance scope.

## 8. Signature Encoding

Detached JWS-style encoding SHALL be used.

Protected header:

``` json
{
  "alg":"...",
  "kid":"...",
  "typ":"AGCP+PROV"
}
```

Signing input:

    protected_header_b64 + "." + payload_b64

Wire format:

    protected_header_b64 + ".." + signature_b64

Verification SHALL reconstruct the canonical representation and signing
input exactly.

## 9. Replay Protection

Replay protection SHALL enforce:

-   configurable clock-skew tolerance
-   configurable replay window
-   nonce uniqueness

The tuple:

    tenant_id
    signer
    scope
    nonce

SHALL be unique for the replay window.

Previously accepted requests SHALL NOT be replayed.

## 10. Governance Evidence

Successful provenance verification SHALL produce Governance Evidence
recording:

-   verification outcome
-   signer
-   key identifier
-   timestamp
-   applicable governance stage

## 11. Error Handling

Failed provenance verification SHALL return the appropriate rejection
code from the Rejection Code Registry.

Tenant-scope violations SHALL be rejected before governance processing
continues.

## 12. Conformance

Conformant implementations SHALL:

-   implement deterministic canonicalization
-   generate interoperable signatures
-   validate replay protection
-   enforce tenant-scoped verification
-   generate Governance Evidence for successful verification

## 13. Security Considerations

Implementations SHALL:

-   protect signing keys
-   validate certificate or key trust chains where applicable
-   reject cross-tenant key use
-   verify signature algorithms
-   preserve immutable provenance records

## 14. Repository Versioning

This specification follows repository release versioning.

Canonicalization rules, signature encoding, signing input structure, or
replay semantics SHALL NOT change incompatibly within a repository
release series.
