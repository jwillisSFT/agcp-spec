# Reference Artifacts

**Status:** Informational\
**Repository Versioning:** Repository Release Governed

## Purpose

This directory contains informational reference materials that assist
implementers, reviewers, researchers, and tool developers in
understanding and implementing the AGCP specifications.

Reference artifacts are intended to clarify concepts, illustrate
implementation strategies, and provide educational guidance. They are
**not normative** and do not create additional implementation
requirements.

Where any reference artifact differs from a normative specification, the
normative specification always takes precedence.

------------------------------------------------------------------------

# Reference Contents

Reference artifacts may include, but are not limited to:

-   deterministic pseudocode
-   architecture reference models
-   implementation examples
-   workflow illustrations
-   design notes
-   explanatory diagrams
-   optimization guidance
-   deployment patterns
-   interoperability examples
-   educational and tutorial material

The specific contents of this directory may evolve between repository
releases without changing normative behavior.

------------------------------------------------------------------------

# Relationship to the AGCP Specifications

The authoritative AGCP requirements are defined by the specifications
contained in:

``` text
/spec/
```

Reference artifacts are intended to help explain or implement those
specifications but SHALL NOT:

-   modify normative requirements;
-   redefine normative terminology;
-   introduce new conformance requirements;
-   alter protocol semantics; or
-   supersede published specifications.

------------------------------------------------------------------------

# Implementation Freedom

Implementations are free to diverge from the approaches illustrated in
this directory provided they satisfy all applicable normative
requirements.

Implementations MAY differ in:

-   software architecture;
-   programming language;
-   deployment model;
-   storage technology;
-   execution environment;
-   networking architecture;
-   cryptographic library selection;
-   optimization techniques; and
-   operational tooling.

Conformance is determined by externally observable behavior, not by
internal implementation details.

------------------------------------------------------------------------

# Deterministic Behavior Requirement

Regardless of implementation strategy, conformant implementations SHALL
preserve the externally observable behavior defined by the AGCP
specifications.

This includes, where applicable:

-   deterministic governance evaluation;
-   deterministic Proposal Qualification;
-   deterministic Governance Decision behavior;
-   Human Review enforcement;
-   Execution Authorization semantics;
-   Commit Boundary enforcement;
-   Governance Evidence generation;
-   provenance verification;
-   ordered Append-Only Governance Ledger behavior;
-   Canonical State derivation from ordered ledger history (or a
    verifiable materialized state reproducible from that history);
-   deterministic replay behavior; and
-   tenant and Governance Domain isolation.

Internal implementation differences SHALL NOT alter these externally
observable behaviors.

------------------------------------------------------------------------

# Canonical State

Reference implementations and examples SHOULD reflect the AGCP
architectural principle that Canonical State is derived from the ordered
Append-Only Governance Ledger, or from a verifiable materialized state
whose derivation can be deterministically reproduced from ordered ledger
entries.

Reference artifacts SHOULD NOT illustrate architectures that derive
authoritative state from timestamp ordering or other non-authoritative
ordering mechanisms.

------------------------------------------------------------------------

# Relationship to Conformance

Reference artifacts do not participate directly in conformance
evaluation.

Conformance is established through the authoritative traceability chain:

``` text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

Executable Harness Checks and Harness Test Vectors verify implementation
behavior but do not alter the normative requirements.

------------------------------------------------------------------------

# Intended Audience

This directory is intended for:

-   implementers
-   architects
-   system integrators
-   framework developers
-   researchers
-   educators
-   reviewers
-   certification teams

------------------------------------------------------------------------

# Repository Versioning

Reference artifacts follow repository-release versioning.

They may evolve between repository releases to improve clarity,
educational value, or implementation guidance without changing normative
AGCP behavior.

------------------------------------------------------------------------

# Notes

Reference artifacts are explanatory rather than prescriptive.

Implementers are encouraged to use these materials as guidance while
relying on the normative specifications for all conformance-critical
behavior.
