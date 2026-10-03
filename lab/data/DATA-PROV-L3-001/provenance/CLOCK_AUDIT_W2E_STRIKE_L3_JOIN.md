# CLOCK AUDIT — W2E STRIKE L3 JOIN

- **AUDIT_ID:** `CLOCK_AUDIT_W2E_STRIKE_L3_JOIN`
- **FEATURE:** `DRAFT-FEAT-20260913-002`
- **GATE:** `DRAFT-ABST-20260913-002`
- **WAVE:** `W2-E / Wave 003`
- **AUDITED_AT_UTC:** 2026-09-13T19:23:07.917859+00:00
- **VERDICT (join only):** **CONDITIONAL**
- **VERDICT_SCOPE:** join_only

## Scope (hard)

- No alpha / no Examiner Δ or scores
- No CF as oracle; L3 is NOT the settlement oracle
- EXPIRATION_VALUE audit-only — never a feature / never in join keys
- No new fetch; sources listed below

## Sources

- **checkpoints:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **pm001_kalshi:** `/workspace/lab/data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson`
- **l3_btc:** `/workspace/lab/data/DATA-PROV-L3-001/derived/BTCUSDT_1m_spot_2026-09-04_2026-09-11.parquet`
- **l3_eth:** `/workspace/lab/data/DATA-PROV-L3-001/derived/ETHUSDT_1m_spot_2026-09-04_2026-09-11.parquet`
- **feature_card:** `/workspace/lab/archive/features/DRAFT-FEAT-20260913-002-W2E-strike-vs-mid.md`
- **gate_card:** `/workspace/lab/archive/features/DRAFT-ABST-20260913-002-W2E-rules-strike.md`
- **prior_clock_l3:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_REPORT.json`
- **script:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/clock_audit_W2E_STRIKE_L3_JOIN.py`
- **new_fetch:** `False`

## Join rule (fail-closed)

```
knowable_bar = argmax { bar in L3 | bar.close_time_ms <= decision_time_ms }; S_t = knowable_bar.close; require knowable_bar exists AND (decision_time_ms - close_time_ms) <= 90000; K = PM-001.FLOOR_STRIKE joined by contract_id / venue_native_id; require OPEN_TIME <= decision_time and FLOOR_STRIKE present (fail-closed if missing).
```

- Stale / missing S_t: if no knowable bar OR lag > 90000 ms → missing (card: no L3 bar within 90s of t).
- Missing K: FLOOR_STRIKE null OR PM-001 join miss OR OPEN_TIME > decision_time → fail-closed.
- Scored rows: rem=300, implied_p_method==mid, not near-deg (≤0.02/≥0.98), VOID/DISPUTED out (TEST-007-style hygiene).

## Exact counts per headline

### headline_BTC_T5m — `KALSHI|15m|BTC|T-5m|mid`

- **N scored** after TEST-007-style excludes (mid, rem=300, not near-deg, not VOID/DISPUTED): **569**
- **N with K+S_t pairable:** **569**
- **N missing K:** **0**
- **N missing S_t:** **0**
- **N missing either (fail-closed):** **0**
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 35, 'void_disputed_scored_dropped': 0}`
- Missing reasons: `{}`
- S_t lag_ms: min=1 max=1 median=1.0 unique=[1] all_le_90s=True
- Alt window miss (knowable bar not in (t-90s,t]): 0
- Decision_times in L3 window: 569/569 (all_in=True); L3 span open 2026-09-04T00:00:00Z → 2026-09-11T23:59:00Z
- K: present=569, null=0, OPEN<=t=569, knowable_at_t=True
- S_t: knowable_at_t=True, lookahead=False, incomplete_bar_used=0

### headline_ETH_T5m — `KALSHI|15m|ETH|T-5m|mid`

- **N scored** after TEST-007-style excludes (mid, rem=300, not near-deg, not VOID/DISPUTED): **545**
- **N with K+S_t pairable:** **545**
- **N missing K:** **0**
- **N missing S_t:** **0**
- **N missing either (fail-closed):** **0**
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 59, 'void_disputed_scored_dropped': 0}`
- Missing reasons: `{}`
- S_t lag_ms: min=1 max=1 median=1.0 unique=[1] all_le_90s=True
- Alt window miss (knowable bar not in (t-90s,t]): 0
- Decision_times in L3 window: 545/545 (all_in=True); L3 span open 2026-09-04T00:00:00Z → 2026-09-11T23:59:00Z
- K: present=545, null=0, OPEN<=t=545, knowable_at_t=True
- S_t: knowable_at_t=True, lookahead=False, incomplete_bar_used=0

## Certify A–G

