# DRAFT-ABST-20260913-001 — W2-C bad-calibration eligibility gate

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 002 step 3  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; not an entry)  
**CARD_ID:** DRAFT-ABST-20260913-001 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-where-TEST-007-ECE-above-median  
**WAVE:** W2-C (`governance/WAVE_002_ORTHOGONAL_SLOT_2026-09-13.md`)  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor Governor Packet 2026-09-13 · axis W2-C · parent baseline TEST-20260911-007 · nearest dead Features FEAT-20260912-001/002 (F1), FEAT-20260912-003/004 (F3)  
**CONFIDENCE:** Low [H] on *value* of gating — the cell set and ECE figures themselves are [V] from TEST-007 / slot stamp  
**TRADE:** FORBIDDEN  

This card does **not** propose a \(p_t\). It only says when a Wave 002 Feature is allowed to speak vs must output the incumbent (abstain).

---

## THESIS

F1 and F3 spoke on well-calibrated T-5m cells and lost. A Feature on W2-C may alter \(p_t\) **only** on cells where TEST-20260911-007 already measured market mid ECE **strictly above** the locked six-cell median; elsewhere it must abstain (\(p_t = m_t\)). [H] on usefulness; [V] on the ECE lock source.

## MECHANISM

Where Kalshi mid is already well calibrated, incremental Features fight a strong incumbent and mostly add noise/redundancy (F1/F3 sheet). Where mid ECE is worse, there is more room for a legal scored \(p_t\) to improve calibration vs \(m_t\). [H]  
This is **not** a new regime invented after a kill to rescue a dead Feature — the ECE ranking and median cut are pre-registered in the Wave 002 slot from already-published TEST-007 numbers. [V]

## LOCKED CONSTANTS (do not refit; do not peek new cells)

From TEST-20260911-007 `expected_calibration_error` on \(m_t\) (mid-only cells) and `WAVE_002_ORTHOGONAL_SLOT_2026-09-13.md`:

| Cell | ECE [V] |
|------|--------:|
| `KALSHI\|15m\|ETH\|T-14m\|mid` | 0.047409 |
| `KALSHI\|15m\|BTC\|T-10m\|mid` | 0.041487 |
| `KALSHI\|15m\|BTC\|T-14m\|mid` | 0.034636 |
| `KALSHI\|15m\|ETH\|T-5m\|mid` | 0.032856 |
| `KALSHI\|15m\|BTC\|T-5m\|mid` | 0.024279 |
| `KALSHI\|15m\|ETH\|T-10m\|mid` | 0.022895 |

- Six-cell ECE set [V]: `{0.034636, 0.047409, 0.041487, 0.022895, 0.024279, 0.032856}`  
- Median [V from slot]: `0.033746`  
- **Eligibility predicate (locked):** cell ECE **strictly greater than** `0.033746`  
- **ELIGIBLE_CELLS [V]:** `{ETH T-14m mid, BTC T-10m mid, BTC T-14m mid}`  
- **INELIGIBLE (hard abstain) [V]:** all T-5m; ETH T-10m; any non-mid method; any other venue/tenor/asset not in the six-cell table  

Do **not** recompute ECE at decision time. Do **not** add cells. Do **not** move the median.

## HEADLINES vs ANNEX (AMD-005, no pool)

**Headlines (primary measure; separate; no pool):**
1. `KALSHI|15m|ETH|T-14m|mid` (ECE 0.047409)
2. `KALSHI|15m|BTC|T-10m|mid` (ECE 0.041487)

**Annex (Cartographer says so now, before Feature peek):**
- `KALSHI|15m|BTC|T-14m|mid` (ECE 0.034636) — **annex-eligible under this gate**  
- A subsequent Feature Card may opt into this annex **only if it says so before peek**. If silent, annex stays dark.  
- Annex is not a third headline. No pooling with headlines.

**Forbidden cells for speak:** T-5m (both assets), ETH T-10m — even if a Feature wants them. This gate denies.

## ELIGIBILITY RULE (knowable at decision timestamp \(t\))

### Inputs knowable at \(t\) [A/V]
- `venue`, `window` (15m), `asset` ∈ {BTC, ETH}
- `quote_source` = mid on the **same** checkpoint row (same-\(t\) incumbent; decision timestamp = mid timestamp). **Not** T−1. **Not** last-fallback.
- `checkpoint` / T-minus from `time_remaining_sec` using the TEST-007 map [V]:
  - T-14m ↔ rem = 840
  - T-10m ↔ rem = 600
  - T-5m ↔ rem = 300
- Frozen allowlist `ELIGIBLE_CELLS` / `HEADLINES` / `ANNEX` above (constants; not estimated at \(t\))

