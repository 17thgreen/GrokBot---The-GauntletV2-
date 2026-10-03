# STATUS — S5 KXMVECROSSCATEGORY panel stub LAND 2026-09-22

**Seat:** Collector (Astra/Kalshi)  
**Stubbed_at:** `2026-09-22T23:56:34Z` UTC  
**panel_version:** `2026-09-22.s5-kxmvecrosscategory-v0`  
**Packet:** S5-KXMVECROSSCATEGORY-MEAS  
**Freeze sha256:** `a28932ba13b4913b69c48b73dde8ba066cebd212670d0b1cbb5ea8e93734b8ba`  
**ADMIT-1 prospective/:** **UNTOUCHED** (listing unchanged; no recorder/poll share)

## Absolute paths
| Artifact | Absolute path |
|---|---|
| Schema | `/workspace/lab/governance/astra/registry/schemas/s5_kxmvecrosscategory_panel.schema.json` |
| Panel stub | `/workspace/lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_PANEL_STUB_2026-09-22.json` |
| Capture plan | `/workspace/lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_CAPTURE_PLAN_2026-09-22.md` |
| Idle slot | `/workspace/lab/astra-capture/s5-kxmvecrosscategory/` |
| Idle README | `/workspace/lab/astra-capture/s5-kxmvecrosscategory/README.md` |
| Freeze | `/workspace/lab/governance/astra/packets/S5_KXMVECROSSCATEGORY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| Scout | `/workspace/lab/governance/astra/packets/scout_s5_kxmvecrosscategory/` |
| This STATUS | `/workspace/lab/governance/astra/reports/STATUS_S5_KXMVECROSSCATEGORY_PANEL_STUB_2026-09-22.md` |

## Cohort (seed vs open)
| Metric | Value |
|---|---|
| Markets seed N | **5** (bounded sample) |
| Open markets inventory | **≫200** (cursor on successful list; box list often 429) |
| Multivariate events seed M | **21** |
| MVE open lower bound | **≥800** (has_more=True) |
| Legs join rate (`mve_selected_legs`) | **5/5** |
| Collection join (`mve_collection_ticker`) | **5/5** |
| Sample tickers | `KXMVECROSSCATEGORY-S20264CF5F0166A4-D93D828F247` · `KXMVECROSSCATEGORY-S2026FFD15C7F85E-073CF08455C` · (+3 more) |
| Trades on seed | empty tape (HTTP 200, n=0) — **OK, not invented** |

## Fee / rails
- **fee_type confirmed:** `quadratic_with_combo_maker_fees` (live GET `/series/KXMVECROSSCATEGORY` + SHARD1 + KXMVESPORTSMULTIGAMEEXTENDED)  
- **fee_multiplier:** 1  
- **R1-P1:** `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551`  
- **R1-P5:** `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`  
- **Forbid** inherited Q7/Q6 fee literals  
- **Explicitly NOT R1-P4 strategy**

## Out of scope (noted)
- `/communications/rfqs` (401)  
- `is_block_trade` density (429)  
- Signed trading host  

## Gates
- `admitted_at`: **null**  
- admit.py: **not run** (WAIT_CLOCK_JOIN)  
- recorder/poll: **not started**  
- scout results/pnl: **null** (status=NOT_RUN; frozen results=None)  
- ADMIT-1 `prospective/`: untouched (14 entries present; not modified)

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS on disk. Ready for Clock join / Conductor ping.
