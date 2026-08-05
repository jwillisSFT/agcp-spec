# AGCP Interface Definition Catalog

- Catalog ID: `IF-CATALOG-1.0`
- Catalog version: `1.0.5`
- Specification version: `v2.0.1`
- Publication status: `CURRENT`
- Artifact lifecycle state: `CURRENT`
- Repository release target: `v2.0.1` (`UNRELEASED_ACCUMULATED_CORRECTION_SET`)
- Controlling published baseline: `v2.0.0` (`PUBLIC_REVIEW_CONTROLLED_BASELINE`)
- Baseline date: `2026-07-30`
- Last modified: `2026-08-03`

| IF ID | Interface | Version | Contract version | Controlled artifact | CR mappings |
|---|---|---|---|---|---:|
| `IF-001` | AGCP HTTP Interface v2 | `v2` | `2.0.1` | `spec/AGCP-HTTP-Interface-Specification.md` | 56 |
| `IF-002` | AGCP Policy Evaluation Contract | `v2` | `2.0.1` | `spec/AGCP-Policy-Evaluation-Contract.md` | 40 |

## IF-001 provenance wire contract

IF-001 is explicitly mapped to CR-005 for requests and submitted artifacts carrying provenance. The machine-readable contract references `schemas/common.json#/$defs/provenance`, and the normative representation is defined by `spec/AGCP-Provenance-Wire-Format-Specification.md`.

## IF-002 controlled profile companion

The proposed Rust Student Service profile adopts the following profile-specific machine contract. It specializes IF-002 and does not make WebAssembly universal:

| Companion identifier | Version | ABI | Applicable profile | Specification | Machine contract | Vectors |
|---|---:|---|---|---|---|---|
| `IF-002-WASM-RUST-STUDENT-SERVICE-2.0.0` | `1.0.0` | `agcp_pec_abi_v1` | `AGCP-RUST-STUDENT-SERVICE-2.0.0` | `spec/AGCP-WASM-Policy-Evaluation-Machine-Contract.md` | `api/if-002/AGCP-WASM-PEC-Machine-Contract.json` | `conformance/if-002/AGCP-WASM-PEC-Test-Vectors.json` |

### IF-001 governance-approval command/record binding

`submitGovernanceApproval` accepts DS-045 `Governance Approval Submission` as untrusted ingress. DS-026 `Governance Approval Artifact` is an authoritative AGCP-created or AGCP-qualified record and is never accepted as request content.

## IF-001 v2.0.1 Public Error and Metadata Contract

IF-001 normalizes public protected-resource lookup failures to `404 RESOURCE_NOT_FOUND`, defines pre-governance throttling as `429 REQUEST_THROTTLED` with required delay-seconds `Retry-After`, defines unavailable system/node capacity as `503 CAPACITY_UNAVAILABLE`, and keeps governance quota or entitlement denial as an authoritative Governance Outcome. DS-003 metadata advertises immutable baseline and profile digests, schema and validator digests, active governance version, and optional public-safe deployment binding.
