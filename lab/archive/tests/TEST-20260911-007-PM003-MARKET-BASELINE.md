# TEST-20260911-007 — PM-003 MARKET BASELINE

**Overall verdict:** `BASELINE_MEASURED`
**invented_numbers:** `False` · **Trading:** FORBIDDEN · **Model p_t:** none
**Run UTC:** `2026-09-11T23:06:10Z` · SHA256 verified · PM-002 overlap 0

## Primary cells

| Cell | N | WR | Brier_market | LogLoss_market | mean(m_t) | ECE | Verdict |
|------|--:|---:|-------------:|---------------:|----------:|----:|---------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 0.6043 | 0.234728 | 0.662648 | 0.5049 | 0.034636 | BASELINE_MEASURED |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 0.6417 | 0.232936 | 0.658864 | 0.5029 | 0.047409 | BASELINE_MEASURED |
| `KALSHI|15m|BTC|T-10m|mid` | 604 | 0.7053 | 0.198177 | 0.581969 | 0.5109 | 0.041487 | BASELINE_MEASURED |
| `KALSHI|15m|ETH|T-10m|mid` | 604 | 0.6960 | 0.198214 | 0.579565 | 0.5025 | 0.022895 | BASELINE_MEASURED |
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 0.7944 | 0.141266 | 0.434744 | 0.5055 | 0.024279 | BASELINE_MEASURED |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 0.8037 | 0.134160 | 0.415843 | 0.4879 | 0.032856 | BASELINE_MEASURED |

Thin T−14m bins [0.70,0.98) UNTESTED. Do not pool. Model Δ keys UNTESTED.

## Annex — Kalshi T−1m mid (CLEARED_WITH_STRONG_CAVEAT)

| Cell | N | Brier_market | LogLoss_market | mean(m_t) |
|------|--:|-------------:|---------------:|----------:|
| BTC T-1m mid | 219 | 0.149206 | 0.464352 | 0.4463 |
| ETH T-1m mid | 178 | 0.126928 | 0.400601 | 0.5240 |

This annex is the incumbent used by TEST-20260913-001 F2.
