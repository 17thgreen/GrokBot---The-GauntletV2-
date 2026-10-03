# CEM-ASTRA-20260924-001 — Card 09 crypto settlement-window pricing (CEMETERY_UP_FRONT)

- **CEM_ID:** CEM-ASTRA-20260924-001
- **DATE:** 2026-09-24 (ET) · filed by The Archivist (Registry) on the Adversary's up-front list
- **CARD:** Kalshi Edge Research card 09, "Crypto settlement-window pricing" (`research/KALSHI_EDGE_RESEARCH_2026-09-24.txt`)
- **FAMILY:** KXBTC15M / KXETH15M close-minute CF RTI 60s-average remainder ("locked settlement-window remainder"; F2 lineage)
- **DECISION:** **CEMETERY_UP_FRONT**. Do not build as written.
- **CLASS of killing evidence:** historical replay (Gauntlet TEST on captured CF + Kalshi data)

## Cause of death

The card is the same idea as the closed Gauntlet feature F2, `FEAT-20260912-005`. It uses the formula `required_remaining_avg = (K*60 − sum(ticks[0:k]))/(60−k)` on Kalshi 15m with the CF RTI 60s simple average.

F2 was tested in `TEST-20260913-001`, overall verdict **`REDUNDANT / FAIL-INSUFFICIENT`**: "Function is closed. No v2 map." The card's "remaining joint path distribution" is the soft remainder. `POST_KILL_ATTENTION_2026-09-13.md` lists it as **Forbidden as next**.

## Evidence (Adversary packet IDs verbatim + on-disk pins)

