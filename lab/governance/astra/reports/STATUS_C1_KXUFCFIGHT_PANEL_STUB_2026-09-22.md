# C1 KXUFCFIGHT Panel Stub STATUS — 2026-09-22

**Status:** stub complete; not admitted. `admitted_at` remains `null`. `results` / `pnl` / `volume` / OI remain `null`. Fee+queue honesty bakeoff objects remain **null** until Examiner.

**Stubbed_at:** `2026-09-23T00:33:00Z` (`2026-09-22 20:33:00 EDT`)  
**panel_version:** `2026-09-22.c1-kxufcfight-v0`

## Freeze and packet
- Packet ID: `C1-KXUFCFIGHT-MEAS`
- Freeze: `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`
- Freeze SHA-256: `a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9` (verified `sha256sum`)
- Collector stub: `/workspace/lab/governance/astra/packets/scout_c1_kxufcfight/COLLECTOR_STUB.md`

## Series
| Series | Category | Role | fee_type / mult |
|---|---|---|---|
| `KXUFCFIGHT` | Sports | UFC fight ML | quadratic / 1 |

## Sampled counts
| Object | N | Notes |
|---|---:|---|
| Series | 1 | |
| Events | 2 | CONGUA finalized + DEGMOR active |
| Markets | 4 | after honest shrink |
| Dropped | 2 | ORTDAS |

Markets: `KXUFCFIGHT-26SEP22CONGUA-GUA`, `KXUFCFIGHT-26SEP22CONGUA-CON`, `KXUFCFIGHT-26SEP22DEGMOR-MOR`, `KXUFCFIGHT-26SEP22DEGMOR-DEG`.

## Pins
- R1-P1 `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551`
- R1-P5 `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`
- Shared $5k bakeoff **label only**

## 429 notes (honest)
| Route | HTTP | Handling |
|---|---:|---|
| `/series/KXUFCFIGHT` (first) | 429 | retry → 200 |
| `/markets/…ORTDAS-ORT` | 429×2 | drop ORTDAS event |
| `/markets?series_ticker=KXUFCFIGHT&status=open&limit=6` | 429 | keep ticker seed |

## Gate and isolation
- `admitted_at`: **null**; `admit.py` **not** run.
- ADMIT-1 prospective/: **untouched** (sqlite mtime still `2026-09-22 17:21:53 EDT`; admission_log `17:18:13 EDT`).
- No recorder start; no orders.
- Capture slot idle except stub artifacts.

## Artifact paths (absolute)
- `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json`
- `/workspace/lab/astra-capture/c1-kxufcfight/panel_stub.json`
- `/workspace/lab/astra-capture/c1-kxufcfight/README.md`
- `/workspace/lab/governance/astra/registry/schemas/c1_kxufcfight_panel.schema.json`
- `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_CAPTURE_PLAN_2026-09-22.md`
- `/workspace/lab/governance/astra/packets/scout_c1_kxufcfight/live_get_2026-09-22/`
- `/workspace/lab/governance/astra/reports/STATUS_C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.md`

**ADMIT-1 prospective recorder:** untouched.
