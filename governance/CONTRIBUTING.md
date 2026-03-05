# Contributing to AGCP

AGCP is released for **public technical review**.  
Contributions are welcome in the form of **review comments, defect reports, and architectural feedback**.

This repository is **maintainer-controlled** to preserve specification integrity.

External contributors **do not submit pull requests**.  
Instead, feedback is submitted through **GitHub Issues**.

---

# Contribution Model

The AGCP specification follows an **issue-driven review process**.

Public reviewers may:

- Report specification defects
- Identify ambiguities
- Propose clarifications
- Identify structural gaps
- Raise determinism concerns
- Raise security concerns
- Raise multitenant isolation concerns

Maintainers evaluate submissions and incorporate accepted changes into future specification versions.

---

# How to Submit Feedback

1. Open a **GitHub Issue**
2. Select the appropriate issue category
3. Provide structured feedback using the format below

Required information:

- Specification document
- Section number
- Assertion ID (if applicable)
- Description of the issue
- Proposed resolution language

Example:

```
Document: AGCP-Core
Section: 7.3
Assertion: A-PEC-001

Issue:
Invariant evaluation ordering is ambiguous when multiple invariant types are present.

Proposed Resolution:
Clarify evaluation ordering requirements and specify deterministic ordering guarantees.
```

---

# Issue Categories

Please classify submissions using one of the following categories:

- Normative Defect
- Structural Gap
- Ambiguity
- Conformance Clarification
- Security Concern
- Determinism Concern
- Multitenant Isolation Concern

Correct categorization helps reviewers prioritize issues.

---

# Review Expectations

Contributions should be:

- Technically precise
- Evidence-based
- Constructive
- Focused on specification improvement

Submissions that do not include sufficient technical detail may not be actionable.

---

# Change Evaluation

Maintainers evaluate submissions according to:

- Determinism guarantees
- Security guarantees
- Multitenant isolation guarantees
- Conformance impact
- Compatibility impact
- Architectural consistency

Accepted changes will be incorporated through the **AGCP versioning process**.

See:

`/governance/AGCP-Versioning.md`

---

# Compatibility Discipline

Proposed changes must consider compatibility impact:

| Change Type | Version Impact |
|-------------|---------------|
Breaking change | MAJOR |
Additive extension | MINOR |
Editorial clarification | PATCH |

Maintainers determine the final classification.

---

# Public Review Scope

Public review may address:

- Core specification
- HTTP interface
- Policy Evaluation Contract
- Security profile
- Multitenant operational profile
- Conformance framework
- Schema definitions
- Registries

---

# Non-Goals for Contributions

The following are outside the scope of this repository:

- Product feature requests
- Vendor-specific implementation guidance
- Non-deterministic architecture proposals
- Changes that weaken security or isolation guarantees

---

# Code of Conduct

Professional and respectful discourse is expected.

Constructive technical debate is encouraged.

Personal attacks, harassment, or disruptive behavior will not be tolerated.

---

# Maintainer Responsibilities

Maintainers are responsible for:

- Evaluating submitted issues
- Determining architectural impact
- Maintaining specification integrity
- Applying versioning rules
- Publishing updated releases

---

# Acknowledgment

Significant technical contributions may be acknowledged in future specification releases.
