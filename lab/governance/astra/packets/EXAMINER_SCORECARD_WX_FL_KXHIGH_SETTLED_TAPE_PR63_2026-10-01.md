# EXAMINER SCORECARD: WX-FL KXHIGH settled-tape, PR63

**Seat:** Examiner (Kalshi), Astra. **Filed:** 2026-10-01T20:49:49-04:00 (ET). **Template:** v1.2 `56bcf6269a42031d9d90496e9a65c2292321aed2165033f6fb44ff8cc4d6b1cc`.
**SCORE JSON:** `packets/EXAMINER_SCORE_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` `3ab89d3a8a9221461fb286610fc395f9b5bd49091b538011452fcc277b13015d`
**READY:** `packets/EXAMINER_READY_NOT_SCORED_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` `6ffae37a9242c0a99dad138e0948c4e771fe69842d413c761b85c8e39bf55f42`
**Merge:** f233079d9e7d2a91e2100f2085bcf85d0006e28f (local_git_object_only; main containment conductor-attested). **Kick:** `e0c5203d…`. **Freeze:** WX-FL `aec5b760…`, amended by ACCEPT `b5bd4f04…` and addendum `68e1ff7a…`.

## Verdict

| | |
|---|---|
| **Reading H1** | **inconclusive** |
| **Reading H2** | **inconclusive** |
| **Verdict** | **ITERATE** (capped for any reading by addendum 68e1ff7a; contradicts_H1 would not map to KILL; date_level_n = 1) |
| Scope | CHI/MIA/NY 2026-09-25 only: D01 = D21 = KXHIGHCHI-26SEP25, KXHIGHMIA-26SEP25, KXHIGHNY-26SEP25 (n_eff = 3, need 2) |
| Labels | IN_SAMPLE_DEV / HISTORICAL_REPLAY; public_counterparty_realized; family_size 1; effective n = 3 city-days on 1 date; counts_toward_keep **false**; promote **false** |

**Rule, verbatim (aec5b760 line 180, which is fb6540f5 line 118 with a `> ` blockquote prefix):**
> - **Variants-proposed reading (Examiner owns the verdict):** `supports_H1` if the full-sample delta > 0 **and** ≥2 of 3 leave-one-event-out deltas > 0. `contradicts_H1` if the full-sample delta ≤ 0 **and** ≥2 of 3 LOEO deltas ≤ 0. Otherwise `inconclusive`. **Verdict ceiling ITERATE:** measurement only, no KEEP, `counts_toward_keep=false`. `contradicts_H1` supports a KILL of the FL-band maker thesis **for KXMLBSPREAD only**.

**Domain substitutions (aec5b760 lines 183-189):**
1. "event" := **city-day**. "full-sample delta" := the **PRIMARY `EW_delta`** under the PRIMARY gap mapping, over all 8 city-days.
2. "≥2 of 3 LOEO" := **≥ ⌈2·n/3⌉ of the n LOCDO deltas**, where n = `n_eff`; with n = 8 this is **≥ 6 of 8**. If `n_eff < 3`, the reading is `inconclusive` (insufficient city-days).
3. KILL scope "for KXMLBSPREAD only" := **for KXHIGHCHI/LAX/MIA/NY only (this snapshot universe)**.
4. H2 reading uses the Examiner form from `2e74f17b` (`secondary.reading_H2`: "consistent with H2 (full ≤ 0; 2/3 LOEO ≤ 0)"):
   - `consistent_with_H2` if `EW_delta_FL2_minus_FL1 ≤ 0` and ≥ ⌈2n/3⌉ LOCDO ≤ 0
   - `inconsistent_with_H2` if `> 0` and ≥ ⌈2n/3⌉ LOCDO > 0
   - else `inconclusive`

**Addendum 68e1ff7a ruling 2 (verbatim):** Under the primary, n_eff = 3 (CHI25, MIA25, NY25) for H1 and H2: compute the reading per the freeze formula (>= 2 of 3). BUT all 3 units share ONE date, so date-level n = 1 and leave-one-date-out is impossible. Therefore: verdict capped at ITERATE for ANY reading; contradicts_H1 does NOT map to KILL in this run. Reading scope is CHI/MIA/NY on 2026-09-25 only (LAX and all Sep-24 carry no FL1 data). Without-Sep-25 subset: report n_eff = 0, inconclusive.

