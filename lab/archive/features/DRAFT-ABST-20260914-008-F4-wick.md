# DRAFT-ABST-20260914-008 — F4 wick-gate eligibility (knowability)

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 009  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; no blend/wick algebra; not an entry)  
**CARD_ID:** DRAFT-ABST-20260914-008 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-when-F4-wick-lookback-knowable  
**WAVE:** F4 (`governance/WAVE_009_ORTHOGONAL_SLOT_2026-09-14.md` · `governance/CARTOGRAPHER_ORDER_F4_2026-09-14.md`)  
**GOVERNOR:** `GOVERNOR_SIGN_F4_WICK_2026-09-14.md` SIGNED [V]  
**CLOCK / TAPE:** PM-004 × L3-002 CONDITIONAL lock B + L3-001 Sep-11 edge; Sep-12 **855/855** [V order]  
**PROVENANCE:** The Cartographer · 2026-09-14 UTC · Conductor Wave 009 · compose target DRAFT-FEAT-20260912-006 (frozen W=5, θ=1.5 on disk) · nearest dead: FEAT-20260913-007 (W2-B), TEST-20260912-002 / FEAT-002 (unconditional F1), FEAT-20260913-005 (CB-VEL)  
**CONFIDENCE:** Low [H] on Feature value; knowability locks [V]/[A]  
**TRADE:** FORBIDDEN  
**EXAMINER:** Not authorized by this card.

No Feature algebra. No wick histogram. No θ/W search. No PM-003 peek.

---

## THESIS

An F4 Feature may alter Kalshi-incumbent \(p_t\) **only** on the two T-5m PM-004 mid headlines, and **only** when the frozen wick lookback (W=5 completed L3 bars under **lock B**) is knowable at decision time \(t\). Missing mid or bars → hard abstain (\(p_t := m_t\)). Whether the wick *fires* is Feature silence (off-wick \(p = m\)), **not** a second Cartographer headline. [H]/[V]

## MECHANISM

Unconditional F1 (FEAT-002 / TEST-20260912-002) spoke on all rows and died. F4 is a **selection gate**: structural blend only on wick rows. [V/I]  
Cartographer’s job here is **knowability**, not re-deriving Φ(z) or searching θ: if the W=5 lock-B path cannot be formed at \(t\), the Feature must not speak. [V order]

## LOCKED HEADLINES (AMD-005; no pool)

1. `KALSHI|15m|BTC|T-5m|mid`  
2. `KALSHI|15m|ETH|T-5m|mid`  

Incumbent = **PM-004** same-t mid (Sep-12 tape). [V]  
**Annex T-10m:** report-only per slot — **not** a speak headline for this gate; Cartographer does not open T-10m as ALLOW_SPEAK. [V slot]  
**Forbidden rem:** T-14m (lookback crosses open). [V order]

## TAPE BOUNDARY

- **In:** Sep-12 PM-004 × L3-002 lock B (+ L3-001 midnight edges as Clock-named). Coverage 855/855 named in order [V].  
- **Out:** PM-003, Sep-13, any peek into other windows. [V]  
- L3 = external predictor, **≠** CF settlement oracle. [V]

## FROZEN WICK LOOKBACK (named; not searched)

From `DRAFT-FEAT-20260912-006` already on disk [V] — Cartographer **does not** retune:

- **W = 5** completed 1m bars  
- **θ = 1.5** (Feature owns wick inequality; not redefined here)  
- **Lock B:** bar usable iff `bar_end < decision_time` (strict prior; same honesty class as CB-VEL on-minute policy B) [V/A align]

Knowability for ALLOW_SPEAK requires at minimum:

1. \(S_t\) = close of last L3 1m bar with `bar_end < decision_time`  
2. \(S_{t-W}\) = close of the bar W completed steps back in that same strict-prior chain  
3. Both joins present (no fill from Binance/CF/invented closes)

If Feature also needs \(\hat\sigma_t\) / other DRAFT-FEAT-20260912-006 inputs, those inherit the Feature card’s missing→drop rules — Cartographer fail-closes when the **W=5 lock-B lookback chain** itself is incomplete.

