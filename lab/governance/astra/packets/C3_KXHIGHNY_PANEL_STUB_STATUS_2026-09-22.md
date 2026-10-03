# C3 KXHIGHNY (+CHI) Panel Stub STATUS — 2026-09-22

**Status:** stub complete; not admitted. `admitted_at` remains `null`. `results` / `pnl` / `volume` / OI remain `null`. Measurement objects remain **null** until Examiner.

**Stubbed_at:** `2026-09-23T00:26:30Z` (`2026-09-22 20:26:30 EDT`)  
**panel_version:** `2026-09-22.c3-kxhighny-v0`

## Freeze and packet
- Packet ID: `C3-KXHIGHNY-MEAS`
- Freeze: `/workspace/lab/governance/astra/packets/C3_KXHIGHNY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`
- Freeze SHA-256: `0e79a0194e2371efae8d8cac0f4f2ec9ce4cf53f60dd870bae1a1ed7acff3604` (verified `sha256sum`)
- Collector stub: `/workspace/lab/governance/astra/packets/scout_c3_kxhighny/COLLECTOR_STUB.md`
- Empty results: `/workspace/lab/governance/astra/packets/scout_c3_kxhighny/results.json` → results/pnl **null**

## Series
| Series | Category | Role | fee_type / mult |
|---|---|---|---|
| `KXHIGHNY` | Climate and Weather | primary | quadratic / 1 |
| `KXHIGHCHI` | Climate and Weather | multi-city proof | quadratic / 1 |

**R3-P3:** tagged `r3p3_weather_eligible=true` — panel material preference only; kernels distinct.

## Sampled counts
| Object | N | Notes |
|---|---:|---|
| Series | 2 | NY + CHI |
| Events | 3 | KXHIGHNY-26SEP22, KXHIGHCHI-26SEP22, KXHIGHNY-26SEP23 |
| Markets | 6 | individual ticker GET |
| Open list | 0 | 429 |

Markets: `KXHIGHNY-26SEP22-B67.5`, `KXHIGHNY-26SEP22-T70`, `KXHIGHNY-26SEP22-B65.5`, `KXHIGHCHI-26SEP22-B64.5`, `KXHIGHCHI-26SEP22-B66.5`, `KXHIGHNY-26SEP23-B67.5`.

## Pins
- R1-P1 `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551`
- R1-P5 `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`

## 429 notes (honest)
| Route | HTTP | Handling |
|---|---:|---|
| `/markets?series_ticker=KXHIGHNY&status=open&limit=8` | 429 | shrink to ticker GETs |
| `/markets?series_ticker=KXHIGHCHI&status=open&limit=8` | 429 | shrink to ticker GETs |

Full log: `packets/scout_c3_kxhighny/live_get_2026-09-22/http_log.jsonl`.

## Gate and isolation
- `admitted_at`: **null**; `admit.py` **not** run.
- ADMIT-1 prospective/: **untouched** (sqlite mtime still `2026-09-22 17:21:53 EDT`; admission_log `17:18:13 EDT`).
- No recorder start; no orders.
- Capture slot idle except stub artifacts.

## Artifact paths (absolute)
- `/workspace/lab/governance/astra/packets/C3_KXHIGHNY_PANEL_STUB_2026-09-22.json`
- `/workspace/lab/astra-capture/c3-kxhighny/panel_stub.json`
- `/workspace/lab/astra-capture/c3-kxhighny/README.md`
- `/workspace/lab/governance/astra/registry/schemas/c3_kxhighny_panel.schema.json`
- `/workspace/lab/governance/astra/packets/C3_KXHIGHNY_CAPTURE_PLAN_2026-09-22.md`
- `/workspace/lab/governance/astra/packets/scout_c3_kxhighny/live_get_2026-09-22/`
- `/workspace/lab/governance/astra/reports/STATUS_C3_KXHIGHNY_PANEL_STUB_2026-09-22.md`

**ADMIT-1 prospective recorder:** untouched.
