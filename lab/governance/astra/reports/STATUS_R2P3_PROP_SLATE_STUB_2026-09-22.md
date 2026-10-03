# STATUS — R2-P3 Prop Slate T− panel stub (Collector)

**When:** 2026-09-22 ~19:42 ET (America/New_York) / `2026-09-22T23:42:45Z`  
**Seat:** Collector (Astra/Kalshi Collector Ops)  
**Action:** SCHEMA + seeded empty-admit panel stub ONLY. **admit.py not run.** No recorder/poll. No live orders.

## Landed
| Artifact | Absolute path |
|---|---|
| Schema | `/workspace/lab/governance/astra/registry/schemas/r2_p3_prop_slate_panel.schema.json` |
| Panel stub | `/workspace/lab/governance/astra/packets/R2_P3_PROP_SLATE_PANEL_STUB_2026-09-22.json` |
| Capture plan | `/workspace/lab/governance/astra/packets/R2_P3_PROP_SLATE_CAPTURE_PLAN_2026-09-22.md` |
| Idle capture slot | `/workspace/lab/astra-capture/r2-p3-prop-slate/` |
| Slot README | `/workspace/lab/astra-capture/r2-p3-prop-slate/README.md` |
| Slot panel copy | `/workspace/lab/astra-capture/r2-p3-prop-slate/panel_stub.json` |
| This STATUS | `/workspace/lab/governance/astra/reports/STATUS_R2P3_PROP_SLATE_STUB_2026-09-22.md` |

**panel_version:** `2026-09-22.r2-p3-prop-slate-v0`  
**admitted_at:** `null`  
**stub_status:** `PANEL_SCHEMA_STUB_SEED_NOT_ADMITTED`  
**occurrence_source:** `scout_packet` (not assumed ET; matches ET conversion)

## Events (6) + kickoff / T−7d
| Event | occurrence_utc | t_minus_7d_utc | Past at stub? |
|---|---|---|---|
| `KXNFLPASSYDS-26SEP27LACBUF` | `2026-09-27T20:00:00Z` | `2026-09-20T20:00:00Z` | YES |
| `KXNFLRECYDS-26SEP27LACBUF` | `2026-09-27T20:00:00Z` | `2026-09-20T20:00:00Z` | YES |
| `KXNFLRSHYDS-26SEP27LACBUF` | `2026-09-27T20:00:00Z` | `2026-09-20T20:00:00Z` | YES |
| `KXNFLPASSYDS-26SEP27BALDAL` | `2026-09-27T23:25:00Z` | `2026-09-20T23:25:00Z` | YES |
| `KXNFLRECYDS-26SEP27BALDAL` | `2026-09-27T23:25:00Z` | `2026-09-20T23:25:00Z` | YES |
| `KXNFLRSHYDS-26SEP27BALDAL` | `2026-09-27T23:25:00Z` | `2026-09-20T23:25:00Z` | YES |

ET labels (scout): LAC@BUF 16:00 ET · BAL@DAL 19:25 ET on 2026-09-27.

## Blockers / gates
- **REFUSE_PAST_TMINUS7D:** both games' T−7d already past as of stub (~2026-09-22T23:42Z). Live `admit.py` would refuse; **no backfill**. Wait Clock join + Conductor.
- ATL@GB explicitly excluded (late).
- No Kalshi private routes called; occurrence from scout packet.

## ADMIT-1
**Untouched.** No writes under `lab/astra-capture/prospective/`; no pid/DB/panel changes.

## Ping
Parent: SendToAgent with paths above when Clock/Conductor ready. Do not start recorder until greenlight.
