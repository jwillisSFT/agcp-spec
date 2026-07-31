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

Where a reference artifact differs from another AGCP source, the conflict SHALL be resolved using the Core-defined precedence order: published CRs; Core Specification; applicable adopted normative Companion Specifications; Implementation Profiles; Conformance Test Suite; and Reference Implementations. The ARM governs architectural terminology and concept meaning. Normative Statements are Core-derived extraction and traceability artifacts rather than an independently superior source.

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

The authoritative normative requirements are established first by the published CRs and then by the Core Specification, together with any applicable normative Companion Specifications expressly adopted by an implementation profile. The ARM provides the authoritative architectural vocabulary and conceptual reference. The `/spec/` directory contains the Core, ARM, Normative Statements, and Companion Specifications, while the controlled CR dataset and RTM provide normative capability requirements and authoritative traceability respectively.

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
-   Governance Approval enforcement;
-   Execution Authorization semantics;
-   Commit Boundary enforcement;
-   Governance Evidence generation;
-   provenance verification;
-   ordered Append-Only Governance Ledger behavior;
-   Canonical State resolution from qualified authoritative governance
    sources, including authoritative ledger ordering for incorporated
    governance events and Derived Lifecycle State;
-   deterministic replay behavior; and
-   tenant and Governance Domain isolation.

Internal implementation differences SHALL NOT alter these externally
observable behaviors.

------------------------------------------------------------------------

# Canonical State

Reference implementations and examples SHOULD reflect the AGCP
architectural principle that Canonical State is deterministically resolved
from one or more qualified authoritative governance sources. The ordered
Append-Only Governance Ledger is authoritative for recorded governance
events, event ordering, and Derived Lifecycle State, but need not originate
every governance-relevant fact incorporated into Canonical State.

Reference artifacts SHOULD NOT illustrate architectures that derive
authoritative state from timestamp ordering or other non-authoritative
ordering mechanisms.

------------------------------------------------------------------------

# Relationship to Conformance

Reference artifacts do not participate directly in conformance
evaluation.

Conformance is established through the authoritative traceability chain:

``` text
Published AGCP Runtime Governance Conformance Requirements (CRs)
        +
AGCP Core Specification
        +
Applicable adopted normative Companion Specification obligations
        |
        | mapped in the authoritative RTM using Core-derived
        | Normative Statement (NS) identifiers
        v
Conformance Test Case (TC)
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
