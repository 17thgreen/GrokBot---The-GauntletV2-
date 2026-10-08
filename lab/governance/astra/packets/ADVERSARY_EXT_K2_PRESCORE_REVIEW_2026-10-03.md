# ADVERSARY: EXT-K2 pre-score review (optimism-tax dependence stress, PR #67)

**Seat:** The Adversary "KALSHI" (Astra Drift Guard, Working Plan v0.1). **This review is advisory only.** It does not replace the Examiner, it invents no failures, and it fabricates no numbers. I placed no live orders, made no Kalshi call and sent no message to anyone.
**Filed:** 2026-10-03, about 19:30 ET (America/New_York, UTC−4).
**Target:** `17thgreen/GPT-6-Astra-Deathmatch` main@`a940355af42a15b86c5ed57ba8c7bf0e6af2b200`. That commit squashes PR #67 head `f30145c7707cd341918554bfb38017b33a36aeac` onto parent `09b56273`. Lab dir: `kalshi_ext_k2_optimism_tax_lab_20261003/`.
**Evidence tags:** [V] verified on the box this session · [I] inferred · [H] hypothesis · [A] assumption · [U] unknown.

## VERDICT: **CLEAR_WITH_ADVISORIES**

- **Part (a):** the Examiner may score it, within {DESCRIPTIVE, ITERATE, INCONCLUSIVE} only. I reproduced the reported DESCRIPTIVE result exactly: Δ\*, CI and constancy hash (§1).
- **Part (b):** the guard and code review is done (§10). **The output review stays pending until the Simulator's box run lands.** Use the checklist in §11.
- **Blocking fixes: none.** No item below could change the part (a) verdict or invalidate its labels or gates.
  - The tracked advisories are in §12.
  - Two of them (A4 RAM gate, A5 clean-tree/pin check) are **mandatory pre-run conditions for part (b)**. They do not block part (a).
- **Q6-000 is unchanged.** It was not retuned and its verdict was not touched. The 000 code and ledger shas equal the freeze pins (§13).
- **Scope reminder for the Examiner.** The primary regime label is **contemporaneous** (freeze R15): the ticker-hour bucket contains the fill's own triggering print and later prints in the same hour. Δ\*_a is therefore a static descriptive split. It is not a causal or tradable signal, it is dev-grade on the reused 31-game cohort, and it does not count toward KEEP.

## 0. Inputs checked (hashes recomputed on the box this session) [V]

| Item | sha256 / value |
|---|---|
| Freeze md `packets/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.md` (declared 16:48:49 ET) | `d69a4f627cb420b59bbc961b072d28242faeb9d21d5d29b9f90a77f6825acbce` |
| Freeze json twin | `025a01a121e5b3a64a0b683a8030f9cbd1681f132365dadb419377d09d71ff6c` |
| `CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` (16:50:38 ET) | `d76779e1a309388e6bc7f401a2c992a3be2015ae81ba910b8f5655fb10472fc0` (the vendored copy in `pins/governance/` is byte-identical) |
| `CONDUCTOR_RULING_EXT_K2_PR67_R45_HISTORY_2026-10-03.json` (17:56:39 ET) | `ac8e26c80f694b57b2862c05b67b4bf43b8d2f08f03f5c2d7c7da4cb6d70f24c` |
| `CONDUCTOR_MERGE_PR67_EXT_K2_2026-10-03.md` (19:02 ET) | read; claims checked in §1–§10 |
| `CONDUCTOR_KICK_ADVERSARY_EXT_K2_PR67_2026-10-03.json` (17:54 ET) | read |
| Commission `CONDUCTOR_COMMISSION_EXT_K2_2026-10-03.json` | `1f2c7f68396131d65ef31e492355c2937a9a0a91fb6cdf67c7d66e220f0b51f5` (vendored copy identical) |
| Variants HOLD `/workspace/v67/REPORT.md` (head d4bc79d9) | `fd20006248c319b1ca27b4220852b05f760bdfe6364982ad8c61c1285cd38e55` |
| Variants re-verify `/workspace/v67b/REPORT_f30145c7.md` | `e8d6ac84b66a81b96833ceb7e2c419c9264e6d90127628f0117cfa0c90a36cb4` (= merge packet pin) |
| Packet dir `EXT_K2_OPTIMISM_TAX/MANIFEST.sha256` | `3478b405…` (= ACCEPT `verified.manifest`). TERCILE_FIXTURE `4acbb826…`, TERCILE_BUCKETS `9acb5288…`, SOURCE_PINS `5133c826…`, structural script `cf7112e4…` |
| Box-only Becker manifest / exclusion list | `fd5e10531f48…` / `61a4c993fbea…` (both match the runner constants, `run_part_b.py:36-37`) |
| Becker t0 trades / markets parquet | `a1e1027e…` / `7238e858…` (match the freeze §2; checked before my label-free reads) |
| main@a940355a tree vs head f30145c7 tree | identical: `13585ece244ca0f857e3bb6e1aa35ea4a589ba4e` for both |
| Diff 09b56273..a940355a | 107 files, +20586/−0. Outside the lab dir the only change is `docs/EXPERIMENT_REGISTRY.md` (+2: the K2 row and a blank line; the K1 row is untouched) |

