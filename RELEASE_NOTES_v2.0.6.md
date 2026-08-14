# AGCP v2.0.6 Release Notes

**Release target:** AGCP v2.0.6  
**Status:** Public Review Controlled Baseline  
**Artifact lifecycle:** CURRENT  
**Controlling baseline status:** PUBLIC_REVIEW_CONTROLLED_BASELINE  
**Baseline date:** 2026-08-14  
**Controlling baseline:** AGCP v2.0.6 Public Review Controlled Baseline, 2026-08-14  
**Released:** 2026-08-14

## v2.0.6 release-version authority and repository synchronization correction

AGCP v2.0.6 corrects release-governance and repository-synchronization defects identified after publication of v2.0.5. The correction establishes the repository root `VERSION` file as the authoritative source for the current AGCP specification release and extends release synchronization so current-release metadata is derived from that source rather than maintained through independent hard-coded version values.

This release is a release-integrity and metadata-governance correction. It does not add, remove, weaken, or otherwise alter AGCP normative runtime-governance requirements.

## 1. Root VERSION file established as current-release authority

- Confirmed the repository root `VERSION` file as the authoritative source for the current AGCP specification release.
- Aligned current-release lifecycle metadata and the conformance manifest with the release version derived from `VERSION`.
- Preserved historical release artifacts and historical release-note content as historical records rather than rewriting them to the current release number.
- Prevented archive filenames, historical release notes, or stale embedded metadata from overriding the repository-controlled current-release version source.

## 2. Release-version synchronization expanded

Updated `governance/sync_release_version.py` so current-release metadata is synchronized from the root `VERSION` file across the controlled repository instead of requiring independent manual version edits.

The synchronization mechanism now covers, as applicable:

- Release lifecycle metadata.
- `conformance/agcp-conformance-manifest.yml`.
- OpenAPI release metadata.
- Schema Catalog metadata and machine-readable catalog records.
- Interface Catalog metadata and machine-readable catalog records.
- Registry Entry Catalog metadata and machine-readable catalog records.
- Controlled registry release envelopes.
- Implementation Profile catalog and manifest release metadata.
- Requirements Traceability Matrix specification-version cells.
- Current specification and companion-specification release headers.
- Current repository README and index metadata.
- Current synchronization-manifest references and generated validation metadata.

The synchronization process remains scoped to current-release metadata and does not rewrite historical release records.

## 3. Validator release-number hard-coding removed

- Removed remaining hard-coded v2.0.4 current-release assumptions from `governance/validate_repository_integrity.py`.
- Removed remaining hard-coded v2.0.4 current-release assumptions from `governance/validate_normative_companion_references.py`.
- Updated validation logic so current-release checks consume repository-controlled release identity rather than embedding an independently maintained release number.
- Retained explicit historical-version references where they describe historical artifacts rather than current-release state.

## 4. Current-release catalogs, registries, and specification metadata synchronized

Current controlled metadata was regenerated or synchronized so the repository presents one internally consistent release identity across:

- `api/AGCP-HTTP-Contract.yaml`.
- Interface catalogs and interface traceability validation.
- Schema catalogs and schema catalog machine-readable records.
- Registry catalogs and controlled registry JSON records.
- Implementation Profile catalogs and manifest.
- Current normative companion specification headers.
- Conformance mapping and fixture synchronization records.
- Requirements Traceability Matrix specification-version metadata.
- Governance validation records.
- Repository README and controlled index files.

This synchronization corrects release identity and controlled metadata only; it does not change the substantive meaning of the corresponding AGCP interfaces, schemas, registries, requirements, or test procedures.

## 5. v2.0.5 synchronization artifacts completed as the migration basis

The repository repair that forms the basis for v2.0.6 generated the previously absent v2.0.5 synchronization artifacts needed to establish a clean predecessor state:

- `governance/AGCP-v2.0.5-REPOSITORY-SYNCHRONIZATION-UPDATE.md`.
- `governance/AGCP-v2.0.5-repository-synchronization-manifest.json`.
- `governance/AGCP-v2.0.5-repository-synchronization-validation.json`.
- `governance/AGCP-v2.0.5-repository-integrity-validation.json`.

These artifacts document and validate the repaired v2.0.5 predecessor baseline from which the v2.0.6 release-version governance correction is made.

## 6. Validation results

After synchronization and validator correction, the repaired repository reached a stable validation fixed point: rerunning release synchronization produced no additional changes.

The controlled validation pipeline completed successfully with:

- Release lifecycle validation: **PASS, 37 of 37 checks**.
- Repository synchronization validation: **PASS, 12 of 12 checks**.
- Repository-wide integrity validation: **PASS, 11 of 11 checks**.
- AGCP assessment-runner baseline preflight: **PASS, 15 of 15 checks, zero baseline anomalies**.
- Controlled CR inventory discovered by the assessment runner: **122 requirements**.
- Controlled Formal Test Case inventory discovered through the RTM: **122 Formal Test Cases**.

These results demonstrate that the release-governance corrections restore a single internally consistent current-release identity suitable for controlled assessment baseline discovery.

## 7. Compatibility and normative effect

AGCP v2.0.6 is intended to be compatible with implementations and assessment targets evaluated against the substantive v2.0.5 governance requirements.

This release:

- Does not change CR cardinality.
- Does not change Formal Test Case cardinality.
- Does not introduce a new normative runtime-governance obligation.
- Does not weaken an existing normative obligation.
- Does not change the semantic meaning of existing DS, IF, or REG controlled artifacts solely as a consequence of this release correction.
- Does not alter the Normative Statement inventory disposition established in v2.0.5.
- Does not create an implementation conformance claim merely by publication.

The primary effect is to make release identity, lifecycle metadata, catalogs, validation tooling, and repository synchronization consistently governed by the repository root `VERSION` file.

## 8. Historical record preservation

Historical release notes, historical validation records, and prior-release identifiers remain historical artifacts. They SHALL NOT be rewritten merely because v2.0.6 becomes the current release.

Current-release automation SHALL derive the active release identity from the root `VERSION` file and SHALL distinguish current controlled state from historical provenance.
