# Archivist index: Scout House fee source packet (ADDENDUM_02) — recorded 2026-09-24T21:42:50-04:00

Scout brief only; Scout did not edit registry. Archivist indexes here.

## Artifacts
| path | sha256 | bytes |
|---|---|---|
| `SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md` | `02fb1de12c573c2330899562cd832b48bd024a1c9f0e3886f23e1be83751b8e8` | 6066 |
| `packets/scout_house_fee_2026-09-24/MANIFEST.sha256` | `fd2c7894bedbcf53126d7dc2eda5a4ea3164fa027a438ed12d9c42802717eb8f` | 2731 |
| `packets/scout_house_fee_2026-09-24/raw/docs/kalshi_fee_schedule.pdf` | `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601` | 281129 |

PDF fetch ~2026-09-24 21:40 EDT via Playwright (curl hit 429 ERRORBODY, labeled). URL kalshi.com/docs/kalshi-fee-schedule.pdf (effective July 7, 2026). PDF sha **matches** Scout cite `c326a69f…` [V].

## Terms (from Scout; not re-derived by Archivist)
- Taker: round_up(M × 0.07 × C × P × (1−P)), default M=1
- Maker: round_up(M × 0.0175 × C × P × (1−P)), default M=0
- House multiplier M=1; not in Non-Standard (0 HOUSE matches in PDF + API)
- Cap: none beyond centicent rounding
- API: KXHOUSERACE + sampled HOUSE*/KXHOUSE* → fee_type=quadratic, fee_multiplier=1
- Agrees with R1-P1 default 0.07·p(1−p) — **not** a House carve-out

## Still OPEN
- Member-type for fee manifest (Logan/Conductor)
- ADDENDUM_02 formal registry edit / Conductor ACK of sourcing (this is Scout brief + packet only)

## MANIFEST check
Verified path hashes: 27 OK; mismatches/missing: 0 (see Archivist note if any).

Ticker list lines (HOUSE_and_KXHOUSE): 100

**Status:** SOURCED_PACKET_INDEXED. Unblocks fee-parameter fill for House series pending member-type + Conductor ADDENDUM_02. No orders.
