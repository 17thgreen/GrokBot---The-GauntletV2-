# DATA VERDICT — W2-B Kalshi mid × Poly last T-5m JOIN

**Issued by:** The Clock
**Issued UTC:** 2026-09-13T19:55:47Z
**Authority:** `CLOCK_ORDER_W2B_POLY_T5_JOIN_2026-09-13.md` · `DRAFT-FEAT-20260913-004` · `DRAFT-ABST-20260913-004`
**Trade:** FORBIDDEN
**Feature door:** **NEEDS_DATA** — this verdict alone does **not** READY and does **not** alone authorize Examiner

---

## DATA VERDICT: CONDITIONAL

**VERDICT_SCOPE:** join_only
**QUALITY_STATUS:** JOIN_CERTIFIED_WITH_CAVEATS
**THIS JOIN:** Kalshi same-t mid (PM-003) × Poly 15m last-print (PM-005) at rem=300 / T-5m; exact (asset, OPEN, CLOSE) pairing
**NOT:** Poly mid · invented bid/ask · PM-002 silent union · venue pool · rem=600/840 headlines · alpha · Examiner Δ

## Rationale

Join works under documented caveats: partial coverage vs full Kalshi T-5m scored universe (many Kalshi opens predate Poly 15m label span / lack OC twin); Poly last is lagged (obs_time < decision_time; documented obs_lag_sec); last ≠ mid (bid/ask null; mid BLOCKED — do not invent); fail-closed on miss_L / miss_m / miss_pairing; Feature door stays NEEDS_DATA — this join verdict alone does not READY or Examiner-route.

## Coverage (exact)

| Headline | N_scored | N_OC_twin | N_pairable | miss_pairing | miss_L | miss_m |
|----------|----------:|----------:|-----------:|-------------:|-------:|-------:|
| `KALSHI|15m|BTC|T-5m|mid` | 569 | 254 | 254 | 315 | 0 | 0 |
| `KALSHI|15m|ETH|T-5m|mid` | 545 | 240 | 240 | 305 | 0 | 0 |

Kalshi T-5m rem=300 mid universe before hygiene: 1208 (604 BTC + 604 ETH). Pairable ≪ universe because Poly 15m labels start ~2026-09-08T14:30Z while Kalshi opens earlier; fail-closed on miss_pairing.

## Lag (pairable rows)

- **BTC:** n=254, min=23.0s, median=45.0s, mean=44.20s, p90=47.0s, max=103.0s
- **ETH:** n=240, min=23.0s, median=45.0s, mean=44.18s, p90=47.0s, max=103.0s

## Certifications A–G (summary)

- **A_m:** pass=True
- **B_L:** pass=True
- **C_pairing:** pass=True
- **D_scored_row:** pass=True
- **E_coverage:** pass=True
- **F_knowability:** pass=True
- **G_forbidden:** pass=True

## Inventory cross-check

- pairing_N_rem300_last BTC **276** / ETH **275** (claims 276/275) — match
- empty histories **2** (claim 2) — match
- no PM-002 union: **True**

## SAFE / UNSAFE

### SAFE (under CONDITIONAL)

- Using Poly **last** with `obs_time <= decision_time` on exact OC twins
- Fail-closed when m_t or L_t missing (`p_t := m_t`)
- Keeping yes_bid/yes_ask null; not inventing mid from last
- Headlines rem=300 only; dark rem unused for scoring cells
- Independent PM-005 fetch (no PM-002 sheet union)

### UNSAFE

- Treating Poly last as contemporaneous mid
- Inventing bid/ask or mid from last
- Silent PM-002∪PM-003 union to inflate N
- Pooling Kalshi+Poly into one score / one metric
- Using rem=600/840 dark rows as headlines
- Citing this join as Feature READY or Examiner clearance alone
- Look-ahead (`obs_time > decision_time`)

## FAILURES / blockers

1. **Partial coverage [V]:** Large miss_pairing vs full Kalshi scored T-5m universe (Poly label span starts later than Kalshi opens).
2. **Lag [A]:** Poly last median obs_lag_sec ≈ 45s — weaker than same-t mid; Feature clip exists for this reason.
3. **Mid BLOCKED [V]:** Poly bid/ask null; last must not be relabeled mid.
4. **Door [V]:** Feature stays NEEDS_DATA; join CONDITIONAL ≠ Examiner route.

## REQUIRED REMEDIATION (toward stronger clearance)

1. Document lag + last≠mid caveats on any future Examiner sheet honesty.
2. Do not fabricate denser Poly quotes or invent mid to rescue coverage.
3. Separate Door/Conductor step required before Feature READY / Examiner; this Clock join alone is insufficient.
4. Optional: if denser contemporaneous Poly quotes ever exist, new DATA-* + Clock order — not this audit.

## Examiner / Door

**NOT authorized by this alone.** Feature `DRAFT-FEAT-20260913-004` door remains **NEEDS_DATA**. Gate `DRAFT-ABST-20260913-004` may use this CONDITIONAL join as the legal match rule once Door/Conductor advances — not automatic Examiner routing. Not alpha. Trade FORBIDDEN.

## Artifacts

- **script:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/clock_audit_W2B_POLY_T5_JOIN.py`
- **json:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.json`
- **md:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/CLOCK_AUDIT_W2B_POLY_T5_JOIN.md`
- **verdict:** `/workspace/lab/data/DATA-PROV-PM-005/provenance/DATA_VERDICT_W2B_POLY_T5_JOIN.md`

---

## Clock seal

**DATA VERDICT: CONDITIONAL** (join only) — sealed by The Clock 2026-09-13T19:55:18.964387+00:00. Feature stays NEEDS_DATA. Not Examiner-READY from this alone. Not alpha. Trade FORBIDDEN.
