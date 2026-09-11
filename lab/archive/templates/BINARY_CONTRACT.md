# CONTRACT-YYYYMMDD-NNN

Binary contract ground-truth record — prediction-market domain.
Blank schema per `governance/PREDICTION_MARKET_MISSION_2026-09-11.md`.
Venue adapters are abstractions (`POLYMARKET_US`, `KALSHI`, …) — not hard-primary.

- **CONTRACT_ID:** (Archivist-assigned)
- **VENUE_ADAPTER:** POLYMARKET_US | KALSHI | (other registered adapter)
- **VENUE_NATIVE_ID:**
- **TITLE / QUESTION:**
- **OUTCOMES:** YES | NO
- **STATUS:** OPEN | CLOSED | RESOLVED | VOID | DISPUTED | QUARANTINED
- **PROVENANCE:** originator · date UTC · DATA-* / AMD links
- **CONFIDENCE / tags:** material claims tagged [V][I][H][A][U]

## Rules & resolution
- **RULES_URI:**
- **RULES_HASH:** (when frozen)
- **RESOLUTION_SOURCE:**
- **RESOLUTION:** YES | NO | VOID | (empty if unresolved)
- **RESOLUTION_EVIDENCE:** pointer + tag [V] / [U]
- **DISPUTE_NOTES:**

## Timeline (UTC)
- **OPEN_TIME:**
- **CLOSE_TIME:** (trade cutoff)
- **RESOLVE_TIME:** (official / expected)
- **TIMEZONE / clock source:** exchange event vs receive time

## Market microstructure linkage
- **TICK_SIZE:**
- **FEE_SCHEDULE_REF:**
- **LIQUIDITY_NOTES:** (tag each claim; inventing depth forbidden)
- **BENCHMARK_PRICE_RULE:** mid | microprice | last | other (explicit) — used as \(m_t\)

## Knowability (Clock grades)
- What is knowable at decision timestamp t?
- Revision / restatement policy:
- Unsafe / leak-prone fields:

## Data layer links
- **L1 PM DATA-*:**
- **L2 oracle / resolution DATA-*:**
- **L3 external predictors:** (optional; decision-time only)

## Intended uses
- STRATEGY_IDs / Feature Cards this may support:
- Forbidden uses:

## Clock DATA VERDICT
- Verdict:
- Failures:
- Required remediation:
