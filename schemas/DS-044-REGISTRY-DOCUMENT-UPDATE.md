# DS-044 Registry Document Update

## Status

Implemented and validated for AGCP v2.0.

## Canonical schema

- DS ID: DS-044
- File: `schemas/registry_document.schema.json`
- Canonical URI: `https://agcp.ai/schemas/registry_document.schema.json`

## Registry cleanup

The three duplicate registry payloads were removed from `schemas/`. Their authoritative copies remain under `registries/` and now declare DS-044 as their validator.

- `registries/constraint-type-registry.json` — 26 entries
- `registries/invariant-type-registry.json` — 26 entries
- `registries/rejection-code-registry.json` — 40 entries

## Canonical controls

DS-044 validates stable REG identity, explicit release and lifecycle state, document and entry-set integrity, source and requirements traceability, registry rules, field definitions, entry lifecycle metadata, and typed specialized entry structures. It provides the canonical `registry_document_ref`.

## Clean migration

`common.json#/$defs/registry_id` and `common.json#/$defs/registry_ref` were removed. All consumers now reference `registry_document.schema.json#/$defs/registry_document_ref`. No compatibility aliases remain.

## Traceability

DS-044 maps to CR-004, CR-063, CR-076, and CR-110. The RTM was advanced to RTM-1.38 and the REG_ID column now records the authoritative registry identities for those mappings.

## Validation

- 44 Draft 2020-12 schemas validated.
- 3245 references and JSON Pointer fragments resolved.
- All three registry documents passed schema, uniqueness, entry-digest, entry-set-digest, and document-digest checks.
- Duplicate registry payload mirrors under `schemas/`: 0.
- Unused common definitions: 0.
