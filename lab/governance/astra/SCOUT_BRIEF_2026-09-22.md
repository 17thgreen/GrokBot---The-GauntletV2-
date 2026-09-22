# Market Scout Brief — 2026-09-22

**Desk:** Astra / Kalshi (Working Plan v0.1 GO)  
**Role:** Scout (measurement kernels + T−7d calendar awareness only; no bots, no panel admission)  
**Status timestamp:** **2026-09-22 17:07 ET** (America/New_York, UTC−4)  
**Incumbent:** NFL Kalshi maker / Astra Deathmatch (displaceable) — Scout does **not** re-pitch NFL game MM.

**Sources (GET-only):**
- Kalshi public: `https://api.elections.kalshi.com/trade-api/v2/` — `/series` (200), `/markets?series_ticker=KXNFLGAME` (200), `KXMLBGAME` (200), `KXNBAGAME` (200), `KXNFLPASSYDS` (200), `/events/KXNFLGAME-26SEP28PHICHI` (200), `/events/KXNFLGAME-26OCT01PITCLE` (200)
- Repo: `17thgreen/GPT-6-Astra-Deathmatch` → `nfl_factorial_lab_20260921/RESERVED_HOLDOUT.json` (+ collector copy)
- Local: `ASTRA_NEXT_STEPS_2026-09-22.md`

**API blockers (honest):**
| Call | Result |
|---|---|
| `/series` | OK — 14,274 series (~3,741 Sports) |
| `/markets?series_ticker=KXNFLGAME` | OK — 64 open markets / 32 events |
| `/markets` default page | OK but dominated by `KXMVECROSSCATEGORY*` parlays — not useful as sports inventory |
| `/markets?series_ticker=` for `KXNFLSPREAD`, `KXNFLTOTAL`, `KXNCAAFGAME`, `KXNHLGAME`, `KXNFLANYTD` | **429 too_many_requests** after burst (series metadata still confirmed present) |
| `/events?series_ticker=KXNFLGAME` list | **429** intermittent |
| `https://trading-api.kalshi.com/trade-api/v2/` | **401** without auth — do not use for public listing |
| Liquidity / P&L / fill rates | **Not invented.** Where shown, figures are raw API `volume_fp` / `volume_24h_fp` / `open_interest_fp` only |

---

## 1. NFL T−7d calendar (next ~14 days)

**Convention:** T−7d = kickoff − 7d (same as holdout / collector protocol). Kickoffs from `RESERVED_HOLDOUT.json` unless noted. Venue IDs from live Kalshi where resolved.

**Holdout registry status:** `PENDING_FUTURE_WINDOWS_NO_HOLDOUT_RESULTS` · freeze `2026-09-21T15:29:51Z` · 32 games. PHI@CHI full window already incomplete for complete-cohort gate (see Next Steps).

### 1a. Holdout games with T−7d in window (through ~2026-10-06)

| Game | Venue event (Kalshi) | Kickoff (UTC) | Kickoff (ET) | T−7d (UTC) | T−7d (ET) | Window status |
|---|---|---|---|---|---|---|
| PHI@CHI | `KXNFLGAME-26SEP28PHICHI` | 2026-09-29T00:15Z | **2026-09-28 20:15 ET** | 2026-09-22T00:15Z | **2026-09-21 20:15 ET** | **OPEN — MISSED full start** (~21h late as of brief) |
| **PIT@CLE** | **`KXNFLGAME-26OCT01PITCLE`** *(was `null` in holdout; live-resolved today)* | 2026-10-02T00:15Z | **2026-10-01 20:15 ET** | 2026-09-25T00:15Z | **2026-09-24 20:15 ET** | **UPCOMING — next hard deadline** |
| IND@WAS | `KXNFLGAME-26OCT04INDWAS` | 2026-10-04T13:30Z | 2026-10-04 09:30 ET | 2026-09-27T13:30Z | **2026-09-27 09:30 ET** | Upcoming |
| ARI@NYG | `KXNFLGAME-26OCT04ARINYG` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| DAL@HOU | `KXNFLGAME-26OCT04DALHOU` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| GB@TB | `KXNFLGAME-26OCT04GBTB` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| JAX@CIN | `KXNFLGAME-26OCT04JACCIN` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| LA@PHI | `KXNFLGAME-26OCT04LARPHI` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| NE@BUF | `KXNFLGAME-26OCT04NEBUF` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| NYJ@CHI | `KXNFLGAME-26OCT04NYJCHI` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| TEN@BAL | `KXNFLGAME-26OCT04TENBAL` | 2026-10-04T17:00Z | 2026-10-04 13:00 ET | 2026-09-27T17:00Z | 2026-09-27 13:00 ET | Upcoming |
| MIA@MIN | `KXNFLGAME-26OCT04MIAMIN` | 2026-10-04T20:05Z | 2026-10-04 16:05 ET | 2026-09-27T20:05Z | 2026-09-27 16:05 ET | Upcoming |
| DEN@SF | `KXNFLGAME-26OCT04DENSF` | 2026-10-04T20:25Z | 2026-10-04 16:25 ET | 2026-09-27T20:25Z | 2026-09-27 16:25 ET | Upcoming |
| KC@LV | `KXNFLGAME-26OCT04KCLV` | 2026-10-04T20:25Z | 2026-10-04 16:25 ET | 2026-09-27T20:25Z | 2026-09-27 16:25 ET | Upcoming |
| LAC@SEA | `KXNFLGAME-26OCT04LACSEA` | 2026-10-04T20:25Z | 2026-10-04 16:25 ET | 2026-09-27T20:25Z | 2026-09-27 16:25 ET | Upcoming |
| DET@CAR | `KXNFLGAME-26OCT04DETCAR` | 2026-10-05T00:20Z | 2026-10-04 20:20 ET | 2026-09-28T00:20Z | 2026-09-27 20:20 ET | Upcoming |
| ATL@NO | `KXNFLGAME-26OCT05ATLNO` | 2026-10-06T00:15Z | 2026-10-05 20:15 ET | 2026-09-29T00:15Z | 2026-09-28 20:15 ET | Upcoming |

