# EXAMINER SCORECARD: EXT-K2 optimism-tax dependence stress, PART (a) ONLY (PR #67)

- Seat: Examiner (Kalshi), Astra. Filed 2026-10-03 19:32:27 ET (2026-10-03T23:32:27Z).
- Template v1.2 `56bcf626…` (md `ad1dd283…`).
- Source: main@`a940355af42a15b86c5ed57ba8c7bf0e6af2b200`.
  - Parent `09b56273`. Tree `13585ece` equals the tree of PR head `f30145c7`.
  - Verified as a local git object only. Containment on main is conductor-attested.
- READY `6e7bb25cf2305e385d43e6351f96327500606714f32556b009cd21c5ec9f5b87`
- SCORE JSON `0dc21298f0b2dcd1c2804df9fab44585bea9275550b352ccb65c8c52cc0703b8`
- Authority: a Conductor message, plus ruling `6142d4c7…`: "Examiner may score part (a) at a940355a now. Gross is the headline, net is illustrative (R39), and N6 applies." There is no `CONDUCTOR_SCORE_KICK_*EXT_K2*` file.

## Verdict (part (a), which is the packet verdict): **DESCRIPTIVE**

- **Labels:** dev-grade (DEV_GRADE_REUSED_31_GAME_COHORT) · HYPOTHETICAL_REPLAY_FILLS · IN_SAMPLE_DEV.
- **Regime label:** contemporaneous, not causal (R15).
- **Claims and flags:** no tradable-signal claim · counts_toward_keep=false · promote=false · feeds_gate=false · fee label CACHE_NOT_R1P1.
- **Q6-000:** unchanged. It was not retuned, and K2 gives it no KEEP and no KILL.

**Promote bar**, freeze R08 (L197), quoted verbatim:

> **Verdict domain {DESCRIPTIVE, ITERATE, INCONCLUSIVE} only.** No KEEP, no KILL of 000, no retune, no promotion. `counts_toward_keep=false`, `promote=false`, `feeds_gate=false`. The packet verdict is the part (a) verdict (R23). Part (b) carries its own label ∈ {DESCRIPTIVE, INCONCLUSIVE} (R44) and **can never move** the part (a) verdict or any gate. `results`/`pnl`/`roi` = null in this packet.

**Pre-declared rule**, freeze R23 (L216, md `d69a4f62…`), quoted verbatim:

> **Part (a) verdict (Examiner-owned; proposal).** **INCONCLUSIVE** if any of these holds: the K1 R36 gate fails; the T03 fixture reproduction fails; UNCLASSIFIED exceeds 20% of opening contracts; censoring at H\* exceeds 20% of opening contracts in T1 or in T3; fewer than 5 games contribute opening portions to T1 or to T3; more than 5% of bootstrap resamples are dropped. Otherwise **ITERATE** if the 95% CI of Δ\*_a excludes 0, in either direction: flow-mix dependence of 000's open-leg markout is then visible on the dev cohort and warrants a separate freeze. Otherwise **DESCRIPTIVE**.

**Overlay:** N6 ruling `0b68c4bf…` says an undefined Δ* or CI means INCONCLUSIVE. The code implements this as `undefined_contrast`.

**How the rule applies:**
- **No INCONCLUSIVE trigger fires.**

  | Trigger | Value | Limit |
  |---|---|---|
  | K1 R36 gate | Passes (independent recount below) | Must pass |
  | T03 fixture | Cuts exact; bucket table byte-identical to `9acb5288…` | Must reproduce |
  | UNCLASSIFIED | 0% of opening contracts | ≤ 20% |
  | Censored at H*: T1 | 0.4873% | ≤ 20% |
  | Censored at H*: T3 | 0.9654% | ≤ 20% |
  | Games contributing: T1 | 27 | ≥ 5 |
  | Games contributing: T3 | 30 | ≥ 5 |
  | Bootstrap resamples dropped | 0 of 10,000 | ≤ 5% |
  | N6 (undefined Δ* or CI) | Both defined | Must be defined |

  R36 recount, done independently: 12,853 / 681,732 / 364,988 / 62; maker NO share 0.989706; taker YES share 0.916882; 6,161 portions; UCH 603,262.7291.
- **The ITERATE test fails:** the gross 95% CI contains 0.
- **Result:** DESCRIPTIVE. Under R25, only Δ*_a can move the verdict.

