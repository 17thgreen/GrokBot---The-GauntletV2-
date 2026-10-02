# CLOCK AUDIT — DATA-PROV-CB-001 × PM-007 rem=180 join (lock B)

- **AUDIT_ID:** `CLOCK_AUDIT_CB001_PM007_JOIN`
- **AUDITED_AT_UTC:** 2026-09-13T21:20:59.672848+00:00
- **VERDICT (join only):** **CLEARED**
- **VERDICT_SCOPE:** `join_only`
- **QUALITY_STATUS:** `JOIN_CLEARED_LOCK_B`
- **Feature lock:** **B** (`bar_end < decision_time`)
- **Policy A:** caveat count only (`bar_end <= t`) — not Feature-scored
- **Trade:** FORBIDDEN
- **Not a Feature. Not READY.** No alpha. No Examiner scores / no `p_t`.
- **Wave:** 008 / W2-D / DRAFT-FEAT-20260913-006 inventory join

## Scope (hard)

- Independent rebuild from raw Coinbase CSV + PM-007 rem=180 checkpoints — do **not** trust claim
- Primary score = lock **B**; Policy A = caveat count ONLY
- Incomplete current minute = missing (fail-closed)
- No Binance / CF / BRTI / L3 fill
- Do **not** invent coverage from PM-003 join (rem=180 not covered)
- `v_CB` not treated as forecast
- No new network fetch

## Sources