**Clone and working tree.** I fetched a fresh scratch clone at `/workspace/scratch_extk2_adv/repo`, detached at a940355a. Shared clones were not touched, and `git status --porcelain` was empty after every run. The branch chain behind the squash: d4bc79d9 (17:17:18 ET) → 132248cb (18:08:30) → 6e52dd48 (18:25:12) → f30145c7 (18:54:31) → squash a940355a (19:02:06 ET).

## 1. Part (a) reproduction: **PASS, exact** [V]

I called `run_part_a(out_dir=/workspace/scratch_extk2_adv/out_a)` on the merged code. It ran 19:05:46–19:06:04 ET, took 17.1 s and peaked at 440 MB RSS. Log: `run_a.log` `7c4614b6…`.

| Quantity | My rerun (unrounded) | Reported | Match |
|---|---|---|---|
| Δ\*_a gross (T3−T1, MO_1800, contract-weighted) | −0.0003016413076326061 | −0.000301641 | = |
| CI95 gross (B=10,000, seed 20261003, type-7) | [−0.0010309890421085896, 0.0004501346780537653]; 10,000 used, 0 dropped | [−0.001030989, 0.000450135] | = |
| Constancy sha | `523f840babd3e57d8a305ecc458f979d9288e69082210edaf8648e3132101968` | `523f840b` | = |
| Bucket table sha | `9acb52888a411be801bb701d12f3982e1e2f1c884accc162ca6f1f1d8fef6a14` | same (= pinned TERCILE_BUCKETS) | = |
| Verdict | DESCRIPTIVE, reasons [] (gate ok, failures []) | DESCRIPTIVE | = |
| Net Δ\* / CI (sensitivity, CACHE_NOT_R1P1) | −0.00041388938 / [−0.0010838975, 0.0002450875] | −0.000414 / [−0.001084, 0.000245] | = |

- **Results files.** All 5 `results_a/*.json` files are **byte-identical** to the committed ones: EMPTY_RESULTS `57a5761e…`, MARKOUTS_BY_TERCILE `8d87aa62…`, STRUCTURAL `474ae6d7…`, TERCILES `6229abb4…`, UCH_BY_TERCILE `efc30be9…`.
- **UNIT_RESULTS.md.** It differs only by the hand-appended verification paragraph, a known cosmetic item. That paragraph still says "34 tests" while the suite now has 37 (A9).
- **Test suite.** `python3 -m unittest discover -s tests -v` (19:08:29–19:08:43 ET) → **Ran 37 tests in 13.941 s, OK**. Log: `tests_run_a940355a.log` `2c4a6503…`.

## 2. Tercile cuts are label-free: **PASS** [V]

**Code path.**
- `load.py:72-80`: trade rows are projected to `(ticker, at, taker_side, size)` before anything else. Quote rows go to a separate dict.
- `terciles.py:66-124`: `flow_terciles` accepts only that projection.
  - `_as_flow` (`:51-63`) refuses any non-flow key, including `result`, `outcome`, `outcome_mid_at_fill`, `bid`, `ask`, `price` and `close_time` (`:18-22`).
  - `_reject_label_kwargs` (`:46-48`) refuses quote, fill, score and result arguments.
  - Cuts come from type-7 quantiles of unweighted eligible bucket shares: `q7` at `:25-35`, applied at `:101-102` and `:112-113`.

**Frozen numbers vs computed.** The cuts are both computed and gated:
- They are recomputed at run time and then compared within 1e-12 to the frozen constants `PINNED_C1/C2/E1/E2` (`terciles.py:11-15`).
- The bucket table must also match its pinned sha (`orchestrator.py:123-128`).
- Any mismatch adds `K1_R36` → INCONCLUSIVE (`orchestrator.py:178-179`).
- Portion assignment uses the computed cuts (`terciles.py:105, 206`), which equal the frozen ones to the last digit.

**Timestamps (ET).**
1. The fixture `TERCILE_FIXTURE.json` (`4acbb826…`) and `TERCILE_BUCKETS.json` (`9acb5288…`) were written at **16:42:57** by `structural_verify_devtape.py` (`cf7112e4…`). Its docstring (`:2-3`) and code (`:24-27`, skipping `kind=="quote"`) read B1 trade rows and `markets.json` only. No fill, quote bid/ask, score or settlement is read.
2. Freeze declared: 16:48:49.
3. ACCEPT: 16:50:38.
4. First implementation commit: 17:17:18.

So no 000 fill was joined before the cuts were frozen [V script]. The author's claim not to have looked at fills is [A], as freeze §6 states. Disclosed design-time look: `MIN_TRADES=5` was picked after seeing flow-only share quantiles at thresholds 1/5/10/20 (freeze R13, §6). That information is label-free, so [A] and acceptable.

