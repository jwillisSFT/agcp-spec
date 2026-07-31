# DS-009 Governance Exception Artifact Update

The v2.0 update replaces the legacy broad `ALLOW_CONSTRAINT_OVERRIDE` model with a canonical integrity-bound artifact restricted to ordinary exceptionable constraints. The artifact requires attributable source lineage, bounded scope and validity, current Authority Lineage, external Governance Approval, Governance Evidence, protected-governance review, non-weakening assertions, DS-042 compilation and validation, DS-043 Controlled Governance Activation, Governance Version, integrity protection, and replay material.

## Related changes

- DS-015 can record applied DS-009 references in the Governance Decision basis.
- DS-020 can aggregate DS-009 references and classify exception artifacts as typed evidence.
- OpenAPI exposes `ExceptionArtifact` and `ExceptionArtifactRef`.
- RTM mappings were added for CR-110 through CR-114 and CR-117.
