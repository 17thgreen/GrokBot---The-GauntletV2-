# DATA VERDICT — CB-001 × PM-007 rem=180 completed-bar join (lock B)

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T21:21:29Z
**Authority:** `governance/CLOCK_ORDER_CB001_PM007_JOIN_2026-09-13.md` · `governance/CBVEL_ON_MINUTE_POLICY_2026-09-13.md`
**Trade:** FORBIDDEN
**Wave:** 008 / W2-D / DRAFT-FEAT-20260913-006 inventory join

---

## DATA VERDICT: CLEARED

**VERDICT_SCOPE:** join_only
**QUALITY_STATUS:** JOIN_CLEARED_LOCK_B
**Feature lock:** **B** (`bar_end < decision_time`) — PRIMARY score
**Policy A:** (`bar_end <= decision_time`) — caveat count ONLY; not Feature-scored
**Layer:** Coinbase Exchange public 1m candle tape (BTC-USD / ETH-USD) × PM-007 Kalshi 15m rem=180 mid checkpoints
**THIS JOIN:** lock-B `cb_close_t` / `cb_close_tm1` / `v_CB` at every PM-007 `decision_time` (rem=180 / T-3m)
**NOT:** Feature · READY · alpha · Examiner scores / `p_t` · Binance · CF/BRTI · L3 fill · forecast treatment of `v_CB` · PM-003-join reuse as rem=180 proof

## Rationale

Independent rebuild under Feature lock B (bar_end < decision_time) matches claim 1208/1208, 0 lookahead, dense BTC/ETH, B never uses bar_end==t (lag typically 60s when t on-minute). Policy A on-minute coincidence (1208/1208) noted as caveat-count only — not Feature-scored. PM-003 join does not cover rem=180; this audit is independent from CB raw CSV + PM-007 checkpoints.

## Coverage under lock B (exact)

| Headline | N_pm007 | B_close_ok | B_velocity_ok | B_lookahead | B_eq_t | A_on_min (caveat) |
|----------|---------|------------|---------------|-------------|--------|-------------------|
| `KALSHI|15m|BTC|T-3m` | 604 | 604 | 604 | 0 | 0 | 604 |
| `KALSHI|15m|ETH|T-3m` | 604 | 604 | 604 | 0 | 0 | 604 |

**Independent rebuild (B):** close_ok **1208/1208**; velocity_ok **1208/1208**
**Claim:** 1208/1208 — **100% field match** vs independent rebuild: **1208** rows; mismatches **0**
**Lookahead under B (bar_end >= t):** **0**
**B bar_end == t:** **0** (must be 0)
**Raw density:** BTC/ETH each **10140/10140** in-window; missing=0

**implied_p_method:** `{'mid': 1208}` — mid-only required and satisfied

## Lag under lock B

| Measure | Count |
|---------|-------|
| decision_time exact minute (`…:00Z`) | 1208/1208 |
| B bar_end < decision_time | 1208/1208 |
| B bar_end == decision_time | 0/1208 |
| B lag_sec unique | [60] |
| B lag histogram | {60: 1208} |

Expect typically **60s** lag when `t` is on the minute (B selects the prior completed minute).

## Policy A caveat counts (NOT Feature-scored)

| Measure | Count |
|---------|-------|
| A close_ok / velocity_ok | 1208 / 1208 |
| A on-minute (bar_end == t) | 1208/1208 |
| A lookahead (bar_end > t) | 0 |
| A lag_sec unique | [0] |

Policy A would land every on-minute decision on `bar_end == t` — same on-boundary knowability class as CB×PM003. **Feature lock is B**; A is documented as caveat count only. Do not silently switch.

## Certifications A–G (under lock B)

- **A_cb_close_B:** pass=True — bar_end < t only; B_eq_t=0
- **B_prior:** pass=True
- **C_velocity:** pass=True — formula + knowable iff both closes under B
- **D_m:** pass=True — same-row PM-007 mid only
- **E_coverage:** pass=True — independent 1208/1208 matches claim; mismatches=0
- **F_lookahead:** pass=True — B lookahead=0; B_silently_A=0
- **G_forbidden:** pass=True — no foreign fill; no PM-003-join reuse as rem=180 proof; no Examiner

## FAILURES / CAVEATS

1. **Policy A on-minute (caveat count only):** 1208/1208 A joins would use `bar_end == decision_time`. Not Feature-scored. Lock B never uses that bar.
2. **PM-003 join does not cover rem=180:** Prior CONDITIONAL CB×PM003 verdict is rem 840/600/300/60/0 only. This audit rebuilds rem=180 independently.
3. None on lock-B tape/join integrity.

## SAFE / UNSAFE

### SAFE (under CLEARED, lock B)

- Using completed-bar closes with `bar_end < decision_time` from DATA-PROV-CB-001 raw CSV only.
- Fail-closed if a bar is missing.
- Inventory use of lock-B `v_CB` as a candidate velocity input for DRAFT-FEAT-20260913-006.
- Counting Policy A on-minute as a named caveat (not a Feature input).

### UNSAFE

- Feature-scoring Policy A (`bar_end <= t`) or silently switching from B to A.
- Inventing rem=180 coverage from the PM-003 join.
- Filling holes with Binance / CF / BRTI / L3.
- Treating `v_CB` as a forecast or scoring Examiner Δ in this provenance step.
- Declaring Feature / READY from this join alone.

## REQUIRED REMEDIATION

None for lock-B join clearance. Document Policy A on-minute caveat-count (not scored) on any downstream Feature card. Re-Clock if raw CB tape or PM-007 checkpoints change.

## Examiner / Wave 008 gate

**CLEARED** as Wave 008 W2-D inventory join gate for DRAFT-FEAT-20260913-006 (Coinbase velocity at T-3m under lock B). This document contains **no** Examiner scores and **no** `p_t`. Not alpha clearance. Trade FORBIDDEN. Not Feature. Not READY.

## Artifacts

- **script:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/clock_audit_CB001_PM007_JOIN.py`
- **json:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM007_JOIN.json`
- **md:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/CLOCK_AUDIT_CB001_PM007_JOIN.md`
- **verdict:** `/workspace/lab/data/DATA-PROV-CB-001/provenance/DATA_VERDICT_CB001_PM007_JOIN.md`

---

## Clock seal

**DATA VERDICT: CLEARED** (join only, Feature lock B) — sealed by The Clock 2026-09-13T21:20:59Z.
Independent rebuild matches claim 1208/1208; 0 B lookahead; B never bar_end==t; A on-minute caveat-count only.
Not a Feature. Not READY. Not Examiner. Trade FORBIDDEN.
PM-003 join does not cover rem=180.
