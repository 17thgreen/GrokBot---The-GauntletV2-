
## Constitutional promotion path (amended 2026-09-10)

HYPOTHESIS → RESEARCH TEST → VALIDATION → **HISTORICAL SEALED HOLDOUT** → **CROSS-VENUE REPLICATION** → **FORWARD SHADOW** → PAPER → MICRO → LIMITED → PRODUCTION

Source: `governance/CONSTITUTIONAL_AMENDMENT_FORWARD_AND_CROSS_VENUE.md`. Historical holdout ≠ production proof.

# Master Index

Cycle 0 — archive stood up 2026-09-10 UTC. First intake: Statistician STAT batch.

**Artifact lock:** Universal competitive unit = Atomic Edge Card only (`governance/EDGE_CARD.md`). Essays refused as pipeline substitute.

## Counts

| Registry | Count |
|----------|------:|
| Edges | 12 |
| Strategies | 0 |
| Tests | 3 |
| Cemetery | 3 |
| Deployments | 0 |
| Datasets | 2 |
| Red Team findings | 0 |
| Overrides | 0 |

## Informal ↔ canonical map

| Informal | EDGE_ID | Title | Role | Status | Pre-test |
|----------|---------|-------|------|--------|----------|
| STAT_003A | EDGE-20260910-001 | Low-RV continuation | PRIMARY | **REJECTED** | FAIL TEST-20260910-001 |
| STAT_001 | EDGE-20260910-002 | Quiet-bar continuation | RESERVE | HYPOTHESIS_RESERVE | WARN_RELATED |
| STAT_002 | EDGE-20260910-003 | Range-expansion snapback | Cycle 2 | **REJECTED** | FAIL TEST-20260910-002 (cites CEM-001) |
| STAT_004 | EDGE-20260910-004 | BTC lead → ETH response | Cycle 3 | **REJECTED** | FAIL TEST-20260910-003 (cites CEM-001+002) |
| PROVISIONAL-TR-C1-01 | EDGE-20260910-005 | Aggressor burst replenishment fade | Cycle1 Tape | HYPOTHESIS | CLEAR_TO_TEST |
| PROVISIONAL-TR-C1-02 | EDGE-20260910-006 | Transient spread blowout snap-back | Cycle1 Tape | HYPOTHESIS | CLEAR_TO_TEST |
| A-NOT-LOWRV / CART_A_NOT_LOWRV | EDGE-20260910-007 | Outside Low-RV abstain | Cartographer companion | **REJECTED_WITH_PARENT** | WARN_RELATED |
| A-LOWRV-CHOP / CART_A_LOWRV_CHOP | EDGE-20260910-008 | Low-RV chop abstain | Cartographer companion | **REJECTED_WITH_PARENT** | WARN_RELATED |
| CAT_LIQ_EXHAUST | EDGE-20260910-009 | Liq burst deceleration fade | Cycle1 Catalyst | HYPOTHESIS | CLEAR_TO_TEST |
| CAT_FUND_OI_CROWD | EDGE-20260910-010 | Funding×OI against crowd | Cycle1 Catalyst | HYPOTHESIS | CLEAR_TO_TEST |



## Cycle 1 Cartographer companions

- EDGE-20260910-007 (A-NOT-LOWRV) WARN_RELATED → parent EDGE-20260910-001
- EDGE-20260910-008 (A-LOWRV-CHOP) WARN_RELATED → parent EDGE-20260910-001
- Filed as NEW EDGEs (Conductor), not annexes

## Cycle 1 Catalyst filings

- EDGE-20260910-009 (CAT_LIQ_EXHAUST) CLEAR_TO_TEST
- EDGE-20260910-010 (CAT_FUND_OI_CROWD) CLEAR_TO_TEST

## Cycle 1 Tape Reader filings

