# BINARY EXAMINER SPEC — required metrics
**Document:** `BINARY_EXAMINER_SPEC.md`  
**Authority:** Logan M (Human Governor)  
**Date (UTC):** 2026-09-11  
**Classification:** MEASUREMENT SPEC (forecast vs market on actual binary contracts)  
**RETROACTIVE:** **NO**  
**Baseline:** `gauntlet-v2.0-alpha` **unchanged**  
**Sequence position:** after DATA → CONTRACT REGISTRY → ORACLE → HISTORICAL PRICE STATE (`TRACK_B_ORDERS_2026-09-11.md`)  
**Does not:** fetch market data · invent fills · auto-trade · require a cockpit · reuse futures Examiner as a binary scoreboard without this spec

**Patched 2026-09-13:** AMD-20260913-001 (legal scored \(p_t\)); AMD-20260913-006 (named ECE). Baseline `gauntlet-v2.0-alpha` **unchanged**. `RETROACTIVE: NO`.

Companion mission metrics: `PREDICTION_MARKET_MISSION_2026-09-11.md` §6.5. This file is the **operable required list** for Track B. League snapshot table: `archive/templates/STRATEGY_LEAGUE.md`.

---

## 0. Unit of measurement

| Item | Rule |
|------|------|
| **Ground truth** | Contract **resolution** (`YES` / `NO` / `VOID`) on a registered `CONTRACT_ID` |
| **Forecast** | \(p_t = P(\text{YES} \mid \mathcal{I}_t)\) at a declared decision timestamp \(t\) |
| **Market baseline** | \(m_t\) = venue implied YES probability at the **same** \(t\) (benchmark construction declared: mid / microprice / last / other; tag `[A]` if conventional) |
| **VOID / DISPUTED / QUARANTINED** | Exclude from scored N **or** report a separate void bucket — never recode as YES/NO by narrative |
| **Cell** | Pre-register tournament cell (venue adapter, contract family, checkpoint \(t\), side/abstention, cost stack) **before** peeking at outcomes |
| **Missing metric** | **`UNTESTED`** — never blank, never invented, never “N/A” that hides non-measurement |

Forecast metrics are reported **even when** the strategy abstains. Trade authorization is a **separate** gate.

Futures TESTs TEST-20260911-003/004/005 **skipped** the binary scoreboard `[V]`. This spec is the path that was missing — it does not reopen those futures cells.

---

## 0.1 Legal scored \(p_t\) (AMD-20260913-001)

| Item | Rule |
|------|------|
| **Scored range** | A scored \(p_t\) submitted to the Binary Examiner **must** lie in \((\varepsilon, 1-\varepsilon)\) unless Clock has recorded an **algebraic lock** (Map 1) |
| **Raw 0/1** | Legal as unit-test predicates and diagnostics — **not** Examiner inputs |
| **ε-clip** | Numerical hygiene only. **Not** a model of remainder-window uncertainty. Turning \(1\) into \(0.9999\) still asserts near-certainty |
| **Failed map** | Stays failed. A materially different uncertainty map = **new** Feature Card (explicit lineage, independent evaluation) |
| **No rehab** | Does **not** rehabilitate TEST-20260913-001 or FEAT-005. `RETROACTIVE: NO` |
| **Same-\(t\) incumbent** | Claim that \(p_t\) beats \(m_t\) is `UNTESTED` unless mid timestamp = decision timestamp, or Clock recorded why that mid is blocked and named the legal substitute. F2 vs T−1m is **not** a same-\(t\) beat |
| **Learned \(p_t\)** | Not licensed by this AMD; see packet §1.4 / `archive/templates/FEATURE_LEARNED_PT.md` |

## 1. Required metrics (Logan list)

Every Binary Examiner package that leaves `HYPOTHESIS` must report **each** row below or mark it **`UNTESTED`**.

