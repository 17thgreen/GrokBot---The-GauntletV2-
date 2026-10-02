# CLOCK AUDIT — W2A CF T-14m HOUR-TAPE JOIN

- **AUDIT_ID:** `CLOCK_AUDIT_W2A_CF_T14_JOIN`
- **FEATURE:** `DRAFT-FEAT-20260913-003`
- **GATE:** `DRAFT-ABST-20260913-003`
- **WAVE:** `W2-A / Wave 004`
- **AUDITED_AT_UTC:** 2026-09-13T19:36:29.235808+00:00
- **VERDICT (join only):** **CONDITIONAL**
- **VERDICT_SCOPE:** join_only

## Scope (hard)

- No alpha / no Examiner Δ or scores
- No invented CF prints
- No Binance; EXPIRATION_VALUE audit-only never a feature
- NOT the close-minute CLEARED path (F2)
- No T−1 mid substitute
- No new fetch; sources listed below
- Trade FORBIDDEN

## Sources

- **checkpoints:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **pm001_kalshi:** `/workspace/lab/data/DATA-PROV-PM-001/normalized/kalshi_15m_btc_eth_resolved.ndjson`
- **cf_hour_raw:** `/workspace/lab/data/DATA-PROV-CF-001/raw`
- **feature_card:** `/workspace/lab/archive/features/DRAFT-FEAT-20260913-003-W2A-cf-mid-basis.md`
- **gate_card:** `/workspace/lab/archive/features/DRAFT-ABST-20260913-003-W2A-uncertainty.md`
- **prior_cf_verdict:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md`
- **clock_order:** `/workspace/lab/governance/CLOCK_ORDER_W2A_CF_T14_JOIN_2026-09-13.md`
- **script:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/clock_audit_W2A_CF_T14_JOIN.py`
- **forbidden_close_minute_not_used:** `/workspace/lab/data/DATA-PROV-CF-001/derived/close_minute_1hz.ndjson`
- **forbidden_pre_close_not_used:** `/workspace/lab/data/DATA-PROV-CF-001/derived/pre_close_last.ndjson`
- **new_fetch:** `False`

## Join rule (fail-closed)

```
cf_t = last-in-second CF print from DATA-PROV-CF-001 HOUR tape (BRTI if BTC else ETHUSD_RTI); s = floor(decision_time_ms/1000); among prints with floor(time/1000)==s AND time<=decision_time_ms, take max(time) print's value; require exists. K = PM-001.FLOOR_STRIKE by contract_id; require present AND OPEN_TIME<=decision_time. m_t = same-row PM-003 mid; mid timestamp = decision_time. rem=840. Fail-closed if any missing. NOT close-minute CLEARED extractor; NOT Binance; NOT EXPIRATION_VALUE; NOT T-1 mid.
```

### Incomplete-second (A vs B)

- **A (order-literal / primary pairable counts):** `s=floor(t/1000)`; last print in `s` with `time<=t`
- **B (completed-second safe / measured):** if `t%1000==0` use last-in-second of `s-1`; else same as A
- Do **not** silently switch Feature to B; document caveat if A/B diverge or if A uses incomplete current second.

## Exact counts per headline

### headline_BTC_T14m — `KALSHI|15m|BTC|T-14m|mid`

