# R3-P4 L2 shape — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (bounded stratified seed; `admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-23T00:06:20Z` (~2026-09-22 20:06 ET)  
**panel_version:** `2026-09-22.r3-p4-l2-shape-v0`  
**Packet:** R3-P4-L2-SHAPE-SF1-SF2  
**Freeze:** `packets/R3-P4_L2_SHAPE_LONGSHOT_DEPTH_FREEZE_KERNEL_2026-09-22.md` · sha `4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528`  
**Scout / empty results:** `packets/r3_p4_l2_shape/` (results/pnl **null** — FROZEN_NOT_RUN)  
**Owners:** Collector (panel/capture) → Simulator (SF1/SF2 shape stats) → Examiner  
**Hard rules:** No live orders · no invented volume/OI/depth/PnL · no Lee-Ready · no Q7/Q6 fee literals · **no ADMIT-1 / PIT@CLE / C1 budget steal** · **HOLD R3-P3** · **do not run admit.py** · **no recorder**

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/r3_p4_l2_shape_panel.schema.json` |
| Panel stub (seeded, not admitted) | `lab/governance/astra/packets/R3_P4_L2_SHAPE_PANEL_STUB_2026-09-22.json` |
| Capture slot (idle) | `lab/astra-capture/r3-p4-l2-shape/` |
| Live GET artifact | `lab/governance/astra/packets/r3_p4_l2_shape/live_get_2026-09-22/` |
| Freeze kernel | `lab/governance/astra/packets/R3-P4_L2_SHAPE_LONGSHOT_DEPTH_FREEZE_KERNEL_2026-09-22.md` |
| Empty results dir | `lab/governance/astra/packets/r3_p4_l2_shape/` |
| STATUS | `lab/governance/astra/reports/STATUS_R3_P4_L2_SHAPE_PANEL_STUB_2026-09-22.md` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook / reciprocal book | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` · `ask_YES=1−best_NO_bid` etc. · formula `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| R1-P5 rails / freshness | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` · **`content_fresh_flag` required** on every market row |
| Capture | GET-only public orderbook · stratified sports vs non-sports · raw depth only when GET succeeds |

## Panel design
1. **Cohort:** stratified **sports vs non-sports** seed (small OK if 429).  
2. **panel_version:** `2026-09-22.r3-p4-l2-shape-v0`.  
3. **Markets:** ticker + `category_slice` + `content_fresh_flag` + optional `raw_orderbook` / `reciprocal_tob`; **`admitted_at` null**.  
4. **Volume/OI:** null in panel — do not copy API zeros as admitted facts.  
5. **SF1 / SF2:** measurement object schema present; **values null** until Simulator/Examiner.  
6. **Host:** `https://api.elections.kalshi.com/trade-api/v2` GET-only. Throttle; on 429 keep smaller scout/freeze sample.

## Live resolve (this stub pass)
| Surface | Result |
|---|---|
| `GET /series/{KXHIGHNY,KXBTC,KXFEDDECISION,INXY,KXGDP}` | **200** — metadata only |
| `GET /markets?limit=5&status=open` | **429** |
| `GET /events?series_ticker=…` | **429** |
| `GET /markets?series_ticker=KXHIGHNY\|KXFED\|KXGDP` | **429** (retry 429) |
| `GET /markets?series_ticker=KXBTC&limit=2` | **200** — 2 active range markets |
| `GET /markets/{KXNCAAFGAME…}` + `/orderbook` | **200** — sports seed |
| `GET /markets/{KXBTC-…}` + `/orderbook` | **200** (one OB retried after intermittent 429) |
| Weather/econ open tickers | **unresolved** this pass — honest smaller non-sports = KXBTC |

## Seed cohort
| Slice | N | Series | Tickers (sample) |
|---|---|---|---|
| sports | **4** | KXNCAAFGAME | `…BUCKPITT-PITT/BUCK`, `…TEXTENN-TENN`, `…PREMRST-MRST` |
| non_sports | **2** | KXBTC | `KXBTC-26SEP2317-T76250`, `…T95749.99` |
| orderbook OK | **6/6** primary | — | raw `orderbook_fp` stored |
| scout only | 2 finalized empty | KXBTC15M | Sep11 probes — not primary |

## Measurement objects (null until Simulator/Examiner)
1. **SF1:** half-spread bps by mid decile (median) — sports / non-sports / all  
2. **SF2:** L1/top-10 depth share + KL vs uniform \(1/10\)  
3. **Slice:** sports vs non-sports (no `000` knobs)

## Out of scope
- admit.py / recorder start  
- R3-P3 FL crawl  
- Lee-Ready  
- Live orders / signed host  
- Invented depth / volume / OI / results / pnl  

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS on disk. Ready for Simulator SF1/SF2 compute after Conductor ping.
