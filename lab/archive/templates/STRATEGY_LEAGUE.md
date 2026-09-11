# STRATEGY-YYYYMMDD-NNN

Strategy League Table entry — prediction-market domain.
Blank schema per `governance/PREDICTION_MARKET_MISSION_2026-09-11.md`.
States: HYPOTHESIS | RESEARCH | CHALLENGER | CHAMPION | INACTIVE | RETIRED | CEMETERY.
Forecast ≠ trade. Market price \(m_t\) is the benchmark. No auto real-money.

- **STRATEGY_ID:** (Archivist-assigned)
- **NAME:**
- **STATE:** HYPOTHESIS
- **PROVENANCE:** originator · date UTC · related STRATEGY/EDGE/FEAT/CONTRACT/TEST/CEM/AMD IDs

## Scope
- **CONTRACT_SCOPE:** single CONTRACT_ID | family | universe rule
- **VENUE_ADAPTERS:** POLYMARKET_US | KALSHI | … (not hard-primary)
- **OUTCOME_SIDE:** YES | NO | BOTH (with abstention rule)

## Forecast spec
- **FORECAST_SPEC_REF:** frozen recipe / model hash / notebook-or-harness pointer
- **FEATURE_CARD_REFS:**
- **EDGE_CARD_REFS:** (optional; trade thesis separate)
- **ENSEMBLE_OF:** (component STRATEGY_IDs if any)
- **DECISION_TIME_RULE:**
- **INFORMATION_SET:** what enters \(\mathcal{I}_t\)
- **BENCHMARK_DEF:** how \(m_t\) is built (mid / microprice / last / other)

## Cost & trade separation
- **COST_STACK_REF:**
- **NET_EDGE_FORMULA:** \(e^{net} = p_t - m_t - c\) (or documented equivalent)
- **ABSTENTION_RULE:** when NO TRADE
- **TRADE_AUTHORIZATION:** NONE (default) | PAPER | (capital only via Treasurer — never auto)

## Tournament cell (pre-register before eval peek)
- **TOURNAMENT_CELL_ID:**
- **HORIZON / CUTOFF:**
- **MULTIPLE_TESTING_BUDGET:** pointer / family id
- **HOLDOUT / FORWARD REFS:**

## Required forecast metrics (or UNTESTED)
| Metric | Value | Notes / tags |
|--------|-------|--------------|
| Log loss (model) | UNTESTED | |
| Log loss (market baseline) | UNTESTED | |
| Δ log loss vs market | UNTESTED | |
| Brier (model) | UNTESTED | |
| Brier (market) | UNTESTED | |
| Δ Brier vs market | UNTESTED | |
| ECE / reliability | UNTESTED | |
| Net edge dist / abstention rate | UNTESTED | |
| N / span / #contracts | UNTESTED | |
| Cost sensitivity | UNTESTED | |

## League / promotion evidence
- **CELL_CHAMPION_OF:** (empty unless CHAMPION — revocable, evidence-gated)
- **EXAMINER / PROSECUTOR / MECHANIC / CANARY refs:**
- **FAILURE_CLASS:** (if CEMETERY) NO_EDGE | OVERFIT | DATA_FAILURE | COST_KILLED | CALIBRATION_FAIL | LEAKAGE | DUPLICATE | OTHER

## Evidence notes
Tag every material claim: [V] [I] [H] [A] [U]. No fabricated performance. Untested = UNTESTED.
