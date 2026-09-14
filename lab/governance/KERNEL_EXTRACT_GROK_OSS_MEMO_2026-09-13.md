# Kernel extract — Grok OSS/forum memo (2026-09-13)

**Source:** Logan inbound, third-party Grok research memo (docx).  
**Posture:** Conductor extract only (packet §3.3). **Not** a READY/PROHIBITED catalog. **Not** a hire. **Not** a TEST.  
**Dead-card overlap named first.**

## What died already (do not reopen as a Feature)

| Memo line | Nearest dead card | Note |
|-----------|-------------------|------|
| Price-to-beat / `(live−strike)/strike` as the state | F1 (FEAT-001/002 path) + **FEAT-20260913-002** W2-E | Same instrument, new adjectives. |
| Clipped CF / settlement-index vs mid as residual | **FEAT-20260913-003** W2-A | Already scored REDUNDANT. |
| ETH card as sibling-mid blend | **FEAT-20260913-001** W2-C | Dead. “BTC impulse, ETH mid hasn’t” is only legal if it is *lead-lag*, not a blend. |
| Last-tick / last-10s push-spot | F2 / Poly TWAP patch (memo’s own ban) | Do not research how to recreate it. |
| Omega / Ax / berry / warbot / “87%” clients | PROHIBITED path (packet §4.4) | Feature *names* only, if anything. |

## Measurement kernels (Clock-joinable shape, still UNTESTED)

1. **BRTI-constituent velocity (Coinbase 1m) vs Kalshi same-t mid.**  
   **DEAD** TEST-20260913-005 / FEAT-20260913-005. Do not reopen.  
   Object: `Δ = g(v_CB,t) − m_t` or `p_t = clip(m_t + λ v_CB,t)`. Incumbent = Kalshi mid at `decision_time`. Not Binance last. Not F1 moneyness.  
   Data hole: entitled Coinbase (or other BRTI-constituent) 1m known at t, joined to PM-003.  
   Nearest dead card: W2-A (CF print, not Coinbase velocity).

2. **Seconds-to-close bucketed *re-score*** of already-scored sheets (900–600 / 600–180 / 180–60 / 60–0).  
   Same Features, new cut. If skill only lives in 180–60s, the headline TEST washed it.  
   This is a **cut**, not a new Feature. Overlaps leftover **W2-D** (one new time cell, declared before peek).

3. **Implied variance vs short realized var as a silence rule.**  
   **DEAD** TEST-20260913-006 / FEAT-20260913-006 (T-3m unsigned iv−c·rv). Do not retune annex.  
   Compare `m_t(1−m_t)` to a 30–90s realized-var known at t. Output may be “abstain / emit mid,” not a new direction.  
   Nearest dead card: F2 last-minute remainder (different object: Map 2 0/1, not a var gate).

4. **Follow-vs-fade as one pre-registered switcher.**  
   If short-horizon RV **and** book velocity > A → follow Coinbase; if book velocity spikes with no index velocity → fade the book. One TEST, not two cards sharing a good week.  
   Needs the velocity tape from (1) plus a book-velocity series. Poly last ≠ book velocity.

## Not kernels (yet)

- Hawkes/LOB event-time: no Clock-clean L2. NEEDS_DATA, do not commission.  
- Soft HMM regime posteriors: process risk (look-ahead if label uses the closing bar).  
- 5minPATH / theruviparambil: **method peers** (executable prices, one row per window, clustered SEs). Clone as cemetery/protocol, not as `p_t`.  
- yt-feng / HF kachoio books: data design. Our Sep 4–11 Poly book hunt already showed the week is not gettable.

## Pilot note

This memo is **case (1)** of packet §3.3 (rough external draft). Cases (2) and (3) are not run in this file. Hire of Refiner / Intake Auditor remains **forbidden** until the three-case pilot completes.

## Forbidden readings

- Do not treat this extract as a fourth READY.  
- Do not Examiner-score from this note.  
- Do not stand up a Bot named Visionary, Scout, or Grok-research.
