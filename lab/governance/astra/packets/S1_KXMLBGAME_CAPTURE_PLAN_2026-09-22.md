# S1 KXMLBGAME — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB (events empty; results/pnl null)  
**Stubbed_at:** `2026-09-22T23:02:43Z`  
**panel_version:** `2026-09-22.s1-kxmlbgame-v0`  
**Packet:** S1-KXMLBGAME-MEAS  
**Freeze:** `packets/S1_KXMLBGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha `58a0c20182a075ba339629f94451fb65b7876d635ecdd51338d1c2dd852279c5`  
**Owners:** Collector (panel/capture) → Simulator (units/markout harness) → Examiner (Kalshi)  
**Hard rules:** No live orders · no invented PnL · no Q7 fee literals · **no ADMIT-1 / PIT@CLE budget steal**

## Paths
| Role | Path |
|---|---|
| Panel schema | `lab/governance/astra/registry/schemas/s1_kxmlbgame_panel.schema.json` |
| Panel stub (empty events) | `lab/governance/astra/packets/S1_KXMLBGAME_PANEL_STUB_2026-09-22.json` |
| Capture slot (idle) | `lab/astra-capture/s1-kxmlbgame/` |
| Freeze kernel | `lab/governance/astra/packets/S1_KXMLBGAME_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| Scout bundle | `lab/governance/astra/packets/scout_s1_kxmlbgame/` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` · formula `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Kickoff SoT | Kalshi `occurrence_datetime` / market close — **not** NFL holdout +3h |

## Panel design
1. **Series:** `KXMLBGAME` only (MLB game moneyline binaries).  
2. **Cohort:** bounded **same-day or next-day** slate at admit time — no backfill of started windows.  
3. **panel_version:** `2026-09-22.s1-kxmlbgame-v0` (Conductor-directed).  
4. **Events:** empty in this stub; fill only on future admit with public listing match (`GET .../events?series_ticker=KXMLBGAME`).  
5. **SoT fields on each event (when admitted):** align R2-P5 kickoff block where applicable (`kalshi_occurrence_datetime`, `sot_pin`, `window_clock_source=kalshi_occurrence`); `t_minus_7d_utc` optional for daily MLB.  
6. **Not stored in panel:** scores, settlements, prices, invented depth.

## GET-only capture plan (future recorder — not started)
| Item | Plan |
|---|---|
| Host | `api.elections.kalshi.com` public GETs only |
| Routes | events listing (admit-time only), event metadata, market orderbook, public trades |
| DB | `lab/astra-capture/s1-kxmlbgame/capture.sqlite` (new; never ADMIT-1 DB) |
| PID namespace | `s1-kxmlbgame` — separate from ADMIT-1 pid **852286** |
| Interval | TBD at admit; default candidate 30–60s **only if** ADMIT-1 budget uncontended |
| Freshness | R1-P5 `content_fresh_flag` from content/transaction time — not WS ping |
| Fee on any hypothetical fill | R1-P1 `order_fee` only — refuse completed-profit label without fee channel |
| Markout horizons | Simulator factorial later: {1m, 5m, 15m} with feebook+rails fixed |

## Schedule vs C1 / ADMIT-1
- **Now:** schema + empty panel stub only. No second recorder.  
- **Admit/live poll:** only after Conductor greenlight **and** when it does not contend with PIT@CLE T−7d ADMIT-1 coverage.  
- Prefer off-peak vs ADMIT-1 pulse; never share the ADMIT-1 process or SQLite.

## Explicit non-owns
- No Q6-`000` retune · no Q7 reopen · no capital A-arms · no external-odds bot (R1-P3 optional later)  
- No expansion to KXNCAAFGAME / KXMVENFL*  
- results/pnl remain null until Examiner run

## Simulator handoff
Panel schema stub is on disk — units/markout harness may start against freeze pins above. Empty `events[]` / null results are expected until admit.
