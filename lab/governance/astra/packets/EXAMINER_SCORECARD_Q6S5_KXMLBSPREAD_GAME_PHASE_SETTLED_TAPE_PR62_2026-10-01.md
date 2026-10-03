# EXAMINER SCORECARD — Q6S5 KXMLBSPREAD game-phase settled-tape (PR62)

Template v1.2 (`56bcf6269a42031d9d90496e9a65c2292321aed2165033f6fb44ff8cc4d6b1cc`). Filed 2026-10-01T19:52:49-04:00 ET by Examiner (Kalshi). Machine record: `EXAMINER_SCORE_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` sha256 `1626e2d0e19f0e8cf35fc7b3a9e551f489957dab8e48be2f35216fd36ebda693`. Examiner READY: `EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` sha256 `e6c9ac56be33af2ccc7757409b3bd918034fd2c48a438fd749827cbbd186e4e6`.

## Verdict

**ITERATE.** The reading is **contradicts_H1**. The freeze does not declare that contradicts_H1 supports a KILL, and ACCEPT 08d23b36 and the kick label every reading on this universe as hypothesis-generating only. So KILL is not available, and the verdict is the ITERATE ceiling. KEEP is impossible. counts_toward_keep=false, promote=false.

Pre-declared rule (freeze 5beba803, verbatim):

> - **H1 (in-play adverse selection on passive counterparties):** `maker_gross_roi_delta_GP1_minus_GP0 < 0`. Resting liquidity hit during the game earns less per dollar at risk than resting liquidity hit pregame, because in-play takers act on live game state.
>
> - **Variants-proposed reading (Examiner owns the verdict):** `supports_H1` if the full-sample primary < 0 **and** ≥2 of 3 LOEO primaries < 0. `contradicts_H1` if the full-sample primary ≥ 0 **and** ≥2 of 3 LOEO primaries ≥ 0. Otherwise `inconclusive`. **Confound cap:** if the within-FL1 secondary has the opposite sign to the primary, the reading is capped at `inconclusive_price_confounded`.
>
> - **Verdict ceiling ITERATE:** measurement only. No KEEP, `counts_toward_keep=false`, `promote=false`, evidence_class `IN_SAMPLE_DEV`.
>
> - **Money path:** if `supports_H1`, the next one-knob freeze would put a `pregame_only` restriction on the Q6S5 maker leg, evaluated **only** on the untouched holdout (p16 item 12), never on this tape. Named prior: the sibling desk lists "MLB pregame MM" as dead (`SIBLING_DEATHMATCH_REVIEW` `7cf177c1…`, Claude STRATEGY_BOARD). So `supports_H1` would also point toward a KILL of the KXMLBSPREAD maker leg, not a build, and the Conductor decides. If `contradicts_H1`, in-play passive liquidity is not worse here, which differs from the sibling's pregame-only framing. No retune of Q6-000 either way.

How the rule applies: the full-sample primary is +0.055487 (≥ 0). LOGO primaries are excl. HOUATH -0.348816, excl. LAASEA +0.206348, excl. 0SDLAD +0.410951, so 2/3 are ≥ 0. The within-FL1 secondary is +0.094565, the same sign as the primary, so there is no confound cap. Result: contradicts_H1. The runner's reading_rule agrees.

**Fragility (reported, does not change the reading):** the within-game delta is negative, which is the H1 direction, in 2 of 3 games (LAASEA −0.566, SDLAD −0.269). The pooled positive result comes from the size of HOUATH's swing (+1.095), driven by HOUATH GP0 maker ROI −0.905, mostly HOU2 GP0 (−0.914, n 498). Without HOUATH the primary is −0.349 (LOGO), and without HOU2 it is −0.384 (LOMO).

## Game-phase definitions (freeze, verbatim)