### Gate
```
cell_key = (KALSHI, 15m, asset, T-minus, mid)

if cell_key not in ELIGIBLE_CELLS:
    ABSTAIN  # Feature must set p_t = m_t (incumbent); no speak
elif cell_key in HEADLINES:
    ALLOW_SPEAK_HEADLINE
elif cell_key in ANNEX and FeatureCard.opts_in_annex_before_peek:
    ALLOW_SPEAK_ANNEX
else:
    ABSTAIN
```

Equivalent predicate (documentation only; implementation uses allowlist, not live ECE):  
`ALLOW iff TEST007_ECE[cell_key] > 0.033746` with the frozen table above.

### Incumbent binding
Same-\(t\): TEST-007 checkpoint mid on the **same cell**. F2 vs T−1m is **not** this claim. [V slot]

## DECISION-TIME / CLOCK JOIN

Clock must be able to join without look-ahead:

1. Confirm `implied_p_method == mid` and mid timestamp = decision timestamp (same row).  
2. Confirm T-minus bucket from `time_remaining_sec` with the locked map; no future rem.  
3. Confirm allowlist membership is a constant lookup — **no** re-estimation of ECE on the scored slice, **no** outcome labels in the gate.  
4. Fail-closed: unknown rem, non-mid, missing mid, VOID/DISPUTED handling per TEST-007 excludes → ABSTAIN (no speak).  
5. If Clock cannot certify knowability → treat as DEV_FAIL for this gate on that row / wave.

This rule is knowable at \(t\): cell identity is observable; ECE cut is a frozen published constant. **Not DEV_FAIL.**

## WHAT THIS GATE IS NOT

- Not F1 digital / structural \(\Phi(z)\)  
- Not F2 Map 2 / T−1m / oracle divergence  
- Not k=50 / BTC-only retune  
- Not raw 0/1 into logloss  
- Not a trade  
- Not a new ECE fit, reliability rebin, or cell search  
- Not permission to speak on T-5m “because the Feature looks good there”

## COMPOSITION WITH A FEATURE

Wave 002 Feature (next seat) produces AMD-001 legal scored \(p_t\) **only** when this gate says ALLOW_SPEAK_*.  
On ABSTAIN rows: \(p_t := m_t\) (Δ = 0 by construction vs incumbent).  
Learned weights only under Governor Packet §1.4. Holdout closed. Trade forbidden.

## FAILURE REGIME

- Gate too tight → headlines starve (N speak too small) → FAIL-INSUFFICIENT downstream [H]  
- Gate ignored → F1/F3 redux on well-calibrated cells [I]  
- Annex treated as headline or pooled → AMD-005 violation  
- Live ECE recompute / new cells after peek → peek / DEV_FAIL  
- Same-\(t\) mid broken (T−1 substitute) → wrong incumbent [V slot forbid]

## FALSIFICATION (of the *gate’s claimed usefulness*)

Downstream Examiner on the two headlines (annex separate): if a legal Feature under this gate still fails to beat same-\(t\) mid on ΔBrier / ΔLogLoss after excludes, the **Feature** dies — the gate may still be correct as a restraint.  
Kill the **gate** as a research bet if: forcing ABSTAIN on T-5m / ETH T-10m is the only reason a Feature “looks better” after the fact without headline wins (post-hoc story). Gate itself is not scored as alpha.

## REQUIRED DATA

- TEST-20260911-007 published ECE table (frozen) [V]  
- Wave slot stamp [V]  
- At score time: same L1 checkpoint fields as TEST-007 (`m_t` mid, rem, asset, contract) + Feature’s own DATA-* (not defined here)  
- Clock clearance on same-\(t\) mid + rem→T-minus map  

## Evidence notes

- ECE figures and cell ranking: [V] TEST-20260911-007  
- Median 0.033746 and eligibility cut: [V] Wave 002 slot (derived from that six-cell set)  
- Claim that gating helps vs unconditional F1/F3: [H]  
- F1/F3 spoke on well-calibrated T-5m and are nearest dead cards: [V] slot / cemetery path (Wave file)  
- Measurement of any Feature under this gate: **UNTESTED**  
- No invented fills, Sharpes, Δ metrics, or new ECE numbers  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-001-W2C-bad-cal.md`  
- Kind: DRAFT abstention / eligibility — await Archivist ID if commissioned  
- Next in sequence: one Feature Card on W2-C (not this seat)

## Compose result — TEST-20260913-002 (2026-09-13T19:17:54Z)
Composed with FEAT-20260913-001. Package **REDUNDANT / FAIL-INSUFFICIENT** (BTC T-10m incremental; ETH T-14m inverts). Gate not independently cemetery'd. No retune of abstention thresholds on this kill.
