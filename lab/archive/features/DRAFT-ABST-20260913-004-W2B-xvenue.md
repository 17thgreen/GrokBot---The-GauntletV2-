# DRAFT-ABST-20260913-004 — W2-B cross-venue eligibility gate

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 005 step (gate)  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; no \(p_t\) formula; not an entry)  
**CARD_ID:** DRAFT-ABST-20260913-004 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-when-Poly-15m-last-knowable-at-same-t  
**WAVE:** W2-B (`governance/WAVE_005_ORTHOGONAL_SLOT_2026-09-13.md` · `governance/CARTOGRAPHER_ORDER_W2B_2026-09-13.md`)  
**DATA_SPEC:** `governance/DATA_PROV_PM_005_SPEC.md` (intended tape); PM-002 Poly last = weaker prototype only — **no silent union** with PM-003  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor Wave 005 after Wave 004 close · incumbent TEST-20260911-007 Kalshi same-t mid · nearest dead: FEAT-20260913-001 (sibling *asset*), FEAT-20260913-003 (CF−mid basis / W2-A), FEAT-20260913-002 (L3-strike / W2-E) · Bridge row COLLAPSED; this is the surviving Bridge *question*  
**CONFIDENCE:** Low [H] on *value*; schema locks [V]/[A]  
**TRADE:** FORBIDDEN  
**DOOR EXPECTATION:** Feature under this gate is **NEEDS_DATA** until Clock clears the same-t Kalshi-mid × Poly-last join [V slot capacity]

No Feature formula. No invented Poly mid. No unlabeled pool. Not sibling-asset blend.

---

## THESIS

A W2-B Feature (cross-venue disagreement) may alter Kalshi-incumbent \(p_t\) **only** on the two T-5m Kalshi mid headlines, and **only** when a Polymarket Global 15m **last-print** for the matched contract is knowable at the **same** decision time \(t\). If Kalshi mid **or** Poly last is missing → hard abstain (\(p_t := m_t^{\mathrm{Kalshi}}\)). [H]

## MECHANISM

Sibling-*asset* blend (FEAT-20260913-001) is dead and is a different instrument (BTC↔ETH on one venue). W2-B is **venue** disagreement: Kalshi mid vs Poly last at the same \(t\). [V/I]  
Eligibility restrains speech to rows where both prints exist without fabricating quotes. Poly is never the incumbent. [V slot]

## LOCKED HEADLINES (AMD-005; no pool; **no annex**)

Incumbent cell (scored):

1. `KALSHI|15m|BTC|T-5m|mid` — instrument: Poly 15m BTC **last** at same \(t\)  
2. `KALSHI|15m|ETH|T-5m|mid` — instrument: Poly 15m ETH **last** at same \(t\)  

T-minus map [V TEST-007]: T-5m ↔ `time_remaining_sec = 300`.  
**Hard abstain** outside these two Kalshi cells (incl. W2-C / W2-A / W2-E pairs, T-10m, T-14m). No annex shop.

## INCUMBENT

Same-\(t\) Kalshi checkpoint **mid** on the scored cell (TEST-007).  
Poly is the **instrument**, never the incumbent. [V slot]  
Poly **mid** is BLOCKED unless/until Clock clears bid/ask quotes — **do not invent mid from last**. [V order / PM-005 spec]

## NEAREST DEAD CARDS (named)

| ID | Why named |
|----|-----------|
| `FEAT-20260913-001` | Sibling *asset* mid blend (W2-C) — not cross-venue |
| `FEAT-20260913-003` | W2-A CF−mid basis — not Poly |
| `FEAT-20260913-002` | W2-E L3-strike pull — not venue |

## KNOWABILITY AUDIT (not DEV_FAIL)

| Ingredient | At \(t\)? | Tag | Gate use |
|------------|-----------|-----|----------|
| Kalshi same-t mid | Yes on PM-003 CLEARED mid cells | [V] | Required; fail-closed if missing |
| Cell rem=300 / T-5m | Yes | [V] | Allowlist |
| Poly 15m **last** with `obs_time ≤ decision_time` | Yes **if** PM-005 (or Clock-named interim) row exists for matched contract | [A]/[U] until inventory + Clock | Required; fail-closed if missing |
| Poly **mid** from bid/ask | Not on PM-002; forbidden to invent from last | [V] | **Not used** |
| Treating Poly last as if it were contemporaneous mid | PM-002 lag caveat stands until Clock says otherwise | [V] | Gate allows speech on *last knowable*; does **not** relabel last as mid |