**Positive-control permutation** (`probes/probe_t01_positive_control.py` `30675fab…` → `.json` `018675c8…`; 19:06:54–19:08:20 ET). I ran 21 permutations: 20 seeded shuffles plus a shift-by-1 derangement. Each permutation:
- attached a synthetic per-game `result`/`settlement_value` to every market;
- permuted (bid, ask) across all 364,988 quote rows;
- shuffled the fills' `outcome_mid_at_fill`;
- then fully rebuilt terciles, lots, labels and markouts through the merged code.

Results:
- **1 distinct constancy sha (`523f840b…`); cuts identical in 21/21.**
- The permutations were live: Δ gross moved in 21/21 (range [−0.0630, −0.0079]).
- **Power check:** shuffling the flow label `taker_side` across trade rows moves c1 0.92717→0.94134, c2 0.98988→0.98896 and the constancy sha to `1d68dc87…`. So the invariance check can fail.

## 3. R45 leak scan of the main tree at a940355a: **PASS, zero PR67-introduced Becker numbers or ids** [V]

Script: `probes/leak_scan_main.py` (`deab0b92…`) → `leak_scan_main_out.json` (`87c0bf47…`).

**Corpus.**
- All 3,380 tracked files at a940355a, on a clean tree.
- Inside the K2 lab dir, every `.gz` was decompressed and every `.tgz` member expanded.
- The squash commit message.
- Total: 3,445 entries and 651 M characters.

**Patterns, taken from the R45 rule and the d4bc79d9 branch-history hits:**
- **47 Becker numbers.** Every integer ≥1000 in box `BECKER_STRUCTURAL_AGG.json` (`ea354f2f…`), plus the freeze §3.2 / Clock numbers: 8,297,967; 530,529; 175,020; 705,549; 7,592,418; 262,380,071; 110,313; 57,027; 773,448. Matched in plain, comma, underscore and space forms.
- **7 strings:** `_EXPECTED_COUNTS`, "2 of 486", "190/428", `7.13e-05`, `7.13e-5`, `KXNFLGAME-25SEP28GBDAL`, `25SEP28GBDAL`.
- **729 Becker ids:** all 486 t0 market tickers and 243 event tickers, read from the markets `ticker`/`event_ticker` columns only.
- **UUIDs:** all 695,664 UUID tokens in the corpus, checked against the `trade_id` column of **all 5** Becker trade tiers with pyarrow `is_in`.

| Pattern class | Result |
|---|---|
| Becker trade_ids (t0–t4) | **0 / 695,664 tokens** |
| High-specificity Becker counts and sizes (33 patterns, e.g. 8,297,967; 705,549; 7,592,418; 530,529; 175,020; file bytes; tier row counts) | **0 hits** |
| `_EXPECTED_COUNTS`, "2 of 486", "190/428", 7.13e-05 | **0 hits** |
| Becker tickers / event ids | Hits only in 5 `stern_lab/` files (2 ids, the public tied GB–DAL game). They predate PR67 (`in_pr67_diff=false`) and are independent of Becker. **0 in the K2 lab, the registry row or the commit message** |
| Remaining numeric hits (14 patterns) | **All coincidental and non-Becker; context checked one by one:**<br>• substrings inside dev-tape trade_id UUIDs (e.g. `…388e15432ea6`);<br>• dev 000 `order_id` values (15432, 17124, 19421, 28844, 32643, 33474);<br>• dev UCH `612003.5366` in `nfl_factorial_lab` results (pre-existing);<br>• nflverse `old_game_id`-style values in `games.csv` (18306, 57027);<br>• a market `volume` in the fee cache (17124);<br>• a dev bucket `yes_contracts` (17464);<br>• the dev-tape count 681,732, which sits in AGG as `dev_tape_trade_ids` and is not Becker |
| Small structural counts (56/64/33/420/210/484/486/243/428/58) as standalone tokens in K2 code and docs outside `pins/` | 0 (the only hits are `len(digest)==64` and a dev pin) |

- **Freeze text.** The freeze md/json are **not vendored**. `pins/governance/FREEZE_SHA256.json` pins them by sha only, and the runner parses the box copy at run time (`run_part_b.py:200-247`).
- **Conclusion.** This independently confirms ruling ac8e26c8's precondition: "Main tree must carry zero Becker numbers/ids." The branch-history counts live only in d4bc79d9's reachable history, which I did not re-scan, per the ruling.

## 4. T01(b) is a genuine end-to-end rebuild: **PASS, K1 N1 fix inherited**, with an advisory [V]

