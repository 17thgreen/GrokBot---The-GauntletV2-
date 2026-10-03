# DATA-PROV-PM-005 — Inventory (Poly Global 15m last-print @ rem=300)

**Class:** DATA inventory. Not a Feature. Not Examiner. Not Clock CLEARED.
**Stamp:** 2026-09-13
**Trade:** FORBIDDEN
**Auth:** none (public CLOB / gamma labels from PM-001). No keys.

## Pairing rule (measured here; Clock owns legal match)

Exact match on `(asset, OPEN_TIME, CLOSE_TIME)` between:
- **Incumbent cell:** DATA-PROV-PM-003 Kalshi 15m checkpoint at `time_remaining_sec=300` with `implied_p_method=mid`
- **Instrument:** Polymarket Global 15m last-print at rem=300 (`obs_time ≤ decision_time`; bid/ask null)

No silent PM-002 ∪ PM-003 union. No invented mid. No pooling.

## Upstream stocks

| Source | What | Count |
|--------|------|------:|
| PM-001 normalized poly | All Global BTC/ETH 5m+15m resolved labels | 2496 |
| PM-001 poly 15m BTC | Labels only (CLOB_TOKEN_IDS present) | 312 |
| PM-001 poly 15m ETH | Labels only | 311 |
| PM-001 poly 15m open span | | 2026-09-08T14:30Z → 2026-09-11T20:15Z |
| PM-002 Poly 15m contracts with prices-history | Stride prototype | 30 BTC + 30 ETH |
| PM-002 Poly 15m rem=300 last-print rows | `implied_p_method=last`, yes_bid/ask null | 30 BTC + 30 ETH |
| PM-002 Poly 15m open span | | 2026-09-08T17:00Z → 2026-09-11T20:15Z |
| PM-003 Kalshi 15m rem=300 mid | Full remaining after PM-002 exclude | 604 BTC + 604 ETH |
| PM-003 Kalshi open span | | 2026-09-04T20:45Z → 2026-09-11T20:15Z |

PM-001 has **no** intra-window last-prints (labels / terminal OUTCOME_PRICES only — forbidden as m_t).

## Pre-fetch pairing N (exact OPEN+CLOSE → PM-003)

| Instrument stock | BTC | ETH | vs target N≥80 |
|------------------|----:|----:|----------------|
| PM-002 Poly 15m rem=300 last ∩ PM-003 exact OC | **26** | **26** | **FAIL-INSUFFICIENT** alone |
| PM-001 Poly 15m labels ∩ PM-003 exact OC (fetch candidates) | **277** | **276** | enough labels if history hits |
| PM-001 Poly 15m with no Kalshi OC twin in PM-003 | 35 | 35 | mostly PM-003 gaps (PM-002-excluded slots) |

Kalshi opens before Poly label start (2026-09-08T14:30Z): **327/asset** — no Poly twin in PM-001 raw; not inventable.

## Decision

Public CLOB `prices-history` probed live (HTTP 200, history points present on a known PM-002 token). Fetch of the **277+276** pairable PM-001 Poly 15m labels into DATA-PROV-PM-005 is warranted to raise rem=300 coverage toward N≥80/headline. Resume-safe; polite pacing; rem={300} headline, {600,840} captured dark if present in the same history response.

## Post-fetch (filled after run)

See `FETCH_SUMMARY.json` and § below after fetch completes.

## Post-fetch results (2026-09-13)

| Metric | BTC | ETH |
|--------|----:|----:|
| Universe attempted (exact OC ∩ PM-003) | 277 | 276 |
| HTTP 200 with ≥1 intra-window print | 276 | 275 |
| **Pairing N @ rem=300 last** (headline) | **276** | **275** |
| rem=600 last (DARK) | 276 | 275 |
| rem=840 last (DARK) | 274 | 274 |
| Meets N≥80 / headline | YES | YES |

- Empty history (HTTP 200, 0 intra points): **2** total — recorded in coverage as not-ok; not invented.
- HTTP fail / auth / 404 blockers: **0**
- `yes_bid` / `yes_ask`: null on all rows (last-print only; mid BLOCKED)
- `obs_time ≤ decision_time`: enforced; 0 lookahead violations on rem=300
- PM-002 prototype **not** unioned into this sheet (independent fetch of pairable PM-001 labels)
- Paths: `raw/poly_prices/` (553 json), `derived/checkpoints.ndjson`, `derived/poly_15m_last_prints.ndjson`, `derived/contract_coverage.ndjson`, `provenance/FETCH_SUMMARY.json`

**Pre-fetch PM-002-only pairing N was 26/26 — insufficient. Post-fetch PM-005 pairing N is 276/275 — sufficient labels+prints for later Clock join vs PM-003 T-5m mid.**

<!-- POST_FETCH_ANCHOR -->

