# S5 KXMVECROSSCATEGORY — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (bounded seed; `admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-22T23:56:34Z` (~ET desk 2026-09-22)  
**panel_version:** `2026-09-22.s5-kxmvecrosscategory-v0`  
**Packet:** S5-KXMVECROSSCATEGORY-MEAS  
**Freeze:** `packets/S5_KXMVECROSSCATEGORY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `a28932ba13b4913b69c48b73dde8ba066cebd212670d0b1cbb5ea8e93734b8ba`  
**Scout:** `packets/scout_s5_kxmvecrosscategory/` (results/pnl **null** — FROZEN_NOT_RUN)  
**Owners:** Collector (panel/capture) → Clock (join) → Conductor greenlight → admit.py (later) → Simulator (fill-vs-legs) → Examiner  
**Hard rules:** No live orders · no invented fills/PnL/OI · no Q7/Q6 fee literals · **no ADMIT-1 / PIT@CLE / S1 / R2-P3 / S4 budget steal** · **do not run admit.py yet** · **Explicitly NOT R1-P4 strategy** · RFQ/block out of scope

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/s5_kxmvecrosscategory_panel.schema.json` |
| Panel stub (seeded, not admitted) | `lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_PANEL_STUB_2026-09-22.json` |
| Capture slot (idle) | `lab/astra-capture/s5-kxmvecrosscategory/` |
| Freeze kernel | `lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| Scout bundle | `lab/governance/astra/packets/scout_s5_kxmvecrosscategory/` |
| STATUS | `lab/governance/astra/reports/STATUS_S5_KXMVECROSSCATEGORY_PANEL_STUB_2026-09-22.md` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` · formula `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| Fee shape | series override **`quadratic_with_combo_maker_fees`** / multiplier **1** (live GET confirmed on KXMVECROSSCATEGORY, SHARD1, KXMVESPORTSMULTIGAMEEXTENDED) — **forbid** Q7/Q6 literals |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Strategy kinship | Family only with R1-P4 — **measurement-access**, not RFQ strategy open |

## Panel design
1. **Series:** `KXMVECROSSCATEGORY*` (prefer over empty `KXMVENFL*`). Related fee-pin series: SHARD1, KXMVESPORTSMULTIGAMEEXTENDED when fee_type matches.  
2. **Cohort:** bounded **seed sample** vs open inventory ≫200 (document sample vs full).  
3. **panel_version:** `2026-09-22.s5-kxmvecrosscategory-v0`.  
4. **Markets:** seeded with ticker + `mve_selected_legs` + `mve_collection_ticker`; **`admitted_at` null**.  
5. **Events (MVE):** seed sample from `/events/multivariate` joined to market `event_ticker` where available.  
6. **Volume/OI:** null in panel — do not copy API zeros as admitted facts (zeros remain valid future observations).  
7. **Trades:** probe empty on seed tickers — empty tape OK; do not invent fills.

## Live resolve (this stub pass)
| Surface | Result |
|---|---|
| `GET /series/KXMVECROSSCATEGORY` | **200** · `fee_type=quadratic_with_combo_maker_fees` · multiplier 1 |
| `GET /series/KXMVECROSSCATEGORY-SHARD1` | **200** · same fee_type |
| `GET /series/KXMVESPORTSMULTIGAMEEXTENDED` | **200** · same fee_type |
| `GET /markets?series_ticker=...&status=open` (box) | **429** often — document; do not wait forever |
| `GET /markets` via alternate egress / WebFetch | **200** + cursor → open inventory ≫ page |
| `GET /markets/{ticker}` + `?event_ticker=` | **200** after cooldown — seed source |
| `GET /events/multivariate?series_ticker=KXMVECROSSCATEGORY` | **200** · ≥800 events sampled with has_more=True |
| `GET /markets/trades` on seed | **200** · empty tape (OK) |
| `/communications/rfqs` | **OUT OF SCOPE** (401) |
| `is_block_trade` filter | **OUT OF SCOPE** (429) |

### Seed cohort size
- **Markets N = 5** (bounded seed; full open ≫200)  
- **Events M = 21** (seed sample; MVE open ≥800+)  
- **Legs join rate = 5/5** (`mve_selected_legs` non-empty)  
- **Collection join = 5/5** (`mve_collection_ticker`)  
- **Sample tickers:** KXMVECROSSCATEGORY-S20264CF5F0166A4-D93D828F247, KXMVECROSSCATEGORY-S2026FFD15C7F85E-073CF08455C, KXMVECROSSCATEGORY-S2026FAFE350FA8F-2DEC47CF182, KXMVECROSSCATEGORY-S2026FAFE350FA8F-D22687ACA9C, KXMVECROSSCATEGORY-S2026FAFE350FA8F-20154DED5EC

## GET-only capture plan (future recorder — not started)
| Item | Plan |
|---|---|
| Host | `api.elections.kalshi.com` public GETs only |
| Routes | series fee metadata; markets by series/event/ticker; multivariate events; orderbook; public + historical trades |
| DB | `lab/astra-capture/s5-kxmvecrosscategory/capture.sqlite` (new; never ADMIT-1 DB) |
| PID namespace | `s5-kxmvecrosscategory` — separate from ADMIT-1 / S1 / R2-P3 / S4 |
| Interval | TBD at admit; throttle ≥60–120s; prefer event/ticker GETs when list 429s |
| Start rule | Clock join + Conductor greenlight + admit.py accept |
| Fee on residual | R1-P1 combo maker channel only — refuse completed-profit label without fee channel |
| Fills | Use tape when present; **null** when empty — never invent |

## Schedule vs ADMIT-1
- **Now:** schema + seeded panel stub + idle slot only. **No recorder. No poll.**  
- **Admit/live poll:** only after Clock join + Conductor greenlight **and** when it does not contend with PIT@CLE ADMIT-1 / S1 / R2-P3 / S4.  
- Never share the ADMIT-1 process or SQLite under `lab/astra-capture/prospective/`.

## Explicit non-owns
- No Q6-`000` retune · no Q7 reopen · no capital A-arms  
- No R1-P4 RFQ strategy open · no `/communications/rfqs` · no block-trade density claim  
- No expansion to empty `KXMVENFL*` preference flip without Scout re-confirm  
- results/pnl/volume remain null until Examiner / live admit sample  
- Scout `scout_s5_kxmvecrosscategory` results/pnl stay null
