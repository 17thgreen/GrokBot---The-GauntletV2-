# DRAFT-ABST-20260913-002 — W2-E rules / FLOOR_STRIKE eligibility gate

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 003 step 2  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; not an entry; not a \(p_t\))  
**CARD_ID:** DRAFT-ABST-20260913-002 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-on-W2E-headlines-with-knowable-FLOOR_STRIKE  
**WAVE:** W2-E (`governance/WAVE_003_ORTHOGONAL_SLOT_2026-09-13.md`)  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor Wave 003 after Wave 002 CLOSE (TEST-20260913-002) · incumbent TEST-20260911-007 same-t mid · nearest dead: DRAFT-FEAT-20260913-001 (sibling-mid), FEAT-20260912-001/002 (F1 Φ(z) used FLOOR_STRIKE)  
**CONFIDENCE:** Low [H] on *value* of this restraint; cell list and knowability claims tagged below  
**TRADE:** FORBIDDEN  

Does **not** retune W2-C / DRAFT-ABST-20260913-001. Does **not** invent λ. Does **not** define Φ(z), moneyness×σ, or a sibling blend.

---

## THESIS

A W2-E Feature (rules / void / dispute / FLOOR_STRIKE distance vs same-t \(m_t\)) may alter \(p_t\) **only** on the pre-registered T-5m headline cells, and **only** when `FLOOR_STRIKE` is Clock-cleared knowable at decision time \(t\). Elsewhere: hard abstain (\(p_t = m_t\)). [H] on usefulness; [V] on headline lock from the Wave 003 slot.

## MECHANISM

W2-C already gated “badly calibrated” cells and died on that pair. W2-E moves to T-5m (where mid ECE was better in TEST-007) and asks whether **rules/strike geometry vs mid** has residual — without rebuilding F1’s digital. [I]  
Eligibility here is a **restraint**: do not speak without a knowable strike anchor; do not shop W2-C cells; do not use post-settlement void labels as if they were live at \(t\). [V/A]

## LOCKED HEADLINES (AMD-005, no pool)

Pre-registered in `WAVE_003_ORTHOGONAL_SLOT_2026-09-13.md` **before** any W2-E peek. **Not** the W2-C pair:

1. `KALSHI|15m|BTC|T-5m|mid`  
2. `KALSHI|15m|ETH|T-5m|mid`  

**No annex declared by this card.** Soft shopping of BTC T-10m / ETH T-14m / etc. = forbid. Hard abstain outside the two headlines for primary speak.

## INCUMBENT

Same-\(t\): TEST-007 checkpoint mid on the **same cell**. Decision timestamp = mid timestamp. No T−1 substitute. [V slot]

## KNOWABILITY AUDIT (why this is not DEV_FAIL)

| Ingredient | At decision time \(t\)? | Tag | Gate use |
|------------|------------------------|-----|----------|
| Cell identity (venue, 15m, asset, rem→T-minus, mid) | Yes — checkpoint row | [V] PM-003 | Allowlist |
| Same-t mid \(m_t\) | Yes — same row | [V] | Required |
| `FLOOR_STRIKE` \(K\) | Yes after OPEN if field is the start-ref and not revised later | [A] join PM-001; Clock must certify | Required; fail-closed if missing/unclear |
| `RULES_PRIMARY` text | Yes at/after OPEN (static rules string) | [V] PM-001 field exists | Optional Feature input; not required for this gate beyond “contract exists” |
| Live VOID / DISPUTE / HALT flag on checkpoint | **Not present** on PM-003 checkpoint schema [V] | [V] keys audited | **Not used** in this gate |
| Final `STATUS` / `RESOLUTION` including VOID | Known only after resolve | [V] | **FORBIDDEN** in eligibility at \(t\) (look-ahead) |
| Spot \(S_t\) / distance to \(K\) | Only with L3 (or other) bar `close_time ≤ t` | [U]/[A] until Feature DATA-* + Clock | **Not required for this eligibility card**; Feature that needs \(S_t\) carries its own DATA/Clock burden |

**Void/dispute clause [V/I]:** Examiner still excludes VOID/DISPUTED from scored N per BINARY_EXAMINER_SPEC (post-label hygiene). That is **not** the same as a decision-time abstention signal. Cartographer will **not** pretend final void is knowable at \(t\). If a future DATA-* ships a live dispute flag with timestamps, a later amendment may add it — not this card.

