# R2-P3 Prop Slate — Panel design + GET-only capture plan

**Status:** PANEL_SCHEMA_STUB_SEED · LIVE_GET_ATTEMPTED_RATE_LIMITED (6 events retained; `admitted_at` null; results/pnl/volume null)  
**Stubbed_at:** `2026-09-22T23:42:45Z`  
**panel_version:** `2026-09-22.r2-p3-prop-slate-v0`  
**Packet:** R2-P3-KXNFLPASSYDS-MEAS  
**Scout/frozen experiment:** `/workspace/lab/governance/astra/packets/scout_r2p3_kxnflpassyds/FROZEN_EXPERIMENT.json`
**Freeze:** `/workspace/lab/governance/astra/packets/R2-P3_KXNFLPASSYDS_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` · sha256 `a30108f658359590e170c73ea00d1a1f0852d5751cb15c9f2a9c6389f4dd3eaa`  
**Owners:** Collector (panel/capture) → Clock (join) → Conductor greenlight → admit.py (later)  
**Hard rules:** No live orders · no invented volume/PnL · no Q7 fee literals · **no ADMIT-1 / PIT@CLE budget steal** · **do not run admit.py yet**

## Paths
| Role | Path |
|---|---|
| Panel schema | `/workspace/lab/governance/astra/registry/schemas/r2_p3_prop_slate_panel.schema.json` |
| Panel stub (seeded, not admitted) | `/workspace/lab/governance/astra/packets/R2_P3_PROP_SLATE_PANEL_STUB_2026-09-22.json` |
| Capture slot (idle) | `/workspace/lab/astra-capture/r2-p3-prop-slate/` |
| Frozen scout packet | `/workspace/lab/governance/astra/packets/scout_r2p3_kxnflpassyds/FROZEN_EXPERIMENT.json` |
| Freeze kernel | `/workspace/lab/governance/astra/packets/R2-P3_KXNFLPASSYDS_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md` |
| STATUS | `/workspace/lab/governance/astra/packets/R2_P3_PANEL_STUB_STATUS_2026-09-22.md` |

## Binds (mandatory)
| Dep | Pin |
|---|---|
| R1-P1 feebook | `kalshi_feebook_lab_20260922` @ `22371178cb2663250b4762f328069571c48cb551` · formula `astra.r1p1.feebook.claude_order_level_ceil.v1` |
| R1-P5 rails | `kalshi_rails_lab_20260922` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` |
| Kickoff SoT | Kalshi `occurrence_datetime` (scout packet) |
| R2-P5 fields | `astra.registry.r2_p5_admit_fields.v1` kickoff block |

## Panel design
1. **Series:** `KXNFLPASSYDS` (kernel) + siblings `KXNFLRECYDS` / `KXNFLRSHYDS`.  
2. **Games:** Sun 2026-09-27 **LAC@BUF** + **BAL@DAL** (6 events).  
3. **panel_version:** `2026-09-22.r2-p3-prop-slate-v0`.  
4. **Events:** seeded with tickers + `kalshi_occurrence_datetime` + `t_minus_7d_utc` + `window_clock_source=kalshi_occurrence` + `sot_pin`; **`admitted_at` null**.  
5. **Volume:** null/absent — do not copy scout OI/vol as admitted facts.  
6. **Excluded:** ATL@GB (too late).  

## Live GET resolution and freeze delta

Public GET-only attempts were made against `https://api.elections.kalshi.com/trade-api/v2/` in the required order (PASSYDS, wait ≥45s, RECYDS, wait ≥45s, RSHYDS). All three open-markets requests and all three open-events listing requests returned **HTTP 429**. Therefore live event ticker/occurrence confirmation is unconfirmed; the six frozen scout tickers and occurrence values are retained with `occurrence_source = scout_packet`. No raw volume was obtained and all panel volume fields remain null.

## Kickoff / T−7d (occurrence_source = scout_packet; API rate-limited)
| Game | Kickoff ET | occurrence_utc | t_minus_7d_utc | Past at stub? |
|---|---|---|---|---|
| LAC@BUF | 2026-09-27 16:00 ET | `2026-09-27T20:00:00Z` | `2026-09-20T20:00:00Z` | **YES** |
| BAL@DAL | 2026-09-27 19:25 ET | `2026-09-27T23:25:00Z` | `2026-09-20T23:25:00Z` | **YES** |

**Admit gate:** honor admit.py — real UTC; refuse past T−7d; never backfill. Live admit would hit **REFUSE_PAST_TMINUS7D** under current clock. Stub waits for Clock join + Conductor disposition. **Do not backfill. Do not run admit.py in this pass.**

## Event tickers (frozen scout retained; live API unconfirmed)
1. `KXNFLPASSYDS-26SEP27LACBUF`
2. `KXNFLRECYDS-26SEP27LACBUF`
3. `KXNFLRSHYDS-26SEP27LACBUF`
4. `KXNFLPASSYDS-26SEP27BALDAL`
5. `KXNFLRECYDS-26SEP27BALDAL`
6. `KXNFLRSHYDS-26SEP27BALDAL`

## GET-only capture plan (future recorder — not started)
| Item | Plan |
|---|---|
| Host | `api.elections.kalshi.com` public GETs only |
| Routes | markets listing by series, event metadata, orderbook, public trades |
| DB | `lab/astra-capture/r2-p3-prop-slate/capture.sqlite` (new; never ADMIT-1 DB) |
| PID namespace | `r2-p3-prop-slate` — separate from ADMIT-1 |
| Interval | TBD at admit; throttle ≥45–90s between series; only if ADMIT-1 budget uncontended |
| Start rule | Clock join + Conductor greenlight + admit.py accept (T−7d not past) |

## Schedule vs ADMIT-1
- **Now:** schema + seeded panel stub + idle slot only. No recorder. No poll.  
- **Admit/live poll:** only after Clock join + Conductor greenlight **and** when it does not contend with PIT@CLE T−7d ADMIT-1 coverage.  
- Never share the ADMIT-1 process or SQLite under `lab/astra-capture/prospective/`.

## Explicit non-owns
- No Q6-`000` retune · no Q7 reopen · no capital A-arms  
- No ATL@GB · no ANYTD until 429 clears  
- results/pnl/volume remain null until Examiner / live sample
