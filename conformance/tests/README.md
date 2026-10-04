# AGCP Conformance Test Suite

The Test Cases are organized in files containing ten Test Cases each, except the final file, which contains TC-121 and TC-122. The current files are synchronized to the v2.1.x Core and Normative Statements. The formal RTM remains the next controlled synchronization step; until that step is completed, `../v2.1.x-formal-test-sync.json` records the delta that must be carried into the RTM.

## Files

- [TC001-TC010.md](TC001-TC010.md) — TC-001 through TC-010
- [TC011-TC020.md](TC011-TC020.md) — TC-011 through TC-020
- [TC021-TC030.md](TC021-TC030.md) — TC-021 through TC-030
- [TC031-TC040.md](TC031-TC040.md) — TC-031 through TC-040
- [TC041-TC050.md](TC041-TC050.md) — TC-041 through TC-050
- [TC051-TC060.md](TC051-TC060.md) — TC-051 through TC-060
- [TC061-TC070.md](TC061-TC070.md) — TC-061 through TC-070
- [TC071-TC080.md](TC071-TC080.md) — TC-071 through TC-080
- [TC081-TC090.md](TC081-TC090.md) — TC-081 through TC-090
- [TC091-TC100.md](TC091-TC100.md) — TC-091 through TC-100
- [TC101-TC110.md](TC101-TC110.md) — TC-101 through TC-110
- [TC111-TC120.md](TC111-TC120.md) — TC-111 through TC-120
- [TC121-TC122.md](TC121-TC122.md) — TC-121 through TC-122

## Traceability Rules

- `Direct Test-Generating NS IDs` reflect the current v2.1.x Core/Normative Statement synchronization set. After the RTM update, the RTM SHALL match these controlled mappings for the corresponding CR.
- Conditional NS entries must be tested when applicable or receive an evidence-supported Not Applicable disposition.
- Supporting/contextual NS entries are integrated constraints or references and are not claimed as independent direct verifications.
- Each direct NS must map to a unique assertion block with procedure, expected result, evidence, and pass/failure criteria.

## Governance observation and controlled test preconditions

AGCP v2.1.x permits a harness to use IF-003 Governance Observation Points and the optional IF-005 Conformance Test Control interface to observe behavior and establish deterministic preconditions. Test controls SHALL NOT inject the expected outcome. Preserve setup request/result artifacts separately from target runtime evidence. See `../test-control-mapping.json`.


## v2.1.x synchronization status

- Formal Test Case identifiers remain `TC-001` through `TC-122`; no `TC-123` is introduced.
- 42 Test Cases carry formal traceability/assertion changes.
- 22 additional Test Cases carry regression/scenario changes.
- Retired NS identifiers `NS-8.6A-01`, `NS-8.6A-03`, and `NS-9.1-01` are not current test targets.
- New Core-derived NS obligations are incorporated into the existing CR-linked TCs as direct, conditional, or supporting coverage rather than creating new CRs.
- Final RTM synchronization is complete at `RTM-1.47`; the Formal Test Cases remain the authoritative assessment procedures under the synchronized RTM.
