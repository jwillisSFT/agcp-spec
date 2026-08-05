# AGCP Deterministic WASM Policy Evaluation Machine Contract

**Status:** Normative Profile Companion  
**Base Interface:** IF-002 - AGCP Policy Evaluation Contract v2  
**Companion Interface Identifier:** `IF-002-WASM-RUST-STUDENT-SERVICE-2.0.0`  
**Companion Contract Version:** `1.0.0`  
**ABI Identifier:** `agcp_pec_abi_v1`  
**Applicable Implementation Profile:** `AGCP-RUST-STUDENT-SERVICE-2.0.0`  
**AGCP Release Target:** v2.0.1  
**Artifact Lifecycle:** Current  
**Repository Release Target Status:** Unreleased Accumulated Correction Set  
**Controlling Published Baseline:** AGCP v2.0.0 Public Review - Controlled Baseline  
**Baseline Date:** 2026-07-30

## 1. Purpose and scope

This specification defines the deterministic WebAssembly machine boundary selected by the controlled Rust Student Service Implementation Profile. It specializes IF-002 without changing the implementation-independent AGCP Policy Evaluation Contract or making WebAssembly a universal AGCP requirement.

A conforming module under this companion SHALL be a pure, side-effect-free function over a canonical input envelope, exact module bytes, declared runtime compatibility, and evidence-recorded resource limits. A Policy Evaluation Module SHALL NOT create an authoritative Governance Outcome, Governance Receipt, Execution Authorization, Controlled Governance Activation, or Commit Boundary result.

## 2. Authority and precedence

The following order applies to this companion:

1. AGCP Runtime Governance Conformance Requirements and AGCP Core;
2. `spec/AGCP-Policy-Evaluation-Contract.md` (IF-002);
3. this profile-specific machine contract;
4. `api/if-002/AGCP-WASM-PEC-Machine-Contract.json` and its envelope schemas;
5. the applicable Implementation Profile; and
6. implementation code and deployment overlays.

A deployment overlay may set bounded numeric resource values but SHALL NOT alter ABI signatures, canonical envelope semantics, prohibited capabilities, failure mappings, digest binding, or activation rules.

## 3. Contract identifiers and versioning

- Base interface identifier: `IF-002`.
- Base interface version: `v2`.
- Companion identifier: `IF-002-WASM-RUST-STUDENT-SERVICE-2.0.0`.
- Companion version: `1.0.0`.
- ABI identifier: `agcp_pec_abi_v1`.

Breaking ABI changes require a new ABI identifier and companion major version. Backward-compatible additions require a companion minor version and synchronized schemas and vectors. Clarifications that do not change observable behavior require a patch version.

## 4. Module format and required exports

The module format SHALL be WebAssembly Core 1.0 using `wasm32` linear memory. WASI, shared memory, memory64, threads, and component-model dependencies are outside ABI v1.

The module SHALL export exactly the following required ABI surface, in addition to any private non-exported functions:

| Export | Signature | Requirement |
|---|---|---|
| `memory` | WebAssembly memory | Required linear memory used only through the bounded conventions below. |
| `agcp_pec_abi_version_v1` | `() -> i32` | SHALL return `1`. |
| `agcp_alloc_v1` | `(i32 size) -> i32 ptr` | Allocates a bounded buffer in module memory. Zero or out-of-range pointers fail closed. |
| `agcp_dealloc_v1` | `(i32 ptr, i32 size) -> ()` | Releases a buffer previously returned by the module. |
| `agcp_evaluate_v1` | `(i32 input_ptr, i32 input_len) -> i64` | Evaluates the canonical input and returns the packed output pointer and length. |

The `i64` result of `agcp_evaluate_v1` SHALL be interpreted as:

`(uint64(output_ptr) << 32) | uint64(output_len)`

The high 32 bits contain `output_ptr`; the low 32 bits contain `output_len`. The host SHALL reject overflow, wraparound, zero-length output, out-of-bounds memory, output beyond the active output limit, or a pointer/length pair that changes during copying.

## 5. Memory ownership

1. The host SHALL canonicalize and validate the input envelope before invocation.
2. The host SHALL call `agcp_alloc_v1(input_len)` and copy exactly `input_len` bytes to the returned module-memory range.
3. The host SHALL invoke `agcp_evaluate_v1(input_ptr, input_len)` once per evaluation.
4. The module SHALL return one complete canonical output or controlled-failure envelope.
5. The host SHALL copy exactly the returned byte range, validate it, and call `agcp_dealloc_v1` for both input and output allocations.
6. No module pointer may address host memory, another module instance, or memory outside the active module instance.
7. Reused instances SHALL NOT expose prior-evaluation data. Hosts SHALL use fresh instances or zero reusable memory according to the runtime assurance design.

## 6. Canonical input envelope

The input SHALL validate against `api/if-002/AGCP-WASM-PEC-Input-Envelope.schema.json` and SHALL be serialized as UTF-8 RFC 8785 JCS bytes.

The envelope binds:

- companion identifier, companion version, and ABI version;
- evaluation identifier, tenant, and Governance Domain;
- Proposal Identity, Proposal version, and qualified-proposal digest;
- immutable Canonical State snapshot identifier, digest, resolution time, and source-manifest digest;
- active Governance Version, policy-set digest, Governance Configuration digest, Compiled Governance Artifact digest, and exact module digest;
- authoritative evaluation time supplied as input;
- Authority Lineage and Governance Evidence references; and
- exact fuel, linear-memory, output-size, and timeout limits used for the invocation.