## Primary contrast (gross is the headline)

Δ*_a = contract-weighted MO_1800(T3_HIGH) − MO_1800(T1_LOW), on the primary ticker-hour unit, in $/contract.

| | Δ*_a | 95% CI (game-cluster bootstrap, B = 10,000, seed 20261003, type-7) |
|---|---|---|
| **Gross (headline)** | **−0.000301641** | **[−0.001030989, 0.000450135]** |
| Net (illustrative only; $0.01 round-up, CACHE_NOT_R1P1) | -0.000413889 | [-0.001083898, 0.000245087] |

**Examiner recompute.** I built my own pipeline from the pinned bundles, with no lab or runner imports:
- inputs: K1 bundle `0f8f5297…` and K2 delta bundle `963f7663…`;
- my own code throughout: flow terciles, FIFO lots, trailing-60 window, quote-mid MO_1800, Decimal fees;
- the bootstrap mirrors the code at a940355a exactly.

Results:
- **Gross:** -0.0003016413076326061, CI [-0.0010309890421085896, 0.0004501346780537653]. Equal to the claimed and Adversary values to every printed digit.
- **Net:** -0.00041388938, CI [-0.0010838975, 0.0002450875].
- **Resamples:** 10000 kept, 0 dropped.
- **Mismatch: none.**
- **Constancy sha recomputed:** `523f840babd3e57d8a305ecc458f979d9288e69082210edaf8648e3132101968`. It matches the claimed `523f840b`.
- **Cuts:** c1 0.9271702456462422, c2 0.989881659505818, e1 0.9126590461375717, e2 0.9359888338062846. All exact.

**Cells at H = 1800 s:**

| Cell | Portions | Contracts | Games | MO gross | MO net |
|---|---|---|---|---|---|
| T1_LOW | 1677 | 34,273.54 | 27 | 0.00508 | 0.001278 |
| T3_HIGH | 751 | 25,175.31 | 30 | 0.004778 | 0.000864 |

Portion counts:
- Primary: T1 1,677 / T2 3,733 / T3 751.
- Secondary: 2,299 / 2,276 / 1,586.
- Causal trailing-60 sensitivity: 1,853 / 3,654 / 654.

**Tests and reruns:**
- A fresh checkout at a940355a gives **Ran 37 tests, OK**, and the tree is clean afterwards.
- Re-running `run_part_a` in a scratch copy reproduces all 5 `results_a/*.json` files byte-for-byte.
- `UNIT_RESULTS.md` differs only in the hand-appended "34 tests" paragraph (A9).

**Bootstrap ordering (descriptive only).** Freeze R22 does not pin the draw primitive or the game order.
- The code uses `randrange` over the unsorted `week_membership.json` key order.
- K1 used `choices` over sorted events.
- Alternate gross CIs:
  - `randrange` over sorted games: [-0.001023, 0.000444];
  - K1-style: [-0.001039, 0.000438].
- Both contain 0, so the verdict does not change.

**Descriptive units, outside the verdict (R25).** Point estimates only, recomputed by me and equal to the committed values:
- Secondary event unit: Δ gross +0.000096.
- **Causal trailing-60 sensitivity: Δ gross +0.000581.** This is the opposite sign to the contemporaneous primary.
- Per Adversary A10, Δ*_a is read as a static, contemporaneous description only.

## Fees

- **Headline:** $0.01 round-up per maker order (K1 R24 / freeze R20; CACHE_NOT_R1P1). Maker-order fee total **$1286.22** over 1846 orders, computed with Decimal(str). Equal to K1.
- **Gross is the headline; net is illustrative only.**
- **Direct-member $0.0001 (sensitivity only):** net Δ*_a -0.000417, CI [-0.001086, 0.000239].
- **Member class: null / OPEN.** ADDENDUM_02 `44a69092…` has member_type null, and 530cca94 says "member class NULL stays OPEN".
- **R2-P5:** no fee-honest claim. The fees do not use formula_id `astra.r1p1.feebook.claude_order_level_ceil.v1`.

## Outcome exposure