- **Q6S5GP0** — `pregame` — `created_time < scheduled_start_utc` — the print happened before scheduled first pitch
- **Q6S5GP1** — `inplay` — `scheduled_start_utc ≤ created_time < close_time` — the print happened at or after scheduled first pitch and before market close
- **`scheduled_start_utc` (declared, pre-outcome, static contract text):** parse the pinned measured market GET `rules_primary` with the regex `originally scheduled for (Mon) (D), (YYYY) at (H):(MM) (AM|PM) EDT`, convert EDT (UTC−4) to UTC, and require equality with the `event_ticker` time code `YYMONDDHHMM` read as ET. A mismatch or a missing pattern is a **hard fail** (no fallback, no guess). Declared values: `KXMLBSPREAD-26SEP242140HOUATH` → `2026-09-25T01:40:00Z`, `KXMLBSPREAD-26SEP242140LAASEA` → `2026-09-25T01:40:00Z`, `KXMLBSPREAD-26SEP242210SDLAD` → `2026-09-25T02:10:00Z`. These are parsed static fields, not results. `occurrence_datetime` / `expected_expiration_time` (`04:40Z`) are **not** used: they mark expected game end, which is the +3h mismatch the Scout pinned. `close_time` is used only as the post-close exclusion boundary (same as FL-band) and never to assign a phase before the game ends.
- **Proxy caveat (declared):** the scheduled start is a proxy for the actual first pitch. A delay would put a few true-pregame prints into GP1, which mixes the arms and pulls the delta toward 0 (conservative). Getting the actual first pitch would need a new external or live GET, which is refused here. The `start_shift_plus_30m` stress (below) bounds this.

## Labels

IN_SAMPLE_DEV · historical replay · public_counterparty_realized · effective n = 3 games · family_size = 4 (analysis_slice, fill_model, price_band, game_phase) · hypothesis_generating_only · SCHEDULED_START_PROXY · universe cap: this is the last knob · fee CACHE_NOT_R1P1 (not fee-honest, formula_id null) · Astra results/pnl null.

## GP count recompute vs runner constants

| market | runner constant (GP0, GP1, post-close) | Examiner independent |
|---|---|---|
| ATH2 | (22, 475, 0) | (22, 475, 0) |
| HOU2 | (498, 2057, 2) | (498, 2057, 2) |
| LAA2 | (50, 1054, 1) | (50, 1054, 1) |
| SEA2 | (386, 785, 2) | (386, 785, 2) |
| LAD2 | (836, 3308, 0) | (836, 3308, 0) |
| SD2 | (73, 2173, 1) | (73, 2173, 1) |
| **total** | (1865, 9852, 6) | (1865, 9852, 6) |

No mismatches. 11,717 included rows are confirmed independently: 11,723 pinned prints minus 6 post-close; block, native-side, price, non-yes/no and ADMIT-1 exclusions are all 0. Pre/post: GP0 1865/0, GP1 8815/1037. My own parse of rules_primary, cross-checked against the event_ticker codes, gives the same scheduled starts: HOUATH and LAASEA 01:40Z (21:40 ET Sep 24), SDLAD 02:10Z (22:10 ET). Note: the runner's timestamp_only_phase_counts hard-asserts these constants, so its PASS is not independent; this recompute is.

## Primary and secondary (PRE only: 10,680 rows, created_time < 2026-09-25T04:37:47Z)

| arm | maker gross ROI | taker gross ROI | maker net ROI (CACHE) | maker return $ | maker capital $ | n | markets |
|---|---|---|---|---|---|---|---|
| Q6S5GP0 | +0.077375 | -0.084022 | +0.073223 | 18,246.33 | 235,817.27 | 1865 | 6 |
| Q6S5GP1 | +0.132862 | -0.131864 | +0.129381 | 98,510.73 | 741,453.61 | 8815 | 6 |
| Q6S5GP0 within FL1 | +0.077375 | | | 18,246.33 | 235,817.27 | 1865 | 6 |
| Q6S5GP1 within FL1 | +0.171940 | | | 98,413.34 | 572,369.08 | 6576 | 6 |

