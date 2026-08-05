# AGCP v2.0.1 Repository Synchronization Update

**Date:** 2026-08-03  
**Repository release target:** v2.0.1  
**Status:** Unreleased accumulated correction set  
**Controlling published baseline:** v2.0.0 Public Review Controlled Baseline  
**RTM dataset:** RTM-1.46  
**Schema Catalog:** 1.0.50  
**Interface Catalog:** 1.0.5  
**Registry Entry Catalog:** 1.0.3  
**Implementation Profile Catalog:** 1.0.3

## Scope

This record closes execution-order Step 10 by synchronizing catalogs, hashes, RTM mappings, conformance vectors, validation reports, README and index files, manifests, and release records after completion of the substantive public-repository corrections. It does not add private CMU deployment or agcp-rs implementation artifacts.

## Findings synchronized

P0-01, P0-02, P0-05, P0-06, P0-10, P1-01, P1-03, P1-09, P1-12, P1-14, P1-17, P2-01, P2-02, P2-04, and P2-06.

## Controlled results

- 122 RTM rows identify `RTM-1.46` and specification version `v.2.0.1`.
- DS dispositions: 122 assigned, 0 N/A, 0 blank.
- IF dispositions: 84 assigned, 38 explicit N/A, 0 blank.
- REG dispositions: 117 assigned, 5 explicit N/A, 0 blank.
- Active schemas: 44; controlled registry entries: 94; controlled fixtures: 30.
- All active catalog hashes, profile-package hashes, validation-report source hashes, repository-relative links, and conformance-manifest paths are validated.
- The v2.0.1 worktree remains unreleased; the controlling published baseline remains v2.0.0.

## Step 11 integrity-report handling

The repository synchronization manifest excludes its own file, the generated synchronization report, and the generated repository-integrity report. These exclusions prevent recursive self-hashing while preserving complete coverage of every other distributed repository file. The synchronization validator also excludes the integrity report when checking embedded `source_hashes`; the final integrity validator independently verifies the synchronization manifest and report.
