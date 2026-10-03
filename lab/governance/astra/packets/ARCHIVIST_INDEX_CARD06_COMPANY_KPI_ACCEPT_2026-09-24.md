# Archivist index: Card 06 company-KPI open-window ACCEPT — recorded 2026-09-24T23:47:30-04:00

## CONDUCTOR_ACCEPT
| field | value |
|---|---|
| path | `packets/CONDUCTOR_ACCEPT_CARD06_COMPANY_KPI_OPEN_WINDOW_2026-09-24.json` |
| sha256 | `53cba54a4f8866da82407b3be2e6d2b4dc3ccbf12944ded2924c55cd8d23e5f3` [V] |
| decision | `ACCEPT_MEASUREMENT` |
| issued_at_et | `2026-09-24 23:44 ET` |
| freeze_sha256 | `1413603c964fa8087ea396997e5ecb56c0b0a21e5b3d497629b6078d7fb4a1e8` [V] |
| freeze_path | `packets/scout_card06_company_kpi/FREEZE_CARD06_COMPANY_KPI_2026-09-24.md` |
| freeze_time_ET | `2026-09-24 21:41:48 EDT` |
| brief_sha256 | `78d53479462d7c3992678cb2652cf0d711f931f96d3c9daff8edaf5321b30eff` [V] |
| brief_path | `SCOUT_CARD06_COMPANY_KPI_OPEN_WINDOW_2026-09-24.md` |
| census_json_sha256 | `41271e8e233a76ee7fb2cae48353b0520da6882407b6bf4d5476dcd369174a41` [V] |
| census_path | `packets/scout_card06_company_kpi/out/census.json` |
| cemetery_id | **null** — no new cemetery |
| scoreboard_unchanged | `Q6-000 / Arm D KEEP +$345.24 / +6.90%` |

## Amendments (from ACCEPT; re-sha on disk)
| id | path | sha256 |
|---|---|---|
| A01 | `packets/scout_card06_company_kpi/AMENDMENT_01_2026-09-24.md` | `69d1c4ec685d4e801daba29162f6ca9e555ef868698935a571e04f51d30287d4` [V] |
| A02 | `packets/scout_card06_company_kpi/AMENDMENT_02_2026-09-24.md` | `3a19829dd9b7fd7e9127aa7ae326a07f6c754599e8d2acb16573cade9c922de2` [V] |

## Family verdicts summary (from ACCEPT; not invented)
| family | verdict | disposition |
|---|---|---|
| KXMETADAP | MIXED (8 sourced; 5 yes / 3 no; lt20) | **NO_BUILD** |
| KXCBVOLUME | MIXED (9 sourced; 7 yes / 2 no; lt20) | **NO_BUILD** |
| KXSPOTIFYSUBS | UNSOURCED (7 unsourced; partial) | **PARK** |
| KXNETFLIXSUBS | UNSOURCED (4 unsourced; partial) | **PARK** |
| KXNYTSUBS | UNSOURCED (7 unsourced; partial) | **PARK** |
| KXTESLA | (series_PARK; IR 403) | **PARK** (remains) |

### Headline
- **OPEN_WINDOW families:** none (zero)
- **MIXED → NO_BUILD:** KXMETADAP, KXCBVOLUME
- **UNSOURCED PARK:** KXSPOTIFYSUBS, KXNETFLIXSUBS, KXNYTSUBS
- **series PARK:** KXTESLA
- **cemetery_id:** null — **no new cemetery**
- Card 06 open-window differentiator lane **CLOSED** for this wave (macro CEM-006 + this census)
- decision `ACCEPT_MEASUREMENT`; scoreboard unchanged Q6-000

### Rulings (verbatim intent from ACCEPT)
- No OPEN-WINDOW family. No build / no P&L / no fills / no orders.
- MIXED Meta DAP + Coinbase volume = NO_BUILD (Conductor standing rule).
- Spotify/Netflix/NYT date-only IR → UNSOURCED PARK (not cemetery).
- KXTESLA remains PARK (IR 403).
- Lane CLOSED for this wave; do not retune or reopen without new evidence class.

**Status:** INDEXED. Freeze untouched. No cemetery written. No orders / no P&L invented.