**Next hard deadline for salvage / identity+collector:** **PIT@CLE T−7d = 2026-09-24 20:15 ET** (~51h from this brief). Venue ticker is live; holdout JSON still has `event: null` — Conductor must treat identity update as a separate admission/docs step (Scout does not admit).

### 1b. Non-holdout NFL awareness (incumbent MM territory)

Open `KXNFLGAME` book also shows Week 3 slate already trading hard (examples; volumes = API sums of both team markets):

| Event | Subtitle cue | Market close (UTC) | Notes |
|---|---|---|---|
| `KXNFLGAME-26SEP24ATLGB` | ATL@GB (Thu) | 2026-09-27T00:15Z | Also listed as measurement_development; heavy tape already (`vol_24h` ~5e5 contracts aggregate) |
| `KXNFLGAME-26SEP27*` Sunday slate (CIN/PIT, SEA/WAS, …, LAR/DEN) | Sun 2026-09-27 | closes 2026-09-29… | High OI; **overlap with incumbent** — calendar only |
| `KXNFLGAME-26SEP28PHICHI` | PHI@CHI | close 2026-10-01T00:15Z | Holdout game 1; active (OI large) |

### 1c. Other sports kickoffs (clear from open markets)

| Sport / series | What we saw | Kickoff / close cue | Scout note |
|---|---|---|---|
| **MLB** `KXMLBGAME` | 42 open events (same-day 2026-09-22 slate) | Closes ~2026-09-25 evening UTC for tonight’s games | Daily cadence; strong same-day `volume_24h` on several books — candidate for non-NFL kernel |
| **NBA** `KXNBAGAME` | 3 early events (e.g. `…-26OCT20BOSDET`) | Tip ~2026-10-20 | Season not open yet; thin early listing |
| **CFB / NHL / NFL spread·total** | Series exist | Inventory **not confirmed** this pass (429) | See kernels / blind spots |
| **NFL props** `KXNFLPASSYDS` | 2 events open (`…ATLGB`, `…LACBUF`) | Same game windows as ML | Ladder/threshold structure present |

**Kickoff caveat:** Live `occurrence_datetime` on PHI/PIT events is **+3h** vs holdout `kickoff` (e.g. PIT event `2026-10-02T03:15Z` vs holdout `2026-10-02T00:15Z`; subtitle “Oct 1”). Desk should pin one source of truth before capture windows — Scout flags, does not choose.

---

## 2. Measurement kernels (≤5)

Not product pitches. Each answers a **measurement** question the desk could run with public GET capture only.

