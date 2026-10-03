# EXAMINER SCORECARD — EXT-K1 Q6-000 legging-risk audit (PR #66)

- Seat: Examiner (Kalshi), Astra. Filed 2026-10-03 17:19:36 ET (2026-10-03T21:19:36Z).
- Template v1.2 `56bcf626…` (md `ad1dd283…`).
- Source: main@`09b56273eb3b11ec3968e273a28767569e368561` (parent `761eaaed`; tree `622e4c93` = PR head `7415447c` tree). Verified as a local git object only; containment on origin main is conductor-attested.
- READY `490112654a87699ea33bc60a60c05954428ecc41d0a31ac54556e89e3971b00f`
- SCORE JSON `0e5b10605798b45d69fde326e06fa1b9be52642dd4c64b28f79657b4d68edd5b`
- Authority: the Conductor SCORE request (a message). There is no `CONDUCTOR_SCORE_KICK_*EXT_K1*` file on disk. The on-disk routing is N6 ruling `0b68c4bf…`: "SCORE EXT-K1 main@09b56273 within DESCRIPTIVE/ITERATE/INCONCLUSIVE".

## Verdict: **DESCRIPTIVE**

Labels: dev-grade · EX_POST_ANCHOR_U · no tradable-signal claim · counts_toward_keep=false · promote=false · fee label CACHE_NOT_R1P1. Q6-000 is unchanged: no KEEP, no KILL, no retune.

The verdict comes from the pre-declared rule in freeze R32 (L148, freeze md `5c40fb9d…`; ACCEPT `02129007…`), quoted verbatim:

> INCONCLUSIVE if any of: join ≠ 31/31; any R36 repro fails; UNCLASSIFIED > 5% of opening contracts; censored at H\* > 20% of opening contracts in the ON or the AGAINST bucket; `open_at_window_end_contracts` ≠ 0. Otherwise ITERATE if the 95% CI of Δ\* excludes 0 (either sign); that means a consensus-related legging effect is visible ex post and warrants a separate counterfactual-gate freeze. Otherwise DESCRIPTIVE.

How the rule applies:
- **No INCONCLUSIVE trigger fires:**
  - Join is 31/31.
  - All R36 repros pass. The Examiner re-derived them independently: 12,853 / 681,732 / 364,988 / 62; maker NO share 0.989706; taker YES share 0.916882; UCH 603,262.7291.
  - UNCLASSIFIED is 0%.
  - Censored at H*=1800 s: ON 0.2248%, AGAINST 0.4304%.
  - open_at_window_end is 0.
- **The ITERATE test fails:** the 95% CI of gross Δ* contains 0.
- **Result:** DESCRIPTIVE. Under R38, only gross Δ* (R31) can move the verdict.

## (a) Primary contrast: gross and net, reported together

Δ* = contract-weighted MO_1800(AGAINST) − MO_1800(ON), with δ = 0.005, proportional de-vig, in $/contract. Uncertainty is a game-cluster bootstrap over the 31 games.

| | Δ* | 95% CI |
|---|---|---|
| **Gross** | **−0.000205** | **[−0.000577, 0.000188]** |
| **Net (headline $0.01 fee)** | **−0.000373** | **[−0.000775, +0.000087]** |

**Examiner recompute:** an independent pipeline built from the pinned bundle bytes, with no runner imports. It uses its own FIFO lots, nflverse join and de-vig, quote-mid markouts and Decimal fee book. The bootstrap mirrors the pinned method exactly: `random.Random(20261003)`, B = 10,000, `choices` over the 31 sorted events, linear-interpolation percentile.

| | Δ* | 95% CI |
|---|---|---|
| Gross | -0.000205191 | [-0.000577471, 0.000188188] |
| Net | -0.000373009 | [-0.000775055, 0.000086859] |

- Resamples: 10000 kept, 0 dropped.
- **Mismatch vs claimed: none at 6 dp.** The values also match the Adversary re-run.

**Buckets:**

| Bucket | Portions | Contracts |
|---|---|---|
| ON | 2,664 | 68,640.58 |
| AGAINST | 2,578 | 72,781.55 |
| NEUTRAL | 919 | 22,096.09 |
| UNCLASSIFIED | 0 | 0 |

Total: 6,161 portions, 163,518.22 opening contracts.

**MO_1800, gross vs net:**

| Bucket | Gross | Net |
|---|---|---|
| ON | 0.004955 | 0.001084 |
| AGAINST | 0.004750 | 0.000711 |

Fees absorb most of the markout.

## (b) Gate share under both de-vig methods (descriptive, outside the verdict)

