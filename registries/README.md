# Registries

**Status:** Normative  
**Artifact Lifecycle:** Current  
**Publication Status:** CURRENT  
**Repository Release Target:** AGCP v2.0.8  
**Repository Release Target Status:** Public Review Controlled Baseline  
**Controlling Published Baseline:** AGCP v2.0.8 Public Review Controlled Baseline  
**Controlling Baseline Status:** PUBLIC_REVIEW_CONTROLLED_BASELINE  
**Baseline Date:** 2026-08-14  
**Repository Versioning:** Repository Release Governed

## Purpose

This directory contains the published AGCP registries used to define
controlled vocabularies, stable identifiers, and enumerated values
referenced by the normative specifications.

Registries promote interoperability by ensuring that conformant
implementations interpret registered values consistently while
preserving implementation freedom for internal architectures.

Where a normative specification references a registry, implementations
SHALL interpret registered values according to that registry.

------------------------------------------------------------------------


## Canonical Validation

Every JSON registry document in this directory SHALL validate against:

```text
../schemas/registry_document.schema.json
```

Each registry document carries stable registry identity, explicit release and lifecycle metadata, integrity digests, document-level traceability, and typed entry metadata. Every normative entry also carries a permanent `REG-NNN` identifier and direct NS and CR references. Registry payloads SHALL NOT be duplicated under `schemas/`. Implementations SHALL verify the declared document and entry-set digests before using a registry release.

------------------------------------------------------------------------


## Entry Identifiers and Traceability

The active registry-entry namespace is cataloged in:

```text
registry-entry-catalog.json
registry-entry-catalog.csv
REGISTRY-ENTRY-CATALOG.md
```

The current catalog assigns `REG-001` through `REG-094`. Each entry records `ns_refs` and `cr_refs`; release-level traceability SHALL NOT be used as a substitute for the entry-level mappings. REG identifiers are permanent and SHALL NOT be reused.

------------------------------------------------------------------------

# Registry Contents

Depending on the repository release, this directory may include
registries such as:

-   Constraint Type Registry
-   Invariant Type Registry
-   Rejection Code Registry
-   Governance Stage Registry
-   Governance Evidence Type Registry
-   Governance Approval Role Registry
-   Policy Evaluation Registry
-   Additional implementation-independent controlled vocabularies

The exact set of registries may expand in future releases.

------------------------------------------------------------------------

# Relationship to the Specifications

Registries complement the specifications by defining controlled values
used throughout AGCP.

Normative behavior is defined by the specifications under:

``` text
/spec/
```

Registries define the allowable identifiers and values referenced by
those specifications but do not independently introduce new behavioral
requirements.

------------------------------------------------------------------------

# Stability

Registered identifiers SHOULD remain stable across repository releases.

When changes are necessary:

-   Existing identifiers SHOULD NOT be repurposed.
-   Deprecated identifiers SHOULD remain documented until formally
    removed.
-   New identifiers SHOULD be additive whenever practical.
-   Breaking registry changes SHOULD accompany an appropriate repository
    release.

------------------------------------------------------------------------

# Conformance

Where a specification requires the use of a published registry:

-   Registered identifiers SHALL be recognized.
-   Unknown values SHALL be handled according to the applicable
    specification.
-   Validation behavior SHALL remain deterministic.

The AGCP Conformance Harness verifies registry usage where applicable.

------------------------------------------------------------------------

# Machine-Readable Use

Registry files are intended to support:

-   schema validation
-   policy validation
-   conformance testing
-   automated tooling
-   documentation generation
-   implementation interoperability

Implementations MAY cache registry contents but SHOULD remain
synchronized with the repository release they implement.

------------------------------------------------------------------------

# Repository Versioning

Registries follow repository-release versioning.

Repository releases define the authoritative registry contents
applicable to that release.

------------------------------------------------------------------------

# Notes

Registries define standardized identifiers and controlled vocabularies
used throughout AGCP.

They improve interoperability, consistency, and long-term compatibility
without constraining implementation architecture beyond the normative
requirements of the specifications.

## v2.0.4 Public Error Contract

The rejection-code registry release `v2.0.4` normalizes every public protected-resource lookup to `RESOURCE_NOT_FOUND`, deprecates resource-specific not-found codes for public IF-001 use, and adds `REQUEST_THROTTLED` (429 plus required Retry-After) and `CAPACITY_UNAVAILABLE` (503). Transport/service conditions are not authoritative Governance Outcomes.
