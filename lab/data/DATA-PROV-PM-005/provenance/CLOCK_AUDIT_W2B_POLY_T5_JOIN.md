# CLOCK AUDIT — W2B POLY T-5m JOIN

- **AUDIT_ID:** `CLOCK_AUDIT_W2B_POLY_T5_JOIN`
- **FEATURE:** `DRAFT-FEAT-20260913-004`
- **GATE:** `DRAFT-ABST-20260913-004`
- **WAVE:** `W2-B / Wave 005`
- **AUDITED_AT_UTC:** 2026-09-13T19:55:18.964387+00:00
- **VERDICT (join only):** **CONDITIONAL**
- **VERDICT_SCOPE:** join_only
- **Feature door:** **NEEDS_DATA** — this verdict alone does **not** READY or Examiner-route
- **Trade:** FORBIDDEN

## Scope (hard)

- No alpha / no Examiner Δ or scores
- No invented Poly mid / prints / quotes
- No PM-002∪PM-003 silent union; no venue pool
- Headlines rem=300 only; rem=600/840 dark
- No new fetch; sources listed below

## Sources

- **pm003_checkpoints:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **pm001_kalshi:** `/workspace/lab/data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson`
- **pm005_checkpoints:** `/workspace/lab/data/DATA-PROV-PM-005/derived/checkpoints.ndjson`
- **pm005_coverage:** `/workspace/lab/data/DATA-PROV-PM-005/derived/contract_coverage.ndjson`
- **pm005_prints:** `/workspace/lab/data/DATA-PROV-PM-005/derived/poly_15m_last_prints.ndjson`
- **fetch_summary:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/FETCH_SUMMARY.json`
- **inventory:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/INVENTORY.md`
- **feature_card:** `/workspace/lab/archive/features/DRAFT-FEAT-20260913-004-W2B-poly-last.md`
- **gate_card:** `/workspace/lab/archive/features/DRAFT-ABST-20260913-004-W2B-xvenue.md`
- **clock_order:** `/workspace/lab/governance/CLOCK_ORDER_W2B_POLY_T5_JOIN_2026-09-13.md`
- **script:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_POLY_T5_JOIN.py`
- **new_fetch:** `False`

## Join rule (fail-closed)

```
m_t = PM-003 Kalshi same-row mid; implied_p_method==mid; rem=300; mid timestamp = decision_time (same-t). L_t = PM-005 Poly 15m last-print; pairing = exact (asset, OPEN_TIME, CLOSE_TIME) vs Kalshi contract via PM-001; obs_time <= decision_time; yes_bid/yes_ask null; implied_p_method==last (NOT mid). Missing m_t or L_t → fail-closed. FORBIDDEN: PM-002∪PM-003 silent union; treat last as mid; pool venues; invent prints/quotes; rem=600/840 as headlines (dark).
```

- **Deterministic pick:** If multiple PM-005 rem=300 last rows share the same (asset, open_time, close_time), select among those with obs_time<=decision_time the row with maximum obs_time, ties broken by contract_id ascending. Expected: one row per rem per OC key.

## Coverage (exact)

| Headline | N_scored | N_OC_twin | N_pairable | miss_pairing | miss_L | miss_m |
|----------|----------:|----------:|-----------:|-------------:|-------:|-------:|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 254 | 254 | 315 | 0 | 0 |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 240 | 240 | 305 | 0 | 0 |

Scored excludes (TEST-007):
- **BTC:** candidates=604; non_mid=0; near_deg=35; VOID/DISPUTED=0; null_m=0
- **ETH:** candidates=604; non_mid=0; near_deg=59; VOID/DISPUTED=0; null_m=0

## Lag stats (obs_lag_sec = decision_time − obs_time) on pairable

| Headline | n | min | median | mean | p90 | max |
|----------|--:|----:|-------:|-----:|----:|----:|
| `KALSHI|15m|BTC|T-5m|mid` | 254 | 23.0 | 45.0 | 44.20 | 47.0 | 103.0 |
| `KALSHI|15m|ETH|T-5m|mid` | 240 | 23.0 | 45.0 | 44.18 | 47.0 | 103.0 |

## Inventory cross-check

- pairing_N_rem300_last: measured BTC=276 (claim 276, match=True); ETH=275 (claim 275, match=True)
- empty histories: measured=2 (claim 2, match=True) by_asset={'BTC': 1, 'ETH': 1}
- no PM-002 union: True
- bid/ask nonnull rem300: 0

## Certifications A–G

- **A_m:** pass=True — Kalshi same-t mid on scored rows: implied_p_method==mid, implied_p present, rem=300, decision_time as mid timestamp. miss_m totals: BTC=0, ETH=0
- **B_L:** pass=True — Poly L_t is last-print only: implied_p_method==last on all PM-005 rows; yes_bid/yes_ask null on all rem=300; not treated as mid. obs_time<=decision_time enforced (look-ahead discarded).
- **C_pairing:** pass=True — Exact (asset, OPEN_TIME, CLOSE_TIME) after UTC normalize; no PM-002∪PM-003 silent union; one rem=300 last per OC key; inventory rem300 last BTC=276 ETH=275.
- **D_scored_row:** pass=True — TEST-007 hygiene: venue KALSHI, window 15m, rem=300, implied_p_method==mid, drop near-deg ≤0.02/≥0.98, drop VOID/DISPUTED, require same-t mid present. See per-headline exclude breakdown.
- **E_coverage:** pass=True — Inventory cross-check: rem300 last BTC 276 (claim 276); ETH 275 (claim 275); empty histories 2 (claim 2). Among scored Kalshi T-5m mid: BTC N_scored=569 OC_twin=254 pairable=254 miss_pairing=315; ETH N_scored=545 OC_twin=240 pairable=240 miss_pairing=305
- **F_knowability:** pass=True — L_t requires obs_time <= decision_time; look-ahead discarded before pick. lookahead_discarded_total=0. Lag on pairable rows documented in obs_lag_sec_stats (last is weaker).
- **G_forbidden:** pass=True — No invented mid; no bid/ask fabrication; no venue pool; no PM-002 silent union; rem=600/840 present as dark only — not used as headlines in this audit.

## Verdict rationale

Join works under documented caveats: partial coverage vs full Kalshi T-5m scored universe (many Kalshi opens predate Poly 15m label span / lack OC twin); Poly last is lagged (obs_time < decision_time; documented obs_lag_sec); last ≠ mid (bid/ask null; mid BLOCKED — do not invent); fail-closed on miss_L / miss_m / miss_pairing; Feature door stays NEEDS_DATA — this join verdict alone does not READY or Examiner-route.

**Does NOT** make Feature READY. **Does NOT** alone authorize Examiner. Door stays **NEEDS_DATA**.

## Artifacts

- script: `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_POLY_T5_JOIN.py`
- json: `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.json`
- md: `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.md`
- verdict: `/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_POLY_T5_JOIN.md`
