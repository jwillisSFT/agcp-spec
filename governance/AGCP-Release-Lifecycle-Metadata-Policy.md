# AGCP Release and Artifact Lifecycle Metadata Policy

**Status:** Controlled Engineering Policy  
**Policy Version:** 1.1.0  
**Finding:** P2-01  
**Repository Release Target:** AGCP v2.0.5  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.5 Public Review - Controlled Baseline  
**Baseline Date:** 2026-08-05  
**Artifact Lifecycle:** Current

## 1. Purpose

This policy separates repository release identity, publication maturity, artifact lifecycle, catalog publication state, and historical introduction or retirement metadata.

## Authoritative version source

The root `VERSION` file is the sole maintained repository release number. Current-release labels in machine-readable metadata, validation output filenames, RTM specification-version cells, and build-controlled release metadata are generated or validated from `VERSION`. Historical release notes and historical records retain their published release identity.


## 2. Controlled dimensions

| Dimension | Controlled value for this release | Meaning |
|---|---|---|
| Repository release target | `v2.0.5` | Current repository release identity. |
| Release-target status | `PUBLIC_REVIEW_CONTROLLED_BASELINE` | The tagged repository release is the current controlled public-review baseline. |
| Controlling published baseline | `v2.0.5` | The release governs the artifacts contained in this repository snapshot. |
| Baseline release status | `PUBLIC_REVIEW_CONTROLLED_BASELINE` | Publication maturity of the controlling baseline. |
| Baseline date | `2026-08-05` | Date of the controlled release snapshot. |
| Current controlled-artifact lifecycle | `CURRENT` | Artifact is active in this repository release. |
| Current catalog publication status | `CURRENT` | Catalog is the active catalog for this repository release. |
| Current repository specification version | `2.0.5` | Version applied to current specifications, interfaces, catalogs, and release metadata. |

## 3. Rules

1. Publication maturity, artifact lifecycle, specification version, repository release target, and controlling baseline SHALL be represented as separate fields.
2. `Working Draft` SHALL NOT label an active controlled catalog or artifact in this release.
3. Historical `introduced_in_release`, superseded-release, and retired-artifact metadata SHALL be preserved as release history.
4. Implementation Profiles retain the lifecycle and status values defined by the Implementation Profile Specification and are not automatically promoted by repository metadata changes.
5. The release tag, release archive, checksum publication, and repository content SHALL identify the same `v2.0.5` artifact set.

## 4. Controlled machine-readable representation

The authoritative machine-readable policy is `governance/release-lifecycle-metadata.json`.
