# CLOCK AUDIT — DATA-PROV-CB-001 × PM-003 completed-bar join

- **AUDIT_ID:** `CLOCK_AUDIT_CB001_PM003_JOIN`
- **AUDITED_AT_UTC:** 2026-09-13T20:51:23.593424+00:00
- **VERDICT (join only):** **CONDITIONAL**
- **VERDICT_SCOPE:** `join_only`
- **QUALITY_STATUS:** `JOIN_CERTIFIED_WITH_ON_MINUTE_CAVEAT`
- **Trade:** FORBIDDEN
- **Not a Feature. Not READY.** No alpha. No Examiner scores / no `p_t` in this audit.

## Scope (hard)

- Independent rebuild from raw Coinbase CSV + PM-003 checkpoints — do **not** trust claim 6040/6040
- Completed-bar policy only; incomplete current minute = missing
- No Binance / CF / BRTI / L3 fill
- `v_CB` not treated as forecast
- Inventory join for later Coinbase-velocity card (Wave 007 gate)
- No new network fetch

## Sources

- **pm003:** `/workspace/lab/data/DATA-PROV-PM-003/derived/checkpoints.ndjson`
- **btc_csv:** `/workspace/lab/data/DATA-PROV-CB-001/raw/BTC-USD_1m.csv`
- **eth_csv:** `/workspace/lab/data/DATA-PROV-CB-001/raw/ETH-USD_1m.csv`
- **claim_join:** `/workspace/lab/data/DATA-PROV-CB-001/derived/pm003_cb_join.ndjson`
- **claim_coverage:** `/workspace/lab/data/DATA-PROV-CB-001/derived/pm003_cb_join_coverage.json`
- **join_script_intent_only:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/join_pm003_cb.py`
- **fetch_summary:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/FETCH_SUMMARY.json`
- **new_network_fetch:** `False`

## Join rule (fail-closed)

```
cb_close_t   = Coinbase 1m close whose bar_end <= decision_time
               bar_end = candle_start + 60s
               product = BTC-USD if BTC else ETH-USD
               source  = DATA-PROV-CB-001 raw CSV
cb_close_tm1 = prior completed 1m close (bar immediately before cb_close_t)
v_CB,t       = (cb_close_t - cb_close_tm1) / cb_close_tm1
m_t          = same-row PM-003 mid/implied_p; timestamp = decision_time
```

## Raw density

- **BTC-USD:** in-window 10140/10140; missing=0; file_unique=10142; extra_outside=2 ['2026-09-04T19:59:00Z', '2026-09-11T21:00:00Z']
- **ETH-USD:** in-window 10140/10140; missing=0; file_unique=10142; extra_outside=2 ['2026-09-04T19:59:00Z', '2026-09-11T21:00:00Z']

## PM-003 inventory

- rows_total / with_decision_time: **6040 / 6040**
- decision_times on exact minute (`…:00`): **6040/6040**
- implied_p_method counts: `{'mid': 5330, 'last': 709, 'null': 1}`

## Independent rebuild vs claim

| Metric | Independent | Claim |
|--------|-------------|-------|
| join / close_ok | 6040 | 6040 |
| velocity_ok | 6040 | (claimed all) |
| 100% field match rows | 6040 | — |
| mismatch rows | 0 | — |
| lookahead (bar_end > t) | 0 | claimed 0 |

## On-minute coincidence (CRITICAL)

- bar_end == decision_time: **6040/6040**
- bar_end < decision_time: **0/6040**
- lag_sec unique: `[0]`
- lag histogram: `{0: 6040}`

**Knowability caveat:** SPEC allows `bar_end <= decision_time`, so the bar ending at `t` is selected when Kalshi `decision_time` is an exact minute boundary. Whether that Coinbase 1m candle close is knowable-at-t at the exact second the minute ends (exchange close availability) is **not** established by this tape. Same class as W2-A incomplete-second. **Do not silently CLEARED.**

### Strict prior-minute alt (measured, not adopted)

