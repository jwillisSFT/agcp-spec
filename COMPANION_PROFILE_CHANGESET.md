# AGCP v2.1.x Companion and Implementation-Profile Change Set

This working change set aligns the companion/lifecycle/profile layer with the updated AGCP Trust Model, Architecture Reference Model, and Core.

Key changes:

- GDF explicitly maps to the PDP functional role; GDF decision is not commit-bound authority.
- GRF owns current commit eligibility, PEP Profile application, and Enforcement Context construction.
- PEP controls crossing of the enforcement boundary.
- Human identity resolution now includes authoritative identity-system authorization/entitlements through an IAS Profile.
- IAS authorization/entitlements are distinguished from AGCP Execution Authorization.
- Human review, HTTP, multitenancy, management, test control, error mapping, provenance, ledger, and lifecycle documents are synchronized.
- Implementation Profile format is revised to 2.0.0 and genericized.
- New IAS Profile and PEP Profile specification/schema/template/example families are added.
- Commitment is distinguished from later asynchronous execution completion.

This change set does not modify CR-001 through CR-122 or the Normative Statements, DS schemas/OpenAPI, Formal Test Cases, or RTM. Those remain subsequent controlled steps.
