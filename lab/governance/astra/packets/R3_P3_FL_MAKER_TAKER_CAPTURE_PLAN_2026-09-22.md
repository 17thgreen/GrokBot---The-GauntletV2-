# R3-P3 FL maker/taker bands — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (C3 weather first-panel seed; `admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-23T00:19:20Z` (~2026-09-22 20:19 ET)  
**panel_version:** `2026-09-22.r3-p3-fl-maker-taker-v0`  
**Packet:** R3-P3-FL-MAKER-TAKER  
**Freeze:** `packets/R3-P3_FL_MAKER_TAKER_BANDS_FREEZE_KERNEL_2026-09-22.md` · sha `0ed697149136acb3aa840aeeb79d11c8f6ef80f37ce4dd692a3cb690212206a7`  
**C3 prefer:** `packets/C3_KXHIGHNY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`  
**Empty results:** `packets/r3_p3_fl_maker_taker/` (results/pnl **null** — FROZEN_NOT_RUN)  
**Owners:** Collector (panel/capture) → Simulator/Polars → Examiner  
**Hard rules:** Settled **public** tape · **refuse Lee-Ready** · no live orders · no invented PnL/ROI/volume · no `000` retune · **no ADMIT-1 steal** · **do not run admit.py** · **HOLD R3-P2** · prefer weather/politics/econ; avoid S1/S4/S5/R2-P3 as first panel

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/r3_p3_fl_maker_taker_panel.schema.json` |
| Panel stub | `lab/governance/astra/packets/R3_P3_FL_MAKER_TAKER_PANEL_STUB_2026-09-22.json` |
| Capture slot | `lab/astra-capture/r3-p3-fl-maker-taker/` |
| Bands registry | `lab/astra-capture/r3-p3-fl-maker-taker/bands_registry_10c.json` |
| Live GET | `lab/governance/astra/packets/r3_p3_fl_maker_taker/live_get_2026-09-22/` |
| STATUS | `lab/governance/astra/reports/STATUS_R3_P3_FL_MAKER_TAKER_PANEL_STUB_2026-09-22.md` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook (later ROI channel) | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` — Collector does **not** compute ROI |
| R1-P5 rails (optional freshness) | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Bands | Pre-register 10¢ bands **before** outcome join |
| Trades | Native `taker_outcome_side` / `taker_book_side` only — refuse Lee-Ready |

## Panel design
1. **Cohort:** C3 weather first (`KXHIGHNY`, `KXHIGHCHI`); econ series metadata probed as secondary.
2. **panel_version:** `2026-09-22.r3-p3-fl-maker-taker-v0`.
3. **Bands (locked first):** `[0-0.10)`, `[0.10-0.20)`, … `[0.90-1.00]`.
4. **Trades:** public GET `/markets/trades`; map `taker_outcome_side` + `taker_book_side` honestly; `taker_side` deprecated alias; `taker_action` absent on Trade — do not invent.
5. **Resolution join:** only when `status=settled` + non-empty `result` — deferred this stub (seed markets still active; settled listing 429).
6. **Measurement shells null:** MZ; post-fee ROI by band; maker vs taker.
7. **Host:** `https://api.elections.kalshi.com/trade-api/v2` GET-only. Throttle; honest 429 notes.

## Live resolve (this stub pass)
| Surface | Result |
|---|---|
| `GET /series/KXHIGHCHI` | **200** Climate and Weather |
| `GET /series/KXHIGHNY` | **429** then retry **200** |
| `GET /series/KXFEDDECISION`, `KXGDP` | **200** Economics |
| `GET /series/INXD` | **404** |
| `GET /markets?status=settled&series_ticker=KXHIGH*` / Fed / GDP | **429** (all attempts) |
| `GET /events?status=settled&series_ticker=KXHIGH*` | **429** |
| `GET /markets/KXHIGHNY-26SEP22-B67.5` (+T70, CHI B64.5) | **200** — status **active**, result empty |
| `GET /markets/trades?ticker=KXHIGHNY-26SEP22-*` / CHI | **200** — native taker fields present |
| Guessed prior-day settled tickers SEP20/21 | **404** — not invented further |

## Seed cohort
| Slice | N | Series | Notes |
|---|---|---|---|
| weather markets | **3** | KXHIGHNY, KXHIGHCHI | pre-settlement seed |
| weather events | **2** | …-26SEP22 | |
| trades sampled | **15** | same | +3 recent unrelated in live_get |
| settled resolved | **0** | — | listing 429 |

## Measurement objects (null until Examiner)
1. **MZ:** \(Y-P=\alpha+\psi P\) event-clustered  
2. **Post-fee ROI by 10¢ band** via R1-P1 (Collector does not compute)  
3. **Maker vs Taker** via native taker fields  

## Out of scope
- admit.py / ADMIT-1 recorder  
- R3-P2  
- Lee-Ready  
- Live orders / signed host  
- Invented ROI / PnL / volume / settled tickers  
- Q6-`000` retune  

## Done =
Schema + bands registry + seed panel stub + capture plan + idle slot + STATUS on disk. Ready for Examiner after settlement join + Conductor ping.
