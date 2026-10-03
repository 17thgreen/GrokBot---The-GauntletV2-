# STATUS — S4 KXNCAAFGAME football OOS panel stub (Collector)

**When:** 2026-09-22 ~19:49 ET (America/New_York) / `2026-09-22T23:49:34Z`  
**Seat:** Collector (Astra/Kalshi Collector Ops)  
**Action:** SCHEMA + seeded empty-admit panel stub ONLY. **admit.py not run.** No recorder/poll. No live orders. No invented volume.

## Landed
| Artifact | Absolute path |
|---|---|
| Schema | `/workspace/lab/governance/astra/registry/schemas/s4_kxncaafgame_panel.schema.json` |
| Panel stub | `/workspace/lab/governance/astra/packets/S4_KXNCAAFGAME_PANEL_STUB_2026-09-22.json` |
| Capture plan | `/workspace/lab/governance/astra/packets/S4_KXNCAAFGAME_CAPTURE_PLAN_2026-09-22.md` |
| Idle capture slot | `/workspace/lab/astra-capture/s4-kxncaafgame/` |
| Slot README | `/workspace/lab/astra-capture/s4-kxncaafgame/README.md` |
| Slot panel copy | `/workspace/lab/astra-capture/s4-kxncaafgame/panel_stub.json` |
| Live GET | `/workspace/lab/governance/astra/packets/s4_kxncaafgame_live_get_2026-09-22/` |
| Freeze (cited) | `/workspace/lab/governance/astra/packets/S4_KXNCAAFGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| This STATUS | `/workspace/lab/governance/astra/reports/STATUS_S4_KXNCAAFGAME_PANEL_STUB_2026-09-22.md` |

**panel_version:** `2026-09-22.s4-kxncaafgame-v0`  
**admitted_at:** `null`  
**stub_status:** `PANEL_SCHEMA_STUB_SEED_NOT_ADMITTED`  
**occurrence_source:** `kalshi_public_get`  
**freeze_packet_sha256:** `9e6556c150c726b679ac8393f1f5338cf983489259b0f34cdedf221c030be795`  
**football_oos_vs_000:** true · **not_kxnflgame_capacity:** true

## Fee / rails pins
| Pin | Value |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` |
| Fee shape | `maker_fees`/1 via feebook (live series `quadratic_with_maker_fees` / multiplier `1`) — **no Q7/Q6 literals** |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |

## Resolved cohort (bound = ticker `26SEP26` / Sat 2026-09-26)
- **Events:** 113  
- **Markets:** 226 (2 YES/NO per event)  
- **Live GET:** `2026-09-22T23:48:33Z` page1 open nested  
- **LSU:** `KXNCAAFGAME-26SEP26TXAMLSU` @ `2026-09-26T20:00:00Z` (2 mkts)  
- **MCNS:** `KXNCAAFGAME-26SEP26ETAMMCNS` @ `2026-09-27T02:00:00Z` (2 mkts)  
- **Volume/OI in panel:** all null (verify-only sidecar under live_get/; scout results stay null)

### Sample rows (full list in panel stub)
| Event | occurrence_utc | t_minus_7d_utc | mkts | Past? |
|---|---|---|---|---|
| `KXNCAAFGAME-26SEP26BUCKPITT` | `2026-09-26T19:00:00Z` | `2026-09-19T19:00:00Z` | 2 | YES |
| `KXNCAAFGAME-26SEP26TEXTENN` | `2026-09-26T19:00:00Z` | `2026-09-19T19:00:00Z` | 2 | YES |
| `KXNCAAFGAME-26SEP26MISSFLA` | `2026-09-26T20:00:00Z` | `2026-09-19T20:00:00Z` | 2 | YES |
| `KXNCAAFGAME-26SEP26TXAMLSU` | `2026-09-26T20:00:00Z` | `2026-09-19T20:00:00Z` | 2 | YES |
| `KXNCAAFGAME-26SEP26ETAMMCNS` | `2026-09-27T02:00:00Z` | `2026-09-20T02:00:00Z` | 2 | YES |
| `KXNCAAFGAME-26SEP26NAUMTST` | `2026-09-27T05:30:00Z` | `2026-09-20T05:30:00Z` | 2 | YES |

Full event ticker list + occurrence_datetime + market_tickers: see panel stub `events[]`.

## Blockers / gates
- **REFUSE_PAST_TMINUS7D:** all 113 events' T−7d already past as of stub (`2026-09-22T23:49:34Z`). Live `admit.py` would refuse; **no backfill**. Wait Clock join + Conductor.
- **admit.py not run** (`admit_py_run: false`).
- GET-only public; no private routes; no orders.

## ADMIT-1 / peer slots
**Untouched.** No writes under `lab/astra-capture/prospective/`; no S1 / R2-P3 / S5 recorder or poll changes. Separate idle slot only — **no poll steal**.

## Scout
`packets/scout_s4_kxncaafgame/FROZEN_EXPERIMENT.json` + `results.json` — **results/pnl remain null** (unchanged).

## Ping
Parent: paths above when Clock/Conductor ready. Do not start recorder until greenlight.
