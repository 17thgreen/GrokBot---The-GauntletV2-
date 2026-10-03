# VARIANTS HOLDOUT MAKER-NULL FEASIBILITY NOTE — Q6S5 KXMLBSPREAD (pre-reg ACCEPT 9a987a77)

**Status:** `DESIGN_ONLY_LABEL_FREE`. Descriptive feasibility only. No settlement or label was read, and no PnL or ROI was computed. `results = null`, `pnl = null`, `roi = null`.
**Filed by:** R&D Variants ("KALSHI"), Astra/Kalshi desk. **Drafted:** 2026-10-02 ~09:56 ET, on the box.
**Answers:** Conductor KICK `packets/CONDUCTOR_KICK_VARIANTS_HOLDOUT_MAKER_NULL_FEASIBILITY_2026-10-02.json`, sha256 `2a072aa01ed3881751fd3d3d1b68c25c75ba297a159666192937f8b92deb4da9` (re-hashed: **MATCH**).
**Tags:** `[V]` = verified from a pinned file by the scripts in `/workspace/v_holdout_feas/`. `[I]` = inference. `[H]` = hypothesis or proposal.
**Scope guard:** Sep-24 and Sep-25 KXMLBSPREAD are described here **only** as examples of book/tape regimes, to judge feasibility. They are not reopened as strategy evidence. No frozen fill, queue or quote rule is changed or proposed for change. The ADMIT-1 window `[2026-09-27T00:00Z, 2026-09-30T04:00Z)` is excluded (0 rows fell in it). Lee-Ready is refused. No GET, no `admit.py`, no sqlite, no orders.

---

## 0. Bottom line

**Verdict on 9a987a77 maker legs: NO, they are not null by construction. → GO for the untouched holdout capture, with no amendment.**

1. `[V]` The pre-reg's maker legs are H_a `maker_gross_roi[Q6S5FL1] > 0` and H_b `maker_gross_roi[Q6S5FL2] − maker_gross_roi[Q6S5FL1] < 0`, with label `public_counterparty_realized`. The metric is `Σ q·(p_taker − Y_s) / Σ q·(1 − p_taker)` over **every eligible native public print** (addendum `370dc31d…` §4, §5.1, §5.8). It scores the passive counterparty of prints that actually happened. It never places, simulates or queues an order of ours.
2. `[V]` The holdout inputs are the panel + Clock stamp, the per-ticker trade pages and the settlement GETs (§3.2). **No orderbook is an input**, so `queue_ahead` cannot even be computed inside the holdout scoring. The 9f50ba19 back-of-queue rule (`public_trade_through_conservative`) belongs to the Q6S5 strategy-fill packet (A0/A1). Nothing in `370dc31d…` (md + json) or `9a987a77…` cites it: rg finds no `queue_ahead`, `public_trade_through` or `9f50ba19`, and the only `fill_model` mention is "fill_model PR60" in the in-sample family-size list (§6).
3. `[V]` Under the pre-reg's own definition, a maker leg is null only if an eligible game has **no FL1 native print** (FL1 `maker_capital_usd = 0`, §3.6). On the pinned tapes, FL1 maker capital is > 0 in **6 of 6 games**: 3/3 Sep-24 and 3/3 Sep-25, even though the Sep-25 tape is a thin pregame tape of 21 prints (table §4).
4. `[V]` The back-of-queue rule **would** null an own-order maker leg on pregame books like Sep-25. There, 0/30 windows could fill, and 0/30 even under the best-case bound that uses all window volume. That is a risk for the **downstream money-path freeze** that a holdout KEEP would open (§5.6, "FL1-only maker band filter on the Q6S5 maker leg"). It is not a risk for the holdout read. §6 has a non-binding advisory for that later freeze.

## 1. Inputs (all sha256 re-hashed on the box; full list in the JSON twin)

