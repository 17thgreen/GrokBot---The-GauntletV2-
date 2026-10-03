# Archivist index: Card 06 open-window census ACCEPT + cemetery (recorded 2026-09-24T21:40:41-04:00)

## (1) CONDUCTOR_ACCEPT
| field | value |
|---|---|
| path | `packets/CONDUCTOR_ACCEPT_CARD06_OPEN_WINDOW_CENSUS_2026-09-24.json` |
| sha256 | `ebf6eb03aef7b75552d3d6f3e0b8723b130cca4614c917d9918c671e0f169cef` (4434 B) |
| decision | `ACCEPT_MEASUREMENT` |
| issued_at_et | `2026-09-24 21:38 ET` |
| freeze_sha256 | `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` (on-disk match [V]) |
| cemetery_id | `CEM-ASTRA-20260924-006` |
| scoreboard | unchanged (`Q6-000 / Arm D KEEP +$345.24 / +6.90%`) |

### Family disposition
- **CEMETERY (5):** KXJOBLESSCLAIMS, KXPCECORE, KXFEDDECISION, KXFED, KXEIACRUDEW → `CEM-ASTRA-20260924-006`
- **MIXED → NO_BUILD (not cemetery):** KXPAYROLLS, KXGDP
- **PARK:** KXTESLA (IR 403)
- **OPEN_WINDOW:** none

### Rulings (from ACCEPT)
- No OPEN-WINDOW family. No strategy build, no P&L, no fills, no orders from this card census.
- Cemetery five CEMETERY families under CEM-ASTRA-20260924-006 (sourced rows all close_before_arrival).
- MIXED (PAYROLLS, GDP): single YES rows are API close_time anomalies vs rules close language; freeze uses API close_time. Do NOT treat as tradeable open-window. NO_BUILD. Optional later anomaly audit only — not a measurement lane.
- KXTESLA UNSOURCED (IR 403). PARK; reopen only with official scheduled arrival evidence.
- CPI/CPIYOY remain CEM-ASTRA-20260924-003; excluded from this census.

## (2) Cemetery entry
| field | value |
|---|---|
| path | `cemetery/CEM-ASTRA-20260924-006_CARD06_MACRO_OPEN_WINDOW.md` |
| sha256 | `b57a819677e0f633462b021a329b25616806502dee4117286277203c9292545d` (2981 B) |
| CEM_ID | CEM-ASTRA-20260924-006 |
| class | CEMETERY_UP_FRONT / CLASS_FIT_POOR (close-before-source) |

**Status:** both **INDEXED**. Freeze untouched still holds. No orders / no P&L from this census.