### A_K
- **pass:** True
- K = FLOOR_STRIKE from PM-001 joined by contract_id/venue_native_id. Present on all scored contracts; OPEN_TIME<=decision_time on all. [V] static dump snapshot — one FLOOR_STRIKE per CONTRACT_ID; [A] no post-OPEN revision feed in this dump (cannot observe revisions). Fail-closed if null/missing.

### B_S_t
- **pass:** True
- S_t = last L3 completed 1m close with close_time_ms <= decision_time_ms (BTC→BTCUSDT, ETH→ETHUSDT). Preferred fail-closed: bar exists AND lag <= 90000 ms. Both interpretations measured; preferred used for pairable counts. Lag unique=1ms on this slice.

### C_scored_row
- **pass:** True
- Scored: rem=300, implied_p_method==mid, not near-deg (≤0.02/≥0.98), VOID/DISPUTED excluded (TEST-007-style). See per-headline exclude breakdown.

### D_coverage
- **pass:** True
- Per headline: {'KALSHI|15m|BTC|T-5m|mid': {'N_scored': 569, 'N_pairable': 569, 'N_missing_K': 0, 'N_missing_S_t': 0, 'N_missing_either': 0}, 'KALSHI|15m|ETH|T-5m|mid': {'N_scored': 545, 'N_pairable': 545, 'N_missing_K': 0, 'N_missing_S_t': 0, 'N_missing_either': 0}}

### E_knowability
- **pass:** True
- K_knowable=True; S_t_knowable=True; lookahead=False
- K: Yes if frozen at OPEN and OPEN<=t. Certified OPEN<=t on all scored; static dump [V]/ no revision feed [A].
- S_t: Yes: completed bar close_time_ms <= t; lag always 1ms <= 90s.
- Look-ahead: No look-ahead under preferred rule. Using incomplete bar (open_time == floor_minute(t)) would be look-ahead — count=0.

### F_L3_NOT_oracle_no_EXPIRATION_VALUE
- **pass:** True
- L3 rows labeled external_predictor_NOT_oracle_NOT_CF_BRTI; layer=L3. EXPIRATION_VALUE not used in feature join (PM-001 field inventory-only).

### G_decision_times_in_L3_window
- **pass:** True
- All rem=300 decision_times for scored headlines land inside L3 coverage (2026-09-04T00:00:00Z open → 2026-09-11T23:59:59.999Z last close).

## Knowability answers

- **K knowable at t?** **True**
  - Yes if frozen at OPEN and OPEN<=t. Certified OPEN<=t on all scored; static dump [V]/ no revision feed [A].
- **S_t knowable at t?** **True**
  - Yes: completed bar close_time_ms <= t; lag always 1ms <= 90s.
- **Look-ahead?** **False**
  - No look-ahead under preferred rule. Using incomplete bar (open_time == floor_minute(t)) would be look-ahead — count=0.

## Integrity footnotes

- PM-001 meta: `{'n_rows': 1328, 'n_unique_contract_id': 1328, 'n_unique_venue_native_id': 1328, 'n_null_FLOOR_STRIKE': 0, 'status_counts': {'RESOLVED': 1328}, 'resolution_counts': {'YES': 660, 'NO': 668}, 'one_row_per_contract': True, 'revision_feed_present': False, 'revision_policy_tag': '[V] static dump snapshot — one FLOOR_STRIKE per CONTRACT_ID; [A] no post-OPEN revision feed in this dump (cannot observe revisions).', 'EXPIRATION_VALUE_note': 'Field present on PM-001 rows for audit inventory only; FORBIDDEN in feature join / p_t construction.', 'n_null_EXPIRATION_VALUE': 0}`
- L3 labels: all selected bars `external_predictor_NOT_oracle_NOT_CF_BRTI`; layer=L3; no EXPIRATION_VALUE column on L3 parquet.
- Prior Clock L3 join class reused: `knowable_bar = argmax close_time_ms <= decision_time_ms`.

## Verdict recommendation (join only)

**CONDITIONAL** — Join-only: K present on all scored rows with OPEN_TIME<=t; S_t always within 90s (lag=1ms on this PM-003 :00 slice) via close_time_ms<=decision_time_ms. No look-ahead. CONDITIONAL (not CLEARED) because L3 is external_predictor_NOT_oracle and is NOT CF BRTI / settlement oracle — S_t is spot proxy [A], not CF TWAP. No EXPIRATION_VALUE in feature join. Static dump: [V] snapshot / [A] no revision feed for FLOOR_STRIKE.

This is not an Examiner skill verdict and not permission to trade. L3 remains NOT_oracle / NOT CF BRTI.
