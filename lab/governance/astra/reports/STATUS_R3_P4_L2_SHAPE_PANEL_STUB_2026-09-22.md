# STATUS — R3-P4 L2 shape panel stub LAND 2026-09-22 (ET desk)

**Seat:** Collector (Astra/Kalshi)  
**Stubbed_at:** `2026-09-23T00:06:20Z` UTC (~2026-09-22 20:06 ET)  
**panel_version:** `2026-09-22.r3-p4-l2-shape-v0`  
**Packet:** R3-P4-L2-SHAPE-SF1-SF2  
**Freeze sha256:** `4a4e7cc61efcb436955c566edc7a2681603a014725bc79047f9d825392064528`  
**ADMIT-1 prospective/:** **UNTOUCHED** (mtimes unchanged; no recorder/poll share)  
**R3-P3:** **HOLD** — not started

## Absolute paths
| Artifact | Absolute path |
|---|---|
| Schema | `/workspace/lab/governance/astra/registry/schemas/r3_p4_l2_shape_panel.schema.json` |
| Panel stub | `/workspace/lab/governance/astra/packets/R3_P4_L2_SHAPE_PANEL_STUB_2026-09-22.json` |
| Capture plan | `/workspace/lab/governance/astra/packets/R3_P4_L2_SHAPE_CAPTURE_PLAN_2026-09-22.md` |
| Idle slot | `/workspace/lab/astra-capture/r3-p4-l2-shape/` |
| Idle README | `/workspace/lab/astra-capture/r3-p4-l2-shape/README.md` |
| Live GET seed | `/workspace/lab/governance/astra/packets/r3_p4_l2_shape/live_get_2026-09-22/` |
| Freeze | `/workspace/lab/governance/astra/packets/R3-P4_L2_SHAPE_LONGSHOT_DEPTH_FREEZE_KERNEL_2026-09-22.md` |
| Empty results | `/workspace/lab/governance/astra/packets/r3_p4_l2_shape/` (`results`/`pnl` null) |
| This STATUS | `/workspace/lab/governance/astra/reports/STATUS_R3_P4_L2_SHAPE_PANEL_STUB_2026-09-22.md` |
| R3-P1 FIXTURE_GAP (pre-existing) | `/workspace/lab/governance/astra/packets/r3_p1_fee_cost/R3-P1_FIXTURE_GAP_2026-09-22.md` |

## Cohort (seed)
| Metric | Value |
|---|---|
| Markets seed N | **6** |
| Sports N | **4** (KXNCAAFGAME) |
| Non-sports N | **2** (KXBTC active range) |
| Orderbook GET OK | **6/6** primary (raw depth stored) |
| Events N | **4** |
| `content_fresh_flag` | **present on all market rows** (initial seed snapshot → true when OB payload present) |
| `admitted_at` | **null** |
| SF1 / SF2 values | **null** (schema objects only) |
| volume / OI / results / pnl | **null** |

### Sample tickers
- Sports: `KXNCAAFGAME-26SEP26BUCKPITT-PITT` · `…-BUCK` · `…TEXTENN-TENN` · `…PREMRST-MRST`  
- Non-sports: `KXBTC-26SEP2317-T76250` · `KXBTC-26SEP2317-T95749.99`

## Pins
- **R1-P1:** `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` — reciprocal `ask_YES=1−best_NO_bid` applied to raw OB → `reciprocal_tob`  
- **R1-P5:** `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` — `content_fresh_flag` required  
- **Forbid** inherited Q7/Q6 fee literals · no `000` retune · no Lee-Ready

## 429 / blocker notes (honest)
- `GET /markets?limit=5` → **429**  
- `GET /events?series_ticker=…` → **429**  
- `GET /markets?series_ticker=KXHIGHNY|KXFEDDECISION|KXGDP` → **429** (retry 429) — weather/econ open tickers **unresolved**; non-sports seed shrunk to **KXBTC**  
- Intermittent orderbook **429** on `KXBTC-26SEP2317-T95749.99` — succeeded on retry  
- BTC15M Sep11 probes: market+OB **200** but **finalized/empty** — scout only, not primary cohort

## R3-P1 fee_cost fixtures
- **FIXTURE_GAP already filed** (not rewritten): `/workspace/lab/governance/astra/packets/r3_p1_fee_cost/R3-P1_FIXTURE_GAP_2026-09-22.md`  
- No auth fill fixtures with venue `fee_cost` found on box; parent hunting separately. Did not ask Logan for keys; did not run live fills.

## Gates
- `admitted_at`: **null**  
- admit.py: **not run**  
- recorder/poll: **not started** (idle slot only)  
- scout results/pnl: **null**  
- ADMIT-1 `prospective/`: untouched  
- R3-P3: **HOLD**

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS on disk. Ready for Simulator SF1/SF2 / Conductor ping.
