# EXAMINER SCORECARD — Q6S5 KXMLBSPREAD MEASURED HARNESS 2026-09-25

**Seat:** Examiner (Kalshi) · Astra desk  
**Packet:** `Q6S5-KXMLBSPREAD-FEEQUEUE-HARNESS` · family `Q6S5-MLBSPREAD-FEEQUEUE`  
**Template:** v1.2 (`56bcf626…`)  
**Status:** SCORED  
**Verdict:** **ITERATE** (2nd / harness re-SCORE)  
**promote / live_promotion / counted_as_experiment_pnl:** false / false / false  
**Stamped ET:** 2026-09-25T01:48:30-04:00  
**Score packet sha256:** `348e2981d191fda5a228ef77fc578b0821bd731ae6aa38b1b8004d9d82ba3d62`

## Desk headline

Measured feequeue harness READY_NOT_SCORED — digests PASS. Re-SCORE=**ITERATE**: `maker_vs_taker_roi_delta=null` (no native `taker_*` / no fills); `fresh_vs_stale_gap=null` (content_fresh countable 29; gap≠ROI); `settled_join_n=6` observational; `n_books=12`; `results`/`pnl=null`. Fee **CACHE×0.5 / CACHE_NOT_R1P1** (FEE_PIN `9c0f3554…` formula_id absent). Q6-000 unchanged. Follow-up to prior measured SCORE `db9bd220…` (bytes untouched).

## Authority pins (verified on disk)

| Item | sha256 |
|---|---|
| RESCORE kick | `06dc4abc146802a168f13c854fe6f3a265f4e0ade69ae87ba35ede83a61cc3db` |
| ACK Simulator READY | `1811542260ff28ba28938bb1c2dbbb285d4e30e6ad3cd38e7fec08a609fd0111` |
| Simulator kick (cite) | `c799f3f2771da1b6ae56e80bbbd20b6f5b145176630d9a4bfdf523bafea32961` |
| Simulator READY | `1c84cc6b8d44ab720ffe537d6f3e9e257de12e2ca8706cc1ec96c51d127e7bb3` |
| MEASURED_RUN_RESULTS | `954d2a31cd504421e826d07ac9c73a2ef66aaebb48997b5c8ac57591952060e2` |
| MEASURED_METRICS | `d6da3f6d120e60d17d6a05956a1bbfad5301de1133f720852cb25d8dd08776e0` |
| Freeze | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| ACCEPT harness | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` |
| ACCEPT iterate | `4122d100fe27ac855d3c186a2d7e048dbe2d2da547fb25545ed67e13b8e530de` |
| FEE_PIN | `9c0f3554eedc582ed4bed940575bf7ee6c0540ce5134140c5ea19e7c458d2b6a` |
| Prior SCORE (cite) | `db9bd220b5dd61229b6481a27d03222f36ac0ec816efa3402ef35404a0d4fb8e` |
| Prior HOLD (cite) | `bd34d2075dc285b2bd2e2a83b15fdb85715b24389aa41e99f46b20672c8a91eb` |

## Metrics from disk (MEASURED_METRICS / RESULTS)

| Field | Value |
|---|---|
| maker_vs_taker_roi_delta | null |
| fresh_vs_stale_gap | null |
| settled_join_n | **6** (observational; not fills/PnL) |
| n_books | **12** |
| results | null |
| pnl | null |
| arm A1 content_fresh True | 29 rows classified |

## Fee honesty

**CACHE_NOT_R1P1** — CACHE quadratic×0.5; `fee_honest=false`; FEE_PIN confirmed `formula_id` absent. Do **not** claim `astra.r1p1.feebook.claude_order_level_ceil.v1`.

## Freeze / ACCEPT / kick clauses (quoted)

- Freeze hard rules: "No invent fills/PnL/depth/settled counts" · "`results`/`pnl` null until Examiner after Clock admit"
- Freeze fee: "CACHE-LABELED quadratic×0.5 (not R1-P1 live until Examiner tests `/series` pin)"
- Freeze arms: Q6S5A0 native `taker_*` only / Lee-Ready REFUSED; Q6S5A1 content_fresh bins; invent fills REFUSED
- Freeze refuse: "claim cache fee = R1-P1 live without Examiner `/series` test"
- No freeze fail-closed KILL when arm ROI null after honest harness (invent fills refused)
- ACCEPT harness: "Fee remains CACHE-LABELED … do not claim R1-P1"
- ACCEPT iterate: why_not_kill "CACHE allowed until live /series pin"; allocate "not_now: Refiner — measurement ITERATE not strategy-corporeal"
- Simulator kick: emit metrics "or honest nulls with reason if join impossible without invent fills"
- RESCORE kick: "ROI/gap null is honest (no fills) — do not invent"; "n_books=12 and settled_join_n=6 … not KEEP"

## Verdict bar

| Candidate | Decision |
|---|---|
| KEEP | **REFUSED** — required arm metrics null; results/pnl null; CACHE_NOT_R1P1; coverage≠KEEP |
| KILL | **REFUSED** — freeze/ACCEPT treat measurement+CACHE as open; harness honest-null allowed; not Refiner corporeal |
| **ITERATE** | **STAMPED** — harness ran; KEEP gates still blocked; wait fills/native-taker (+ optional R1-P1 pin) |

## Relation to prior ITERATE `db9bd220…`

Prior SCORE = capture-complete / harness-absent ITERATE. This packet = harness-present / arm-ROI still honest-null ITERATE. Prior bytes untouched; this re-SCORE supersedes context only.

## wait_for / blockers

**wait_for:** fills path and/or native `taker_*` for Q6S5A0 ROI; fill/PnL series for Q6S5A1 gap; optional Examiner R1-P1 formula_id pin if fee-honest KEEP sought; Conductor ACCEPT/allocate.

**blockers:** maker_vs_taker_roi_delta=null · fresh_vs_stale_gap=null · results=null · pnl=null · fee_class=CACHE_NOT_R1P1

## Scoreboard

**Unchanged:** Q6-000 / Arm D KEEP +$345.24 / +6.90%

## Calibration

N/A (`emits_probabilities=false`)

## Refuse

KEEP with null ROI/gap/PnL · invent fills/PnL · claim CACHE as R1-P1 · treat coverage/settled_join as KEEP · live orders · Q6-000/Cap-SR/S1 retune · edit prior SCORE/FEE_PIN/HOLD bytes