**Primary GP1−GP0 = +0.055487** (+5.55 pp; H1 says < 0, so not supported).  
**Secondary within FL1 = +0.094565.** All 1,865 GP0 rows fall inside FL1.

### Per game (pre)

| game | GP0 ROI (n) | GP1 ROI (n) | primary | FL1 GP0 (n) | FL1 GP1 (n) | secondary | CACHE primary |
|---|---|---|---|---|---|---|---|
| HOUATH | -0.905061 (520) | +0.189987 (2532) | +1.095048 | -0.905061 (520) | +0.173788 (1957) | +1.078848 | +1.095698 |
| LAASEA | +0.676525 (436) | +0.110215 (1839) | -0.566310 | +0.676525 (436) | +0.237963 (1223) | -0.438562 | -0.565045 |
| 0SDLAD | +0.370687 (909) | +0.101486 (4444) | -0.269201 | +0.370687 (909) | +0.143240 (3396) | -0.227447 | -0.268717 |

### Per market (pre)

| market | GP0 ROI (n) | GP1 ROI (n) | primary | secondary |
|---|---|---|---|---|
| ATH2 | -0.189538 (22) | -0.291626 (475) | -0.102088 | -0.216455 |
| HOU2 | -0.914156 (498) | +0.320141 (2057) | +1.234298 | +1.218711 |
| LAA2 | -0.715805 (50) | +0.113470 (1054) | +0.829275 | +1.016816 |
| SEA2 | +0.743423 (386) | +0.104382 (785) | -0.639042 | -0.627004 |
| LAD2 | +0.387997 (836) | +0.173420 (3077) | -0.214577 | -0.138942 |
| SD2 | -0.049781 (73) | -0.072395 (1367) | -0.022614 | -0.053937 |

## Robustness (pre, as frozen)

| check | primary | secondary (FL1) |
|---|---|---|
| LOGO excl. HOUATH | -0.348816 | -0.282168 |
| LOGO excl. LAASEA | +0.206348 | +0.224595 |
| LOGO excl. 0SDLAD | +0.410951 | +0.446711 |
| LOMO excl. ATH2 | +0.087029 | +0.135752 |
| LOMO excl. HOU2 | -0.383910 | -0.335166 |
| LOMO excl. LAA2 | +0.051328 | +0.069630 |
| LOMO excl. SEA2 | +0.209802 | +0.250311 |
| LOMO excl. LAD2 | +0.356432 | +0.379832 |
| LOMO excl. SD2 | +0.084540 | +0.134529 |
| one_tick_worse | +0.053497 | +0.091998 |
| first pitch +30 min (GP0 2944 / GP1 7736; 1079 rows moved) | +0.020549 | n/a (frozen as primary only) |
| fees_2x (CACHE) | +0.056829 | +0.094925 |

LOMO: 5 of 6 primaries are ≥ 0; only excluding HOU2 turns it negative. All three stresses keep the primary ≥ 0, and the +30 min shift shrinks it to +0.0205.

## Fee views (pre)

| view | primary | secondary (FL1) |
|---|---|---|
| fee-free gross | +0.055487 | +0.094565 |
| CACHE_NOT_R1P1 cache fee | +0.056158 | +0.094745 |
| CACHE fees_2x | +0.056829 | +0.094925 |

Cache basis: feebook.order_fee(round_up=True), quadratic, multiplier 0.5, from FEE_PIN 9c0f3554, applied per public print. Not fee-honest; not R1-P1.

## POST-cutoff (separate, never pooled; SDLAD only)

GP0 has 0 rows. GP1 has n 1037 (2 markets): maker gross ROI +0.005461, CACHE +0.003855. Within FL1: GP1 n 127 (SD2 only), +0.116277. Per market: LAD2 GP1 +0.000043 (n 231), SD2 GP1 +0.006221 (n 806). **The primary, secondary, LOGO, LOMO and all stresses are null after the cutoff**, because there is no post GP0 capital: every pregame print predates the 04:37:47Z cutoff. HOUATH and LAASEA have no post rows because their finalized close_time (04:30:17–04:30:20Z) is before the cutoff; SDLAD closed at 05:06:42Z.

