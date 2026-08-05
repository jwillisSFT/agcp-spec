# DS-001 Content Digest Contract Update

**Finding:** P1-12  
**Release target:** AGCP v2.0.1  
**Controlled schema:** `schemas/common.json#/$defs/content_digest`

## Corrected contract

The generic content-digest definition now binds the declared algorithm to an
exact lowercase-hexadecimal output length:

| Algorithm | Exact hexadecimal length |
|---|---:|
| `SHA-256` | 64 |
| `SHA-384` | 96 |
| `SHA-512` | 128 |
| `BLAKE2B-256` | 64 |
| `BLAKE2B-512` | 128 |

Uppercase hexadecimal, non-hexadecimal values, ambiguous `BLAKE2B`, and any
algorithm/value length mismatch are invalid. The retained `hash_hex` scalar is
deprecated, lowercase-only, and limited to 64, 96, or 128 hexadecimal
characters. New and revised contracts shall use `content_digest`.

## Dependency effect

Every active schema that references `common.json#/$defs/content_digest`
inherits this rule without duplicating the algorithm table. Controlled
examples, the OpenAPI component, formal Test Cases, RTM mappings, schema
catalog, conformance vectors, validation report, and CI gate are synchronized
with the corrected contract.
