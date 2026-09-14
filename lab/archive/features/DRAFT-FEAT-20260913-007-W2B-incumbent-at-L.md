**SUPERSEDED** by FEAT-20260913-007.md (INACTIVE after TEST-20260913-007 invert kill).

# DRAFT-FEAT-20260913-007 — W2-B Poly last vs Kalshi mid at L

- **FEATURE_ID:** (Archivist-assigned on commission)
- **NAME:** Frozen clip of (Poly last_L − Kalshi m_L) into m_L
- **STATUS:** HYPOTHESIS
- **CARD_KIND:** FEATURE (one instrument)
- **WAVE:** W2-B Wave 006 (`governance/FEATURE_ORDER_W2B_W006_2026-09-13.md` · `governance/WAVE_006_ORTHOGONAL_SLOT_2026-09-13.md`)
- **PROVENANCE:** The Statistician · 2026-09-13 UTC · compose DRAFT-ABST-20260913-007-W2B-incumbent-at-L · Clock DATA_VERDICT_W2B_INCUMBENT_AT_OBS CLEARED (254/240) · lineage DRAFT-FEAT-20260913-004 HELD (decision-time incumbent; not edited) · not FEAT-20260913-006 (W2-D) · not FEAT-20260913-005 (CB-VEL) · not FEAT-20260913-001 (sibling)
- **CONFIDENCE:** Low [H] — UNTESTED; not a validity grade
- **TRADE:** FORBIDDEN
- **EXAMINER:** **DARK** — this filing does not lift Examiner. Governor lift required. [V order]
- **LEARNED_CLASS:** none (no fit)

## INSTRUMENT

**Cross-venue at legal incumbent L:** Polymarket Global 15m **last** (`last_L`) vs Kalshi official 1m **mid at L** (`m_L`), where \(L\) = Poly last `obs_time`.

`last_L` is last. **Not** mid. Do **not** invent bid/ask. Do **not** relabel last as mid.

`m_L` is the incumbent. **Not** Kalshi mid at `decision_time`. A beat-TEST-007-decision-time-mid claim stays **UNTESTED**.

Frozen clip of `(last_L − m_L)` into \(m_L\). Soft residual — not a venue pool, not a sibling-asset blend.

**004 is held.** This is a new card (007-class), not a λ retune of `DRAFT-FEAT-20260913-004`.

## GATE COMPOSITION

Compose with `DRAFT-ABST-20260913-007-W2B-incumbent-at-L.md`. Do **not** retune it. Do **not** compose with `DRAFT-ABST-20260913-004`.

- ABSTAIN → \(p := m_L\) (not decision-time mid)
- Speak only on ALLOW_SPEAK_HEADLINE
- **No annex.** No rem shop.

**Headlines (no pool):**
1. `KALSHI|15m|BTC|T-5m|mid` — instrument: Poly 15m BTC last at \(L\)
2. `KALSHI|15m|ETH|T-5m|mid` — instrument: Poly 15m ETH last at \(L\)

## DEFINITION

```
ε = 1e-4
w = 0.12           # clip |last_L − m_L| to 12pp before λ; frozen [A]
λ = 0.20           # single scored weight; frozen [A]
# robustness annex only (never select by Δ): λ ∈ {0.10, 0.20, 0.30}; w ∈ {0.08, 0.12, 0.16}
# λ = 0 diagnostic ⇒ Δ = 0
# clip-family constants match held 004; they are not a post-sheet retune

L      = Poly last obs_time
last_L = Poly 15m last-print at L
         # method=last; yes_bid/yes_ask null; NOT mid
m_L    = Kalshi official 1m mid at L
         # completed-bar: argmax end_period_ts among candles with
         # end_period_ts ≤ unix(L), same (asset, OPEN_TIME, CLOSE_TIME)
         # mid only if bid>0, ask>0, bid≤ask
         # implied_p = round((bid+ask)/2, 6); method=mid
         # price.close / last NEVER as mid; no interpolation
         # NOT mid at decision_time

b      = last_L - m_L

if gate ABSTAIN or last_L missing or m_L missing or mid-rule fails:
    p = m_L            # fail-closed; never fall back to decision-time mid
else:
    p = clip(m_L + λ * clip(b, -w, +w), ε, 1-ε)
```

AMD-001: scored \(p \in (\varepsilon,1-\varepsilon)\). ε-clip is hygiene. No raw 0/1.

Scored incrementality is vs **\(m_L\)**. Decision-time mid is not the incumbent on this card.

## MECHANISM

Poly last at \(L\) is a lagged print, ~45s before Kalshi `decision_time` on the Wave 005 pairable set [V Clock / Governor Hold B]. That last is not same-\(t\) vs TEST-007 mid, so 004’s decision-time incumbent was not a legal same-\(t\) beat. [V]

