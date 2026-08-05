# AGCP Release and Artifact Lifecycle Metadata Policy

**Status:** Controlled Engineering Policy  
**Policy Version:** 1.0.0  
**Finding:** P2-01  
**Repository Release Target:** AGCP v2.0.1  
**Repository Release Target Status:** Unreleased Accumulated Correction Set  
**Controlling Published Baseline:** AGCP v2.0.0 Public Review - Controlled Baseline  
**Baseline Date:** 2026-07-30  
**Artifact Lifecycle:** Current

## 1. Purpose

This policy separates metadata dimensions that were previously conflated across AGCP specifications, catalogs, registries, manifests, examples, validation reports, and release records.

## 2. Controlled dimensions

| Dimension | Controlled value for this worktree | Meaning |
|---|---|---|
| Repository release target | `v2.0.1` | Version to which the accumulated public-repository corrections are being applied. |
| Release-target status | `UNRELEASED_ACCUMULATED_CORRECTION_SET` | The v2.0.1 worktree has not yet been published. |
| Controlling published baseline | `v2.0.0` | Published baseline against which v2.0.1 corrections are accumulated. |
| Baseline release status | `PUBLIC_REVIEW_CONTROLLED_BASELINE` | Publication maturity of the controlling v2.0.0 baseline. |
| Baseline date | `2026-07-30` | Date of the controlling published baseline. |
| Current controlled-artifact lifecycle | `CURRENT` | Artifact is active in the current repository worktree. |
| Current catalog publication status | `CURRENT` | Catalog is the active catalog for the current worktree. |
| Current repository specification version | `2.0.1` | Version applied to current v2.0.1 specifications, interfaces, and catalogs. |

## 3. Rules

1. Publication maturity, artifact lifecycle, specification version, repository release target, and controlling baseline SHALL be represented as separate fields.
2. `Working Draft` SHALL NOT label an active controlled catalog or artifact in the current repository. It is reserved for an artifact intentionally outside the controlled current set.
3. The unreleased status of the v2.0.1 worktree SHALL NOT be represented as though the v2.0.1 release were already published.
4. The v2.0.0 published baseline SHALL remain explicitly identified until a v2.0.1 release decision supersedes it.
5. Implementation Profiles retain the lifecycle and status values defined by the Implementation Profile Specification and are not automatically promoted by repository metadata changes.
6. Historical `introduced_in_release`, superseded-release, and retired-artifact metadata SHALL be preserved.

## 4. Controlled machine-readable representation

The authoritative machine-readable policy is `governance/release-lifecycle-metadata.json`.