- EDGE-20260910-005 / EDGE-20260910-006 filed HYPOTHESIS (microstructure). Not Cycle 0 primary attention unless Conductor expands.
- Still distinct from EDGE-20260910-001 per mechanism contrast [I/V search].




## Datasets

| DATA_ID | Status | Series | Notes |
|---------|--------|--------|-------|
| DATA-PROV-001 | **CLOCK_CONDITIONAL** | Binance USD-M BTC/ETH 5m; raw 2021-01-01→2026-08-31 UTC; 595872×2; 0 gaps | Clock CONDITIONAL / APPROVED_WITH_LIMITATIONS. Limitations on datasets/DATA-PROV-001.md. Examiner CLEARED provisional RESEARCH for EDGE-001. Holdout LOCKED. Expect TEST-* intake.|

### DATA-PROV-001 slice spans (dates only)

| Slice | Span UTC |
|-------|----------|
| Research | 2021-01-03 → 2024-05-27 |
| Validation | 2024-05-27 → 2025-07-14 |
| Historical holdout | 2025-07-14 → 2026-08-31 **LOCKED** |


## Provisional harness registry

| Package ID | Path | Target | Ceiling | DATA attachment |
|------------|------|--------|---------|-----------------|
| PROV-MEAS-20260910-001 | `/workspace/lab/harness/provisional/PROVISIONAL_MEASUREMENT_PACKAGE_EDGE-20260910-001.md` | EDGE-20260910-001 (+007/008 overlays) | Provisional validation only | DATA-PROV-001 **CLOCK_CONDITIONAL** — Examiner CLEARED provisional RESEARCH for 001; holdout LOCKED; limitations on DATA record |

**[V]** Cost sensitivity on 001 → provisional [A] C_base=7.0 bps RT. No RESEARCH TEST until Clock-approved DATA-PROV.




## Cycle 4 attention lock (Conductor)

| Priority | Item | Note |
|----------|------|------|
| **PRIMARY** | Staged Tape | EDGE-20260911-001/002 HYPOTHESIS CLEAR; primary cells locked; **DATA CLOCK_REVIEW**; TEST held for Clock + Conductor; 005/006 L2-blocked |
| DATA | DATA-PROV-TRADES-001 | **CLOCK_REVIEW** — 2069+2069 aggTrade zips; Examiner blocked until Clock |
| FROZEN | EDGE-20260910-005, EDGE-20260910-006 | **DATA-BLOCKED / UNMEASURABLE WITHOUT L2** — no proxy rewrite |
| Cycle 5 | EDGE-20260910-009, EDGE-20260910-010 | Event edges deferred |
| STAND-DOWN | Statistician OHLCV clones | MEASUREMENT_STANDDOWN_OHLCV remains (001/003/004 cemetery; 002 dark) |


### Cycle 4 trade-flow edges (new)

| Informal | EDGE_ID | Title | Role | Status | Pre-test |
|----------|---------|-------|------|--------|----------|
| TR_FLOW_CNT_01 | EDGE-20260911-001 | Trade-count aggressor imbalance residual | Cycle4 Tape | HYPOTHESIS | CLEAR_TO_TEST |
| TR_FLOW_LRG_01 | EDGE-20260911-002 | Large-trade clustering + persistence | Cycle4 Tape | HYPOTHESIS | CLEAR_TO_TEST |

## MEASUREMENT_STANDDOWN_OHLCV (Conductor) [OHLCV clones still stand down]

**MEASUREMENT_STANDDOWN_OHLCV** until Logan picks Cycle 4 (L2 / event feeds / new orthogonal / retrospective) or new `DATA-*` (L2 for EDGE-005/006 or event feeds for EDGE-009/010) **or** new orthogonal HYPOTHESIS commission.

