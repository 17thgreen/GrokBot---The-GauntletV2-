# EXAMINER SCORECARD — Q6S5 KXMLBSPREAD FL-band settled-tape (PR61)

Template: EXAMINER_KALSHI_SCORECARD_TEMPLATE v1.2 (json `56bcf6269a42031d9d90496e9a65c2292321aed2165033f6fb44ff8cc4d6b1cc`). Filed 2026-10-01T19:31:19-04:00 ET. Seat: Examiner (Kalshi). Machine record: `EXAMINER_SCORE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` sha256 `2e74f17b1307b8b57f33a6475cd7ce8af48c470099478cadfb07877b0d70745f`.

## Verdict

**KILL**, scoped to the FL-band maker thesis (H1: maker_gross_roi_delta_FL0_minus_FL1 > 0) **for KXMLBSPREAD only**. It does not kill Q6S5, the parent harness, PR58/PR60, or any other series. The verdict ceiling is ITERATE, which only bars KEEP. KEEP is impossible. counts_toward_keep=false, promote=false.

Pre-declared decision rule (freeze fb6540f5, quoted verbatim):

> **Variants-proposed reading (Examiner owns the verdict):** `supports_H1` if the full-sample delta > 0 **and** ≥2 of 3 leave-one-event-out deltas > 0. `contradicts_H1` if the full-sample delta ≤ 0 **and** ≥2 of 3 LOEO deltas ≤ 0. Otherwise `inconclusive`. **Verdict ceiling ITERATE:** measurement only, no KEEP, `counts_toward_keep=false`. `contradicts_H1` supports a KILL of the FL-band maker thesis **for KXMLBSPREAD only**.

Reading: **contradicts_H1**. The full-sample pre delta is -0.104764 (≤ 0). LOEO deltas are excl. HOUATH -0.240144, excl. LAASEA +0.031111, excl. SDLAD -0.122538, so 2/3 are ≤ 0. The merged runner's reading_rule independently returned contradicts_H1. The runner's verdict_for() hard-codes ITERATE as a ceiling constant, but the Examiner owns the verdict per the freeze.

## Labels

| field | value |
|---|---|
| evidence_class | IN_SAMPLE_DEV |
| study_label | historical replay |
| label | public_counterparty_realized |
| effective n | 3 games |
| family_size | 4 |
| counts_toward_keep | false |
| promote | false |
| fee label | CACHE_NOT_R1P1 (not fee-honest, formula_id null) |
| Astra results / pnl | null (no Astra orders or fills) |

## Inputs (all sha256 verified)

| input | sha256 |
|---|---|
| Conductor SCORE kick | `0f8de7cd6b2187076e2bd8f914c4de51b3d8bfecdd59e324a41a9f030f5f26b6` |
| simulator_ready | `8e8a17566747cb29077c2f7abccb49640739ae873d3d5c20fbfa819bbde36e1b` |
| examiner_ready | `bf9aafa3363a45388aa8ebac2fffbaa0a556dba56d1cb59914119f6f78cfbffc` |
| examiner_ack_simulator_ready | `26684451a2cc11070090c06068b8e96f740fc0965616b7fa003d22d2eb897a27` |
| accept | `8e4fbac7d0426bc67c1f53fb8057a382fe46da738bd701cb970a9812a6dc2a3b` |
| addendum_in_sample_dev | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` |
| freeze | `fb6540f52ed5f819ccf6e80bf0cf7eb6d951e065416b9d550fead0c6d06043fa` |
| merge_packet | `469de2376ae413f66684df26c08656e705a7fb5a0a1d128a4270d789c841df32` |
| bundle_tgz | `63b5d981bc06f684eebb69a8ac29394534f8ae52c101f3018557544f14e29857` |
| band_registry | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` |
| fee_pin | `9c0f3554eedc582ed4bed940575bf7ee6c0540ce5134140c5ea19e7c458d2b6a` |
| admit1_ruling | `ac7cfe63623ca342ab5b4285ff58382a8138b58fb6cd8e95310a5d30d90304f2` |
| runner | `01a0bf5a3343eb5e9f12eaae9ac64120899603513bffd552f7eb4e616885f80c` |
| feebook | `eaf5aac7126efcd574c972fa77438c4118d44d50acafa17c504bdd48768bebe7` |
| merge commit | `d7558fc4b92256c68eaea66b9700021206de0a2d` |
| scoring driver score_pr61.py | `d6f52f0197b8ad63e96aa449f957d4c4a54bc69df00129d227eabd606a0bd975` |
| runner output measure_pre_post.json | `5dd5ea93d10c18636cb8530ff762afa1993feef0e73dfc3ea5e9ae9eb74f1a79` |
| independent_recompute.py | `36fd44de3916b66c6689495a1e0f28a9d37ca94d5d810ded7295be42dc934c8f` |
| independent_recompute.json | `f457107439c23c6e1d453f2c3e96ba5badb0b8f59d1693f3ba00ebeaa8aac969` |
| rows digest | `d31d2f861e0f588e31f00a51be66687ed92b6830750ebcdb977a3933fada6a7c` |

