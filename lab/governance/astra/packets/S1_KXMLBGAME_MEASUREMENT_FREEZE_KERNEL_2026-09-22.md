# S1 — KXMLBGAME measurement kernel — FREEZE 2026-09-22 (ET)

**Packet ID:** S1-KXMLBGAME-MEAS  
**Scout series:** `KXMLBGAME` (MLB game moneyline binaries)  
**Owner (freeze):** Deep Research  
**Implementer (later):** Collector (panel) → Simulator (markout harness) → Examiner (Kalshi)  
**Reviewer:** Conductor triage; Adversary on fee-blind / clock SoT  
**Status:** **FROZEN** — results/pnl **null** (not run)  
**Cite:** Conductor assign 2026-09-22; Scout brief + triage TRY; R2-P2; R1-P1 feebook; R1-P5 rails  
**Repo (future lab dir):** `17thgreen/GPT-6-Astra-Deathmatch` → e.g. `kalshi_mlb_game_meas_lab_20260922/` (do not mutate Q6/Q7/capital labs)  
**Hard rules:** No live orders. No invented PnL. No Q6-`000` signal retune. No capital-structure arms. **Must** bind R1-P1 feebook + R1-P5 rails — **forbid** inherited Q7/Q6 `0.0175`/`0.07` fee literals.

---

## Intent (one measurement kernel)

Measure whether the NFL T−7d→T−3h **timing / microstructure lab objects** generalize to **daily MLB** `KXMLBGAME` books under **fee-honest + content-fresh** instruments — without porting the Q6-`000` allocator or inventing maker EV.

**Not a strategy.** Pre-settlement measurement only until Examiner opens a scorecard after freeze+units.

---

## Dead-card / live-pin overlap (named)

| Pin / card | Overlap | Handling |
|---|---|---|
| Q6-`000` KEEP | **None on signal** — this packet does not quote, size, or route like `000` | Subject is MLB series microstructure, not NFL paired allocator |
| Q7 pair-check / Arm B KILL | **None** — no pair-check knob | Cemetery CEM-ASTRA-20260922-001 stands; do not reopen |
| Capital-structure A1/A2/A3 | **None** — no wallet/slice arms | Separate freeze in flight |
| Crypto F1–F3 / Gauntlet | **N/A** | Idle science |
| More `KXNFLGAME` MM | **Explicitly out** | Scout excluded; incumbent territory |
| R2-P1 fee hygiene on `000` | **Complementary, not duplicate** — R2-P1 stresses fee on NFL `000` tape; S1 stresses feebook+rails on **MLB** tape | May share feebook/rails libs only |
| R1-P3 adverse objects | **Optional join later** if external odds present | Not required for first freeze; bot port remains KILL |
| R2-P4 SPREAD/TOTAL | **Distinct** | Deferred until C1 PIT@CLE |

---

## Mandatory instrument pins (not inherited Q7 fees)

| Dep | Pin | Rule |
|---|---|---|
| Fee | R1-P1 `kalshi_feebook_lab_20260922/` @ `22371178cb2663250b4762f328069571c48cb551` (or Archivist-updated tip if re-pinned) | Reciprocal book + `order_fee` / `round_up` / series maker flag via feebook API only |
| Rails | R1-P5 `kalshi_rails_lab_20260922/` @ `6a28e0d6254327ea4e6451c781bec56215ac6cac` | `content_fresh_flag`, `maker_credit_floor_zero_refuse`, `queue_attribution_bin` labels — instrument only |
| Kickoff / close SoT | Kalshi public event `occurrence_datetime` / market close fields | Do not mix holdout NFL +3h clocks into MLB windows |
| Capture | GET-only public elections host allowlist (events, markets, orderbook, trades) | Same Collector discipline as ADMIT-1; no signed trading host required for public GETs |

**Refuse gate:** any completed-profit label without feebook fee channel → refuse. Freshness from content/transaction time, not WS ping.

---

## Measurement objects (pre-settlement)

For each admitted `KXMLBGAME` event / YES-NO market pair, at each sample time `t` with `content_fresh_flag=true`:

1. **Reciprocal book:** `bid_YES`, `bid_NO`, `ask_YES=1-bid_NO`, `ask_NO=1-bid_YES`, `spread_YES` (R1-P1 Pin A).  
2. **Fee channel on any fill or hypothetical fill size C at P:** R1-P1 `order_fee` (taker 0.07 / maker 0.0175 or series override) — never shadow literals.  
3. **Rails labels:** `maker_credit_floor_zero_refuse`, `queue_attribution_bin` vs reference rails defaults (3300 / 10000 as **labels**, not strategy claims).  
4. **Timing shape:** minutes-to-scheduled-close (or occurrence), liquidity proxies from public `volume_fp` / `open_interest_fp` **as raw API only** (not invented depth).  
5. **Adverse mid markout (pre-settlement):** mid change over short horizons (e.g. 1m / 5m / 15m) conditional on touch trade — **no** outcome P&L required for first unit page.

**Explicitly null until Examiner run:** `results`, `pnl`, fill rates as strategy EV, annualization, live promotion.

---

## Panel / cohort (freeze rule — admit is Collector)

- Series: `KXMLBGAME` only.  
- First implementable panel: **bounded same-day or next-day slate** after Conductor/Collector admit (do not backdate).  
- Do **not** steal NFL ADMIT-1 / PIT@CLE poll budget; separate panel version string required.  
- Suggested panel_version pattern: `2026-09-22.s1-kxmlbgame-v0` (Collector owns final admit stamp).

---

## Arms (optional contrast — still one kernel)

If Simulator needs a factorial later, **one knob only**: markout horizon ∈ {`1m`, `5m`, `15m`} with feebook+rails fixed.  
**Not arms:** capital slices; Q6 signal; pair-check; queue as strategy; external odds bot.

First PR may be **schema + unit fixtures only** (empty results unchanged).

---

## Do-not-modify

1. No live orders / no live launcher.  
2. No invented PnL / no author-wallet anecdotes as evidence.  
3. No Q6-`000` retune; no Q7 reopen; no capital A2/A3.  
4. No scoring with inherited Q7/Q6 fee literals.  
5. No silent panel backfill.  
6. Do not mutate feebook/rails/Q labs — new MLB meas lab dir when implementing.  
7. Do not expand to `KXNCAAFGAME` / `KXMVENFL*` in this packet (Scout defer/skip).

---

## Empty results (on disk)

- `packets/scout_s1_kxmlbgame/FROZEN_EXPERIMENT.json` — `results`/`pnl` null  
- `packets/scout_s1_kxmlbgame/results.json` + `results/EMPTY_RESULTS.json` — `NOT_RUN`

---

## Done =

Freeze packet on disk + Conductor ping with path. Implementation / admit / Examiner score = later seats.

## Frozen-at

`2026-09-22T22:57:55+00:00` UTC. Desk 2026-09-22 ET.  
Deep Research freeze under Conductor assign (Scout S1).