| Status | EDGE_IDs | Note |
|--------|----------|------|
| Cemetery | 001 → CEM-001 NO_EDGE; 003 → CEM-002 COST_KILLED; 004 → CEM-003 NO_EDGE | OHLCV-native Statistician queue exhausted |
| Dark | 002 | not rescue |
| REJECTED_WITH_PARENT | 007, 008 | parent 001 dead |
| DATA-BLOCKED | 005, 006, 009, 010 | need L2 / event feeds |
| No active PRIMARY | — | stand-down |


## Cycle 3 attention lock (Conductor) [superseded — STAND-DOWN]

| Priority | EDGE_IDs | Role |
|----------|----------|------|
| **PRIMARY next** | — | **STAND-DOWN** — no active measurement target |
| CLOSED | EDGE-20260910-001 | CEM-20260910-001 ↔ TEST-20260910-001 (NO_EDGE) |
| CLOSED | EDGE-20260910-003 | CEM-20260910-002 ↔ TEST-20260910-002 (COST_KILLED) |
| CLOSED | EDGE-20260910-007, EDGE-20260910-008 | REJECTED_WITH_PARENT |
| Dark | EDGE-20260910-002 | not rescue |
| DATA-BLOCKED | EDGE-20260910-005, EDGE-20260910-006, EDGE-20260910-009, EDGE-20260910-010 | need non-OHLCV / event feeds |


## Cycle 2 attention lock (Conductor) [superseded by Cycle 3]

| Priority | EDGE_IDs | Role |
|----------|----------|------|
| **PRIMARY next** | EDGE-20260910-003 | **CLOSED FAIL** — TEST-20260910-002 / CEM-20260910-002 (COST_KILLED); cites CEM-001 |
| CLOSED | EDGE-20260910-001 | CEM-20260910-001 ↔ TEST-20260910-001 (NO_EDGE) |
| CLOSED | EDGE-20260910-007, EDGE-20260910-008 | REJECTED_WITH_PARENT |
| Dark | EDGE-20260910-002 | WARN_RELATED cousin — **not** rescue |
| DATA-BLOCKED | EDGE-20260910-005, EDGE-20260910-006, EDGE-20260910-009, EDGE-20260910-010 | Need non-OHLCV / event feeds beyond DATA-PROV-001 |
| RESERVE | EDGE-20260910-004 | BTC→ETH lagged response — inactive |

**[V]** CEM↔TEST link confirmed: `CEM-20260910-001` ↔ `TEST-20260910-001` ↔ `EDGE-20260910-001`.
No RESEARCH TEST on 003 until Conductor + Clock/package gates for that edge are explicit.

## Cycle 1 wave closed — attention lock (Conductor) [superseded by Cycle 2]

Registry: **10 edges**. No RESEARCH TEST until data/venue/costs/holdout.

| Priority | EDGE_IDs | Role |
|----------|----------|------|
| First measurement | EDGE-20260910-001 | **CLOSED FAIL** — TEST-20260910-001 / CEM-20260910-001 (NO_EDGE); holdout sealed |
| Abstention overlays (with 001 only) | EDGE-20260910-007, EDGE-20260910-008 | Not separate alpha hunt |
| Microstructure queue (later) | EDGE-20260910-005, EDGE-20260910-006 | Stand by |
| Event queue (later) | EDGE-20260910-009, EDGE-20260910-010 | Stand by |
| Dark | EDGE-20260910-002, EDGE-20260910-003, EDGE-20260910-004 | Inactive reserves — **002 not rescue** after CEM-20260910-001 |

Researchers stand by unless commissioned.

## Cycle 0 attention lock (Conductor + Statistician ack)

- **PRIMARY only:** EDGE-20260910-001 — active research attention
- **RESERVE (do not activate Cycle 0):** EDGE-20260910-002 / 003 / 004
- Informal `STAT_*` dropped in future Conductor/Examiner traffic — **EDGE-* only**
- RESEARCH TEST still blocked lab-wide until data/venue/costs/holdout locks

## Edges