- **What the test does.** `test_part_a.py:117-188` clears `support._STATE` and `load._CACHE` (`:126-127`) and reloads B1/B2 from disk with sha checks. It then rebuilds `flow_terciles` → `bucket_document` → `reconstruct` (on fills with shuffled `outcome_mid_at_fill`) → `portion_labels`, and **asserts** constancy `== 523f840b…` (`:183-186`) and c1/c2 (`:187-188`). It is no longer the cached-object self-comparison that K1 N1 flagged.
- **Limitation (A1).** The 1,000 result permutations, the shift-1 derangement and the quote shuffle are only passed to the refusing keyword arguments (`:136-156`). The rebuild itself runs on unpermuted flow, so for those labels invariance holds by construction (input-type restriction), not by observation. Only the fill-mid shuffle actually reaches the pipeline.
- **Gap closed this session.** My §2 probe feeds the permuted labels, quotes and mids through the live pipeline (markets, quote index, lots, markouts) and gets 1 constancy sha while markouts move.

Not blocking. Suggested follow-up: fold the probe's live path into T01(b).

## 5. R39 net-illustrative labelling and the Decimal fee fix: **PASS** [V], with advisory A8

**Part (b) net cells** (`metrics.py:323-351`, `_cell`):
- Every non-GROSS cell carries `net_label=NET_ILLUSTRATIVE_2026_SCHEDULE_NOT_HISTORICAL` (the ACCEPT R39 wording), `PER_TRADE_PROXY`, `FEE_SCHEDULE_2026_CACHE_APPLIED_TO_2025_TRADES_U`, the R38 overstatement disclosure (`fees.py:136-140`) and `fee_label=CACHE_NOT_R1P1`.
- `gross_is_headline` is true only for GROSS cells.
- Net values are nulled unless the ACCEPT's R39 ruling starts with "ALLOW" (`run_part_b.py:352-356`; `metrics.py:326-328`).

**Part (a) net:**
- It is the K1 R24 order fee, labelled `CACHE_NOT_R1P1`, with `net_is_headline:false`, `gross_is_headline:true` and `examiner_pin_account_class:null` (`orchestrator.py:253-255, 311-313`).
- UNIT_RESULTS calls it "not the headline".
- A grep of the README, SPEC, UNIT_RESULTS and the registry row found no fee-honest, "after-fee edge", PnL or ROI wording. `results`/`pnl`/`roi` are null.

**Decimal fix** (`fees.py:143-149`, `D()` converts floats via `str`). Script: `probes/probe_fee_hand.py` `4fdc90bb…` → `6267e489…`.
- Across 1,846 maker orders: code **$1,286.22** = hand Decimal(str) $1,286.22 = K1 STRUCTURAL. The old Decimal(float) path gives $1,286.59, with 37 orders differing by 1¢. T04 asserts equality with K1 (`test_part_a.py:265-280`).

**Hand rows (part a):**

| Order | Calculation | Hand | Code |
|---|---|---|---|
| Single fill, 247.48 @ 0.61 | 0.0175×247.48×0.61×0.39 = 1.03032111 → ceil 6dp 1.030322 → ceil cent | **$1.04** | $1.04 |
| 13 fills @ 0.60 (the first order where the two paths differ) | Decimal(str) path | **$1.05** | $1.05 |
| same order | old Decimal(float) path | $1.06 | — |

**Hand rows (part b per-trade proxy), all 6 matching freeze T09:**
- 0.0175×10×0.97×0.03 = 0.0050925 → $0.01
- 0.0175×250×0.37×0.63 = 1.0198125 → $1.02
- 0.07×1×0.5×0.5 = 0.0175 → $0.02
- 0.07×250×0.37×0.63 = 4.07925 → $4.08
- 0.07×1000×0.99×0.01 = 0.693 → $0.70
- Sweep check: two rows of 2 @ 37¢ cost $0.08 per-row vs $0.07 grouped.

**A8 (completeness, not labelling).** R39 also lists taker-side nets built from `taker_fee_row`. The code accumulates `taker_fee_yes/no` but emits taker nets only as the `SENSITIVITY_TAKER_SWEEP` group variant (`metrics.py:309-320`). Per-row taker net and the taker gross mirrors are not emitted. This is descriptive only and changes no label.

## 6. B2 traded-only exclusion: **PASS. Consistent with the freeze, and zero effect on the t0 eligible set** [V]

- **Code.** Markets are filtered to `ticker in scan["n_rows"]` (`exclusion.py:75`; again at `run_part_b.py:508`). Introduced in f30145c7 (18:54 ET), after the v67b synthetic finding and **before any real Becker run** (none has happened).
- **Effect on real data** (label-free probe `probes/probe_b2_untraded.py` `23bdd320…` → `f145eabe…`; reads only `ticker`, `event_ticker`, `status` and `volume` from markets and `ticker` from trades, after sha checks; no result, price, side or time is read):
  - 486 markets, 484 traded, **2 untraded**: both `active`, both with volume < 100, both in events that have a traded sibling.
  - **Both of those events are already in the pinned excluded set.** A full-market closure would therefore add **0** eligible tickers.
