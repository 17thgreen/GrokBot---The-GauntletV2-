# SCOUT — House fee terms sourcing (for FEE-ACCT ADDENDUM_02)

- **Seat:** Market Scout
- **Written:** 2026-09-24 21:41:54 EDT / 2026-09-25T01:41:54Z
- **Mode:** READ-ONLY. No orders. New files only (RULE-FROZEN-EDIT: no rewrite of prior briefs/manifest).
- **Feeds:** `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_02.json` gap `HOUSE_FEE_MISSING` (still DRAFT_NOT_ADOPTED). Archivist can copy fields below into ADDENDUM_02 / a later addendum. **This Scout brief does not edit the registry.**
- **Packet:** `packets/scout_house_fee_2026-09-24/` (+ `MANIFEST.sha256`)

## Answer (published schedule → House)

| Field | Value | Source |
|---|---|---|
| **Taker rate** | **0.07** (in formula `M × 0.07 × C × P × (1−P)`) | PDF `kalshi.com/docs/kalshi-fee-schedule.pdf` |
| **Maker rate** | **0.0175** when maker fees apply; **default maker multiplier M = 0** (no maker fee) unless the series is listed under Maker/Non-Standard | same PDF |
| **Multiplier M** | **1** (taker default) for House — not in Non-Standard table | PDF + API `fee_multiplier: 1` |
| **Fee type (API)** | `quadratic` | GET `/series/{ticker}` |
| **Cap** | **None stated** for trading fees beyond rounding (“fee + positionCost … to a centicent”). Deposit card fee max 2% is unrelated. | PDF |
| **Effective date** | **July 7, 2026** (“Last updated and effective: July 7, 2026”) | PDF footer (every page checked) |
| **Upcoming changes** | Web UI: “No upcoming fee changes scheduled.” API `/series/fee_changes` → `{"series_fee_change_arr":[]}` | browser + API |
| **Applies to** | All event-contract markets **not** listed in Non-Standard Fees — including **KXHOUSERACE** and older House district series (see ticker lists). HOUSE tickers are **absent** from the Non-Standard list (0 matches). | PDF §Trading Fees; nonstandard API search |

### Doc-quoted formula (verbatim)
From PDF page 1 (sha256 of PDF body `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601`):

> Trading fees are charged as a variable percentage fee of the expected earnings on an individual contract… The current general fee charged for a trade in dollars is given by the following formula:
>
> `fees = round up(M x 0.07 x C x P x (1-P))`
>
> P = the price of a contract in dollars (50 cents is 0.5)
> C = the number of contracts being traded
> M = the multiplier for each contract (default is 1 unless otherwise indicated)
> round up = rounds up such that the fee + positionCost is rounded to a centicent
>
> Maker Fees
> `fees = round up(M x 0.0175 x C x P x (1-P))`
> M = the multiplier for each contract (**default is 0** unless otherwise indicated)

Web UI “Most markets” (Predictions tab): Fee multiplier **1**, Fee range (100 contracts) **$0.07 – $1.75** taker fees — consistent with the formula at P→0 and P=0.5.

### Scout arithmetic (labeled; not a doc quote)
At M=1, C=1, P=0.50: taker fee = 0.07×1×0.5×0.5 = **$0.0175** (1.75¢). For C=100: **$1.75**. Maker with default M=0: **$0**. Maker if a series listed maker M=1: 0.0175×0.5×0.5 = **$0.004375** per contract before rounding.

## API cross-check
| Series | fee_type | fee_multiplier | GET |
|---|---|---|---|
| KXHOUSERACE | quadratic | 1 | 200 @ 21:41:08 ET |
| KXHOUSE | quadratic | 1 | 200 |
| HOUSE | quadratic | 1 | 200 |
| HOUSECA47 (legacy district) | quadratic | 1 | 200 |
| KXHOUSEUT01 | quadratic | 1 | 200 |
| CONTROLH | quadratic | 1 | 200 |

All **311** Politics/Elections series matching a loose House filter share `fee_type=quadratic`, `fee_multiplier=1` (`raw/kalshi/house_series_fee_fields.csv`).

**HOUSE\* / KXHOUSE\* tickers (100):** `raw/kalshi/HOUSE_and_KXHOUSE_tickers.txt` (includes KXHOUSERACE, KXHOUSE, HOUSE, legacy `HOUSECA47`-style districts, `KXHOUSEUT01`-style).

**vs R1-P1 feebook:** stub has no House overrides → `default_unknown_series` = taker 0.07×p(1−p), M=1. **Published schedule agrees** with that default for House (not a special carve-out). Gap for ADDENDUM_02 is filled by citing this PDF + API, not by inventing a different rate.

## Fetch evidence
| Artifact | URL | fetch_time_ET | fetch_time_UTC | HTTP | sha256 |
|---|---|---|---|---|---|
| **Fee schedule PDF** | https://kalshi.com/docs/kalshi-fee-schedule.pdf | 2026-09-24 21:40:xx EDT (browser download) | 2026-09-25T01:40:xxZ | **200** (browser); curl/Python/fresh Chromium **429** checkpoint | `c326a69f596a11e8f8be2620402d39a8d4823920c21cc97c93a114d862699601` |
| Fee schedule HTML (browser text) | https://kalshi.com/fee-schedule | ~21:39 EDT | ~01:39Z | 200 browser; curl 429 | see `fee_schedule_predictions_BROWSER.txt` |
| curl ERRORBODY | same URLs | 21:38:35 EDT | 2026-09-25T01:38:35Z | 429 | `fee_schedule_*_ERRORBODY_http429.html` (not data) |
|  Nonstandard series JSON (`raw/docs/nonstandard_fee_series.json`) | https://api.elections.kalshi.com/v1/search/series?fee_types=nonstandard&with_milestones=true | 21:38–21:39 EDT | 01:38–01:39Z | 200 | `558a4fa75516cc68b31568ca83aeb15e1b5f301c2696b32647315668e464c5be` |
| Fee changes | https://api.elections.kalshi.com/trade-api/v2/series/fee_changes | 21:41:30 EDT | 2026-09-25T01:41:30Z | 200 | `6780c8eb7edbb5e1ca3b15166f17cef054befacb2cc8f4bc479c54074a9a2c18` |
| Series lists Politics/Elections | `/series?category=` | 21:38:06–09 EDT | 01:38:06–09Z | 200 | Politics `09ae6ecb…`; Elections `551040a6…` |
| Help Fees | https://help.kalshi.com/trading/fees | 21:38:36 EDT | 01:38:36Z | 200 | points to website fee schedule; no numeric House carve-out |
| docs fee_rounding | https://docs.kalshi.com/getting_started/fee_rounding.md | 21:38:35 EDT | 01:38:35Z | 200 | rounding mechanics only |

## Still OPEN (do not invent)
- **Member-type** for the fee manifest (Logan/Conductor) — OPEN.
- Whether any *future* House listing will be moved into Non-Standard (none scheduled now).

## Blockers
- `kalshi.com/fee-schedule` and PDF: **429 Vercel checkpoint** for curl/unauthenticated Python/fresh headless Chromium. Worked via warmed box Playwright browser download. ERRORBODY files retained and labeled.
