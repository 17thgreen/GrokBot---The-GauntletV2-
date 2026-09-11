# TEST-20260911-006 — PM-002 MARKET BASELINE

**TEST_ID:** `TEST-20260911-006`
**Package:** `PM002-MARKET-BASELINE`
**Purpose:** venue calibration of $m_t$ — **not** a strategy
**DATA:** `DATA-PROV-PM-002` checkpoints + PM-001 resolution labels
**Overall verdict:** `FAIL-INSUFFICIENT`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Model p_t:** none (UNTESTED for all model metrics)
**Run UTC:** `2026-09-11T21:32:23Z`

## Authority
- `governance/EXAMINER_ORDER_PM002_MARKET_BASELINE.md`
- `governance/PM002_COVERAGE_FROZEN_2026-09-11.md`
- `governance/BINARY_EXAMINER_SPEC.md`
- `data/DATA-PROV-PM-002/provenance/DATA_VERDICT_DATA-PROV-PM-002.md`

## Filters (primary)
- venue=KALSHI, window=15m, assets BTC/ETH separate
- checkpoints: T-14m (rem≈840), T-10m (rem≈600), T-5m (rem≈300) — labels from rem map; actual rem values verified in data
- `implied_p_method == mid` only; exclude last-fallback
- exclude `implied_p ≤ 0.02` or `≥ 0.98`
- VOID/DISPUTED out of scored N (void bucket separate)
- **Do not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as $m_t$
- Never pool Kalshi+Poly; never score Poly as mid

## WR definition (descriptive only)
`mid > 0.5` ⇒ YES prediction; `mid < 0.5` ⇒ NO; `mid == 0.5` excluded from WR denominator. **Not a skill claim.**

## Primary cells

| Cell | N | WR | CI | Brier_market | LogLoss_market | mean(m_t) | Calibration note | Verdict |
|------|--:|---:|----|-------------:|---------------:|----------:|------------------|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 60 | 0.6333 | [0.5068, 0.7438] (Wilson 95%) | 0.234892 | 0.662958 | 0.4848 | powered calibration underpowered: N=60, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-14m|mid` | 60 | 0.6833 | [0.5577, 0.7869] (Wilson 95%) | 0.219355 | 0.629950 | 0.4675 | powered calibration underpowered: N=60, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-10m|mid` | 60 | 0.6833 | [0.5577, 0.7869] (Wilson 95%) | 0.198882 | 0.576943 | 0.4672 | powered calibration underpowered: N=60, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-10m|mid` | 60 | 0.6949 | [0.5685, 0.7975] (Wilson 95%) | 0.184715 | 0.541790 | 0.4627 | powered calibration underpowered: N=60, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|BTC|T-5m|mid` | 54 | 0.7963 | [0.6710, 0.8823] (Wilson 95%) | 0.141273 | 0.430744 | 0.4434 | powered calibration underpowered: N=54, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-5m|mid` | 51 | 0.8039 | [0.6754, 0.8898] (Wilson 95%) | 0.118026 | 0.368297 | 0.5103 | powered calibration underpowered: N=51, powered_bins=1 (need ≥2 bins with n≥20 and/or N≥100 for ECE); thin bins UNTESTED, not pooled | `FAIL-INSUFFICIENT` |

### Reliability tables (pre-registered bins; thin → UNTESTED, not pooled)

#### `KALSHI|15m|BTC|T-14m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 36 | 0.4192 | 0.2778 | [0.1585, 0.4399] (Wilson 95%) |
| [0.50,0.55) | 8 | 0.5225 | UNTESTED | UNTESTED |
| [0.55,0.60) | 8 | 0.5800 | UNTESTED | UNTESTED |
| [0.60,0.70) | 7 | 0.6364 | UNTESTED | UNTESTED |
| [0.70,0.80) | 1 | 0.7250 | UNTESTED | UNTESTED |
| [0.80,0.90) | 0 | UNTESTED | UNTESTED | UNTESTED |
| [0.90,0.98) | 0 | UNTESTED | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