| # | Metric | Symbol / report as | Role | Missing |
|---|--------|--------------------|------|---------|
| 1 | **N** | `N` (scored contracts / scored decision-events — declare which) | Power / honesty. Also report contract count, distinct days/expiry cluster, span UTC | `UNTESTED` |
| 2 | **WR** | `WR` win rate | Directional hit rate of the **scored** action vs resolution (define: \(p_t>m_t\) ⇒ YES-side, etc.). Not a substitute for proper scores | `UNTESTED` |
| 3 | **CI** | `CI` (interval + method) | Uncertainty on WR and on Δ vs market. Name the method (e.g. binomial / bootstrap). If N too small for a named CI → `UNTESTED`, do not fake tight bands | `UNTESTED` |
| 4 | **Brier** | `Brier_model` | Mean \((p_t - y)^2\), \(y\in\{0,1\}\) YES indicator | `UNTESTED` |
| 5 | **logloss** | `LogLoss_model` | Mean binary log loss of \(p_t\) vs \(y\). State eps-clip if any | `UNTESTED` |
| 6 | **calibration** | `Calibration` (ECE / reliability summary + diagram pointer when N allows) | Reliability vs sharpness. If N cannot support bins → `UNTESTED` with reason, not a one-bin theater plot | `UNTESTED` |
| 7 | **market Brier / logloss** | `Brier_market`, `LogLoss_market` | **Same windows, same \(t\), same contracts** as the model. Default benchmark | `UNTESTED` |
| 8 | **delta vs market** | `ΔBrier`, `ΔLogLoss` (model − market; **sign convention declared**) | Primary skill claim. Negative Δ on loss/Brier = better than market **only if** convention is model−market and lower-is-better — **write the convention on the report** | `UNTESTED` |
| 9 | **avg market price** | `mean(m_t)` | Where the market sat at scored checkpoints (plus optional distribution / quantiles). Context for WR and gap | `UNTESTED` |
| 10 | **gap** | `gap` = \(p_t - m_t\) (mean, and distribution) | Forecast-minus-market at \(t\). Report signed mean and \|gap\|. Abstention uses \|gap\| vs costs | `UNTESTED` |
| 11 | **gross / net EV** | `EV_gross`, `EV_net` | Gross: edge from \(p_t-m_t\) under the pre-registered action rule (no costs). Net: after cost stack \(c\). **Not** live P&L. **Not** fabricated fills | `UNTESTED` |
| 12 | **abstention** | `abstention_rate` (+ coverage) | Fraction of candidate \(t\) where \|gap\| ≤ \(c\) (or risk veto) → **NO TRADE**. First-class. Report metrics on **scored** vs **all-including-abstain** if both exist | `UNTESTED` |
| 13 | **cost sensitivity** | `cost_sensitivity` | Repeat net EV / abstention at pre-registered \(c\), \(2c\), \(3c\) (or declared grid). Each cost leg tagged `[V]\[I]\[H]\[A]\[U]` | `UNTESTED` |

**If a metric was not computed: write `UNTESTED`. Do not infer it from a cousin. Do not leave the cell empty.**

---

## 1.1 ECE / calibration (AMD-20260913-006)

Filed with AMD-20260913-001. **Do not invent a new estimator. Do not import a calibrator. No power theater.**

| Item | Binding |
|------|---------|
| **Estimator** | `expected_calibration_error` in `harness/examiner/src/pm002_market_baseline.py` |
| **Bins** | `RELIABILITY_BINS` = [0.02,0.50), [0.50,0.55), [0.55,0.60), [0.60,0.70), [0.70,0.80), [0.80,0.90), [0.90,0.98) — same bins already used on TEST-006/007 |
| **Formula** | Weighted mean |obs_rate − mean_m| over bins with n ≥ `MIN_N_FOR_BIN_RATE_CI` = 20 |
| **UNTESTED when** | N < `MIN_N_FOR_ECE` = 100 **or** `powered_bin_count` < `MIN_POWERED_BINS_FOR_CAL` = 2 |
| **Default comparison** | Model ECE vs market ECE on the **same cell**, same estimator, same bins |
| **Power rule** | Minimum **DISPLAY** rule, not a published-power claim. Thin → `UNTESTED`. Never a pass. Never a silent skip on promote |
| **Honesty** | N ≥ 100 does **not** prove statistical power |

When N cannot support the display rule, report calibration as `UNTESTED` with reason — not a one-bin theater plot, not a silent omit on promote.

## 2. Sign conventions & formulae (frozen for reports)

Let \(y=1\) if resolved YES, else \(0\) (VOID excluded per §0).

**Brier (model):** \(\frac{1}{N}\sum_i (p_{t_i}-y_i)^2\)  
**Brier (market):** \(\frac{1}{N}\sum_i (m_{t_i}-y_i)^2\)  
**ΔBrier:** `Brier_model − Brier_market` (lower model Brier than market ⇒ ΔBrier \(< 0\) = skill). Write this sentence on every report.

**Log loss (model):** \(\frac{1}{N}\sum_i -\big[y_i\log p_{t_i}+(1-y_i)\log(1-p_{t_i})\big]\) (clip \(p\) only if declared).  
**ΔLogLoss:** `LogLoss_model − LogLoss_market` (same lower-is-better convention).

**Gross edge (YES side):** \(e^{\mathrm{gross}}_{\mathrm{YES}}(t)=p_t-m_t\)  
**Net edge (YES side):** \(e^{\mathrm{net}}_{\mathrm{YES}}(t)=p_t-m_t-c_{\mathrm{YES}}\)  
**NO side:** \(m_t-p_t-c_{\mathrm{NO}}\).

