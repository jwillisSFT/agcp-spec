# DS-041 Governance Configuration Update

## Status

Implemented as `schemas/governance_configuration.json` under DS-041.

## Purpose

DS-041 is the canonical explicit, attributable, versioned, integrity-protected, and governance-evaluation-available configuration artifact. It includes deterministic risk-based re-evaluation controls required to identify affected nonterminal proposals when material governance conditions change.

## Clean migration changes

The canonical Governance Configuration identifier and reference moved from `common.json` to DS-041. No backward-compatibility alias remains. Direct consumers now reference DS-041.

## Direct RTM mappings

- RTM-00117 / CR-117 — Governance Self-Modification Isolation
- RTM-00122 / CR-122 — Risk-Based Re-Evaluation

## Key controls

- complete explicit setting manifest;
- hidden and implicit configuration prohibited;
- externally retrievable and evaluation-available artifact;
- deterministic material-change rules and proposal selectors;
- preservation of unaffected proposals;
- external approval, compilation, constitutional validation, omission analysis, and controlled activation for changes;
- integrity, provenance, evidence, attribution, and replay material;
- active configuration bound to Governance Version and atomic activation evidence;
- no authority-at-commitment, execution authorization, or self-activation semantics.
