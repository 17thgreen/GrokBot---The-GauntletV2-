# DOMAIN ALIGNMENT DIRECTIVE — Prediction Market Mission
**Document:** `PREDICTION_MARKET_MISSION_2026-09-11.md`  
**Authority:** Logan M (Human Governor)  
**Date (UTC):** 2026-09-11  
**Classification:** **DOMAIN OBJECTIVE EXPANSION**  
**Not:** a retroactive strategy rule change; **not** a rewrite of the institutional freeze  
**Baseline (unchanged):** `gauntlet-v2.0-alpha` — see `BASELINE_gauntlet-v2.0-alpha.md` and `INSTITUTIONAL_LOCK_2026-09-11.md`  
**Change control:** `AMENDMENT_RULE.md` · stub `AMD-20260911-PM-001` (`RETROACTIVE: NO`)  
**Status:** GOVERNOR-ISSUED MISSION · operable going forward only

---

## 0. Classification & immutability of baseline

| Claim | Binding |
|-------|---------|
| **What this is** | Expansion of the lab’s **primary domain objective** to prediction-market **contract resolution probability** vs venue market price |
| **What this is not** | Retroactive amendment of strategy gates, cemetery verdicts, Edge Card bodies, Clock seals, or Examiner outputs already filed under `gauntlet-v2.0-alpha` |
| **Baseline tag** | `gauntlet-v2.0-alpha` remains the **unchanged institutional baseline**. Do not move, recreate, or silently reinterpret that tag |
| **INSTITUTIONAL_LOCK / AUTHORITY / BASELINE bodies** | **Unmodified** by this directive (optional one-line pointer footers only if Archivist later indexes). Operable detail lives **here** + companion templates |
| **Retroactivity** | **`NO`**. Past tests, kills, promotions, and seals stand under the rules then in force |
| **BTC/ETH Cycle work** | Continues under existing cycle orders; Cycle 5 Catalyst proceeds (see §11) |

Institutional doctrine (six lines, hard vetoes, gated routing, evidence tags) **still binds**. This file adds a **domain objective** and companion artifacts — it does not waive Clock / Examiner / Prosecutor / Mechanic / Treasurer / Canary.

---

## 1. New primary mission

**Primary mission (going forward):** Produce **calibrated, decision-time-honest forecasts** of **binary contract resolution** that beat the **venue market’s implied probability** on a risk- and cost-aware basis — then (only later, under Treasurer + Canary) consider whether any **trade** of that edge is executable.

| Element | Definition |
|---------|------------|
| **Target** | \(P(\text{contract resolves YES} \mid \mathcal{I}_t)\) at decision time \(t\) |
| **Benchmark** | Venue **market mid / last trade / best available implied probability** at the same \(t\) (see §14) |
| **Ground truth** | **Contract resolution outcome** as defined by the venue’s official rules + resolution source — not narrative, not LLM consensus |
| **Success unit** | Forecast quality **and** market-relative edge — not essay quality, not multi-agent agreement |
| **Non-goal (near term)** | Auto real-money deployment; venue scraping theater; rewriting BTC/ETH Edge Cards to “fit” PM |

Secondary (unchanged): institution-learning — whether asymmetric authority, seals, cemetery, and evidence discipline still function when the **domain** expands.

---

## 2. Contract as ground truth · venue adapter abstraction

### 2.1 Contract is ground truth

- The **BINARY_CONTRACT** record is the unit of truth for resolution, rules, cutoffs, and payout semantics.
- Forecasts, features, and strategies **must** bind to a specific `CONTRACT_ID` (or explicit basket with per-contract scoring).
- Disputes, ambiguous rules, or unresolved markets → mark `[U]` / QUARANTINE; do not invent resolution.

### 2.2 Venue adapter abstraction (not hard-primary)

Venues are **adapters**, not hard-coded primaries.

| Adapter ID | Role |
|------------|------|
| `POLYMARKET_US` | Polymarket (US-accessible surface as configured) — **adapter**, not institutional primary |
| `KALSHI` | Kalshi — **adapter**, not institutional primary |
| `(future)` | Additional adapters only via registered dataset + Clock verdict + Archivist index |

**Rules:**

