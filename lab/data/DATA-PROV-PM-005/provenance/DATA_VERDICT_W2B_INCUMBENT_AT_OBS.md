# DATA VERDICT — W2-B legal incumbent: Kalshi mid at Poly last obs_time

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T21:59:29.698467+00:00
**Authority:** `CLOCK_ORDER_W2B_INCUMBENT_AT_OBS_2026-09-13.md` · `DRAFT-FEAT-20260913-004` · `DRAFT-ABST-20260913-004`
**Trade:** FORBIDDEN
**Feature door:** **NEEDS_DATA** — this verdict alone does **not** READY and does **not** alone authorize Examiner

---

## DATA VERDICT: CONDITIONAL

**VERDICT_SCOPE:** join_only_incumbent_at_obs
**QUALITY_STATUS:** INCUMBENT_AT_OBS_JOIN_CERTIFIED_WITH_CAVEATS
**THIS JOIN:** Kalshi official 1m mid at Poly last obs_time L (PM-003 candles) × Poly 15m last-print (PM-005) on Wave 005 T-5m pairable OC twins
**NOT:** Poly mid · invented bid/ask · decision_time Kalshi mid as m_L · interpolation · alpha · Examiner Δ · Feature READY

## Candle rule

**`completed_bar_at_L_end_period_ts_le_L`:** m_L is the mid of the latest completed Kalshi 1m candlestick for the OC-twin ticker whose end_period_ts (bar CLOSE) is <= unix(L) and strictly after OPEN and <= CLOSE; mid=(yes_bid.close+yes_ask.close)/2 only when bid>0, ask>0, bid<=ask — no last fallback, no interpolation, no decision_time bar.

## Rationale

Incumbent-at-obs join works under caveats: Poly last lagged vs decision_time (obs_lag_sec documented; 45s-stale last ≠ same-t); candle rule completed_bar_at_L_end_period_ts_le_L: completed bar at L; m_L ≠ decision_time mid by construction; last ≠ mid (Poly bid/ask null; last-as-mid=0); fail-closed on miss candle / mid-rule; Feature door stays NEEDS_DATA — join verdict alone does not READY/Examiner.

## Coverage (exact)

| Headline | N_scored | N_wave005_pairable | N_with_m_L | miss_m_L | miss_pairing | miss_L |
|----------|----------:|-------------------:|-----------:|---------:|-------------:|-------:|
| `KALSHI|15m|BTC|T-5m|mid@L` | 569 | 254 | 254 | 0 | 315 | 0 |
| `KALSHI|15m|ETH|T-5m|mid@L` | 545 | 240 | 240 | 0 | 305 | 0 |

## Lag (L vs decision_time) — Wave 005 pairable

- **BTC:** n=254, min=23.0s, median=45.0s, mean=44.20s, p90=47.0s, max=103.0s
- **ETH:** n=240, min=23.0s, median=45.0s, mean=44.18s, p90=47.0s, max=103.0s

## Integrity flags

- **last-as-mid:** 0 (must be 0)
- **decision_time bar used as m_L:** 0 (must be 0)
- **lookahead baked into pairable:** False
- **lookahead discarded count:** 0

## Certifications (summary)

- **A_m_L:** pass=True
- **B_L:** pass=True
- **C_pairing:** pass=True
- **D_scored_row:** pass=True
- **E_coverage:** pass=True
- **F_knowability:** pass=True
- **G_forbidden:** pass=True

## SAFE / UNSAFE

### SAFE (under this verdict)

- Using m_L from completed Kalshi 1m bar at Poly L (end_period_ts<=L)
- Keeping Poly last as last (bid/ask null); not inventing mid
- Fail-closed when candle missing or mid-rule fails
- Documenting lag(L vs decision_time); not treating stale last as same-t

### UNSAFE

- Using Kalshi mid at decision_time as m_L
- Inventing Poly mid from last
- Interpolating between candle bars
- Citing this as Feature READY or Examiner clearance
- Look-ahead (obs_time > decision_time or future candle bar)

## FAILURES / blockers

1. None that force QUARANTINED/REJECTED — caveats documented under CONDITIONAL.

## Examiner / Door

**NOT authorized by this alone.** Feature `DRAFT-FEAT-20260913-004` door remains **NEEDS_DATA**. Not alpha. Trade FORBIDDEN.

## Artifacts

- **script:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_INCUMBENT_AT_OBS.py`
- **json:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS.json`
- **md:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS.md`
- **verdict:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md`
- **archive:** `/workspace/lab/archive/audit/2026-09-13-Clock-DATA-VERDICT-W2B-INCUMBENT-AT-OBS.md`

---

**DATA VERDICT: CONDITIONAL** (join only) — sealed by The Clock 2026-09-13T21:59:29.698467+00:00. Feature stays NEEDS_DATA. Not Examiner-READY from this alone. Not alpha. Trade FORBIDDEN.
