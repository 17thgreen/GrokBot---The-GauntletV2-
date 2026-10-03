# Archivist index: Sports Q6 screen ACCEPT + Variants Q6S5 kick — recorded 2026-09-25 00:04 ET

**CORRECTION:** supersedes prior same-path receipt `7595402ea76018e506ea54a133fc576ef6a7a9fac3389b71a5fc70fb5acedadf` (garbled paths/hashes). `_prev` saved.

## (1) CONDUCTOR_ACCEPT — sports / microstructure screen vs Q6-000
| field | value |
|---|---|
| path | `packets/CONDUCTOR_ACCEPT_SPORTS_Q6_SCREEN_2026-09-24.json` |
| sha256 | `2aefbc1712a0389d65f565439d5599a7275688e872e8bc67d5c6dde3b1cd81f8` (4367 B) |
| decision | `ACCEPT_SCREEN` |
| issued_at_et | `2026-09-25 00:02 ET` |
| freeze | `packets/scout_sports_q6_screen/FREEZE_SPORTS_Q6_SCREEN_2026-09-24.md` |
| freeze_sha256 | `552314d2822f86bf4127be5de03b8d64aa8c16d6c0c81887bdc0cfbd411571df` (9777 B; on-disk match [V]) |
| brief | `SCOUT_SPORTS_Q6_SCREEN_2026-09-24.md` |
| brief_sha256 | `fae1d7cb85279a900e20043da697ab189c77c7cf4f7131f8607b6310548f0047` (7406 B; on-disk match [V]) |
| cemetery_id | **null** (no cemetery this screen) |
| scoreboard | unchanged (`Q6-000 / Arm D KEEP +$345.24 / +6.90%`) |
| Card 06 | stays **CLOSED** (open-window differentiator; no Cap-SR/FQ/RFQ reopen) |

### Slot rulings (from ACCEPT)
| slot | series | rec | note |
|---|---|---|---|
| Q6S5 | `KXMLBSPREAD` | **TRY** | Distinct vs occupied S1 KXMLBGAME ML; strongest fee-channel stress this screen. |
| Q6S1 | `KXATPMATCH` | **TRY** | Inventory re-proof for existing ATP fee/queue + settled-join lane; bakeoff candidacy when settlements land. Not a new cash-cow C* re-nominate. |
| Q6S2 | `KXNHLGAME` | **TRY** | C2 reinforce/refine only; do not steal ADMIT-1; no new sibling freeze this wave. |
| Q6S4 | `KXBUNDESLIGAGAME` | **HOLD** | Structure live; oi≈12 too thin for bakeoff. UCL/EPL empty. |
| Q6S3 | `KXNFLANYTD` | **DEFER** | ANYTD/FIRSTTD 429; 2TD empty. No invented inventory. |

## (2) CONDUCTOR_KICK — Variants Q6S5 KXMLBSPREAD fee-queue freeze
| field | value |
|---|---|
| path | `packets/CONDUCTOR_KICK_VARIANTS_Q6S5_KXMLBSPREAD_FEEQUEUE_FREEZE_2026-09-25.json` |
| sha256 | `9c68ab12f6f5561ee176c5669b17ef40c4f5be20299687823ad7f0e9b67701c8` (1231 B) |
| id | `CONDUCTOR_KICK_VARIANTS_Q6S5_KXMLBSPREAD_FEEQUEUE_FREEZE` |
| decision | `FREEZE` |
| freeze_owner | `R&D Variants` |
| series | `KXMLBSPREAD` |
| packet_id | `Q6S5-KXMLBSPREAD-FEEQUEUE-HARNESS` |
| parent_accept | `packets/CONDUCTOR_ACCEPT_SPORTS_Q6_SCREEN_2026-09-24.json` |
| scout_freeze_sha256 | `552314d2822f86bf4127be5de03b8d64aa8c16d6c0c81887bdc0cfbd411571df` (= freeze [V]) |
| stamped_at_et | `2026-09-25T00:02:00-04:00` |
| kernel | On MLB spread (not S1 game-ML), do fee-honest fills + queue/freshness under quadratic×0.5 produce completed-net / unresolved-inventory stats that beat or stress Q6-000 under shared $5k bakeoff? |
| constraints | GET-only / no orders / no invent fills or PnL; freeze before implement; fee pin cache-labeled until live |

**Status:** both **INDEXED** (hashes re-verified on disk). No cemetery. No orders / no P&L. Card 01 KEEP / member_type gates untouched.