- No strategy may hard-assume a single venue as “the market” without stating adapter ID and liquidity/fee assumptions.
- Cross-venue claims require **equivalent contract semantics** (or explicit mapping) and remain subject to constitutional cross-venue discipline where applicable.
- Provisional reference venue ≠ venue marriage (same spirit as crypto progression).
- **Do not fetch venue data under this commission** — schemas and mission only.

---

## 3. BINARY_CONTRACT schema (summary)

Blank operable template: `archive/templates/BINARY_CONTRACT.md`.

| Field | Required | Meaning |
|-------|----------|---------|
| `CONTRACT_ID` | YES | Archivist-assigned |
| `VENUE_ADAPTER` | YES | e.g. `POLYMARKET_US` \| `KALSHI` \| … |
| `VENUE_NATIVE_ID` | YES | Venue’s own market/contract identifier |
| `TITLE` / `QUESTION` | YES | Human-readable question text (verbatim from venue where possible) |
| `OUTCOMES` | YES | Binary: `YES` / `NO` (map multi-outcome venues to explicit binary slices or reject) |
| `RULES_URI` / `RULES_HASH` | YES | Resolution rules pointer + content hash when frozen |
| `RESOLUTION_SOURCE` | YES | Official resolver / oracle / venue resolution mechanism |
| `OPEN_TIME` / `CLOSE_TIME` / `RESOLVE_TIME` | YES | UTC; distinguish trade cutoff vs resolution time |
| `STATUS` | YES | `OPEN` \| `CLOSED` \| `RESOLVED` \| `VOID` \| `DISPUTED` \| `QUARANTINED` |
| `RESOLUTION` | WHEN DONE | `YES` \| `NO` \| `VOID` + evidence tag `[V]` + pointer |
| `TICK_SIZE` / `FEE_SCHEDULE_REF` | YES | Pricing grid + fee doc ref (tagged) |
| `LIQUIDITY_NOTES` | YES | `[V]`/`[I]`/`[H]` — depth, spreads; inventing depth forbidden |
| `KNOWABILITY` | YES | What is knowable at decision \(t\) (Clock grades) |
| `PROVENANCE` | YES | Registration agent, date UTC, DATA-* links |

---

## 4. Forecast vs trade separation · market-relative edge

### 4.1 Separation (mandatory)

| Track | Artifact | Question |
|-------|----------|----------|
| **Forecast** | Probability / distribution at \(t\) | Is \(p_t\) calibrated and informative vs market? |
| **Trade** | Position / order intent | Given \(p_t\), market \(m_t\), fees, and risk — **should** we trade? |

A strong forecast **does not** auto-authorize a trade. Mechanic + Treasurer + Canary remain non-waivable for any capital path. Cockpit is **decision support first** (§10).

### 4.2 Market-relative edge (canonical formula)

Let:

- \(p_t\) = model’s forecast \(P(\text{YES} \mid \mathcal{I}_t)\)
- \(m_t\) = venue implied probability of YES at decision time \(t\) (document mid vs microprice vs last; tag `[A]` if choice is conventional)
- \(c\) = round-trip cost in probability points (fees + half-spread + expected slippage), tagged `[V]`/`[I]`/`[H]`/`[U]`

**Gross edge (YES side):**

\[
e^{\text{gross}}_{\text{YES}}(t) = p_t - m_t
\]

**Net edge (YES side):**

\[
e^{\text{net}}_{\text{YES}}(t) = p_t - m_t - c_{\text{YES}}
\]

**Net edge (NO side)** uses \( (1-p_t) - (1-m_t) - c_{\text{NO}} \) equivalently \( m_t - p_t - c_{\text{NO}} \).

**Abstention:** if \( |p_t - m_t| \le c \) (or risk veto) → **NO TRADE** is first-class.

Report forecast metrics **even when** abstaining. Never invent fills or live P&L.

---

## 5. Strategy League Table

Blank operable template: `archive/templates/STRATEGY_LEAGUE.md`.

### 5.1 Fields (minimum)

