# Generic Enterprise IAS Profile Example

This informational example shows one protected identity/authorization source resolving stable human identity, account status, Tenant membership, roles, entitlements, governance permissions, reviewer classes, and delegation attributes.

The example deliberately separates **entitlement possession** from **AGCP governance approval**. For example, a subject may possess an entitlement permitting participation in a review class; the GDF/PDP still evaluates the proposal, policy, Canonical State, other approvals, and constraints. The entitlement does not itself authorize execution.

Commitment-sensitive facts such as account status, reviewer eligibility, or a revocable entitlement are revalidated by the GRF when required by the controlling governance and Implementation Profile.

See `IAS-GENERIC-ENTERPRISE-EXAMPLE.yaml` for the machine-readable example.
