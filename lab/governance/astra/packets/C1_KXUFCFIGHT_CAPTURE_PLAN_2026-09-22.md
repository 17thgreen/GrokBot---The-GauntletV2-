# C1 KXUFCFIGHT — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (`admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-23T00:33:00Z` (~2026-09-22 20:33:00 EDT)  
**panel_version:** `2026-09-22.c1-kxufcfight-v0`  
**Packet:** C1-KXUFCFIGHT-MEAS  
**Freeze:** `packets/C1_KXUFCFIGHT_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `a191c9b3f71030445d1d32684feb6dc1bf09abb7e09403d5dbdf1927eafc63c9`  
**Scout COLLECTOR_STUB:** `packets/scout_c1_kxufcfight/COLLECTOR_STUB.md`  
**Owners:** Collector → Simulator → Examiner  
**Hard rules:** GET-only · no live orders · no invented PnL/OI/volume · no Q6-`000` retune · shared $5k = **label only** · **no ADMIT-1 steal** · **do not run admit.py**

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/c1_kxufcfight_panel.schema.json` |
| Panel stub | `lab/governance/astra/packets/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json` |
| Capture slot | `lab/astra-capture/c1-kxufcfight/` |
| Live GET | `lab/governance/astra/packets/scout_c1_kxufcfight/live_get_2026-09-22/` |
| STATUS | `lab/governance/astra/reports/STATUS_C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.md` |

## Binds
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` — live `fee_type=quadratic` / mult **1** |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Bakeoff capital | **$5k label** — measurement contrast only |

## Live resolve (this stub)
| Surface | Result |
|---|---|
| `GET /series/KXUFCFIGHT` | **429** then retry **200** Sports / UFC Fight / quadratic/1 |
| `GET /markets/…CONGUA-GUA|CON` | **200** — status **finalized** (settled fight) |
| `GET /markets/…DEGMOR-MOR|DEG` | **200** — status **active** |
| `GET /markets/…ORTDAS-ORT` | **429** x2 — event dropped |
| `GET /markets/…ORTDAS-DAS` | **200** but unpaired — dropped |
| `GET /markets?status=open&series=KXUFCFIGHT&limit=6` | **429** |

## Seed cohort
| Slice | N | Notes |
|---|---|---|
| series | **1** | KXUFCFIGHT |
| events | **2** | CONGUA (finalized) + DEGMOR (active) |
| markets | **4** | YES/NO pairs |
| dropped | **2** | ORTDAS honest shrink |

## Out of scope
- admit.py / ADMIT-1 recorder / live orders  
- Invented OI / PnL / volume  
- Q6-`000` retune / combat MM strategy port  

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS. `admitted_at` null until Clock.
