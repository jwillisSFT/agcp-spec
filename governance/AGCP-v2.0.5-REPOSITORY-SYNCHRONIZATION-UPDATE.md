# AGCP v2.0.5 Repository Synchronization Update

**Date:** 2026-08-14  
**Repository release target:** v2.0.5  
**Version source:** `VERSION`  
**Status:** Public Review Controlled Baseline synchronization  
**Controlling published baseline:** v2.0.5 Public Review Controlled Baseline  
**Baseline date:** 2026-08-05  
**RTM dataset:** RTM-1.46  
**Schema Catalog:** 1.0.50  
**Interface Catalog:** 1.0.5  
**Registry Entry Catalog:** 1.0.3  
**Implementation Profile Catalog:** 1.0.3

## Scope

This record closes the v2.0.5 repository synchronization step after aligning current-release identity to the root `VERSION` file. It synchronizes current release metadata, RTM specification-version cells, catalog and registry release metadata, conformance-manifest metadata, generated release validation records, source hashes, repository synchronization artifacts, and repository-wide integrity validation. Historical release records remain historical and are not rewritten as current-release records.

## Version-source correction

The root `VERSION` file is the sole maintained repository release number. For this repository snapshot it contains `2.0.5`, which yields release tag `v2.0.5` and RTM specification version `v.2.0.5`.

Current-release build and validation tooling derives release identity from `governance/release_version.py`. Validators and generated report filenames do not maintain an independent hard-coded current AGCP release number.

## Controlled results

- 122 RTM rows identify `RTM-1.46` and specification version `v.2.0.5`.
- DS dispositions: 122 assigned, 0 N/A, 0 blank.
- IF dispositions: 84 assigned, 38 explicit N/A, 0 blank.
- REG dispositions: 117 assigned, 5 explicit N/A, 0 blank.
- Active schemas: 44; controlled registry entries: 94; controlled fixtures: 30.
- Current Schema, Interface, Registry Entry, and Implementation Profile catalogs identify the v2.0.5 repository release.
- Current controlled registry documents identify v2.0.5 and carry recomputed integrity digests.
- The conformance manifest identifies `VERSION` as its release-version source.
- Release lifecycle metadata is generated from `VERSION`.
- Repository synchronization and repository-wide integrity reports are generated under v2.0.5 filenames.

## Historical release preservation

Release-specific v2.0.0, v2.0.1, and v2.0.4 notes, synchronization records, and integrity records remain historical provenance artifacts. Historical descriptions of corrections introduced or resolved in v2.0.4 remain unchanged where they describe that historical release rather than current repository identity.
