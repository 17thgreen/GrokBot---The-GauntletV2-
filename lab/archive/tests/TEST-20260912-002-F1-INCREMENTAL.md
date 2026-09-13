# TEST-20260912-002 — F1-INCREMENTAL

**Overall verdict:** `REDUNDANT / FAIL-INSUFFICIENT`
**invented_numbers:** `False` · **Trading:** FORBIDDEN · **Run UTC:** `2026-09-12T00:19:13Z`
Headlines: BTC+ETH T-5m. λ=0.35. L3 is not the oracle.

| Card | Cell | N | ΔBrier | ΔLogLoss | Verdict |
|------|------|--:|-------:|---------:|---------|
| FEAT-001 frozen σ | BTC T-5m | 569 | +0.003343 | +0.013816 | REDUNDANT |
| FEAT-001 frozen σ | ETH T-5m | 545 | +0.004107 | +0.018475 | REDUNDANT |
| FEAT-002 RV σ | BTC T-5m | 569 | +0.001072 | +0.002517 | REDUNDANT |
| FEAT-002 RV σ | ETH T-5m | 545 | +0.001216 | +0.003705 | REDUNDANT |

Cards INACTIVE. Not NO_EDGE. No λ/σ retune.