**Why inconclusive.**
- **H1:** EW = +0.0237 > 0, but only 1 of 3 LOCDO deltas are > 0. Dropping CHI gives -0.0108, dropping MIA +0.1012, dropping NY -0.0192.
- **H2:** EW = -0.2402 ≤ 0, but only 1 of 3 LOCDO deltas are ≤ 0. Dropping CHI gives +0.0718, dropping MIA -0.8960, dropping NY +0.1035.

## fb6540f5 question

**Resolved; this is not the stop case.** The kick's `freeze_sha256`, the ACCEPT and the addendum all pin the WX-FL freeze `aec5b760`; the MERGE pins the ACCEPT and the addendum. `fb6540f5` is the Q6S5 FL-band freeze (PR61). The ACCEPT pins it only as `fl_band_freeze_sha256`, the source of the H1/H2/rule text. The WX-FL freeze quotes that text at lines 178-180; each line equals the fb6540f5 line plus a `> ` prefix. I scored H1/H2 from `aec5b760` as amended.

**Erratum to my READY `6ffae37a`:** it called those lines "byte-identical". Precisely, they are identical apart from the 2-byte blockquote prefix.

## Primary: GM-COV union, city-day equal-weighted (gross, fee-free)

| City-day | maker ROI WXFL0 | WXFL1 | WXFL2 | Δ FL0−FL1 | Δ FL2−FL1 |
|---|---|---|---|---|---|
| KXHIGHCHI-26SEP25 | +0.0355 | -0.0573 | -0.9216 | +0.0928 | -0.8643 |
| KXHIGHMIA-26SEP25 | -2.5e-05 | +0.1311 | +1.2025 | -0.1311 | +1.0714 |
| KXHIGHNY-26SEP25 | +0.0373 | -0.0723 | -1.0000 | +0.1096 | -0.9277 |
| **EW mean** | | | | **+0.0237** | **-0.2402** |

## Secondary: trade-weighted (non-decisive)

| | FL0−FL1 | FL2−FL1 |
|---|---|---|
| TW (freeze definition: pooled over all city-days with rows) | -0.0114 | -0.4723 |
| TW, D-scope only (descriptive) | -0.0211 | -0.1832 |

Pooled maker ROI by arm: WXFL0 +0.0211, WXFL1 +0.0325, WXFL2 -0.4398.

