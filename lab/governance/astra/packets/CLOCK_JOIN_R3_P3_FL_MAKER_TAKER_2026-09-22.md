# CLOCK JOIN — R3-P3 FL maker/taker panel stub (SoT / freshness only)

**Issued by:** The Clock  
**Issued UTC:** 2026-09-23T00:23:17Z  
**Issued ET:** 2026-09-22 20:23:17 ET  
**Packet:** `R3-P3-FL-MAKER-TAKER`  
**panel_version:** `2026-09-22.r3-p3-fl-maker-taker-v0`  
**Stub:** `/workspace/lab/governance/astra/packets/R3_P3_FL_MAKER_TAKER_PANEL_STUB_2026-09-22.json`  
**Capture:** `/workspace/lab/astra-capture/r3-p3-fl-maker-taker/`

---

## DATA VERDICT (join / SoT scope): **CONDITIONAL — ADMIT REFUSED / RESOLUTION JOIN DEFERRED**

**Scope:** SoT integrity + freshness of the panel stub seed. **Not** admit. **Not** Examiner. **Not** Feature READY. Trade FORBIDDEN.

### PASS [V]
| Check | Result |
|-------|--------|
| `admitted_at` | **null** (honest) |
| Settled markets resolved N | **0** (honest; listing 429; no invented tickers) |
| Freeze SHA-256 | **PASS** — matches claimed `0ed697…206a7` |
| C3 weather first | **PASS** — KXHIGHNY + KXHIGHCHI only on panel |
| Trades sampled | **15** |
| Native `taker_outcome_side` / `taker_book_side` | **15/15 present** |
| Lee-Ready | **REFUSED** on all 15; `aggressor_inference` null |
| `occurrence_datetime` SoT vs live_get | **PASS** — all 3 markets `2026-09-23T14:00:00Z` match live GET artifacts |
| `close_time` future vs Clock now | **PASS** — all three still pre-close |
| status | **active**; `result` empty — pre-settlement |
| sqlite | empty admitted shells; seed JSON is source until admit |
| Stub freshness | stubbed `2026-09-23T00:19:20Z` (~minutes before this join) |

### REFUSE / DEFER [V]
| Gate | Stamp |
|------|--------|
| `admit.py` / panel admit | **REFUSED** — settled join N=0; markets not settled |
| Resolution / outcome join | **DEFERRED** until settled listing succeeds with real N>0 **or** markets settle and re-GET yields `result` |
| Treating stub as admitted panel | **REFUSED** |
| Lee-Ready aggressor inference | **REFUSED** (native taker fields present) |
| Backfill / invent settled tickers | **REFUSED** (prior-day guesses 404; settled routes 429) |

### SoT notes
- `occurrence_source`: `live_get_market` — verified against `packets/r3_p3_fl_maker_taker/live_get_2026-09-22/market_*.json` for the three seed tickers.
- Bands registry pre-registered before outcome join — OK for measurement hygiene; does **not** clear admit.
- Measurement shells (MZ / post-fee ROI / maker-vs-taker) remain null until Examiner — out of Clock admit scope.

### Required next (Collector / Conductor — not Clock admit)
1. Re-GET settled weather listings when 429 clears **or** wait for Sep-22 weather markets to settle.
2. Only then request Clock re-join for resolution SoT with N>0.
3. Keep ADMIT-1 / C1 / PIT@CLE budget isolation.

---

## Clock seal

**ADMIT: REFUSED.** **Resolution join: DEFERRED** (settled N=0 honest).  
SoT occurrence on seed markets: **PASS**. Native taker fields + Lee-Ready refuse: **PASS**.  
Stub is not an admitted panel.
