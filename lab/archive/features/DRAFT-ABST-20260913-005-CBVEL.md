# DRAFT-ABST-20260913-005 — CB-VEL Coinbase velocity eligibility gate

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 007  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; no velocity→\(p_t\) algebra; not an entry)  
**CARD_ID:** DRAFT-ABST-20260913-005 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-with-strict-prior-Coinbase-1m-bar-at-T-14m  
**WAVE:** CB-VEL (`governance/WAVE_007_ORTHOGONAL_SLOT_2026-09-13.md` · `governance/CARTOGRAPHER_ORDER_CBVEL_2026-09-13.md`)  
**CLOCK:** `DATA_VERDICT_CB001_PM003_JOIN` **CONDITIONAL** · on-minute policy **B** locked (`governance/CBVEL_ON_MINUTE_POLICY_2026-09-13.md`)  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor Wave 007 · incumbent TEST-20260911-007 Kalshi same-t mid · DATA-PROV-CB-001 · nearest dead: FEAT-20260913-003 (W2-A CF−mid), FEAT-20260913-002 (W2-E L3-strike), FEAT-20260912-005 / FEAT-005 (F2 Map 2)  
**CONFIDENCE:** Low [H] on *value*; join/policy locks [V]  
**TRADE:** FORBIDDEN  

No Feature algebra. No Examiner. No invented Coinbase mid. No Binance. No CF. No Poly last.

---

## THESIS

A Coinbase 1m velocity Feature may alter Kalshi-incumbent \(p_t\) **only** on the two T-14m mid headlines, **only** with same-t Kalshi mid, **only** with a Clock-usable Coinbase completed bar under lock **B** (`bar_end < decision_time`), and **only** while not in close-minute / Map 2 lock territory. Otherwise hard abstain (\(p_t := m_t\)). [H]

## MECHANISM

CB-VEL is BRTI-*constituent* exchange velocity (Coinbase 1m), not the CF settlement print (W2-A / FEAT-20260913-003), not L3-strike distance (W2-E / FEAT-20260913-002), not Map 2 remainder (FEAT-005). [V/I]  
Eligibility enforces knowable-at-t completed bars under the locked strict-prior rule so the Feature cannot speak on an unproven on-minute close (`bar_end == t`). [V Clock CONDITIONAL + policy B]

## LOCKED HEADLINES (AMD-005; no pool; **no annex**)

1. `KALSHI|15m|BTC|T-14m|mid`  
2. `KALSHI|15m|ETH|T-14m|mid`  

T-minus [V TEST-007]: T-14m ↔ `time_remaining_sec = 840`.  
**Hard abstain** on T-10m / T-5m / T-1m / T-0 and all other wave pairs. No rem shopping after peek.

## INCUMBENT

Same-\(t\) Kalshi checkpoint **mid** on the scored cell. Decision timestamp = mid timestamp.  
Coinbase is the **instrument tape**, never the incumbent. [V]  
No T−1 mid rescue. [V ban]

## ON-MINUTE LOCK **B** (binding)

From `CBVEL_ON_MINUTE_POLICY_2026-09-13.md` [V]:

```
bar usable iff bar_end < decision_time
```

- SPEC `bar_end <= decision_time` is **not** the scored eligibility path for this wave (on-minute coincidence caveat). [V Clock CONDITIONAL]  
- Annex A (`<=`) is **not** a headline and **not** a rescue. [V policy]  
- Fail-closed if no such completed bar / prior close missing. No silent switch to A. No Binance/CF fill. [V]  
- Coverage under B on this tape: 6040/6040 claimed in Clock rebuild [V] — Cartographer does not re-score; fail-closed still applies row-wise.

**Note:** This card does **not** define \(v_{\mathrm{CB},t}\) → \(p_t\). Policy B quotes the velocity *inputs* for Feature use; Feature Card owns frozen map.

## NEAREST DEAD CARDS (named)

| ID | Why named |
|----|-----------|
| `FEAT-20260913-003` | W2-A clipped CF−mid basis — same rem family, **CF** tape, not Coinbase |
| `FEAT-20260913-002` | W2-E L3-strike disagreement pull — not CB velocity |
| `FEAT-20260912-005` / **FEAT-005** | F2 Map 2 hard remainder / close-minute lock — **banned territory** for speech |

## KNOWABILITY AUDIT (not DEV_FAIL)

