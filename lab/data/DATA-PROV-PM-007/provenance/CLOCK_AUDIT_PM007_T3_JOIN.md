# CLOCK AUDIT — CLOCK_AUDIT_PM007_T3_JOIN

- **AUDIT_ID:** `CLOCK_AUDIT_PM007_T3_JOIN`
- **DATA_ID:** `DATA-PROV-PM-007`
- **WAVE:** `WAVE_008 / W2-D`
- **CELL:** rem=180 (T-3m) Kalshi 15m mid
- **AUDITED_AT_UTC:** 2026-09-13T21:08:30Z
- **RECOMMENDED VERDICT:** **CLEARED**
- **SCOPE:** join/tape only — Not Feature / Not READY / Not Examiner / Trade FORBIDDEN
- **NEW_FETCH:** False

## Rule certified

- `decision_time = CLOSE_TIME - 180s`
- Candle: `end_period_ts == unix(CLOSE_TIME) - 180`
- `yes_bid = yes_bid.close_dollars`; `yes_ask = yes_ask.close_dollars`
- Mid ONLY if `bid>0 AND ask>0 AND bid<=ask`; `implied_p = round((bid+ask)/2, 6)`; `method=mid`
- `last = price.close_dollars` audit-only — NEVER as mid
- Fail-closed if candle missing or mid rule fails

## Independent rebuild vs claim

| Metric | Independent | Claim |
|--------|------------:|------:|
| Universe BTC | 604 | 604 |
| Universe ETH | 604 | 604 |
| rem=180 mid BTC | **604** | 604 |
| rem=180 mid ETH | **604** | 604 |
| Candle present | 1208 | 1208 |
| Mid-rule fails | 0 | 0 |
| Missing candles | 0 | 0 |
| Field mismatches vs claimed | 0 | 0 |
| missing_vs_pm003 | 0 | 0 |
| extra_vs_pm003 | 0 | 0 |

## Certify A–G

| Gate | Pass | Notes |
|------|:----:|-------|
| A_candle | PASS | present=1208 missing=0 |
| B_mid_rule | PASS | mid_ok=1208 fails=0 |
| C_no_last_as_mid | PASS | leaks=0 method_ne_mid=0 |
| D_pairing | PASS | missing=0 extra=0 |
| E_coverage | PASS | independent 604/604 vs claim 604/604 |
| F_lookahead / knowability | PASS | obs_eq_dec=1208 lag0=1208 on_minute=1208 |
| G_forbidden | PASS | PM-003 has rem180=False; poly=0; pm002=0 |

## Knowability / on-minute

- obs_time == decision_time: **1208** / 1208
- end_period_ts == decision unix: **1208** / 1208
- obs_lag_sec == 0: **1208** (nonzero: 0)
- decision_time on exact minute (:00Z): **1208** / 1208
- Knowability class: on-boundary candle close (lag=0) — same class as CB-001 / W2-A
- Live probe (FETCH, partial [V]): 2×200 rem180 confirmed, 2×429 — primary is historical PM-003 tape

## PM-003 rem cell check

- PM-003 derived checkpoints N: 6040
- rem distribution: `{'0': 1208, '300': 1208, '60': 1208, '600': 1208, '840': 1208}`
- rem=180 already in PM-003: **False** (expect False — new cell)

## Caveats

- Knowability: candle close at end_period_ts is on-boundary (obs_lag_sec=0). Same class as CB-001 / W2-A lag=0 on-boundary — treat as knowable-at-t with on-minute boundary semantics; not a future candle.
- Live probe evidence in FETCH: partial [V] only (2×200 rem180 confirmed, 2×429). Primary evidence is historical PM-003 tape.
- PM-003 derived checkpoints lack rem=180 by design (840/600/300/60/0 only); PM-007 is a new rem cell re-extracted from the same official 1m candle tape.

## Blockers

- None

## Verdict recommendation

**CLEARED** — Independent rebuild matches claimed 1208/1208 rem=180 mid rows on all compare fields; mid rule clean (no last-as-mid); pairing exact vs PM-003 (missing=0, extra=0); obs_lag_sec=0 on-boundary knowability (CB-001 / W2-A class); PM-003 lacked rem=180 by design — new cell from same raw tape; no Examiner/Poly/PM-002/interpolation. Live probe partial [V] only (2×200 + 2×429) — documented caveat, not a blocker; primary is historical PM-003 candle tape.

Not an Examiner skill verdict. Not permission to trade. Not Feature / Not READY.
Wave 008 W2-D waits on CLEARED or CONDITIONAL.

## Artifacts

- `/workspace/lab/data/DATA-PROV-PM-007/provenance/CLOCK_AUDIT_PM007_T3_JOIN.json`
- `/workspace/lab/data/DATA-PROV-PM-007/provenance/CLOCK_AUDIT_PM007_T3_JOIN.md`
- `/workspace/lab/data/DATA-PROV-PM-007/provenance/DATA_VERDICT_PM007_T3_JOIN.md` (draft)
- auditor: `/workspace/lab/data/DATA-PROV-PM-007/provenance/clock_audit_PM007_T3_JOIN.py`

