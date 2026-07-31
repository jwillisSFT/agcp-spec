# DS-003 Implementation Metadata Response Update

## Status

Implemented and validated for the AGCP v2.0 schema set on 2026-07-30.

## Purpose

`meta_response.json` is now the canonical implementation-capability and release-advertisement response used by the AGCP HTTP metadata endpoint. It no longer relies on repository tags alone or state that supported specification versions are intentionally omitted.

## Required Advertisements

DS-003 requires the response to identify:

- the implementation and implementation release;
- every supported AGCP specification release and the default release;
- the complete schema-set identity, catalog version, manifest, schema count, and integrity digests;
- each advertised schema's DS identifier, filename, canonical URI, lifecycle state, and content digest;
- the claimed implementation profile and its integrity digest;
- supported constraint-type, invariant-type, and rejection-code registry releases through DS-044;
- supported conformance levels L1 through L5;
- conformance claims, scope, test-suite release, evidence, and verification status;
- supported governance capabilities and capability evidence;
- the implemented HTTP contract, OpenAPI version, path versions, media types, and contract digest;
- attribution, provenance, response digest, and integrity signature.

## Claim Integrity

Outcome-specific schema rules require evidence for claimed, partially verified, and verified conformance claims. A verified claim additionally requires an assessed status, verification time, verification authority, and Conformance Test Suite release.

A capability marked `VERIFIED` must include Governance Evidence. Advertising L5 support requires an L5 conformance claim. The three current normative registry classes must all be advertised.

## Semantic Boundaries

DS-003 states that metadata:

- does not establish authority at commitment;
- does not authorize execution;
- is not Canonical State;
- cannot expand conformance beyond demonstrated scope;
- cannot use an Implementation Profile to redefine mandatory Core behavior;
- cannot use namespaced extensions to alter canonical governance meaning.

## Integration Changes

- OpenAPI `MetadataResponse` now references `../schemas/meta_response.json`.
- OpenAPI exposes `MetadataResponseRef` from DS-003.
- The metadata endpoint description now identifies release, schema-set, registry, profile, conformance, capability, and interface advertisements.
- The Schema Catalog advanced to version 1.0.38.
- RTM-00089 and RTM-00090 now reference DS-003 and the authoritative schema and HTTP-contract files.
- The RTM dataset advanced to RTM-1.41.

## Traceability

### ARM

- ARM-701 Deterministic Governance
- ARM-707 Technology, Transport, and Node Independence
- ARM-708 Architectural Extensibility

### Normative Statements

DS-003 traces principally to Core Section 17 and NS-17.1-01 through NS-17.10-02, including the requirements to identify the claimed Implementation Profile, supported capabilities, applicable Companion Specifications, conformance scope, specification version, and supporting objective evidence.

### Conformance Requirements

- CR-089 Implementation Passes AGCP Conformance Suite
- CR-090 Independent Implementations Produce Equivalent Outcomes

## Validation Summary

- 44 Draft 2020-12 schemas passed metaschema validation.
- 3,477 schema references and JSON Pointer fragments resolved.
- A complete v2.0 metadata response passed.
- Missing release, schema hash, registry, claim evidence, capability evidence, profile integrity, and response-integrity information were rejected.
- Unrestricted `metadata` was rejected.
- OpenAPI references resolved.
- All 63 common definitions remained actively reachable.
- RTM structure and formatting were preserved.
