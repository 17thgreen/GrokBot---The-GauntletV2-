# DATA-PROV-CATALYST-001 — Specification (provisional stub)
Provisional **event / positioning-stress** family for Cycle 5.
Distinct from DATA-PROV-001 (OHLCV) and DATA-PROV-TRADES-001 (trades).
**Status:** SPEC ONLY — not a fetch, not Clock-cleared, not Examiner-ready.

## Intent
Give Catalyst and Clock a shared checklist for **first provisional event-dataset registration**.
Supports incremental tests: do liquidation / OI / funding labels add predictive value beyond co-occurring price/volume (and ordinary trade flow) at 5/10/15m?

## Scope (to lock at registration)
- Venue family: [U] — provisional reference expected same family as DATA-PROV-001 (e.g. Binance USD-M) until Archivist assigns; **not** a venue marriage
- Instruments: BTCUSDT, ETHUSDT perpetual (separate series)
- Event streams (may be sub-series under one DATA_ID or sibling IDs):
  1. Liquidations (actual venue liquidation events — **not** inferred from wicks)
  2. Open interest (snapshots or updates with honest timestamps)
  3. Funding (settled prints with settlement timestamps)
- Target calendar: align to OHLCV/trades coverage where practical; document shortfalls

## Required fields (raw) — by stream

### Liquidations
- exchange event timestamp (and receive timestamp if distinct)
- symbol / instrument
- side (long liq vs short liq)
- price, quantity / notional
- venue event ID (if any)
- source endpoint / feed name

### Open interest
- timestamp of OI observation (exchange time)
- OI level (contracts or coin — units explicit)
- symbol / instrument
- source; revision policy (restated vs first-print)

### Funding
- **settlement** timestamp (knowability anchor)
- funding rate value for that settled interval
- symbol / instrument
- next-settlement time only as metadata — **never** use unsettled/future rate at decision t
- source; convention notes (venue-specific)

## Knowability (Clock will grade)
| Feature class | Knowable at decision t only if… |
|---------------|----------------------------------|
| Liquidation burst ending at t | All liq prints in window have event time ≤ t; no mid-print fantasy |
| OI level / shock at t | OI print timestamp ≤ t; no revised-after-t restatement without quarantine |
| Funding extreme | Latest **settled** funding with settlement time ≤ t; **no future funding leak** |
| Deceleration / aggression gates | Trade or bar features knowable at t (reuse TRADES/OHLCV lineage; do not invent) |

## Timestamp semantics (must declare on card)
- Exchange **event time** vs ingest/receive time
- Bar alignment rule to 5m closes (inclusive/exclusive)
- Funding: settlement boundary vs “current predicted funding” (latter forbidden for SIGNAL)
- Liquidation: actual force-close events vs mark-price triggers — state which
- Clock / bar alignment to DATA-PROV-001 and DATA-PROV-TRADES-001 when joining

## Hard rules
- Distinct DATA-* family — **do not** merge into OHLCV or trades datasets
- Preserve raw immutably; hash; full provenance (venue, path, fetch time when fetched)
- No silent gap/duplicate repair; no inferred liquidations labeled as actual
- No future funding in features; no look-ahead OI restatements
- Seal policy for research / validation / holdout after Clock sees coverage (prefer calendar align to existing SEAL_LOCK where timestamps allow)
- Primary cell pre-register before RESEARCH TEST; horizons separate; redundancy controls mandatory

## Clock audit checklist (first registration)
event-time vs receive-time · ordering · duplicate/missing IDs · venue/source identity · funding settlement knowability (no leak) · OI revision policy · liquidation = actual events · alignment to 5m bars · join integrity to OHLCV/trades · holdout seal proposal · safe vs unsafe feature list

## Intended EDGE support (non-binding until Clock VERDICT)
- EDGE-20260910-009 (liq burst / decelerate) — needs liquidations + price/aggression
- EDGE-20260910-010 (funding × OI) — needs settled funding + OI
- Future atomic cards for OI shocks / funding-only controls / crowded unwind

## Forbidden until VERDICT
- Examiner RESEARCH TEST on Catalyst claims
- Capital / L2 escalation justified by unregistered Catalyst series
- Silent rewrite of EDGE-009/010 to match incomplete columns

## Registration handoff
1. Catalyst + data steward fill dataset card (`archive/templates/DATASET.md`) from this stub  
2. Archivist assigns DATA_ID / files under `archive/datasets/`  
3. Clock issues DATA VERDICT (APPROVED / CONDITIONAL / QUARANTINED / REJECTED)  
4. Conductor may then route Examiner  

*Provisional stub — no market data fetched under this spec alone.*
