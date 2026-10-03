# R2-P3 Panel Stub STATUS — 2026-09-22

**Status:** revised stub complete; not admitted. `admitted_at` remains `null`; `volume`, `volume_fp`, `volume_24h_fp`, and `open_interest_fp` remain `null`.

## Freeze and packet
- Packet ID: `R2-P3-KXNFLPASSYDS-MEAS`
- Freeze: `/workspace/lab/governance/astra/packets/R2-P3_KXNFLPASSYDS_MEASUREMENT_FREEZE_KERNEL_2026-09-22.md`
- Freeze SHA-256: `a30108f658359590e170c73ea00d1a1f0852d5751cb15c9f2a9c6389f4dd3eaa` (verified with `sha256sum`)
- Frozen scout packet: `/workspace/lab/governance/astra/packets/scout_r2p3_kxnflpassyds/FROZEN_EXPERIMENT.json` (contains the same packet hash)

## Public GET resolution
Host: `https://api.elections.kalshi.com/trade-api/v2/`; GET-only. Required series order was used: PASSYDS → wait ≥45s → RECYDS → wait ≥45s → RSHYDS.

All live ticker/event-listing attempts were rate-limited; no API confirmation or spelling delta was available. The six frozen scout event tickers are retained, and `occurrence_source` remains `scout_packet`.

| Series | Route | HTTP | Response time (ET) | Result |
|---|---|---:|---|---|
| KXNFLPASSYDS | `/markets?series_ticker=KXNFLPASSYDS&status=open` | 429 | 19:43:53 | live unresolved; scout retained |
| KXNFLRECYDS | `/markets?series_ticker=KXNFLRECYDS&status=open` | 429 | 19:44:48 | live unresolved; scout retained |
| KXNFLRSHYDS | `/markets?series_ticker=KXNFLRSHYDS&status=open` | 429 | 19:45:38 | live unresolved; scout retained |
| KXNFLPASSYDS | `/events?series_ticker=KXNFLPASSYDS&status=open` | 429 | 19:46:31 | live unresolved; scout retained |
| KXNFLRECYDS | `/events?series_ticker=KXNFLRECYDS&status=open` | 429 | 19:47:51 | live unresolved; scout retained |
| KXNFLRSHYDS | `/events?series_ticker=KXNFLRSHYDS&status=open` | 429 | 19:48:41 | live unresolved; scout retained |

Retained six event tickers:
- `KXNFLPASSYDS-26SEP27LACBUF` — LAC@BUF — `2026-09-27T20:00:00Z` (`2026-09-27 16:00 ET`)
- `KXNFLRECYDS-26SEP27LACBUF` — LAC@BUF — `2026-09-27T20:00:00Z` (`2026-09-27 16:00 ET`)
- `KXNFLRSHYDS-26SEP27LACBUF` — LAC@BUF — `2026-09-27T20:00:00Z` (`2026-09-27 16:00 ET`)
- `KXNFLPASSYDS-26SEP27BALDAL` — BAL@DAL — `2026-09-27T23:25:00Z` (`2026-09-27 19:25 ET`)
- `KXNFLRECYDS-26SEP27BALDAL` — BAL@DAL — `2026-09-27T23:25:00Z` (`2026-09-27 19:25 ET`)
- `KXNFLRSHYDS-26SEP27BALDAL` — BAL@DAL — `2026-09-27T23:25:00Z` (`2026-09-27 19:25 ET`)

No ATL@GB event was admitted or placed in the panel. No raw volume was obtained; panel volume fields remain null.

## Gate and isolation
- T−7d gate: **REFUSE_PAST_TMINUS7D**. LACBUF T−7d was `2026-09-20T20:00:00Z`; BALDAL T−7d was `2026-09-20T23:25:00Z`; both are past. No backfill.
- `admitted_at`: `null`; `admit.py` was not run.
- ADMIT-1: untouched. Nothing under `/workspace/lab/astra-capture/prospective/` was killed, restarted, or modified; no poll budget was taken.
- Capture slot `/workspace/lab/astra-capture/r2-p3-prop-slate/` remains idle.

## Artifact paths
- Panel: `/workspace/lab/governance/astra/packets/R2_P3_PROP_SLATE_PANEL_STUB_2026-09-22.json`
- Schema: `/workspace/lab/governance/astra/registry/schemas/r2_p3_prop_slate_panel.schema.json`
- Capture plan: `/workspace/lab/governance/astra/packets/R2_P3_PROP_SLATE_CAPTURE_PLAN_2026-09-22.md`
- Capture README: `/workspace/lab/astra-capture/r2-p3-prop-slate/README.md`
- Raw GET evidence: `/workspace/lab/governance/astra/packets/r2p3_live_get_2026-09-22/`
- This STATUS: `/workspace/lab/governance/astra/packets/R2_P3_PANEL_STUB_STATUS_2026-09-22.md`

**ADMIT-1 prospective recorder:** untouched.
