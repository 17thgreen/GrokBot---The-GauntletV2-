# DRAFT-FEAT-20260913-004 — W2-B Kalshi mid vs Poly last

- **FEATURE_ID:** (Archivist-assigned on commission)
- **NAME:** Clipped Kalshi-mid vs Poly-15m-last basis
- **STATUS:** **NEEDS_DATA** (not READY; Clock join + DATA-PROV-PM-005 required)
- **CARD_KIND:** FEATURE (one instrument)
- **WAVE:** W2-B (`governance/FEATURE_ORDER_W2B_2026-09-13.md`)
- **PROVENANCE:** The Statistician · 2026-09-13 UTC · compose DRAFT-ABST-20260913-004 · incumbent TEST-20260911-007 Kalshi same-t mid · intended tape DATA-PROV-PM-005 · PM-002 Poly last = prototype only, no silent union · not FEAT-20260913-001 (sibling asset) · not FEAT-20260913-002/003 · Bridge question only (row COLLAPSED)
- **CONFIDENCE:** Low [H] — UNTESTED; not a validity grade
- **TRADE:** FORBIDDEN
- **LEARNED_CLASS:** none (no fit)

## INSTRUMENT

**Cross-venue disagreement:** Kalshi same-t mid \(m_t\) vs Polymarket Global 15m **last-print** \(L_t\) (Clock-matched contract, `obs_time ≤ t`).

\(L_t\) is last. **Not** mid. Do **not** invent bid/ask. Do **not** relabel last as contemporaneous mid.

Clipped basis in probability space, then a frozen pull of Kalshi \(p_t\) toward that last. Soft residual — not a venue pool, not a sibling-asset blend.

## GATE COMPOSITION

Compose with `DRAFT-ABST-20260913-004-W2B-xvenue.md`. Do **not** retune it.

- ABSTAIN → \(p_t := m_t^{\mathrm{Kalshi}}\)
- Speak only on ALLOW_SPEAK_HEADLINE
- **No annex.**

**Headlines (no pool):**
1. `KALSHI|15m|BTC|T-5m|mid` — instrument: Poly 15m BTC last at same \(t\)
2. `KALSHI|15m|ETH|T-5m|mid` — instrument: Poly 15m ETH last at same \(t\)

## DEFINITION

```
ε = 1e-4
c = 0.12           # clip |L - m| to 12pp before λ; frozen [A]
λ = 0.20           # single scored weight; frozen [A]
# robustness annex only (never select by Δ): λ ∈ {0.10, 0.20, 0.30}; c ∈ {0.08, 0.12, 0.16}
# λ = 0 diagnostic ⇒ Δ = 0

m_t    = Kalshi same-row mid (incumbent)
L_t    = Poly 15m last-print on Clock-matched contract, obs_time ≤ decision_time
         # NOT mid; NOT invented quotes

b_t    = L_t - m_t
b_clip = clip(b_t, -c, +c)

if gate ABSTAIN or m_t missing or L_t missing or Clock join not cleared:
    p_t = m_t
else:
    p_t = clip(m_t + λ * b_clip, ε, 1-ε)
```

AMD-001: scored \(p_t \in (\varepsilon,1-\varepsilon)\). ε-clip is hygiene. No raw 0/1.

## MECHANISM

Two US-visible 15m Up/Down venues can disagree at the same remaining time. If Poly last (stale-tolerant, weaker) still carries residual vs Kalshi mid after a clip, a frozen pull may improve proper scores vs Kalshi mid alone. [H]

Last is a **lagged print**, not a book. The clip exists so a stale last cannot yank \(p_t\) to near-certainty. [A]

Not sibling-asset (BTC↔ETH on one venue). Not CF−mid. Not L3-strike.

## CONTRACT / UNIVERSE SCOPE

- Scored universe: DATA-PROV-PM-003 Kalshi 1208, TEST-007 excludes, rem=300 only.
- Instrument tape: **DATA-PROV-PM-005** (intended). PM-002 n≈30 last = prototype — **no silent union**.
- Pairing: asset + 15m + closest OPEN/CLOSE; **Clock** names the legal match [U] until cleared.
- KALSHI incumbent only. No Poly-as-incumbent. No Kalshi+Poly pooled score.

## DECISION-TIME / KNOWABILITY

- \(m_t\), rem=300: PM-003 same row [V]
- \(L_t\): PM-005 last with `obs_time ≤ t` [A]/[U] until inventory + Clock
- FORBIDDEN at \(t\): invented Poly mid; treating last as mid; T−1 Kalshi; sibling-asset mid; Φ(z); Map 2

## DATA LAYER

- L1 Kalshi: DATA-PROV-PM-003
- L1 Poly last: DATA-PROV-PM-005 (**NEEDS_DATA**)
- L2/L3: not used
- Fields: Kalshi `implied_p` + `implied_p_method==mid`; Poly `last`, `obs_time`; Clock match keys

## TRANSFORMS / NORMALIZATION

- Missing either print → ABSTAIN, never impute last or mid
- clip basis to \(\pm c\); clip \(p_t\) to \((\varepsilon,1-\varepsilon)\)
- No learned weights. No quote fabrication

## EXPECTED SIGN / USE IN FORECAST

If Poly last > Kalshi mid, \(b_t>0\) and \(p_t\) rises (capped). Converse if last < mid. Not an ensemble. Not a trade.

## FAILURE REGIME

Sparse Poly last at rem=300 → FAIL-INSUFFICIENT / chronic ABSTAIN; stale last after clip still noise; Clock rejects pairing; last-as-mid leakage if someone relabels.

## FALSIFICATION

On **each** headline separately vs **Kalshi** same-t mid:

Skill requires **both** ΔBrier < 0 and ΔLogLoss < 0 (model − market).  
Kill / REDUNDANT if ΔBrier ≥ 0 **or** ΔLogLoss ≥ 0, or CIs cover 0.  
Also kill if one headline works and the other inverts (no pool, no venue pool).

Placebos:
1. Shuffle \(L_t\) vs \(m_t\) within cell
2. λ = 0 (must give Δ = 0)
3. Flip sign of \(b_t\)
4. Using Poly last *as* \(m_t\) (must not be this card)

Do not retune λ/\(c\) or headlines after the sheet. Do not invent denser Poly quotes to rescue.

## LEAKAGE & REDUNDANCY CONTROLS

- Ablation vs Kalshi \(m_t\) alone required
- Ablation vs unclipped last (no \(c\)) — if required to win, instrument is not *clipped* last
- Not W2-C sibling-asset; not W2-A; not W2-E
- USED_RESEARCH if ever scored on PM-003 overlap

## Evidence notes

Thesis [H]. λ/\(c\)/ε [A] frozen before sheet. Headlines [V]. Poly mid blocked [V]. PM-005 + Clock join [U]. Status **NEEDS_DATA**. Measurement **UNTESTED**. No invented Δ or Poly mids. Trade FORBIDDEN.
