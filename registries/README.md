# AGCP Registries

Status: Normative  
Version: 0.9.0  

This directory contains registry artifacts used by AGCP implementations.

Registries define enumerated identifiers used throughout the specification.

---

# Registry Types

The registries currently defined include:

| Registry | Purpose |
|---|---|
| rejection-code-registry.json | Standard rejection codes |
| constraint-type-registry.json | Supported constraint evaluation types |
| invariant-type-registry.json | Supported invariant types |

---

# Purpose

Registries ensure consistent behavior across AGCP implementations by defining stable identifiers used by:

- policy evaluation
- decision reporting
- error handling
- conformance validation

---

# Versioning

Registry changes are governed by the versioning rules defined in:


governance/AGCP-Versioning.md


Additions to registries MAY be backward compatible.

Removal or semantic changes require a **major specification version increment**.
