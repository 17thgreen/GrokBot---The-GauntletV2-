# ADVERSARY — EXT-K1 pre-score review (Q6-000 legging-risk audit, PR #66)

**Seat:** The Adversary "KALSHI" (Astra Drift Guard, Working Plan v0.1). **ADVISORY ONLY.** This does not replace the Examiner and invents no failures. No live orders, no Kalshi GET, no messages to anyone.
**Filed:** 2026-10-03 ~17:05 ET (America/New_York, UTC−4).
**Target:** `17thgreen/GPT-6-Astra-Deathmatch` main@`09b56273eb3b11ec3968e273a28767569e368561` (PR #66 squash of head `7415447c591dd75a19a2974ebbc458fb3acc3380`). Lab dir `kalshi_ext_k1_q6000_legging_audit_lab_20261003/`.
**Evidence tags:** [V] verified on box this session · [I] inferred · [H] hypothesis · [A] assumption · [U] unknown.

## VERDICT: **CLEAR**. The Examiner may score, within {DESCRIPTIVE, ITERATE, INCONCLUSIVE} only.

- **Blocking fixes: none.** No item below could change the DESCRIPTIVE verdict or undermine the gate or label validity for this run. The flags are tracked advisories (§6).
- **Q6-000 is unchanged.** Its verdict does not move and there is no retune. The 000 code and ledger shas equal the freeze pins (§5).
- **Scope reminder for the Examiner (binding per freeze §6 and R33).** EXT-K1 is an ex-post description of the *replayed* 000 against a consensus line of unknown timing. It is not a tradable signal and not evidence that a gate works. The verdict should not count toward KEEP, and nothing should be promoted.

## 0. Inputs checked (hashes re-computed on box this session) [V]

| Item | sha256 / value |
|---|---|
| Freeze md `packets/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.md` | `5c40fb9d03a924e40577a81f262231701e331c98922f60f6dc7ab65a2dbed6d3` |
| Freeze json twin | `be3e88336389bc62c40413785e6ffb4a572e1dbd006d7cf3dfbc962f8184efaa` |
| `CONDUCTOR_ACCEPT_EXT_K1_FREEZE_2026-10-03.json` (issued 16:16:49 ET) | `021290077cbbed277455145d2e56e1335f6ae331d56c2ad79d4d85b405559397` |
| `CONDUCTOR_MERGE_PR66_EXT_K1_2026-10-03.json` (issued 16:54:08 ET) | `9de0933b8ec8ade5cbb89d5372116fb76048e30007af1b8f0e09f17fbae28deb` |
| `CONDUCTOR_KICK_ADVERSARY_EXT_K1_PR66_DESCRIPTIVE_2026-10-03.json` | `113c111ad6e1bc02d0ff413945f5364038bf8cc4d4128be542a7ac3ed4beab7b` |
| Packet dir `EXT_K1_LEGGING_AUDIT/MANIFEST.sha256` | `5e8f7906…`; `sha256sum -c` all OK, including box `CONSENSUS_FIXTURE.json` `9996b198…` |
| Variants verify `/workspace/v66/REPORT.md` | `f3552b58d571be2147024e94e666831e036cb11f199214c53d0c6750b978c4d0` |
| main@09b56273 tree vs head 7415447c tree | identical (`622e4c93b8afbbaeea9fd6185916a8a54719ec30`, both) |
| PR diff 761eaaed..7415447c | 80 A under the lab dir plus 1 M `docs/EXPERIMENT_REGISTRY.md`; nothing else |
| R1-P3-ADVERSE brief `briefs/R1-P3-ADVERSE_2026-09-22.md` | `01df4d8d831ba3e4f8ba4034e67d0951f92b7e02a505cc882c3871e9fbc281cd` |

**My re-run** used a read-only copy of the clone at `/workspace/scratch_extk1_adv/repo` with `measure(write=False)`. `git status` stayed clean, and no shared file was touched. It reproduced: verdict DESCRIPTIVE; Δ\* gross −0.000205191, CI95 [−0.000577471, 0.000188188]; net −0.000373009, CI95 [−0.000775055, 0.000086859]; 10,000 resamples kept, 0 dropped; constancy `a73a90e0…` [V]. Scripts and outputs: `/workspace/scratch_extk1_adv/adv_probe.py` (`95f1a143…`) → `adv_probe_out.json` (`d1988cce…`); `probe_invariance_adv.py` (`d599d79b…`) → `probe_invariance_adv_out.json` (`d63307a3…`).

## 1. Timeline (ET) — were the parameters fixed before outcomes were seen?

| ET (2026-10-03) | Event | Source | Tag |
|---|---|---|---|
| 15:59:53 | Scout external-hunt freeze stamp | `scout_external_hunt_2026-10-03/FREEZE_STAMP.txt` | [V] |
| 16:00:58 | nflverse `games.csv` fetched; it contains scores for all cohort games | `raw/MANIFEST.sha256` | [V] |
| 16:06:39 | Ruling file mtime (`issued_et` 16:10, clerical skew already noted) | freeze §0 | [V] |
| 16:10:29 | Variants `consensus_table.json` written (moneylines only); byte-identical to box `CONSENSUS_FIXTURE.json` | `/workspace/ext_k1_scratch/` mtime, `cmp` | [V] |
| 16:11:11–16:11:17 | `structural_verify.py` and its output (counts only; reads no score) | mtimes; `rg score` finds only the docstring | [V] |
| ~16:07–16:14:59 | Scores printed while the join was being checked (disclosure) | freeze §6 L164; no print log or timestamp exists on box | [I] window / [U] exact time |
| **16:14:59** | **Freeze declared.** x=0.02, E=0, δ=0.005, H\*=1800, grid and de-vig all fixed | freeze L3, R16/R27/R28; `ext_k1_scratch/NOW.txt` | [V] |
| 16:16:49 | Conductor ACCEPT | ACCEPT json | [V] |
| 16:39:33 | Cloud test run | `results/UNIT_RESULTS.md` L7 (20:39:33Z) | [V] |
| 16:45:06–16:45:23 | PR commits `3ab5cd59` (pins) → `32e10492` (code) → `7415447c` (results) | git log (20:45Z) | [V] |
| 16:54:01 | Squash merge `09b56273` | git log (13:54:01 −0700) | [V] |

## 2. Per-item rulings

### (a) LOOKAHEAD via the ex-post nflverse anchor — **CLEAR (advisory A1–A4)**

1. **Does the anchor use information unavailable at decision time?** Possibly, by design. nflverse does not document the moneyline snapshot time [U] (freeze R09, L68). The file was fetched after every cohort game [V]. 000's fills run up to about 7 days before kickoff, so the line may post-date every fill. The freeze names this and binds it: §6 L167 says "cannot support any claim that a tradable pre-game signal or gate exists". The PR carries it in code: `constants.py:92` EX_POST_SENTENCE, `report.py:258-275` `stamp_ex_post`, and the `UNIT_RESULTS.md` L49 headline paragraph [V]. Variants counted 0 of about 9.9k result dicts missing the tag (REPORT.md L21).
2. **Does it leak into the gate, the buckets or the side labels?** The anchor *defines* the S_DEV labels and the gate threshold input (`consensus.py:203-246`, `orchestrator.py:238-252`, `gate.py:31-54,80-85`). That is the measurement, not a leak, and it is exactly what `EX_POST_ANCHOR_U` covers. **Realized outcomes do not reach labels, gate or buckets** [V]:
   - Code: scores are copied into join rows (`consensus.py:176-177`) and read only by `settlement_value` (`consensus.py:248-267`) → SETTLE markout (`markouts.py:101-106`) and `artifacts.settle_artifact`. `gate_on_fill` refuses `score`/`tape`/`markout` arguments (`gate.py:31-45`).
   - End-to-end: I permuted scores inside the `games.csv` text and rebuilt join → consensus → gate/splits → fees → markouts for **100 permutations** (Variants' 25 seed-7 shuffles plus shift-1, reproduced, and 74 more with seed 20261003). All gave **1 distinct constancy sha `a73a90e0…`**, while SETTLE took 101 distinct values [V].
   - **Positive control** (the test has power): a shift-1 permutation of the *moneylines* changes the constancy sha to `fec95851…`, and `gate_assignments` and `splits` both change [V].
3. **Is the primary metric even outcome-dependent?** No. Δ\* is MO_1800, a mid-to-mid markout from B1 quote rows (R19/R20/R31); scores never enter it [V code]. Outcome exposure could only matter through *parameter choice*. Choosing δ or x to tilt a 30-minute mid markout from 31 final scores would also need per-portion dev values or markouts, and none existed before the freeze [I]. The disclosure says none was computed (freeze §6 L164), and the pre-freeze scratch dir holds only moneyline and count artifacts [V file listing].
4. **Were 2c and 0.5c fixed before outcomes were seen?** Yes, both are in the freeze at 16:14:59 ET [V]. No earlier freeze draft, `_prev` copy or parameter sweep exists on box (`rg`/`find` over `/workspace`; only `ext_k1_scratch/` and the bundle) [V absence]. The PR constants match exactly: `constants.py:67-75` (H\*=1800, δ=0.005, δ-sens {0, 0.01}, primary gate {x 0.02, E 0, proportional}, grid) [V].
   - **x = 2c** has a label-free rationale (two 1¢ ticks; B1 median quoted spread 1¢, Scout brief L22, filed ~16:05) [V]. It also matches **prior-dated lab use of a 2¢ probability gap**: `packets/CARD01_EXP2_CENSUS_GATECOUNT_FREEZE_KERNEL_2026-09-24.md` L119 (noise floor `gap_abs ≤ 0.02`, "2¢ probability") and the NH-001 "2c buffer" (`CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24.md` L191; `CARD02_…_2026-09-24.md` L115). Those files are named 09-24 with mtimes 2026-10-01 23:12 ET, both before the outcomes [V prior-dated]. The contexts differ (buffer and noise floor, not a refusal threshold), so this is consistency rather than a binding convention.
   - **δ = 0.5c**: I found **no** prior lab convention (`rg` for 0.005, half-tick and dead band in governance and astra-science found nothing comparable) [V absence]. Its rationale, half the 1¢ tick (R16), is label-free [I]. The Scout brief, read before the freeze, cites an external 0.5¢ median Kalshi–book gap (L82); that is also label-free.
   - **Robustness** (my scratch run, sensitivities only, never selection): δ=0 gives Δ\* −0.000153, CI [−0.000443, 0.000200]; δ=0.01 gives −0.000308, CI [−0.000862, 0.000163]. The verdict is unchanged across the frozen δ range [V].
5. **Does the label-permutation test address outcome exposure?** **Partly.** It proves the *code path* is outcome-free (the label leak). It **cannot** prove the *researcher* did not choose parameters after seeing outcomes; that rests on the timeline, the label-free rationales and the disclosure [A for anything that leaves no file]. It also says nothing about whether the moneyline itself post-dates the fills [U]. For this run the residual risk is low because Δ\* never reads outcomes and the verdict is stable across δ and de-vig [I].
6. **Is the label adequate and the claim scoped?** Adequate for a DESCRIPTIVE verdict. **A1:** do not narrate the GATE.json "refused vs kept" markouts (refused 0.003685 vs kept 0.005068 gross at 1800 s, `UNIT_RESULTS.md` L70) as gate efficacy. They are static attribution (R30), ex-post, outside the verdict (R38), and the share depends on de-vig (see (e)). **A2:** the T02 truncation test (`tests/test_t02_lookahead.py:17-32`) cannot catch anchor-time lookahead, because p_cons is passed in untruncated. It guards the tape and ledger only; the anchor's timing stays [U].

### (b) N1 — T01 reuses precomputed results — **ACCEPTABLE for this score; tracked fix A3**

- **What T01 checks** [V]. `tests/test_t01_permutation.py:51-67` calls `measure()` once. It then runs 1,000 `Random(20261003)` shuffles plus shift-1 on the cached portions through `invariance_blobs → artifact_bytes`. Only `settle_artifact` sees the permuted games, so join, consensus, gate and markouts are **not rebuilt**. Part (b) is close to tautological. Part (a) (L26-49) is a real fixture test, though L43 is a no-op assertion (`... for token in left and []`).
- **Can reuse mask a bug?** In principle yes: if join, consensus or gate ever read a score column, T01(b) would still pass. For the merged code, the end-to-end probe closes that gap (100/100 constant, positive control fires; see (a)2).
- **Are the 26 shuffles logged and reproducible?** Yes, on box only. `/workspace/v66/probe_invariance.py` (`be83472f…`) uses `random.Random(7)`, 25 shuffles plus shift-1, and its output is `probe_invariance.json`. I re-ran it byte-for-byte and got the same constancy [V]. It is **not** in the repo.
- **A3 (tracked fix, before the code is reused for any new cohort or freeze):** move the end-to-end rebuild (permute the csv bytes and rebuild join, consensus, gate and markouts) into T01, add the moneyline positive control, and delete the no-op L43. Also correct `UNIT_RESULTS.md` L76: "One thousand … shuffles … left these artifacts byte-identical" overstates T01(b). The end-to-end coverage is 26 runs (Variants) plus 100 (Adversary, including those 26 reproduced).

### (c) N5 — INVARIANCE.json missing R33 flags — **COSMETIC; tracked fix A4**

- **R33** (freeze L149): every output carries `DEV_GRADE_REUSED_31_GAME_COHORT`, `HYPOTHETICAL_REPLAY_FILLS` and `IN_SAMPLE_DEV`; p_cons outputs also carry `EX_POST_ANCHOR_U` plus the sentence.
- `results/INVARIANCE.json` is written by the test (`test_t01_permutation.py:68-85`) through `stamp_ex_post` only, not `_common_header()` (`orchestrator.py:374-391`). So it has `EX_POST_ANCHOR_U`, the sentence, `[U]`, null results/pnl/roi and `counts_toward_keep:false`, but lacks the three R33 dev flags [V]. The other six results JSONs carry them [V].
- **Does it hide a failed or unrun check?** No. The file records `permutations:1000`, `seed:20261003`, `derangement:shift-1`, the four artifact shas and constancy `a73a90e0…`. All of these reproduce (Variants recompute and my run), and T01 passes in `tests_run.log` [V]. The flags are labels, not checks. Fix: build the record with `_common_header()`, or have T14 also assert the R33 flags.

### (d) N6 — an empty bucket would return DESCRIPTIVE — **LATENT, does not bind this run; tracked fix A5**

- **Mechanism** [V]. If the ON or AGAINST bucket is empty, `summarize` gives `mean_gross=None` (`report.py:52-55`), so Δ\* is None (`report.py:154-157`). Every bootstrap draw is dropped (L180-182), so the CI is None and `ci_excludes_0=False` (L189). `censored_share` returns None for 0 contracts (L214-218), so no INCONCLUSIVE trigger fires, and `decide_verdict` returns **DESCRIPTIVE** (L250-252). Freeze criterion (iv) favours INCONCLUSIVE.
- **This run, pooled buckets (S_DEV, δ=0.005)** [V re-run]:

| Bucket | Portions | Contracts | Censored @1800 s (contract share) |
|---|---|---|---|
| ON | 2,664 | 68,640.58 | 0.22% |
| AGAINST | 2,578 | 72,781.55 | 0.43% |
| NEUTRAL | 919 | 22,096.09 | — |
| UNCLASSIFIED | 0 | 0 | — |

  Bootstrap: 10,000 kept, **0 dropped**. No pooled bucket is empty or near-empty.
- **Game-level sparsity** [V], which the bootstrap tolerated with 0 drops: 9 of 31 games lack ON or AGAINST. ARILAC ON17 only; CHICAR NEUTRAL31; MIALV NEUTRAL88; TBCIN ON15/N1; WASPHI AGAINST1; CLETB ON27; INDKC ON11; PHITEN ON232; SEAARI ON17/N19. AGAINST appears in 23 games and ON in 28. The smallest non-zero per-game count is 1 for both. This is descriptive context for the Examiner; it does not trigger anything.
- **Ruling:** a **tracked fix**, not a pre-score blocker, because it cannot change this run's verdict. **A5:** return INCONCLUSIVE when Δ\* or the CI is None, or when dropped resamples exceed a pre-stated share. Make it binding before this code is reused (any counterfactual-gate freeze, season-scale or new cohort). Because it changes R32 semantics, it needs a Conductor-accepted note or a new freeze, not a silent edit.

### (e) N3 — overround and de-vig convention — **CLEAR; de-vig named in the freeze; tracked fixes A6/A7**

- **De-vig is named in the freeze.** R12 (L128) fixes **proportional as PRIMARY**, p_home = q_h/(q_h+q_a), with **Shin as SENSITIVITY** (bisection z∈[0, 0.4], 200 iterations). R27/R28 put both in the gate grid, and the primary cell is `x=0.02|E=0|devig=proportional` [V]. This meets R1-P3-ADVERSE §1 L42 / L81 ("freeze must name which de-vig") [V]. The code matches: `consensus.py:73-106`, `orchestrator.py:238-252`, `constants.py:72-75`.
- **Overround** is not a de-vig input. The PR defines it as q_a+q_h (`consensus.py:155`, `orchestrator.py:723`); the frozen box fixture uses q_a+q_h−1 (`EXT_K1_LEGGING_AUDIT/CONSENSUS_FIXTURE.json`, NE@SEA 0.040727 vs PR 1.040727). The difference is a constant 1.0 within 5e-7 for every row [V]. **No metric reads overround** (`rg overround` hits only the fixture writer and T11/T14) [V]. p_home_prop and p_home_shin match the box fixture within 4.98e-7 and 4.80e-7 [V].
  - **A6:** T11 as implemented compares the PR output with itself (`tests/test_t11_devig.py:26-40`), not with the frozen box fixture. Freeze T11 (L188) asks for overround reproduction within 1e-6, so literally the overround check fails by a definitional 1.0. Record the definitional deviation and point T11 at the frozen fixture (it can be vendored by sha `9996b198…`).
- **Can the choice flip with/against labels near 50/50 or within the dead band?** Within the dead band, yes; across sides, no [V re-run]:
  - Proportional vs Shin moves **1,439 portions / 35,534.02 contracts** (about 21.7% of the 163,518.22 opening contracts) between buckets: ON→NEUTRAL 509, NEUTRAL→AGAINST 491, NEUTRAL→ON 281, AGAINST→NEUTRAL 158. **Zero ON↔AGAINST flips.** Max |p_cons,shin − p_cons,prop| = 0.01556.
  - **S_FAV flips between methods: 0** (favorite identical for 31/31 games; consistent with freeze §4). Only 2 games have p_cons within 2¢ of 0.5 (BUFHOU, NYJTEN; 267 portions).
  - 614 portions (17,803.69 contracts) sit within 0.25¢ of the ±0.5¢ boundary.
  - **Δ\* under Shin labels** (Adversary sensitivity, never selection): −0.000216, CI [−0.000545, 0.000179]. **The verdict is unchanged.**
  - **A7:** the **gate headline does depend on de-vig.** The primary cell refuses 12.25% of contracts (700 portions) and 14.42% of UCH; the Shin twin `x=0.02|E=0|devig=shin` refuses **7.97%** (462 portions) and **10.72%** of UCH (GATE.json cell 10) [V]. Quote "12.3% / 14.4%" only together with the Shin twin. It is descriptive, not a robust property.

## 3. Fee blindness — **CLEAR (advisory A8)**

- R31/R32 make the verdict gross-based by freeze. Net is reported beside it (`report.py:196-201`; `UNIT_RESULTS.md` L58). Under the **fee-honest view the verdict is the same**: net Δ\* −0.000373, CI95 [−0.000775, +0.0000869] still includes 0 [V]. A fee-honest view is therefore available and does not move the DESCRIPTIVE verdict; no additional fee work is needed before scoring.
- **A8:** the fee headline is `CACHE_NOT_R1P1` `NON_DIRECT_CENT_HEADLINE` ($1,286.22), and `examiner_pin_account_class` is still null [V]. The Examiner should pin it. Also, fees absorb most of the 30-minute markout: ON 0.004955 gross vs 0.001084 net, AGAINST 0.004750 vs 0.000711 $/contract [V]. Any later gate or variant claim must be net and counterfactual (R30), never gross static attribution.

## 4. Other named risks

- **Regime break / capacity fantasy:** none beyond what the freeze already binds. The data is the reused 31-game dev cohort with hypothetical replay fills (queue 3,300 assumption), the tape ends at K−174 min, and the verdict cannot count toward KEEP [V freeze §7]. Nothing in EXT-K1 scales size or claims capacity [V].
- **A9 (registry wording):** the `docs/EXPERIMENT_REGISTRY.md` row says "Hypothesis frozen 2026-10-03 before this implementation" but does not mention that final scores were viewed before the freeze (freeze §6 does). Add "outcome exposure disclosed (scores viewed pre-freeze; no gate parameter derived from them)" so the public row is not read as a clean pre-outcome prereg.
- **Carried, not re-litigated:** N2 (T10 tamper test does not exercise the runtime path; Variants probed the runtime path fail-closed), N4 (schedule line-number reading), N7 (ADMIT-1 rows raise instead of being counted; 0 rows). None affects the verdict [V from REPORT.md; not re-run by me except where stated].

## 5. Drift / 000 retune check — **CLEAR**

These box shas equal the freeze pins [V]: `nfl_factorial_lab_20260921/` `replay_v2.py` `5aba1bf3…`, `queue_policies.py` `641d0df3…`, `run_experiment.py` `c1a0fd2d…`, `q3300_d0.25_000.json` `78b94ae5…`, fills `9d56f5d3…`, orders `c390801b…`, decisions `e6db5237…`, `SHADOW_CANDIDATE_FREEZE.json` `b55ff36c…`. `git status` of that dir in `astra-science` is clean, and the PR diff touches nothing outside the new lab dir plus one registry row. Zero 000 knobs and zero changed parameters (freeze L7; `_common_header new_knobs: 0`). **The Q6-000 shadow incumbent verdict is unchanged.**

## 6. Advisory list (tracked; none blocking)

| ID | Advisory | When |
|---|---|---|
| A1 | Do not read GATE refused-vs-kept markouts as gate efficacy; static, ex-post, outside the verdict | Examiner narrative now |
| A2 | T02 cannot test anchor-time lookahead; the anchor stays [U] | Note in scorecard |
| A3 | Move the end-to-end permutation rebuild plus the moneyline positive control into T01; drop the L43 no-op; fix `UNIT_RESULTS.md` "1000 shuffles" wording | Before code reuse |
| A4 | INVARIANCE.json: add the three R33 dev flags (use `_common_header`); extend T14 | Before code reuse |
| A5 | Empty bucket or undefined CI → INCONCLUSIVE (needs a Conductor note or new freeze) | Before code reuse |
| A6 | Overround definition deviation (q_a+q_h vs q_a+q_h−1); point T11 at the frozen fixture `9996b198…` | Before code reuse |
| A7 | Quote the gate share with its Shin twin (12.25% vs 7.97% of contracts; 14.42% vs 10.72% of UCH) | Examiner narrative now |
| A8 | Examiner pins the fee account class; any future gate claim must be net and counterfactual | Examiner now |
| A9 | Registry row should mention the pre-freeze outcome exposure | Next docs PR |

*Advisory only. Not an Examiner score. No KEEP/KILL. Q6-000 unchanged. No live orders. No messages sent.*
