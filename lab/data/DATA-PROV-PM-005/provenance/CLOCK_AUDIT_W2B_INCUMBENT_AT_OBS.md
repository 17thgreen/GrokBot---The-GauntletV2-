# CLOCK AUDIT — W2B INCUMBENT AT OBS (Kalshi mid @ Poly last L)

- **AUDIT_ID:** `CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS`
- **FEATURE:** `DRAFT-FEAT-20260913-004` (door NEEDS_DATA)
- **GATE:** `DRAFT-ABST-20260913-004`
- **WAVE:** `W2-B / Wave 006 leftover after WAVE_008_CLOSE`
- **AUDITED_AT_UTC:** 2026-09-13T21:59:29.698467+00:00
- **VERDICT (join only):** **CONDITIONAL**
- **VERDICT_SCOPE:** join_only_incumbent_at_obs
- **Feature door:** **NEEDS_DATA** — this verdict alone does **not** READY or Examiner-route
- **Trade:** FORBIDDEN

## Candle rule (named)

- **ID:** `completed_bar_at_L_end_period_ts_le_L`
- **Rule:** m_L is the mid of the latest completed Kalshi 1m candlestick for the OC-twin ticker whose end_period_ts (bar CLOSE) is <= unix(L) and strictly after OPEN and <= CLOSE; mid=(yes_bid.close+yes_ask.close)/2 only when bid>0, ask>0, bid<=ask — no last fallback, no interpolation, no decision_time bar.

## Scope (hard)

- No alpha / no Examiner Δ or scores
- No invented Poly mid from last
- No Kalshi decision_time mid as m_L
- No interpolation
- Wave 005 T-5m pairable set only; rem=300 headline
- No new fetch; raw PM-003 candles on disk

## Sources

