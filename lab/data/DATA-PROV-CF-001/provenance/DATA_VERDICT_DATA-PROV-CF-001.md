# DATA VERDICT — DATA-PROV-CF-001
**Issued by:** The Clock (executor DATA-PROV-CF-001)  
**Issued UTC:** 2026-09-13T17:53:52Z  
**Authority:** `governance/DATA_PROV_CF_001_SPEC.md` · `governance/CF_001_COVERAGE_FROZEN_2026-09-13.md`

---

## DATA VERDICT: CLEARED

**QUALITY_STATUS:** APPROVED  
**Layer:** **L2 official settlement-index tape** (Kalshi CF passthrough → CF Benchmarks BRTI / ETHUSD_RTI)  
**CLEARED uses:** F2 close-minute 1Hz last-in-second + `pre_close_last`  
**NOT:** Binance-as-oracle · T−0 mid as incumbent · EXPIRATION_VALUE as feature · incomplete current second

---

## DATA MANIFEST

| Field | Value |
|-------|-------|
| DATASET_ID | DATA-PROV-CF-001 |
| SOURCE | Signed `GET /trade-api/v2/cfbenchmarks/history/values` on `https://external-api.kalshi.com` |
| INDICES | BRTI (BTC), ETHUSD_RTI (ETH) |
| START_HOUR | 2026-09-04T20:00:00.000Z |
| END_HOUR | 2026-09-11T20:00:00.000Z (inclusive) |
| FREQUENCY | 1Hz last-in-second (`max timestamp_ms` in unix second) |
| CLOSE_WINDOW | `[close_time_ms-60000, close_time_ms)` |
| PARENT_ARENA | DATA-PROV-PM-003 1208 |
| RAW_HOURS | 169 × 2 = 338 files (HTTP 337×200 + 1 SKIP_EXISTING) |
| CONTRACTS_60_60 | 1208 / 1208 |
| CONTRACTS_MISSING_ANY | 0 |
| PRE_CLOSE_LAST | 1208 / 1208 |
| MISSING_SEC_RATE_BTC | 0.000000 |
| MISSING_SEC_RATE_ETH | 0.000000 |
| RECON_MEAN_vs_EXPIRATION_VALUE | n=1208 MAE=0.144134 (audit only; not a feature) |

---

## HARD CLOCK RULES [V]

```
close_start_ms = close_time_ms - 60000
assert close_start_ms % 1000 == 0
s_start = close_start_ms // 1000
slot i locked iff (s_start + i + 1) * 1000 <= now_ms
1Hz print = max(timestamp_ms) among prints with floor(ts/1000)==s
Missing locked slot → MISSING (do not shrink /60)
```

All 1208 PM-003 close minutes have 60/60 locked seconds present on the entitled tape. Hour-level archive had ≤96 missing seconds per index outside these close minutes (declared; does not affect F2 join).

---

## BLOCKED PATHS (still forbidden)

- Binance-as-oracle substitution  
- T−0 mid as incumbent for F2 incrementality  
- EXPIRATION_VALUE as model feature / p  
- Using incomplete current second  
- Trading / holdout open / BTC+ETH pool

---

## Examiner gate

**OPEN** for `TEST-20260913-001` F2-INCREMENTAL (Map 2) under CLEARED tape + PM-003 T−1m mid + PM-001 FLOOR_STRIKE/RESOLUTION. Gate used; result filed TEST-20260913-001.
