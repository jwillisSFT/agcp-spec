# AGCP v2.1.x Formal Test Case Synchronization Update

**Status:** Formal Test Cases synchronized to current v2.1.x Core and Normative Statements; final RTM synchronization pending.

## Scope

This change set preserves the frozen CR-001 through CR-122 requirement set and the one-CR-to-one-TC model. It updates existing Formal Test Cases rather than introducing TC-123 or any other new top-level Test Case.

- Formal traceability/assertion changes: **42 TCs**
- Additional regression/scenario changes: **22 TCs**
- Total affected: **64 of 122 TCs**
- New top-level TC identifiers: **0**
- Retired NS test targets removed: `NS-9.1-01`, `NS-8.6A-01`, `NS-8.6A-03`

## New NS coverage dispositions

| NS ID | Existing TC | Relationship |
|---|---|---|
| `NS-12.2-03` | `TC-096` | conditional |
| `NS-12.6-06` | `TC-096` | direct |
| `NS-13.6-08` | `TC-121` | direct |
| `NS-13.6B-07` | `TC-065` | direct |
| `NS-13.6B-08` | `TC-065` | conditional |
| `NS-13.6B-09` | `TC-065` | conditional |
| `NS-13.6B-10` | `TC-096` | conditional |
| `NS-16.6-07` | `TC-118` | direct |
| `NS-17.5-04` | `TC-089` | conditional |
| `NS-3.3-03` | `TC-089` | support |
| `NS-4.12-01` | `TC-045` | direct |
| `NS-4.12A-01` | `TC-089` | conditional |
| `NS-4.12A-02` | `TC-045` | direct |
| `NS-4.13B-01` | `TC-120` | direct |
| `NS-4.13E-01` | `TC-120` | conditional |
| `NS-4.13E-02` | `TC-120` | conditional |
| `NS-4.7-02` | `TC-081` | support |
| `NS-5.6-01` | `TC-102` | conditional |
| `NS-6.4-04` | `TC-045` | direct |
| `NS-6.4-05` | `TC-045` | direct |
| `NS-6.6A-03` | `TC-045` | direct |
| `NS-7.1-03` | `TC-031` | direct |
| `NS-7.6-05` | `TC-122` | conditional |
| `NS-8.4-03` | `TC-096` | direct |
| `NS-8.6A-04` | `TC-096` | direct |
| `NS-8.6A-05` | `TC-096` | direct |
| `NS-8.6A-06` | `TC-096` | conditional |
| `NS-9.1-03` | `TC-102` | direct |
| `NS-9.4-05` | `TC-120` | conditional |
| `NS-9.4-06` | `TC-120` | direct |
| `NS-9.4-07` | `TC-087` | direct |
| `NS-9.4-08` | `TC-120` | direct |
| `NS-9.4-09` | `TC-120` | direct |
| `NS-9.5-05` | `TC-081` | conditional |
| `NS-9.6A-05` | `TC-121` | conditional |
| `NS-9.6A-06` | `TC-121` | conditional |

## RTM relationship

The current Formal Test Case files are intentionally synchronized before the RTM. `v2.1.x-formal-test-sync.json` is the controlled delta record for the next RTM update. Once the RTM is regenerated, the RTM again becomes the authoritative consolidated mapping among CR, Core, NS, TC, DS/interface/profile, and test evidence.

## Harness and injection maturity

Formal TC procedures may identify required conditions or observations before every corresponding harness fixture/injection hook has been implemented. This is consistent with the repository development-status notice: IF-005 controls establish test conditions only and never inject the required governance outcome. Executable vector/harness coverage must be synchronized and qualified separately.