| # | Market / series | Structure | Why measure (question) | Overlap vs incumbent NFL game MM | Rough capture cost (public GET) | Rec |
|---|---|---|---|---|---|---|
| 1 | `KXNFLSPREAD` (+ sibling `KXNFLTOTAL` / `KXNFLTEAMTOTAL` if inventory confirms) | Binary side markets on same NFL events (spread / total / team total) | Does quote/queue microstructure and adverse selection **differ** from moneyline on the **same** kickoff, or is ML already a sufficient statistic? | **High** — same events & T−7d windows as incumbent | Series confirmed; markets listing **429 this pass**. Cost if unblocked: same pattern as Q4 collector (`/events`, `/markets`, orderbook, trades) × N side markets per game | **try** (after rate-limit cool-down; do not steal holdout collector cycles from PIT@CLE) |
| 2 | `KXNFLPASSYDS` (family: `KXNFLANYTD`, `KXNFLRECYDS`, `KXNFLRSHYDS`, …) | Multi-strike player props / ladders on game events | Do ladder thresholds share one latent (player mean) or fragment into independent books? Useful for **multi-outcome** kernel design without leaving football. | **Medium** — same games, different contracts; competes for poll budget | Confirmed open: 27 markets / 2 events this pass. GET allowlist same as game MM | **try** (small panel; ATL@GB already late — prefer next prop-rich slate) |
| 3 | `KXMLBGAME` | Binary game moneyline, daily baseball | Does the NFL T−7d→T−3h timing lab **generalize** to shorter, daily sports with same-day liquidity spikes? | **Low** — different sport/season clock; little schedule collision with NFL Thu/Sun/Mon | 84 markets / 42 events pulled OK. Capture cost: high **event count**, short windows (intraday) | **try** |
| 4 | `KXNCAAFGAME` (+ `KXNCAAFSPREAD` / `KXNCAAFTOTAL` if present) | College football game ML (weekend cluster) | Is CFB a cleaner **out-of-sample sport** than MLB for football-specific features (drive clock, scoring rates) without touching NFL holdout? | **Medium** — weekend overlap with NFL Sun; different series | Series confirmed; **markets 429** — inventory unknown | **defer** until listing succeeds + next Saturday slate mapped |
| 5 | `KXMVENFLSINGLEGAME` / `KXMVENFLMULTIGAME` | Exotic multi-leg (MVE) NFL collections | Are parlays a distinct microstructure class (leg correlation, early close) worth a kernel? | **High thematic**, but **zero open markets** on single-game series this pass (`markets: []`); default `/markets` flood is cross-category MVE noise | Listing cheap; durable capture design unclear until stable event tickers exist | **skip** (no measurable open inventory today) |

**Explicitly not proposed as Scout kernels:** more `KXNFLGAME` moneyline capacity (incumbent), season-long futures (`KXNFLAFCCHAMP`, win totals), or NBA tip-off books until closer to 2026-10-20 (`defer` informally — not in the five).

---

## 3. Blind spots

1. **Rate limits** blocked spread/total/CFB/NHL/anytime-TD market pages — structure existence ≠ confirmed open inventory or liquidity.
2. **Holdout identity lag:** PIT@CLE now `KXNFLGAME-26OCT01PITCLE` on venue; registry still `null`. Week-4+ games need the same resolve-before-T−7d pass.
3. **Kickoff disagreement** (+3h) between holdout CSV snapshot and Kalshi `occurrence_datetime` / subtitle date — risk of wrong T−7d if someone mixes sources.
4. **MVE flood:** unfiltered `/markets` is mostly cross-category parlays; Scout must always filter by `series_ticker`.
5. **No orderbook/trades depth pulled this brief** (avoided further 429). Capture-cost estimates are route counts, not bandwidth proven.
6. **Complete 32-game cohort** already broken for PHI@CHI full window — Scout calendar still lists it for awareness; science path is Conductor ADMIT-1 / partial-salvage labeling, not Scout.
7. **Alternate host** `trading-api.kalshi.com` is not a public fallback (401).

---

## 4. TLDR for Conductor (5 lines)

1. Scout brief on disk; NFL T−7d calendar built from holdout + live `KXNFLGAME` (32 open events).  
2. **Next hard deadline: PIT@CLE T−7d 2026-09-24 20:15 ET** — venue ticker live `KXNFLGAME-26OCT01PITCLE` (holdout still null).  
3. PHI@CHI full T−7d remains **missed**; do not backdate.  
4. **Kernels:** try `KXNFLSPREAD`(+totals), `KXNFLPASSYDS` props, `KXMLBGAME`; defer `KXNCAAFGAME`; skip empty `KXMVENFL*`.  
5. API: elections host OK with throttling; spread/CFB/NHL listings **429**; no invented liquidity/P&L.

---

*End Scout Brief 2026-09-22 · GET-only · no orders · no panel admission*