**Per-city trade-weighted maker ROI** (pooled over that city's days; LAX has no WXFL1):

| City | WXFL0 | WXFL1 | WXFL2 |
|---|---|---|---|
| KXHIGHCHI | +0.0229 | -0.0573 | -0.9216 |
| KXHIGHLAX | +0.0282 | null | -1.0000 |
| KXHIGHMIA | +0.0015 | +0.1311 | +1.2025 |
| KXHIGHNY | +0.0327 | -0.0723 | -1.0000 |

## Robustness

**Leave-one-city-out** (not a verdict input). Each city has one D unit, so the EW values equal LOCDO. LOCO-LAX EW equals the full EW.

| Held out | EW FL0−FL1 | EW FL2−FL1 | TW FL0−FL1 | TW FL2−FL1 |
|---|---|---|---|---|
| KXHIGHCHI | -0.0108 | +0.0718 | -0.0306 | -0.4442 |
| KXHIGHLAX | +0.0237 | -0.2402 | -0.0214 | -0.1832 |
| KXHIGHMIA | +0.1012 | -0.8960 | +0.0957 | -0.9237 |
| KXHIGHNY | -0.0192 | +0.1035 | -0.0627 | -0.2595 |

- **Leave-one-date-out: not computable** (date_level_n = 1). Dropping 26SEP25 leaves n_eff = 0. Dropping 26SEP24 removes no D unit.
- **Without Sep-25:** n_eff D01 = D21 = 0, so both readings are inconclusive. The 26SEP24 data is 638 trades, all at p_taker = 0.01 and all losing, and WXFL0 is the only populated arm.
- **one_tick_worse (primary):** EW +0.0331 / -0.3596; TW -0.0012 / -0.5398. Readings are inconclusive / consistent_with_H2 (non-decisive).
- **fees_2x:** n/a, because there is no fee view.

## Sensitivities (non-decisive)

| Mapping | kept rows | EW FL0−FL1 | EW FL2−FL1 | TW FL0−FL1 | TW FL2−FL1 | reading H1 / H2 | one_tick_worse H1 / H2 |
|---|---|---|---|---|---|---|---|
| GM-COV union (PRIMARY) | 33757 | +0.0237 | -0.2402 | -0.0114 | -0.4723 | inconclusive / inconclusive | inconclusive / consistent_with_H2 |
| GM-COV-SINGLE | 15647 | +0.0232 | -0.3012 | +0.0208 | -0.5287 | supports_H1 / consistent_with_H2 | supports_H1 / consistent_with_H2 |
| GM-LIT (original freeze primary) | 6558 | -0.0858 | +0.0889 | -0.0096 | -0.3740 | contradicts_H1 / inconsistent_with_H2 | contradicts_H1 / inconclusive |
| GM-LIT-PAD | 135 | counts only | | | | not reported | |

The reading is mapping-dependent and fragile. KXHIGHMIA-26SEP25 is the outlier city-day in both deltas.

## Counts, universe and date_level_n (independent recompute vs runner constants)

| Item | Independent recompute | Runner constant / committed | Match |
|---|---|---|---|
| Markets / city-days | 48 / 8 (derived universe equals FROZEN 48) | 48 / 8 (hard-asserted) | yes |
| Trades created < W0 | 33,757 (26SEP24 638, 26SEP25 33,119) | TRADES_IN_SCOPE 33,757; TRADES_BY_DATE | yes |
| Row-rule exclusions | 0 in every category | 0 | yes |
| Per arm | WXFL0 11,739 / WXFL1 13,043 / WXFL2 8,975 | same | yes |
| GM-COV union dropped | 0 / 0 / 0 (windows proven/not proven: budget 966/84, 429 115/16, storm 43/182) | same | yes |
| GM-COV-SINGLE dropped | 6,581 / 6,592 / 4,937 | same | yes |
| GM-LIT dropped (per arm) | 9,330 / 10,536 / 7,333 (timestamp-only 27,199 / kept 6,558) | same (hard-asserted) | yes |
| GM-LIT-PAD kept | 95 / 32 / 8 | same | yes |
| date_level_n | 1 (from the snapshot and from committed GM_COV_COUNTS) | AUTHORITY_REPORT 1 (**hard-coded constant**); run_scope 1 (computed) | yes; flagged as hard-coded |

## Driver deviation

The Simulator's `run_pr63.py` (`a2fc190b…`) did not call `conduct()`, which extracts to a /tmp directory. Instead it called the runner's entry points in order (verify_pins_manifest → load_frame(dest=lab) → build_counts → published_scorecard → write_count_files → authority_report).

- **Verified:** all 7 `outputs/results/*.json` files are byte-identical to the `results/` files committed at f233079d.
- I also re-ran the merged runner from `git archive f233079d` into scratch. Those outputs are byte-identical too (7/7).

## Cross-check

- **Runner path:** merged runner loader, `classify_trade`, gap_mapping and pure algebra functions. Rows were **not** relabelled synthetic and no code was edited; `RealTapeRoiRefused` was respected.
- **Independent recompute:** no runner import, exact Fractions.
- **Agreement:** 746 values compared, max |diff| 1.4e-16. Readings, D sets and counts are identical.

## Labels, fees, ADMIT-1, pre_admitted_at

- **Labels:** gross, fee-free. `CACHE_NOT_R1P1`; fee_honest false. **net / maker_net_roi_cache / taker_net_roi_cache = null** because there is no KXHIGH FEE_PIN (kalshi_series_meta has 0 rows) and no GET is allowed.
- **pre_admitted_at:** null. The freeze says "admitted_at null; card02 never admitted"; there is no pre/post split.
- **ADMIT-1:** window [2026-09-27T00:00Z, 2026-09-30T04:00Z), 0 rows in it.
  - Max trade created_time is 2026-09-26T07:56:23.196542Z; max settlement_ts is 2026-09-26T14:21:36.457911Z; max first finalized receipt is 2026-09-26T18:30:52.882Z.
  - So Sep 25 is **before** the 09-27 outage gap (2026-09-27T13:31:52Z → 09-29T20:39:41Z, ruling `ac7cfe63…`).
  - **Weather/card03 relaunch context:** weather is GO_STAGED (≤5 rpm) and card03 GO_REDUCED. Post-relaunch capture would be the only untouched evaluation source; none of it is used here (p16 item 12 missing).

## Multiplicity

- family_size is 1 and p-values are null (clustered inference is not in scope).
- With n = 3, the minimum one-sided sign-test p is 0.125. The observed per-city-day sign splits are 2/3 for both H1 and H2, giving p = 0.5.
- All three units share one date, so date-level n = 1. This is directional description only.

## v1.2 common fields

| Field | Value |
|---|---|
| net_pnl_without_rewards / with_rewards / rewards_actually_earned | null: no Astra orders, fills or rewards |
| calibration | N/A: emits_probabilities = false |
| fill_rate, feasible_vs_requested_size, unresolved_inventory | null: no Astra orders |
| adverse_selection_after_fills (+60s/+300s/settlement) | null: no Astra fills |
| capital_hours, drawdown | null: no Astra positions or P&L |
| event_concentration | null (needs Astra P&L). Descriptive: maker-capital HHI by city-day 0.2929; trade HHI 0.2631 |
| simulated_fills | n/a; counts_toward_keep false |
| executable_dollars_per_day | null: not our executions |
| controls | market_only applies; no_trade and simple_model n/a |
| p16 checklist | 8 satisfied, 3 n/a, 1 missing (item 12) |

## Anomalies
- fb6540f5 wording: the kick says "verbatim from fb6540f5", but fb6540f5 is the Q6S5 FL-band freeze (PR61). The kick freeze_sha256, ACCEPT, addendum and MERGE pin the WX-FL freeze aec5b760, whose H1/H2/rule lines match fb6540f5 byte-for-byte apart from the "> " blockquote prefix. Resolved; no stop.
- The pre-registered primary mapping changed twice before any ROI was computed. The freeze named GM-LIT, with LOCDO >= ceil(2n/3) of n = n_eff (illustrated as >= 6 of 8). ACCEPT made GM-COV primary and wrote a fixed >= 6 of 8. The addendum made GM-COV union primary and restored the freeze formula (n = n_eff = 3, need 2). Under the original freeze primary (GM-LIT, same formula) the reading would be contradicts_H1 / inconsistent_with_H2; it is reported only as a non-decisive sensitivity. Clarifies READY 6ffae37a anomalies[1], which shortened the freeze rule to ">= 6 of 8".
- The reading flips with the gap mapping (inconclusive primary; supports_H1 under single-poll; contradicts_H1 under GM-LIT). Fragile and mapping-dependent.
- Runner guard: measure_synthetic/_accumulate refuse real rows (RealTapeRoiRefused). The runner-path cross-check reused runner row and gap code and pure algebra; it did not relabel rows or edit code, and summed buckets in the driver with the identical formula.
- AUTHORITY_REPORT date_level_n = 1 is a hard-coded constant; the runner universe is hard-asserted. Both independently recomputed: match.
- Freeze declared LOCO with 4 values and LODO with 2; with D = 3 city-days on one date, LOCO-LAX is trivially equal to the full EW and LODO is not computable.
- TW secondary (freeze definition) pools non-D rows (LAX25 WXFL0/WXFL2 and 26SEP24 WXFL0), so it is not restricted to the reading scope. A scope-only TW is reported as descriptive.
- Erratum to Examiner READY 6ffae37a (fb6540f5_question.resolution and anomalies[0]): it says aec5b760 lines 178-180 are byte-identical to fb6540f5 lines 116-118. Precisely, each aec5b760 line is the fb6540f5 line prefixed with the 2-byte Markdown blockquote marker "> " (310/145/429 vs 308/143/427 characters); the text is otherwise identical. The resolution is unchanged.
- Conductor stamped_at_et times are 4-5 min after file mtimes (ACCEPT, addendum, MERGE, kick). Simulator READY was filed before the Examiner READY. Recorded in READY 6ffae37a.
- The bundle vendors copies of Examiner PR61 scratch files and precheckpoint sqlite -wal/-shm (provenance only; inner MANIFEST 55/55 OK).

No orders. No messages. No fetch. results = null, pnl = null.
