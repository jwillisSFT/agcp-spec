# AGCP PEP Profile Template

## 1. Profile Control

- Profile ID:
- Version:
- SHA-256:
- Owner:
- Applies to Implementation Profile:

## 2. PEP Interface

- PEP implementation/interface ID:
- Endpoint/RPC/in-process boundary:
- Timeout/retry model:

## 3. GRF Caller Authentication

- Allowed GRF/control-plane caller:
- Authentication/integrity mechanism:
- Credential reference:

## 4. Governed Action / Target Mappings

| Governed action | Target type | PEP operation | Required source fields | Target-ID mapping | Allowed deterministic transforms |
|---|---|---|---|---|---|
| | | | | | |

## 5. Enforcement Context

List required proposal, decision, authorization, commit, Tenant/Domain, target, validity, lifecycle, prior-use, profile, and other binding fields/references.

## 6. Mapping Fidelity

State that no unsupported action may be approximated, substituted, widened, or weakened.

## 7. Idempotency / Single Use / Replay

- Key rule:
- Authorization consumption rule:
- Safe retry rule:
- Validity window:

## 8. Response Mapping

| PEP result | AGCP interpretation | Evidence required |
|---|---|---|
| success | | |
| refusal | | |
| failure | | |
| unknown | fail closed | |

## 9. Commitment and Execution

Declare atomic, asynchronous/distinct, or mixed-by-operation semantics.

## 10. PEP-to-Target Authority

- Target credential reference:
- Authorized target/effect scope:
- Alternate mutation paths:

## 11. Evidence / Receipts

Document request/response digests, target receipts, and resulting-state evidence.

## 12. Profile-Specific Tests

Include unsupported action, wrong target, wrong authorization, wrong profile, stale/replay, wrong GRF caller, duplicate effect, direct bypass, PEP refusal, and target-failure cases.
