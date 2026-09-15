# Line desk config (Week 0)

Status: **PENDING PROVISION** — Conductor default locked; Switchboard does not purchase.

| Field | Value | Notes |
|---|---|---|
| Dedicated DID | _unset_ | Always forward to producer cell |
| Producer cell | _unset_ | State Farm partner |
| Forward mode | always | Never park on voicemail without SMS path |
| Missed-call SMS | **HOLD** | Instant Response OFF until (1) DID live + forward tested and (2) Conductor-approved SMS copy |
| Recommended provider | **Grasshopper True Solo** (~$16–22/mo all-in) | Conductor default 2026-09-15 |
| Backup provider | Quo Business (formerly OpenPhone) (~$25–36/mo) | External forward needs Business+ |
| Phone / SMS provider | _unset until Logan/producer provision_ | Switchboard does not buy |
| Token sheet handoff | from The Drop, day-of drop | token ↔ Radar ID ↔ list |
| Inbound log path | `almanac-fleet/switchboard/INBOUND_LOG.md` | Mirror to shared sheet when ready |

## Blockers to go-live
1. Logan/producer provision Grasshopper True Solo (GA local DID)
2. Forward to producer cell verified with a test call
3. Conductor-approved missed-call SMS text on file — then Instant Response
4. A2P/10DLC started (SMS deliverability)
5. Token sheet from Drop before first mail lands

## Research
Full comparison: `/workspace/lab/governance/almanac-fleet/DID_OPTIONS_2026-09-15.md`