Method: I ran the merged runner (orchestrator.py 01a0bf5a, verbatim copy from the Simulator runner_tree, which equals git d7558fc4) read-only on the pinned bundle in a scratch dir, using classify_trade, then measure_rows separately on the pre and post rows. An independent recompute (no orchestrator import, own band assignment from registry 0860cbe2, no rebin) matches the runner exactly on the primary, the secondary, LOEO and post values.

Rows: 11717 included (10680 pre / 1037 post). Cutoff: created_time < 2026-09-25T04:37:47Z, strict (00:37:47 ET). Exclusions: post_close 6; block, taker_conflict, price_inconsistent, non-yes/no result and ADMIT-1 window all 0. ADMIT-1: 0 rows in the window. Data span is 2026-09-23T22:06Z to 2026-09-25T05:07Z.

## Primary / secondary (PRE only, the scored set; fee-free gross)

| arm | maker gross ROI | taker gross ROI | maker return $ | maker capital $ | contracts | n trades | markets |
|---|---|---|---|---|---|---|---|
| Q6S5FL0 | +0.039584 | -0.313475 | 5,885.71 | 148,690.26 | 167,465.95 | 1004 | 6 |
| Q6S5FL1 | +0.144347 | -0.148782 | 116,659.67 | 808,186.35 | 1,592,282.74 | 8441 | 6 |
| Q6S5FL2 | -0.283821 | +0.035874 | -5,788.32 | 20,394.27 | 181,746.93 | 1235 | 6 |

**Primary H1 delta FL0−FL1 = -0.104764** (-10.48 pp). The hypothesis was > 0, so not supported.  
**Secondary H2 delta FL2−FL1 = -0.428168**. The hypothesis was ≤ 0, which is consistent (2/3 LOEO ≤ 0).

### Per game (pre)

| game | FL0 ROI (n) | FL1 ROI (n) | FL2 ROI (n) | H1 FL0−FL1 | H2 FL2−FL1 |
|---|---|---|---|---|---|
| 26SEP242140HOUATH | +0.108577 (234) | -0.080740 (2477) | +1.341840 (341) | +0.189317 | +1.422580 |
| 26SEP242140LAASEA | -0.146439 (306) | +0.371157 (1659) | -0.468338 (310) | -0.517596 | -0.839495 |
| 26SEP242210SDLAD | +0.129673 (464) | +0.217761 (4305) | -0.919659 (584) | -0.088088 | -1.137420 |

Effect sign by game: H1 is positive in 1/3 (HOUATH) and negative in 2/3 (LAASEA, SDLAD).

### Per market (pre, maker gross ROI)

| market | FL0 | FL1 | FL2 |
|---|---|---|---|
| ATH2 | +0.114 | -0.402 | -1.000 |
| HOU2 | +0.105 | -0.027 | +1.932 |
| LAA2 | -0.328 | +0.271 | -0.295 |
| SEA2 | +0.122 | +0.461 | -1.000 |
| LAD2 | +0.119 | +0.305 | -1.000 |
| SD2 | +0.158 | -0.100 | -0.697 |

### Robustness (pre)

| check | H1 FL0−FL1 | H2 FL2−FL1 |
|---|---|---|
| LOEO excl. 26SEP242140HOUATH | -0.240144 | -1.098389 |
| LOEO excl. 26SEP242140LAASEA | +0.031111 | -0.346755 |
| LOEO excl. 26SEP242210SDLAD | -0.122538 | +0.629420 |
| LOMO excl. ATH2 | -0.139989 | -0.417811 |
| LOMO excl. HOU2 | -0.184957 | -1.062780 |
| LOMO excl. LAA2 | -0.009036 | -0.414595 |
| LOMO excl. SEA2 | -0.081848 | -0.368611 |
| LOMO excl. LAD2 | -0.053446 | +0.247417 |
| LOMO excl. SD2 | -0.149992 | -0.376277 |
| one_tick_worse | -0.094232 | -0.464659 |
| fees_2x (CACHE) | -0.098693 | -0.435857 |

All 6 LOMO H1 deltas are negative. H1 stays negative under both stresses.

Maker gross ROI by registry band (pre): b00 +0.040, b01 +0.039, b02 -0.094, b03 +0.222, b04 +0.536, b05 -0.571, b06 -0.208, b07 +1.282, b08 -0.826, b09 +1.595. These are thin and swing on single game outcomes.

## Fee views (pre)

| view | FL0 maker ROI | FL1 maker ROI | FL2 maker ROI | H1 | H2 |
|---|---|---|---|---|---|
| fee-free gross | +0.039584 | +0.144347 | -0.283821 | -0.104764 | -0.428168 |
| CACHE_NOT_R1P1 (cache fee) | +0.038595 | +0.140323 | -0.291689 | -0.101728 | -0.432013 |

CACHE fee basis: feebook.order_fee(round_up=True), multiplier 0.5, quadratic, from FEE_PIN 9c0f3554 (observed in the measured /series body), applied per public print. **Not fee-honest.** formula_id is null.

## POST-cutoff (reported separately, never pooled; SDLAD only, 1 game)

