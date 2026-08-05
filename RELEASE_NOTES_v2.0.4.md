# AGCP v2.0.4 Release Notes

**Release target:** AGCP v2.0.4  
**Status:** Public Review Controlled Baseline  
**Artifact lifecycle:** CURRENT  
**Controlling baseline status:** PUBLIC_REVIEW_CONTROLLED_BASELINE  
**Baseline date:** 2026-08-05  
**Controlling baseline:** AGCP v2.0.4 Public Review Controlled Baseline, 2026-08-05  
**Released:** 2026-08-05

## v2.0.4 public-release finalization

- Removed all non-public implementation-specific deployment artifacts and references while retaining the generic Implementation Profile framework and informational example.
- Removed stale references to deleted implementation-specific machine-contract companion artifacts and absent hosted workflow files.
- Corrected the repository synchronization validator so it accepts the controlled synchronization-manifest release context and produces the v2.0.4 report.
- Aligned the OpenAPI metadata, catalogs, registries, conformance assets, RTM specification-version column, validation records, repository indexes, and release-specific filenames to v2.0.4.
- Published v2.0.4 as the current Public Review Controlled Baseline dated 2026-08-05.

## 1. Scope of this accumulated change

This revision integrates the public Implementation Profile format, schema, template, informational example, catalogs, and validation required by findings P0-01, P1-14, P2-02, and P2-06. Private deployment profiles are outside the public repository.

## 2. Added controlled profile-format artifacts

- `implementer/AGCP-Implementation-Profile-Specification.md` - controlled profile format specification, version `1.1.0`.
- `implementer/AGCP-Implementation-Profile-Schema.json` - JSON Schema Draft 2020-12 serialization contract for format version `1.1.0`.

## 3. Template supersession

The misleading path `implementer/AGCP-Implementation-Decision-Record-Template.md` was removed and superseded by `implementer/AGCP-Implementation-Profile-Template.md`. The content now links to the controlled format specification and schema and states that material ADR/IDR decisions remain separately controlled records.

## 4. Catalog, manifest, and validation integration

Added:

- `implementer/README.md`;
- `implementer/IMPLEMENTATION-PROFILE-CATALOG.md`;
- `implementer/implementation-profile-catalog.json`;
- `implementer/implementation-profile-catalog.csv`;
- `implementer/implementation-profile-manifest.json`;
- `governance/validate_implementation_profiles.py`;
- `governance/AGCP-implementation-profile-validation.json`; and


The validator rejects prohibited YAML constructs, validates the authoritative YAML against the controlled schema, verifies canonical filenames and companion content, recomputes the profile content digest, enforces the lifecycle-dependent baseline-URI rule, and verifies the package manifest.

## 5. Repository indexes updated

Updated `README.md`, `ARCHITECTURE.md`, `conformance/agcp-conformance-manifest.yml`, and `governance/CHANGELOG.md` so the controlled profile package, catalog, manifest, validation script, and automated validation are discoverable through canonical repository paths.

## 6. Compatibility effect

This change is additive for public profile-format artifacts and the informational example. It does not establish an AGCP conformance claim.

## 8. P0-02 provenance wire/schema synchronization

- Made `spec/AGCP-Provenance-Wire-Format-Specification.md` and `schemas/common.json#/$defs/provenance` structurally identical.
- Replaced the nested signature object with top-level `kid` and `alg` plus a detached signature string.
- Added required `nonce` and `scope`, optional `expires_at`, exact verification rules, and RFC 8785 canonicalization.
- Updated all controlled wire-provenance examples and executable harness instances.
- Added real Ed25519 cross-language vectors and automated validation.
- Updated DS-001/IF-001 catalogs, DS-001 hash, CR-005 RTM mapping, validation records, and public repository references.

## P0-06 command-versus-authoritative-record separation

- Added DS-045 `governance_approval_submission.json` as the sole IF-001 governance-approval ingress schema.
- Changed the governance-approval POST operation to accept DS-045 rather than DS-026.
- Strengthened DS-026 with `artifact_origin: AGCP_CREATED_OR_QUALIFIED`.
- Added claimant-field rejection vectors, harness updates, RTM mappings, catalog updates, CI, and controlled validation.

## P1-12 algorithm-specific content digest enforcement

- Tightened `schemas/common.json#/$defs/content_digest` so SHA-256 and BLAKE2B-256 require 64 lowercase hexadecimal characters, SHA-384 requires 96, and SHA-512 and BLAKE2B-512 require 128.
- Rejected uppercase hexadecimal, non-hexadecimal values, ambiguous `BLAKE2B`, missing fields, undeclared fields, and every algorithm/value length mismatch.
- Deprecated algorithm-implicit `hash_hex` for new contracts and limited retained uses to lowercase 64-, 96-, or 128-character values.
- Added controlled examples, conformance vectors, OpenAPI registration, RTM and Test Case mappings, validation, and automated checks.