| Ingredient | At \(t\)? | Tag | Gate use |
|------------|-----------|-----|----------|
| Kalshi same-t mid | Yes on mid cells | [V] | Required; fail-closed |
| rem=840 / T-14m | Yes | [V] | Allowlist |
| CB completed bar with `bar_end < decision_time` | Yes under lock B if bar present | [V] policy B; Clock CONDITIONAL join | Required; fail-closed |
| CB bar with `bar_end == decision_time` | On-minute; knowability unproven | [V] Clock caveat | **Not usable** under B |
| Close-minute / Map 2 lock | Active only near CLOSE | [V] FEAT-005 / CF-001 rules | ABSTAIN if active |
| Binance / CF / Poly last / invented CB mid | Forbidden | [V] | Not inputs |

Gate is writeable without fabricating closes → **not DEV_FAIL**.

## CLOSE-MINUTE / MAP 2 ABSTAIN

Settlement close window [V]: `close_start_ms = close_time_ms - 60000`.  
**ABSTAIN** if `decision_time_ms >= close_start_ms` OR any Map 2 / Map 1 hard-lock predicate would be active.  
At rem=840 this is false by construction when the checkpoint is honest; still evaluate fail-closed.

## ELIGIBILITY RULE (no Feature algebra)

```
HEADLINES = {
  (KALSHI, 15m, BTC, T-14m, mid),
  (KALSHI, 15m, ETH, T-14m, mid),
}

cb_bar = last DATA-PROV-CB-001 1m candle for asset (BTC-USD|ETH-USD)
         with bar_end < decision_time     # LOCK B only
# NOT bar_end == decision_time; NOT Binance; NOT CF; NOT Poly last

if implied_p_method != mid OR mid timestamp != decision_time:
    ABSTAIN
elif cell_key not in HEADLINES:            # rem must be 840
    ABSTAIN
elif mid missing OR cb_bar missing OR prior completed close missing:
    ABSTAIN                                # fail-closed
elif decision_time_ms >= close_start_ms OR Map2/Map1 lock active:
    ABSTAIN                                # F2 grave — no speech
else:
    ALLOW_SPEAK_HEADLINE
```

On ABSTAIN: \(p_t := m_t\).

## WHAT THIS GATE IS NOT

- Not W2-A CF−mid / FEAT-20260913-003  
- Not W2-E strike pull / FEAT-20260913-002  
- Not Map 2 / FEAT-005 / k / hard 0/1 remainder  
- Not Poly last / W2-B  
- Not Binance fill / invented Coinbase closes  
- Not on-minute SPEC-`<=` rescue (policy A)  
- Not Φ(z) / sibling blend  
- Not a trade  

## COMPOSITION

Wave 007 Feature speaks only on ALLOW_SPEAK_HEADLINE under lock **B**.  
Examiner (when routed) scores **B only**. Kill if both headlines Δ not < 0; no retune.  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- Missing CB bar under B → chronic ABSTAIN [V fail-closed]  
- Silent use of `bar_end == t` → on-minute false knowability [V Clock]  
- Close-minute speech → Map 2 redux [V]  
- Binance/CF substitution → Door PROHIBITED [V]  

## FALSIFICATION (gate as restraint)

Gate is not alpha. Do not open T-5m/T-10m or policy A after peek to rescue a Feature sheet.

## REQUIRED DATA

- PM-003 Kalshi T-14m mid [V]  
- DATA-PROV-CB-001 1m candles; join under lock B [V Clock CONDITIONAL]  
- PM-001 CLOSE_TIME for close-window abstain [V]  

## Evidence notes

- Headlines / bans: [V] Wave 007 slot + Cartographer order  
- Lock B / Examiner B-only: [V] CBVEL_ON_MINUTE_POLICY  
- Clock CONDITIONAL + on-minute caveat: [V] DATA_VERDICT_CB001_PM003_JOIN  
- Dead cards named per order: [V]  
- No Feature algebra, invented mids, or Δ claims  
- Feature under gate: **UNTESTED**  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-005-CBVEL.md`  
- Kind: DRAFT abstention / eligibility — **not DEV_FAIL**  
- Next: one Feature Card (not this seat)

## Compose result — TEST-20260913-005 (2026-09-13T20:59:30Z)
Composed with FEAT-20260913-005. Package **REDUNDANT / FAIL-INSUFFICIENT** (both T-14m ΔBrier and ΔLogLoss > 0). Gate not independently cemetery'd. No retune. Policy B only.
