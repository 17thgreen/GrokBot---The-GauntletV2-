# MACHINE_READABLE_LOCAL — oversized TEST JSON policy

## Why pointers exist

Examiner TEST `*.json` artifacts for `TEST-20260910-001`, `TEST-20260910-002`, and `TEST-20260910-003` are larger than the GitHub MCP push ceiling (~11KB). Full blobs therefore remain on **lab storage** and are **not** mirrored verbatim to GitHub.

## What GitHub holds

| Layer | Location | Role |
|-------|----------|------|
| Human-readable reports | `lab/archive/tests/TEST-*.md` and `*-full.md` | Canonical human record of verdicts and narrative |
| Institutional pointers | `lab/archive/tests/TEST-*-EDGE-*.json` with `artifact_kind=MACHINE_READABLE_POINTER` | sha256-bound stub: TEST_ID, edge_id, local_path, size_bytes, sha256, companion_md, slim_metrics |
| Full MACHINE_READABLE JSON | `/workspace/lab/archive/tests/*.json` (lab only) | Authoritative machine record including `full_instrument_summaries` |

## Reconstruct / verify

1. Locate the local file named in the pointer's `local_path` (same basename under `lab/archive/tests/`).
2. Compute `sha256sum` of that file.
3. Confirm it equals the pointer's `sha256` and `size_bytes`.
4. Only then treat the local JSON as the verified MACHINE_READABLE artifact for that TEST_ID.

Do **not** invent performance numbers. Pointer `slim_metrics` were copied from the verified local JSON. Large nested blocks (`full_instrument_summaries`) are omitted from GitHub and referenced solely by the full-file sha256.

## Bound artifacts (V)

| TEST_ID | Filename | size_bytes | sha256 |
|---------|----------|------------|--------|
| TEST-20260910-001 | TEST-20260910-001-EDGE-20260910-001.json | 186598 | 05b360199a30f160680c756e94ed7f306e076161ff0bd584e68c6443e98e6eb5 |
| TEST-20260910-002 | TEST-20260910-002-EDGE-20260910-003.json | 71612 | 08aed389f5917b7340e8924902f63bbbcf986b06c68c7897a2c0294e988764ac |
| TEST-20260910-003 | TEST-20260910-003-EDGE-20260910-004.json | 36001 | 498a4d6eea520ac56614e2804ebb05b0f4f528cdd3ff133276048fa5feccd509 |

## Non-goals

- Do not push `lab/data` or raw market data.
- Do not commit secrets.
- Do not replace MD reports with invented metrics; MD reports remain the canonical human record on GitHub.
