# Kernel extract — TradingView teach clip (2026-09-14)

**Source:** Logan teach recording `teach-20260914T003910Z` (TradingView chart `vjOMz6eD`).
**Posture:** Conductor extract only. **Not** READY. **Not** a TEST. **Not** a TV backtest.
**Stamp:** 2026-09-14T01:12:05Z
**Trade:** FORBIDDEN

## Surface (what the clip showed)
Signed-in TradingView. GME 5m then Bitstamp `BTCUSD` 1m. Interval menu included 1s / 5s / 1m / 5m. Free-plan indicator cap → pricing page (tick charts listed as Ultimate). Favorites opened.

On-chart / favorites as a **catalog** (names only; do not import signals):
MACD · Lorentzian Classification · LuxAlgo SMC · EMA Stack 3T v.3 · 4MA · Squeeze · Trade Statistics · TTM Squeeze · ML kNN / Lorentzian · ChatGPT-labelled MACD+RSI+ADX · order blocks / harmonics / reversal overlays.

TV strategy tester / win-rate panel **is not Examiner**. Buying Premium does not waive Clock.

## Dead-card overlap (refuse as Feature)
| Object on the chart | Nearest dead card | Note |
|---------------------|-------------------|------|
| EMA stack / 4MA / MACD sign | FEAT-20260913-005 CB-VEL | Smoothed signed 1m velocity |
| Lorentzian / kNN / “ChatGPT strategy” | black-box overlay | Cannot reconstruct under lock B |
| SMC / order blocks / harmonics | unfrozen geometry | No Clock-joinable definition |
| Trade-stats / strategy report | — | Not a Δ |
| Tick / 5s bars | new tape | NEEDS_DATA; not a subscription |
| Bitstamp close vs Coinbase/L3 | W2-B family (different venues) | Cross-spot ≠ Poly last vs Kalshi mid |

## Measurement kernel (UNTESTED)
**Squeeze / compression speak-gate** (complementary to dead F4 wick).
- Object: BB-inside-KC / TTM-style squeeze on **completed** 1m (CB-001 or L3), lock B (`bar_end < t`)
- Gate: off-squeeze → `p = m`. On-squeeze → Feature may speak (map frozen **before** any sheet)
- Incumbent = Kalshi same-t mid
- Nearest dead: FEAT-20260914-008 (F4 wick = **expansion** `|ln return| > θσ√dt`, not BB-in-KC)
- Do not Examiner-score a TV overlay. Reconstruct on our tape. Clock owns the join.

## Forbidden readings
TV backtest as skill · θ retune of F4 · Lorentzian as p_t · tick-chart purchase as a data plan · trade

## Why squeeze was isolated (Governor asked 2026-09-14)
Lorentzian Classification prints buys/sells plus a Trade Stats panel (winrate, W/L, early flips) on 1m. That panel is a TV strategy report on the chart symbol, **not** ΔBrier vs Kalshi mid. The clip's Strategy Tester was empty ("requires trade data"). Even when filled it does not waive Examiner.

Lorentzian as a Feature is refused until a frozen kNN (named features, k, completed-bar only, lock B) is reconstructed on lab tape. TV labels and TV winrate are not that reconstruction. Directional 1m labels overlap **FEAT-20260913-005 CB-VEL** and unconditional speak overlaps **F1**.

Squeeze was isolated as the only catalog object that is (1) algebra we can reconstruct (BB/KC, completed 1m), and (2) orthogonal to dead F4 (F4 = expansion wick; squeeze = compression). Off-squeeze → p = m. Not a TV overlay score.