**Off-wick:** when lookback is knowable but wick predicate is false → Feature sets \(p_t = m_t\) (Feature silence). That is **not** ABSTAIN-for-missing and **not** a second headline. [V order]

## NEAREST DEAD CARDS (named)

| ID | Why named |
|----|-----------|
| `FEAT-20260913-007` | W2-B invert — not a wick gate |
| `TEST-20260912-002` / `FEAT-002` | Unconditional F1 — F4 exists to *not* always speak |
| `FEAT-20260913-005` | CB-VEL — Coinbase velocity, not L3 wick selection |

## KNOWABILITY AUDIT (not DEV_FAIL)

Gate uses PM-004 mid + L3 lock-B W=5 chain with frozen W/θ from the signed F4 draft — no PM-003 peek, no new θ → **not DEV_FAIL**.

## ELIGIBILITY RULE (no Feature algebra)

```
HEADLINES = {
  (KALSHI, 15m, BTC, T-5m, mid),   # PM-004 Sep-12
  (KALSHI, 15m, ETH, T-5m, mid),
}

m_t = PM-004 same-row mid at decision_time
lookback_ok = (W=5 lock-B L3 closes S_t .. S_{t-W} all present)
              # bar_end < decision_time each; no CF/Binance fill; L3 ≠ oracle

if tape not Sep-12 PM-004 OR PM-003 row used:
    ABSTAIN / PROHIBITED
elif implied_p_method != mid OR mid timestamp != decision_time:
    ABSTAIN
elif cell_key not in HEADLINES:          # no T-14m; no rem shop
    ABSTAIN
elif m_t missing OR not lookback_ok:
    ABSTAIN                              # fail-closed; p := m when m exists
else:
    ALLOW_SPEAK_HEADLINE                 # Feature may evaluate wick; off-wick → p=m
```

On Cartographer ABSTAIN: \(p_t := m_t\).  
On ALLOW + off-wick: Feature silence \(p_t := m_t\) (not a Cartographer cell split).

**Explicit non-contents:** no Φ(z), λ, σ grid, wick formula expansion, histogram, or θ/W search in this card.

## WHAT THIS GATE IS NOT

- Not F1-always-speak / FEAT-002 retune  
- Not W2-B / FEAT-20260913-007  
- Not CB-VEL / FEAT-20260913-005  
- Not PM-003 peek / Sep-13  
- Not cheap-binary wick / \|m − p_struct\| wick  
- Not T-14m / pool / θ search  
- Not an Examiner commission  

## COMPOSITION

Wave 009 Feature composes `DRAFT-FEAT-20260912-006` onto **this** gate.  
Door → Examiner later — **not** from this filing.  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- Incomplete W=5 lock-B chain → ABSTAIN [V]  
- Speaking without lookback / always-speak F1 → Door PROHIBITED [V]  
- θ/W search after peek → DEV_FAIL class [V]  
- PM-003 contamination → slot ban [V]  

## FALSIFICATION (gate as restraint)

Gate is not alpha. Do not open T-14m or new θ after a sheet. If Feature loses on both T-5m headlines, Feature dies; do not widen speak to off-wick by Cartographer rewrite.

## REQUIRED DATA

- DATA-PROV-PM-004 Sep-12 mid at T-5m [V]  
- L3-002 lock B (+ L3-001 edge as Clock-named) [V]  
- Frozen W=5, θ=1.5 on DRAFT-FEAT-20260912-006 [V]  

## Evidence notes

- Governor SIGN + Wave 009 slot + Cartographer order: [V]  
- Sep-12 855/855; lock B; no PM-003: [V] order  
- Dead cards named per order: [V]  
- No Feature algebra, histogram, or invented θ  
- Feature / Examiner under this gate: **UNTESTED** / not lifted here  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260914-008-F4-wick.md`  
- Kind: NEW DRAFT abstention / eligibility (008-class) — **not DEV_FAIL**  
- Next: one Feature compose of DRAFT-FEAT-20260912-006 (not this seat); no Examiner from this card

## Compose result — TEST-20260914-001 (2026-09-14T01:05:59Z)
Composed with FEAT-20260914-008. Package **REDUNDANT / FAIL-INSUFFICIENT** (both N_wick < 80). No θ/W/λ retune.
