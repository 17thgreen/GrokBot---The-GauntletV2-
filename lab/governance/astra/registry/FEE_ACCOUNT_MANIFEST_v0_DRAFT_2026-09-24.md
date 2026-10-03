# FEE-ACCT-MANIFEST-v0-DRAFT-20260924 — Fee / account-version manifest (DRAFT)

**Status:** `DRAFT_NOT_ADOPTED` · **Owner:** The Archivist (Registry) · **Drafted:** 2026-09-24 ~19:45 ET
**Machine-readable:** `registry/FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24.json` (sha256 listed in `packets/ARCHIVIST_STEP0_RECORD_REPAIR_2026-09-24.md`)
**Rules:** records only · no past result recomputed · missing values = null + flag · adoption needs Conductor + Examiner stamps.

## (a) July 7 2026 Kalshi fee schedule

| Item | Value | Source (quoted) | Tag |
|---|---|---|---|
| Schedule effective | 2026-07-07 | report S19: "Kalshi Fee Schedule, effective July 7, 2026. Downloaded 12-page schedule; market multipliers and fee versions matter." | [V] (PDF bytes not on disk) |
| Taker rate | `0.07` | `kalshi_feebook_lab_20260922/series_fee_table.stub.json`: `"rates": {"taker": "0.07", "maker": "0.0175"}`; also `kalshi_general_fee_table.json` `rate` | [V] R1-P1 transcription |
| Maker rate | `0.0175` | same stub | [V] |
| Standard multiplier M | `1` | stub note: "Research default only. M is 1 and maker fees are enabled." | [V] research default, not a live lookup |
| Maker multiplier default (PDF prose) | `0` | stub note: "The July 7, 2026 fee-schedule PDF prose says the maker multiplier defaults to 0. The KXNFLGAME row on that PDF lists maker and taker multipliers of 1, which this default matches." | [V] second-hand · **CONFLICT** vs stub M=1 maker-enabled |
| KXNFLGAME maker / taker multipliers | 1 / 1 | same note | [V] second-hand |
| Numeric multiplier stated in research report | **null** · `NOT_IN_SOURCE` | report L654-655 gives only "Illustrative unrounded standard-multiplier taker cost at 50c is 1.75c." ([I] consistent with 0.07 at M=1) | — |
| Other series multipliers | **null** · `NOT_ON_DISK` | stub overrides map empty on purpose | — |
| Per-contract cap | **null** · `NOT_SOURCED_TO_SCHEDULE` | stub has `0.035` disabled; unit results call it "the Claude optional flag" | — |
| Fee version ids | **null** · `NOT_ON_DISK` | — | — |

## (b) Member-type rounding precision

Report L655-657 [S20]: *"API documentation distinguishes direct-member balance precision of $0.0001 from non-direct precision of $0.01 and describes per-order rounding accumulators."*

| Member type | Precision | Tag |
|---|---|---|
| Direct member | $0.0001 | [V] report |
| Non-direct member | $0.01 | [V] report |
| **Lab account member type** | **null — UNKNOWN** | [U] |
| Account fee tier / private terms | **null — UNKNOWN** | [U] |

The feebook unit results (L33-35) say: "The July 7, 2026 fee-schedule PDF says rounding makes fee plus position cost land on a centicent. The general taker table matches ceiling the fee itself to one cent."

## (c) Harness conventions on disk and on main@34a27202

| Convention | Definition | Harnesses (paths) |
|---|---|---|
| **CONV-A order-level cent ceiling** (the "older cent-ceiling convention") | `astra.r1p1.feebook.claude_order_level_ceil.v1`: the order fee is ceiled to $0.01 (`feebook.py` `round_up_to_cent` L48-53, `order_fee` L133). `round_up_to_centicent` exists at L66 but is not the Examiner path. | feebook; rails (`rails.py` L101, L354: taker ceiled, maker unrounded comparator); capital_structure; queue_fragility; examiner fee+queue honesty; r3_p1 fee_cost; r3_p4 shape; C1 bakeoff / honesty / empty-ob; C3 bordering; C5 honesty; C2-NHL / C4-CPI / ATP / ETH / S4 FQ orchestrators; R2P3 prop ladder; R2P5 SOT-ID (asserts the formula id, L552); R3P3 FL; L2-CAT; L2-SF; S5 fill-legs; soft-blended `soft_policy.py`; cap_sr `effects_path.py`; r3_p2 `ingest.py` (1 ref). Main-only labs are at `main@34a27202:<lab>/`. |
| **CONV-B NFL replay_v2 fixed-point** | The nominal fee is ceiled to $0.000001 (`replay_v2.py` L25). Balance precision is $0.0001 (L17), with a per-order accumulator/rebate. Coefficients: maker .0175, taker .07 (L48-49). | `maker_replay_round2`, `nfl_queue`, `nfl_timing`, `nfl_completion`, `nfl_adaptive`, `nfl_factorial` (each `replay_v2.py`); `verify_results.py` in adaptive / completion / factorial / queue / timing. `nfl_paircheck` (Q7) `run_experiment.py` L11 and Q7 rehab P1 `run_tape_walk.py` L65 import `replay_v2.Config`. **Q6 / Q7 / Q7-B P1 P&L came from CONV-B.** |
| **MIXED** | `hygiene.py` `inherited_order_fee` (L147) reproduces CONV-B. `fee_delta` (L190) takes CONV-A minus CONV-B. | `kalshi_r2p1_hygiene_000_lab_20260922/hygiene.py` |
| No fee arithmetic | pin only / none | RJ settled-join labs; GET-only recorders |

**CONFLICT (report vs code):**
- The report (L657) calls the repo convention "older cent-ceiling".
- On disk, the P&L-producing NFL family uses CONV-B at $0.0001 precision. CONV-A is the Examiner measurement channel.
- Both are recorded here. Neither is edited.

## (d) `RECONCILIATION_REQUIRED`

1. CONV-A ($0.01 order ceiling) does not match the July 7 schedule, which rounds by member type ($0.0001 direct / $0.01 non-direct).
2. CONV-B matches direct-member precision only if the account is a direct member. The account's member type is unknown.
3. Maker multiplier: the stub uses M=1 with maker fees on, but the PDF prose says the maker default is 0.
4. The per-series table is not on disk.
5. The per-trade fee version for historical tapes is not recorded. The report says: "Prefer actual recorded fee components." (L659)

**No past result is recomputed.** Q6, Q7, Q7-B P1, R3-P2, AMS, NH, and all NOT_SCORED harnesses stay as recorded under their original convention. The Examiner v1.1 template keeps net P&L null "pending Archivist fee/account-version manifest". This draft does not unblock that until it is adopted.


---

## Note appended 2026-09-24T19:50:45-04:00 (ET) — Conductor instruction (status unchanged: **DRAFT_NOT_ADOPTED**)

- Until the account **member type** is resolved (**Market Scout checking**), the **Examiner reports net P&L under BOTH precisions** as a sensitivity: $0.0001 (direct-member) and $0.01 (non-direct). Neither precision is adopted as canonical by this note.
- The **Simulator is running a cost-convention stress on Q6-`000` KEEP**. It is a stress, **not a retune**. Q6-`000` stays the recorded KEEP. No past result is recomputed by this manifest. Stress outputs have not been seen by the Archivist [U].
- Sidecar: `FEE_ACCOUNT_MANIFEST_v0_DRAFT_2026-09-24_ADDENDUM_01.json`. The original JSON manifest is unchanged.
