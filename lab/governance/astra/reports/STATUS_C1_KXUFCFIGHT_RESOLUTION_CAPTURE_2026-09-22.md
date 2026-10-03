# STATUS — C1 KXUFCFIGHT resolution capture (pre-admit)

**Seat:** Collector  
**At:** `2026-09-23T00:46:38Z`  
**panel_version:** `2026-09-22.c1-kxufcfight-v0`  
**clock_admit:** REFUSED · **admitted_at:** null  

## Action
Conductor: capture CONGUA resolution rows; do not stamp admit while waiting Clock re-join.

## Live GET refresh
| Ticker | status | result |
|---|---|---|
| KXUFCFIGHT-26SEP22CONGUA-GUA | finalized | yes |
| KXUFCFIGHT-26SEP22CONGUA-CON | finalized | no |
| KXUFCFIGHT-26SEP22DEGMOR-MOR | finalized | no |
| KXUFCFIGHT-26SEP22DEGMOR-DEG | finalized | yes |

**CONGUA settled N=2.** On refresh, **DEGMOR also finalized N=2** (Conductor note had DEGMOR still active — live now shows both legs finalized). Still **no admitted_at** until Clock re-joins.

## Paths
- Resolutions: `/workspace/lab/astra-capture/c1-kxufcfight/resolutions/CONGUA_resolution_rows_latest.json`
- Panel stub (updated, not admitted): `/workspace/lab/governance/astra/packets/C1_KXUFCFIGHT_PANEL_STUB_2026-09-22.json`
- Capture slot: `/workspace/lab/astra-capture/c1-kxufcfight/`
- Live GET: `/workspace/lab/governance/astra/packets/scout_c1_kxufcfight/live_get_2026-09-22/`

## Gates
- No admit.py · no recorder · no orders · ADMIT-1 untouched · volume/OI/pnl null on panel
