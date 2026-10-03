# C5 KXBTC15M Panel Stub STATUS — 2026-09-22

**Status:** stub complete; not admitted. `admitted_at` remains `null`. `results` / `pnl` / `volume` / OI remain `null`. Fee/queue honesty stress objects remain **null** until Examiner. **Not live crypto trading.**

**Stubbed_at:** `2026-09-23T00:39:30Z` (`2026-09-22 20:39:30 EDT`)  
**panel_version:** `2026-09-22.c5-kxbtc15m-v0`

## Freeze and packet
- Packet ID: `C5-KXBTC15M-MEAS`
- Freeze: `/workspace/lab/governance/astra/packets/C5_KXBTC15M_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`
- Freeze SHA-256: `4d1b72a38603de181e71f80b3cc6515b170a2bffe11f8770dac1296373e50263` (verified `sha256sum`)
- Collector stub: `/workspace/lab/governance/astra/packets/scout_c5_kxbtc15m/COLLECTOR_STUB.md`

## Series
| Series | Category | Role | fee_type / mult |
|---|---|---|---|
| `KXBTC15M` | Crypto | BTC 15m up/down rolling | quadratic / 1 |

## Sampled counts
| Object | N | Notes |
|---|---:|---|
| Series | 1 | |
| Events | 1 | `KXBTC15M-26SEP222045` |
| Markets | 1 | `KXBTC15M-26SEP222045-45` (live; freeze sample `-15` differed) |

## Pins
- R1-P1 `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551`
- R1-P5 `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac`

## 429 notes (honest)
| Route | HTTP | Handling |
|---|---:|---|
| `/markets/KXBTC15M-26SEP222015-15` | 429×2 | abandon guessed freeze suffix |
| `/markets/KXBTC15M-26SEP222045-45` | 429 | use open-list embedded market (list **200**) |

## Gate and isolation
- `admitted_at`: **null**; `admit.py` **not** run.
- ADMIT-1 prospective/: **untouched**.
- No recorder start; no orders; no live crypto trading.
- Capture slot idle except stub artifacts.

## Artifact paths (absolute)
- `/workspace/lab/governance/astra/packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json`
- `/workspace/lab/astra-capture/c5-kxbtc15m/panel_stub.json`
- `/workspace/lab/astra-capture/c5-kxbtc15m/README.md`
- `/workspace/lab/governance/astra/registry/schemas/c5_kxbtc15m_panel.schema.json`
- `/workspace/lab/governance/astra/packets/C5_KXBTC15M_CAPTURE_PLAN_2026-09-22.md`
- `/workspace/lab/governance/astra/packets/scout_c5_kxbtc15m/live_get_2026-09-22/`
- `/workspace/lab/governance/astra/reports/STATUS_C5_KXBTC15M_PANEL_STUB_2026-09-22.md`

**ADMIT-1 prospective recorder:** untouched.
