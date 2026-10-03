# C3 KXHIGHNY (+CHI) — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED (`admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-23T00:26:30Z` (~2026-09-22 20:26:30 EDT)  
**panel_version:** `2026-09-22.c3-kxhighny-v0`  
**Packet:** C3-KXHIGHNY-MEAS  
**Freeze:** `packets/C3_KXHIGHNY_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `0e79a0194e2371efae8d8cac0f4f2ec9ce4cf53f60dd870bae1a1ed7acff3604`  
**Scout COLLECTOR_STUB:** `packets/scout_c3_kxhighny/COLLECTOR_STUB.md`  
**Empty results:** `packets/scout_c3_kxhighny/` (results/pnl **null** — FROZEN_NOT_RUN)  
**Owners:** Collector (panel/capture) → Simulator → Examiner  
**Hard rules:** GET-only · no live orders · no invented PnL/OI/volume · no Q6-`000` retune · no GitHub weather-spread EV as evidence · **no ADMIT-1 steal** · **do not run admit.py** · prefer as R3-P3 weather first-panel inventory (kernels distinct)

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/c3_kxhighny_panel.schema.json` |
| Panel stub | `lab/governance/astra/packets/C3_KXHIGHNY_PANEL_STUB_2026-09-22.json` |
| Capture slot | `lab/astra-capture/c3-kxhighny/` |
| Live GET | `lab/governance/astra/packets/scout_c3_kxhighny/live_get_2026-09-22/` |
| STATUS | `lab/governance/astra/reports/STATUS_C3_KXHIGHNY_PANEL_STUB_2026-09-22.md` |

## Binds
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` — live series `fee_type=quadratic` / mult **1** |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Structure | bordering-strike ladder — **hypothesis only** |

## Panel design
1. **Cohort:** Primary `KXHIGHNY`; multi-city proof `KXHIGHCHI`.
2. **panel_version:** `2026-09-22.c3-kxhighny-v0`.
3. **Seed:** bordering-strike + Scout samples via individual ticker GET (list 429 → shrink).
4. **SoT:** `occurrence_datetime` from live market GET (SEP22 → 2026-09-23 10:00 ET / 14:00Z).
5. **Measurement shells null:** reciprocal book; bordering ladder; fee channel; rails labels; multi-city proof join.
6. **Host:** `https://api.elections.kalshi.com/trade-api/v2` GET-only.

## Live resolve (this stub)
| Surface | Result |
|---|---|
| `GET /series/KXHIGHNY` | **200** Climate and Weather · fee quadratic/1 |
| `GET /series/KXHIGHCHI` | **200** Climate and Weather · fee quadratic/1 |
| `GET /markets/KXHIGHNY-26SEP22-*` (B67.5,T70,B65.5) | **200** active |
| `GET /markets/KXHIGHCHI-26SEP22-*` (B64.5,B66.5) | **200** active |
| `GET /markets/KXHIGHNY-26SEP23-B67.5` | **200** active |
| `GET /markets?status=open&series=KXHIGH*` limit=8 | **429** — seed not expanded |

## Seed cohort
| Slice | N | Notes |
|---|---|---|
| series | **2** | NY + CHI |
| events | **3** | SEP22 NY/CHI + SEP23 NY |
| markets | **6** | bordering + Scout samples |
| open list | **0** | 429 honest shrink |

## Out of scope
- admit.py / ADMIT-1 recorder  
- Live orders / signed host  
- Invented OI / PnL / volume / list inventory  
- Q6-`000` retune / weather-spread strategy port  

## Done =
Schema + seed panel stub + capture plan + idle slot + STATUS on disk. `admitted_at` null until Clock.
