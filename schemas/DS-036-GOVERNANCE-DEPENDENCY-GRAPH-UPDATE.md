# DS-036 Governance Dependency Graph Update

## Implementation

Implemented `DS-036 governance_dependency_graph.json` as the canonical, independently identifiable and traceable representation of governance-significant relationships among governed sub-transitions of a composite proposal.

## Extraction from DS-021

The transitional `dependency_graph` definition was removed from `governed_action_proposal.json`. The DS-021 composite proposal now references the canonical DS-036 schema directly.

## Relationship model

DS-036 supports typed prerequisite, ordering, authority, synchronization, consistency, execution, resource, policy, evidence, and state relationships. Each relationship carries explicit source and target sub-transition identities, governance domains, mandatory status, failure effect, change materiality, integrity digest, and relationship-specific semantics.

## Validation and change control

The graph records attributable validation of node and dependency identifier uniqueness, endpoint resolution, self-dependency exclusion, cycle analysis, ordering satisfiability, cross-domain governance, and explicit required dependencies. Material dependency-condition changes require deterministic identification and re-evaluation of affected nonterminal proposals before bind.

## Semantic boundary

DS-036 does not itself establish authority, authorize execution, or determine Partial-Bind Admissibility. Those determinations remain assigned to their respective governance processes and schemas.

## Traceability

DS-036 is mapped to CR-106 and CR-107 in RTM-1.19.