| Field | Meaning |
|-------|---------|
| `STRATEGY_ID` | Archivist-assigned |
| `NAME` | Short label |
| `STATE` | League state (below) |
| `CONTRACT_SCOPE` | Single `CONTRACT_ID`, family, or explicit universe rule |
| `VENUE_ADAPTERS` | List; not hard-primary |
| `FORECAST_SPEC_REF` | Frozen forecast recipe / Feature Card set / model hash |
| `EDGE_CARD_REFS` | Linked Edge Cards (if any); Feature Cards companion (§9) |
| `DECISION_TIME_RULE` | When \(t\) is sampled; no look-ahead |
| `BENCHMARK_DEF` | How \(m_t\) is constructed |
| `COST_STACK_REF` | Fee/spread/slippage assumptions + tags |
| `METRICS_SNAPSHOT` | Required forecast metrics (§7) — or `UNTESTED` |
| `TOURNAMENT_CELL` | Pre-registered cell (horizon/cutoff/side/cost) |
| `MULTIPLE_TESTING_BUDGET` | Family-wise / holdout accounting pointer |
| `PROVENANCE` | Originator, date UTC, related TEST/CEM/AMD IDs |
| `PROMOTION_EVIDENCE` | Pointers only — no self-grade |

### 5.2 States

| State | Meaning |
|-------|---------|
| `HYPOTHESIS` | Claim filed; not yet measured under frozen spec |
| `RESEARCH` | Active RESEARCH TEST / measurement under Conductor route |
| `CHALLENGER` | Measured contender; not yet Champion; competing in league |
| `CHAMPION` | Current best **within a pre-registered cell** under explicit metrics — **revocable** |
| `INACTIVE` | Paused; not competing; not cemetery |
| `RETIRED` | Voluntarily or policy-retired; retained for memory |
| `CEMETERY` | Killed (Examiner FAIL / Prosecutor KILL / risk kill) — archive failure class |

**Rules:** Champion is **cell-local** and **evidence-gated**. Conductor cannot crown Champion by narrative. Cemetery entries are not rewritten by this domain expansion (`RETROACTIVE: NO`).

---

## 6. Tournament funnel · multiple-testing · decision-time · calibration · metrics

### 6.1 Tournament funnel

```
Idea / Feature Card
  → HYPOTHESIS Strategy (league)
  → Pre-registered tournament cell
  → RESEARCH measurement (Examiner)
  → CHALLENGER pool
  → Holdout / forward gates (constitutional hierarchy still applies in spirit)
  → CHAMPION (revocable)
  → Paper / shadow (no auto real-money)
  → Treasurer + Canary only if capital ever considered
```

Fail cheaply early. REDUNDANT / NO_EDGE / OVERFIT → cemetery or RETIRED with failure class.

### 6.2 Multiple-testing

- Pre-register cells **before** peeking at evaluation outcomes.
- Track family-wise error / holdout spend in Archivist memory.
- Re-using the same resolved contracts for endless re-tunes → treat as **OVERFIT** risk; Prosecutor may force fresh forward window.

### 6.3 Decision-time dimension

- Every forecast and every \(m_t\) must declare **decision timestamp \(t\)** and **information set \(\mathcal{I}_t\)**.
- Features unknowable at \(t\) are illegal (Clock veto).
- Resolution labels after \(t\) may grade forecasts but **must not** leak into \(\mathcal{I}_t\).

### 6.4 Calibration

- Report reliability diagrams / calibration slopes where sample allows; else mark sample limits `[U]`.
- Sharpness without calibration is incomplete; calibration without market-relative edge is incomplete.

### 6.5 Required forecast metrics (minimum set)

When a strategy leaves `HYPOTHESIS`, Examiner packages must report or explicitly mark `UNTESTED`:

| Metric | Role |
|--------|------|
| **Log loss (binary)** vs outcomes | Proper scoring |
| **Brier score** | Calibration + refinement |
| **Market log-loss / Brier baseline** | Same windows, same \(t\) |
| **Δ vs market** (model − market) on proper scores | Primary skill claim |
| **ECE / reliability summary** | Calibration |
| **Net edge distribution** \(e^{\text{net}}\) | Trade relevance (still not auto-trade) |
| **Coverage / abstention rate** | When model refuses |
| **Sample N, time span, contract count** | Honesty about power |
| **Cost stack sensitivity** | Fees/spread perturbation |

No fabricated Sharpes or live P&L. Untested = `UNTESTED`.

---

## 7. Three data layers