**Outcomes were not viewed before the freeze for part (a).**
- **Basis:** the author's declaration in freeze §6 [A], plus the tercile fixture, which was written at 16:42:57 ET from B1 trade rows only [V, Adversary §2]. Part (a) reads no score, settlement or nflverse byte (R19), so no ex-post anchor applies.
- **Disclosed exposures:**
  - Design-time look: dev-tape flow share quantiles at thresholds 1/5/10/20 seen before R13 pinned (label-free).
  - Scout brief incl. 000's reported net was seen (freeze §6).
  - Becker: which 2025 games did not resolve yes/no (part (b) exclusion) was seen; yes/no split never computed.
  - [V, K1 freeze §6] Same Variants seat printed 2026 W1–W2 nflverse scores before the K1 freeze (K1 §6); part (a) does not use them. (Correction: the SCORE JSON tags this item [U]; the correct tag is [V], per the K1 freeze §6 disclosure.)
  - [U] EXT-K1 results commit 7415447c (16:45:23 ET, MO_1800 of the same 000 portions by consensus bucket) predates the K2 freeze by ~3.5 min; whether the K2 author viewed it is unknown. Tercile cuts were already fixed at 16:42:57 from flow only.

## Part (b): NOT scored

- Part (b) waits for the Simulator's box run under the Conductor pre-run conditions (`6142d4c7…`: A4 RAM gate, A5 receipt integrity, A7 attempt ledger, A11 run dir) and for the Adversary's 24-item output check (review §11).
- At filing, no run dir and no attempt ledger exist.
- All part (b) fields are null for that reason.
- Part (b) can never move the part (a) verdict (R08/R44).

## R32 governance note (`6142d4c7…` §A3)

- R32 is the part (b) Becker exclusion rule. List membership is accepted as an implementation detail, and "No bar changed."
- **No effect on part (a).**

## Adversary advisories carried (review `7fcc66f7…`, CLEAR_WITH_ADVISORIES)
- **A1** (latent / test power): T01(b) passes permuted labels and quotes only to the refusing kwargs, so the rebuild runs on unpermuted flow. Fold the live-permutation path from `probe_t01_positive_control.py` into the test
  - Disposition: tracked (test power); fold live-permutation path into T01(b)
- **A2** (latent (gate passes)): When the R36 gate fails, markouts are still computed and written (the verdict becomes INCONCLUSIVE). Freeze R12 says "no markout"
  - Disposition: tracked (latent; gate passed this run)
- **A3** (documentation): The R32 deviation (membership instead of bytes) is recorded only in the merge note. Add the byte assert or file a deviation note
  - Disposition: recorded as Conductor governance note 6142d4c7; part (b) only; no part (a) effect
- **A4** (operational, part (b) only): **Part (b) RAM gate not in code. Mandatory pre-run condition** (checklist item 1)
  - Disposition: MANDATORY part (b) pre-run condition (Conductor wrapper: MemAvailable >= 7 GiB x3, ~6.5 GB cap)
- **A5** (integrity, part (b) only): **Receipt does not prove a clean tree. FREEZE_SHA256 and the vendored ACCEPT (net flag) are not sha-checked at run time. Mandatory pre-run check** (checklist item 2)
  - Disposition: MANDATORY part (b) pre-run condition (clean tree, FREEZE_SHA256 + vendored ACCEPT sha check)
- **A6** (latent): The T11 banned set omits event tickers and untraded market tickers, and matching is exact-match only
  - Disposition: test-only follow-up per Conductor; not a run blocker
- **A7** (process): A part (b) INCONCLUSIVE leaves no labelled artifact (receipt and exception only). The Simulator must record it
  - Disposition: process: attempt ledger per Conductor (one published attempt)
- **A8** (completeness): R39 per-row taker nets and taker gross mirrors are not emitted (only the sweep-group variant)
  - Disposition: completeness, part (b) descriptive
- **A9** (cosmetic, known): "34 tests" in UNIT_RESULTS.md and the registry row; actual 37
  - Disposition: cosmetic; merge note says it is to be fixed in the K1 follow-up PR
- **A10** (scope): The primary label is contemporaneous (R15). The Examiner should read Δ\*_a as descriptive only. The causal trailing-60 split exists (T1 1,853 / T3 654 portions)
  - Disposition: SCOPE — applied in this score: Δ*_a read as contemporaneous, static, descriptive only
- **A11** (process): The run-dir path is not pinned in code, and the freeze's `results_b/` copy sits in the governance tree. Keep it out of any sync
  - Disposition: process: run-dir pinned by Conductor to /workspace/runs/ext_k2_partb_20261003/
