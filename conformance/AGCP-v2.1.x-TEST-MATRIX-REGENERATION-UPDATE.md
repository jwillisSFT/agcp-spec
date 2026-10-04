# AGCP v2.1.x Test Matrix Regeneration Update

**Status:** Complete for the Test Matrix step  
**Date:** 2026-10-03

## Purpose

This change regenerates `conformance/AGCP-Test-Matrix.md` from the synchronized Formal Test Case source files (`TC-001` through `TC-122`). It replaces the prior partial patch approach with a complete TC-derived matrix.

## Scope

The regenerated matrix:

- enumerates all 122 Formal Test Cases;
- preserves the one-to-one CR-001 through CR-122 / TC-001 through TC-122 model;
- reports conformance level, requirement group, and active direct/conditional/supporting NS relationship counts for every TC;
- identifies the 42 formal assertion/traceability changes and 22 additional regression/scenario changes;
- exposes current NS relationships for all 64 affected TCs;
- records disposition of all 36 new Core-derived NS relationships;
- confirms retired NS identifiers are not active TC metadata targets; and
- explicitly marks test mappings, test-control mappings, vectors, checks, and final RTM regeneration as downstream work.

## Non-goals

This step does **not** regenerate `test-mapping.json`, `test-control-mapping.json`, Harness Test Vectors, Harness Checks, or the RTM. Those are intentionally subsequent controlled steps.

## Next controlled step

Regenerate the test mappings from the synchronized Formal Test Cases and this Test Matrix.