| Layer | Name | Contents | Clock duty |
|-------|------|----------|------------|
| **L1 — PM** | Prediction-market native | Contract metadata, order/trade prints, books if any, resolution events — via venue **adapters** | Knowability, revision policy, seal |
| **L2 — Oracle / resolution** | Official resolution inputs | Rules, resolver feeds, dispute timelines, void conditions | No silent restatement; hash frozen rules |
| **L3 — External predictors** | Non-venue features | News, polls, on-chain, macro, crypto microstructure exports, LLM features, etc. | Strict decision-time; leakage kills |

Cross-layer joins require explicit timestamps and DATA-* registration. Staged progression spirit (cheap → expensive data) still applies: do not buy exotic L3 before PM+oracle integrity exists for the claim.

---

## 8. Feature Cards (companion to Edge Cards)

Blank operable template: `archive/templates/FEATURE.md`.

Atomic **Edge Cards** remain the competition unit for **trade theses**. **Feature Cards** are the companion unit for **forecast inputs**:

| | Edge Card | Feature Card |
|---|-----------|--------------|
| Primary question | Is there a tradable edge? | Is this input knowable, honest, and predictive? |
| Binds to | Thesis / entry / exit / abstention | Feature definition / latency / leakage tests |
| May feed | Strategy League + Mechanic | Forecast specs + Ensemble |

Feature Cards do **not** replace Edge Cards. Do **not** rewrite existing Edge Cards under this directive.

---

## 9. Ensemble rules

1. **Base learners** expose \(p_t^{(k)}\) with frozen specs and Feature Card provenance.
2. **Ensemble** \(p_t = f(p_t^{(1)},\ldots,p_t^{(K)}, m_t)\) must itself be a **frozen Strategy** in the League (no silent weight fiddling after peeking).
3. Market \(m_t\) may be a feature — but “copy the market” is the **baseline**, not a Champion claim.
4. Stacking that consumes holdout labels → Prosecutor kill / OVERFIT class.
5. Ensemble promotion still requires Examiner measurement + constitutional gates before any capital path.

---

## 10. Cockpit · no auto real-money

| Rule | Binding |
|------|---------|
| **Cockpit role** | **Decision support first** — display forecasts, \(m_t\), net edge, calibration, abstention, risk flags |
| **Auto real-money** | **Forbidden** under this directive. No unsupervised order routers |
| **Paper / shadow** | Allowed only under explicit Conductor + Mechanic route and Treasurer policy |
| **Human Governor** | Capital overrides never silent; archive required |
| **Conductor** | Still may not deploy real capital or waive vetoes |

---

## 11. Cycle 5 continuity (explicit)

This domain expansion **does not** interrupt Cycle 5:

| Item | Status under this directive |
|------|----------------------------|
| **Catalyst Cycle 5** | **Proceeds** per `CYCLE_5_RESEARCH_ORDERS.md` |
| **Tape cemetery** | **Stands** — CEM-20260911-001 / 002 and kin; no rescue |
| **EDGE-20260910-005 / 006** | Remain **L2-blocked** / UNMEASURABLE WITHOUT L2; frozen |
| **OHLCV cemetery** | Stands; amendments do not rewrite prior verdicts |
| **Edge Card rewrites** | **Not authorized** by this file |

PM work is **additive** attention — not a license to abandon Catalyst measurement discipline.

---

## 12. Role deltas (summary)

Institutional roles **unchanged in veto power**. Domain deltas:

| Role | Delta (PM domain) |
|------|-------------------|
| **Clock** | Grade contract/rules knowability; resolution revision policy; decision-time for L1/L2/L3; quarantine disputed/void ambiguity; adapter timestamp honesty |
| **Examiner** | Measure required forecast metrics vs market baseline; enforce pre-registered cells; mark `UNTESTED` honestly; kill improper leakage |
| **Prosecutor** | Attack calibration cherry-picks, multiple-testing, venue-specific mirages, ensemble peeking, “forecast good ⇒ trade good” conflation |
| **Mechanic** | Separate executable trade path from forecast skill; fee/spread/latency on PM adapters; block non-executable paper alpha |
| **Treasurer** | No auto real-money; kill capital enthusiasm; size/limits if paper→micro ever proposed |
| **Canary** | Monitor forward forecast decay vs market; alert when Champion calibration or Δ-vs-market collapses; CONTINUE / DEMOTE / KILL recommendations |