## v1.2 common fields

| field | value | reason |
|---|---|---|
| net_pnl_without_rewards | null | No Astra orders/fills; observations are public_counterparty_realized, never Astra P&L |
| net_pnl_with_rewards | null | No Astra P&L; no rewards thesis |
| rewards_actually_earned | null | No Astra activity |
| calibration | N/A | Not probability-emitting (stub declares emits_probabilities=false) |
| fill_rate | null | No demo/shadow/live Astra fills |
| adverse_selection_after_fills | null | No real Astra fills. (The GP1−GP0 delta is itself a public-counterparty adverse-selection proxy, reported as the primary, not as this field.) |
| feasible_vs_requested_size | null | No Astra orders |
| unresolved_inventory | null | No Astra positions |
| capital_hours | null | No Astra positions; public holding periods unobservable |
| drawdown | null | No Astra P&L series |
| event_concentration | null | template uses Astra positive net P&L; none exists |
| simulated_fills | n/a (counts_toward_keep=false) | no fills modeled |
| stress_sensitivity | ROI-delta stresses above; P&L columns null | no Astra P&L |
| executable_dollars_per_day | null | not our executions |
| controls | market_only applies; no_trade and simple_model n/a | |
| Mincer-Zarnowitz / intra-game state | NOT_IN_SCOPE | 3 clusters / not on disk |
| p16 checklist | 8 satisfied / 3 n/a / 1 missing (item 12: no untouched evaluation set) | |

Descriptive concentration (pre, 3 games):
- Maker capital, both arms: HOUATH 0.320, LAASEA 0.205, SDLAD 0.475. HHI 0.3701, top-1 0.475.
- GP0 capital: SDLAD top-1 **0.5286 (>50%, flagged)**, HHI 0.3939. GP1: top-1 0.458.
- Trades: SDLAD top-1 **0.5012 (flagged)**.
- Public-counterparty maker return (not Astra P&L): HOUATH −$11,984.70, LAASEA +$48,067.65, SDLAD +$80,674.12. SDLAD's share of the positive total is **0.6266 (flagged)**.

## Multiplicity

family_size = 4. No p-values (freeze: 3 clusters). The minimum 3-game sign-test p is 0.125, which is above 0.05 and above Bonferroni 0.0125. Directional and hypothesis-generating only.

## Holdout pre-reg 9a987a77 game-phase slot (report only)

The **R2 condition is met** on both clauses: within-FL1 GP1 maker gross ROI is +0.171940 > 0, and the reading is contradicts_H1 with the within-FL1 secondary ≥ 0. R1 and R3 are not met. Fold-in needs a Conductor accept of this SCORE plus a sha-stamped amendment before any holdout outcome join. The Examiner files no amendment.

## Cross-check

The merged runner (orchestrator c6c4c0a1 = git blob 9cd5cfad at 749bc146) on real rows agrees exactly (Decimal) with the independent recompute on: arm ROIs, primary, secondary, all LOGO/LOMO values, one_tick, +30 min, per-game values, post GP1 ROI, and counts. CACHE views come from the runner only.

## Inputs (sha256)

