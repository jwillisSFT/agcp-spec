# AGCP Specification Changelog

This document records versioned changes to the AGCP specification set.

The versioning model follows Semantic Versioning:

MAJOR.MINOR.PATCH

Compatibility rules and governance procedures are defined in:

/governance/AGCP-Versioning.md

---

# Version 0.9.0

Release Date: 2026-02-25  
Compatibility: Initial Public Review Release

## Summary

Initial public specification release of the AGCP Core architecture and supporting profiles.

This release establishes the normative baseline for public review and implementation prototyping.

## Specification Documents

The following documents are included in this release:

- AGCP-Core
- AGCP-HTTP-Interface
- AGCP-PEC
- AGCP-Security-Profile
- AGCP-Multitenant-Profile
- AGCP-Conformance
- AGCP-Versioning-and-Governance

## Schema Bundle

Version: 0.9.0

Includes:

- ActionEnvelope schema
- HITL token schema
- Operational profile schema
- Supporting schema definitions

## Registry Bundle

Includes the following registries:

- Rejection Code Registry
- Constraint Type Registry
- Invariant Type Registry

## Conformance Framework

Includes:

- Conformance Harness Specification
- Assertion Registry
- Requirement mapping
- Test matrix

## Compatibility Notes

This is the first public release. No backward compatibility constraints apply.

---

# Changelog Format

Future entries MUST follow this format.

Each release entry SHOULD include:

Version number  
Release date  
Compatibility classification (MAJOR / MINOR / PATCH)

Sections:

Summary  
Specification Changes  
Schema Changes  
Registry Changes  
Conformance Changes  
Security Changes  
Compatibility Impact  
Migration Guidance (if required)

---

# Example Entry (Future Release)

## Version 0.10.0

Release Date: YYYY-MM-DD  
Compatibility: MINOR

### Summary

Added support for additional invariant types.

### Specification Changes

- Clarified PEC invariant evaluation ordering.
- Added new invariant enforcement guidance.

### Schema Changes

- Added optional field `invariant_parameters`.

### Registry Changes

- Added new invariant type `core.resource_quota`.

### Conformance Changes

- Added new conformance assertion `A-INVARIANT-PARAMETERS`.

### Compatibility Impact

Backward compatible within MAJOR version.

### Migration Guidance

Existing implementations do not require modification.
