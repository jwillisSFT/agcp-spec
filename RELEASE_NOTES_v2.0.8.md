# AGCP v2.0.8 Release Notes

**Release target:** AGCP v2.0.8  
**Status:** Public Review Controlled Baseline  
**Artifact lifecycle:** CURRENT  
**Controlling baseline status:** PUBLIC_REVIEW_CONTROLLED_BASELINE  
**Baseline date:** 2026-08-14  
**Controlling baseline:** AGCP v2.0.8 Public Review Controlled Baseline, 2026-08-14  
**Released:** 2026-08-14

## v2.0.8 single-source release-version dependency closure

AGCP v2.0.8 completes the repository-wide release-version governance correction. The repository root `VERSION` file is the sole maintained source of current AGCP release identity. Executable release tooling derives the semantic version, release tag, RTM specification version, current release-note filename, synchronization artifact filenames, integrity-report filename, and current release context from that file through `governance/release_version.py`.

This release corrects release metadata, synchronization coverage, validation coverage, and packaging discipline. It does not add, remove, weaken, or otherwise alter AGCP normative runtime-governance requirements.

## 1. Root VERSION is authoritative

The root `VERSION` file contains `2.0.8`. Current-release tooling derives:

- semantic version `2.0.8`;
- release tag `v2.0.8`;
- RTM specification version `v.2.0.8`;
- current release notes `RELEASE_NOTES_v2.0.8.md`;
- current repository synchronization manifest and validation filenames; and
- current repository integrity-validation filename.

Current-release metadata SHALL NOT be independently maintained as a competing release authority.

## 2. Synchronization coverage expanded

The VERSION-driven synchronizer now covers the complete identified current-release metadata surface, including the previously synchronized catalogs, registries, specifications, OpenAPI contract, conformance manifest, implementation-profile package, RTM cells, repository indexes, and release lifecycle metadata, plus current conformance-harness release metadata and the current normative-companion disposition release identity.

Historical provenance records, historical release notes, historical validation records, and intentionally versioned fixture/example payload values remain historical and are not rewritten merely because the repository release changes.

## 3. Hard-coded current-release dependency audit

The release validation now checks that executable Python tooling outside `governance/release_version.py` does not contain the current semantic version as a literal release dependency. Historical-version literals used to validate historical records or describe historical corrections remain permitted when they do not control current release identity.

A separate repository-wide audit distinguishes current-release metadata from historical snapshots and semantic test/example data so historical evidence is not silently rewritten as current state.

## 4. v2.0.7 release-note disposition

No `RELEASE_NOTES_v2.0.7.md` artifact is published in this repository. The release-version governance and synchronization correction documented here is released as v2.0.8.

## 5. Release build discipline

After a change to root `VERSION`, the controlled release pipeline SHALL synchronize VERSION-derived metadata, refresh controlled source hashes to a fixed point, validate single-source version consistency, generate the VERSION-derived synchronization manifest, validate repository synchronization, run repository-wide integrity validation, and only then package the release archive.

A repository snapshot whose current-release metadata conflicts with root `VERSION` is not a completed controlled release payload.

## 6. Normative Statement inventory disposition retained

The controlled inventory remains **357 unique controlled Normative Statement identifiers** and **358 controlled normative source-text occurrences**. `NS-17.2-01` remains intentionally unassigned because the corresponding obligation is canonically represented by `NS-2.7-01`. This release does not alter that disposition.

## 7. Normative effect

AGCP v2.0.8 is a release-governance, metadata-synchronization, validation, and packaging correction. It does not change CR cardinality, Formal Test Case cardinality, conformance semantics, controlled runtime-governance behavior, or implementation obligations solely as a consequence of this correction.
