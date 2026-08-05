# AGCP Provenance Wire-Format Vectors

`AGCP-Provenance-Wire-Format-Test-Vectors.json` is the controlled, implementation-independent cross-language vector package for the AGCP provenance wire envelope.

The package contains:

- exact unsigned JSON data;
- RFC 8785-compatible canonical UTF-8 bytes for the constrained vector data;
- protected-header JSON and unpadded base64url encoding;
- detached Ed25519 signing input and signature;
- the complete signed object; and
- schema, cryptographic, protected-header, algorithm, and replay negative cases.

The private seed is test-only deterministic material and SHALL NOT be used outside conformance testing.
