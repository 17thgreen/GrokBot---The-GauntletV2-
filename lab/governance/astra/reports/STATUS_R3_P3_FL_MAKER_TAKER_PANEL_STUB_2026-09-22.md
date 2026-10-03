# R3-P3 FL maker/taker bands Panel Stub STATUS — 2026-09-22

**Status:** stub complete; not admitted. `admitted_at` remains `null`. `results` / `pnl` / `volume` remain `null`. Measurement MZ / post-fee ROI by band / maker vs taker remain **null** until Examiner.

**Stubbed_at:** `2026-09-23T00:19:20Z` (`2026-09-22 20:19:20 EDT`)  
**panel_version:** `2026-09-22.r3-p3-fl-maker-taker-v0`

## Freeze and packet
- Packet ID: `R3-P3-FL-MAKER-TAKER`
- Freeze: `/workspace/lab/governance/astra/packets/R3-P3_FL_MAKER_TAKER_BANDS_FREEZE_KERNEL_2026-09-22.md`
- Freeze SHA-256: `0ed697149136acb3aa840aeeb79d11c8f6ef80f37ce4dd692a3cb690212206a7` (verified `sha256sum`)
- Collector stub: `/workspace/lab/governance/astra/packets/R3-P3_COLLECTOR_STUB_2026-09-22.md`
- C3 weather prefer: `/workspace/lab/governance/astra/packets/C3_KXHIGHNY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`
- Empty results: `/workspace/lab/governance/astra/packets/r3_p3_fl_maker_taker/results.json` → results/pnl **null**

## Series chosen (C3 weather first)
| Series | Category | Role |
|---|---|---|
| `KXHIGHNY` | Climate and Weather | primary first-panel |
| `KXHIGHCHI` | Climate and Weather | multi-city proof |
| `KXFEDDECISION` / `KXGDP` | Economics | series metadata only (settled list 429) |

**Avoided as first panel:** KXMLBGAME, KXNCAAFGAME, KXMVECROSSCATEGORY, KXNFLPASSYDS/RECYDS/RSHYDS.

## Sampled counts
| Object | N | Notes |
|---|---:|---|
| Series (panel) | 2 | NY + CHI |
| Events | 2 | `KXHIGHNY-26SEP22`, `KXHIGHCHI-26SEP22` |
| Markets | 3 | still `status=active`; result empty |
| Trades sampled | 15 | 5×3 weather tickers |
| Settled markets resolved | 0 | listing 429; no invented tickers |

Markets: `KXHIGHNY-26SEP22-B67.5`, `KXHIGHNY-26SEP22-T70`, `KXHIGHCHI-26SEP22-B64.5`.

## Native taker fields
**Present on all 15 sampled trades:** `taker_outcome_side`, `taker_book_side`, and deprecated `taker_side`.  
**Absent:** `taker_action` (not on Kalshi Trade schema — documented; not inferred).  
**Lee-Ready:** **REFUSED** (native fields present; no aggressor inference).

## Bands pre-registered (before outcome join)
`[0-0.10)`, `[0.10-0.20)`, `[0.20-0.30)`, `[0.30-0.40)`, `[0.40-0.50)`, `[0.50-0.60)`, `[0.60-0.70)`, `[0.70-0.80)`, `[0.80-0.90)`, `[0.90-1.00]`  
Registry: `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/bands_registry_10c.json` (registered_at `2026-09-23T00:12:45Z` before trade/outcome sampling).

## Pins
- R1-P1 `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` (fee channel for later ROI — **Collector did not compute ROI**)
- R1-P5 `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` (optional freshness)

## 429 notes (honest)
| Route | HTTP | ET |
|---|---:|---|
| `/series/KXHIGHNY` (first) | 429 | 20:13:00 EDT |
| `/markets?status=settled` Fed/GDP/CHI/NY (multiple) | 429 | 20:13:31–20:18:26 EDT |
| `/events?status=settled` NY/CHI | 429 | 20:15:33 / 20:15:59 EDT |

Full log: `packets/r3_p3_fl_maker_taker/live_get_2026-09-22/http_log.jsonl`.

## Gate and isolation
- `admitted_at`: **null**; `admit.py` **not** run.
- ADMIT-1 prospective/: **untouched** (sqlite mtime still `2026-09-22 17:21:53 EDT`; admission_log `17:18:13 EDT`).
- No recorder start; no orders; no R3-P2.
- Capture slot idle except stub artifacts + empty schema sqlite.

## Artifact paths (absolute)
- `/workspace/lab/governance/astra/packets/R3_P3_FL_MAKER_TAKER_PANEL_STUB_2026-09-22.json`
- `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/panel_stub.json`
- `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/bands_registry_10c.json`
- `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/capture.sqlite`
- `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/README.md`
- `/workspace/lab/governance/astra/registry/schemas/r3_p3_fl_maker_taker_panel.schema.json`
- `/workspace/lab/governance/astra/packets/R3_P3_FL_MAKER_TAKER_CAPTURE_PLAN_2026-09-22.md`
- `/workspace/lab/governance/astra/packets/r3_p3_fl_maker_taker/live_get_2026-09-22/`
- `/workspace/lab/governance/astra/reports/STATUS_R3_P3_FL_MAKER_TAKER_PANEL_STUB_2026-09-22.md`

**ADMIT-1 prospective recorder:** untouched.
