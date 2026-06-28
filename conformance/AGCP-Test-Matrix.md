# AGCP Conformance Test Matrix

**Status:** Informational

This document provides a human-readable traceability matrix linking the
normative AGCP conformance model to the executable conformance harness.

The authoritative machine-readable mapping is maintained in:

``` text
/conformance/test-mapping.json
```

This document is intended for reviewers, implementers, auditors, and
certification activities. The JSON mapping remains the normative
machine-readable source for automated tooling.

------------------------------------------------------------------------

# Conformance Traceability Model

AGCP conformance verification follows the repository's authoritative
traceability model:

``` text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
        ↓
Harness Test Vector (implementation layer)
```

The first four levels constitute the authoritative normative
traceability chain.

Harness Test Vectors provide an executable realization of the published
Test Cases and SHALL NOT introduce additional normative requirements.

All Normative Statements SHALL be covered by one or more Conformance
Requirements.

All Conformance Requirements SHALL be verified by one or more Test
Cases.

Every Test Case SHOULD be exercised by one or more Harness Test Vectors.

------------------------------------------------------------------------

# Test Matrix

  -----------------------------------------------------------------------
  Validated Capability        Representative Harness Test Vectors
  --------------------------- -------------------------------------------
  Proposal Qualification      TV-PROP-001, TV-PROP-002

  Governance Decision --      TV-GOV-001
  Authorized                  

  Governance Decision --      TV-GOV-002
  Denied                      

  Governance Decision --      TV-GOV-003
  Human Review Required       

  Human Review -- Partial     TV-HR-001
  Quorum                      

  Human Review -- Quorum      TV-HR-002
  Satisfied                   

  Human Review -- Invalid /   TV-HR-003
  Expired Review Rejected     

  Execution Authorization --  TV-AUTH-001
  Success                     

  Execution Authorization --  TV-AUTH-002
  Authorization Failure       

  Commit Boundary --          TV-CB-001
  Successful Commit           

  Commit Boundary -- Commit   TV-CB-002
  Without Authorization       
  Rejected                    

  Commit Boundary -- Commit   TV-CB-003
  With Changed Governance     
  Conditions Rejected         

  Tenant Isolation            TV-XTEN-001, TV-XTEN-002

  Governance Domain Isolation TV-XDOM-001

  Canonical State             TV-LEDGER-001
  Reconstruction              

  Reordered Ledger Detection  TV-LEDGER-002

  Ledger Immutability         TV-LEDGER-003

  Governance Pipeline         TV-META-001
  Ordering                    

  Idempotent Proposal         TV-META-002
  Submission                  

  Deterministic Replay        TV-META-003
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Coverage Expectations

The authoritative Requirements Traceability Matrix (RTM) SHALL ensure:

-   Every Normative Statement (NS) maps to one or more Conformance
    Requirements (CR).
-   Every Conformance Requirement maps to one or more Test Cases (TC).
-   Every mandatory Test Case is represented by one or more Harness Test
    Vectors.
-   No mandatory normative behavior is left without executable
    verification.

Representative Harness Test Vectors listed in this document are
illustrative. The complete mapping is maintained in the machine-readable
mapping file.

------------------------------------------------------------------------

# Canonical State Verification

The conformance harness SHALL verify that:

-   Canonical State is derived from the ordered Append-Only Governance
    Ledger, or from a verifiable materialized state whose derivation
    from the ordered ledger can be deterministically reproduced.
-   Ledger sequence order, rather than timestamp order, determines
    authoritative state transitions.
-   Reordered ledger histories are rejected or produce a Canonical State
    that is not accepted as equivalent to the authoritative Canonical
    State.
-   Governance Evidence remains consistent throughout Canonical State
    reconstruction.

------------------------------------------------------------------------

# Governance Evidence Verification

The conformance harness SHALL verify that Governance Evidence:

-   conforms to the published schema;
-   is linked to the corresponding governance event;
-   maintains integrity throughout governance processing;
-   remains attributable to the originating tenant and Governance
    Domain; and
-   supports deterministic replay and audit.

------------------------------------------------------------------------

# Tenant and Governance Domain Isolation

The conformance harness SHALL verify:

-   tenant isolation;
-   Governance Domain isolation, where implemented;
-   prevention of unauthorized cross-tenant access;
-   prevention of unauthorized cross-domain access;
-   tenant-scoped Governance Evidence;
-   tenant-scoped Append-Only Governance Ledger history; and
-   tenant-scoped Canonical State derivation.

------------------------------------------------------------------------

# Relationship to Other Conformance Artifacts

  -----------------------------------------------------------------------
  Artifact                              Purpose
  ------------------------------------- ---------------------------------
  Requirements Traceability Matrix      Authoritative NS → CR → TC
  (RTM)                                 mapping

  AGCP Conformance Specification        Defines conformance model and
                                        profiles

  AGCP Conformance Harness              Defines executable conformance
  Specification                         behavior

  AGCP Conformance Test Vectors         Defines representative executable
                                        test vectors

  test-mapping.json                     Machine-readable traceability
                                        mapping
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Notes

This document is intentionally human-readable.

The authoritative machine-readable mapping remains:

``` text
/conformance/test-mapping.json
```

Where discrepancies exist, the following precedence SHALL apply:

``` text
Normative Specification
        ↓
Normative Statement (NS)
        ↓
Conformance Requirement (CR)
        ↓
Test Case (TC)
        ↓
test-mapping.json
        ↓
Harness Test Vectors
```

Harness artifacts SHALL remain synchronized with the Requirements
Traceability Matrix and SHALL NOT introduce independent normative
behavior.
