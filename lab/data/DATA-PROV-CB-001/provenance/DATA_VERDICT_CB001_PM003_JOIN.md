# DATA VERDICT — CB-001 × PM-003 completed-bar join

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T20:51:41Z
**Authority:** `governance/CLOCK_ORDER_CB001_PM003_JOIN_2026-09-13.md` · `DATA-PROV-CB-001/provenance/SPEC.md`
**Trade:** FORBIDDEN

---

## DATA VERDICT: CONDITIONAL

**VERDICT_SCOPE:** join_only
**QUALITY_STATUS:** JOIN_CERTIFIED_WITH_ON_MINUTE_CAVEAT
**Layer:** Coinbase Exchange public 1m candle tape (BTC-USD / ETH-USD) × PM-003 Kalshi 15m checkpoints
**THIS JOIN:** completed-bar `cb_close_t` / `cb_close_tm1` / `v_CB` at every PM-003 `decision_time` (all rem T-14/10/5/1/0)
**NOT:** Feature · READY · alpha · Examiner scores / `p_t` · Binance · CF/BRTI · L3 fill · forecast treatment of `v_CB`

## Rationale

Independent rebuild matches claim 6040/6040, 0 lookahead, completed-bar SPEC (bar_end <= t) sound and dense. CONDITIONAL (not CLEARED) because EVERY join uses bar_end == decision_time (lag=0 on-minute coincidence): candle close knowability at the exact minute boundary is not proven from the 1m tape alone — same class of caveat as W2-A incomplete-second. Strict-prior alt (bar_end < t) also dense 6040/6040; do not silently switch policy.

## Coverage (exact)

| Headline | N_pm003 | close_ok (SPEC) | velocity_ok | on_min_eq | strict_close_ok |
|----------|---------|-----------------|-------------|-----------|-----------------|
| `KALSHI|15m|BTC|T-14m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|BTC|T-10m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|BTC|T-5m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|BTC|T-1m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|BTC|T-0` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|ETH|T-14m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|ETH|T-10m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|ETH|T-5m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|ETH|T-1m` | 604 | 604 | 604 | 604 | 604 |
| `KALSHI|15m|ETH|T-0` | 604 | 604 | 604 | 604 | 604 |

**Independent rebuild:** close_ok **6040/6040**; velocity_ok **6040/6040**
**Claim:** 6040/6040 — **100% field match** vs independent rebuild: **6040** rows; mismatches **0**
**Lookahead (bar_end > t):** **0**
**Raw density:** BTC/ETH each **10140/10140** in-window; missing=0 (2 padding bars outside window)

**implied_p_method:** `{'mid': 5330, 'last': 709, 'null': 1}` (inventory attaches CB fields to all rem rows; mid vs last counted)

## On-minute coincidence (CRITICAL)

| Measure | Count |
|---------|-------|
| decision_time exact minute (`…:00Z`) | 6040/6040 |
| bar_end == decision_time (lag=0) | 6040/6040 |
| bar_end < decision_time | 0/6040 |
| lag_sec unique | [0] |

SPEC (`bar_end <= decision_time`) selects the bar that **ends at** `t` for every row. Candle-close **knowability-at-t** at the exact minute boundary (exchange close availability / publication lag) is **not** proven from this 1m inventory tape. Same caveat class as W2-A incomplete-second. **Do not silently CLEARED.**

Strict-prior alt (`bar_end < t`): close/velocity **6040/6040** — coverage delta 0 on this dense tape. Document; do not silent-switch.

## Certifications A–G (summary)

- **A_cb_close:** pass=True — completed bar only; caveat: on-minute coincidence
- **B_prior:** pass=True
- **C_velocity:** pass=True — formula + knowable iff both closes; same on-minute caveat
- **D_m:** pass=True — same-row PM-003 implied_p
- **E_coverage:** pass=True — independent 6040/6040 matches claim; 0 mismatches
- **F_lookahead:** pass=True — 0 rows with bar_end > t
- **G_forbidden:** pass=True — no Binance/CF/L3 fill; no Examiner scores in this audit

## FAILURES / CAVEATS

1. **On-minute coincidence [A]/[U]:** All 6040 decision_times are exact minute boundaries; all joins use `bar_end == decision_time`. SPEC permits `<=`, but knowability of the Coinbase candle close at that exact second is unresolved — Conditionally certify with caveat (not CLEARED).
2. **Policy fork:** Strict-prior (`bar_end < t`) is also dense; Feature must document SPEC-`<=` vs strict-`<` explicitly.

## SAFE / UNSAFE

### SAFE (under CONDITIONAL)

- Using completed-bar closes with `bar_end <= decision_time` from DATA-PROV-CB-001 raw CSV only.
- Fail-closed if a bar is missing (none missing in this window).
- Inventory use of `v_CB` as a candidate velocity input **with** on-minute knowability caveat named.
- Retaining mid vs last method counts; not inventing mids.

### UNSAFE

- Treating on-boundary candle close as proven knowable-at-t without caveat.
- Silently switching to strict-prior minute without Clock order amendment.
- Filling holes with Binance / CF / BRTI / L3.
- Treating `v_CB` as a forecast or scoring Examiner Δ in this provenance step.
- Declaring Feature / READY / fourth READY from this join alone.

## REQUIRED REMEDIATION

1. **Document on-minute candle-close knowability** on any Feature/Examiner sheet that consumes this join: either (a) accept SPEC-`<=` with explicit boundary caveat, or (b) adopt strict-`<` via Clock order amendment — do not silent-switch.
2. **Do not** claim CLEARED knowability-at-t for `v_CB` at exact minute boundaries from this audit alone.
3. No remediation needed for coverage holes or lookahead (none observed under SPEC).

## Examiner / Wave 007 gate

**CONDITIONAL OPEN** as Wave 007 join gate for a later Coinbase-velocity card. Governor may lift Examiner dark for Coinbase velocity **after** this verdict lands; this document itself contains **no** Examiner scores and **no** `p_t`. Cartographer wake is Conductor's call post-gate. Not alpha clearance. Trade FORBIDDEN.

## Artifacts

- **script:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/clock_audit_CB001_PM003_JOIN.py`
- **json:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM003_JOIN.json`
- **md:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM003_JOIN.md`
- **verdict:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM003_JOIN.md`

---

## Clock seal

**DATA VERDICT: CONDITIONAL** (join only) — sealed by The Clock 2026-09-13T20:51:23Z.
Independent rebuild matches claim 6040/6040; 0 lookahead; on-minute coincidence named.
Not a Feature. Not READY. Trade FORBIDDEN.

---

## Conductor policy lock (2026-09-13T20:52:13Z)

**On-minute policy:** locked to **B** — `bar_end < decision_time` only (`governance/CBVEL_ON_MINUTE_POLICY_2026-09-13.md`).  
Not SPEC-`<=` / not `bar_end == t`. Examiner scores **B only**.  
Coverage under B already measured [V]: **6040/6040** close+velocity (same as SPEC on this dense tape).  
Cartographer wake: Conductor's. No `p_t` from Clock. Clock idle unless Examiner reports a knowability defect on B.
