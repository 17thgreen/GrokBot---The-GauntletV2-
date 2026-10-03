# Scout maximize delta — 2026-09-22

**Seat:** Market Scout (Astra / Kalshi)  
**Timestamp:** **2026-09-22 19:35 ET** (America/New_York, UTC−4)  
**Mode:** Continuous maximize · GET-only · no orders · no panel admits · no capital-structure  
**Prior:** `SCOUT_Q6_STRESS_KERNELS_2026-09-22.md` (S1–S5) · `SCOUT_BRIEF_2026-09-22.md`  
**Hosts used:** `https://api.elections.kalshi.com/trade-api/v2/` and `https://external-api.kalshi.com/trade-api/v2/` (docs-recommended; same public surface). `trading-api.kalshi.com` skipped (401).

**Kickoff SoT:** Kalshi `occurrence_datetime` (unchanged).

---

## 1. S5 RFQ / combo access check (R1-P4)

### What is public without auth

| Surface | Result | Notes |
|---|---|---|
| `/series` | **200** | MVE/combo/prepack/SGP series present (~75 name hits). No `KXRFQ*` series ticker. |
| Combo fee pin | **OK (metadata)** | `KXMVECROSSCATEGORY`, `KXMVECROSSCATEGORY-SHARD1`, `KXMVESPORTSMULTIGAMEEXTENDED` → `fee_type=quadratic_with_combo_maker_fees` / `fee_multiplier=1`. Independent NFL MVE (`KXMVENFLSINGLEGAME` / `MULTIGAME` / `EXTENDED`) → `quadratic` / 1 (not combo-maker). |
| `/markets` (default / MVE flood) | **200** | First open page = **200** `KXMVECROSSCATEGORY*` binaries with `mve_selected_legs` + `mve_collection_ticker`. Sampled page **volume_fp / volume_24h_fp / open_interest_fp all 0.00** — inventory exists; liquidity cues on that page = none. Cursor present → open inventory ≫ 200. |
| `/events/multivariate` | **200** | Returns combo events (e.g. `KXMVECROSSCATEGORY-SHARD1-*`); public. |
| `/markets/{ticker}/orderbook` | **200** | Empty book on zero-vol sample ticker. |
| `/markets/trades?ticker=` | **200** | Public (`security: []` in docs). Empty on zero-vol MVE sample; **non-empty** on liquid sports (PASSYDS / SPREAD) this pass. Field `is_block_trade` marks RFQ/negotiated block fills when present. |
| `/historical/trades` | **200** | Public historical tape (sample returned ATP / politics tickers; not MVE-specific). |

### What needs a key

| Surface | Result |
|---|---|
| `/communications/rfqs` | **401** live (`token_authentication_failure`). Docs: requires `KALSHI-ACCESS-*` headers. RFQ *objects* / quote stream = **read-only API key**, not public GET. |
| `/rfqs`, `/portfolio/rfqs` | **404** on elections/external hosts. |

### Independent-NFL combo inventory

| Series | Result |
|---|---|
| `KXMVENFLMULTIGAME` | **200** · `markets: []` (open) — still empty |
| `KXMVENFLSINGLEGAME` / `EXTENDED` / `KXNFLCOMBO` / prepacks | **429** this maximize pass after burst — structure exists in `/series`; open count **unconfirmed** this packet (prior brief already SKIP empty single-game) |

### Sample tickers (access proof only)

- MVE market: `KXMVECROSSCATEGORY-S20264CF5F0166A4-D93D828F247` (legs in title; vol/OI 0.00 this sample)
- MVE event (multivariate): `KXMVECROSSCATEGORY-SHARD1-S2026FF7C4259D33`
- Public trades worked on: `KXNFLPASSYDS-26SEP27BALDAL-DALDPRESCOTT4-275`, `KXNFLSPREAD-26SEP28PHICHI-PHI4`

### S5 verdict

**UPGRADE TRY**

**Reason:** Combo/MVE **market inventory + fill history** are accessible via public GET (markets, multivariate events, `/markets/trades`, `/historical/trades`) without auth. Combo fee schedule is visible on series metadata (`quadratic_with_combo_maker_fees`). That is enough for an R1-P4-family **fill-vs-independent-legs / fee-honest** measurement kernel on cross-category combo books.

**Still deferred (narrow):** live RFQ quote/object feed (`/communications/rfqs`) until Collector has a read-only key. Block-trade filter (`is_block_trade=true`) **429** this pass — do not claim RFQ-fill density until that query succeeds. Independent-NFL MVE open inventory remains empty/unconfirmed — prefer `KXMVECROSSCATEGORY*` (combo fee) over `KXMVENFL*` for first TRY.

---

## 2. Market delta vs S1–S5 (R1-P1 / R1-P5 honesty)

Liquidity figures = raw API `volume_fp` / `volume_24h_fp` / `open_interest_fp` only. Never invented.