- **pm003_checkpoints:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **pm003_candles_dir:** `/workspace/lab/data/DATA-PROV-PM-003/raw/kalshi_candles`
- **pm001_kalshi:** `/workspace/lab/data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson`
- **pm005_checkpoints:** `/workspace/lab/data/DATA-PROV-PM-005/derived/checkpoints.ndjson`
- **pm005_coverage:** `/workspace/lab/data/DATA-PROV-PM-005/derived/contract_coverage.ndjson`
- **pm005_prints:** `/workspace/lab/data/DATA-PROV-PM-005/derived/poly_15m_last_prints.ndjson`
- **fetch_summary:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/FETCH_SUMMARY.json`
- **inventory:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/INVENTORY.md`
- **prior_wave005_audit_json:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.json`
- **prior_wave005_audit_md:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.md`
- **prior_wave005_verdict:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_POLY_T5_JOIN.md`
- **prior_wave005_script:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_POLY_T5_JOIN.py`
- **feature_card:** `/workspace/lab/archive/features/DRAFT-FEAT-20260913-004-W2B-poly-last.md`
- **gate_card:** `/workspace/lab/archive/features/DRAFT-ABST-20260913-004-W2B-xvenue.md`
- **clock_order:** `/workspace/lab/governance/CLOCK_ORDER_W2B_INCUMBENT_AT_OBS_2026-09-13.md`
- **script:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_INCUMBENT_AT_OBS.py`
- **new_fetch:** `False`

## Join rule (fail-closed)

```
On Wave 005 T-5m pairable set (Kalshi rem=300 mid scored × Poly last OC twin): L = Poly last obs_time; last_L = Poly last (method=last; bid/ask null); m_L = Kalshi official 1m mid at L from raw candlesticks (PM-003), same (asset, OPEN, CLOSE) via PM-001. CANDLE_RULE=completed_bar_at_L_end_period_ts_le_L: m_L is the mid of the latest completed Kalshi 1m candlestick for the OC-twin ticker whose end_period_ts (bar CLOSE) is <= unix(L) and strictly after OPEN and <= CLOSE; mid=(yes_bid.close+yes_ask.close)/2 only when bid>0, ask>0, bid<=ask — no last fallback, no interpolation, no decision_time bar. FORBIDDEN: use decision_time Kalshi mid as m_L; invent Poly mid from last; interpolate; Examiner Δ; Feature READY.
```

- **Deterministic pick:** Wave 005 pairable pick unchanged: among PM-005 rem=300 last rows with obs_time<=decision_time sharing (asset, open_time, close_time), max obs_time, ties by contract_id ascending. Then m_L from completed-bar-at-L on that row's L.

## Coverage (exact)

| Headline | N_scored | N_OC_twin | N_wave005_pairable | N_with_m_L | miss_pairing | miss_L | miss_m_L |
|----------|----------:|----------:|-------------------:|-----------:|-------------:|-------:|---------:|
| `KALSHI|15m|BTC|T-5m|mid@L` | 569 | 254 | 254 | 254 | 315 | 0 | 0 |
| `KALSHI|15m|ETH|T-5m|mid@L` | 545 | 240 | 240 | 240 | 305 | 0 | 0 |

### m_L miss breakdown

- **BTC:** candle_file_miss=0; no_completed_bar=0; mid_rule_fail=0; last_as_mid=0; decision_time_bar=0; m_L==decision_mid (numeric, informational)=10
- **ETH:** candle_file_miss=0; no_completed_bar=0; mid_rule_fail=0; last_as_mid=0; decision_time_bar=0; m_L==decision_mid (numeric, informational)=6

## Lag (L vs decision_time) on Wave 005 pairable

| Headline | n | min | median | mean | p90 | max |
|----------|--:|----:|-------:|-----:|----:|----:|
| `KALSHI|15m|BTC|T-5m|mid@L` | 254 | 23.0 | 45.0 | 44.20 | 47.0 | 103.0 |
| `KALSHI|15m|ETH|T-5m|mid@L` | 240 | 23.0 | 45.0 | 44.18 | 47.0 | 103.0 |

## Lag on rows with m_L present

| Headline | n | min | median | mean | p90 | max |
|----------|--:|----:|-------:|-----:|----:|----:|
| `KALSHI|15m|BTC|T-5m|mid@L` | 254 | 23.0 | 45.0 | 44.20 | 47.0 | 103.0 |
| `KALSHI|15m|ETH|T-5m|mid@L` | 240 | 23.0 | 45.0 | 44.18 | 47.0 | 103.0 |

## Certifications

- **A_m_L:** pass=True — m_L from completed_bar_at_L_end_period_ts_le_L on official yes bid/ask closes; no last-as-mid; no decision_time bar. BTC with_m_L=254/254 miss_m_L=0, ETH with_m_L=240/240 miss_m_L=0
- **B_L:** pass=True — Poly last_L is method=last only; yes_bid/yes_ask null; not invented mid; obs_time<=decision_time.
- **C_pairing:** pass=True — Exact (asset, OPEN_TIME, CLOSE_TIME) OC twin Kalshi↔Poly; no PM-002 union; candle ticker = PM-001 VENUE_NATIVE_ID.
- **D_scored_row:** pass=True — Wave 005 T-5m pairable universe: KALSHI 15m rem=300 mid scored with TEST-007 hygiene, then Poly last OC twin.
- **E_coverage:** pass=True — Inventory rem300 last BTC/ETH match; candle files 1208/1208; BTC wave005=254 with_m_L=254; ETH wave005=240 with_m_L=240
- **F_knowability:** pass=True — Completed-bar at L (end_period_ts<=L) — no future bar; Poly obs_time<=decision_time; lag documented. last_as_mid=0.
- **G_forbidden:** pass=True — No invented Poly mid; no decision_time mid as m_L; no interpolation; no Examiner/READY from this alone; trade forbidden.

## Verdict rationale

Incumbent-at-obs join works under caveats: Poly last lagged vs decision_time (obs_lag_sec documented; 45s-stale last ≠ same-t); candle rule completed_bar_at_L_end_period_ts_le_L: completed bar at L; m_L ≠ decision_time mid by construction; last ≠ mid (Poly bid/ask null; last-as-mid=0); fail-closed on miss candle / mid-rule; Feature door stays NEEDS_DATA — join verdict alone does not READY/Examiner.

**Does NOT** make Feature READY. **Does NOT** alone authorize Examiner. Door stays **NEEDS_DATA**.

## Artifacts

- script: `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_INCUMBENT_AT_OBS.py`
- json: `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS.json`
- md: `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_INCUMBENT_AT_OBS.md`
- verdict: `/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_INCUMBENT_AT_OBS.md`
- archive pointer: `/workspace/lab/archive/audit/2026-09-13-Clock-DATA-VERDICT-W2B-INCUMBENT-AT-OBS.md`
