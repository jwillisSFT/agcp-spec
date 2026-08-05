# IF-002 Deterministic WASM Machine Contract

This directory contains the machine-readable contract and envelope schemas for the controlled profile companion `IF-002-WASM-RUST-STUDENT-SERVICE-2.0.0`.

The companion specializes the implementation-independent `IF-002` Policy Evaluation Contract for the proposed Rust Student Service profile. It does not make WebAssembly or the selected ABI universal AGCP requirements.

Controlled artifacts:

- `AGCP-WASM-PEC-Machine-Contract.json` - ABI, exports, memory ownership, deterministic restrictions, failure mapping, activation, rollback, and compatibility.
- `AGCP-WASM-PEC-Input-Envelope.schema.json` - canonical qualified input envelope.
- `AGCP-WASM-PEC-Output-Envelope.schema.json` - canonical module result envelope.
- `AGCP-WASM-PEC-Error-Envelope.schema.json` - stable controlled failure representation.

The normative human-readable companion is `spec/AGCP-WASM-Policy-Evaluation-Machine-Contract.md`.