- **Selection bias / traded-ness leak.** Part (b) metrics are per-print, so an untraded contract contributes no row to any metric under either rule. Part (b) has no "refused/neutral" category it could belong to. Selection on traded-ness is the Becker volume≥100 selection already disclosed (R43, Clock (c)). B2 adds nothing on t0.
- **Freeze consistency.** Freeze §3.2 counts are traded-only: 64 excluded + 420 eligible = 484 traded tickers, and "8 closed (175,020 rows)" is a row-bearing set. The pinned generator `k2_becker_structural.py` (`6f5af907…`) is traded-only (v67b: lines 55–64). R32's "no markets row (0)" clause covers orphan trades, not untraded markets.
- **Latent [I].** On another dataset, an untraded unsettled market in an otherwise eligible event would not trigger closure of its traded siblings. That cannot happen here, because the exclusion list is sha-pinned.

## 7. counts_match now uses the event-level list only: **PASS. Not a weakening in effect** [V]

- **The change.** f30145c7 (18:54 ET) removed the `(n_excluded_tickers, n_excluded_tickers_direct)` pair from `counts_match` (`run_part_b.py:250-269`). The trigger was the v67b synthetic finding (18:30–18:50 ET) that comparing the freeze count against *both* lists would refuse valid data whenever sibling closure lengthens the event list. No real run had happened.
- **No silent ticker-level mismatch.** The ticker-level list is still checked **member-by-member** against the sha-pinned file: `excluded_tickers_ticker_level` is in `LIST_KEYS` (`exclusion.py:7-15`) and `compare_exclusion` runs before `counts_match` (`run_part_b.py:512-516`). My probe `probes/probe_r32_equivalence.py` (`4e01c06d…` → `34b9e833…`) dropped one ticker-level member and got `InconclusiveNoOutput("exclusion membership")`.
- **Market-level checks** remain: `n_traded_tickers` and the orphan count are still compared.
- **On the real data,** the pinned ticker-level list equals the event-level list (both 64), so the removed pair could never have fired.
- **Pre-declared?** Not explicitly. But the freeze defines the "64 tickers" count as the "ticker-level union = event-level closure" (§3.2; T07). The change aligns the code with that definition and made no bar easier to clear on these data.

## 8. R32 list membership vs byte equality: **PASS. Equivalent on the pinned file, so not bar-softening drift.** Documentation advisory A3 [V]

- **History.**
  - d4bc79d9 (17:17 ET, first draft): byte-compare, then a weak fallback on a non-existent `excluded_tickers` key, so it always failed (v67 B2).
  - 6e52dd48 (18:25 ET): replaced by per-list sorted membership over all 7 lists, plus both source shas, experiment_id and a non-empty rule (`run_part_b.py:160-176`).
  - Unchanged since. The change answered a schema bug in synthetic tests, not a real-data failure.
- **Equivalence probe (pinned `61a4c993…`):**
  - The pinned file **is canonical JSON** (`canon_bytes(json.loads(raw)) == raw`).
  - All 11 of its keys are compared.
  - All 7 lists are sorted and unique.
  - The recomputed lists are emitted sorted (`exclusion.py:119-131`), and the recomputed `rule` is copied from the pinned file (`run_part_b.py:510`).
  - The exclusion file itself is sha-gated to `61a4c993` before anything is read (`run_part_b.py:431-446`).
  - Conclusion: **any recomputed document that passes membership serializes to the pinned bytes.**
- **What could pass now but fail byte equality:** only a different `rule` text, which is unreachable because the runner copies it from the pinned file (probe: rule drift is not caught by `compare_exclusion`, by design). No non-deterministic ordering is involved, because both sides are sorted.
- **A3 (documentation).** Freeze R32/T07 call for canonical-JSON/byte equality. Neither the freeze nor ACCEPT d76779e1 records the deviation. It appears only in the Conductor merge note, line 9 ("(c) R32 list-membership accepted", 19:02 ET), and in v67b N4. Suggested follow-up: add `canon_bytes(recomputed) == pinned_bytes` as an extra assert (no behaviour change on these data), or file a formal deviation note.

## 9. N6 empty or undefined bucket → INCONCLUSIVE: **PASS, K1 N6 fix inherited** [V]

- **Implementation.**
  - `orchestrator.py:195-196` adds `undefined_contrast` when `delta_gross` or `ci95_gross` is None.
  - An empty T1 or T3 also trips `games_<5` (`:191-192`) and, through 100% dropped resamples, `bootstrap_dropped` (`:193-194`).
  - Test: `test_part_a.py:292-312`. v67b probe: 4 None cases → INCONCLUSIVE.
- **Part (a) bucket counts** (rerun = committed):

| Unit | Counts |
|---|---|
| Ticker-hour buckets | T1 3,093 / T2 3,092 / T3 3,092 / UNCL 812 (10,089 total, 9,277 eligible) |
| Events | 11 / 10 / 10 / 0 |
| Portions, primary | T1 1,677 / T2 3,733 / T3 751 / UNCL 0 |
| Portions, secondary | 2,299 / 2,276 / 1,586 / 0 |
| Portions, causal trailing-60 sensitivity | 1,853 / 3,654 / 654 / 0 |

