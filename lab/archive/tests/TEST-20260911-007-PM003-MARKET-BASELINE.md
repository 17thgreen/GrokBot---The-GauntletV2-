# TEST-20260911-007 — PM-003 MARKET BASELINE

**TEST_ID:** `TEST-20260911-007`
**Package:** `PM003-MARKET-BASELINE`
**Purpose:** venue calibration of $m_t$ on the 1208-slice — **not** a strategy
**DATA:** `DATA-PROV-PM-003` checkpoints + PM-001 official resolution labels
**Overall verdict:** `BASELINE_MEASURED`
**invented_numbers:** `False`
**Trading:** FORBIDDEN
**Model p_t:** none (UNTESTED for all model metrics)
**Run UTC:** `2026-09-11T23:06:10Z`
**SHA256 verified:** `True`
**PM-002 overlap:** `0` (union forbidden)
**Poly:** none (not in this dataset; not scored)

## Authority
- `governance/EXAMINER_ORDER_PM003_MARKET_BASELINE.md`
- `governance/PM003_COVERAGE_FROZEN_2026-09-11.md`
- `governance/BINARY_EXAMINER_SPEC.md`
- `data/DATA-PROV-PM-003/provenance/DATA_VERDICT_DATA-PROV-PM-003.md`

## Filters (primary)
- venue=KALSHI, window=15m, assets BTC/ETH **separate** (no pool)
- THIS 1208 only — **do not** union with PM-002 240; **do not** include PM-002 checkpoint rows
- checkpoints: T-14m (rem=840), T-10m (rem=600), T-5m (rem=300)
- `implied_p_method == mid` only; exclude last-fallback
- exclude `implied_p ≤ 0.02` or `≥ 0.98`
- VOID/DISPUTED out of scored N (void bucket separate)
- **Do not** use PM-001 `LAST_PRICE_DOLLARS` / `OUTCOME_PRICES` as $m_t$
- No Poly under this label

## WR definition (descriptive only)
`mid > 0.5` ⇒ YES prediction; `mid < 0.5` ⇒ NO; `mid == 0.5` excluded from WR denominator. **Not a skill claim.**

## Primary cells

| Cell | N | WR | CI | Brier_market | LogLoss_market | mean(m_t) | Calibration note | Verdict |
|------|--:|---:|----|-------------:|---------------:|----------:|------------------|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.6043 | [0.5648, 0.6425] (Wilson 95%) | 0.234728 | 0.662648 | 0.5049 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.6417 | [0.6025, 0.6790] (Wilson 95%) | 0.232936 | 0.658864 | 0.5029 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.7053 | [0.6677, 0.7403] (Wilson 95%) | 0.198177 | 0.581969 | 0.5109 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.6960 | [0.6581, 0.7314] (Wilson 95%) | 0.198214 | 0.579565 | 0.5025 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.7944 | [0.7592, 0.8256] (Wilson 95%) | 0.141266 | 0.434744 | 0.5055 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.8037 | [0.7682, 0.8348] (Wilson 95%) | 0.134160 | 0.415843 | 0.4879 | powered bins present; ECE computed if N allows | `BASELINE_MEASURED` |

### Reliability tables (pre-registered bins; thin → UNTESTED, not pooled)

#### `KALSHI|15m|BTC|T-14m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 290 | 0.4171 | 0.3862 | [0.3320, 0.4434] (Wilson 95%) |
| [0.50,0.55) | 115 | 0.5224 | 0.4783 | [0.3891, 0.5688] (Wilson 95%) |
| [0.55,0.60) | 88 | 0.5723 | 0.6477 | [0.5437, 0.7394] (Wilson 95%) |
| [0.60,0.70) | 90 | 0.6416 | 0.6444 | [0.5415, 0.7356] (Wilson 95%) |
| [0.70,0.80) | 18 | 0.7378 | UNTESTED | UNTESTED |
| [0.80,0.90) | 3 | 0.8550 | UNTESTED | UNTESTED |
| [0.90,0.98) | 0 | UNTESTED | UNTESTED | UNTESTED |
- ECE: `0.034636`