| arm | maker gross ROI | taker gross ROI | maker net ROI (CACHE) | n | markets |
|---|---|---|---|---|---|
| Q6S5FL0 | +0.094642 | -1.000000 | +0.093899 | 391 | 2 |
| Q6S5FL1 | +0.116277 | -0.132972 | +0.113234 | 127 | 1 |
| Q6S5FL2 | -1.000000 | +0.087196 | -1.008044 | 519 | 2 |

Post H1 = -0.021635, H2 = -1.116277. CACHE H1 = -0.019335. one_tick_worse: -0.012948 / -1.095738. LOEO is null (one event). The ±1 values are single-outcome artifacts.

## Common scorecard fields (v1.2)

| field | value | reason |
|---|---|---|
| net_pnl_without_rewards | null | No Astra orders/fills; observations are public counterparties' prints (public_counterparty_realized), never Astra P&L |
| net_pnl_with_rewards | null | No Astra P&L; no rewards thesis |
| rewards_actually_earned | null | No Astra activity; no rewards cash |
| calibration | N/A | Not a probability-emitting strategy (freeze: emits_probabilities=false); band ROI is the market-only calibration residual, reported under controls |
| fill_rate | null | No demo/shadow/live Astra fills exist |
| adverse_selection_after_fills | null | No real Astra fills; null per kick/template |
| feasible_vs_requested_size | null | No Astra orders; no requested size |
| unresolved_inventory | null | No Astra positions |
| capital_hours | null | No Astra positions; public counterparties' holding periods not observable |
| drawdown | null | No Astra cumulative P&L series |
| simulated_fills | n/a (label simulated, counts_toward_keep=false) | no fills modeled |
| stress_sensitivity | ROI-delta stresses above; P&L columns null | no Astra P&L |
| executable_dollars_per_day | null | not our executions; no book depth |
| controls | market_only applies (band ROI is the market-only residual); no_trade and simple_model n/a | |
| Mincer-Zarnowitz | NOT_IN_SCOPE | 3 clusters |
| preregistration p16 | 8 satisfied / 3 n/a / 1 missing (item 12: no untouched evaluation set) | |

### Event concentration (3 games)

The template's P&L-based top-1 share is **null** because there is no Astra P&L. The following are descriptive only:
- Maker-capital share: HOUATH 0.3202, LAASEA 0.2048, SDLAD 0.4750. HHI 0.3701, top-1 0.475.
- Contracts: HHI 0.3769, top-1 0.4733. Trades: HHI 0.3783, top-1 **0.5012 (>50%, flagged)**.
- Public-counterparty maker gross return (all arms, not Astra P&L): HOUATH −$11,984.70, LAASEA +$48,067.65, SDLAD +$80,674.12. Top-1 share of the positive total is **0.6266 (SDLAD, >50%, flagged)**. HHI over positive games is 0.5321.

## Multiplicity

family_size = 4. No p-values: the freeze rules out meaningful inference with 3 clusters. With 3 games, the minimum one-sided sign-test p is 0.125, which is above α = 0.05 and well above Bonferroni 0.05/4 = 0.0125. Nothing on this universe can be significant. The KILL rests on the pre-declared directional rule, not on a significance test.

## Lineage

- EXAMINER_READY_NOT_SCORED PR61 `bf9aafa3…` → ACK of the Simulator READY `26684451…` (SCORE_KICK_RECEIVED) → this SCORE.
- Parent study: trades-join SCORE `a18f2ad2…` (ITERATE 3).
- PR60: READY stub `85cdd05c…` is **not scored** per the kick.

## Anomalies and notes

- Merged runner verdict_for() hard-codes ITERATE; freeze rule maps contradicts_H1 → KILL; Examiner applied the freeze rule.
- Post-cutoff FL0 taker_gross_roi = −1 and FL2 maker_gross_roi = −1: all post rows in those arms are in SDLAD markets whose outcome made every FL0 taker lose; single-game artifact.
- Kick stamped_at_et 19:29:00 ET is later than the kick file mtime 19:27:51 ET.
- Scoring and scratch writes were authorized by the dispatcher's update after the user's original task said no scoring; flagged for the user.
- **Erratum to the machine record** (the JSON can't be overwritten): its post_separate.note says HOUATH/LAASEA "closed 04:30Z". That's wrong. Their **last pinned prints** were at 04:31:04Z and 04:31:13Z, before the 04:37:47Z cutoff. Market close_time is 2026-09-28T01:40Z. SDLAD's last print was at 05:07:00Z. The conclusion stands: all post rows are SDLAD.
- The Simulator ran from runner_tree because the box `P/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE/` subdir trips the digest gate under PARENT=/workspace. Simulator unit run1 was 15/16 for an environment path reason. There is no CONDUCTOR_KICK_SIMULATOR file on disk.
- No orders, no messages, no fetch. Writes were limited to new EXAMINER_* files in P plus the scratch dir.

## Next

Per freeze: H1 money path (band filter on Q6S5 maker leg) is not opened; any re-test needs a new freeze with an untouched post-freeze settled set (p16 item 12).
