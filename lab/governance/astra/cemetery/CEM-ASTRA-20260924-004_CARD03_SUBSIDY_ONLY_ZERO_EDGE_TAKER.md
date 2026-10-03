# CEM-ASTRA-20260924-004 — Card 03 variant: volume subsidy as the only reason for a zero-edge taker trade (CEMETERY_UP_FRONT)

- **CEM_ID:** CEM-ASTRA-20260924-004
- **DATE:** 2026-09-24 (ET) · The Archivist (Registry)
- **CARD:** Kalshi Edge Research card 03, "Selective liquidity rewards". This entry covers the **subsidy-only zero-edge taker variant only**. Per the Adversary, the card-03 resting-liquidity lane stays open (PROCEED_WITH_DIFFERENTIATOR).
- **FAMILY:** ordinary middle-price taker trades justified only by the public event-volume reward
- **DECISION:** **CEMETERY_UP_FRONT (variant)**
- **CLASS of killing evidence:** historical replay (AMS-003 triage cost bound over captured reward catalog + fee data) [I]

## Cause of death

`AMS:triage/DECISIONS.md` line 8 (blob `c7faade28ccd0bfd38e2df47f59a063338ccf3c4` @ `cba057e62b3162bbf5cab17f4e2fee532a209ddc`), verbatim:

> "| Volume subsidy as sole reason for a zero-edge taker trade | Reject the ordinary middle-price version | Standard M=1 unrounded taker fee exceeds the maximum public event-volume reward between about 7.74 and 92.26 cents. This is a cost bound, not a universal rejection of volume rewards. |"

Supporting evidence, `AMS:wide_threshold/RESULTS.md` (blob `7307bc01c610ff3179c75e934e239b9b8a330309`): "The active public event-volume catalog returned 0 programs with no remaining cursor. We could not establish an applicable volume subsidy to offset these costs."

## Evidence IDs + pins

| Evidence ID | Path | git object / sha256 |
|---|---|---|
| AMS-003 decisions | `all_market_structure_20260924/triage/DECISIONS.md` @ `cba057e62b3162bbf5cab17f4e2fee532a209ddc` | blob `c7faade28ccd0bfd38e2df47f59a063338ccf3c4` (identical at report pin `a59c9e33…`; triage tree `50896d0e42c3bf77b50e14003c4975bcb5a14c81` at both) |
| AMS-003 freeze | `…/triage/FREEZE.json` | blob `4d9a11769c61b67ca4822a73a6e38533dc730341` |
| AMS reward census (context; lane stays open) | `…/reward_census/RESULTS.md` | blob `c56e2ed3739c335df36154123a6ed485060af589` |
| AMS-012 capacity (context) | `…/reward_capacity/RESULTS.md` | blob `49c3e115615e817a2ce8f74c1c0b524b4510dfb1` |
| Adversary packet | `lab/governance/astra/packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (up-front list item 4; card-03 row) | sha256 in PACKET_INDEX |

**Fee caveat:** the cost bound uses the "Standard M=1 unrounded taker fee". Under the draft `FEE-ACCT-MANIFEST-v0-DRAFT-20260924`, member-type rounding and account fee tier are **UNKNOWN**. The bound is not recomputed here, and this entry does not depend on any recomputation.

## Rules

- Frozen negative stays visible. Never delete or soften this entry.
- No resurrection without a **new freeze**.
- Count `rewards_actually_earned` only (Examiner template).
- A no-reward P&L control is mandatory for any card-03 study.
- No live orders. No PnL invented.
