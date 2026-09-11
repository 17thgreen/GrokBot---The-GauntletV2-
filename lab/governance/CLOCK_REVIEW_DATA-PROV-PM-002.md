# CLOCK REVIEW ORDER — DATA-PROV-PM-002

**From:** Conductor  
**To:** Clock (hard authority)  
**Date (UTC):** 2026-09-11  
**DATA_ID:** DATA-PROV-PM-002  
**Parent:** DATA-PROV-PM-001 (your CONDITIONAL; labels only; books/mids ABSENT)

Issue an independent **DATA VERDICT**: APPROVED / CONDITIONAL / QUARANTINED / REJECTED.

Do **not** search for alpha. Do **not** invent Examiner scores.

## What this dataset claims

Bounded reconstruction of decision-time market implied probability \(m_t\) at remaining-time checkpoints for 240 parent contracts, using public APIs only.

| Venue | n | ≥1 intra-window | Checkpoint rows |
|-------|--:|----------------:|----------------:|
| Kalshi 15m BTC+ETH | 120 | 120 | 600 |
| Polymarket Global 5m+15m BTC+ETH | 120 | 120 | 540 |

Paths: `/workspace/lab/data/DATA-PROV-PM-002/` · `REPORT.md` · `archive/datasets/DATA-PROV-PM-002.md`

## Required Clock questions

Establish, with evidence tags:

1. SOURCE / VENUE / INSTRUMENT / MARKET TYPE / START / END / SAMPLING
2. TIMESTAMP SEMANTICS of Kalshi 1m candlestick close vs declared `decision_time`
3. TIMESTAMP SEMANTICS of Polymarket CLOB `prices-history` print `t` vs `decision_time` (report states mean lag ~43s, max 52s)
4. KNOWABILITY at decision time — would a trader have had that bid/ask/last?
5. Whether Kalshi mid = (yes_bid.close + yes_ask.close)/2 is a valid \(m_t\) construction, and when fallback-to-last contaminates
6. Whether Poly last-only (bid/ask all null) can support market-relative scoring, or only a weaker last-print benchmark
7. T−0 Kalshi degeneracy (120/120 near 0/1) — exclude from forecast cells?
8. Exact OPEN (T−15m / T−5m) missing because no closed 1m candle — acceptable to use T−14m / T−4m?
9. Confirm **no** use of PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as \(m_t\)
10. Confirm this is **not** a book archive and **not** an independent oracle
11. Pre-cutoff Kalshi `/historical` route UNTESTED — does that quarantine older coverage?
12. Usable coverage freeze for this 240-slice (do not silently reuse PM-001 label windows)

## Examiner gate you own

PM-001 market-relative Examiner remains BLOCKED until you say otherwise.

If CONDITIONAL: state exactly which checkpoints / venues / implied_p methods are CLEARED vs still blocked.

If you clear any market-relative path: specify the frozen cells (horizon, asset, decision offset) before Examiner runs.

## Forbidden

- Treating 240 as the full 3824
- Treating this slice as sealed holdout
- Waiving independent-oracle UNTESTED by substitution of Binance prices
- Inventing missing bid/ask