| Cell | Refused portions | Refused contracts | Refused unhedged contract-hours |
|---|---|---|---|
| Primary: x=0.02, E=0, **proportional** | 700 | **12.25%** | **14.42%** |
| Shin twin: x=0.02, E=0, **Shin** (GATE cell 10) | 462 | **7.97%** | **10.72%** |

- Recomputed independently: proportional 0.122505 / 0.144157; Shin 0.079706 / 0.107201. These match the claimed 12.25% / 14.42% and 7.97% / 10.72%.
- The share depends on the de-vig method by about 4.3 percentage points of contracts and 3.7 points of UCH, so both must always be quoted together.
- The 16-cell grid never selects a cell (R28/R30).

## (c) Fees

- **Headline:** non-direct-member rule, rounded **up to $0.01 per maker order** (R24; label CACHE_NOT_R1P1, NON_DIRECT_CENT_HEADLINE). Maker-order fee total **$1286.22** over 1846 orders. Independently recomputed; matches the runner.
- **Sensitivity only, never the headline:** direct-member $0.0001 (ledger fee/size, R25).
  - Total $1277.0453.
  - Net Δ* under it: -0.000373, 95% CI [-0.000775, 0.000081]. Computed by the Examiner; not a lab output.
- **Account member class pin: null.** There is no on-disk evidence of whether the account is a direct or non-direct member.
  - FEE_ACCOUNT_MANIFEST ADDENDUM_02 (`44a69092…`) has `member_type: null`, status OPEN, and says "Logan/Conductor only — Archivist refuses to invent".
  - The base manifest (`aa765876…`) says: "No on-disk record of whether the lab account is a direct or non-direct member."
  - The headline therefore stays at $0.01, per ruling `870895a5…`.
- **R2-P5:** no fee-honest claim is made. These fees do not use formula_id `astra.r1p1.feebook.claude_order_level_ceil.v1`.
- **Becker gross-of-fee rule:** not applicable to K1, because R39 forbids Becker data here. Any Becker comparison (K2) must first subtract maker 0.0175·p(1−p) and taker 0.07·p(1−p).
- K1, K2 and K3 box results on the 31-game cohort are dev-grade, with no KEEP.

## (d) Outcome exposure

**Outcomes were viewed before the freeze.** While checking the join (about 16:07 to 16:14:59 ET), the author printed the nflverse `away_score`, `home_score` and `result` columns.
- The freeze (16:14:59 ET) discloses this in §6, and ACCEPT logs "outcome-exposure disclosure (1)".
- T01 label permutation keeps the gate, splits and markouts constant (`a73a90e0…`, reproduced).
- Even so, this is **not** a clean pre-outcome preregistration.
- The nflverse moneyline timestamp is undocumented [U]. p_cons may post-date fills, and T02 cannot test anchor-time lookahead (A2).

## (e) The gate is not shown to work

Refused-vs-kept markouts (primary cell, 1800 s, gross: refused 0.003685 vs kept 0.005068) are **NOT evidence that the gate works**, and are not treated as such here. They are:
- static attribution on an ex-post anchor;
- outside the verdict (R38);
- dependent on the de-vig method;
- gross of fee;
- not counterfactual.

Any future gate claim must be net and counterfactual, under its own freeze.

## (f) Adversary tracked fixes (review `676ba2fa…`, CLEAR)

- **N1: REQUIRED before any reuse.**
  > A3 (tracked fix, before the code is reused for any new cohort or freeze): move the end-to-end rebuild (permute the csv bytes and rebuild join, consensus, gate and markouts) into T01, add the moneyline positive control, and delete the no-op L43. Also correct `UNIT_RESULTS.md` L76: "One thousand … shuffles … left these artifacts byte-identical" overstates T01(b). The end-to-end coverage is 26 runs (Variants) plus 100 (Adversary, including those 26 reproduced).
- **N6: REQUIRED before any reuse.**
  > A5: return INCONCLUSIVE when Δ* or the CI is None, or when dropped resamples exceed a pre-stated share. Make it binding before this code is reused (any counterfactual-gate freeze, season-scale or new cohort). Because it changes R32 semantics, it needs a Conductor-accepted note or a new freeze, not a silent edit.

  Conductor ruling `0b68c4bf…`:
  > Prospective only: undefined Delta* or undefined CI => verdict INCONCLUSIVE. No effect on PR66 result (ON 2664 / AGAINST 2578 portions; 0/10k resamples dropped). Implement in follow-up PR after K2 PR lands, with N1/N5/N3 fixes.

  N6 does not bind this run: there are no empty buckets and 0 of 10,000 resamples were dropped.
- **N5: COSMETIC.** INVARIANCE.json lacks the three R33 dev flags. Note that the Adversary's own table lists A4 as "Before code reuse".
  > The flags are labels, not checks. Fix: build the record with `_common_header()`, or have T14 also assert the R33 flags.

