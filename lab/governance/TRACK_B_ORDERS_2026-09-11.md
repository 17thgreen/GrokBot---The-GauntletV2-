# TRACK B ORDERS — Prediction-market data + measurement
**Document:** `TRACK_B_ORDERS_2026-09-11.md`  
**Authority:** Logan M (Human Governor)  
**Date (UTC):** 2026-09-11  
**Classification:** RESEARCH / DATA ORDERS (domain measurement standup)  
**RETROACTIVE:** **NO**  
**Baseline:** `gauntlet-v2.0-alpha` **unchanged**  
**Predecessor:** Cycle 5 close Outcome B (`CYCLE_5_CLOSE_2026-09-11.md`)  
**Does not:** fetch market data · place trades · open a full cockpit · invent a new science family · rewrite cemetery / Edge Cards · start Examiner on empty contract sample

---

## 1. Primary objective

**Build data and measurement sufficient to determine whether Gauntlet can estimate the resolution probability of actual BTC/ETH binary contracts better than the market.**

| Element | Binding |
|---------|---------|
| **Target** | \(P(\text{contract resolves YES} \mid \mathcal{I}_t)\) at decision time \(t\) |
| **Benchmark** | Venue market implied probability \(m_t\) at the **same** \(t\) — not 50/50, not an in-sample fitted null |
| **Ground truth** | Official contract **resolution** under venue rules + settlement source — not narrative, not LLM consensus |
| **Success** | Honest Δ vs market on proper scores in pre-registered cells — **or** honest UNTESTED / cemetery when not |
| **Non-goal (this track open)** | Auto real-money; full cockpit UI; rescue of Cycle 5 Funding/OI futures cells; L2 book spend |

Forecast ≠ trade. A calibrated forecast that beats \(m_t\) does **not** authorize orders. Mechanic / Treasurer / Canary remain non-waivable for any capital path (`PREDICTION_MARKET_MISSION_2026-09-11.md`).

This is **data + measurement infrastructure**, not a new researcher caste.

---

## 2. Sequence (mandatory order)

Do not skip stages. Do not Examiner-peek before the sample exists. **No market-data fetch under this commission** — schemas, registries, and harness spec only until a later Governor/Conductor fetch order.

```
DATA
  → CONTRACT REGISTRY
  → ORACLE
  → HISTORICAL PRICE STATE
  → BINARY EXAMINER
  → MARKET BASELINE
  → STRATEGY LEAGUE
  → FORWARD SHADOW
  → COCKPIT
```

| Stage | Done when | Not done when |
|-------|-----------|---------------|
| **DATA** | Distinct DATA-* family(ies) for L1 PM prints / metadata **and** L2 oracle/resolution inputs registered; Clock path named; raw immutable + hash policy stated | Silent scrape; merging PM ticks into DATA-PROV-001 / TRADES / FUNDING / OI |
| **CONTRACT REGISTRY** | Archivist-assigned `CONTRACT-YYYYMMDD-NNN` rows exist for the working universe; each binds `BINARY_CONTRACT` fields (rules, settlement source, status) | Ad-hoc ticker lists; title-only “markets” without rules hash / native ID |
| **ORACLE** | Resolution source, rules URI/hash, void/dispute policy Clock-gradable per contract | Invented resolutions; LLM-as-oracle |
| **HISTORICAL PRICE STATE** | For each registered **resolved** contract: \(m_t\) at declared checkpoints, knowable-at-t, no look-ahead | Last-price-only vibes; post-resolution prints used as \(m_t\) |
| **BINARY EXAMINER** | Harness implements `BINARY_EXAMINER_SPEC.md`; missing metrics = `UNTESTED` | Futures Examiner reused as if it scored binaries; fabricated Brier/logloss |
| **MARKET BASELINE** | Same windows, same \(t\), same contracts: market Brier / logloss / calibration as the **default** benchmark | Coin-flip or always-0.5 dressed as skill |
| **STRATEGY LEAGUE** | Strategies in `HYPOTHESIS`/`RESEARCH` with frozen forecast spec + pre-registered tournament cell (`STRATEGY_LEAGUE.md`) | Champion by narrative; ensemble peeking |
| **FORWARD SHADOW** | After historical gates: sealed forward window / paper shadow; Canary path named | Live capital; cockpit “executable” labels without Mechanic |
| **COCKPIT** | Decision-support display of \(p_t\), \(m_t\), net edge, abstention — **later** | **Not this open.** No full cockpit yet (§5) |

