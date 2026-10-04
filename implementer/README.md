# AGCP Implementation Profiles

AGCP uses controlled profiles to bind generic normative semantics to concrete implementations without placing deployment-specific technology into Core.

## Profile layers

1. **AGCP Implementation Profile** - controlling implementation/deployment decisions, function placement, trust boundaries, interfaces, Canonical State, lifecycle, evidence, and conformance scope.
2. **Identity and Authorization Store (IAS) Profile** - authoritative identity plus identity-system authorization/entitlement resolution used as governance input.
3. **PEP Profile** - exact GRF-to-PEP enforcement mapping for governed actions/targets.

The controlling Implementation Profile references IAS and PEP Profiles by controlled identity/version/digest.

IAS authorization/entitlement information is not AGCP Execution Authorization. The GRF, not the GDF/PDP, applies the PEP Profile for commitment/enforcement realization.

Operational customer, product, course, or other deployment-specific profiles may be distributed separately from this generic repository.