## Multiplicity and cohort context

- family_size = 1. Only gross Δ* can move the verdict (R38).
- Descriptive only: the 16-cell grid, δ, Shin labels, S_FAV, other horizons, CLOSE, SETTLE, net, and the direct-member fee.
- Sensitivities, recomputed by the Examiner and matching the Adversary: δ=0 gives −0.000153; δ=0.01 gives −0.000308; Shin labels give −0.000216. None changes the verdict.
- Cohort: the reused 31-game 2026 W1–W2 dev cohort, so the effective n is 31 game clusters. 22 games contribute both ON and AGAINST; 9 lack one of the two.
- The same cohort underlies the K1, K2 and K3 box results: all dev-grade, not out-of-sample, with no KEEP. No multiplicity correction is applied because nothing is claimed.

## v1.2 common fields (all null, with reasons)
- **net_pnl_without_rewards**: null. Measurement-only audit; results/pnl/roi null by freeze; ROI/PnL framing of markouts refused; fills are hypothetical replay, not Astra
- **net_pnl_with_rewards**: null. No Astra P&L; no rewards thesis
- **rewards_actually_earned**: null. No Astra activity
- **calibration**: "N/A". Not probability-emitting; p_cons is an ex-post anchor, not a forecast scored here
- **fill_rate**: null. Fills are Q6-000 hypothetical replay matches; no demo/shadow/live Astra orders
- **adverse_selection_after_fills**: null. Template field is defined on real Astra fills (positive = against us). EXT-K1 reports hypothetical-fill MO_1800 with the opposite sign (MO = mid_out − p_entry, positive = favourable); descriptive only
- **feasible_vs_requested_size**: null. No Astra orders; orders ledger hashed, not parsed (freeze)
- **unresolved_inventory**: null. No Astra positions (replay open_at_window_end_contracts = 0, descriptive)
- **capital_hours**: null. No Astra positions; replay UCH 603,262.7291 contract-hours is hypothetical and descriptive
- **drawdown**: null. No Astra P&L series
- **event_concentration**: null. Template metric uses Astra net P&L; none exists
- **study_label**: historical replay.
- **executable_dollars_per_day**: null. No signal claim; Archivist fee/account manifest still DRAFT_NOT_ADOPTED.

## Pins

- Freeze md `5c40fb9d…` / json `be3e8833…`
- ACCEPT `02129007…`
- MERGE `9de0933b…`
- Adversary `676ba2fa…`
- Fee ruling `870895a5…`
- N6 ruling `0b68c4bf…`
- Packet MANIFEST `5e8f7906…` (9/9 files OK)
- Bundle `0f8f5297…` (inner manifest `a041561e…`, 37/37 files OK)
- HOLD_PRE_PR (in repo, untouched) `51e36811…`
- Simulator READY: none on disk.
- Tests: 22/22 pass in a fresh worktree at 09b56273.
- Re-running `measure(write=True)` in a scratch copy reproduces 6 results JSONs byte-for-byte: STRUCTURAL, UCH, EMPTY_RESULTS, CONSENSUS_FIXTURE, MARKOUTS, GATE.
- INVARIANCE.json is written by T14, not by measure. It is also byte-identical.
- The READY lists all 7 under measure_rerun_byte_compare; this card refines that.

## Anomalies
- No CONDUCTOR_SCORE_KICK_*EXT_K1* file on disk; authority is the relayed message plus examiner_routed in N6 ruling 0b68c4bf.
- No Simulator READY for EXT-K1 on disk (run record = /workspace/v66/REPORT.md f3552b58...).
- Merge object 09b56273 present only in /workspace/tmp/pr57-verify/repo/.git; containment on origin main is conductor-attested, not fetched.
- T13 errors in a no-git scratch copy (environment); 22/22 pass in a fresh worktree at 09b56273.
- Ruling 870895a5 issued_et 16:10 vs file mtime 16:06:39 ET (clerical; already noted in ACCEPT).
- ACCEPT.verified.manifest 5e8f7906 is the packet-dir MANIFEST, not the inner bundle MANIFEST a041561e (runner flag; both verified).
- In-repo EXAMINER_HOLD_EXT_K1_PRE_PR file is implementer-authored (signed_by_examiner=false) under an EXAMINER_ prefix; left untouched.
- Freeze R10 alias gap (LAR→LA) resolved in freeze; overround deviation A6; registry row lacks outcome-exposure note A9; INVARIANCE.json missing R33 flags (N5).

No orders were placed, no messages sent, and nothing was fetched. Only new EXAMINER_* files and scratch files were written.
