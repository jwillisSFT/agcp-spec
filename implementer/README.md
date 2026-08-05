# AGCP Implementation Profiles

This directory contains the public Implementation Profile format, schema, template, informational example, catalogs, and package-integrity records. Implementation Profiles are lower precedence than the published AGCP Runtime Governance Conformance Requirements, the AGCP Core Specification, and applicable adopted normative Companion Specifications.

Profile-format validation establishes serialization validity only. It does not establish AGCP conformance.


## Controlled format artifacts

- [`AGCP-Implementation-Profile-Specification.md`](./AGCP-Implementation-Profile-Specification.md) - format authority, lifecycle, canonicalization, consistency, and change-control rules; version `1.1.0`.
- [`AGCP-Implementation-Profile-Schema.json`](./AGCP-Implementation-Profile-Schema.json) - JSON Schema Draft 2020-12 structure for format version `1.1.0`.
- [`AGCP-Implementation-Profile-Template.md`](./AGCP-Implementation-Profile-Template.md) - human-readable authoring template; supersedes the misleading filename `AGCP-Implementation-Decision-Record-Template.md`.

## Informational example

- [`AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-PROFILE.md`](./AGCP-FULL-SCOPE-MULTITENANT-EXAMPLE-PROFILE.md) - non-normative worked example; not an operational deployment or conformance claim.

## Catalog and manifest

- [`IMPLEMENTATION-PROFILE-CATALOG.md`](./IMPLEMENTATION-PROFILE-CATALOG.md) - human-readable profile catalog.
- [`implementation-profile-catalog.json`](./implementation-profile-catalog.json) - machine-readable catalog.
- [`implementation-profile-catalog.csv`](./implementation-profile-catalog.csv) - tabular catalog representation.
- [`implementation-profile-manifest.json`](./implementation-profile-manifest.json) - exact SHA-256 and byte-size manifest for the public profile package.

## Validation


The validator:

1. rejects YAML aliases, anchors, explicit tags, merge keys, duplicate keys, non-finite values, and non-JSON data types;
2. converts the YAML to the JSON data model;
3. validates the profile against the controlled JSON Schema;
4. verifies public artifact paths and catalog consistency;
5. checks that no private deployment profile is included; and
6. verifies the profile package manifest hashes.

## Repository synchronization

- Repository release target: `v2.0.1`
- RTM dataset: `RTM-1.46`
- Profile catalog: `1.0.3`
- Package manifest: `1.0.3`
