# AGCP Normative Companion Reference Dispositions

**Status:** Controlled repository reference disposition  
**Version:** 1.0.0  
**Release target:** AGCP v2.0.4  
**Finding:** P1-01

## 1. Purpose

This document resolves references that named normative companion artifacts not present in the controlled AGCP repository. It does not create new normative obligations. It identifies the existing controlled artifacts that govern the referenced subject matter and establishes canonical naming rules for future repository references.

The machine-readable companion is `governance/normative-companion-reference-dispositions.json`.

## 2. Controlling rule

A normative reference shall identify:

1. an existing controlled repository artifact by canonical title and path; or
2. an explicitly identified external normative source.

A subject-area label shall not be written as though it were a standalone specification when no such controlled artifact exists. Distributed obligations shall reference the applicable CRs, Core provisions, companion specifications, schemas, registries, and conformance artifacts that actually control the behavior.

## 3. Reference dispositions

### 3.1 Standalone security-companion label

The former standalone security-companion label is retired as an absent repository reference. AGCP v2.0.4 does not publish one umbrella security specification.

Security-relevant normative obligations remain distributed across:

- `spec/AGCP_Runtime_Governance_Requirements_CR-001_thru_CR-122.csv`;
- `spec/AGCP-Core.docx`;
- `spec/AGCP-Provenance-Wire-Format-Specification.md`;
- `spec/AGCP-Multitenant-Operational-Specification.md`;
- `spec/AGCP-Error-Mapping.md`;
- `spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`;
- applicable active schemas, including `schemas/common.json`; and
- applicable controlled registries, including `registries/rejection-code-registry.json`.

A repository document shall reference the applicable artifacts from this set rather than the retired umbrella label.

### 3.2 Standalone governance-evidence-companion label

The former standalone governance-evidence-companion label is retired as an absent repository reference. AGCP v2.0.4 does not publish a separate governance-evidence specification.

The evidence contract is controlled by:

- the published CRs and `spec/AGCP-Core.docx`;
- DS-020 Governance Evidence, `schemas/governance_evidence.json`;
- DS-033 Evidence Qualification Result, `schemas/evidence_qualification_result.json`;
- `spec/AGCP-Provenance-Wire-Format-Specification.md`; and
- `spec/ledger/AGCP-Append-Only-Governance-Ledger-Specification.md`.

Repository references shall identify those exact artifacts rather than the retired umbrella label.

### 3.3 Human-adjudication companion title

The controlled artifact is:

- **Canonical title:** AGCP Human Adjudication and Governance Approval Specification
- **Canonical path:** `spec/AGCP-Human-Review-Specification.md`

The reversed noncanonical title is retired. This is a naming correction only; the underlying controlled artifact is unchanged in authority.

## 4. Repository-wide disposition

The v2.0.4 correction pass searched specifications, lifecycle documents, governance documents, conformance documents, schemas, OpenAPI, registries, examples, catalogs, the RTM workbook, and Office-document text. Active stale references were found only in the Markdown files corrected under finding P1-01.

Historical comparison records may preserve earlier wording when the text is explicitly presented as historical `before` or `after` data. Such records are not active normative references.

## 5. Change-control rule

A future standalone companion may be introduced only through the controlled repository change process. Until such an artifact is published, cataloged, traceably mapped, and included in a versioned release, repository documents shall not reference it as an existing normative source.