- **pm007:** `/workspace/lab/data/DATA-PROV-PM-007/derived/checkpoints.ndjson`
- **btc_csv:** `/workspace/lab/data/DATA-PROV-CB-001/raw/BTC-USD_1m.csv`
- **eth_csv:** `/workspace/lab/data/DATA-PROV-CB-001/raw/ETH-USD_1m.csv`
- **claim_join:** `/workspace/lab/data/DATA-PROV-CB-001/derived/pm007_cb_join.ndjson`
- **claim_coverage:** `/workspace/lab/data/DATA-PROV-CB-001/derived/pm007_cb_join_coverage.json`
- **join_script_intent_only:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/join_pm007_cb.py`
- **new_network_fetch:** `False`

## Join rule — Feature lock B (PRIMARY)

```
decision_time = PM-007 row decision_time (CLOSE−180)
product       = BTC-USD if BTC else ETH-USD
bar           = last CB-001 1m candle with bar_end < decision_time   # STRICT <
prior         = immediately previous completed 1m (bar_end = bar.bar_end - 60)
v_CB          = (bar.close - prior.close) / prior.close
m_t           = PM-007 same-row mid; require implied_p_method == mid
```

## Policy A (caveat count ONLY)

```
bar = last CB-001 1m with bar_end <= decision_time
# Count how often A selects bar_end == decision_time (on-minute coincidence)
# Do NOT Feature-score. Do NOT silently switch from B to A.
```

## Raw density

- **BTC-USD:** in-window 10140/10140; missing=0; file_unique=10142; extra_outside=2 ['2026-09-04T19:59:00Z', '2026-09-11T21:00:00Z']
- **ETH-USD:** in-window 10140/10140; missing=0; file_unique=10142; extra_outside=2 ['2026-09-04T19:59:00Z', '2026-09-11T21:00:00Z']

## PM-007 inventory

- rows_total / with_decision_time: **1208 / 1208**
- rem counts: `{180: 1208}`
- decision_times on exact minute (`…:00Z`): **1208/1208**
- implied_p_method counts: `{'mid': 1208}`

## Independent rebuild (lock B) vs claim

| Metric | Independent (B) | Claim |
|--------|-----------------|-------|
| join / close_ok | 1208 | 1208 |
| velocity_ok | 1208 | (claimed all) |
| 100% field match rows | 1208 | — |
| mismatch rows | 0 | — |
| lookahead (bar_end >= t under B) | 0 | claimed 0 |
| B bar_end == t | 0 | (must be 0) |

## Lag under lock B

- lag_sec unique: `[60]`
- lag histogram: `{60: 1208}`
- bar_end < t: **1208/1208**; bar_end == t: **0/1208**
- Expect typically **60s** lag when decision_time is on the minute (B skips the on-boundary bar).

## Policy A caveat counts (NOT Feature-scored)

- A close_ok / velocity_ok: **1208 / 1208**
- A on-minute (bar_end == t): **1208/1208**
- A lookahead (bar_end > t): **0**
- A lag_sec unique: `[0]`

**Knowability note:** Policy A would select the bar ending at `t` for every on-minute decision_time — same on-boundary caveat class as CB×PM003. Feature lock is **B**, which uses the prior completed minute (`bar_end < t`). A counts are documented only.

## By asset × rem

| asset | rem | n | B_close | B_vel | B_lookahead | B_eq_t | A_on_min | mid_ok |
|-------|-----|---|---------|-------|-------------|--------|----------|--------|
| BTC | T-3m | 604 | 604 | 604 | 0 | 0 | 604 | 604 |
| ETH | T-3m | 604 | 604 | 604 | 0 | 0 | 604 | 604 |

## Certify A–G (under lock B)

### A_cb_close_B
- **pass:** True
- Feature lock B: last CB-001 1m with bar_end < decision_time. B_close_ok=1208/1208; B_bar_end_lt_t=1208; B_bar_end_eq_t=0 (must be 0); B_lookahead(bar_end>=t)=0.

### B_prior
- **pass:** True
- Prior completed bar (bar_end_B - 60) present for velocity under lock B. B_velocity_ok=1208; missing_prior_only=0.

### C_velocity
- **pass:** True
- v_CB=(bar.close - prior.close)/prior.close under lock B; knowable iff both closes exist. B_velocity_ok=1208/1208.

### D_m
- **pass:** True
- m_t = same-row PM-007 mid; require implied_p_method == mid. mid_ok=1208/1208; non_mid=0; method_counts={'mid': 1208}.

### E_coverage
- **pass:** True
- Independent B close_ok=1208/1208; B velocity_ok=1208/1208; claim join_rows=1208; 100% field match vs claim=1208; mismatches=0; rem=180 only=1208.
- **note:** PM-003 join does NOT cover rem=180 — this audit is independent.

### F_lookahead
- **pass:** True
- Under B: bar_end >= t count=0; bar_end == t count=0; B_silently_equals_A_on_minute=0. (Policy A lookahead bar_end > t = 0 — caveat count only.)

### G_forbidden
- **pass:** True
- No Binance/CF/BRTI/L3 fill; raw source = DATA-PROV-CB-001 CSV only; no PM-003-join reuse as proof of rem=180 coverage; v_CB not treated as forecast; no Examiner scores / no p_t / no alpha; Trade FORBIDDEN; Not Feature; Not READY.

## Verdict

**CLEARED** — Independent rebuild under Feature lock B (bar_end < decision_time) matches claim 1208/1208, 0 lookahead, dense BTC/ETH, B never uses bar_end==t (lag typically 60s when t on-minute). Policy A on-minute coincidence (1208/1208) noted as caveat-count only — not Feature-scored. PM-003 join does not cover rem=180; this audit is independent from CB raw CSV + PM-007 checkpoints.

### Blockers

- (none under lock B)

### Caveats (named, non-blocking under B when CLEARED)

- **policy_A_on_minute_caveat_count_only:** Policy A (bar_end <= t) selects bar_end == t for every on-minute decision_time. That is a caveat COUNT only — Feature lock is B (bar_end < t), which never uses the on-boundary bar. Do not Feature-score A. Do not silently switch from B to A.
- **pm003_join_does_not_cover_rem_180:** Prior CB×PM003 CONDITIONAL verdict covers rem 840/600/300/60/0 only. This rem=180 join is rebuilt independently; do not invent coverage from PM-003.

## Artifacts

- script: `/workspace/lab/data/DATA-PROV-CB-001/provenance/clock_audit_CB001_PM007_JOIN.py`
- json: `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM007_JOIN.json`
- md: `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM007_JOIN.md`
- verdict: `/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM007_JOIN.md`

---

Sealed join-only under Feature lock B. Not Feature / Not READY / Not Examiner. Trade FORBIDDEN. PM-003 join does not cover rem=180.
