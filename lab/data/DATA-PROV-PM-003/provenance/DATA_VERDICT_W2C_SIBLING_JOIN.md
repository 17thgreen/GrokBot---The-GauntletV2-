# DATA VERDICT — W2-C sibling mid JOIN
**Issued by:** The Clock  
**Issued UTC:** 2026-09-13T19:12:41Z  
**Feature draft:** `DRAFT-FEAT-20260913-001-W2C-sibling-mid`  
**Gate draft:** `DRAFT-ABST-20260913-001-W2C-bad-cal`  
**Audit:** `/workspace/lab/data/DATA-PROV-PM-003/provenance/CLOCK_AUDIT_W2C_SIBLING_JOIN.json`  
**DATA:** DATA-PROV-PM-003 + DATA-PROV-PM-001 OPEN/CLOSE — **no new fetch**

---

## DATA VERDICT: CLEARED

**Scope:** the **sibling join only** — not alpha, not incrementality, not Examiner Δ.  
**READY ≠ CLEARED for Feature speak** remains Conductor's wave door; this certifies join knowability.

---

## Join certified (fail-closed)

Pair KALSHI 15m BTC↔ETH by:
- same `OPEN_TIME` + `CLOSE_TIME` (PM-001 / coverage)
- same `time_remaining_sec` ∈ {840, 600}
- sibling `implied_p_method == mid` (no last-fallback)
- same `decision_time` as scored row
- TEST-007-style excludes on both sides (near-deg ≤0.02/≥0.98 dropped; VOID/DISPUTED → missing)
- missing sibling → `p_t := m_t` (fail-closed; card already states this)
- **no** EXPIRATION_VALUE · **no** CF · **no** L3 · **no** future rem

---

## Coverage [V]

| Cell | N scored | N pairable | N missing | present-but-excluded |
|------|----------:|----------:|----------:|---------------------:|
| Headline A `KALSHI\|15m\|ETH\|T-14m\|mid` → BTC mid | 604 | 604 | 0 | 0 |
| Headline B `KALSHI\|15m\|BTC\|T-10m\|mid` → ETH mid | 604 | 604 | 0 | 0 |
| Annex `KALSHI\|15m\|BTC\|T-14m\|mid` → ETH mid (DARK) | 604 | 604 | 0 | 0 |

Universe twinning: BTC OPEN/CLOSE keys 604 · ETH 604 · shared **604** · BTC-only **0** · ETH-only **0**.  
When paired: decision_time equality 604/604; rem equality 604/604; future-window violations **0**.  
OPEN/CLOSE vs PM-001 mismatches **0**.

Fail-closed path unused on this slice (0 missing) but remains binding.

---

## Knowability

| Question | Answer |
|----------|--------|
| Knowable at decision time \(t\)? | **Yes** — opposite-asset same-window same-rem mid is L1 on the sibling PM-003 checkpoint row at the same \(t\) [V] |
| Look-ahead? | **No** — sibling rem == scored rem; sibling decision_time == scored decision_time; same OPEN/CLOSE window; no future rem [V] |

---

## CLEARED vs still out of scope

**CLEARED:** sibling mid join for headlines A/B (and annex coverage join if a future card opts in before peek) under the rule above, on DATA-PROV-PM-003 1208 universe.

**NOT CLEARED by this verdict:**
- Feature incrementality / ΔBrier / ΔLogLoss (UNTESTED; Examiner only)
- Speaking on ineligible gate cells (T−5m, ETH T−10m, etc.)
- Annex speak (card DARK)
- Pooling headlines
- CF / L3 / EXPIRATION_VALUE as inputs
- Union with PM-002 / sealed holdout
- Trade

---

## FAILURES

None on join integrity for this slice.

---

## REQUIRED REMEDIATION

None for join clearance. If a later slice has missing twins, keep fail-closed; re-Clock if pairing keys change.
