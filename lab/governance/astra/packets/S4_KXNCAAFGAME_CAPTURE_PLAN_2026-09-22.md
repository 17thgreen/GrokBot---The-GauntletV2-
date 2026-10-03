# S4 KXNCAAFGAME — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (113 events seeded; `admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-22T23:49:34Z` (~2026-09-22 19:49 ET)  
**panel_version:** `2026-09-22.s4-kxncaafgame-v0`  
**Packet:** S4-KXNCAAFGAME-MEAS  
**Freeze:** `packets/S4_KXNCAAFGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `9e6556c150c726b679ac8393f1f5338cf983489259b0f34cdedf221c030be795`  
**Scout:** `packets/scout_s4_kxncaafgame/` (results/pnl null — FROZEN_EXPERIMENT)  
**Owners:** Collector (panel/capture) → Clock (join) → Conductor greenlight → admit.py (later)  
**Hard rules:** No live orders · no invented volume/PnL · no Q7/Q6 fee literals · **no ADMIT-1 / PIT@CLE / S1 / R2-P3 / S5 budget steal** · **do not run admit.py yet** · football OOS vs `000` (not more `KXNFLGAME` capacity)

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/s4_kxncaafgame_panel.schema.json` |
| Panel stub (seeded, not admitted) | `lab/governance/astra/packets/S4_KXNCAAFGAME_PANEL_STUB_2026-09-22.json` |
| Capture slot (idle) | `lab/astra-capture/s4-kxncaafgame/` |
| Live GET artifact | `lab/governance/astra/packets/s4_kxncaafgame_live_get_2026-09-22/` |
| Freeze kernel | `lab/governance/astra/packets/S4_KXNCAAFGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| Scout bundle | `lab/governance/astra/packets/scout_s4_kxncaafgame/` |
| STATUS | `lab/governance/astra/reports/STATUS_S4_KXNCAAFGAME_PANEL_STUB_2026-09-22.md` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` · formula `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| Fee shape | `maker_fees` / **1** via feebook only (live series: `fee_type=quadratic_with_maker_fees`, `fee_multiplier=1`) — **forbid** Q7/Q6 `0.0175`/`0.07` literals |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Kickoff SoT | Kalshi `occurrence_datetime` (market-level public GET) |

## Panel design
1. **Series:** `KXNCAAFGAME` only (college football game moneyline binaries).  
2. **Cohort bound:** next **Saturday** Kalshi slate = `event_ticker` contains `26SEP26` (Sat 2026-09-26).  
3. **Live resolve:** public GET `events?series_ticker=KXNCAAFGAME&status=open&with_nested_markets=true` @ `2026-09-22T23:48:33Z` → **113 events / 226 markets**.  
4. **panel_version:** `2026-09-22.s4-kxncaafgame-v0`.  
5. **Events:** seeded with tickers + `kalshi_occurrence_datetime` + `market_tickers` + `t_minus_7d_utc` + `window_clock_source=kalshi_occurrence` + `sot_pin`; **`admitted_at` null**.  
6. **Volume:** null — do not copy scout/live OI/vol as admitted facts.  
7. **Scout OI note:** live verify shows `KXNCAAFGAME-26SEP26TXAMLSU` (LSU) and `KXNCAAFGAME-26SEP26ETAMMCNS` (MCNS) present; OI not written to panel.  
8. **Football OOS:** vs Q6-`000`; **no** `000` retune; **not** more `KXNFLGAME` MM capacity.  
9. **Weekend edge (ineligible/not primary):** SEP25 ticker with Sat early-AM ET occurrence (e.g. CLEMCAL) noted separately — not in primary `26SEP26` seed.

## Kickoff / T−7d (occurrence_source = kalshi_public_get)
| Bound | Value |
|---|---|
| Earliest occurrence | `2026-09-26T19:00:00Z` (`2026-09-26 15:00 ET`) — `KXNCAAFGAME-26SEP26BUCKPITT` |
| Latest occurrence | `2026-09-27T05:30:00Z` (`2026-09-27 01:30 ET`) — `KXNCAAFGAME-26SEP26NAUMTST` |
| Earliest T−7d | `2026-09-19T19:00:00Z` |
| Past at stub? | **YES** (all 113 events) |

**Admit gate:** honor admit.py — real UTC; refuse past T−7d; never backfill. Live admit would hit **REFUSE_PAST_TMINUS7D**. Stub waits for Clock join + Conductor disposition. **Do not backfill. Do not run admit.py in this pass.**

## GET-only capture plan (future recorder — not started)
| Item | Plan |
|---|---|
| Host | `api.elections.kalshi.com` public GETs only |
| Routes | events listing by series, series metadata, event metadata, orderbook, public trades |
| DB | `lab/astra-capture/s4-kxncaafgame/capture.sqlite` (new; never ADMIT-1 / S1 / R2-P3 / S5 DB) |
| PID namespace | `s4-kxncaafgame` — separate idle slot |
| Interval | TBD at admit; throttle ≥45–90s; only if other capture budgets uncontended |
| Start rule | Clock join + Conductor greenlight + admit.py accept (T−7d not past) |

## Schedule vs other capture slots
- **Now:** schema + seeded panel stub + idle README slot only. **No recorder. No poll.**  
- **Admit/live poll:** only after Clock join + Conductor greenlight **and** when it does not contend with PIT@CLE ADMIT-1, S1, R2-P3, or S5.  
- Never share ADMIT-1 process or SQLite under `lab/astra-capture/prospective/`.

## Explicit non-owns
- No Q6-`000` retune · no Q7 reopen · no capital A-arms · no `KXNFLGAME` MM expand  
- No `KXNCAAFSPREAD` / `KXNCAAFTOTAL` until Scout listing confirm  
- results/pnl/volume remain null; scout_s4 results stay null  