#### `KALSHI|15m|ETH|T-14m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 35 | 0.3929 | 0.2857 | [0.1633, 0.4506] (Wilson 95%) |
| [0.50,0.55) | 8 | 0.5238 | UNTESTED | UNTESTED |
| [0.55,0.60) | 10 | 0.5725 | UNTESTED | UNTESTED |
| [0.60,0.70) | 7 | 0.6264 | UNTESTED | UNTESTED |
| [0.70,0.80) | 0 | UNTESTED | UNTESTED | UNTESTED |
| [0.80,0.90) | 0 | UNTESTED | UNTESTED | UNTESTED |
| [0.90,0.98) | 0 | UNTESTED | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

#### `KALSHI|15m|BTC|T-10m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 35 | 0.3174 | 0.2286 | [0.1207, 0.3902] (Wilson 95%) |
| [0.50,0.55) | 3 | 0.5083 | UNTESTED | UNTESTED |
| [0.55,0.60) | 3 | 0.5783 | UNTESTED | UNTESTED |
| [0.60,0.70) | 10 | 0.6390 | UNTESTED | UNTESTED |
| [0.70,0.80) | 5 | 0.7630 | UNTESTED | UNTESTED |
| [0.80,0.90) | 3 | 0.8483 | UNTESTED | UNTESTED |
| [0.90,0.98) | 1 | 0.9115 | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

#### `KALSHI|15m|ETH|T-10m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 33 | 0.2837 | 0.2727 | [0.1507, 0.4422] (Wilson 95%) |
| [0.50,0.55) | 5 | 0.5130 | UNTESTED | UNTESTED |
| [0.55,0.60) | 4 | 0.5650 | UNTESTED | UNTESTED |
| [0.60,0.70) | 4 | 0.6350 | UNTESTED | UNTESTED |
| [0.70,0.80) | 9 | 0.7328 | UNTESTED | UNTESTED |
| [0.80,0.90) | 3 | 0.8650 | UNTESTED | UNTESTED |
| [0.90,0.98) | 2 | 0.9210 | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

#### `KALSHI|15m|BTC|T-5m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 30 | 0.1748 | 0.1333 | [0.0531, 0.2968] (Wilson 95%) |
| [0.50,0.55) | 1 | 0.5250 | UNTESTED | UNTESTED |
| [0.55,0.60) | 3 | 0.5783 | UNTESTED | UNTESTED |
| [0.60,0.70) | 2 | 0.6500 | UNTESTED | UNTESTED |
| [0.70,0.80) | 5 | 0.7390 | UNTESTED | UNTESTED |
| [0.80,0.90) | 9 | 0.8550 | UNTESTED | UNTESTED |
| [0.90,0.98) | 4 | 0.9376 | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

#### `KALSHI|15m|ETH|T-5m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 26 | 0.2053 | 0.1923 | [0.0851, 0.3788] (Wilson 95%) |
| [0.50,0.55) | 0 | UNTESTED | UNTESTED | UNTESTED |
| [0.55,0.60) | 2 | 0.5775 | UNTESTED | UNTESTED |
| [0.60,0.70) | 4 | 0.6350 | UNTESTED | UNTESTED |
| [0.70,0.80) | 1 | 0.7500 | UNTESTED | UNTESTED |
| [0.80,0.90) | 8 | 0.8562 | UNTESTED | UNTESTED |
| [0.90,0.98) | 10 | 0.9392 | UNTESTED | UNTESTED |
- ECE: `UNTESTED`

## UNTESTED keys (no model / no strategy)
Brier_model, LogLoss_model, ΔBrier, ΔLogLoss, gap, EV_gross, EV_net, abstention_rate, cost_sensitivity — all **UNTESTED** on every cell.

## Filter / join stats (primary)
```json
{
  "candidates": 360,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 15,
  "excluded_no_label": 0,
  "excluded_void_or_other": 0,
  "scored": 345,
  "void_bucket_n": 0,
  "void_bucket": []
}
```

