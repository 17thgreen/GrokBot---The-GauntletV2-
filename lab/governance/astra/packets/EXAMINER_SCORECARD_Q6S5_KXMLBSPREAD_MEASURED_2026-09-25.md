# EXAMINER SCORECARD — Q6S5 KXMLBSPREAD MEASURED PATH 2026-09-25

**Seat:** Examiner (Kalshi) · Astra desk  
**Packet:** `Q6S5-KXMLBSPREAD-FEEQUEUE-HARNESS` · family `Q6S5-MLBSPREAD-FEEQUEUE`  
**Template:** v1.2 (`56bcf626…`)  
**Status:** SCORED  
**Verdict:** **ITERATE**  
**promote / live_promotion / counted_as_experiment_pnl:** false / false / false  
**Stamped ET:** 2026-09-25T01:37:30-04:00  
**Score packet sha256:** `db9bd220b5dd61229b6481a27d03222f36ac0ec816efa3402ef35404a0d4fb8e`

## Desk headline

Measured GET-only path READY **12/12** `honest_full_sweep` — clears INCOMPLETE_HONEST HOLD `bd34d207…`. SCORE=**ITERATE**: `results`/`pnl` null (not invented); fee **CACHE** quadratic×0.5 ≠ R1-P1; arm metrics still null. Q6-000 scoreboard unchanged.

## Clears / supersedes

| Item | Sha / note |
|---|---|
| Clears HOLD | `EXAMINER_HOLD_Q6S5_KXMLBSPREAD_MEASURED_INCOMPLETE_HONEST` `bd34d2075dc285b2bd2e2a83b15fdb85715b24389aa41e99f46b20672c8a91eb` (bytes untouched) |
| Prior READY stub (cite only) | `cb25d9a7…` PR58 harness stub ≠ measured SCORE |
| SCORE kick | `fee42dec435553bb375180a98cfa7ca48d3ca032714260f096dcc4e6817ff504` |
| Collector ACK READY | `c1d82c6e95174ddc322d35a19c63879996883b13773b56fab427dd810ac85bae` |
| Freeze | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` |
| Panel admitted | `e36de2d1…` admitted_at `2026-09-25T04:37:47Z` |

## Digests verified (PASS)

| Artifact | sha256 |
|---|---|
| READY_NOT_SCORED.json | `0617d540763d71a813672c9f9aa6766072c8461a1290c124b89e9fb3f2bf5de2` |
| STATUS.json | `dc7f22e69b06a5d90bcb5a5deb0515cd35343bed8506b5688400da5b31623f62` |
| DIGESTS.txt | `6e6898ce956b7d97e71ec675accc52fb29b73843a16b58f4620cf513e1c7d94b` |
| CAPTURE_MANIFEST.json | `2591dda5b73331f0328cf3d8a52d6021d22c5076800af27b454524d43027c6d2` |

Integrity: DIGESTS.txt entries **160/160** ok, **0** fail (before stamp). CREATE-only afterward.

## Coverage

- series 1/1 · events 6/6 · markets 12/12 · orderbooks **12/12** · gaps `[]` · `honest_full_sweep=true` · n_polls=3 · n_200=83 · n_429=8
- Active books with depth: **6/12** (10 yes_dollars / 10 no_dollars levels)
- Finalized empty books: **6/12** (honest post-settlement)
- Coverage complete ≠ arm SCORE; admit alone ≠ score

## Fee honesty label

**CACHE_NOT_R1P1** — observed GET `/series/KXMLBSPREAD` quadratic×0.5; `claim_as_live_R1P1=false`; **not** fee-honest under `astra.r1p1.feebook.claude_order_level_ceil.v1`. Lab feebook pin `22371178…` cited only. R2-P5: refuse fee-honest KEEP without formula_id pin.

## Metrics (null not invented)

| Field | Value |
|---|---|
| results | null |
| pnl | null |
| maker_vs_taker_roi_delta | null |
| fresh_vs_stale_gap | null |
| settled_join_n | null |
| n_books | **12** (observed coverage) |

## Freeze / ACCEPT clauses (quoted)

- Freeze hard rules: "`results`/`pnl` null until Examiner after Clock admit" · "No invent fills/PnL/depth/settled counts"
- Freeze fee pin: "CACHE-LABELED quadratic×0.5 (not R1-P1 live until Examiner tests `/series` pin)"
- Freeze refuse: "claim cache fee = R1-P1 live without Examiner `/series` test"
- Kick fee instruction: "Pin live `/series` fee if scoring fee honesty; do NOT promote CACHE as R1-P1"
- ACCEPT implement: "Fee remains CACHE-LABELED … do not claim R1-P1" · score after admit + measured path

## Verdict bar

| Candidate | Decision |
|---|---|
| KEEP | **REFUSED** — null results/pnl; CACHE≠R1-P1; 12/12≠score |
| KILL | **REFUSED** — honest 12/12 plumbing PASS; CACHE allowed until pin |
| **ITERATE** | **STAMPED** — plumbing PASS + HOLD cleared; fee/arm KEEP gates blocked |

## wait_for / blockers

**wait_for:** Simulator harness results on measured books (Q6S5A0/A1); Examiner live `/series` R1-P1 pin if fee-honest KEEP sought; Conductor follow-up SCORE when results land.

**blockers:** results=null · pnl=null · fee_class=CACHE_not_R1P1 · no_simulator_harness_results_on_measured_path · arm_metrics_null

## Scoreboard

**Unchanged:** Q6-000 / Arm D KEEP +$345.24 / +6.90%

## Refuse

KEEP with null PnL · invent fills/PnL · claim CACHE as R1-P1 · fee-honest without feebook pin · treat coverage/admit as KEEP · live orders · Q6-000/Cap-SR/S1 retune · edit prior HOLD/READY stub bytes
