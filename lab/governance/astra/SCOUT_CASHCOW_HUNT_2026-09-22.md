# Scout cash-cow hunt — external slots vs Q6-000
**Seat:** Market Scout (Astra / Kalshi desk)  
**Timestamp:** **2026-09-22 20:10 ET** (America/New_York, UTC−4)  
**Mode:** Conductor STANDING MO — external cash-cow hunt · GET-only · no orders · no invented volume/OI/PnL · no capital-structure  
**Hosts used:** `https://api.elections.kalshi.com/trade-api/v2/` (primary). Fee pins from prior `/series` cache (`/tmp/kalshi_series.json`, 14274 series) after live `/series` **429**. `trading-api.kalshi.com` skipped (401).  
**Pins:** Kickoff SoT = Kalshi market `occurrence_datetime` (ET labeled below). Do **not** reopen `SHADOW_CANDIDATE_FREEZE` / `000`. S2 / R2-P4 (`KXNFLSPREAD`/`KXNFLTOTAL`) left alone (no hard poll).  
**Raw packet:** `packets/scout_cashcow_hunt_2026-09-22/`  
**Cite prior:** `SCOUT_Q6_STRESS_KERNELS_2026-09-22.md`, `SCOUT_MAXIMIZE_DELTA_2026-09-22.md`, `SCOUT_R2P3_PROP_SLATE_2026-09-22.md`, `SCOUT_TRIAGE_2026-09-22.md`, `SCOUT_TRIAGE_MAXIMIZE_DELTA_2026-09-22.md`, `SCOUT_TRIAGE_Q6_STRESS_2026-09-22.md`, `SCOUT_TRIAGE_R2P3_SLATE_2026-09-22.md`

---

## ≤5 TRY table (fresh external only)

| ID | Market / structure | Kernel question (1 sentence) | Dead-overlap vs Q6-000 | Fee / queue honesty hook | Raw inventory proof (page-sample) | Rec |
|---|---|---|---|---|---|---|
| **C1** | `KXUFCFIGHT` (UFC fight ML binaries) | Does a fight-night discrete settlement clock + deep YES/NO books show fee-honest maker/taker + queue fragility that **beats** NFL T−window shadow EV under shared $5k bakeoff? | **None / low** — combat card calendar, not NFL week/T−7d allocator; no pair-router semantics. | Series fee pin: `quadratic` / **1** (cached `/series`). Stress R1-P1 ceil book near extreme prices on favorite legs; R1-P5 refuse zero-credit quotes on fight-night L2. | **200** · 58 open markets / 29 events · Σ volume_fp≈**1.7088e6** · Σ volume_24h_fp≈**1.5108e6** · Σ open_interest_fp≈**1.2545e6** (full open set, no cursor). Samples: `…-26SEP22CONGUA-GUA` vol24≈602326 oi≈345780; `…-CON` vol24≈413990 oi≈273188. SoT sample occ=`2026-09-23T04:20:00Z` → **2026-09-23 00:20 ET**. | **TRY** |
| **C2** | `KXNHLGAME` (NHL game ML) | Does daily/near-daily hockey ML generalize the S1 MLB timing lab under the **same** maker-fee channel as NFL game books, enough to displace or stress `000`? | **Low** — different sport clock (puck-drop SoT); not a silent retune of NFL ML allocator. | Fee: `quadratic_with_maker_fees` / **1** (readable). Same R1-P1 maker path as NFL/NCAAF game books → clean fee-honest OOS vs `000`. | **200** · 66 markets / 33 events · Σ vol≈**3.8255e5** · Σ vol24≈**3.7325e5** · Σ oi≈**3.6027e5** (no cursor). Samples: `…-26SEP22DETPIT-PIT` vol24≈62739 oi≈61628 occ→**2026-09-22 22:00 ET**; `…-FLACAR-CAR` oi≈58346. | **TRY** |
| **C3** | `KXHIGHNY` weather high-temp ladder (+ multi-city `KXHIGHCHI` proof) | On daily max-temp threshold ladders, does a fee-honest Bernoulli / bordering-strike MM kernel (GitHub weather-spread structure) beat `000` after settlement-penalty + queue attribution? | **None** — climate binaries; no NFL event join. | Fee: `quadratic` / **1** (NY + CHI). Ladder near 0/1 strikes is the R1-P1 stress; multi-city inventory enables bordering-contract EV checks without RFQ. | **NY 200** · 12 mkts / 2 events · Σ vol≈**1.6799e5** · Σ vol24≈**1.5363e5** · Σ oi≈**1.0118e5**. Samples: `KXHIGHNY-26SEP22-T70` oi≈30276; `…-B67.5` vol24≈41513. Occ→**2026-09-23 10:00 ET**. **CHI 200** · 12 mkts · Σ vol24≈**5.1343e4** · Σ oi≈**3.5869e4** (multi-city proof). | **TRY** |
| **C4** | `KXCPI` (CPI release threshold ladder) | On a scheduled macro print, do threshold ladders under maker fees show different adverse-selection / queue fragility than sports T−windows — enough to stress `000`’s fee-honest edge claims? | **None** — economics release; no sports kickoff router. | Fee: `quadratic_with_maker_fees` / **1**. Maker-fee path + sparse 24h tape vs high OI = honesty stress (don’t invent fill density). | **200** · 44 mkts / 4 events · Σ vol≈**3.7390e5** · Σ vol24≈**4.4042e4** · Σ oi≈**1.6599e5**. Samples: `KXCPI-26SEP-T0.4` oi≈49774 vol24≈29715; `…-T0.5` oi≈36846. Some strikes lack `occurrence_datetime` (honest gap); sample with SoT: `…-T0.6` occ=`2026-10-14T13:56:00Z` → **2026-10-14 09:56 ET**. | **TRY** |
| **C5** | `KXBTC15M` (BTC 15-minute up/down binary) | Do ultra-short crypto binaries force fee/queue honesty failures (turnover ≫ sports T−window) that refute or beat `000`’s inherited maker/taker assumptions under shared capital rules? | **None** — crypto clock; rolling 15m windows. | Fee: `quadratic` / **1**. Extreme turnover → R1-P5 freshness/queue instruments dominate; GitHub `kxeth15m-research` structure parallel (ETH sibling). | **200** · **1** open market / 1 event (rolling) · volume_fp≈**133994.61** · volume_24h_fp≈**107298.17** · open_interest_fp≈**88032.36**. Sample: `KXBTC15M-26SEP222015-15` occ=`2026-09-23T00:20:00Z` → **2026-09-22 20:20 ET**. | **TRY** |