Conductor allocates attention across BTC/ETH Cycle 5 **and** PM standup without waiving any hard authority.

---

## 13. Success definition · milestones 1–10

### 13.1 Success definition

**Success** = the lab can, under `gauntlet-v2.0-alpha` institutional rules:

1. Register binary contracts with honest resolution ground truth  
2. Produce decision-time forecasts with required metrics  
3. Show **positive Δ vs market** on proper scores in pre-registered cells — or honestly cemetery when not  
4. Keep forecast≠trade separation; cockpit decision-support only  
5. Preserve Cycle 5 / cemetery integrity (`RETROACTIVE: NO`)

Failure to beat the market after honest measurement is **successful institution-learning**, not a reason to fabricate edge.

### 13.2 Milestones

| # | Milestone | Done when |
|---|-----------|----------|
| 1 | Mission + schemas filed | This doc + `BINARY_CONTRACT` / `FEATURE` / `STRATEGY_LEAGUE` templates on disk |
| 2 | AMD stub indexed | `AMD-20260911-PM-001` as DOMAIN OBJECTIVE EXPANSION · `RETROACTIVE: NO` |
| 3 | First DATA-* family for PM adapter | Dataset card + Clock review path (no silent fetch mandate here) |
| 4 | First BINARY_CONTRACT registrations | ≥1 contract per intended adapter family or explicit single-adapter scope |
| 5 | Feature Card pipeline live | Companion cards linkable to forecast specs |
| 6 | League table instantiated | Strategies in `HYPOTHESIS`/`RESEARCH` with pre-registered cells |
| 7 | Examiner forecast harness | Required metrics vs market baseline runnable under frozen spec |
| 8 | First CHALLENGER measured | Honest PASS/FAIL or UNTESTED clearance — cemetery OK |
| 9 | Cockpit v0 decision support | Displays \(p_t\), \(m_t\), net edge, abstention — **no** auto real-money |
| 10 | Forward / Canary discipline | Champion (if any) under forward monitoring; decay → demote/kill path proven |

---

## 14. Doctrine addendum — market price is the benchmark

**Addendum (domain):** For prediction-market work, the **venue market implied probability at decision time** is the **default benchmark**. Beating a naive 50/50 or an in-sample fitted null is **not** sufficient to claim skill.

| Maxim | Operable meaning |
|-------|------------------|
| **Market price is the benchmark** | Report Δ vs \(m_t\) on proper scores; “we predicted well” without market comparison is incomplete |
| **Contract resolves truth** | Resolution outcome grades forecasts; vibes do not |
| **Forecast ≠ license to trade** | Edge formula informs; Mechanic/Treasurer/Canary govern action |
| **Adapters not altars** | `POLYMARKET_US` / `KALSHI` are interchangeable interfaces under schema — not hard-primary ideology |
| **Baseline tag stands** | `gauntlet-v2.0-alpha` unchanged; this is expansion, not freeze rewrite |

Core six lines in `DOCTRINE.md` remain binding. This addendum **extends** domain interpretation; it does not edit `DOCTRINE.md` body in this commission.

---

## 15. Pointers (read-only)

| Doc | Role |
|-----|------|
| `BASELINE_gauntlet-v2.0-alpha.md` | Unchanged baseline checklist |
| `INSTITUTIONAL_LOCK_2026-09-11.md` | Institutional freeze (unmodified) |
| `AMENDMENT_RULE.md` / `AMD-20260911-PM-001` | Change control · this expansion |
| `CYCLE_5_RESEARCH_ORDERS.md` | Catalyst continuity |
| `archive/templates/BINARY_CONTRACT.md` | Contract schema |
| `archive/templates/FEATURE.md` | Feature Card schema |
| `archive/templates/STRATEGY_LEAGUE.md` | League schema |
| `archive/templates/EDGE.md` | Existing Edge Card schema (unchanged) |

---

*End DOMAIN ALIGNMENT DIRECTIVE — 2026-09-11. Classification: DOMAIN OBJECTIVE EXPANSION. Baseline `gauntlet-v2.0-alpha` unchanged. RETROACTIVE: NO.*
