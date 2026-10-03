# Archivist stamp receipt: FEE ADDENDUM_02 House fee terms — 2026-09-24T23:47:00-04:00

## Edit (RULE-FROZEN-EDIT-PREV-BYTES-001)
| field | value |
|---|---|
| target | `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` |
| old sha256 | `eec516fc8ed8ea09634b24842c7ae4cf55fb8f5b40a81e50418213424139f7f9` |
| new sha256 | `44a69092461a94b259209b60c583166bf1ec56b322fc5dc9bf69f1b0fa2a9a12` |
| _prev path | `registry/_prev/eec516fc8ed8ea09634b24842c7ae4cf55fb8f5b40a81e50418213424139f7f9.FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` |
| _prev sha256 verified | `eec516fc8ed8ea09634b24842c7ae4cf55fb8f5b40a81e50418213424139f7f9` [V] |

## Authority
| artifact | sha256 |
|---|---|
| `packets/CONDUCTOR_KICK_ARCHIVIST_HOUSE_FEE_ADDENDUM_02_2026-09-24.json` | `0a5adcddc702af3e505e6c8b5dddacec44c93568e17b07da0267bfec49f93511` [V] |
| `SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md` | `02fb1de12c573c2330899562cd832b48bd024a1c9f0e3886f23e1be83751b8e8` [V] |
| prior index `packets/ARCHIVIST_INDEX_SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md` | `ae12a636d33441cac9d3ec3ee563010e7125d82d5c4cf3885a306527aa8da171` |
| PDF `packets/scout_house_fee_2026-09-24/raw/docs/kalshi_fee_schedule.pdf` | `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601` [V] (281129 B) |
| parent manifest `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.json` | `aa7658764061912073b8d9fc1f2ae03fc970fa382dca1c49335944be650552ba` [V] (unchanged; not edited) |

## Stamp outcome
- **status:** still `DRAFT_NOT_ADOPTED` (not claimed ADOPTED)
- **fee_terms_status:** `STAMPED_FROM_SCOUT`
- **gap HOUSE_FEE_MISSING:** **CLEARED** → gap now `MEMBER_TYPE_OPEN`
- **member_type:** null / **OPEN** (Logan/Conductor only; Archivist refused invent)
- **house_fee_terms:** taker 0.07; maker 0.0175; maker_default_M 0; fee_type quadratic; fee_multiplier 1; formulas as Scout; cap none beyond centicent; effective_date 2026-07-07; aligns_r1_p1_default true; house_carve_out false
- **series_affected:** KXHOUSERACE + HOUSE*/KXHOUSE* (100 tickers per Scout packet) — cited, not invented
- **Card 01 after-cost KEEP:** **NOT claimed.** Fee terms stamped; HOUSE_FEE_MISSING cleared; member_type still OPEN; KEEP still requires Conductor member_type + remaining gates.
- Parent fee manifest md/json left untouched (prefer; ADDENDUM_02 only).

**Refuse honored:** no invent member_type; no ADOPTED claim; no KEEP claim; no orders.
