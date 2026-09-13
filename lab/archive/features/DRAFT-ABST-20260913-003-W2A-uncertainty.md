# DRAFT-ABST-20260913-003 — W2-A uncertainty / not-locked eligibility gate

**STATUS:** DRAFT / HYPOTHESIS — Cartographer Wave 004 step 2  
**CARD_KIND:** ABSTENTION / ELIGIBILITY (not a Feature; no \(p_t\) formula; not an entry)  
**CARD_ID:** DRAFT-ABST-20260913-003 (Archivist assigns permanent ID on commission)  
**NAME:** Speak-only-under-CF-mid-uncertainty-at-T-14m  
**WAVE:** W2-A (`governance/WAVE_004_ORTHOGONAL_SLOT_2026-09-13.md` · `governance/CARTOGRAPHER_ORDER_W2A_2026-09-13.md`)  
**PROVENANCE:** The Cartographer · 2026-09-13 UTC · Conductor Wave 004 after Wave 003 close · incumbent TEST-20260911-007 same-t mid · nearest dead: FEAT-20260912-005 / TEST-20260913-001 (F2 Map 2 hard remainder; also cited as FEAT-005) · FEAT-20260913-002 (W2-E L3-strike pull; L3 ≠ CF)  
**CONFIDENCE:** Low [H] on *value*; locks below are [V]/[A]  
**TRADE:** FORBIDDEN  

No Feature formula. No Map 2. No T−1 incumbent. No Φ(z). No sibling blend. No W2-E λ/δ. No invented thresholds beyond rules-locked 60s close window and TEST-007 rem map.

---

## THESIS

A W2-A Feature (clipped CF−mid *basis* under uncertainty) may alter \(p_t\) **only** on the two T-14m headlines, **only** with same-t mid and a decision-time CF print from the CF-001 **hour** tape, and **only** while the settlement remainder is **not** hard-locked (not inside the close-minute Map 2 regime). Elsewhere: hard abstain (\(p_t := m_t\)). [H]

## MECHANISM

F2 (FEAT-005) scored a **hard 0/1 remainder** once close-minute seconds lock — that is the opposite of this axis and is dead on ETH logloss [V TEST-20260913-001].  
W2-E (FEAT-20260913-002) pulled on L3 strike distance at T-5m — different index layer and cell pair [V].  
W2-A asks whether a **clipped CF−mid basis** has residual while the path is still uncertain (far from close-minute lock). Eligibility restrains speech to that uncertainty window and forbids Map 2 lock territory. [I/H]

## LOCKED HEADLINES (AMD-005; no pool; **no annex**)

1. `KALSHI|15m|BTC|T-14m|mid`  
2. `KALSHI|15m|ETH|T-14m|mid`  

T-minus map [V TEST-007]: T-14m ↔ `time_remaining_sec = 840`.  
**Hard abstain** on T-10m, T-5m, close-minute / k=*, and all W2-C / W2-E headline pairs. No shopping after peek.

## INCUMBENT

Same-\(t\): TEST-007 checkpoint mid on the **same cell**. Decision timestamp = mid timestamp.  
**Forbidden:** T−1 mid as incumbent (F2’s honest label — not this claim). If CF cannot join at headline \(t\), fail-closed / UNTESTED — do **not** silently fall back to T−1. [V slot]

## NEAREST DEAD CARDS (named)

| ID | Why named |
|----|-----------|
| `FEAT-20260912-005` (FEAT-005) / `TEST-20260913-001` | F2 Map 2 hard remainder vs T−1m; close-minute CLEARED CF path; raw 0/1 remainder — **banned shape for this wave** |
| `FEAT-20260913-002` | W2-E L3−strike disagreement pull; L3 ≠ CF; T-5m graves — **not** this instrument |

## KNOWABILITY AUDIT (not DEV_FAIL)

| Ingredient | Knowable at headline \(t\)? | Tag | Gate use |
|------------|----------------------------|-----|----------|
| Cell identity + rem=840 | Yes — PM-003 checkpoint | [V] | Allowlist |
| Same-t mid | Yes — same row | [V] | Required; fail-closed if missing |
| CF 1Hz last-in-second at `decision_time` from **hour** archive | Yes if that unix second has a print in DATA-PROV-CF-001 hour tape | [A] pending Clock on **this** join | Required; fail-closed if missing |
| Close-minute CLEARED CF path (F2) | CLEARED for close window only | [V] CF-001 verdict | **Forbidden** as this join |
| Close-window timing | `close_start_ms = close_time_ms - 60000` from PM-001 CLOSE_TIME | [V] rules / CF-001 hard rules | Lock predicate |
| Map 2 hard lock active | Only once `now_ms` enters close minute and slots lock | [V] FEAT-005 / CF-001 | ABSTAIN if active |
| FLOOR_STRIKE \(K\) | After OPEN | [A] | Not required for *this* eligibility predicate (Feature may use later); optional |

**CF join note [V/A]:** CF-001 DATA VERDICT CLEARED uses = F2 close-minute + `pre_close_last` only. Hour tape **exists** for the arena [V]. The T-14m decision-time join is a **new** Clock path for this wave — not the close-minute CLEARED path. Cartographer defines the rule; Clock must clear the join before Examiner. Missing print → ABSTAIN (fail-closed), not T−1 rescue.

