# The Gauntlet V2 — BTC/ETH Short-Horizon Alpha Lab

Governed multi-agent research lab. **AI proposes. Code measures. Evidence promotes. Risk governs.**

## Canonical on-disk lab
Primary working copy lives on the Conductor box at `/workspace/lab/`. This repo mirrors **ledger + governance + harness specs** — not raw market data.

## Do not commit
- `data/DATA-PROV-001/` OHLCV parquets
- `data/DATA-PROV-TRADES-001/` aggTrade zips (~77GB)
- Examiner `.venv/`

Raw data stays hashed + provenance-local. Dataset IDs and Clock verdicts are recorded under `lab/archive/datasets/`.

## Layout
```
lab/
  governance/     # Authority, Edge Card standard, Cycle orders, constitutional amendments
  archive/        # Edges, cemetery, tests, datasets registry, audit
  harness/        # Provisional measurement packages
  execution/      # Mechanic EXECUTABLE rubric
```

## Current state (as of seed)
- OHLCV-native Statistician queue: EDGE-001/003/004 **cemetery** (NO_EDGE / COST_KILLED / NO_EDGE)
- Cycle 4: Tape trade-flow cards EDGE-20260911-001/002; DATA-PROV-TRADES-001 complete; Clock verdict pending
- EDGE-005/006 frozen **UNMEASURABLE WITHOUT L2**
- Promotion path: Research → Validation → Historical Sealed Holdout → Cross-Venue → Forward Shadow → Paper → Micro Capital

## Hard authorities
Clock (data) · Examiner (empirical) · Prosecutor (adversarial) · Treasurer (capital) — Conductor cannot waive.