- **Primary T1 vs T3:**

| | Distinct games | Opening contracts | Censored at H\* | Censored share |
|---|---|---|---|---|
| T1 | 27 | 34,273.54 | 167.02 | 0.49% |
| T3 | 30 | 25,175.31 | 243.03 | 0.97% |

- UNCLASSIFIED share is 0%. Bootstrap dropped 0/10,000.
- No R23 trigger is near its threshold.

## 10. Part (b) guards (code review; no outputs yet) [V code / I where noted]

| Guard | Finding |
|---|---|
| **RAM gate** | **Not in code.** `run_part_b.py` has no memory check. v67b estimates ~10–11 min runtime and a peak of up to ~5.7 GB ([I], upper bound, from about 683 B/row). Box at 19:08 ET: **4,405 MiB available** of 16,013 [V `free -m`]. Fail-closed for K2, because publishing happens only after a full pass (`run_part_b.py:404-418, 549`). **But the box is shared:** an OOM could kill other agents' processes. → mandatory pre-run condition (A4) |
| **Input pins** | Before any read, the runner checks the manifest `fd5e1053`, the exclusion list `61a4c993` and the box freeze md `d69a4f62` (`run_part_b.py:430-446`). On a mismatch it writes a receipt and refuses. Every runner item is sha-checked (`:116-130`). The tier refusal and data-table mix refusal apply only to parquet (`:97-104, 133-143`). t0 shas re-verified this session [V]. The download dir is hashed before the run (`:465`) and re-hashed before publishing (`:404-413`). The hash covers `data/` only, not the whole `becker_2026-10-03/` tree [V `_download_dir`, `:287-292`] |
| **Receipt** | Written before any table read (`:466-469`). Records the commit (`git_head` reads HEAD only), runner sha, manifest, exclusion and freeze shas, and the dir hash. **Gaps (A5):** a dirty working tree is not detected, and `pins/governance/FREEZE_SHA256.json` (`90a4c639…`) and the vendored ACCEPT that gates `NET_FEE_PROXY` (`d76779e1…`) are read **without a sha check** (`:70-73, 352-356`) |
| **No Becker numbers in the main tree** | The writer refuses a run dir inside the repo (`writer.py:25-31, 61`). The runner refuses a run dir that overlaps the download dir (`:462-463`). The output path is CLI-chosen, so the freeze path `…/ext_k2_becker_boxonly_2026-10-03/run_<utc>/` is not enforced. The committed `results_b/` holds only a null sha pointer and a receipt template [V] |
| **T11 row-level scan** | Forbidden keys are refused. Output strings are exact-matched against t0 trade_ids and **traded** tickers (`writer.py:47-57`). Event tickers and the 2 untraded market tickers are not in the banned set, and substring matches are not detected (A6). Cells carry no data-derived free text, except the selection-bias and coverage text parsed from the freeze md, which contains Becker structural numbers (fine while box-only) |
| **Determinism / seeds** | Each cell uses `random.Random(seed)`: weeks 20261003+w, pooled 20261003, bands 20261003+100+b. Events are sorted before resampling (`metrics.py:280-299`). Sums use exact integer/Decimal arithmetic, so the result is independent of order. v67b's synthetic rerun was byte-identical [V per v67b E1b]. The PRE stratum reuses seed 20261003, which is harmless |
| **Verdict domain** | On publish the label is always `"DESCRIPTIVE"` (`run_part_b.py:543`). Every failure raises `InconclusiveNoOutput` / `ReceiptMismatchRefused` / `ManifestTamper` and writes **no** aggregate, so **INCONCLUSIVE leaves no labelled artifact**, only the receipt and the exception (A7). `feeds_gate`/`promote`/`counts_toward_keep` are false and `results`/`pnl`/`roi` are null (`metrics.py:465-471`). It cannot be ITERATE |
| **Selective re-run / tuning** | Code, parameters and seeds are frozen at a940355a (R47). The only CLI freedom is `--root` and `--run-dir`. Items stay sha-checked under `--root`, so only byte-identical data can pass. **Nothing in code stops repeated runs or the choice among run dirs.** Because the runner is deterministic, every rerun must reproduce the same digest. Any second, different digest is a flag |
| **Label dependence** | MNO, MYES and the taker mirrors read `result` (`metrics.py:173-174`) and carry `BECKER_LABEL_DEPENDENT_DESCRIPTIVE_ONLY` (`:349-350`). `refuse_becker_value` blocks part (b) values from the part (a) verdict (`orchestrator.py:204-208`; T15) |
| **close_time** | Used only inside the exclusion recompute (`exclusion.py:89`; T13) |

## 11. Part (b) output checklist (to verify when the Simulator's run lands)

