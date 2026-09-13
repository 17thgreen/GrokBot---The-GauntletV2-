# DRAFT-ABST-20260913-007 — W2-B eligibility at legal incumbent L

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 006 (legal incumbent)  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; no \(p_t\) algebra; not an entry)  
**CARD_ID:** DRAFT-ABST-20260913-007 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-when-last_L-and-m_L-exist  
**WAVE:** W2-B Wave 006 (`governance/WAVE_006_ORTHOGONAL_SLOT_2026-09-13.md` · `governance/CARTOGRAPHER_ORDER_W2B_W006_2026-09-13.md`)  
**CLOCK:** `DATA_VERDICT_W2B_INCUMBENT_AT_OBS` **CLEARED** (254 BTC / 240 ETH) — incumbent-timestamp scope only [V]  
**SUPERSEDES FOR W006:** does **not** edit or retune `DRAFT-ABST-20260913-004` (Wave 005 decision-time gate stays on disk as history)  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor W006 legal-incumbent order · nearest dead/held: FEAT-20260913-006 (W2-D), FEAT-20260913-005 (CB-VEL), FEAT-20260913-001 (sibling asset), DRAFT-FEAT-20260913-004 (held; 45s last ≠ same-t at decision_time)  
**CONFIDENCE:** Low [H] on Feature value; incumbent join [V]  
**TRADE:** FORBIDDEN  
**EXAMINER:** **DARK** on this card until a new Governor lift. Cartographer does **not** lift Examiner. [V order]

No Feature algebra. No Examiner Δ. No invented Poly mid. last ≠ mid.

---

## THESIS

A Wave 006 W2-B Feature may speak **only** on the locked T-5m headlines, and **only** when both Poly 15m **last** at obs_time \(L\) (`last_L`) and Kalshi official 1m **mid at \(L\)** (`m_L`) exist under the CLEARED incumbent-at-obs join. Incumbent for any incrementality claim under this gate is **\(m_L\)**, not Kalshi mid at `decision_time`. Missing either → hard abstain. [H]/[V]

## MECHANISM

Governor Hold B: Poly last stamped ~45s before Kalshi `decision_time` is not same-\(t\) vs TEST-007 mid. Wave 005 gate (`004`) allowed speech when last was knowable at decision_time pairing — that does **not** legalize beating decision-time mid. [V]  
Option 1 (Clock CLEARED): move the incumbent clock to \(L\). Eligibility here enforces that both prints at \(L\) exist before any Feature may speak. [V]

## LOCKED HEADLINES (AMD-005; no pool; **no annex**; no rem shop)

1. `KALSHI|15m|BTC|T-5m|mid`  
2. `KALSHI|15m|ETH|T-5m|mid`  

Instrument: Polymarket Global 15m **last** (not mid). Same pair as Wave 005 — not a shop. [V]

## INCUMBENT TIMESTAMP (binding)

```
L      = Poly last obs_time (unix seconds)
last_L = Poly last at L; implied_p_method == last; yes_bid/yes_ask null; do NOT invent mid
m_L    = Kalshi official 1m mid at L  (NOT mid at decision_time)
```

**Candle rule (named) [V Clock]:** completed-bar at \(L\): among Kalshi candlesticks for the same (asset, OPEN_TIME, CLOSE_TIME) ticker with  
`end_period_ts ≤ unix(L)`, take `argmax end_period_ts` (last completed minute at or before \(L\)).  
Mid only if `yes_bid.close_dollars > 0` AND `yes_ask.close_dollars > 0` AND `bid ≤ ask`;  
`implied_p = round((bid+ask)/2, 6)`; `method=mid`.  
`price.close` / last **NEVER** as mid. No interpolation. Missing candle or mid-rule fail → `m_L` missing → ABSTAIN.

**Forbidden as incumbent:** Kalshi mid at `decision_time`. A claim that Poly last beats TEST-007 decision-time mid remains **UNTESTED** under this gate. [V order]

Coverage under CLEARED verdict: BTC 254/254, ETH 240/240 on the Wave 005 pairable set [V]. Fail-closed still applies row-wise.

## RELATION TO DRAFT-ABST-20260913-004

