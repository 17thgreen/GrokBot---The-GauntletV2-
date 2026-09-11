# DATA-PROV-PM-002

- **DATA_ID:** DATA-PROV-PM-002
- **NAME:** Bounded decision-time checkpoint \(m_t\) for PM-001 short-window BTC/ETH binaries
- **STATUS:** **CONDITIONAL**
- **Registered:** 2026-09-11 UTC (Track B next bottleneck after PM-001 CONDITIONAL)
- **Parent:** DATA-PROV-PM-001 (labels only; books/mids were ABSENT)
- **Path:** `/workspace/lab/data/DATA-PROV-PM-002/`
- **Report:** `/workspace/lab/data/DATA-PROV-PM-002/REPORT.md`
- **Role:** L1 **historical price state** at declared remaining-time checkpoints. Not books. Not independent oracle. Not a trade feed.
- **Auth:** Public APIs only — **no API keys** `[V]`
- **Schema:** checkpoint rows: contract_id, venue, decision_time, time_remaining_sec, yes_bid, yes_ask, last, implied_p, source_endpoint. Null = `[U]`.

## Inventory `[V]`

| Slice | n contracts | ≥1 intra-window | Checkpoint rows |
|-------|------------:|----------------:|----------------:|
| Kalshi 15m BTC+ETH | 120 | 120 | 600 |
| Polymarket Global 5m+15m BTC+ETH | 120 | 120 | 540 |
| Combined | 240 | 240 | 1140 |

Prototype first: 20+20 (Kalshi 18/20 then 429-recovered; Poly 20/20). Extend stride-sampled; **not** all 3824.

## Construction
- Kalshi: live `GET /series/{series}/markets/{ticker}/candlesticks` period_interval=1; mid if bid>0 and ask>0 else last.
- Poly: CLOB `/prices-history` last `p`; bid/ask `[U]`.
- Forbidden sources: PM-001 terminal `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES`; post-CLOSE prints; interpolation.

## Access gates
| Path | Access |
|------|--------|
| raw/ | immutable snapshot of public candle/history payloads |
| derived/ | provisional checkpoints; PENDING_CLOCK |
| Examiner market-relative | **PARTIAL** — CLEARED cells only (see Clock verdict); freeze before run |
| Trading | **Forbidden** |

## Known limitations
- T−15m/T−5m exact OPEN not available from closed 1m candles (use T−14m/T−4m)
- T−0 Kalshi near-degenerate (120/120 implied_p near 0/1)
- Poly bid/ask absent; last only
- Not historical L2 books
- Independent oracle still UNTESTED
- Kalshi 429 soft limiter on bulk
- Provisional PROV-* IDs

## Clock DATA VERDICT
- **Verdict:** CONDITIONAL (APPROVED_WITH_LIMITATIONS) — issued 2026-09-11T21:27:41Z
- **CLEARED primary:** Kalshi mid @ T−14m / T−10m / T−5m (exclude near-deg & last-fallback)
- **CLEARED weaker:** Poly last @ non-T−0 (lag caveat; not mid)
- **BLOCKED:** T−0 Kalshi; Poly mid; books; oracle; full 3824; sealed; unlabeled pool; pre-cutoff historical; PM-001 terminals as m_t
- **Full:** `/workspace/lab/data/DATA-PROV-PM-002/provenance/DATA_VERDICT_DATA-PROV-PM-002.md`