- rule: `bar_end < decision_time` (≡ `bar_end <= decision_time - 1s`)
- strict close_ok / velocity_ok: **6040 / 6040**
- coverage delta vs SPEC: close `0`, velocity `0` (dense tape → no coverage loss)
- Do **not** silently switch Feature join to strict without Clock order amendment.

## By asset × rem

| asset | rem | n | close_ok | velocity_ok | on_min_eq | strict_close | missing_close | lookahead |
|-------|-----|---|----------|-------------|-----------|--------------|---------------|-----------|
| BTC | T-14m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| BTC | T-10m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| BTC | T-5m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| BTC | T-1m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| BTC | T-0 | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-14m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-10m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-5m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-1m | 604 | 604 | 604 | 604 | 604 | 0 | 0 |
| ETH | T-0 | 604 | 604 | 604 | 604 | 604 | 0 | 0 |

## Certify A–G

### A_cb_close
- **pass:** True
- Completed bar only (bar_end <= decision_time); no incomplete-minute close used. close_ok=6040/6040; incomplete_used=0.
- **caveat:** ALL joins have bar_end == decision_time (on-minute coincidence). SPEC allows <= ; exchange candle close availability at the exact second the minute ends is not proven from this tape alone — knowability caveat (cf. W2-A incomplete-second).

### B_prior
- **pass:** True
- Prior completed bar (start_t-60) present for velocity. velocity_ok=6040; missing_prior_only=0.

### C_velocity
- **pass:** True
- v_CB=(cb_close_t - cb_close_tm1)/cb_close_tm1; knowable only if both closes exist. velocity_ok=6040/6040.
- **caveat:** ALL joins have bar_end == decision_time (on-minute coincidence). SPEC allows <= ; exchange candle close availability at the exact second the minute ends is not proven from this tape alone — knowability caveat (cf. W2-A incomplete-second).

### D_m
- **pass:** True
- m_t = same-row PM-003 implied_p at decision_time (inventory; method mix retained). method_counts={'mid': 5330, 'last': 709, 'null': 1}.
- **note:** Not all rows are mid; mid vs last counted — join attaches CB velocity to every rem row.

### E_coverage
- **pass:** True
- Independent N close_ok=6040/6040; velocity_ok=6040/6040; claim join_rows=6040; 100% field match vs claim=6040; mismatches=0.

### F_lookahead
- **pass:** True
- bar_end > decision_time count=0.

### G_forbidden
- **pass:** True
- No Binance/CF/BRTI/L3 fill; raw source = DATA-PROV-CB-001 CSV only; v_CB not treated as forecast; no Examiner scores / no p_t in this audit.

## Verdict

**CONDITIONAL** — Independent rebuild matches claim 6040/6040, 0 lookahead, completed-bar SPEC (bar_end <= t) sound and dense. CONDITIONAL (not CLEARED) because EVERY join uses bar_end == decision_time (lag=0 on-minute coincidence): candle close knowability at the exact minute boundary is not proven from the 1m tape alone — same class of caveat as W2-A incomplete-second. Strict-prior alt (bar_end < t) also dense 6040/6040; do not silently switch policy.

### Blockers

- On-minute coincidence: 6040/6040 joins use bar_end == decision_time (lag=0). Candle-close knowability at exact minute boundary unresolved — document before Feature/Examiner treat v_CB as knowable-at-t without caveat.
- Strict-prior alt also 6040/6040 dense; policy choice (SPEC <= vs strict <) must be explicit — do not silent-switch.

## Artifacts

- script: `/workspace/lab/data/DATA-PROV-CB-001/provenance/clock_audit_CB001_PM003_JOIN.py`
- json: `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM003_JOIN.json`
- md: `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM003_JOIN.md`
- verdict: `/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM003_JOIN.md`

---

Sealed join-only. Examiner may be woken for Coinbase-velocity **only after** this CONDITIONAL/CLEARED gate; this audit itself carries **no** Examiner scores. Trade FORBIDDEN.