#### `KALSHI|15m|ETH|T-14m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 292 | 0.4113 | 0.3733 | [0.3198, 0.4301] (Wilson 95%) |
| [0.50,0.55) | 115 | 0.5260 | 0.6000 | [0.5086, 0.6849] (Wilson 95%) |
| [0.55,0.60) | 85 | 0.5723 | 0.6706 | [0.5652, 0.7612] (Wilson 95%) |
| [0.60,0.70) | 88 | 0.6401 | 0.6477 | [0.5437, 0.7394] (Wilson 95%) |
| [0.70,0.80) | 19 | 0.7355 | UNTESTED | UNTESTED |
| [0.80,0.90) | 5 | 0.8430 | UNTESTED | UNTESTED |
| [0.90,0.98) | 0 | UNTESTED | UNTESTED | UNTESTED |
- ECE: `0.047409`

#### `KALSHI|15m|BTC|T-10m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 301 | 0.3344 | 0.2890 | [0.2407, 0.3427] (Wilson 95%) |
| [0.50,0.55) | 40 | 0.5210 | 0.5750 | [0.4219, 0.7149] (Wilson 95%) |
| [0.55,0.60) | 47 | 0.5743 | 0.5745 | [0.4328, 0.7049] (Wilson 95%) |
| [0.60,0.70) | 82 | 0.6509 | 0.6220 | [0.5138, 0.7192] (Wilson 95%) |
| [0.70,0.80) | 77 | 0.7492 | 0.8182 | [0.7176, 0.8885] (Wilson 95%) |
| [0.80,0.90) | 49 | 0.8481 | 0.8163 | [0.6864, 0.9002] (Wilson 95%) |
| [0.90,0.98) | 8 | 0.9344 | UNTESTED | UNTESTED |
- ECE: `0.041487`

#### `KALSHI|15m|ETH|T-10m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 318 | 0.3200 | 0.3333 | [0.2838, 0.3869] (Wilson 95%) |
| [0.50,0.55) | 41 | 0.5237 | 0.4878 | [0.3425, 0.6352] (Wilson 95%) |
| [0.55,0.60) | 32 | 0.5773 | 0.5938 | [0.4226, 0.7448] (Wilson 95%) |
| [0.60,0.70) | 65 | 0.6542 | 0.7077 | [0.5880, 0.8042] (Wilson 95%) |
| [0.70,0.80) | 71 | 0.7488 | 0.7324 | [0.6195, 0.8215] (Wilson 95%) |
| [0.80,0.90) | 62 | 0.8396 | 0.8871 | [0.7848, 0.9442] (Wilson 95%) |
| [0.90,0.98) | 15 | 0.9371 | UNTESTED | UNTESTED |
- ECE: `0.022895`

#### `KALSHI|15m|BTC|T-5m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 282 | 0.2137 | 0.1986 | [0.1562, 0.2491] (Wilson 95%) |
| [0.50,0.55) | 25 | 0.5214 | 0.5200 | [0.3350, 0.6997] (Wilson 95%) |
| [0.55,0.60) | 17 | 0.5809 | UNTESTED | UNTESTED |
| [0.60,0.70) | 47 | 0.6601 | 0.5745 | [0.4328, 0.7049] (Wilson 95%) |
| [0.70,0.80) | 47 | 0.7544 | 0.7234 | [0.5824, 0.8306] (Wilson 95%) |
| [0.80,0.90) | 51 | 0.8559 | 0.8627 | [0.7428, 0.9319] (Wilson 95%) |
| [0.90,0.98) | 100 | 0.9433 | 0.9800 | [0.9300, 0.9945] (Wilson 95%) |
- ECE: `0.024279`

#### `KALSHI|15m|ETH|T-5m|mid`

