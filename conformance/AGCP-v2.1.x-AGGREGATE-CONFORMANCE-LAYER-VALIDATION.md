# AGCP v2.1.x Aggregate Conformance-Layer Validation

**Validation ID:** `AGCP-v2.1.x-AGGREGATE-CONFORMANCE-LAYER-VALIDATION-2026-10-03`  
**Status:** **PASS**  
**Date:** 2026-10-03  
**RTM status:** `PENDING_FINAL_RTM_SYNCHRONIZATION`  
**Next controlled step:** **Final RTM synchronization**

## 1. Purpose

This record documents the aggregate pre-RTM validation of the synchronized AGCP v2.1.x conformance layer. It verifies that the Formal Test Cases, regenerated Test Matrix, test mappings, test-control mappings, Harness Checks, Harness Test Vectors, controlled fixtures, and standardized test-control/observation vocabularies are internally consistent before the Requirements Traceability Matrix is regenerated.

This validation does **not** establish implementation conformance and does **not** replace the RTM. It validates the repository conformance artifacts that will feed the final RTM synchronization.

## 2. Aggregate result

All **33 aggregate checks passed** with no errors or warnings.

| Item | Result |
|---|---:|
| Formal Test Cases | 122 |
| Test-mapping records | 122 |
| Test-control mapping records | 122 |
| Harness Checks | 21 |
| Harness Test Vectors | 71 |
| Controlled conformance fixtures | 36 |
| New NS dispositions | 36 |
| Formal assertion/traceability changes | 42 TCs |
| Regression/scenario changes | 22 TCs |
| Standardized test-control bindings | 108 |
| Governance Observation Point references | 477 |
| Additional implementation/profile-dependent injection needs | 7 |
| Active references to retired NS test targets | 0 |

## 3. Cross-layer checks performed

The aggregate validator confirmed that:

- `TC-001` through `TC-122` are present exactly once and preserve the one-to-one `CR-001` through `CR-122` model;
- direct and conditional NS metadata match the actual assertion blocks in the Formal Test Cases;
- all 36 newly introduced Core-derived NS relationships are assigned to the intended existing TCs;
- retired `NS-8.6A-01`, `NS-8.6A-03`, and `NS-9.1-01` are not active test targets;
- the Test Matrix matches the Formal TC titles, CRs, and direct/conditional/supporting NS counts;
- `test-mapping.json` matches the Formal TC NS relationships and all mapped DS, IF, REG, schema, fixture, and profile references resolve;
- `test-control-mapping.json` covers all 122 TCs, all standardized controls resolve against DS-050, and all observation points resolve against DS-046;
- all 108 standardized control bindings agree with their recommended-control entries and all 477 observation references use current vocabulary;
- all 21 Harness Checks and all 71 Harness Test Vectors are unique, resolvable, and referenced by the synchronized TC mapping;
- the YAML vector catalog and Markdown vector catalog contain the same 71 vector identifiers;
- all 17 v2.1.x IAS/GRF/PEP/DS-052 vectors are present;
- the seven implementation/profile-dependent injection needs identified for `TC-081`, `TC-120`, and `TC-121` have corresponding harness representations without being misrepresented as universally standardized IF-005 capabilities;
- all 36 controlled fixtures validate against their active schemas; and
- DS-018 and the Commit Boundary harness vectors do not accept or inject GRF-derived current-authority, qualified-evidence, PEP Profile, or DS-029 Enforcement Context content.

## 4. Corrections made during aggregate validation

The aggregate pass identified and corrected two residual conformance-layer inconsistencies before the final PASS was recorded.

### 4.1 Harness Check count metadata

`conformance/harness-checks.json` contained 21 synchronized check records but retained a stale top-level `check_count` value of 17. The declared count was corrected to **21**. No Harness Check definition or normative requirement changed.

### 4.2 Semantic fixture assumptions for DS-018

The semantic-fixture catalog still contained v2.0-era assumptions that DS-018 carried current Authority Re-Derivation, qualified evidence, resulting-state validation, and nested DS-029 Enforcement Context content. Under the current architecture those are established by the GRF after DS-018 is received.

The semantic-fixture rules were therefore synchronized as follows:

- DS-018 semantic equality checks now cover only the bindings the caller legitimately supplies: tenant, governance domain, and target consistency between the Proposal reference and request-level target/context identifiers;
- proposal/current-authority mismatch testing moved to DS-029, where GRF-derived authority is actually represented;
- Enforcement Context reference mismatch testing moved to DS-019, where the PEP/commit result binds the GRF-created DS-029;
- evidence mismatch testing moved to DS-026, using independently repeated evidence bindings;
- Canonical State mismatch testing moved to DS-039, where multiple current-state references are semantically required to agree; and
- the DS-018 fixture description now explicitly states that current authority, current qualified evidence, PEP Profile selection, and DS-029 construction belong to the GRF.

After those corrections, the existing semantic-fixture validator passed with all controlled positive fixtures schema-valid and all semantic negative vectors proving semantic inconsistency beyond schema validation.

## 5. Development-stage test and injection points

The aggregate PASS does not mean every internal test/injection hook is already implemented by every runtime. The current repository continues to distinguish standardized IF-005 controls from implementation-specific or future-standardization negative-test hooks. In particular, asynchronous execution timing/outcome controls and selected PEP/GRF binding-tamper paths remain profile- or implementation-dependent. Their harness semantics are represented, but runtime support must be discovered and proven for the assessed implementation.

## 6. Validation boundary

This pre-RTM aggregate validation intentionally excludes final RTM regeneration and repository-release manifest/hash closure. Those are downstream controlled activities. Historical per-step validation records remain point-in-time records and are not rewritten merely because a later aggregate step completed.

## 7. Next controlled step

**Final RTM synchronization is now the next step.** The RTM should be regenerated from the now aggregate-validated chain:

```text
CR
 ↓
Core / adopted Companion obligations
 ↓
NS
 ↓
DS / IF / Profile / Registry
 ↓
Formal TC
 ↓
Test mapping / Test-control mapping
 ↓
Harness Check / Harness Test Vector
 ↓
Evidence
```

Only after the RTM is synchronized should repository-wide release/manifest/hash validation and final release-note/repository closure be performed.