Because headlines + same-t mid + Clock-cleared \(K\) **are** joinable without look-ahead, this slot is **not DEV_FAIL**.

## ELIGIBILITY RULE (computable at \(t\))

T-minus map [V TEST-007]: T-5m ↔ `time_remaining_sec = 300` (T-10m=600, T-14m=840 — listed only to forbid accidental use).

```
cell_key = (KALSHI, 15m, asset, T-minus, mid)

HEADLINES = {
  (KALSHI, 15m, BTC, T-5m, mid),
  (KALSHI, 15m, ETH, T-5m, mid),
}

if implied_p_method != mid OR mid timestamp != decision_time:
    ABSTAIN                         # fail-closed; no T−1, no last-fallback-as-mid
elif cell_key not in HEADLINES:
    ABSTAIN                         # hard; includes all W2-C cells
elif FLOOR_STRIKE K missing OR Clock cannot certify K knowable at t:
    ABSTAIN                         # no speak without strike anchor
elif rem not in locked map / unknown checkpoint:
    ABSTAIN
else:
    ALLOW_SPEAK_HEADLINE
```

On ABSTAIN: Feature must set \(p_t := m_t\) (Δ = 0 vs incumbent by construction).

No invented numeric thresholds (no θ on \|m−0.5\|, no σ, no λ). Allowlist + join completeness only.

## WHAT THIS GATE IS NOT

- Not F1 Φ(z) / moneyness / σ / structural digital  
- Not W2-C ECE gate / sibling-mid blend / λ retune  
- Not F2 Map 2 / k=50 / T−1 incumbent  
- Not raw 0/1 into logloss  
- Not a trade  
- Not a live void/dispute classifier from final RESOLUTION  
- Not permission to speak on T-14m/T-10m “because strike distance looks interesting”

## COMPOSITION WITH A FEATURE

Wave 003 Feature (next seat) produces AMD-001 legal scored \(p_t\) **only** on ALLOW_SPEAK_HEADLINE under this gate.  
Must not be Φ(z)/moneyness×σ; must not be sibling-mid.  
If Feature needs \(S_t\) (or other L3) for “distance to FLOOR_STRIKE,” that join is Feature DATA + Clock — this card does not waive it. If that DATA is missing → Feature NEEDS_DATA; do not invent a regime to rescue.  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- \(K\) systematically missing / revised after OPEN → chronic ABSTAIN or Clock block [A]  
- Feature sneaks Φ(z) using \(K\) → Door/Prosecutor PROHIBITED (renamed F1) [V ban]  
- Using final VOID as if live at \(t\) → look-ahead / DEV_FAIL for that design [V]  
- Shopping non-headline cells after peek → AMD-005 violation  

## FALSIFICATION (of the gate as restraint)

Gate is not scored as alpha. Downstream: if a legal W2-E Feature still fails vs same-t mid on both headlines, the **Feature** dies; do not retune this allowlist to chase W2-C cells. Kill the gate’s research bet only if headline restriction is post-hoc storytelling without a declared Feature instrument.

## REQUIRED DATA

- Wave 003 slot + TEST-007 cell map [V]  
- PM-003 checkpoint mid + rem at \(t\) [V]  
- PM-001 `FLOOR_STRIKE` (and Clock policy on revision) [A]  
- Live void flags: **not** required (and not available on PM-003 checkpoints [V])  

## Evidence notes

- Headlines locked in Wave 003 slot: [V]  
- PM-003 checkpoint schema lacks VOID/DISPUTE fields: [V] audited keys  
- PM-001 has `FLOOR_STRIKE`, `RULES_PRIMARY`, post-hoc `STATUS`/`RESOLUTION`: [V]  
- \(K\) knowable after OPEN without later revision: [A] until Clock certifies  
- No invented ECE/λ/θ/Δ metrics in this card  
- Measurement of any Feature under this gate: **UNTESTED**  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-002-W2E-rules-strike.md`  
- Kind: DRAFT abstention / eligibility — not DEV_FAIL  
- Next: one Feature Card on W2-E (not a second Cartographer pass)

## Compose result — TEST-20260913-003 (2026-09-13T19:28:51Z)
Composed with FEAT-20260913-002. Package **REDUNDANT / FAIL-INSUFFICIENT** (both T-5m headlines ΔBrier and ΔLogLoss > 0). Gate not independently cemetery'd. No retune. L3 ≠ oracle.
