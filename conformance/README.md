# Conformance

## Purpose

This directory contains the AGCP conformance framework used to verify
that an implementation satisfies the normative requirements defined by
the AGCP specifications.

The conformance artifacts provide human-readable documentation,
machine-readable mappings, executable harness checks, and deterministic
test vectors. Together they support repeatable, auditable, and
deterministic verification of AGCP implementations.

------------------------------------------------------------------------

# Conformance Architecture

The authoritative traceability model is:

``` text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
```

The executable conformance layer builds upon that foundation:

``` text
Test Case (TC)
        ↓
Harness Check
        ↓
Harness Test Vector
```

Harness Checks and Harness Test Vectors SHALL NOT introduce independent
normative requirements.

------------------------------------------------------------------------

# Directory Contents

  -----------------------------------------------------------------------
  Artifact                              Purpose
  ------------------------------------- ---------------------------------
  AGCP-Conformance.md                   Defines the AGCP conformance
                                        model, profiles, and verification
                                        requirements.

  AGCP-Test-Matrix.md                   Human-readable summary of
                                        validated capabilities and
                                        representative Harness Test
                                        Vectors.

  AGCP-Conformance-Test-Vectors.md      Deterministic execution scenarios
                                        covering governance behavior and
                                        observable outcomes.

  AGCP-Conformance-Harness-Spec.yml     Defines execution behavior for
                                        the automated conformance
                                        harness.

  AGCP Harness Check Registry.md        Human-readable registry of
                                        executable Harness Checks.

  harness-checks.json *(or              Machine-readable Harness Check
  assertions.json until renamed)*       registry.

  test-mapping.json                     Machine-readable mapping between
                                        NS, CR, TC, and representative
                                        Harness Test Vectors.

  agcp-conformance-manifest.yml         Index of the conformance package
                                        and execution metadata.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Scope

The conformance suite verifies, where applicable:

-   Proposal Qualification
-   Governance Decision Function
-   Human Review
-   Execution Authorization
-   Commit Boundary
-   Governance Evidence
-   Provenance validation
-   Ordered Append-Only Governance Ledger behavior
-   Canonical State reconstruction
-   Deterministic replay
-   Idempotency
-   Tenant lifecycle enforcement
-   Tenant and Governance Domain isolation
-   Published registries

------------------------------------------------------------------------

# Canonical State

Canonical State SHALL be deterministically resolved from qualified authoritative governance sources. The ordered Governance Ledger is authoritative for recorded governance events, authoritative event ordering, and Derived Lifecycle State. Materialized governance state used for replay must be verifiably derived from the applicable authoritative sources and ledger records.

Ledger sequence order is authoritative. Timestamp order is not.

------------------------------------------------------------------------

# Relationship to the Requirements Traceability Matrix

The Requirements Traceability Matrix (RTM) is the authoritative mapping
between:

-   Normative Statements (NS)
-   Conformance Requirements (CR)
-   Test Cases (TC)

The conformance artifacts in this directory provide the executable
realization of those mappings and SHALL remain synchronized with the
RTM.

------------------------------------------------------------------------

# Normative vs. Informational Artifacts

Normative artifacts define required implementation behavior.

Informational artifacts explain, summarize, or execute the normative
model without creating new requirements.

Machine-readable artifacts support automation but do not supersede the
normative specifications.

------------------------------------------------------------------------

# Repository Versioning

This directory follows repository-release versioning.

Individual artifacts generally do not embed specification version
numbers unless required for interoperability.

------------------------------------------------------------------------

# Future Evolution

Future repository releases may expand the conformance suite with
additional Harness Checks, Test Vectors, or execution capabilities while
preserving the authoritative NS → CR → TC traceability model.