| Bin | n | mean_m | obs_rate | CI |
|-----|--:|-------:|---------:|----|
| [0.02,0.50) | 282 | 0.2033 | 0.2163 | [0.1722, 0.2680] (Wilson 95%) |
| [0.50,0.55) | 23 | 0.5291 | 0.6087 | [0.4079, 0.7784] (Wilson 95%) |
| [0.55,0.60) | 24 | 0.5717 | 0.6250 | [0.4271, 0.7884] (Wilson 95%) |
| [0.60,0.70) | 33 | 0.6488 | 0.7576 | [0.5898, 0.8717] (Wilson 95%) |
| [0.70,0.80) | 27 | 0.7483 | 0.7037 | [0.5152, 0.8415] (Wilson 95%) |
| [0.80,0.90) | 70 | 0.8529 | 0.8286 | [0.7238, 0.8991] (Wilson 95%) |
| [0.90,0.98) | 86 | 0.9462 | 1.0000 | [0.9572, 1.0000] (Wilson 95%) |
- ECE: `0.032856`

## UNTESTED keys (no model / no strategy)
Brier_model, LogLoss_model, ΔBrier, ΔLogLoss, gap, EV_gross, EV_net, abstention_rate, cost_sensitivity — all **UNTESTED** on every cell.

Sign convention (if a model existed): ΔBrier = Brier_model − Brier_market; ΔLogLoss = LogLoss_model − LogLoss_market; negative = better than market. No model here — keys present as UNTESTED.

## Filter / join stats (primary)
```json
{
  "candidates": 3624,
  "excluded_method_not_mid": 0,
  "excluded_near_deg": 94,
  "excluded_no_label": 0,
  "excluded_void_or_other": 0,
  "scored": 3530,
  "void_bucket_n": 0,
  "void_bucket": []
}
```

## Integrity

- checkpoints.ndjson sha256: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- expected: `90e38c2f23e224def13db05924f6470a1e738778882f6b0cc17ed708b3143765`
- sha256_verified: `True`
- PM-002 overlap_count: `0`
- venues: `{'KALSHI': 6040}`
- Poly annex: **not run** (not in this dataset)
- PM-002 checkpoint rows: **not read / not scored**
- m_t source: PM-003 `checkpoints.implied_p` (mid) — never PM-001 LAST_PRICE / OUTCOME_PRICES

## Annex — Kalshi T−1m mid (CLEARED_WITH_STRONG_CAVEAT)

Optional annex **after** primary. High near-degeneracy at T−1m; last-fallback excluded. Not a primary cell. No Poly.

| Cell | N | WR | CI | Brier_market | LogLoss_market | mean(m_t) | Verdict |
|------|--:|---:|----|-------------:|---------------:|----------:|---------|
| `KALSHI|15m|BTC|T-1m|mid` | 219 | 0.7844 | [0.7251, 0.8338] (Wilson 95%) | 0.149206 | 0.464352 | 0.4463 | `BASELINE_MEASURED` |
| `KALSHI|15m|ETH|T-1m|mid` | 178 | 0.8146 | [0.7511, 0.8648] (Wilson 95%) | 0.126928 | 0.400601 | 0.5240 | `BASELINE_MEASURED` |

## Overall package verdict
**`BASELINE_MEASURED`** — At least one primary cell supports powered calibration metrics; package is honest baseline measurement (not strategy PASS). FAIL-INSUFFICIENT ≠ NO_EDGE.

FAIL-INSUFFICIENT ≠ NO_EDGE. This is **not** a strategy PASS. No trading authorization.

## Artifacts
- `/workspace/lab/harness/examiner/out/TEST-20260911-007-PM003-MARKET-BASELINE.json`
- `/workspace/lab/harness/examiner/out/TEST-20260911-007-PM003-MARKET-BASELINE.md`
- `/workspace/lab/archive/tests/TEST-20260911-007-PM003-MARKET-BASELINE.json`
- `/workspace/lab/archive/tests/TEST-20260911-007-PM003-MARKET-BASELINE.md`
- `/workspace/lab/archive/tests/TEST-20260911-007.json`
- `/workspace/lab/archive/tests/TEST-20260911-007.md`
- `/workspace/lab/archive/audit/2026-09-11-TEST-20260911-007-PM003-MARKET-BASELINE-examiner.md`