Moving the incumbent clock to \(L\) asks a different question: after a clip, does Poly last carry residual vs the Kalshi 1m mid that was already knowable at \(L\)? If yes, a frozen pull of \(m_L\) toward `last_L` may improve proper scores vs \(m_L\) alone. [H]

The clip exists so a stale or extreme last cannot yank \(p\) to near-certainty. [A]

Not sibling-asset. Not CF−mid. Not CB-VEL. Not W2-D rem shop.

## CONTRACT / UNIVERSE SCOPE

- Wave 005 T-5m pairable OC-twin set only [V]
- Coverage under CLEARED incumbent-at-obs: BTC 254/254, ETH 240/240 [V Clock]
- Fail-closed row-wise if `last_L` or `m_L` missing
- KALSHI incumbent at \(L\) only. No Poly-as-incumbent. No Kalshi+Poly pooled score
- No rem ∈ {840, 600, 180, 60}

## DECISION-TIME / KNOWABILITY

- \(L\), `last_L`: Poly 15m last, method=last [V CLEARED join]
- \(m_L\): Kalshi 1m completed-bar mid, `end_period_ts ≤ unix(L)` [V named Clock rule]
- FORBIDDEN as incumbent: Kalshi mid at `decision_time` [V]
- FORBIDDEN at \(t\): invented Poly mid; last-as-mid; sibling-asset mid; Φ(z); Map 2; signed CB-VEL; W2-D rem shop; policy A

## DATA LAYER

- L1 Kalshi candles for \(m_L\): official 1m (PM-003 raw / PM-007-class candles as Clock-joined) [V]
- L1 Poly last: DATA-PROV-PM-005 on the Wave 005 pairable set [V]
- Join: `DATA_VERDICT_W2B_INCUMBENT_AT_OBS` CLEARED [V]
- Fields: Poly `last`, `obs_time`; Kalshi `yes_bid`/`yes_ask` at completed bar; `implied_p_method==mid` for \(m_L\)

## TRANSFORMS / NORMALIZATION

- Missing `last_L` or `m_L` → ABSTAIN, never impute
- clip basis to \(\pm w\); clip \(p\) to \((\varepsilon,1-\varepsilon)\)
- No learned weights. No quote fabrication
- No silent fallback to decision-time mid

## EXPECTED SIGN / USE IN FORECAST

If `last_L` > \(m_L\), \(b>0\) and \(p\) rises vs \(m_L\) (capped). Converse if last < mid-at-L. Not an ensemble. Not a trade.

## FAILURE REGIME

- Sparse last / missing \(m_L\) → FAIL-INSUFFICIENT / chronic ABSTAIN
- Stale last after clip still noise vs \(m_L\)
- Using decision-time mid as incumbent → verdict violation / wrong claim
- last-as-mid leakage if someone relabels
- N=254/240 is the pairable set, not 604 — do not invent 604 coverage

## FALSIFICATION

On **each** headline separately vs **\(m_L\)** (not decision-time mid):

Skill requires **both** ΔBrier < 0 and ΔLogLoss < 0 (model − \(m_L\); lower-is-better).  
Kill / REDUNDANT if ΔBrier ≥ 0 **or** ΔLogLoss ≥ 0, or CIs cover 0.  
Also kill if one headline works and the other inverts (no pool, no venue pool).

A Δ vs TEST-007 decision-time mid is **out of scope** on this card and stays UNTESTED. Do not report it as this instrument.

Placebos:
1. Shuffle `last_L` vs \(m_L\) within cell
2. λ = 0 (must give Δ = 0 vs \(m_L\))
3. Flip sign of \(b\)
4. Swap incumbent to decision-time mid (must not be this card; that is held 004)

Do not retune λ/\(w\) or headlines after a sheet. Do not patch 004. Do not invent Poly mid to rescue. Do not lift Examiner from this filing.

## LEAKAGE & REDUNDANCY CONTROLS

- Ablation vs \(m_L\) alone required
- Ablation vs unclipped last (no \(w\)) — if required to win, instrument is not *clipped* last
- Not 004 (wrong incumbent). Not W2-C / W2-A / W2-E / W2-D / CB-VEL
- USED_RESEARCH if ever scored on the pairable set
- Holdout closed

## Evidence notes

Thesis [H]. λ/\(w\)/ε [A] frozen **before** any sheet. Incumbent = \(m_L\) [V]. CLEARED 254/240 [V]. last ≠ mid [V]. 004 not edited [V]. Examiner **DARK** [V]. Measurement **UNTESTED**. No invented Δ or Poly mids. Trade FORBIDDEN.