## P1-03, P1-09, P1-14, and P1-17 - Public Error and Metadata Reconciliation

- Normalized public protected-resource lookup failures to `404 RESOURCE_NOT_FOUND`; resource-specific not-found codes are deprecated for public IF-001 use.
- Added `429 REQUEST_THROTTLED` with required delay-seconds `Retry-After` and `503 CAPACITY_UNAVAILABLE`.
- Distinguished transport/service rejection from authoritative Governance Outcomes; governance quota or entitlement denial remains a governance result.
- Expanded DS-003 to bind immutable baseline and profile digests, schema and generated-validator digests, active governance version, and optional public-safe deployment binding.
- Added reusable vectors, RTM/test mappings, validation, CI, catalogs, and registry release v2.0.4.

## P0-10 - Semantic fixture correction

- Corrected 14 positive fixtures with conflicting placeholder identities.
- Added semantic equality rules for Tenant, Governance Domain, Proposal, target, policy, approval, evidence, authorization, lifecycle state, and Canonical State bindings.
- Added 10 structurally valid semantic-mismatch negative vectors.
- Integrated the existing 15 claimant-assertion negative vectors from P0-06.
- Added automated validation and automated validation enforcement.

## P1-01 - Normative companion reference integrity

- Dispositioned every active reference to absent umbrella security and governance-evidence companions.
- Replaced those labels with exact existing controlled artifacts, including the Core, Provenance Wire Format, Multitenant Operational, Error Mapping, Append-Only Governance Ledger, DS-020 Governance Evidence, and DS-033 Evidence Qualification Result.
- Normalized the human-adjudication companion to its canonical title and path.
- Added controlled human-readable and machine-readable reference dispositions, repository-wide validation, and automated validation enforcement.
- Verified that schemas, OpenAPI, registries, controlled examples, catalogs, the RTM workbook, and Office-document text contain no unresolved active companion references.


## P2-01 - Release and lifecycle metadata alignment

- Separated the v2.0.4 repository release target from the controlling v2.0.0 Public Review Controlled Baseline.
- Standardized active controlled-artifact lifecycle as `CURRENT`, catalog publication status as `CURRENT`, and current repository specification version as `2.0.4`.
- Advanced the Schema Catalog to `1.0.49`, Interface Catalog to `1.0.4`, and Registry Entry Catalog to `1.0.2`.
- Removed unexplained `Working Draft` labels from active schema-catalog and DS-003 metadata artifacts.
- Aligned normative specification headers, OpenAPI metadata, catalogs, registry metadata, conformance manifest, validation records, repository indexes, and release notes.
- Added controlled metadata policy, machine-readable values, validation, and automated validation enforcement.


## Step 10 - Cross-artifact repository synchronization

- Advanced the Requirements Traceability Matrix dataset to `RTM-1.46` and synchronized all 122 rows to specification version `v.2.0.4`.
- Advanced the Schema Catalog to `1.0.50`, Interface Catalog to `1.0.5`, Registry Entry Catalog to `1.0.3`, and Implementation Profile Catalog to `1.0.3`.
- Added the controlled repository synchronization manifest, validator, report, and automated validation.
- Regenerated current catalog, fixture, test-mapping, companion-disposition, traceability, profile-manifest, and validation records.
- Synchronized README/index files, conformance manifest, hashes, release notes, and change history for findings P0-01, P0-02, P0-05, P0-06, P0-10, P1-01, P1-03, P1-09, P1-12, P1-14, P1-17, P2-01, P2-02, P2-04, and P2-06.


## Step 11 - Repository-wide integrity validation and correction summary

- Added `governance/validate_repository_integrity.py` and `governance/AGCP-v2.0.4-repository-integrity-validation.json` as the final repository-wide integrity gate.
- Re-ran every finding-specific validator and confirmed that Implementation Profile, provenance, command/record, digest, public error/metadata, semantic-fixture, normative-reference, release/lifecycle, and synchronization reports remain current and passing.
- Verified JSON/YAML parsing, Draft 2020-12 schemas, local JSON Schema and OpenAPI references, repository-relative Markdown links, synchronization-manifest coverage, active-schema hashes, RTM versions and DS/IF/REG dispositions, controlled report source hashes, and absence of byte-identical duplicate or transitional payloads.
- Registered the final integrity controls in the conformance manifest, README/index files, repository architecture, release notes, and change history.
- Published v2.0.4 as the Public Review Controlled Baseline; publication does not by itself create an implementation conformance claim.
- Final repository-wide integrity result: `PASS`, 11 of 11 checks, 23 controlled validation reports, 3,794 local references, 165 repository-relative Markdown links, 48 controlled JSON Schemas, 217 controlled source hashes, zero duplicate-byte groups, and zero transitional filenames.