| Slot | Prior | This pass | Action |
|---|---|---|---|
| **S1** `KXMLBGAME` | TRY | **200** — 90 open markets / 45 events; vol_sum ≈ 7.80e6, vol24 ≈ 6.92e6, oi ≈ 6.90e6 (page). Fee: `quadratic_with_maker_fees` / **0.5**. | **KEEP** — still strongest non-NFL daily binary for generalize-vs-`000`. |
| **S2** `KXNFLSPREAD` (+ TOTAL) | TRY after C1; listing was 429 | **SPREAD 200** — ≥20 markets / cursor; PHI@CHI alone vol_sum ≈ 2.31e5, oi ≈ 1.65e5 on first page (e.g. `…-PHI4` vol24 ≈ 1.68e5). **TOTAL 429** this pass. Fee: maker_fees / 1. | **KEEP** — inventory **confirmed**; strengthens stress-on-same-events case. Do not start capture until C1 PIT@CLE stable. |
| **S3** `KXNFLPASSYDS` | TRY | **200** — 30 markets / 2 events (`BALDAL`, `LACBUF`); vol/oi ≈ 1229; top ladder `DALDPRESCOTT4-275` vol24 ≈ 658. Public trades confirmed. Fee: `quadratic` / 1. | **KEEP** — modest tape but structure live; prefer next prop-rich slate after ATL@GB. |
| **S4** weather/politics placeholder | TRY when R1-P2 | `KXHIGHNY` **429** this pass. **`KXNCAAFGAME` listing CLEARED** — 20 mkts / 10 events first page; oi_sum ≈ 2.55e5 (dominated by MCNS/LSU); fee maker_fees / 1. | **REPLACE placeholder → `KXNCAAFGAME` TRY** (see below). |
| **S5** RFQ/combo | DEFER | Access check above | **UPGRADE TRY** (combo public path). |
| NHL / soccer / TOTAL / weather | blind / 429 | `KXNHLGAME`, `KXNFLTOTAL`, `KXHIGHNY` **429** after throttle | **No add** — cannot claim inventory. |

### Rank-order change to ≤5 list

**Changed (one slot + one status):**

| ID | Market / structure | Rec | Dead-overlap note |
|---|---|---|---|
| S1 | `KXMLBGAME` | **TRY** | Low vs `000` NFL allocator — unchanged. |
| S2 | `KXNFLSPREAD` (+ `KXNFLTOTAL` when unblocked) | **TRY after C1** | High schedule overlap; distinct contracts — unchanged. |
| S3 | `KXNFLPASSYDS` | **TRY** | Medium same-games — unchanged. |
| S4 | **`KXNCAAFGAME`** *(replaces weather/politics Collector-pick placeholder)* | **TRY** | **Medium** weekend overlap with NFL Sun; **not** a retune of `000`. Football OOS vs MLB daily — fee channel matches NFL game books (maker_fees / 1). Strictly better than unspecified weather/politics for a runnable fee/queue-honest challenger **now** (confirmed open OI). |
| S5 | Combo shard `KXMVECROSSCATEGORY*` (R1-P4; combo maker fee) | **TRY** *(was DEFER)* | **None** with Q1–Q7 game-book allocator. Prefer cross-category combo fee series over empty `KXMVENFL*`. |

**Explicitly still out:** more `KXNFLGAME` ML capacity; capital-structure (Variants); `KXMVENFL*` empty; inventing Δ/liquidity; panel admits.

**No change** to S1–S3 identity or relative priority. List changed = **S4 series pin + S5 status**.

---

## 3. Next Scout action

1. **Stand by** PIT@CLE T−7d **2026-09-24 20:15 ET** (calendar only; no collector steal).  
2. Hand Conductor: S5 = **UPGRADE TRY** on public combo markets+trades; RFQ objects still key-gated.  
3. If Conductor opens bakeoff slot: prefer **S1 MLB** (capacity) or **S4 NCAAF** (football OOS) before S2 (wait C1).  
4. Optional follow-up GET (throttled ≥90s): `is_block_trade=true` trades page + `KXNFLTOTAL` / `KXNHLGAME` / `KXHIGHNY` inventory once 429 cools.  
5. No orders · no invented Δ · no panel admits.

---

## 4. API blockers (honest)

| Call | Result |
|---|---|
| `/series` | OK (~14.3k series) |
| Burst `/markets?series_ticker=…` | **429** frequent — need ≥45–90s gaps; prefer `external-api` + series filters |
| `KXNFLTOTAL`, `KXNHLGAME`, `KXHIGHNY`, `mve_filter=only`, `is_block_trade=true`, `KXMVENFLSINGLEGAME` | **429** this maximize pass (after earlier successes on other series) |
| `/communications/rfqs` | **401** without key |
| `trading-api.kalshi.com` | **401** — skip |
| Liquidity / P&L | **Not invented** — only raw volume/OI fields above |

---

*End Scout maximize delta 2026-09-22 · GET-only · continuous maximize packet*