| input | sha256 |
|---|---|
| kick | `006d7d5dc08babfb352d94cdde2460d8d49726d87d66d15d05c7cbd7acc2e90a` |
| examiner_ready_pr62 | `e6c9ac56be33af2ccc7757409b3bd918034fd2c48a438fd749827cbbd186e4e6` |
| simulator_ready | `98d0e62581ec54a3cbac60d6fb6d1cc538e765d0ea733360993b5d129082f661` |
| merge_packet | `fa361354aa284b36482b0c4a67715ff6cda63fcf70f2d0c535bd1f7bdc465d5b` |
| accept | `08d23b363d72b8c8599772ee6fc6736cb90f13e8ed814b12c59b58fd5c7dc91e` |
| freeze | `5beba803f3f6d33410409acc23ad3b782be62dc8829a0f54584e1da8ac18575a` |
| inherited_ruling | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` |
| bundle_tgz | `6576ee6cf9f023137e4357270f228dd9a5d29e3dc1d5e7ced85384681f2a7ecc` |
| band_registry | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` |
| fee_pin | `9c0f3554eedc582ed4bed940575bf7ee6c0540ce5134140c5ea19e7c458d2b6a` |
| admit1_ruling | `ac7cfe63623ca342ab5b4285ff58382a8138b58fb6cd8e95310a5d30d90304f2` |
| holdout_prereg_accept | `9a987a77e6cd6293ddaeb14fadbf33a25c1a6cc392af25f46eaaaaae33ebb273` |
| runner | `c6c4c0a13be65e51250c011cca58c22a000e0d2cc65163520a3ad719a1646521` |
| merge commit / PR head | `749bc1464764fda03dcddd1162177ef062b2ece3` / `ba1ef80b641cb625a3f39c0fc95215cb03ba3156` (same tree be477fec) |
| score_pr62.py | `4a862b2740429f596d90b9200c8b001b747b8b8a2cf4c1a9a910606ee2fb550d` |
| measure_pre_post.json | `7f412f323f943f931de3905a41e9d8ab130882028e5fd92c68d7dbd3c5736bf5` |
| independent_recompute.py | `f563856eea045678612db6eb1844fcafd33cad0f596812a32783bd04f4810f16` |
| independent_recompute.json | `1f5d28dd1221628a6ad8c51f38807840c3251fcd180fc6ff4e423a508c24b6b5` |
| rows digest | `4003bc5411901908ad81a90a0be99e513de183bf36584745ea00234724812f35` |

Lineage (cited only): PR61 KILL SCORE `2e74f17b…`, scorecard `1bdb1d9c…`, Conductor accept-KILL `be2357773ca7a842e6896676e3ba0291f40ef8e0b8f997d46f7124d4b2705229`. The PR60 stub `85cdd05c…` stays not scored.

## Anomalies

- Correction to PR61 scorecard 1bdb1d9c erratum and Conductor be235777 'erratum_noted': finalized c0003 GET close_time is 04:30:17Z (HOUATH), 04:30:19–20Z (LAASEA), 05:06:42Z (SDLAD). 2026-09-28T01:40Z is latest_expiration_time / the close_time in the earlier 'active' panel_admitted snapshot. The original PR61 JSON note ('closed 04:30Z') was right; the 04:31Z prints are post-close (excluded). No PR61 or PR62 metric changes.
- The pooled reading (contradicts_H1) is carried by one game: within-game deltas are negative in 2/3 games, and the result flips sign without HOUATH (LOGO −0.349) or without HOU2 (LOMO −0.384).
- Runner verdict_for() returns ITERATE as a constant; the Examiner applied the freeze rule, which here also yields ITERATE.
- Kick 006d7d5d stamped_at_et 19:50:00 is later than its file mtime 19:47:53 ET; MERGE fa361354 stamped 19:47:00 vs mtime 19:44:00 ET.
- Simulator READY 98d0e625 (19:47 ET) preceded the Examiner READY, inverting MERGE's stated order; the kick authorizes one-pass READY+SCORE.
- The Simulator created repo_749bc14 via a git fetch from origin (its declared deviation); the Examiner only read it. Local main refs are stale at d7558fc4, so main containment is conductor-attested only.
- CACHE fee views come only from the runner's feebook path; the independent recompute covers gross metrics only.
- No orders, no messages, no fetch. Writes: new EXAMINER_* files in P plus /workspace/tmp/examiner_scratch_pr62_score/.