Clock grades knowability at DATA / ORACLE / PRICE STATE. Examiner measures only after Clock VERDICT + Conductor RESEARCH TEST route (`ROUTING.md`).

---

## 3. Venues (adapters — not altars)

Per `AMD-20260911-PM-002` and `US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md` (**RETROACTIVE: NO**):

| Rank | Adapter ID | Track B role |
|------|------------|--------------|
| **CO-PRIMARY** | **`KALSHI`** | US-lab planning / historical contract capture / eventual capital planning. Discovery: live 15m BTC/ETH Up-Down; no 5m/10m series at discovery `[V]` |
| **CO-PRIMARY** | **`POLYMARKET_GLOBAL`** | Co-primary with Kalshi for short crypto (5m/15m BTC/ETH Up/Down) **as if US-usable** `[A]` Governor planning assumption. Discovery fact that US trade on Global **may be blocked** is **retained** — planning ≠ verified access law `[U]` counsel |
| **WATCHLIST** | **`POLYMARKET_US`** | Native US product watchlist. Not co-primary. No short-crypto Up/Down inventory at discovery `[V]` |

Rules:

- No strategy hard-assumes a single venue as “the market” without adapter ID + fee/liquidity assumptions.
- Cross-venue claims need equivalent contract semantics (or explicit mapping) + constitutional cross-venue discipline.
- Binance / fapi / Vision remain **Layer-3 predictor data only** — never a PM execution venue.
- New adapters beyond this set: registered DATA-* + Clock + Archivist index.
- **Not legal advice.**

Universe for first sample: **actual BTC/ETH binary contracts** (Up/Down or equivalent binary slices). Map multi-outcome venues to explicit binary slices or reject.

---

## 4. First milestone (the only near-term done-when)

**A clean historical sample of resolved contracts**, each with:

1. **Rules** (URI + content hash when frozen)  
2. **Settlement / resolution source** (official oracle / venue resolver — Clock-gradable)  
3. **Market prices at checkpoints** (\(m_t\) at pre-declared decision timestamps; construction rule explicit: mid / microprice / last)  
4. **Final resolution** (`YES` / `NO` / `VOID` + evidence pointer, tagged `[V]` or quarantine)

| Completeness | Requirement |
|--------------|-------------|
| Identity | `CONTRACT_ID` + `VENUE_ADAPTER` + `VENUE_NATIVE_ID` |
| Semantics | Binary YES/NO (or explicit slice); title/question verbatim from venue where possible |
| Timeline | OPEN / CLOSE (trade cutoff) / RESOLVE — UTC; event vs receive time declared |
| Integrity | No look-ahead in checkpoint prices; disputed/void → `QUARANTINED` / `[U]`, not invented |
| Registry | Rows in the contract registry (template `archive/templates/CONTRACT_REGISTRY.md`); per-contract body `BINARY_CONTRACT.md` |
| Honesty | Untested metrics stay `UNTESTED`. No fabricated fills, fees, Sharpes, or live P&L |

**Not** the first milestone: Strategy League Champion, cockpit, forward shadow, Feature Card library, L3 model zoo.

Do **not** fetch venue data to populate the sample under **this** commission. Spec + empty registry + Examiner metric list only.

---

## 5. Hard locks (Track B open)

