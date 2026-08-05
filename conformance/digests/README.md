# AGCP Content Digest Conformance Vectors

This directory contains implementation-independent vectors for the DS-001
`content_digest` contract corrected under finding P1-12.

The controlled vector package is
`AGCP-Content-Digest-Test-Vectors.json`. It verifies exact algorithm/output
length binding, lowercase hexadecimal encoding, rejection of ambiguous
BLAKE2B identifiers, rejection of non-hexadecimal values, required fields,
and closed-object behavior.

The vectors supplement the formal Test Cases mapped to CR-042, CR-052,
CR-064, and CR-066. They do not independently establish conformance.
