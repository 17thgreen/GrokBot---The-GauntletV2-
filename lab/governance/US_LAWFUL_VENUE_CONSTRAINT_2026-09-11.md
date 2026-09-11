# US LAWFUL VENUE CONSTRAINT — Execution / cockpit / capital
**Document:** `US_LAWFUL_VENUE_CONSTRAINT_2026-09-11.md`  
**Authority:** Logan M (Human Governor)  
**Date (UTC):** 2026-09-11  
**Classification:** **HARD OPERATIONAL CONSTRAINT** (US-operator refinement)  
**Not:** a retroactive rewrite of `gauntlet-v2.0-alpha` constitution, Institutional Lock bodies, or prior cemetery / Edge Card verdicts  
**RETROACTIVE:** **NO**  
**References:** `VENUE_DISCOVERY_2026-09-11.md` · `PREDICTION_MARKET_MISSION_2026-09-11.md`  
**Evidence tags:** `[V]` observed/verified · `[I]` inference · `[U]` unknown / UNTESTED · (claims below tagged accordingly)

---

## 0. Hard constraint

For **execution**, **cockpit decision-support that implies tradability**, and **capital routing** under this mission:

> **US-lawful prediction-market venues only.**

| Surface | Binding |
|---------|---------|
| What this binds | Order placement paths, live trading adapters, Treasurer/Canary capital gates, cockpit “executable” labels, any artifact that implies a US operator may trade the contract |
| What this does not waive | Forecast≠trade; no auto real-money; Clock / Examiner / Prosecutor / Mechanic / Treasurer / Canary still bind `[V]` per mission |
| Baseline | `gauntlet-v2.0-alpha` **unchanged** — this file is a going-forward operator constraint, not a constitutional rewrite `[A]` Governor directive |

Any design that treats a non–US-lawful venue as an **execution** target for Logan / US operators is **out of scope** for capital and cockpit-executable paths until Governor + counsel revise this constraint `[U]` counsel.

---

## 1. Primary adapter priority (US-lawful first)

Priority for **execution / cockpit / capital** adapters (not research inventory rank):

| Rank | Adapter ID | Status for US execution | Product note (per `VENUE_DISCOVERY_2026-09-11.md`) |
|------|------------|-------------------------|-----------------------------------------------------|
| **1 — PRIMARY** | **`KALSHI`** | **US-lawful venue of record for this mission** `[V]` CFTC-regulated exchange surface; live **15m** BTC/ETH Up-Down (`KXBTC15M` / `KXETH15M`) `[V]` | Strong for **15m**; **no 5m/10m** series found at discovery `[V]` |
| **2 — WATCHLIST** | **`POLYMARKET_US`** | Watchlist until **short crypto binaries** exist | Currently sports live; politics/finance/economics “coming soon”; **no** short crypto Up/Down inventory `[V]` |
| **3 — RESEARCH ONLY** | **`POLYMARKET_GLOBAL`** | **NOT** an execution venue for US operators | May remain **Layer-1 research comparable / oracle study only** with explicit **non-execution** label (see §2) |

**Restated priority chain:** **Kalshi → Polymarket US (when products) → Polymarket Global research-only.**

Inventory match for 5m/15m on Global (see Venue Discovery §5) does **not** override this US-lawful execution order `[I]`.

---

## 2. POLYMARKET_GLOBAL — non-execution label

| Rule | Detail |
|------|--------|
| Execution | **Forbidden** as a trading / capital / cockpit-executable venue for US operators under this constraint `[A]` Governor |
| Allowed use | **Layer-1 research comparable** and **oracle / resolution-study** only (rules text, TWAP semantics, historical short-window structure) `[I]` aligned to mission L1/L2 research |
| Required label | Any dataset, adapter stub, notebook, or Edge Card that touches Global must carry an explicit **`NON-EXECUTION`** / **research-only** marker for US-operator paths `[A]` |
| Eligibility | UI messaging that `.com` trading is blocked in the US is observed `[V]`; individual legal eligibility remains **`[U]` counsel** — constraint does not wait on counsel to ban treating Global as executable |

---

## 3. Binance / fapi / Vision — Layer-3 only

| Surface | Role under this mission |
|---------|-------------------------|
| Binance USD-M REST (`fapi.binance.com`) | **Layer-3 external predictor data only** (microstructure / funding / OI / related exports) `[V]` per `PREDICTION_MARKET_MISSION_2026-09-11.md` §7 L3 and `DATA_PROV_CATALYST_SOURCES_2026-09-11.md` |
| Binance Vision archives (`data.binance.vision`) | Same — **L3 historical predictor** backfill only `[V]` |
| Prediction-market trading venue? | **NEVER.** Binance / fapi / Vision are **not** prediction-market Layer-1 venue adapters and **must not** be framed as the PM trading venue for this mission `[A]`/`[V]` |

Cycle 5 Catalyst futures mechanism tests may continue to consume these series as registered DATA-PROV sources; that does **not** authorize PM order routing on Binance `[I]`.

---

## 4. Cross-references

| Document | Role |
|----------|------|
| `VENUE_DISCOVERY_2026-09-11.md` | Read-only product inventory (5m/15m/hourly; fees; APIs) — findings **not rewritten** by this constraint; see appended “US operator constraint” pointer |
| `PREDICTION_MARKET_MISSION_2026-09-11.md` | Domain objective; adapter abstraction; L1/L2/L3; forecast≠trade |
| `AMD-20260911-PM-001.md` | Domain expansion stub; **RETROACTIVE: NO** |
| `BASELINE_gauntlet-v2.0-alpha.md` / `INSTITUTIONAL_LOCK_2026-09-11.md` | **Unmodified** by this file |

---

## 5. Operational reminders

- **Do not place trades** from this constraint file; it gates *where* execution may later be considered, not *whether* to trade now.
- Do not stop running data fetches solely because a source is L3 or research-only.
- Mechanic: separate executable path from forecast skill; fee/spread/latency only on **US-lawful** adapters when sizing capital `[I]` mission Mechanic row.
- New adapters beyond Kalshi / Polymarket US require registered dataset + Clock verdict + Archivist index per mission §2.2 `[V]`.

---

*End of constraint. Claims limited to Governor directive + cited discovery/mission evidence dated 2026-09-11. Legal advice: none — `[U]` counsel.*
