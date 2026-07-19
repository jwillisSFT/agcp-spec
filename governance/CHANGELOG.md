# AGCP Specification Changelog

**Status:** Informational  
**Current Published Normative Release:** v2.0.0

---

# Purpose

This document records the published release history of the Artificial Intelligence Governance Control Plane (AGCP).

Each published release identifies the normative specification set, schemas, registries, conformance artifacts, and supporting documentation applicable to that release.

Versioning follows Semantic Versioning (MAJOR.MINOR.PATCH).

The governing rules for versioning, compatibility, and release management are defined in:

`governance/AGCP-Versioning.md`

---

# Version 2.0.0

**Release Status:** Current Published Normative Release

## Summary

Version 2.0.0 represents the current published normative AGCP release.

This release introduces the governance progression architecture centered on Proposal Qualification, Governance Decision Function, Human Review, Execution Authorization, Commit Boundary, Governance Evidence, the Append-Only Governance Ledger, and Canonical State derived from the ordered ledger.

## Major Highlights

- Governance progression model
- Canonical State architecture
- Ordered Append-Only Governance Ledger
- Governance Evidence framework
- Updated conformance architecture
- Repository-wide documentation modernization

---

# Version 1.0.3

**Release Status:** Public Normative Release

## Summary

Version 1.0.3 represents the mature public AGCP 1.x specification series.

This release stabilized the core governance architecture and provided the basis for subsequent architectural evolution incorporated into Version 2.0.0.

---

# Version 0.9.0

**Release Status:** Initial Public Review

## Summary

Version 0.9.0 was the initial public review release.

It established the initial public specification set and solicited implementation and community feedback that informed the Version 1.x and Version 2.x releases.

---

# Changelog Format

Future releases SHOULD include:

- Version
- Release Date
- Release Status
- Summary
- Normative Specification Changes
- Schema Changes
- Registry Changes
- Conformance Changes
- Documentation Changes
- Security Changes
- Compatibility Impact
- Migration Guidance (if applicable)

---

# Example Future Entry

## Version 2.1.0

**Release Status:** Minor Release

### Summary

Adds backward-compatible governance capabilities and clarifications.

### Normative Specification Changes

- Clarified Governance Decision Function semantics.
- Expanded Human Review guidance.

### Schema Changes

- Added optional governance metadata fields.

### Registry Changes

- Added new governance evidence type.

### Conformance Changes

- Added new Conformance Requirements and Test Cases.

### Documentation Changes

- Expanded implementation guidance.

### Compatibility Impact

Backward compatible within the Version 2 MAJOR release.

### Migration Guidance

Existing Version 2.0.x implementations remain compatible without modification.