| Input | sha256 | Check |
|---|---|---|
| Authentic bundle `/workspace/Q6S5_PR60_SCORABILITY_authentic_pins_2026-10-02.tgz` | `bd94757c4c5748fc3447cf596435ddee0af129c87599d4c48f002b2b61756308` | MATCH vs ACCEPT ping `c176b2b5…` |
| Its `BUNDLE_MANIFEST.sha256` (156 files) | `ef95994d2e2b5d530fb5b2598bfd47453d8a04585d4d1ff422efe662b35d9c19` | `sha256sum -c` 156/156 OK; = ping `bundle_manifest_sha256` |
| `SOURCE_PINS.json` (closed tape manifest, PR60 / 213ee6dd R02) | `1846a9710375dd418983e1a03e05ac15386138ada7c405923b7fd0514cf116a1` | MATCH; inputs_core 9 + inputs_raw 87 each re-hashed before read, and each equals the BUNDLE_MANIFEST entry |
| Holdout pre-reg Conductor ACCEPT | `9a987a77e6cd6293ddaeb14fadbf33a25c1a6cc392af25f46eaaaaae33ebb273` | MATCH (found by `sha256sum packets/*`) |
| Holdout addendum md / json (pinned by 9a987a77) | `370dc31df17191446013b6cebb52d44ee8346f47d2f5b543a1c73049ba52c063` / `a76d2673f85a817af435deb2f70ec8b421ac3d8d2eb57f601eb4da39927d9865` | MATCH vs 9a987a77 `pins` |
| PR60 strategy-fill freeze | `9f50ba19694083c774bbe2a6cff491d1a2f81ed3a6f9cc21a3641a938c84955d` | MATCH |
| Feequeue harness freeze | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` | MATCH |
| PR60 scorability freeze | `213ee6dd33f292c8041977b0b8d7566da9412fd3debe0597643c500dc1e42db4` | MATCH |
| PR64 Conductor ACCEPT | `57a9f5e68f41cf6df1428d2516ace34550267f264396d486f245977a571a871c` | MATCH vs kick |
| MAXIMIZE pin 0949ET md | `151e2870308e8df9dfa791501e1581028948f5f1fa85a74aa074d68e49f0748c` | read for context |
| Prior verify cross-check `/workspace/v64/independent_counts.json` / `independent_recompute_output.txt` | `1627ee7e…` / `54ffe825…` | per-order Sep-25 queue/depletion: my recompute agrees on all 30 orders |

**Sep-24 source.** The same SOURCE_PINS (`1846a971…`, also inside strategy-fill bundle `6602e07e…`) pins the 26SEP24 games' dated books, market GETs and full trade pages (HOUATH, LAASEA, SDLAD). Those are the authentic Sep-24 tape and books. I checked bundles `6602e07e…`, `6576ee6c…` and `63b5d981…` for hashes only and did not use them as extra inputs. **Data gap `[V]`:** every pinned Sep-24 book was captured 2026-09-25 04:44–05:20Z (00:44–01:20 ET), at or after the end of the Sep-24 games. **No pregame or mid-game Sep-24 book exists on the box.**

**Not read:** `settlement_only_2026-10-02/*`, the join manifest, any `result` / `settlement_*` field (the script asserts that none of these field names appear in its output), `capture.sqlite`, and the weather db. From market GETs I read only `status` and `close_time`. I did **not** reuse the settled-join half of `/workspace/v64/independent_recompute.py`. Also, `/workspace/v64/REPORT.md` holds no per-order data; that data is in `independent_recompute_output.txt`.

## 2. Frozen definitions (quoted, not reinterpreted)

- **Window / placement, 9f50ba19 L74–L75:** "Placement instants: each dated measured orderbook snapshot `(ticker, captured_utc)` … but **only** if the latest measured market GET for that ticker at or before `captured_utc` shows `status == "active"`." "Maker legs (per placement × side ∈ {yes, no}): a 1-contract post-only limit bid at the **best displayed bid** for that side …, joining the **back** of the queue. `queue_ahead = displayed size at that price in the snapshot`. **Cancel/replace:** the order is cancelled (model) at the next measured snapshot of the same ticker. … The last order rests until the earliest of: a market GET showing status ≠ active, or the per-ticker trades request `ts_utc` (tape end)."
- **Queue / fill rule, 9f50ba19 L84–L85 (= 213ee6dd R17):** "3. **Conservative queue depletion:** `cum` = sum of `count_fp` over our-side prints with `yes_price_dollars ≤ p` since `t0`. No credit is given for cancels or modifies ahead of us. … 4. **Fill:** at the **first** our-side print with `yes_price_dollars < p` (strictly through) at which `cum` (including that print) is ≥ `queue_ahead + 1`."
- **Resolutions applied, 213ee6dd:** R04 (filename stamp = `captured_utc`), R05, R06 (max level), R08, R09, R11–R13 (print window `floor_s(created_time) > t0` and `< cancel`; tape end = earliest `ts_utc`), R14 (native fields agree; YES bid ← `taker_side=="no"`), R15 (block excluded) and R16 (yes+no = 1 exactly).
- **4f65dcdf** defines no window or queue rule. Its p16 item 7 is "fill_model n/a; no fills; invent fills REFUSED", and its arms Q6S5A0/A1 carry into 9f50ba19 verbatim.
- **Note on the kick wording:** the kick paraphrases the rule as "strictly-through print, **or** depletion ≥ queue_ahead+1". The frozen text requires **both**, in order. I report the frozen condition and, separately, each half and their union (OR) as looser necessary-condition counts. On these tapes all of them coincide.
- **Applying them to Sep-24 is descriptive only.** 213ee6dd closes Sep-24 to its runner (`ClosedUniverseRefused`). Nothing here is a fill, and nothing is a scorable row.

## 3. Queue at the touch vs traded volume, per window `[V]`

Per window (market × side × placement): `queue_ahead`, same-side volume (our-side prints, any price), total window volume (all prints, both sides, any price), prints at the touch, prints strictly through, depletion, and `depletion/(queue_ahead+1)`. Per-window rows are in the JSON twin (`maker_windows`).

**Eligibility `[V]`:** there are 29 dated books.
- Sep-24: 14 books. 12 were refused by the status gate: HOUATH and LAASEA ×all were `finalized` with empty books, SD2 at 05:08:26 was `determined`, and SDLAD at 05:19/05:20 was `finalized`. That leaves **2 placements → 3 maker windows + 1 empty side** (LAD2 YES side had no bid; no order, per R08).
- Sep-25: 15/15 books are eligible → **30 maker windows**.
- Crossed books 0, block 0, price-inconsistent 0, native conflicts 0, ADMIT-1 exclusions 0. There are 11,744 raw prints in total.

| Distribution (min / p25 / median / p75 / max) | Sep-24 (n=3 windows, 1 game) | Sep-25 (n=30 windows, 3 games) | Pooled (n=33) |
|---|---|---|---|
| window length (min, per placement) | 11.65 / 13.90 / 16.15 / 18.40 / 20.65 | 20.63 / 20.65 / 21.27 / 29.02 / 51.28 | 11.65 / 20.65 / 21.27 / 28.82 / 51.28 |
| **queue_ahead** (contracts) | 4,888.27 / 6,834.94 / **8,781.61** / 48,082.71 / 87,383.81 | 296.00 / 2,572.38 / **7,177.56** / 19,010.80 / 31,005.84 | 296.00 / 2,690.26 / **7,192.06** / 19,082.35 / 87,383.81 |
| **same-side volume** | 0 / 30,009.53 / **60,019.06** / 60,360.76 / 60,702.46 | 0 / 0 / **0** / 0 / 357.00 | 0 / 0 / 0 / 0 / 60,702.46 |
| total window volume | 0 / 60,360.76 / 120,721.52 / 120,721.52 / 120,721.52 | 0 / 0 / 0 / 8.00 / 357.00 | 0 / 0 / 0 / 9.00 / 120,721.52 |
| prints at touch | 0 / 1 / 2 / 4.5 / 7 | 0 / 0 / 0 / 0 / 2 | 0 / 0 / 0 / 0 / 7 |
| prints strictly through | 0 / 82.5 / 165 / 170.5 / 176 | 0 / 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 / 176 |
| depletion (cum ≤ p) | 0 / 10,684.14 / 21,368.28 / 24,997.61 / 28,626.93 | 0 / 0 / 0 / 0 / 357.00 | 0 / 0 / 0 / 0 / 28,626.93 |
| depletion/(q+1) | 0 / 1.217 / 2.433 / 4.144 / 5.855 | 0 / 0 / 0 / 0 / **0.0187** | 0 / 0 / 0 / 0 / 5.855 |
| total vol/(q+1) | 0 / 6.87 / 13.75 / 19.22 / 24.69 | 0 / 0 / 0 / 0.0012 / **0.0496** | 0 / 0 / 0 / 0.0014 / 24.69 |

**Fillability counts `[V]`:**

| Count | Sep-24 | Sep-25 | Pooled |
|---|---|---|---|
| frozen rule condition met (strict-through print with cum ≥ q+1) | **2/3** | **0/30** | 2/33 |
| depletion ≥ q+1 | 2/3 | 0/30 | 2/33 |
| any strictly-through print | 2/3 | 0/30 | 2/33 |
| union (depletion ≥ q+1 OR any through) | 2/3 | 0/30 | 2/33 |
| **best-case ceiling:** ALL window volume (any side, any price) ≥ q+1 | **2/3** | **0/30** | 2/33 |

- Sep-25 agrees with PR64 `57a9f5e6…` ("max depletion 357 vs queue 19,082"). The largest best-case ratio is 357/(7,192.06+1) ≈ 0.050, so the whole window's tape would need about 20× more volume just to clear one queue `[V]`.
- **Sep-24 regime `[V]`+`[I]`:** both Sep-24 windows that met the condition are the single SD2 placement at 04:47:47Z (00:47 ET), about 2h37m after the 22:10 ET ticker time code. That is late in-play: 571 prints / 120,721.52 contracts in 20.65 min, and the market was `determined` at its next GET.
  - Prices were YES 0.91 / NO 0.08, so the counterparty taker bands are FL0 and FL2, **not FL1**.
  - The third Sep-24 window (LAD2 NO at 0.99, q = 87,383.81) saw 0 prints.
  - `[I]` This is a near-resolution sweep. It does not represent the mid-band pregame/in-play regime that the holdout's FL1 arm covers.
- **FL1-counterparty windows only `[V]`:** all 30 Sep-25 windows. The frozen-rule count is **0/30** (exact Clopper–Pearson 95% CI 0–11.6%).

**Base rate and uncertainty `[V]`/`[I]`.**
- Frozen-rule fill condition: pooled **2/33 = 6.1%** (CP95 0.7%–20.2%), Sep-25 **0/30** (CP95 0%–11.6%), Sep-24 **2/3** (CP95 9.4%–99.2%).
- `[I]` **n is small and heavily clustered.** The 33 windows come from 17 placements in 4 games, within about 46 minutes of clock time per date. Windows on the same ticker share prints and near-identical queues, so the effective n is closer to 4 games than 33. Neither date is a random draw of holdout regimes: Sep-25 is far pregame, Sep-24 is a resolution sweep. Treat the rates as regime illustrations, not as an estimate of a holdout fill rate.

**Time-to-deplete inference `[I]`.** I took each leg's same-side volume rate over its ticker's whole pinned tape and asked how long that rate would take to clear `q+1`.
- Sep-24: 41, 65 and 353 min.
- Sep-25: 17/30 legs have no measurable rate (≤1 print or 0 same-side volume on the whole tape). The other 13 need 1,371–1,316,958 min (about 23 h to about 2.5 years).

**Supplementary clock-bin view `[I]`** (fixed 20-min bins, not a frozen window; phase proxy = event-ticker time code, not first pitch; total volume, both sides):

| Tape / phase proxy | bins | zero-volume bins | bins ≥ Sep-25 min q+1 (297) | ≥ p25 q+1 (2,573) | ≥ median q+1 (7,178.6) | ≥ p75 q+1 (19,011.8) |
|---|---|---|---|---|---|---|
| Sep-24 pre-start | 368 | 148 | 95 | 32 | **11 (3.0%)** | 6 |
| Sep-24 post-start | 54 | 0 | 54 | 47 | **36 (66.7%)** | 28 |
| Sep-25 pre-start (only phase on tape) | 40 | 24 | 2 | 0 | **0** | 0 |

`[I]` Displayed touch depth of thousands to tens of thousands of contracts is clearable inside about 20 minutes mostly **in-play**. Pregame it almost never is, and this is total volume, which is a ceiling on same-side at-or-through volume. Caveat: the Sep-24 pre-start bins are compared against **Sep-25** queue sizes, because no Sep-24 pregame book is pinned.

## 4. Would the holdout maker legs have rows? Label-free band counts `[V]`

Row rules follow addendum §3.4 verbatim (native side only; `p_taker` from the native side; exclude |yes+no−1| > 1e-9, block, and `created_time ≥ close_time`, using `close_time` from the latest pinned GET). **Not applied:** the `result ∉ {yes,no}` market filter, because applying it needs a label. Prices are used for band counts only, which §3.5 allows. The `pre/post` flag uses `2026-09-25T04:37:47Z` (strict `<`). 6 rows were excluded as at/after close; there were 0 other exclusions.

| Game | FL1 rows pre / post | FL1 contracts (all) | FL1 maker_capital_usd = Σq(1−p_taker) (all) | FL2 rows (all) |
|---|---|---|---|---|
| Sep-24 HOUATH | 2,477 / 0 | 594,232.08 | 276,477.50 | 341 |
| Sep-24 LAASEA | 1,659 / 0 | 268,198.81 | 151,224.09 | 310 |
| Sep-24 SDLAD | 4,305 / 127 | 748,707.27 | 390,543.97 | 1,103 |
| Sep-25 PITDET | 2 / 3 | 383.50 | 255.23 | 0 |
| Sep-25 TBPHI | 6 / 4 | 418.46 | 247.34 | 0 |
| Sep-25 NYMWSH | 3 / 3 | 625.97 | 307.12 | 0 |

- Cross-check `[V]`: the Sep-24 pre-cutoff row total of all bands is **10,680**, which equals Examiner SCORE `2e74f17b…` as quoted in addendum §2.
- `[I]` FL1 maker capital is > 0 in 6/6 games. That includes Sep-25, where the whole tape was a pregame trickle of 21 prints, and the holdout captures a full game life (§3.3 rule 2 requires first pitch after admission).
- The H_a leg needs only ≥ 1 eligible FL1 print per game to count toward `n_min`, so it is **not null by construction**. H_b needs FL2 capital too. The FL2 count is 0 in all 3 Sep-25 pregame tapes and > 0 in all 3 Sep-24 full-life tapes. `[I]` FL2 prints concentrate where prices go extreme, which is mostly in-play. H_b already has its own pre-declared fallback: "If `n_b' < 20`, H_b is descriptive only" (§5.3). So it cannot be silently null either.
- `[H]` The binding feasibility risk for 9a987a77 is **game count**: n_min = 30 finalized games in the postseason / next season (the addendum's own §3.6 caveat). It is not maker nullity. That risk is already handled by the pre-declared `NOT_SCORED_INSUFFICIENT_N` → stays sealed.

## 5. Verdict

**NO — the maker legs of holdout pre-reg 9a987a77 (H_a FL1, H_b FL2−FL1) are not null by construction under the frozen back-of-queue rule, because that rule does not enter their definition.** The legs are public-counterparty realized metrics over native prints, and no orderbook is a holdout input. Their only nullity path is "no FL1 (or FL2) print in an eligible game". On the pinned tapes that never happens for FL1 (6/6 games), and for FL2 it is already covered by the §5.3 n_b' < 20 → descriptive rule.

The Conductor's fear does hold for **own-order simulated maker legs**. On pregame books like Sep-25 (median queue 7,177.56 vs median same-side window volume 0; best case 0/30), the frozen rule yields null by construction. In-play the rule can be met (Sep-24 2/3, near resolution, FL0/FL2 only). That affects the downstream money-path freeze that a holdout KEEP would open (§5.6), not the holdout itself.

## 6. Recommendation

### 6.1 GO note (for Collector / Clock / Examiner)

> **GO — untouched holdout capture under addendum `370dc31d…` / ACCEPT `9a987a77…`, unchanged.** The label-free feasibility check (this note) finds that the H_a/H_b maker legs are `public_counterparty_realized` print-level metrics. They do not depend on the 9f50ba19 back-of-queue rule or on any orderbook input. On the pinned KXMLBSPREAD tapes, FL1 maker capital is > 0 in 6/6 games, so the legs cannot be null by construction. No amendment to §3–§6 is needed, and none is filed. The ordering gate (§3.1) and the capture routing in 9a987a77 (Collector queue behind weather relaunch → card03 → Q6S5 settlement fetch, ≤3 rpm, ≥20 s spacing; no GET before the 429 hold clears, per MAXIMIZE 0949ET) are unchanged. Collector cites 9a987a77 in the capture admission packet as already required.

### 6.2 Advisory for the later money-path freeze — NOT an amendment to 9a987a77 `[H]`

This applies only if a holdout KEEP opens the "FL1-only maker band filter on the Q6S5 maker leg" freeze. That freeze would inherit a fill model. If it inherits 9f50ba19 `public_trade_through_conservative` unchanged (it must stay frozen; no change is proposed), then on pregame books like Sep-25 it will produce 0 modeled fills. The proposed text for **that** freeze keeps every fill rule frozen:

- **(a) Minimum-fill feasibility gate:** "A modeled maker leg is scored only if it has ≥ **k = 10** modeled maker fills across ≥ **5** distinct games under the frozen fill rule. Otherwise its status is `NOT_SCORABLE_INSUFFICIENT_FILLS`, which is not KILL and not ITERATE-evidence, and its ROI fields are null." Rationale: these are label-free, structural numbers. Sep-25 gave 0/30 with a 95% upper bound of 11.6%. Sep-24's only fillable windows were a single near-resolution placement (1 game). Below about 10 fills across about 5 games, a 1-contract-per-leg ROI is a handful of $1 outcomes from 1–2 games, the same structural-artifact pattern that PR64 ruled out as evidence.
- **(b) Null-handling rule:** "A maker leg that is null because of zero modeled fills maps to `NOT_ESTIMABLE (reason: no_modeled_fills)` in the verdict domain. It can never be read as 0 ROI and never triggers KILL. A co-primary that is NOT_ESTIMABLE caps the run at NOT_SCORED for that leg." (This matches the PR64 ACCEPT annotation that 'no co-primary produced a reading' is not evidence.)
- **(c) Label-free capture-time diagnostic** (Collector-owned; only if the Conductor wants it, and only via its own ACCEPT so 9a987a77 is not reopened): "At each holdout book snapshot the Collector may already take, log `queue_ahead` at the best bid per side and the per-window same-side and total traded volume, with the counts-only discipline of §3.5." This makes own-order fillability measurable before any label. It is **not** a holdout input and must not delay capture.

Parameters k = 10 / 5 games come only from structural counts here. No label was consulted.

## 7. Data gaps and caveats

1. **No pregame or mid-game Sep-24 book is pinned `[V]`.** All Sep-24 books are post-game or near resolution, and 12/14 are status-gated out. The Sep-24 queue distribution is n = 3 from 1 game.
2. The Sep-25 tape is pregame only. Prints run 00:43:58Z–05:55:24Z; the games were in the evening ET. `TBPHI-TB2` has 0 prints; DET2 and WSH2 have 1 each.
3. The Sep-24 LAD2 placement at 05:07:41Z passes the frozen status gate (GET 05:07:19Z `active`). A later GET shows `close_time` 05:06:42Z. The window had 0 prints, so this changes nothing; it is reported, not re-ruled.
4. The SD2 window includes one print at 05:07:00Z, after the later-GET `close_time` 05:06:42Z (47.18 contracts at YES 0.99, taker NO). It is not counted in either leg's depletion, because the price is above the YES bid and the side does not match the NO bid. It is included in total window volume, as the frozen window has no close filter.
5. The holdout-row band counts skip the `result ∉ {yes,no}` filter, because applying it needs a label.
6. The phase proxy in the clock-bin table is the event-ticker time code. It is not first pitch and not the 5beba803 `rules_primary` parse.
7. The trade pages look complete: the last page of each ticker has an empty `cursor`. That is `[V]` from the page bytes; tape completeness beyond that is assumed, as in 9f50ba19 L86.

## 8. Integrity

- Only new files were created: this `.md`, its `.json` twin, and the scripts/outputs under `/workspace/v_holdout_feas/`. No frozen file was edited, so no `_prev` copy was needed (RULE-FROZEN-EDIT-PREV-BYTES-001).
- Scripts: `feasibility.py` (`0d1210de…`), `supplementary_bins.py` (`d1404823…`), `stats_ci.py` (`855946da…`), `explore_structure.py` (`b6f63b64…`).
- Outputs: `out/feasibility_output.json` (`b2f85de0…`), `out/supplementary_bins.json` (`a299fd78…`), `out/stats_ci.json` (`3f3e58c8…`).
- Bundle extracted fresh to `/workspace/v_holdout_feas/bundle/`.
- `results = null`, `pnl = null`, `roi = null`. No PR, push or cloud agent. No message sent.