- **N scored** after TEST-007-style excludes (mid, rem=840, not near-deg, not VOID/DISPUTED, same-t mid): **604**
- **N pairable (A: cf+K+m):** **604**
- **N pairable (B: cf+K+m, measured):** **604**
- **N missing cf_t (A):** **0**
- **N missing cf_t (B):** **0**
- **N missing K:** **0**
- **N missing m_t:** **0**
- **N missing either (A, fail-closed):** **0**
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 0, 'void_disputed_scored_dropped': 0, 'missing_same_t_mid_dropped': 0}`
- Missing reasons A: `{}`
- On-second boundary: 604/604
- cf lag_ms A: min=0 max=0 median=0.0 unique=[0]
- cf lag_ms B: min=200 max=200 median=200.0 unique=[200]
- cf print ms-mod A counts: `{'0': 604}`
- K: present=604, null=0, OPEN<=t=604, knowable_at_t=True
- m_t: knowable_at_t=True, T−1_used=False
- cf A: knowable_at_t=True, lookahead=False, close_minute_used=False
- Hour tape: loaded=167, missing_hours=[]
- Before close_start: 604/604 (all=True)

### headline_ETH_T14m — `KALSHI|15m|ETH|T-14m|mid`

- **N scored** after TEST-007-style excludes (mid, rem=840, not near-deg, not VOID/DISPUTED, same-t mid): **604**
- **N pairable (A: cf+K+m):** **604**
- **N pairable (B: cf+K+m, measured):** **604**
- **N missing cf_t (A):** **0**
- **N missing cf_t (B):** **0**
- **N missing K:** **0**
- **N missing m_t:** **0**
- **N missing either (A, fail-closed):** **0**
- Scored exclude breakdown: `{'non_mid_at_rem_dropped': 0, 'near_deg_scored_dropped': 0, 'void_disputed_scored_dropped': 0, 'missing_same_t_mid_dropped': 0}`
- Missing reasons A: `{}`
- On-second boundary: 604/604
- cf lag_ms A: min=0 max=0 median=0.0 unique=[0]
- cf lag_ms B: min=200 max=200 median=200.0 unique=[200]
- cf print ms-mod A counts: `{'0': 604}`
- K: present=604, null=0, OPEN<=t=604, knowable_at_t=True
- m_t: knowable_at_t=True, T−1_used=False
- cf A: knowable_at_t=True, lookahead=False, close_minute_used=False
- Hour tape: loaded=167, missing_hours=[]
- Before close_start: 604/604 (all=True)

## Certify A–G

### A_cf
- **pass:** True
- cf_t = last-in-second from DATA-PROV-CF-001 hour tape (BRTI/ETHUSD_RTI); print.time <= decision_time_ms on all scored (A); no look-ahead; not close-minute path. Incomplete-second caveat: all t on-second; A uses ms=0 print of unfinished s. B (s-1) also complete — documented, not silently adopted.

### B_K
- **pass:** True
- K = FLOOR_STRIKE from PM-001 by contract_id. Present + OPEN_TIME<=t on all scored. [V] static dump snapshot — one FLOOR_STRIKE per CONTRACT_ID; [A] no post-OPEN revision feed in this dump (cannot observe revisions). Tags: [V] snapshot, [A] no revision feed.

### C_m
- **pass:** True
- m_t = same-row PM-003 mid; decision_time present; implied_p present. No T−1 mid substitute.

### D_scored_row
- **pass:** True
- Scored: rem=840, venue=KALSHI, window=15m, implied_p_method==mid, not near-deg (≤0.02/≥0.98), VOID/DISPUTED excluded, same-t mid required (TEST-007-style). See per-headline exclude breakdown.

### E_coverage
- **pass:** True
- Per headline (primary A): {'KALSHI|15m|BTC|T-14m|mid': {'N_scored': 604, 'N_pairable_A': 604, 'N_pairable_B': 604, 'N_missing_cf_A': 0, 'N_missing_cf_B': 0, 'N_missing_K': 0, 'N_missing_m': 0, 'N_missing_either_A': 0}, 'KALSHI|15m|ETH|T-14m|mid': {'N_scored': 604, 'N_pairable_A': 604, 'N_pairable_B': 604, 'N_missing_cf_A': 0, 'N_missing_cf_B': 0, 'N_missing_K': 0, 'N_missing_m': 0, 'N_missing_either_A': 0}}

### F_knowability
- **pass:** True
- cf_detail: Yes under A (print exists, time<=t). Caveat: incomplete-second boundary on all rows — A is not completed-second 1Hz.
- K_detail: Yes if frozen at OPEN and OPEN<=t. Certified OPEN<=t; static dump [V] / no revision feed [A].
- m_detail: Yes: same-row mid at decision_time.
- lookahead_detail: No look-ahead: chosen print.time <= decision_time_ms always (A and B).
- incomplete_second_detail: All decision_times on-second; A lag=0 (print at t); B lag=200ms (s-1). Both dense. CONDITIONAL caveat — do not treat A as completed second.

### G_forbidden_paths
- **pass:** True
- Unused for join values: close_minute_1hz.ndjson, pre_close_last, Binance, EXPIRATION_VALUE as feature/join key, T−1 mid, invented prints. EXPIRATION_VALUE inventoried on PM-001 only.

## Incomplete-second A vs B

### `KALSHI|15m|BTC|T-14m|mid`
- all_on_second_boundary: True
- A_cf_ok: 604
- B_cf_ok: 604
- A_and_B_both_complete: True
- caveat: A has zero holes but uses incomplete-second boundary prints (lag=0, print at exact t). B also complete (lag≈200ms from s-1). Stamp CONDITIONAL knowability caveat; do not silently switch to B.

### `KALSHI|15m|ETH|T-14m|mid`
- all_on_second_boundary: True
- A_cf_ok: 604
- B_cf_ok: 604
- A_and_B_both_complete: True
- caveat: A has zero holes but uses incomplete-second boundary prints (lag=0, print at exact t). B also complete (lag≈200ms from s-1). Stamp CONDITIONAL knowability caveat; do not silently switch to B.

## Knowability / look-ahead

- **cf knowable at t (A)?** **True** — Yes under A (print exists, time<=t). Caveat: incomplete-second boundary on all rows — A is not completed-second 1Hz.
- **K knowable at t?** **True** — Yes if frozen at OPEN and OPEN<=t. Certified OPEN<=t; static dump [V] / no revision feed [A].
- **m_t knowable at t?** **True** — Yes: same-row mid at decision_time.
- **Look-ahead?** **False** — No look-ahead: chosen print.time <= decision_time_ms always (A and B).
- **Incomplete-second caveat?** **True** — All decision_times on-second; A lag=0 (print at t); B lag=200ms (s-1). Both dense. CONDITIONAL caveat — do not treat A as completed second.

## Integrity footnotes

- PM-001 meta: `{'n_rows': 1328, 'n_unique_contract_id': 1328, 'n_unique_venue_native_id': 1328, 'n_null_FLOOR_STRIKE': 0, 'status_counts': {'RESOLVED': 1328}, 'resolution_counts': {'YES': 660, 'NO': 668}, 'one_row_per_contract': True, 'revision_feed_present': False, 'revision_policy_tag': '[V] static dump snapshot — one FLOOR_STRIKE per CONTRACT_ID; [A] no post-OPEN revision feed in this dump (cannot observe revisions).', 'EXPIRATION_VALUE_note': 'Field present on PM-001 rows for audit inventory only; FORBIDDEN in feature join / p_t construction / cf join key.', 'n_null_EXPIRATION_VALUE': 0}`
- Prior CF-001 DATA VERDICT CLEARED = close-minute 1Hz + pre_close_last only; this audit certifies a **different** join (hour tape at rem=840).
- Forbidden derived paths exist on disk but were **not** used for join values: `/workspace/lab/data/DATA-PROV-CF-001/derived/close_minute_1hz.ndjson`, `/workspace/lab/data/DATA-PROV-CF-001/derived/pre_close_last.ndjson`.

## Verdict recommendation (join only)

**CONDITIONAL** — Join-only: hour-tape last-in-second (A) pairs on all scored rows with K present (OPEN_TIME<=t) and same-t m_t; no look-ahead (print.time<=t); forbidden paths unused. CONDITIONAL (not CLEARED) because: (1) all decision_times are on-second boundaries and A selects the ms=0 print of the *incomplete* current second — order forbids treating incomplete current second as complete; B (completed-second safe, s-1) is also dense (document, do not silently switch); (2) FLOOR_STRIKE is [V] snapshot / [A] no revision feed; (3) prior CF-001 CLEARED is close-minute F2 path only — this T-14m hour-tape join is a distinct path (READY ≠ CLEARED for F2 reuse).

This is not an Examiner skill verdict and not permission to trade. Not a claim that the F2 close-minute path CLEARED this join.