**Pre-run (before any Becker read):**
1. `free -m` "available" ≥ ~7 GiB (≥ 5.7 GB peak plus margin), recorded with a timestamp. Alternatively, run under a hard memory cap (e.g. `prlimit --as` or a cgroup MemoryMax) so an OOM cannot hit other agents' processes.
2. The clone is at **a940355af42a15b86c5ed57ba8c7bf0e6af2b200**, `git status --porcelain` is empty, and these shas match:

   | File | Expected sha256 |
   |---|---|
   | `run_part_b.py` | `5c40e72de57c0a18bb8ea77978d7f64e85c6e95ba7f040ec76292ad52e1814c2` |
   | `metrics.py` | `45e3ab8e94c2025ad212830a9c4c5fed5953f382ab03ffe8879654bdebcdc95d` |
   | `exclusion.py` | `22555c51b991ad13d71d651ee372968e02bbe4bd53c16f2d42c1c61660cd8393` |
   | `writer.py` | `ebe181ca1deac6d160a2070cfcde5413ecee8312eba06493f002a9231bbbbbf6` |
   | `guards.py` | `6a0787d9dfd475379c65232e0f5ec9364a9b850d680d9cc1f4f910a7b7462dfe` |
   | `becker_pipeline/pins.py` | `e1498eb9d5cb4cd4aec6b4cafefdba80a7fcb27fb724cf833a69847258e5d105` |
   | `shared/fees.py` | `516f9a6d5bc7af4187717a17a68ba748b83142bc30917d37ae85fc12d5ebc088` |
   | `pins/governance/FREEZE_SHA256.json` | `90a4c63990d6c7514ce2c5ee89ef5a4a9d0a2561af379a68df1fbc09e4a8869e` |
   | `pins/governance/CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` | `d76779e1…` |
   | `pins/bands_registry_10c.json` | `0860cbe2…` |

**Receipt (`PRE_RUN_RECEIPT.json` in the run dir):**

3. `commit_sha` = a940355a.
4. `runner_file_sha256` = `5c40e72d…`.
5. Manifest / exclusion / freeze-md shas = `fd5e1053…` / `61a4c993…` / `d69a4f62…`, with all three `*_match` true.
6. `becker_dir_all_files_sha256` is non-null.
7. The receipt mtime precedes the aggregate's mtime.

**Run accounting:**

8. List **every** run dir created under the box-only area, including failed runs and their exception text.
9. Exactly one published `PART_B_AGGREGATES.json`. If any rerun happened, every digest must be identical.
10. `BOX_ONLY_OUTPUT_SHA256.json` = sha256 of the aggregate = the stdout digest.

**Location and leak:**

11. The run dir sits under `lab/astra-capture/external/ext_k2_becker_boxonly_2026-10-03/run_<utc>/`, as the freeze says, and outside the repo and the download dir.
12. An independent post-run scan of every file in the run dir finds 0 hits against all t0/t1–t4 trade_ids, all 486 market tickers **and** the 243 event tickers, substring matching included (closes A6).
13. Under ACCEPT R45, only the output **sha** may enter git, plus code, synthetic tests and the receipt. Any `packets/EXT_K2_OPTIMISM_TAX/results_b/` copy on the box must stay out of every GitHub push or steward sync.

**Content:**

14. `label` ∈ {DESCRIPTIVE}. If it failed, it is recorded as INCONCLUSIVE with the exception, and there are no aggregates.
15. `feeds_gate`/`promote`/`counts_toward_keep` are false, and `results`/`pnl`/`roi` are null.
16. Attribution line present (R45). Tags `BECKER_EXTERNAL_PRIOR_A`, `TRADE_ONLY_NO_QUOTES`, `SELECTION_VOLUME_GE_100`, `ARCHIVE_ENDS_2025-11-25` and `LICENCE_U_NO_REDISTRIBUTION` present on the document and on every cell.
17. Every non-S cell carries `BECKER_LABEL_DEPENDENT_DESCRIPTIVE_ONLY`.
18. Every non-GROSS cell carries `NET_ILLUSTRATIVE_2026_SCHEDULE_NOT_HISTORICAL`, `PER_TRADE_PROXY`, `FEE_SCHEDULE_2026_CACHE_APPLIED_TO_2025_TRADES_U` and the proxy disclosure. `gross_is_headline` is true only on GROSS cells. The direct-member value never appears as the headline.
19. Bands are b00–b09 exactly (registry `0860cbe2`, no rebin). Weeks are PRE plus W01–W12. Dispersion uses complete weeks only: freeze expects W01–W11, i.e. `n_complete_weeks` 11 for S. W12 is suppressed or has a null CI.
20. `SUPPRESSED_SMALL_CELL` appears on every cell with < 20 rows or < 2 events, with value and CI null.
21. `selection_bias` and `coverage` text equal the freeze §3.2 / R43 text.
22. No PnL, ROI, Sharpe, KEEP or "edge" wording anywhere.
23. Part (b) numbers do not appear in the part (a) verdict or any gate, and part (a) `results_a` is unchanged (`git diff` empty).
24. If the run ended INCONCLUSIVE: no aggregate exists, and the reason is one of the R44 triggers (sha mismatch, counts mismatch, dir hash change, integrity failure).

