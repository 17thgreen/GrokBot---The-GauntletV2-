# DATA-PROV-PM-003

- **DATA_ID:** DATA-PROV-PM-003
- **NAME:** Remaining Kalshi 15m BTC/ETH decision-time checkpoints (PM-001 minus PM-002 coverage)
- **STATUS:** **CONDITIONAL**
- **Registered:** 2026-09-11 UTC (Track B remediate TEST-20260911-006 FAIL-INSUFFICIENT)
- **Parent:** DATA-PROV-PM-001
- **Sibling (used, not holdout):** DATA-PROV-PM-002 SLICE-PM002-BOUNDED-240
- **Path:** `/workspace/lab/data/DATA-PROV-PM-003/`
- **Report:** `/workspace/lab/data/DATA-PROV-PM-003/REPORT.md`
- **Role:** L1 historical price state at declared remaining-time checkpoints. Kalshi-only this label. Not books. Not Poly. Not independent oracle.
- **Auth:** Public APIs only — **no API keys**
- **Schema:** checkpoint rows: contract_id, venue, decision_time, time_remaining_sec, yes_bid, yes_ask, last, implied_p, source_endpoint, implied_p_method. Null = `[U]`.

## Inventory (counts only)

| Slice | n contracts | ≥1 intra-window | Checkpoint rows |
|-------|------------:|----------------:|----------------:|
| Kalshi 15m BTC | 604 | 604 | 3020 |
| Kalshi 15m ETH | 604 | 604 | 3020 |
| Combined remaining | 1208 | 1208 | 6040 |

Poly deferred. Construction identical to PM-002 Kalshi (batch candlesticks).

## Access gates

| Path | Access |
|------|--------|
| raw/ | immutable public candle payloads |
| derived/ | provisional checkpoints; **CONDITIONAL** (Clock) |
| Examiner | **PARTIAL** — CLEARED mid cells on this 1208 only after Conductor freeze |
| Trading | **Forbidden** |

## Clock DATA VERDICT

- **Verdict:** CONDITIONAL — issued 2026-09-11T23:03:13Z
- **overlap_vs_PM002:** 0
- **CLEARED primary:** Kalshi mid T−14m / T−10m / T−5m (exclude near-deg & last-fallback) on THIS 1208
- **BLOCKED:** T−0; union-with-PM-002-as-holdout; Poly; books; oracle; sealed
- **Full:** `/workspace/lab/data/DATA-PROV-PM-003/provenance/DATA_VERDICT_DATA-PROV-PM-003.md`

## Clock join note — W2-C sibling mid (2026-09-13T19:12:41Z)

- **Join verdict:** CLEARED (join only) for DRAFT-FEAT-20260913-001
- **Coverage:** ETH T-14m ↔ BTC mid and BTC T-10m ↔ ETH mid — 604/604 pairable, 0 missing
- **Knowable at t:** Yes · **Look-ahead:** No
- **Full:** `/workspace/lab/data/DATA-PROV-PM-003/provenance/DATA_VERDICT_W2C_SIBLING_JOIN.md`