**Why not DEV_FAIL:** the eligibility rule names **last-print**, not a fabricated mid. Missing Poly last → ABSTAIN, not imputation. Data inventory may leave the Feature NEEDS_DATA; that is not Cartographer DEV_FAIL.

## PAIRING (Clock names legal match; Cartographer does not invent)

Per PM-005 spec [V]: pairing key = asset + window length (15m) + closest OPEN/CLOSE to the Kalshi contract.  
**Clock** owns the legal match rule and same-t join certification.  
Until Clock clears: fail-closed (ABSTAIN / Feature NEEDS_DATA).  
**Forbidden:** silent PM-002 ∪ PM-003 union; unlabeled Kalshi+Poly score pool. [V]

## ELIGIBILITY RULE (no Feature formula)

```
HEADLINES = {
  (KALSHI, 15m, BTC, T-5m, mid),
  (KALSHI, 15m, ETH, T-5m, mid),
}

m_t     = Kalshi same-row mid at decision_time
L_poly  = Polymarket Global 15m last-print for Clock-matched contract
          with obs_time <= decision_time
          # NOT mid; NOT invented quotes; NOT T−0 last-as-forecast label

if implied_p_method != mid OR mid timestamp != decision_time:
    ABSTAIN
elif cell_key not in HEADLINES:          # rem must be 300
    ABSTAIN
elif m_t missing OR L_poly missing OR Clock join not cleared:
    ABSTAIN                              # fail-closed; no fabricate
else:
    ALLOW_SPEAK_HEADLINE                 # Feature may use cross-venue disagreement
```

On ABSTAIN: \(p_t := m_t\) (Kalshi incumbent).

**Explicit:** this card does not define blend/weight/map from \(L_{\mathrm{poly}}\) into \(p_t\). Feature Card owns that after DATA+Clock.

## WHAT THIS GATE IS NOT

- Not sibling-asset (BTC↔ETH) blend  
- Not Poly mid invented from last  
- Not Poly as incumbent  
- Not Map 2 / Φ(z) / W2-E λ/δ / W2-A CF basis  
- Not PM-002∪PM-003 silent union  
- Not a Kalshi+Poly pooled score  
- Not permission to shop T-10m  
- Not a trade / 4th READY without Governor  

## COMPOSITION

Wave 005 Feature speaks only on ALLOW_SPEAK_HEADLINE.  
Sequence: DATA-PROV-PM-005 inventory → Clock same-t join → Feature → Door (expect NEEDS_DATA until Clock) → Examiner vs Kalshi same-t mid, never pooled.  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- No Poly last at rem=300 for matched opens → chronic ABSTAIN / FAIL-INSUFFICIENT downstream [A]  
- Inventing mid from last → DEV_FAIL / Door PROHIBITED [V]  
- Using last as if mid without Clock → lag false contemporaneity [V PM-002 caveat]  
- Pooling venues in one metric → AMD-005 / slot ban [V]  

## FALSIFICATION (gate as restraint)

Gate is not alpha. Do not retune headlines to T-14m/T-10m after peek. If Feature loses once data exists, Feature dies; do not fabricate denser Poly quotes to rescue.

## REQUIRED DATA

- PM-003 Kalshi T-5m mid [V]  
- DATA-PROV-PM-005 Poly 15m last at rem=300 (intended) [A]  
- Clock match rule + same-t join [U] until cleared  
- PM-002 n≈30 last: prototype only — not the sheet [V]  

## Evidence notes

- Headlines / no-annex / bans: [V] Wave 005 slot + Cartographer order  
- Poly mid blocked on PM-002; last = weaker: [V] slot  
- PM-005 method = last with obs_time ≤ decision_time; not mid: [V] spec  
- Dead cards named: [V] order  
- No invented numbers, fills, or Poly mids in this card  
- Feature under gate: **UNTESTED** / expect **NEEDS_DATA**  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-004-W2B-xvenue.md`  
- Kind: DRAFT abstention / eligibility — **not DEV_FAIL**  
- Next: DATA inventory + Clock join; then one Feature Card (not this seat)