No browser, process, environment, host-clock, network, filesystem, or mutable global value may influence evaluation unless it is represented in a qualified, digest-bound input field.

## 7. Canonical output and controlled failure envelopes

Successful module output SHALL validate against `api/if-002/AGCP-WASM-PEC-Output-Envelope.schema.json`, use UTF-8 RFC 8785 JCS, and bind the exact input digest and module digest.

The output may express policy satisfaction, non-satisfaction, Structural Refusal, governed human-adjudication requirement, deferral, or re-evaluation requirement. These are module evaluation results supplied to the Governance Decision Function; they are not independently authoritative Governance Outcomes.

A controlled module failure SHALL use `api/if-002/AGCP-WASM-PEC-Error-Envelope.schema.json`. Every failure SHALL set `authorization_permitted` to `false`.

## 8. Imports and prohibited capabilities

ABI v1 permits no WebAssembly imports. Modules containing any import SHALL be rejected before activation.

The prohibition includes, without limitation:

- WASI;
- network access;
- filesystem reads or writes;
- host clock or timer access;
- randomness;
- environment variables;
- process creation;
- dynamic linking;
- threads, atomics, or shared memory;
- direct host-state mutation; and
- unbounded memory growth.

All input and output transfer occurs through the exported linear-memory ABI. Deterministic fixed-point or domain helpers, if later required, require a new compatible contract revision and explicit import allowlist.

## 9. Resource limits and failure mapping

Numeric limits are deployment configuration, not generic AGCP constants. The exact applied values SHALL be authorized by controlled configuration, included in the input envelope, and recorded in Governance Evidence.

| Condition | Stable failure code | Required result |
|---|---|---|
| ABI or required-export mismatch | `ABI_INCOMPATIBLE` | Reject module or invocation; no authorization. |
| Invalid input envelope | `INVALID_INPUT` | Do not invoke or accept output. |
| Invalid output envelope | `INVALID_OUTPUT` | Discard output; no authorization. |
| Any module import | `PROHIBITED_IMPORT` | Reject before activation. |
| Module digest mismatch | `MODULE_DIGEST_MISMATCH` | Fail closed. |
| Fuel exhausted | `FUEL_EXHAUSTED` | Terminate evaluation; no authorization. |
| Linear-memory limit exceeded | `MEMORY_LIMIT_EXCEEDED` | Terminate evaluation; no authorization. |
| Wall-clock timeout | `TIMEOUT` | Host terminates evaluation; partial output is invalid. |
| WebAssembly trap | `WASM_TRAP` | Stable controlled failure; never Authorized. |
| Output-size limit exceeded | `OUTPUT_LIMIT_EXCEEDED` | Discard output; no authorization. |
| Runtime incompatibility | `RUNTIME_INCOMPATIBLE` | Refuse activation or invocation. |

Transport HTTP 503 is appropriate only when the evaluation service cannot safely begin processing. A module evaluation failure is not itself an authoritative Governance Outcome.

## 10. Module digest and traceability binding

The module digest SHALL be SHA-256 over the exact WebAssembly module bytes. The same digest SHALL be bound in:

- the DS-005 Policy Evaluation Module Artifact;
- the canonical input and output envelopes;
- validation and activation evidence;
- the active Governance Version and module-set manifest;
- any Execution Authorization that depends on the evaluation; and
- commit-time revalidation where the module remains material to admissibility.

Source policy, compiler, compiler version, runtime target, runtime version, compilation context, dependency set, and generated module digest SHALL remain traceable through DS-005, DS-042, DS-043, and applicable Governance Evidence.

## 11. Activation and rollback

A module SHALL NOT become authoritative merely because it is registered, loadable, or ABI-valid. Controlled Governance Activation SHALL atomically bind the validated module set with its policy set, Governance Configuration, Compiled Governance Artifact, Governance Version, and effective Governance Ledger event.

Partial activation visibility is prohibited. Rollback SHALL select a previously approved, validated, digest-pinned module set through the same controlled activation mechanism. Runtime-local substitution, hot swapping outside controlled activation, or fallback to an unpinned module is prohibited.

Activation-time precompilation is permitted only when the generated runtime artifact is target-specific, immutable, digest-bound, and traceable to the source module, compiler/runtime version, and activation record.

## 12. Replay and conformance

Replay evidence SHALL include:

- exact canonical input bytes and SHA-256 digest;
- exact module bytes or immutable module reference and digest;
- companion and ABI identifiers;
- runtime name and version;
- exact applied resource limits;
- exact canonical output or controlled-failure bytes and digest; and
- activation and Governance Version bindings.

Conformance SHALL include schema validation, ABI export validation, import rejection, canonicalization, module substitution, input mutation, output mutation, fuel, memory, timeout, trap, output-limit, activation, rollback, and cross-runtime replay tests.

The controlled vectors are published at `conformance/if-002/AGCP-WASM-PEC-Test-Vectors.json`.

## 13. Non-universality

This companion is adopted only by an Implementation Profile that names it. It SHALL NOT be interpreted as requiring all AGCP implementations to use WebAssembly, Rust, Wasmtime, the Rust Student Service topology, or any specific deployment limit.