| Lock | Binding |
|------|---------|
| **No full cockpit yet** | Cockpit is last in the sequence. Decision-support UI is **not** commissioned now. No auto real-money ever under current mission |
| **No new science family** | Do **not** create a fourth researcher caste (no “PM Reader” / “Oracle Scientist” org). Track B uses existing lattice: Clock, Examiner, Prosecutor, Mechanic, Treasurer, Canary, Archivist, Conductor, Governor. Feature Cards + Strategy League are the artifacts — not a new priesthood |
| **Feature Cards required to reuse dead Edges** | Cemetery Edges (OHLCV, Tape, Funding/OI, kin) are **not** resurrected as trade theses. If a killed SIGNAL is reused as a **forecast input** to \(p_t\), file a **Feature Card** (`archive/templates/FEATURE.md`) that **cites** the CEM / TEST / EDGE ids, states knowability, and ablates vs \(m_t\). No silent Edge rewrite. No parameter retune of EDGE-20260911-004/005/006 |
| **No Cycle 5 retune** | Outcome B stands. Track B is not a back door to re-grid funding/OI futures cells |
| **No L2 book spend** | EDGE-20260910-005/006 remain blocked; Track B does not unlock Tardis |
| **LIQ forward** | Continues **passive** (Cycle 5 close §5). Not a Track B blocker |
| **RETROACTIVE** | **NO** |

---

## 6. Dual hypotheses (Track B)

| Track | Question |
|-------|----------|
| **Market** | Can Gauntlet beat venue \(m_t\) on resolution of actual BTC/ETH binaries (proper scores, costs, abstention) in pre-registered cells? |
| **Institutional** | Can the lab stand up contract-level ground truth, Clock-honest checkpoints, and an Examiner that reports UNTESTED instead of theater — without cockpit, without a new science family, without rewriting cemetery? |

---

## 7. Routing (gated)

```
DATA-* registration (adapters + oracle feeds)
        → Archivist CONTRACT registry + pretest against cemetery if Feature/Edge reuse
        → Clock DATA VERDICT (knowability, revision, checkpoint honesty)
        → Conductor routes Binary Examiner (RESEARCH TEST) only after CLEAR/WARN-ack + VERDICT
        → MARKET BASELINE scored on the same cell
        → Strategy League states update from evidence (not narrative)
```

Default: no whole-team chat (`ROUTING.md`). Hard authorities non-waivable.

Researchers may propose Feature Cards / Strategies **after** the first-milestone sample exists and Clock has a path — not before DATA/REGISTRY/ORACLE/PRICE STATE.

---

## 8. Attention lock

| Bucket | Items |
|--------|-------|
| **PRIMARY** | Track B sequence through **first milestone** (resolved-contract sample: rules, settlement source, checkpoint \(m_t\), resolution) |
| **NEXT (not now)** | Binary Examiner implementation against that sample; market baseline; league HYPOTHESIS rows |
| **LATER** | Forward shadow · cockpit v0 decision support |
| **PASSIVE** | LIQ forward capture |
| **DARK / NO RESCUE** | Cycle 5 Funding/OI retune; Tape/OHLCV cemetery revival via Edge rewrite |
| **WATCHLIST** | `POLYMARKET_US` native product |

---

## 9. Pointers

| Doc | Role |
|-----|------|
| `CYCLE_5_CLOSE_2026-09-11.md` | Outcome B; FAIL-INSUFFICIENT interpretation; LIQ passive |
| `PREDICTION_MARKET_MISSION_2026-09-11.md` | Domain objective, L1/L2/L3, forecast≠trade |
| `AMD-20260911-PM-001.md` | Domain expansion; RETROACTIVE NO |
| `AMD-20260911-PM-002.md` | KALSHI + POLYMARKET_GLOBAL co-primary |
| `US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md` | Operator constraint; not legal advice |
| `VENUE_DISCOVERY_2026-09-11.md` | Read-only product inventory |
| `BINARY_EXAMINER_SPEC.md` | Required metrics; missing = UNTESTED |
| `archive/templates/BINARY_CONTRACT.md` | Per-contract ground truth (do not duplicate as CONTRACT.md) |
| `archive/templates/CONTRACT_REGISTRY.md` | Universe / sample ledger |
| `archive/templates/FEATURE.md` | Required path to reuse dead Edges as forecast inputs |
| `archive/templates/STRATEGY_LEAGUE.md` | League states and metric snapshot |

---

*End Track B orders — 2026-09-11. Data+measurement first. No fetch in this commission. No full cockpit. No new science family. RETROACTIVE: NO. Baseline `gauntlet-v2.0-alpha` unchanged.*
