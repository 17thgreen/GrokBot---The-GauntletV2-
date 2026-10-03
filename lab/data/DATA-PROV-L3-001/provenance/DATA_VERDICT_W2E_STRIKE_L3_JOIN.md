# DATA VERDICT — W2-E FLOOR_STRIKE × L3 JOIN
**Issued by:** The Clock  
**Issued UTC:** 2026-09-13T19:23:35Z  
**Feature draft:** `DRAFT-FEAT-20260913-002-W2E-strike-vs-mid`  
**Gate draft:** `DRAFT-ABST-20260913-002-W2E-rules-strike`  
**Audit:** `/workspace/lab/data/DATA-PROV-L3-001/provenance/CLOCK_AUDIT_W2E_STRIKE_L3_JOIN.json`  
**DATA:** DATA-PROV-PM-003 + DATA-PROV-PM-001 (`FLOOR_STRIKE`) + DATA-PROV-L3-001 — **no new fetch**

---

## DATA VERDICT: CONDITIONAL

**Scope:** join only — not alpha, not Examiner Δ.  
**Why not CLEARED:** L3 spot is **not** CF BRTI / Kalshi settlement oracle [V]; `FLOOR_STRIKE` knowability is [V] static snapshot + [A] no post-OPEN revision feed observed in this dump.

Coverage is complete under the certified rule; fail-closed unused (0 missing) but binding.

---

## Join certified (fail-closed)

```
K   = PM-001.FLOOR_STRIKE by contract_id / venue_native_id
      require present AND OPEN_TIME <= decision_time
S_t = argmax { L3 bar | close_time_ms <= decision_time_ms }.close
      require bar exists AND (decision_time_ms - close_time_ms) <= 90000
asset map: BTC → BTCUSDT spot; ETH → ETHUSDT spot
```

Missing K or S_t → `p_t := m_t`.  
**Forbidden in join:** EXPIRATION_VALUE · CF-as-oracle · incomplete-bar close · T−1 mid · last-fallback-as-mid.

---

## Coverage [V]

| Headline | N scored | N pairable (K+S_t) | miss K | miss S_t | miss either |
|----------|----------:|-------------------:|-------:|---------:|------------:|
| `KALSHI\|15m\|BTC\|T-5m\|mid` | 569 | 569 | 0 | 0 | 0 |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | 545 | 545 | 0 | 0 | 0 |

Scored excludes (near-deg): BTC 35 · ETH 59 · non-mid@rem 0 · VOID/DISPUTED 0.  
S_t lag_ms unique **1** on both headlines (≤90s). All decision_times inside L3 window.

---

## Knowability

| Input | Knowable at \(t\)? | Look-ahead? |
|-------|-------------------|-------------|
| \(K\)=`FLOOR_STRIKE` | **Yes** after OPEN if field is start-ref [V snapshot]; [A] no revision feed in dump | **No** if not revised post-OPEN |
| \(S_t\) L3 completed close | **Yes** iff `close_time_ms ≤ t` | **No** under this rule; incomplete-bar close would be look-ahead (**BLOCKED**) |
| \(m_t\) same-row mid | **Yes** [V] PM-003 CLEARED mid cells | **No** |

---

## CLEARED vs BLOCKED (join scope)

**CONDITIONAL-CLEARED for Examiner routing of this Feature's inputs:**
- K join + L3 completed-bar S_t join on the two T−5m headlines under the rule above
- L3 remains **external predictor**, not settlement truth

**BLOCKED / unchanged:**
- Treating Binance L3 as CF BRTI / Kalshi oracle (F2 still DATA-BLOCKED)
- Incomplete-bar close at open
- EXPIRATION_VALUE as feature
- Speaking outside W2-E headlines / W2-C cells
- Feature incrementality (UNTESTED)
- Trade

---

## FAILURES

None on join completeness for this slice.

---

## REQUIRED REMEDIATION (to upgrade toward CLEARED)

1. Entitled CF BRTI passthrough if settlement-index distance is required (separate L2 DATA-* + Clock) — **not** this join.
2. Optional: live revision log for `FLOOR_STRIKE` if venue ever restates start-ref after OPEN.
