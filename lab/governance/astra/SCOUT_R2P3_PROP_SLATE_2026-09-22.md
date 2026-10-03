# Scout R2-P3 ADMIT-NEXT — KXNFLPASSYDS prop slate map
**Seat:** Market Scout  
**Timestamp:** **2026-09-22 19:40 ET** (America/New_York, UTC−4)  
**Conductor ask:** R2-P3 ADMIT-NEXT — next prop-rich slate for `KXNFLPASSYDS` ladder kernel (**NOT** ATL@GB).  
**Mode:** GET-only · no orders · throttle ≥45–90s between series · raw `volume_fp` / `volume_24h_fp` / `open_interest_fp` only  
**Kickoff SoT:** Kalshi `occurrence_datetime`  
**Hosts:** `https://api.elections.kalshi.com/trade-api/v2/` (primary)

**Pins:** No panel admits. No invented volume. Sibling series pulled when cheap.

---

## Recommended slate

**Name:** **Sun 2026-09-27 dual-game prop slate — LAC@BUF + BAL@DAL**

| Game | Kickoff (`occurrence_datetime` → ET) | Prop events (3 series) | Markets | Raw OI sum | Raw vol24 sum | Raw vol sum |
|---|---|---|---|---|---|---|
| **LAC@BUF** | **2026-09-27 16:00 ET** (`2026-09-27T20:00:00Z`) | PASSYDS / RECYDS / RSHYDS | 92 | 4607.55 | 4402.05 | 4609.31 |
| **BAL@DAL** | **2026-09-27 19:25 ET** (`2026-09-27T23:25:00Z`) | PASSYDS / RECYDS / RSHYDS | 101 | 3777.96 | 3743.50 | 3777.96 |
| **Slate total** | — | **6 events** | **193** | **8385.51** | **8145.55** | **8387.27** |

### Event tickers (recommended)

**Kernel `KXNFLPASSYDS` (38 markets, 4 QB ladders):**
- `KXNFLPASSYDS-26SEP27LACBUF` — kickoff 2026-09-27 16:00 ET — players `LACJHERBERT10`, `BUFJALLEN17` — n=18 · oi=1543.19 · vol24=1543.19
- `KXNFLPASSYDS-26SEP27BALDAL` — kickoff 2026-09-27 19:25 ET — players `DALDPRESCOTT4`, `BALLJACKSON8` — n=20 · oi=691.20 · vol24=691.20

**Sibling ladders (same games):**
- `KXNFLRECYDS-26SEP27LACBUF` · `KXNFLRECYDS-26SEP27BALDAL`
- `KXNFLRSHYDS-26SEP27LACBUF` · `KXNFLRSHYDS-26SEP27BALDAL`

### Sample market tickers (PASSYDS)

- `KXNFLPASSYDS-26SEP27LACBUF-LACJHERBERT10-300`
- `KXNFLPASSYDS-26SEP27LACBUF-BUFJALLEN17-275`
- `KXNFLPASSYDS-26SEP27BALDAL-DALDPRESCOTT4-275`
- `KXNFLPASSYDS-26SEP27BALDAL-BALLJACKSON8-250`

### Why this slate

- Only open PASSYDS inventory beyond ATL@GB is these **two Sunday games** (full inventory: 3 PASSYDS events).
- Dual-game Sunday pack maximizes ladder count (193 mkts / 6 events / 3 series) while kickoffs are still **~5 days** out — early enough for a small T− measurement panel.
- Both games carry full PASSYDS + RECYDS + RSHYDS ladders (kernel + siblings).
- Among Sunday games, LAC@BUF leads raw OI/vol24; BAL@DAL leads market count — jointly richest non-late slate.

---

## Why not ATL@GB

| Field | Value |
|---|---|
| Events | `KXNFLPASSYDS-26SEP24ATLGB`, `KXNFLRECYDS-26SEP24ATLGB`, `KXNFLRSHYDS-26SEP24ATLGB` |
| Kickoff | **2026-09-24 23:15 ET** (`2026-09-25T03:15:00Z`) |
| Inventory | 140 mkts · oi≈188131 · vol24≈161792 (richest raw book) |
| Exclusion | Conductor **NOT ATL@GB (too late)** — Week-3 Thu night; ~2d to kickoff as of this packet; past useful T− window for ADMIT-NEXT measurement panel. Do not use despite superior OI/vol. |

---

## Runner-up

**LAC@BUF single-game prop pack** (if Conductor wants one game only):

- Events: `KXNFLPASSYDS-26SEP27LACBUF`, `KXNFLRECYDS-26SEP27LACBUF`, `KXNFLRSHYDS-26SEP27LACBUF`
- Kickoff: **2026-09-27 16:00 ET**
- 92 markets · oi=4607.55 · vol24=4402.05
- Stronger PASSYDS tape than BAL@DAL (oi 1543 vs 691); fewer total markets (92 vs 101).

**Not runner-up:** ATL@GB (excluded late). No Monday open prop events in inventory this pass.

---

## Inventory source (GET results)

| Series | HTTP | Open markets | Events seen | Notes |
|---|---|---|---|---|
| `KXNFLPASSYDS` | **200** | 47 | ATLGB, LACBUF, BALDAL | Full page; empty cursor |
| `KXNFLRECYDS` | **200** | 148 | same 3 games | After ≥55s throttle |
| `KXNFLRSHYDS` | **200** | 138 | same 3 games | After ≥55s throttle |
| `KXNFLANYTD` | **429** ×2 | — | — | First call + retry after ~75s cooldown both `too_many_requests`. Partial inventory without ANYTD. |

Liquidity figures above = sum of raw API `volume_fp` / `volume_24h_fp` / `open_interest_fp` across open markets in each event. No invented totals.

---

## Dead-overlap vs Q6-000

**Medium — same games / NFL calendar, different contracts.**

- Matches S3 in `SCOUT_Q6_STRESS_KERNELS_2026-09-22.md`: prop ladders stress multi-strike / near-0-1 fee behavior vs binary ML allocator `000`.
- Does **not** reopen `SHADOW_CANDIDATE_FREEZE` or retune Q7 pair-check.
- Same-Sunday kickoffs as any future `KXNFLGAME` / spread books on LACBUF / BALDAL — schedule overlap only; measurement kernel is ladder microstructure, not ML edge claim.

---

## Recommend

**TRY** — small measurement panel on **Sun 2026-09-27 LAC@BUF + BAL@DAL** prop slate (kernel `KXNFLPASSYDS`, siblings RECYDS/RSHYDS).

**HOLD** ATL@GB (late). **HOLD** ANYTD until 429 clears (optional enrichment only).

No orders · no panel admits · no capital-structure.

---

## Cite

- Conductor R2-P3 ADMIT-NEXT  
- `SCOUT_Q6_STRESS_KERNELS_2026-09-22.md` (S3)  
- `SCOUT_MAXIMIZE_DELTA_2026-09-22.md` (PASSYDS inventory prior)  
- API: `/markets?series_ticker=KXNFLPASSYDS|KXNFLRECYDS|KXNFLRSHYDS&status=open`
