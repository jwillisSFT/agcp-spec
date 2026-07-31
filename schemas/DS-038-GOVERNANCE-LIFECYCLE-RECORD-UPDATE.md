# DS-038 Governance Lifecycle Record Update

DS-038 establishes the canonical Governance Lifecycle Record for AGCP v2.0. The record is bound to stable Proposal Identity and derives authoritative lifecycle state from ordered Governance Ledger records. It preserves complete lifecycle-transition history and transition basis, distinguishes terminal and nonterminal state, records approval, refusal, receipt, expiration, cancellation, degradation, re-evaluation, recovery, commitment, and execution effects, and supports deterministic reconstruction and external retrieval.

## Clean migration

DS-038 now owns lifecycle record identity, Derived Lifecycle State, terminality, lifecycle-state references, lifecycle-transition references, and Governance Lifecycle Record references. The superseded shared definitions were removed from `common.json`, and all dependent schemas were migrated to DS-038 references.

## Semantic protections

- Internal processing state cannot become canonical externally visible lifecycle state.
- Only permitted transitions supported by required governance decision and evidence may change lifecycle state.
- Terminal source states cannot transition back to nonterminal state.
- Executed Proposal Identity instances are terminal and non-repeatable.
- DEGRADED is nonterminal, blocks commitment, and requires governed re-evaluation or recovery.
- Approval or quorum alone does not establish authority at commitment or authorize execution.
- Ledger ordering, not timestamp or storage ordering, is authoritative.
