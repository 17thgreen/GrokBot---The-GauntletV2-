# JOIN SPEC — follow-vs-fade (inventory, not a Clock order)

**Stamp:** 2026-09-14 pulse (CB-002 kicked)
**Trade:** FORBIDDEN. Not READY. Not Examiner.

## Instrument (frozen later; thresholds not written)
If short-horizon RV **and** Poly book velocity > A → follow Coinbase 1m.
If book velocity spikes with no index velocity → fade the book.
One TEST, not two cards. A is pre-registered before peek.

## Tapes required
| Tape | Role | State |
|------|------|--------|
| DATA-PROV-PM-006 | Poly YES bid/ask → book mid, then Δmid/Δt | running; 44 closed 15m (22/22) |
| DATA-PROV-PM-008 | Kalshi 15m yes bid/ask → same-t mid | running; poll_s=8.0 |
| DATA-PROV-CB-002 | Coinbase 1m completed bars → velocity | running (live forward; not CB-001) |
| DATA-PROV-CB-001 | Coinbase 1m, lock B | historical Sep 4–11 only — do not append live |

## Join (when Clock is ordered)
For each closed 15m window with both-side PM-006 book:
- L = sample time
- book_mid_L = (bid+ask)/2 (both sides required)
- m_L = PM-008 Kalshi mid at L (completed snapshot ≤ L; no interpolate)
- v_CB = last CB-002 1m with bar_end < L
Missing any → drop row.

## Do not order Clock until
1. Closed 15m both-side count is plausible for N≥80 per headline (now 22/22).
2. PM-008 and CB-002 are recording through those same windows.
3. This spec is unchanged (no A fit).

## Forbidden
Invented Poly mid · last-as-mid · CB-VEL standalone retest · Examiner Δ from this file · mixing CB-002 into CB-001
