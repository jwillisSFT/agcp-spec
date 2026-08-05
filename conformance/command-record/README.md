# Governance Approval Command/Record Separation Vectors

This directory contains implementation-independent vectors for finding P0-06.

- `AGCP-Governance-Approval-Command-Record-Test-Vectors.json` verifies that DS-045 is an untrusted ingress command and DS-026 is an authoritative AGCP-created or AGCP-qualified record.
- Negative vectors add one prohibited server-derived field at a time to the valid DS-045 submission and require schema rejection.
- The vectors do not prescribe private implementation code or deployment topology.