---

## Explicitly out / occupied (do not re-nominate as new cash cows)

| Item | Status |
|---|---|
| S1 `KXMLBGAME` | **Occupied** — ADMIT TRY |
| R2-P3 props (`KXNFLPASSYDS` + RECYDS/RSHYDS slate; ANYTD HOLD) | **Occupied** — ADMIT TRY / HOLD as prior |
| S4 `KXNCAAFGAME` | **Occupied** — TRY (later DR freeze) |
| S5 `KXMVECROSSCATEGORY*` | **FREEZE locked** — measurement-access only (not R1-P4 strategy; no Logan key ask) |
| S2 `KXNFLSPREAD` (+ `KXNFLTOTAL`) | **HOLD** until C1 PIT@CLE — **not polled** this hunt |
| Incumbent more `KXNFLGAME` ML / `000` retune | **OUT** |
| Empty `KXMVENFL*` | **SKIP** (no new inventory proof this pass) |
| `SHADOW_CANDIDATE_FREEZE` / Q6-000 reopen | **Forbidden** |
| Capital-structure Variants probe | **Out of seat** |
| `KXEPLGAME` | **SKIP now** — open markets `[]` (200, empty) |
| `KXFED` | **DEFER** — live markets **429** this pass (no invented inventory) |

---

## GitHub appendix (structure pointers only)

| Repo | Structure pointed at | Inventory-backed slot? |
|---|---|---|
| https://github.com/Ciarnan-Moloney/Kalshi-Weather-Spread-Algo | Multi-city highest-temp bordering strikes; fee-aware EV on adjacent contracts | **Yes → C3** (`KXHIGHNY` + `KXHIGHCHI` live OI/vol) |
| https://github.com/meloun7711/kxeth15m-research | 15-minute crypto up/down fee-honest paper edges (ETH) | **Yes → C5 sibling** (`KXBTC15M` live proof; ETH15M not re-probed this pass — optional watch) |
| https://github.com/polystrategist/kalshi-arbitrage-bot | YES+NO≠1 / spread arb with fee-aware PnL | Idea only — no exclusive series pin → **appendix** |
| https://github.com/MobinHariri/kalshi-polymarket-microstructure | Cross-venue fee+depth survival (read-only) | Idea only — measurement stack, not a Kalshi series → **appendix** |
| https://github.com/Pearlfisheryjersey8695/kalshiquant · https://github.com/Adi7710/kalshiquant · https://github.com/wespanko/tinli · https://github.com/faizan896/prediction-market-quant-lab · https://github.com/asianguy-based/Kalshi-Bot | Fee-aware sizing / microstructure / arb toolkits | Idea only without exclusive inventory pin → **appendix** |

**GitHub yielded inventory-backed slots:** **C3** (weather) and **C5** (15m crypto). Others appendix-only.

---

## API blockers (honest)

| Call | Result |
|---|---|
| `GET /series?limit=200` (hunt start) | **429** — fee pins taken from prior cache; not re-invented |
| `GET /markets?series_ticker=KXFED&status=open` | **429** — skipped; no FED inventory claimed |
| `GET /events?series_ticker=KXNHLGAME&status=open` | **429** — SoT taken from markets.`occurrence_datetime` instead |
| `GET /markets` for C1–C5 + CHI + ATP + EPL | **200** (see table / packet) |
| `trading-api.kalshi.com` | Not used (prior **401**) |
| S2 `KXNFLSPREAD` / `KXNFLTOTAL` | **Not called** (budget protect) |

Throttle: ~50–90s between live GETs after initial 429.

---

## Scout next

1. **Stand by** — do not steal ADMIT-1 / Collector / S2 poll budget.  
2. **Optional watches** (not TRY slots): `KXATPMATCH` (**200** · 48 mkts / 24 events · Σ vol≈3.37e5 · Σ vol24≈2.41e5 · Σ oi≈2.44e5 · fee `quadratic_with_maker_fees`/1) — strong tennis OOS if Conductor wants a 6th; `KXETH15M` sibling of C5; `KXFED` when 429 clears; other `KXHIGH*` cities for C3 multi-city panel.  
3. No orders · no panel admits · no `000` reopen · no S2 hard poll until C1 PIT@CLE stable.