**EV_gross / EV_net:** mean of the pre-registered side’s edge over **acted** events (or over all events — declare). Paper economics only.

**WR:** among acted events, fraction where the taken side matches resolution. If the strategy always abstains, WR is `UNTESTED` (not 0, not 1).

**CI:** at minimum on WR and on ΔBrier / ΔLogLoss when N allows; otherwise `UNTESTED`.

Market price is the benchmark (`PREDICTION_MARKET_MISSION_2026-09-11.md` §14). Beating 50/50 alone is **not** a skill claim.

---

## 3. Segmentation (report separately — never pool as a single claim)

| Cut | Rule |
|-----|------|
| **Venue adapter** | `KALSHI` vs `POLYMARKET_GLOBAL` (co-primary); `POLYMARKET_US` only if sample exists |
| **Underlying** | BTC vs ETH |
| **Horizon / tenor** | 5m vs 15m (and any other listed tenor) — **separate** |
| **Checkpoint \(t\)** | Each pre-registered checkpoint (e.g. T−15m, T−5m, trade cutoff) — **separate** |
| **Side** | YES-acting vs NO-acting vs pooled-with-rule |

Robustness annexes are allowed; they must not replace the pre-registered primary cell.

---

## 4. Gates (Binary Examiner)

| Gate | Binding |
|------|---------|
| **Sample honesty** | If N or distinct-expiry/day gates (pre-registered) are missed → overall `FAIL-INSUFFICIENT` or package-level `UNTESTED` — **not** a powered `NO_EDGE`. Same interpretation as Cycle 5 close: **FAIL-INSUFFICIENT ≠ proven absence of edge** |
| **Leakage** | Features or \(m_t\) unknowable at \(t\) → Clock/Examiner kill (`DATA_FAILURE` / leakage). Resolution after \(t\) grades; it does not enter \(\mathcal{I}_t\) |
| **Redundancy** | Ablate vs market \(m_t\) alone and vs trivial contract metadata. Copy-the-market is the **baseline**, not a Champion |
| **Cemetery reuse** | Dead Edges enter only as **Feature Cards** citing CEM ids (`TRACK_B_ORDERS` §5) |
| **Holdout** | Historical sealed holdout / forward window per constitutional path; no validation laundering (`DATASET_USE_LEDGER`) |
| **Cockpit** | **Not required** to run this Examiner. Do not wait on UI |
| **Trade** | PASS on forecast metrics ≠ Mechanic executable ≠ Treasurer capital |

Invented_numbers must be `false`. No fabricated Sharpes or live P&L.

---

## 5. Package outputs (when Conductor routes)

Minimum Examiner artifacts per TEST:

1. Machine-readable JSON with every required metric key present (`UNTESTED` allowed; key absence forbidden).  
2. Human markdown: cell id, N, WR, CI, Brier/logloss ± market ± Δ, calibration, mean \(m_t\), gap, EV gross/net, abstention, cost sensitivity, BTC/ETH, venue, checkpoint.  
3. Pointers: `CONTRACT_ID`s scored, DATA-* , rules hashes, Clock VERDICT, cost stack tags.  
4. Verdict: `UNTESTED` / `FAIL-INSUFFICIENT` / `FAIL` / `PASS` (PASS still does not auto-trade).

Implement against the first-milestone resolved sample — **after** that sample exists. This spec does not authorize a fetch.

---

## 6. Pointers

| Doc | Role |
|-----|------|
| `TRACK_B_ORDERS_2026-09-11.md` | Sequence; first milestone; no cockpit; no new science family |
| `PREDICTION_MARKET_MISSION_2026-09-11.md` | Domain formulae; L1/L2/L3 |
| `CYCLE_5_CLOSE_2026-09-11.md` | FAIL-INSUFFICIENT interpretation |
| `archive/templates/BINARY_CONTRACT.md` | Per-contract ground truth |
| `archive/templates/CONTRACT_REGISTRY.md` | Sample universe ledger |
| `archive/templates/STRATEGY_LEAGUE.md` | League metric snapshot (must use this list) |
| `archive/templates/FEATURE.md` | Forecast-input reuse of dead Edges |
| `AMD-20260913-001.md` | Legal scored \(p_t\); same-\(t\) incumbent |
| `AMD-20260913-006.md` | Named ECE estimator; display/power rule |
| `GOVERNOR_PACKET_2026-09-13.md` | Stamp source |

---

*End BINARY EXAMINER SPEC — 2026-09-11; patched 2026-09-13 (AMD-001 legal p_t; AMD-006 expected_calibration_error). Required metrics: N, WR, CI, Brier, logloss, calibration/ECE, market Brier/logloss, Δ vs market, avg market price, gap, gross/net EV, abstention, cost sensitivity. Missing = UNTESTED. RETROACTIVE: NO.*
