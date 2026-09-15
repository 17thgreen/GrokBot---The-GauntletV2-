# PolyOrderbooks scope — 2026-09-14 (not a TEST)

**Stamp:** 2026-09-14T03:52Z · Conductor
**Account:** Starter (logged-in dashboard). Key on disk, not in git.
**Trade:** FORBIDDEN. Vendor replay ≠ Examiner.

## What Starter actually is (probed)

| Item | Live fact |
|------|-----------|
| Plan | `GET /v1/usage` → starter · 60/min · 1s granularity · **3 days** history |
| API | Key works. Markets search 200. |
| Sep 4–11 L2 | **403** earliest `start_ts` **2026-09-11T03:46:02Z** |
| Sep 11 04:00Z+ | **200** full L2 (`bids`/`asks` `[price,size]`, ~50 levels) |
| AI quota | 1 NL backtest / month (0 used) · 3 Strategy Builder (0 used) |
| Builder window | docs: Starter `days` cap **1** |
| Paid for research week | **$19/mo** 30-day window. Do not buy from this file. |

## Backtest AI (docs + OpenAPI, not Examiner)

`POST /v1/ai/backtest` — prompt **or** structured `strategy`.

- **Signals allowed:** Polymarket **token prices in (0,1]** and archive L2. **No BTC/ETH spot. No Kalshi mid. No percentages.** Those 400 `unsupported_signal`.
- **Entries:** price threshold / time-into-window / OR. Not book-velocity vs Coinbase.
- **Exits:** TP / SL / hold-to-expiry / trailing / max-hold / exit-before-close.
- **Fills:** claimed ladder walk; documented fill_sources include `book_ladder`, `best_quote`, **`last_price`**, `settlement`. Example report used `last_price`.
- **Outputs:** win_rate, PnL, profit factor, drawdown, equity curve — **Poly-token trading P&L**, not ΔBrier vs Kalshi mid.
- Starter can call it (usage lists quota). Do **not** spend the 1 NL credit unless Logan signs a specific prompt. Follow-vs-fade **cannot** be expressed in this engine.

## What we kicked

DATA-PROV-PM-009: 1m last-book per closed 15m, BTC+ETH, from 2026-09-11T04:00Z through last closed window (~574 jobs). Sleep 1.15s. Not Clock until a join spec + N. Sep 12 is PM-004 week and ages off Starter ~2026-09-15T03:46Z.

## Dead-card / leftover overlap

- Vendor “buy DOWN if token < 0.45 in first 5m” = Poly-price rule, **not** F1/F4, **not** follow-vs-fade.
- Follow-vs-fade still needs Kalshi same-t mid (PM-008 live; PM-004 for Sep 12) + CB 1m. This tape fills the **Poly book** hole for the 3-day window only.

## Forbidden

Treat vendor winrate as a gate · burn AI credit as a TEST · upgrade from this file · Examiner on thin live PM-006

## Site walk (2026-09-14T03:54Z)

Credits **not** spent. Run Backtest consumes the 1; Strategy Builder consumes one of 3. Backtest Agent BETA = Chat/Code/Results; same quota.

Free catalog (CC BY 4.0) is **not** Sep 4–11:
- BTC 5m sample: **2026-08-13T04:50–04:55Z** (`btc-updown-5m-1786596600`)
- Zenodo DOI `10.5281/zenodo.22084114`: Aug 21–24 research dump (already hunted)
- HF/Kaggle 5m mirror: Aug slice (already hunted)

No webhooks in product nav.
