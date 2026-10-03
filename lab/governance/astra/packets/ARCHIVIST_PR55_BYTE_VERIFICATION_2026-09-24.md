# Archivist byte verification: Tier A results PR #55 (recorded 2026-09-24T20:24:55-04:00)

## Verdict: **PASS** [V]

| field | value |
|---|---|
| PR | https://github.com/17thgreen/GPT-6-Astra-Deathmatch/pull/55 |
| head | `0cbe603c4d832c0ab06e1202986332aeb6d36a08` |
| base (merge-base / Steward cite) | `eb4a4a9477011d7d75573bb55c04ea6f81fe0a89` |
| `main` at verification | `95a8645d…` (PR53 docs hygiene squash-merged; Conductor cite) |
| changed vs base | **146** paths, **0** deletions |
| landing-list OK | **146 / 146** (batches 1–2 = 139, batch 3 = 4, batch 3B = 1, batch 4 = 1, Card 01 hash anchor = 1) |
| mismatch / missing / extra | 0 / 0 / 0 |
| path guard | CLEAN — no `source_probe_electindex`, no `evidence_private` |
| Card 01 hash anchor | `lab/governance/astra/packets/card01_hybrid_forecast/CARD01_HASH_ANCHOR_MANIFEST_2026-09-24.json` sha256 `e1d019b5385981730eb2dd1c9b718d40a0a675af2fa0545f202c58005f1b11cd` (2202 B) [V] |

Method: `git fetch` PR head; diff name-status against merge-base `eb4a4a94…`; sha256 each blob at `pr-55:<path>` against Archivist Tier A landing lists + anchor. Batch 3B/4 comment lines parsed as `sha256 + path` before tab.

## Disposition
- Byte OK granted. PR stays **draft** until Conductor merges (Steward affirmed).
- Follow-on LEDGER hash-register extract (Steward; claimed sha `03f9c193…`) is **not yet on box** — will verify when that draft PR opens. Does not block PR #55.
