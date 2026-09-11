# Failure classification

Every cemetery entry gets exactly one primary class; secondary tags optional.

| Class | Meaning |
|-------|---------|
| NO_EDGE | Measured expectancy ≤ 0 even gross / before realistic costs |
| COST_KILLED | Gross positive; net ≤ 0 after spread/fees/slippage/funding |
| LATENCY_KILLED | Edge dies under realistic signal→venue latency |
| OVERFIT | Fails perturbation, nearby thresholds, alternate periods, or leave-best-out |
| DATA_FAILURE | Bad/leaky/unavailable data; temporal integrity break |
| REGIME_FRAGILE | Only works in narrow regime; fails regime holdout |
| SMALL_SAMPLE | Insufficient independent observations; underpowered |
| EXECUTION_FAILURE | Not fillable / Mechanic NOT_EXECUTABLE / impact kills |
| RISK_FAILURE | Treasurer veto / limit breach / unacceptable tail |
| LIVE_DECAY | Lived then deteriorated; demoted on live evidence |
| DUPLICATE | Same or renamed prior idea; not a new test |
| OTHER | Requires free-text; escalate to Archivist + Conductor |

Primary class is immutable once filed unless Conductor + Archivist jointly correct with an audit note.