## Annex A — Poly last-print non-T−0 (weaker; NOT mid)

Scored as last-print benchmark only. Lag caveat per Clock. Never pooled with Kalshi.

| Cell | N | WR | Brier_market | LogLoss_market | mean(m_t) | Verdict |
|------|--:|---:|-------------:|---------------:|----------:|---------|
| `POLYMARKET_GLOBAL|15m|BTC|T-10m|last` | 30 | 0.5667 | 0.263245 | 0.738074 | 0.4713 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|BTC|T-14m|last` | 30 | 0.5333 | 0.267152 | 0.735782 | 0.4850 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|BTC|T-1m|last` | 22 | 0.7273 | 0.187167 | 0.540883 | 0.5281 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|BTC|T-5m|last` | 30 | 0.8000 | 0.155710 | 0.472545 | 0.5730 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|ETH|T-10m|last` | 30 | 0.6667 | 0.221394 | 0.631456 | 0.4818 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|ETH|T-14m|last` | 30 | 0.7667 | 0.240798 | 0.680842 | 0.4820 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|ETH|T-1m|last` | 16 | 0.8750 | 0.074581 | 0.252836 | 0.4322 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|15m|ETH|T-5m|last` | 29 | 0.8621 | 0.122070 | 0.393973 | 0.5522 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|BTC|T-1m|last` | 25 | 0.6800 | 0.199953 | 0.595266 | 0.4962 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|BTC|T-3m|last` | 30 | 0.7333 | 0.189892 | 0.560437 | 0.4950 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|BTC|T-4m|last` | 30 | 0.5667 | 0.226177 | 0.642837 | 0.4885 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|ETH|T-1m|last` | 27 | 0.8148 | 0.119560 | 0.382228 | 0.4194 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|ETH|T-3m|last` | 30 | 0.8333 | 0.166343 | 0.510068 | 0.4950 | `FAIL-INSUFFICIENT` |
| `POLYMARKET_GLOBAL|5m|ETH|T-4m|last` | 30 | 0.5333 | 0.238201 | 0.668483 | 0.5022 | `FAIL-INSUFFICIENT` |

## Annex B — Kalshi T−1m mid (CLEARED_WITH_STRONG_CAVEAT)

High near-degeneracy at T−1m; last-fallback excluded. Optional annex only.

| Cell | N | WR | Brier_market | LogLoss_market | mean(m_t) | Verdict |
|------|--:|---:|-------------:|---------------:|----------:|---------|
| `KALSHI|15m|BTC|T-1m|mid` | 21 | 0.6667 | 0.131831 | 0.386880 | 0.4794 | `FAIL-INSUFFICIENT` |
| `KALSHI|15m|ETH|T-1m|mid` | 15 | 0.8667 | 0.118736 | 0.375575 | 0.4805 | `FAIL-INSUFFICIENT` |

## Overall package verdict
**`FAIL-INSUFFICIENT`** — All six primary cells underpowered for named calibration (thin reliability bins / ECE). Descriptive WR/Brier/LogLoss/mean(m_t) are MEASURED where N>0; powered calibration claim not supported. NOT NO_EDGE.

This is **not** a strategy PASS. No trading authorization.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260911-006-PM002-MARKET-BASELINE.json`
- `/workspace/lab/harness/examiner/out/TEST-20260911-006-PM002-MARKET-BASELINE.md`
- `/workspace/lab/archive/tests/TEST-20260911-006-PM002-MARKET-BASELINE.json`
- `/workspace/lab/archive/tests/TEST-20260911-006-PM002-MARKET-BASELINE.md`
- `/workspace/lab/archive/tests/TEST-20260911-006.json`
- `/workspace/lab/archive/tests/TEST-20260911-006.md`

checkpoints.ndjson sha256: `affbbbd0b07c765d3f7c0af5e6b23564d3973ec82f27fe7d48b84bc4ded89dc0`