| EDGE_ID | Title | Originator | Status |
|---------|-------|------------|--------|
| EDGE-20260910-001 | Low-RV continuation | Statistician | **REJECTED** (TEST-20260910-001 / CEM-20260910-001 NO_EDGE) |
| EDGE-20260910-002 | Quiet-bar continuation | Statistician | HYPOTHESIS_RESERVE |
| EDGE-20260910-003 | Range-expansion snapback | Statistician | **REJECTED** (TEST-20260910-002 / CEM-20260910-002 COST_KILLED) |
| EDGE-20260910-004 | BTC lead → ETH response | Statistician | **REJECTED** (TEST-20260910-003 / CEM-20260910-003 NO_EDGE) |
| EDGE-20260910-005 | Aggressor burst replenishment fade | Tape Reader | **DATA-BLOCKED / UNMEASURABLE WITHOUT L2** |
| EDGE-20260910-006 | Transient spread blowout snap-back | Tape Reader | **DATA-BLOCKED / UNMEASURABLE WITHOUT L2** |
| EDGE-20260910-007 | Abstain outside Low-RV habitat (companion to 001) | Cartographer | **REJECTED_WITH_PARENT** |
| EDGE-20260910-008 | Abstain Low-RV chop / poor path efficiency (companion to 001) | Cartographer | **REJECTED_WITH_PARENT** |
| EDGE-20260910-009 | Post-liquidation burst + deceleration fade | Catalyst | HYPOTHESIS |
| EDGE-20260910-010 | Funding extreme × elevated OI against crowded side | Catalyst | HYPOTHESIS |
| EDGE-20260911-001 | Trade-count aggressor imbalance residual | Tape Reader | HYPOTHESIS |
| EDGE-20260911-002 | Large-trade clustering + persistence | Tape Reader | HYPOTHESIS |


## Strategies

_None._

## Active / live deployments

_None._

## Cemetery (by failure class)

_None._

## Open pre-test searches

| QUERY_ID | EDGE_ID | Informal | Verdict |
|----------|---------|----------|---------|
| QUERY-20260910-001 | EDGE-20260910-001 | STAT_003A | CLEAR_TO_TEST |
| QUERY-20260910-002 | EDGE-20260910-002 | STAT_001 | WARN_RELATED |
| QUERY-20260910-003 | EDGE-20260910-003 | STAT_002 | CLEAR_TO_TEST |
| QUERY-20260910-004 | EDGE-20260910-004 | STAT_004 | CLEAR_TO_TEST |
| QUERY-20260910-005 | EDGE-20260910-005 | PROVISIONAL-TR-C1-01 | CLEAR_TO_TEST |
| QUERY-20260910-006 | EDGE-20260910-006 | PROVISIONAL-TR-C1-02 | CLEAR_TO_TEST |
| QUERY-20260910-007 | EDGE-20260910-007 | A-NOT-LOWRV | WARN_RELATED |
| QUERY-20260910-008 | EDGE-20260910-008 | A-LOWRV-CHOP | WARN_RELATED |
| QUERY-20260910-009 | EDGE-20260910-009 | CAT_LIQ_EXHAUST | CLEAR_TO_TEST |
| QUERY-20260910-010 | EDGE-20260910-010 | CAT_FUND_OI_CROWD | CLEAR_TO_TEST |

## Pending intake (informal → EDGE)

_None — STAT_003 lineage closed as STAT_003A → EDGE-20260910-001._

## Research-test gate

**Blocked lab-wide [U]:** market-data path, venue, cost model, sealed holdout.
Duplicate gate may be CLEAR/WARN; RESEARCH TEST still requires Conductor route after those locks + Archivist report in `audit/`.

## How to use

1. File or request intake → Archivist assigns ID + indexes here.
2. Before RESEARCH TEST → Archivist runs duplicate/semantic search → writes report under `audit/`.
3. On rejection → cemetery entry + INDEX update + failure class.
4. On promotion/demotion → deployment record + INDEX stage update.
