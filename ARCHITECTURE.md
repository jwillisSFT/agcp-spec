# AGCP Architecture Overview

## Purpose

This document provides a high-level overview of the Artificial Intelligence Governance Control Plane (AGCP) architecture and explains how the specification artifacts within this repository relate to one another.

Normative requirements are defined exclusively by the **AGCP Core Specification**. This document is informative and introduces no additional normative requirements.

---

# Architecture Overview

AGCP is a deterministic runtime governance architecture that evaluates and authorizes governance-significant actions immediately prior to execution.

Rather than governing model behavior or training, AGCP governs **action execution** at the runtime execution boundary (the **Commit Boundary**), ensuring that every governed action satisfies deterministic governance requirements before execution is permitted.

The architecture is implementation independent and may be applied to autonomous agents, orchestration platforms, enterprise applications, APIs, robotic systems, cyber-physical systems, and other autonomous or programmatic execution environments.

---

# Runtime Governance Pipeline

At a high level, governed execution proceeds through the following stages:

```
Proposal
    │
    ▼
Proposal Qualification
    │
    ▼
Governance Decision Function
    │
    ▼
Execution Authorization
    │
    ▼
Commit Boundary
    │
    ▼
Governed Execution
    │
    ▼
Governance Evidence
```

Each stage is described normatively in the AGCP Core Specification.

---

# Architectural Principles

The AGCP architecture is founded on several core principles:

* deterministic governance decisions
* implementation independence
* explicit governance authority
* separation of reasoning from execution governance
* non-bypassable execution authorization
* immutable governance evidence
* tenant and domain isolation
* governance configuration integrity
* auditable governance lifecycle

These principles are further explained in the Architecture Reference Model (ARM).

---

# Specification Ecosystem

The AGCP specification is organized into complementary artifacts.

| Artifact                               | Purpose                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------- |
| AGCP Core Specification                | Normative execution governance requirements                                                       |
| Architecture Reference Model (ARM)     | Informative architectural explanations and rationale                                              |
| Normative Statements                   | Individually traceable normative requirements derived from the Core                               |
| Runtime Governance Requirements        | Requirements catalog                                                                              |
| Requirements Traceability Matrix (RTM) | Traceability across requirements, specifications, normative statements, and conformance artifacts |
| Conformance Test Suite                 | Verification of normative behavior                                                                |
| Companion Specifications               | Protocols, schemas, APIs, operational profiles, and related implementation specifications         |

---

# Repository Organization

The repository is organized into the following major areas:

```
spec/
    Core Specification
    Architecture Reference Model
    Normative Statements
    Companion Specifications

requirements/
    Runtime Governance Requirements

rtm/
    Requirements Traceability Matrix

schemas/
    JSON Schemas

api/
    HTTP and API Specifications

registries/
    Registry Definitions

conformance/
    Conformance Specifications
    Test Artifacts

assessment/
    Assessment Frameworks

reference/
    Reference Material
```

---

# Governance Artifacts

The repository contains three categories of artifacts.

## Normative

Normative artifacts define required behavior.

Examples include:

* AGCP Core Specification
* Normative Statements
* Companion Specifications

## Informative

Informative artifacts provide architectural explanation, rationale, implementation guidance, and examples.

Examples include:

* Architecture Reference Model
* Architecture Overview
* Reference documentation

## Machine-readable

Machine-readable artifacts support implementation and conformance.

Examples include:

* JSON Schemas
* OpenAPI definitions
* Registry definitions
* Conformance mappings
* Test manifests

---

# Conformance

Conformance is determined by satisfying the normative requirements defined in the Core Specification.

Traceability between requirements, normative statements, implementation artifacts, and conformance tests is maintained through the Requirements Traceability Matrix (RTM).

---

# Versioning

Repository releases are managed through GitHub Releases.

Released versions are archived through Zenodo.

The repository may contain work in progress between official releases.

---

# Additional Information

The following documents provide further information:

* AGCP Core Specification
* AGCP Architecture Reference Model
* AGCP Normative Statements
* Runtime Governance Requirements
* Requirements Traceability Matrix
* Conformance Test Suite