- **A12** (latent): Traded-only exclusion would not close events around untraded unsettled markets on other datasets. No effect on t0
  - Disposition: latent; no effect on t0

## Multiplicity and cohort context

- family_size = 1. Only gross Δ*_a can move the verdict (R25). Every other unit, horizon, net figure, per-game table, and all of part (b), is descriptive.
- Cohort: the reused 31-game 2026 W1–W2 dev cohort, so the effective n is 31 game clusters. T1 draws from 27 games and T3 from 30.
- The same cohort underlies EXT-K1 (DESCRIPTIVE, `530cca94…`) and K3: all dev-grade, with no KEEP. No correction is applied because nothing is claimed.

## v1.2 common fields (all null, with reasons)
- **net_pnl_without_rewards**: null. Measurement-only; results/pnl/roi null by freeze; markouts of hypothetical replay fills are not P&L
- **net_pnl_with_rewards**: null. No Astra P&L; no rewards thesis
- **rewards_actually_earned**: null. No Astra activity
- **calibration**: "N/A". Not probability-emitting
- **fill_rate**: null. Q6-000 hypothetical replay fills; no demo/shadow/live Astra orders
- **adverse_selection_after_fills**: null. Template field is for real Astra fills (positive = against us); K2 reports hypothetical-fill MO_h with the opposite sign (positive = favourable), descriptive only; no SETTLE in K2 (R19)
- **feasible_vs_requested_size**: null. No Astra orders
- **unresolved_inventory**: null. No Astra positions (replay residual 0, descriptive)
- **capital_hours**: null. No Astra positions; replay UCH 603,262.7291 is hypothetical/descriptive
- **drawdown**: null. No Astra P&L series
- **event_concentration**: null. Template metric uses Astra net P&L; none exists
- **study_label**: historical replay.
- **executable_dollars_per_day**: null. No signal claim; Archivist fee/account manifest DRAFT_NOT_ADOPTED.

## Pins

- Freeze md `d69a4f62…` / json `025a01a1…`
- ACCEPT `d76779e1…`
- MERGE `65b6c7f6…`
- Adversary `7fcc66f7…`
- Part (b) / R32 ruling `6142d4c7…`
- N6 ruling `0b68c4bf…`
- Fee ruling `870895a5…`
- Packet MANIFEST `3478b405…` (11/11 files OK)
- K2 delta bundle `963f7663…`; K1 bundle `0f8f5297…`
- TERCILE_BUCKETS `9acb5288…`
- In-repo HOLD_PRE_PR (untouched) `927bead8…`
- Precedent, cited only: EXT-K1 SCORE `0e5b1060…`, scorecard `b5e08bf8…`, Conductor ACCEPT `530cca94…`

## Anomalies
- No CONDUCTOR_SCORE_KICK_*EXT_K2* file on disk; authority = Conductor message + ruling 6142d4c7.
- No Simulator READY for EXT-K2 (not required for measurement-only lab per 530cca94); run records = Variants v67b e8d6ac84 + Adversary 7fcc66f7.
- a940355a exists locally only in the Adversary's clone and /workspace/tmp/pr57-verify/repo; containment conductor-attested, not fetched.
- Part (a) bootstrap draw primitive/order not pinned by freeze R22 (code: randrange over unsorted week_membership key order; K1 used choices over sorted events). CI shifts in the 5th decimal under alternates; all contain 0; verdict invariant.
- UNIT_RESULTS.md hand paragraph says '34 tests'; actual 37 (A9).
- In-repo EXAMINER_HOLD_PRE_PR.json is implementer-authored (signed_by_examiner=false) under an EXAMINER_ name; left untouched (927bead8...).
- EXT-K1 results commit (16:45:23 ET) predates the K2 freeze (16:48:49); author exposure [U]; tercile cuts fixed earlier (16:42:57) from flow only.
- Packet-dir FROZEN_EXPERIMENT.json (eb7bb3df...) and lab FROZEN_EXPERIMENT.json (4220fd84...) are different artifacts; freeze md/json pinned by sha only (not vendored) per R45 ruling.
- Merge packet is a .md (65b6c7f6...), not JSON.

No orders were placed, no messages sent, and nothing was fetched. No Becker data was read. Only new EXAMINER_* files and scratch files were written.