## 12. Tracked advisories (non-blocking)

| # | Advisory | Severity | Evidence |
|---|---|---|---|
| A1 | T01(b) passes permuted labels and quotes only to the refusing kwargs, so the rebuild runs on unpermuted flow. Fold the live-permutation path from `probe_t01_positive_control.py` into the test | latent / test power | `test_part_a.py:136-163` [V] |
| A2 | When the R36 gate fails, markouts are still computed and written (the verdict becomes INCONCLUSIVE). Freeze R12 says "no markout" | latent (gate passes) | `orchestrator.py:219-242, 387-416` [V] |
| A3 | The R32 deviation (membership instead of bytes) is recorded only in the merge note. Add the byte assert or file a deviation note | documentation | §8 [V] |
| A4 | **Part (b) RAM gate not in code. Mandatory pre-run condition** (checklist item 1) | operational, part (b) only | §10 [V/I] |
| A5 | **Receipt does not prove a clean tree. FREEZE_SHA256 and the vendored ACCEPT (net flag) are not sha-checked at run time. Mandatory pre-run check** (checklist item 2) | integrity, part (b) only | `run_part_b.py:46-58, 70-73, 352-356` [V] |
| A6 | The T11 banned set omits event tickers and untraded market tickers, and matching is exact-match only | latent | `writer.py:47-57`; `run_part_b.py:548` [V] |
| A7 | A part (b) INCONCLUSIVE leaves no labelled artifact (receipt and exception only). The Simulator must record it | process | `run_part_b.py:441-549` [V] |
| A8 | R39 per-row taker nets and taker gross mirrors are not emitted (only the sweep-group variant) | completeness | `metrics.py:309-320` [V] |
| A9 | "34 tests" in UNIT_RESULTS.md and the registry row; actual 37 | cosmetic, known | §1 [V] |
| A10 | The primary label is contemporaneous (R15). The Examiner should read Δ\*_a as descriptive only. The causal trailing-60 split exists (T1 1,853 / T3 654 portions) | scope | freeze R15/R17 [V] |
| A11 | The run-dir path is not pinned in code, and the freeze's `results_b/` copy sits in the governance tree. Keep it out of any sync | process | §10 [V/I] |
| A12 | Traded-only exclusion would not close events around untraded unsettled markets on other datasets. No effect on t0 | latent | §6 [V/I] |

**Not found:**
- **Lookahead:** no real lookahead into outcomes. The labels are flow-only, and the contemporaneous label is disclosed (A10).
- **Fees:** no fee blindness. Gross is the headline, net is labelled, and the Decimal fix is verified.
- **Q6-000:** no retune or verdict change of 000.
- **Registry:** no omission. The K2 row is present, the K1 row is untouched, and the Examiner HOLD_PRE_PR is `scored:false`.
- **Becker mixing:** no Becker mixing into dev (T05, R05; import-graph test passes).

## 13. Q6-000 untouched [V]

| File | main@a940355a | box | Freeze pin |
|---|---|---|---|
| `replay_v2.py` | `5aba1bf3…` | `5aba1bf3…` | `5aba1bf3…` |
| `queue_policies.py` | `641d0df3…` | `641d0df3…` | `641d0df3…` |
| `run_experiment.py` | `c1a0fd2d…` | `c1a0fd2d…` | `c1a0fd2d…` |
| `q3300_d0.25_000.json` | `78b94ae5…` | `78b94ae5…` | `78b94ae5…` |
| fills / orders / decisions gz | (git-ignored on main; vendored copies checked by T16) | `9d56f5d3…` / `c390801b…` / `e6db5237…` | same |
| `RESERVED_HOLDOUT.json` | n/a | `74507e1a…` | `74507e1a…` |

`git diff 09b56273 a940355a -- nfl_factorial_lab_20260921` is empty. T16 passes. **No retune; 000's verdict is unchanged.**

## 14. Artifacts (scratch, box-only; no shared or frozen file was edited)

`/workspace/scratch_extk2_adv/`:
- `repo/` (clean clone at a940355a)
- `out_a/` (rerun results_a)
- `run_a.log` `7c4614b6…`
- `tests_run_a940355a.log` `2c4a6503…`
- `probes/probe_t01_positive_control.{py,json}` `30675fab…` / `018675c8…`
- `probes/leak_scan_main.py` `deab0b92…` → `leak_scan_main_out.json` `87c0bf47…`
- `probes/probe_b2_untraded.{py,json}` `23bdd320…` / `f145eabe…`
- `probes/probe_r32_equivalence.{py,json}` `4e01c06d…` / `34b9e833…`
- `probes/probe_fee_hand.{py,json}` `4fdc90bb…` / `6267e489…`

The probe outputs contain counts, booleans and locations only. No Becker identifier, price, side or result value was printed or written. Becker reads were limited to the `trade_id` column (all tiers), `ticker` (t0 trades), and `ticker`/`event_ticker`/`status`/`volume` (t0 markets). `result` was never read.