| Evidence ID | Path | sha256 (Archivist, 2026-09-24) |
|---|---|---|
| FEAT-20260912-005 | `/workspace/lab/archive/features/FEAT-20260912-005.md` | `dce56be7df0671dd277bcd121c923068a83f17479912c285fff82649bce3c455` |
| TEST-20260913-001 (full card) | `/workspace/lab/archive/tests/TEST-20260913-001-F2-INCREMENTAL.md` | `5aa7ac59428e422dcc546f0d2f87e42a240c61af7782da546f041bc60cb8bfb1` |
| TEST-20260913-001 (json) | `/workspace/lab/archive/tests/TEST-20260913-001-F2-INCREMENTAL.json` | `854fda959c52d2ab736aad27ecacd73074d0b60f3ece1da650ef1464d4205338` |
| TEST-20260913-001 (stub) | `/workspace/lab/archive/tests/TEST-20260913-001.md` | `2e35cfef0fd21db7e6e8a10003377ab1c658493d5ecffedfb216c9acf966f50c` |
| TEST-20260913-001 (stub json) | `/workspace/lab/archive/tests/TEST-20260913-001.json` | `6a3f03bce034edeee5299778b994ac612227381a4d89f25e99c48231589cccbd` |
| POST_KILL_ATTENTION | `/workspace/lab/governance/POST_KILL_ATTENTION_2026-09-13.md` | `b5610e9f30cb6cc71a91017168beee56f109b2402ede0b86db661222d24dee52` |
| GAUNTLET_SCIENCE_PAUSE | `/workspace/lab/governance/GAUNTLET_SCIENCE_PAUSE_2026-09-14.md` | `90b9a67812aee4a4f6ac5b3554f388550b331c58ac8f52cfa7a9e869a4e6787b` |
| Adversary packet | `lab/governance/astra/packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (card-09 row; up-front list item 1) | see PACKET_INDEX STEP0 row |
| DATA-PROV-CF-001 | cited by the Adversary and TEST card; `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md` (relative path as written in TEST card) | not re-hashed |

**Older-lab lineage:** the Conductor steering refers to "the older crypto lab/cemetery by The Archivist b31640de". A grep of `/workspace/lab/archive`, `/workspace/lab/governance` and agent-data found **no on-disk reference to `b31640de`** [U]. The Gauntlet-era archive run by The Archivist is `/workspace/lab/archive/` (README: "Alpha Lab Archive — The Archivist"), and its cemetery is `/workspace/lab/archive/cemetery/CEM-2026091*-00*`. There is no CEM file for F2 there; F2 is closed through the TEST verdict.

## Original result — stays visible, numbers unchanged

Verbatim headline row from `TEST-20260913-001-F2-INCREMENTAL.md` line 45:

`| KALSHI|15m|BTC|CLOSE-k30|mid_T-1m | 219 | 0.041096 | 0.149206 | -0.108110 | 0.378603 | 0.464352 | -0.085749 | 0.4463 | 0.4703 | 0.041096 | INCREMENTAL_RESEARCH |`

ETH headline (line 46): `REDUNDANT / FAIL-INSUFFICIENT` (ΔLogLoss +0.323900). Overall verdict (line 9): `REDUNDANT / FAIL-INSUFFICIENT`.

### FLAG: `LOOKAHEAD-CONTAMINATED` on the favourable BTC result

- **Basis** (Adversary card-09 row, verbatim): "**Timing asymmetry:** the F2 BTC "INCREMENTAL" compared k=30s-into-close model vs **T−1m** mid, so the model had newer information. That is not evidence the market ignores the window."
- **TEST card design** (lines 6 and 29): incumbent "PM-003 T−1m mid", "m_t = T−1m checkpoint mid only".
- **Flag source:** Conductor steering, 2026-09-24. The Archivist records the flag. The Archivist does **not** re-score and does **not** change the numbers above.
- **[I] scope note:** the annex rows `BTC|CLOSE-k50`, `ETH|CLOSE-k50` (lines 62-63) are also labeled `INCREMENTAL_RESEARCH` against the same `mid_T-1m` comparator. The same asymmetry applies by construction. The Conductor should confirm whether the flag extends to them. Until then they are recorded unchanged and unflagged.

## Rules

- Frozen negative stays visible. This entry and the original TEST card are never deleted or softened.
- No resurrection without a **new freeze**. A reopen also needs a Governor reopen of Gauntlet science (`GAUNTLET_SCIENCE_PAUSE_2026-09-14.md`) and a freeze that cites F2 lineage.
- Also excluded: soft remainder, k-shopping, dropping ETH, fills after trading closes, a Binance oracle, and a bacchus/kxeth15m port. These refuse binds come from the Adversary row.
- The only possible new evidence class, per the Adversary: an executable in-window book at realistic arrival on prospective windows.
- No live orders. No PnL invented.


---

## Conductor ruling — appended 2026-09-24T19:50:45-04:00 (ET)

**Ruling:** `LOOKAHEAD-CONTAMINATED` is **extended to the k=50 annex rows**. This closes the [I] scope note above. The text above is not rewritten.

- Rows flagged (verbatim from `TEST-20260913-001-F2-INCREMENTAL.md`, sha256 `5aa7ac59428e422dcc546f0d2f87e42a240c61af7782da546f041bc60cb8bfb1`, unchanged):
  - line 62: `| KALSHI|15m|BTC|CLOSE-k50|mid_T-1m | 219 | 0.009132 | 0.149206 | -0.140074 | 0.084212 | 0.464352 | -0.380141 | 0.4463 | 0.4658 | 0.009132 | INCREMENTAL_RESEARCH |`
  - line 63: `| KALSHI|15m|ETH|CLOSE-k50|mid_T-1m | 178 | 0.000000 | 0.126928 | -0.126928 | 0.000100 | 0.400601 | -0.400501 | 0.5240 | 0.5393 | 0.000000 | INCREMENTAL_RESEARCH |`
- **Basis (Conductor):** the same comparison as the headline BTC k=30 row: close-minute data vs an earlier (T−1m) mid.
- **Kept visible. Numbers unchanged.** Verdict labels stay as written in the TEST card. The flag is a registry annotation, not a re-score.
- Not flagged: lines 60–61 (`BTC|CLOSE-k10`, `ETH|CLOSE-k10`), which read `REDUNDANT / FAIL-INSUFFICIENT`.
- Flag coverage now: BTC k=30 (line 45), BTC k=50 (line 62), ETH k=50 (line 63).
- Recorded in `packets/ARCHIVIST_CONDUCTOR_RULINGS_RECORD_2026-09-24.md` (R2).
