# AGCP Specification Library

## Overview

This directory contains the normative and supporting specifications that define the Artificial Intelligence Governance Control Plane (AGCP).

AGCP is a deterministic runtime governance architecture that governs execution at the Commit Boundary. The specification ecosystem separates normative requirements, architectural guidance, implementation specifications, and conformance artifacts into complementary documents.

---

# Specification Hierarchy

The AGCP specification ecosystem is organized as follows:

```
AGCP Core Specification
        │
        ├── Architecture Reference Model (ARM)
        ├── Normative Statements
        ├── Companion Specifications
        │
        ├── Runtime Governance Requirements
        ├── Requirements Traceability Matrix (RTM)
        └── Conformance Test Suite
```

The Core Specification is the constitutional specification for AGCP. All other specification artifacts derive from or support the Core.

---

# Documents

## AGCP Core Specification

Defines the normative execution semantics and constitutional requirements for runtime governance.

The Core Specification defines:

* architectural scope
* governance processing model
* execution authorization
* Commit Boundary semantics
* governance evidence
* lifecycle semantics
* governance invariants
* conformance requirements

The Core Specification is the authoritative source of normative requirements.

---

## Architecture Reference Model (ARM)

The Architecture Reference Model provides informative architectural guidance and rationale supporting the Core Specification.

The ARM explains:

* architectural concepts
* design rationale
* reference architecture
* implementation considerations
* processing relationships
* governance services
* illustrative examples

The ARM introduces no additional normative requirements.

---

## Normative Statements

The Normative Statements document extracts and enumerates every normative requirement defined by the Core Specification.

Each statement:

* has a unique identifier
* traces to the Core Specification
* supports conformance verification
* supports requirements traceability

---

## Companion Specifications

Companion Specifications define implementation-specific aspects of the AGCP ecosystem.

Examples include:

* Protocol specifications
* Schema specifications
* HTTP/API specifications
* Operational profiles
* Security profiles
* Storage contracts
* Registry specifications

Companion Specifications extend the Core without modifying its constitutional behavior.

---

# Related Repository Artifacts

Additional repository components include:

| Artifact                               | Purpose                                 |
| -------------------------------------- | --------------------------------------- |
| Runtime Governance Requirements        | Requirements catalog                    |
| Requirements Traceability Matrix (RTM) | End-to-end requirements traceability    |
| Conformance Test Suite                 | Verification of normative behavior      |
| JSON Schemas                           | Machine-readable data definitions       |
| API Specifications                     | HTTP/OpenAPI interfaces                 |
| Registries                             | Controlled vocabularies and identifiers |
| Assessment Frameworks                  | Governance evaluation and assurance     |

---

# Normative and Informative Content

The specification ecosystem distinguishes between normative and informative artifacts.

## Normative

Normative artifacts define required behavior.

These include:

* AGCP Core Specification
* Normative Statements
* Applicable Companion Specifications

## Informative

Informative artifacts provide explanation, rationale, examples, and implementation guidance.

These include:

* Architecture Reference Model
* Repository architecture documentation
* Reference material

Informative documents introduce no additional normative requirements.

---

# Repository Versioning

The AGCP repository is versioned through GitHub Releases.

Released versions are archived through Zenodo.

Individual specification documents are maintained without embedded document version numbers. The GitHub Release identifies the authoritative published version of the complete specification ecosystem.

---

# Additional Information

For an overview of the repository architecture, see:

* `../ARCHITECTURE.md`

For repository usage and project information, see:

* `../README.md`

