# DATA VERDICT — W2A CF T-14m HOUR-TAPE JOIN

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T19:36:54Z
**Authority:** `governance/CLOCK_ORDER_W2A_CF_T14_JOIN_2026-09-13.md` · `DRAFT-FEAT-20260913-003` · `DRAFT-ABST-20260913-003`
**Trade:** FORBIDDEN

---

## DATA VERDICT: CONDITIONAL

**VERDICT_SCOPE:** join_only
**QUALITY_STATUS:** JOIN_CERTIFIED_WITH_CAVEATS
**Layer:** L2 official settlement-index **hour** tape (Kalshi CF passthrough → CF Benchmarks BRTI / ETHUSD_RTI)
**THIS JOIN:** last-in-second at T-14m (rem=840) from hour archive
**NOT:** close-minute CLEARED extractor · Binance · EXPIRATION_VALUE as feature · T−1 mid · incomplete current second treated as complete · invented prints

## Rationale

Join-only: hour-tape last-in-second (A) pairs on all scored rows with K present (OPEN_TIME<=t) and same-t m_t; no look-ahead (print.time<=t); forbidden paths unused. CONDITIONAL (not CLEARED) because: (1) all decision_times are on-second boundaries and A selects the ms=0 print of the *incomplete* current second — order forbids treating incomplete current second as complete; B (completed-second safe, s-1) is also dense (document, do not silently switch); (2) FLOOR_STRIKE is [V] snapshot / [A] no revision feed; (3) prior CF-001 CLEARED is close-minute F2 path only — this T-14m hour-tape join is a distinct path (READY ≠ CLEARED for F2 reuse).

## Coverage (exact)

| Headline | N_scored | N_pairable (A) | miss_cf_A | miss_K | miss_m | miss_either_A | N_pairable (B) |
|----------|----------|----------------|-----------|--------|--------|---------------|----------------|
| `KALSHI|15m|BTC|T-14m|mid` | 604 | 604 | 0 | 0 | 0 | 0 | 604 |
| `KALSHI|15m|ETH|T-14m|mid` | 604 | 604 | 0 | 0 | 0 | 0 | 604 |

## Certifications A–G (summary)

- **A_cf:** pass=True
- **B_K:** pass=True
- **C_m:** pass=True
- **D_scored_row:** pass=True
- **E_coverage:** pass=True
- **F_knowability:** pass=True
- **G_forbidden_paths:** pass=True

## FAILURES

1. **Incomplete-second boundary [A]/[U]:** All rem=840 decision_times are on-second (`…:00Z`). Order-literal A selects the print at exact `t` (ms mod 0) — start of unix second `s`, which is **not** yet complete under CF-001 lock rule. Order forbids incomplete current second as if complete. Completed-second-safe B (s−1) is also dense; do not silently switch.
2. **FLOOR_STRIKE revision [A]:** PM-001 is a static dump snapshot [V]; no post-OPEN revision feed — cannot certify absence of revisions.
3. **Path distinction:** Prior `DATA_VERDICT_DATA-PROV-CF-001` CLEARED is close-minute F2 only. This hour-tape T-14m join is separate; READY ≠ CLEARED for F2 reuse.

## SAFE / UNSAFE

### SAFE (under CONDITIONAL)

- Using hour-tape last-in-second with `print.time <= decision_time_ms` (no look-ahead observed).
- Fail-closed on missing cf_t / K / m_t (Feature sets `p_t := m_t`).
- Same-t mid; rem=840; TEST-007 hygiene.
- Not using close-minute derived / Binance / EXPIRATION_VALUE / T−1.

### UNSAFE

- Treating A’s on-boundary print as a **completed** 1Hz second without caveat.
- Silently switching the Feature join to B without documenting the incomplete-second policy.
- Reusing close-minute CLEARED path / `pre_close_last` as if it certified this join.
- Using EXPIRATION_VALUE as feature or CF join key.
- Inventing prints for hour-tape holes (none observed here).

## REQUIRED REMEDIATION

1. **Document incomplete-second policy** on the Feature/Examiner sheet: either (a) accept A with explicit incomplete-second caveat and Examiner honesty that cf_t at on-second `t` is the ms=0 print of an unfinished second, or (b) adopt B (completed-second safe) as the join rule via a Clock order amendment before scoring — do not silent-switch.
2. **Retain K [A] caveat** (static dump / no revision feed) on Examiner honesty.
3. **Do not** cite CF-001 close-minute CLEARED as clearance for this T-14m join.
4. No remediation needed for coverage holes (A and B both 0 miss_cf on both headlines).

## Examiner gate

**CONDITIONAL OPEN** for DRAFT-FEAT-20260913-003 / DRAFT-ABST-20260913-003 under documented caveats. Not alpha clearance. Trade FORBIDDEN.

## Artifacts

- **script:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/clock_audit_W2A_CF_T14_JOIN.py`
- **json:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/CLOCK_AUDIT_W2A_CF_T14_JOIN.json`
- **md:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/CLOCK_AUDIT_W2A_CF_T14_JOIN.md`
- **verdict:** `/workspace/lab/data/DATA-PROV-CF-001/provenance/DATA_VERDICT_W2A_CF_T14_JOIN.md`

---

## Clock seal

**DATA VERDICT: CONDITIONAL** (join only) — sealed by The Clock 2026-09-13T19:36:54Z.  
Examiner may route DRAFT-FEAT-20260913-003 under documented incomplete-second + K-[A] caveats. Not F2 close-minute CLEARED. Not alpha. Trade FORBIDDEN.

---

## Conductor policy lock (2026-09-13T19:37:32Z)

**Incomplete-second policy:** locked to **B** (completed-second safe: if `t%1000==0` use last-in-second of `s−1`; else A).  
Not A. Examiner `TEST-20260913-004` routed on B.  
Coverage under B already measured [V]: BTC/ETH T−14m each **604/604** pairable, miss_cf_B=0, lag unique 200ms, no look-ahead.  
Clock idle unless Examiner reports a knowability defect on s−1.
