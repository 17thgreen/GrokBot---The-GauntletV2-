# Inspect — seconds-to-close (already-published TEST-007 only)

**Stamp:** 2026-09-13  
**Source:** TEST-20260911-007 primary cells + Clock PM-003 audit.  
**Peek-ban:** `INSPECT_MEMO_SLATE_PEEK_BAN_2026-09-13.md` (filed first).  
**Not a TEST. Not READY. Not W2-D.**

## Memo ask vs what we already scored

| Memo bucket | Our cell | Status |
|-------------|---------|--------|
| 900–600s | T-14m rem=840; T-10m rem=600 | **Already scored** (mid baseline) |
| 600–180s | T-5m rem=300 | **Already scored** |
| 180–60s | (none) | **No cell.** Do not invent rem=180 from this note. |
| 60–0s | T-1m rem=60 (caveat); T-0 near-deg | T-1m mid measured with strong caveat; T-0 blocked as mid |

## Incumbent mid Brier (TEST-007, invented_numbers=False)

| Cell | N | Brier_mid | LogLoss_mid |
|------|--:|----------:|------------:|
| BTC T-14m | 604 | 0.234728 | 0.662648 |
| ETH T-14m | 604 | 0.232936 | 0.658864 |
| BTC T-10m | 604 | 0.198177 | 0.581969 |
| ETH T-10m | 604 | 0.198214 | 0.579565 |
| BTC T-5m | 569 | 0.141266 | 0.434744 |
| ETH T-5m | 545 | 0.134160 | 0.415843 |
| BTC T-1m | 219 | 0.149206 | 0.464352 |
| ETH T-1m | 178 | 0.126928 | 0.400601 |

T-1m N collapse is Clock: 697/1094 near-deg + 114 last-fallback excluded. `CLEARED_WITH_STRONG_CAVEAT`. F2 already died on the close-minute remainder.

## What this inspect does **not** prove

- It does not prove a Feature beats the mid in any bucket. These are **mid** scores.
- It does not license opening W2-D at rem=180 or rem=60 after seeing the table.
- W2-C/E/A remain INACTIVE; do not rescore them on another rem from this file.

## Read

The book is already a better classifier as time dies, through T-5m. That is the memo’s “the book is doing its job.” The only uneaten memo bucket is **180–60s**, and eating it requires a W2-D declaration *before* a notebook — leftover, not tonight’s peek.