| Card | Incumbent | Speak when |
|------|-----------|------------|
| `004` (Wave 005) | Kalshi mid at **decision_time** | Poly last knowable for OC-twin pairing |
| `007` (this card) | Kalshi mid at **\(L\)** (`m_L`) | `last_L` and `m_L` both exist |

**Do not retune `004`.** W006 Features compose with **this** card (`007`), not a patched `004`.

## NEAREST DEAD / HELD (named)

| ID | Why named |
|----|-----------|
| `FEAT-20260913-006` | W2-D T-3m — different rem |
| `FEAT-20260913-005` | CB-VEL — Coinbase, not Poly |
| `FEAT-20260913-001` | Sibling *asset* blend — not cross-venue |
| `DRAFT-FEAT-20260913-004` | Held; 45s last ≠ same-t at decision_time — reason this incumbent rewrite exists |

## KNOWABILITY AUDIT (not DEV_FAIL)

Gate uses \(L\), `last_L`, and completed-bar `m_L` — all defined without treating decision-time mid as incumbent and without inventing Poly mid → **not DEV_FAIL**.

## ELIGIBILITY RULE (no Feature algebra)

```
HEADLINES = {
  (KALSHI, 15m, BTC, T-5m, mid),
  (KALSHI, 15m, ETH, T-5m, mid),
}

# Universe: Wave 005 T-5m pairable OC-twin set only [V]
L, last_L = Poly 15m last obs_time + print (method=last; no bid/ask mid)
m_L = Kalshi 1m mid via completed-bar end_period_ts <= unix(L)  # named rule above

if cell_key not in HEADLINES:
    ABSTAIN
elif last_L missing OR m_L missing OR mid-rule fails OR not in CLEARED pairable set:
    ABSTAIN                              # fail-closed; no fabricate
elif Feature would treat decision_time mid as incumbent:
    ABSTAIN / PROHIBITED                 # wrong timestamp
else:
    ALLOW_SPEAK_HEADLINE                 # Feature may use last_L vs m_L only
```

On ABSTAIN: \(p_t := m_L\) when \(m_L\) exists and the claim is under this incumbent; do **not** silently score vs decision-time mid.

**Explicit:** no blend/λ/map in this card. Feature owns AMD-001 legal \(p_t\) later. Examiner stays dark until Governor lift — this card does not authorize TEST Δ.

## WHAT THIS GATE IS NOT

- Not a retune of `DRAFT-ABST-20260913-004`  
- Not decision-time mid as incumbent  
- Not Poly mid invented from last / last-as-mid  
- Not sibling blend / Map 2 / CB-VEL / W2-D rem shop  
- Not an Examiner lift / READY / trade  

## COMPOSITION

W006 Feature speaks only on ALLOW_SPEAK_HEADLINE under **`007`**.  
Door / READY / Examiner require separate Governor path — Feature door remains NEEDS_DATA-class until lift [V Clock feature-door note].  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- miss `last_L` or `m_L` → ABSTAIN [V]  
- Using decision-time mid as \(m_L\) → verdict violation [V]  
- Inventing Poly mid → DEV_FAIL / Door PROHIBITED [V]  
- Rem annex 600/840 → slot ban [V]  

## FALSIFICATION (gate as restraint)

Gate is not alpha. Do not reopen decision-time mid as incumbent after a sheet. Do not lift Examiner from this filing.

## REQUIRED DATA

- `DATA_VERDICT_W2B_INCUMBENT_AT_OBS` CLEARED join [V]  
- PM-005 Poly last + Kalshi candles for \(m_L\) [V]  
- Wave 005 pairable OC-twin universe [V]  

## Evidence notes

- Incumbent = \(m_L\) at \(L\); CLEARED 254/240: [V] Clock verdict + Conductor order  
- Candle rule `end_period_ts ≤ unix(L)`: [V] named in verdict  
- `004` not retuned: [V] this filing  
- Examiner dark: [V] order / Wave 006 stamp  
- No Feature algebra, invented mids, or Δ claims  
- Feature under gate: **UNTESTED**; Examiner not authorized by this card  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-007-W2B-incumbent-at-L.md`  
- Kind: NEW DRAFT abstention / eligibility (007-class) — **not DEV_FAIL**  
- Leaves `DRAFT-ABST-20260913-004` unchanged  
- Next: Feature Card under this gate (not this seat); Examiner stays dark