Because the predicate uses only same-t mid, rem allowlist, close-window timing, and a CF print stamped ≤ \(t\), the gate is **knowable-at-t in definition**. **Not DEV_FAIL.**

## UNCERTAINTY / NOT-LOCKED PREDICATE

Settlement close window [V CF-001 / rules]:  
`close_start_ms = close_time_ms - 60000`, half-open `[close_start_ms, close_time_ms)`.

**Hard lock (Map 2 territory) — ABSTAIN if any:**
1. `decision_time_ms >= close_start_ms` (inside / after close-minute start), **or**
2. Any F2 locked-second predicate would be active (`slot i locked` under CF-001 hard rules), **or**
3. Map 1 `lock_yes` / `lock_no` at k=60 would already apply (remainder fully determined).

At locked headlines rem=840, (1)–(3) are false by construction if `decision_time` matches the T-14m checkpoint [V]. The predicate still must be evaluated fail-closed (bad CLOSE_TIME join → ABSTAIN).

**Uncertainty (required for SPEAK):** not hard-locked **and** CF hour-tape print present at \(t\) **and** same-t mid present **and** cell ∈ headlines.

## ELIGIBILITY RULE (no Feature formula)

```
HEADLINES = {
  (KALSHI, 15m, BTC, T-14m, mid),
  (KALSHI, 15m, ETH, T-14m, mid),
}

cf_t = last-in-second CF print for asset index (BRTI|ETHUSD_RTI)
       from DATA-PROV-CF-001 HOUR tape at unix second of decision_time
       # NOT close-minute CLEARED extractor; NOT Binance; NOT EXPIRATION_VALUE

if implied_p_method != mid OR mid timestamp != decision_time:
    ABSTAIN
elif cell_key not in HEADLINES:          # rem must be 840
    ABSTAIN
elif mid missing OR cf_t missing:
    ABSTAIN                              # fail-closed
elif decision_time_ms >= close_start_ms OR Map2/Map1 lock active:
    ABSTAIN                              # remainder locked / F2 grave — no speech
else:
    ALLOW_SPEAK_HEADLINE                 # uncertainty; Feature may apply clipped basis
```

On ABSTAIN: Feature sets \(p_t := m_t\).

**Explicit non-contents:** this card does **not** define clip, basis algebra, λ, or \(p_t\). Feature Card owns clipped CF−mid basis (AMD-001 legal; not raw 0/1).

## WHAT THIS GATE IS NOT

- Not FEAT-005 Map 2 / k / hard 0/1 remainder  
- Not T−1 mid incumbent  
- Not close-minute CLEARED join reused as if it were T-14m  
- Not FEAT-20260913-002 L3 strike pull / W2-E λ/δ  
- Not Φ(z) / sibling blend / F4 wick  
- Not permission to speak on T-10m/T-5m  
- Not a trade  

## COMPOSITION

Wave 004 Feature speaks **only** on ALLOW_SPEAK_HEADLINE under this gate.  
Clock → **new** CF join at T-14m (hour tape) → Examiner.  
If Clock blocks the join: beat UNTESTED; do not swap incumbent to T−1.  
Holdout closed. Trade forbidden.

## FAILURE REGIME

- Hour-tape holes at T-14m seconds → chronic ABSTAIN / UNTESTED [A]  
- Reusing close-minute CLEARED path → wrong join / Door fail [V]  
- Allowing speech inside close-minute → Map 2 redux [V ban]  
- Silent T−1 fallback when CF missing → slot violation [V]  

## FALSIFICATION (gate as restraint)

Gate is not alpha. Do not retune headlines to T-5m/T-10m or close-minute after a Feature sheet. If Feature loses on both T-14m headlines, Feature dies; mid stays incumbent.

## REQUIRED DATA

- PM-003 same-t mid + rem at T-14m [V]  
- PM-001 CLOSE_TIME (→ close_start) [V]  
- DATA-PROV-CF-001 **hour** 1Hz last-in-second at decision_time [A] Clock on this join  
- Not required for gate: Map 2 remainder engine, L3, Poly  

## Evidence notes

- Headlines / no-annex / same-t / bans: [V] Wave 004 slot + Cartographer order  
- FEAT-005 / TEST-20260913-001 Map 2 death: [V]  
- FEAT-20260913-002 W2-E death: [V]  
- CF-001 close-minute CLEARED ≠ this join: [V] DATA VERDICT + order  
- Hour tape existence: [V] CF-001 manifest  
- T-14m CF join quality: [A]/[U] until Clock clears — missing → ABSTAIN  
- No invented Δ / ECE / λ / k in this card  
- Feature under this gate: **UNTESTED**  

## Archivist / Conductor

- Path: `/workspace/lab/archive/features/DRAFT-ABST-20260913-003-W2A-uncertainty.md`  
- Kind: DRAFT abstention / eligibility — **not DEV_FAIL**  
- Next: one Feature Card on W2-A (clipped basis; not this seat)

## Compose result — TEST-20260913-004 (2026-09-13T19:42:19Z)
Composed with FEAT-20260913-003. Package **REDUNDANT / FAIL-INSUFFICIENT** (both T-14m headlines ΔBrier and ΔLogLoss > 0). Gate not independently cemetery'd. No retune. Join CONDITIONAL / Policy B.
