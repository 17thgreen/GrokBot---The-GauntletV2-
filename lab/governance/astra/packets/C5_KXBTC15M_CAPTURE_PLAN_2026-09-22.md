# C5 KXBTC15M — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (`admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-23T00:39:30Z` (~2026-09-22 20:39:30 EDT)  
**panel_version:** `2026-09-22.c5-kxbtc15m-v0`  
**Packet:** C5-KXBTC15M-MEAS  
**Freeze:** `packets/C5_KXBTC15M_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `4d1b72a38603de181e71f80b3cc6515b170a2bffe11f8770dac1296373e50263`  
**Hard rule:** **15m crypto fee/queue honesty stress — NOT live crypto trading**  
**Owners:** Collector → Simulator → Examiner  

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/c5_kxbtc15m_panel.schema.json` |
| Panel stub | `lab/governance/astra/packets/C5_KXBTC15M_PANEL_STUB_2026-09-22.json` |
| Capture slot | `lab/astra-capture/c5-kxbtc15m/` |
| Live GET | `lab/governance/astra/packets/scout_c5_kxbtc15m/live_get_2026-09-22/` |
| STATUS | `lab/governance/astra/reports/STATUS_C5_KXBTC15M_PANEL_STUB_2026-09-22.md` |

## Binds
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` — live `fee_type=quadratic` / mult **1** |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |

## Live resolve (this stub)
| Surface | Result |
|---|---|
| `GET /series/KXBTC15M` | **200** Crypto · Bitcoin Price Up/Down · quadratic/1 |
| Guessed `…2015-15` / `…2000-15` | **404** / **429** — freeze sample spelling not trusted |
| `GET /markets?series_ticker=KXBTC15M&status=open&limit=4` | **200** → live ticker **`KXBTC15M-26SEP222045-45`** |
| `GET /markets/KXBTC15M-26SEP222045-45` | **429** — used list-embedded market object |

## Seed cohort
| Slice | N | Notes |
|---|---|---|
| series | **1** | KXBTC15M |
| events | **1** | `KXBTC15M-26SEP222045` |
| markets | **1** | current rolling window only |

## Out of scope
- Live crypto trading / signed orders / maker resting  
- bacchus-mm / kxeth15m strategy port  
- Silent backfill of expired windows  
- admit.py / ADMIT-1 recorder / Q6-`000` retune  

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS. `admitted_at` null until Clock.
