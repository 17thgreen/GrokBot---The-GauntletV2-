# Archive Schema

## ID conventions

| Kind | Pattern | Example |
|------|---------|---------|
| Atomic Edge | `EDGE-YYYYMMDD-NNN` | `EDGE-20260910-001` |
| Strategy | `STRAT-YYYYMMDD-NNN` | `STRAT-20260910-001` |
| Strategy version | `STRAT-...-vN` | `STRAT-20260910-001-v1` |
| Test | `TEST-YYYYMMDD-NNN` | `TEST-20260910-001` |
| Cemetery entry | `CEM-YYYYMMDD-NNN` | `CEM-20260910-001` |
| Deployment | `DEP-YYYYMMDD-NNN` | `DEP-20260910-001` |
| Dataset | `DATA-YYYYMMDD-NNN` | `DATA-20260910-001` |
| Red Team finding | `RT-YYYYMMDD-NNN` | `RT-20260910-001` |
| Override | `OVR-YYYYMMDD-NNN` | `OVR-20260910-001` |
| Execution spec | `EXEC-...` | from Mechanic |

IDs are assigned only by Archivist. Dates are UTC calendar dates of first registration.

## Atomic Edge (required fields) — universal card

Competitive unit between agents. Essays are annexes only.

- EDGE_ID (Archivist-assigned only)
- THESIS (one falsifiable claim)
- MECHANISM (economic / market-mechanical why)
- MARKET (BTC/ETH; instrument class; venue explicit)
- HORIZON (5m / 10m / 15m or explicit other)
- SIGNAL (knowable at decision timestamp)
- ENTRY
- EXIT
- ABSTENTION (when not to trade; NO TRADE first-class)
- REQUIRED DATA
- PARAMETERS (initial set + perturbation plan; no magic single param)
- FAILURE REGIME
- FALSIFICATION (kill test)
- COST SENSITIVITY (spread/fees/slippage/latency/funding/impact; each tagged)
- CONFIDENCE (tagged belief — not self-graded validity)
- STATUS (HYPOTHESIS | IN_TEST | VALIDATED | HISTORICAL_HOLDOUT | CROSS_VENUE | FORWARD_SHADOW | PAPER | LIVE_* | REJECTED | RETIRED)
- PROVENANCE (originator, date UTC, related EDGE/CEM/TEST IDs, informal lineage)

Evidence tags mandatory on material statements: [V][I][H][A][U]. Untested = UNTESTED.

## Strategy version

- STRATEGY_ID / VERSION
- COMPOSITION (EDGE_IDs + combination rule)
- FROZEN_SPEC_HASH / Architect reference
- STAGE (promotion stage)
- COST_STACK assumptions (spread/fees/slippage/latency/funding) each tagged
- LINKED_TESTS / CEMETERY / DEPLOYMENTS / RT findings

## Cemetery entry (required)

- CEM_ID
- EDGE_ID / STRATEGY_ID
- ORIGINATOR
- THESIS
- DATE
- DATA (datasets / periods used)
- PARAMETERS
- RESULT (what was measured — or UNTESTED)
- WHY_IT_FAILED
- FAILURE_CLASS (see FAILURE_CLASSES.md)
- RED_TEAM_FINDING (RT_ID or summary)
- REGIME (when it failed / was fragile)
- RETEST_CONDITION (what would make retest worth it)
- RETEST_DATE (if scheduled; else NONE)

## Pre-test search report

Returned before RESEARCH TEST:

- QUERY (normalized thesis + features + horizons)
- EXACT_DUPLICATE: yes/no + IDs
- SEMANTIC_EQUIVALENT: yes/no + IDs + why
- PARAMETER_RENAME_ONLY: yes/no
- RELATED: IDs + relationship
- PRIOR_FAILURES: CEM_IDs + classes
- VERDICT: BLOCK_DUPLICATE | WARN_RELATED | CLEAR_TO_TEST


## Promotion path (constitutional — Logan 2026-09-10)

See `/workspace/lab/governance/CONSTITUTIONAL_AMENDMENT_FORWARD_AND_CROSS_VENUE.md`.

```
HYPOTHESIS
  → RESEARCH TEST
  → VALIDATION
  → HISTORICAL SEALED HOLDOUT
  → CROSS-VENUE REPLICATION   (mandatory before capital)
  → FUTURE SEALED FORWARD WINDOW / FORWARD SHADOW
  → PAPER
  → MICRO CAPITAL
  → LIMITED CAPITAL
  → PRODUCTION
```

Historical sealed holdout ≠ production proof. Forward sealed window + cross-venue mandatory before capital.
Conductor cannot waive this amendment.

## Dataset IDs

| Kind | Pattern | Example |
|------|---------|---------|
| Dataset (general) | `DATA-YYYYMMDD-NNN` | `DATA-20260910-001` |
| Provisional series | `DATA-PROV-NNN` | `DATA-PROV-001` |

Provisional reference venues are **not** venue marriage. Raw must be immutable + sha256 + manifest before Archivist marks READY. Research slices must not open until Conductor seals final 20% holdout and Clock verdicts.
