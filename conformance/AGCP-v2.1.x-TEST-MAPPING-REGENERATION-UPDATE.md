# AGCP v2.1.x Test Mapping Regeneration Update

**Status:** Complete for the test-mapping step  
**Date:** 2026-10-03

## Purpose

This change completely regenerates `conformance/test-mapping.json` and adds the human-readable mirror `conformance/AGCP-Test-Mapping.md` after Formal Test Case synchronization and Test Matrix regeneration. The machine mapping now represents every controlled Formal Test Case from `TC-001` through `TC-122`.

## Regeneration basis

The synchronized Formal Test Case files are the source for current CR/TC identity and direct, conditional, and supporting/contextual NS relationships. The current schema, interface, and registry catalogs are used to validate referenced DS, IF, and REG identifiers. RTM-1.46 is retained only as the pre-final-RTM DS/IF/REG baseline for the twelve TC records that were not represented in the prior machine mapping; this does not update or supersede the RTM.

## Results

- Machine mapping records: **122** (previously **110**).
- Formerly missing records added: `TC-075, TC-076, TC-077, TC-078, TC-089, TC-090, TC-110, TC-111, TC-112, TC-113, TC-114, TC-117`.
- Current Formal TC NS relationships copied exactly into every machine mapping record.
- Retired NS targets `NS-8.6A-01`, `NS-8.6A-03`, and `NS-9.1-01`: **0 active mapping references**.
- DS mappings are regenerated to current active schema paths and include the v2.1.x identity/authorization, realization/enforcement, and governed-execution artifacts where applicable.
- New v2.1.x rejection-code registry entries are mapped where their CR and NS traceability intersect the current TC.
- IAS Profile, PEP Profile, and controlling Implementation Profile references are explicitly represented when invoked by the synchronized TC procedure.
- All **17** current Harness Check identifiers are referenced by at least one TC mapping.
- All **54** current Harness Test Vector identifiers are now referenced by at least one TC mapping or supporting relationship.
- Existing vectors/checks are not declared synchronized to new assertion content by this step; the later vector/check synchronization remains required.

## Deliberate boundary

This step regenerates the **test mappings only**. It does not regenerate `test-control-mapping.json`, change the Harness Test Vector catalog, change Harness Check definitions, or update the RTM.

## Next controlled step

Regenerate the test-control mappings from the synchronized Formal TCs and this current test mapping.
