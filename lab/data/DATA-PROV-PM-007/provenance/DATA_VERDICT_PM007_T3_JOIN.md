# DATA VERDICT — DATA-PROV-PM-007 rem=180 (T-3m) mid JOIN
**Issued by:** The Clock
**Issued UTC:** 2026-09-13T21:09:28Z
**DATA:** DATA-PROV-PM-007 (rebuild from DATA-PROV-PM-003 raw Kalshi 1m candles)
**Audit:** `/workspace/lab/data/DATA-PROV-PM-007/provenance/CLOCK_AUDIT_PM007_T3_JOIN.json`
**Wave:** WAVE_008 / W2-D
**Trade:** FORBIDDEN

---

## DATA VERDICT: CLEARED

**Scope:** rem=180 mid **tape / join integrity only** — not alpha, not Examiner Δ, not Feature, not READY.

---

## Certified rule (fail-closed)

- Pair key: `(asset, OPEN_TIME, CLOSE_TIME)` / `VENUE_NATIVE_ID` vs PM-003 `remaining_universe`
- `decision_time = CLOSE_TIME - 180s` (T-3m)
- Candle: `payload.candlesticks` with `end_period_ts == unix(CLOSE_TIME) - 180`
- Mid only: `yes_bid.close_dollars > 0` AND `yes_ask.close_dollars > 0` AND `bid <= ask`
- `implied_p = round((bid+ask)/2, 6)`, `implied_p_method = mid`
- `last` retained for audit only — **never** mid
- Missing candle or mid-rule fail → no row (fail-closed)

---

## Coverage [V]

| Asset | Independent rem=180 mid | Claim |
|-------|------------------------:|------:|
| BTC | **604** | 604 |
| ETH | **604** | 604 |
| Total | **1208** | 1208 |

- Field mismatches vs claimed checkpoints: **0**
- Mid-rule fails: **0**
- Missing candles: **0**
- missing_vs_pm003: **0** · extra: **0**
- Last-as-mid leaks: **0**

---

## Knowability

| Question | Answer |
|----------|--------|
| Knowable at decision time t? | **Yes (on-boundary)** — candle `end_period_ts` lands on `decision_time`; `obs_lag_sec=0` for 1208/1208 [V]. Same class as CB-001 / W2-A lag=0 on-boundary. |
| Look-ahead? | **No** — `end_period_ts == close-180`; no future candle; decision_time arithmetic ok=1208 bad=0 [V] |
| On-minute? | **Yes** — decision_time ends `:00Z` for 1208/1208; obs_time==decision_time for 1208 [V] |
| Live probe? | Partial [V] only — FETCH 2×200 rem180 confirmed, 2×429; primary = historical PM-003 tape |

---

## A–G summary

- A_candle: PASS
- B_mid_rule: PASS
- C_no_last_as_mid: PASS
- D_pairing: PASS
- E_coverage: PASS
- F_lookahead/knowability: PASS
- G_forbidden: PASS (PM-003 rem=180 absent by design: True)

---

## CLEARED vs still out of scope


**Why CLEARED (not CONDITIONAL like CB-001):** rem=180 mid uses the same Kalshi official 1m candle `yes_bid`/`yes_ask` close_dollars mid rule already CLEARED for Examiner on PM-003 rem=840/600/300 cells. This is a new rem cell on that lineage — not a new venue or incomplete-second print. On-boundary lag=0 is documented inheritance, not a fresh knowability block.

**CLEARED:** rem=180 Kalshi 15m BTC/ETH mid join on DATA-PROV-PM-007 / PM-003 raw tape for Wave 008 W2-D under the rule above.

**NOT CLEARED by this verdict:**
- Feature / READY / Examiner Δ / alpha / trades
- Union with PM-002 / Poly / other rem shops
- Using `last` as mid
- Fabricating rem=180 by interpolating rem=60/300
- Speaking beyond on-boundary knowability class without Conductor door

---

## FAILURES

None on tape/join integrity for this rem=180 cell.

---

## REQUIRED REMEDIATION

None for join clearance. Document on-boundary lag=0 semantics and partial live-probe caveat in any downstream Feature card. Re-Clock if raw tape or pairing keys change.

---

## Caveats

- Knowability: candle close at end_period_ts is on-boundary (obs_lag_sec=0). Same class as CB-001 / W2-A lag=0 on-boundary — treat as knowable-at-t with on-minute boundary semantics; not a future candle.
- Live probe evidence in FETCH: partial [V] only (2×200 rem180 confirmed, 2×429). Primary evidence is historical PM-003 tape.
- PM-003 derived checkpoints lack rem=180 by design (840/600/300/60/0 only); PM-007 is a new rem cell re-extracted from the same official 1m candle tape.

**Rationale:** Independent rebuild matches claimed 1208/1208 rem=180 mid rows on all compare fields; mid rule clean (no last-as-mid); pairing exact vs PM-003 (missing=0, extra=0); obs_lag_sec=0 on-boundary knowability (CB-001 / W2-A class); PM-003 lacked rem=180 by design — new cell from same raw tape; no Examiner/Poly/PM-002/interpolation. Live probe partial [V] only (2×200 + 2×429) — documented caveat, not a blocker; primary is historical PM-003 candle tape.

State: Not Feature / Not READY / Not Examiner. Wave 008 W2-D waits on CLEARED or CONDITIONAL.

---

## Clock seal

**DATA VERDICT: CLEARED** (tape/join only) — sealed by The Clock 2026-09-13T21:09:28Z.  
Wave 008 W2-D gate lands. Not Feature / Not READY / Not Examiner. Trade FORBIDDEN.
