# CEM-ASTRA-20260924-002 — Card 10 core: static rule-implied threshold-basket taker (CEMETERY_UP_FRONT)

- **CEM_ID:** CEM-ASTRA-20260924-002
- **DATE:** 2026-09-24 (ET) · The Archivist (Registry)
- **CARD:** Kalshi Edge Research card 10, "Rule-proven event baskets". This entry covers the **core** static threshold-basket **taker** only. Deadline-nesting / complete-set sub-variants and patient maker completion stay in the backlog and are **not** killed here.
- **FAMILY:** same-event / rule-implied threshold pairs (YES(B)+NO(A) payoff floor), taker execution
- **DECISION:** **CEMETERY_UP_FRONT (core)**
- **CLASS of killing evidence:** historical replay (retained snapshot scans of captured venue data) [I]

## Cause of death

This lane has been parked twice, with no positive net case either time:

- **AMS-002** (`threshold_screen/RESULTS.md`): "180 cases had sufficient displayed depth for both legs. Every one cost more than the conditional $1 normal-resolution payoff floor before fees." Triage `DECISIONS.md` line 7: "Static same-event threshold arbitrage | Park".
- **AMS-008** (`wide_threshold/RESULTS.md`): "32270 depth-complete cases … Five cases across two pairs had positive gross floor margins. None survived the ordinary M=1 unrounded taker-fee benchmark." Also: "Decision: keep the static taker threshold lane parked. … do not continue scanning the same retained data for a desired answer."

## Evidence pin: git objects only (not checked-out files)

- **Repo:** `/workspace/lab/astra-science` (local git clone; read-only `git cat-file` / `git ls-tree` / `git show`; nothing checked out or modified).
- **Commit** `cba057e6` resolves to **`cba057e62b3162bbf5cab17f4e2fee532a209ddc`**:
  - tree `6ae584e68a80e42b3c2ccd0e64b24c7410457a83`
  - parent `6b8e3604253e2f29e5b0c558d3de6eece29ff21d`
  - message "Report original gap strategy windows, capacity and $5,000 sensitivity"
  - This is the GitHub head of `research/all-market-structure-20260924` (list_branches, 2026-09-24 19:38 ET). It is not a local remote-tracking ref in this clone.
- **Report pin** `a59c9e33` resolves to `a59c9e331dcfcd71c957e753bc4fd2460df403c0`, an ancestor 25 commits behind:
  - `threshold_screen/` and `triage/` blob SHAs are identical at both commits [V ls-tree].
  - **`wide_threshold/` (AMS-008) does not exist at a59c9e33** [V]. The AMS-008 evidence is therefore not covered by the report's pin.

Paths below are relative to `all_market_structure_20260924/`.

| Evidence ID | Path | Object | git object SHA |
|---|---|---|---|
| AMS dir @cba057e6 | `all_market_structure_20260924/` | (in root tree) | see sub-trees |
| AMS-002 tree | `threshold_screen/` | tree | `a277e9d1244c1e7b2ed82174442517c98a21ca29` |
| AMS-002 results | `threshold_screen/RESULTS.md` | blob | `fc476d21761baa2c14ad2850d8e45d5a53012c17` |
| AMS-002 freeze | `threshold_screen/FREEZE.json` | blob | `c887686e61b00bc7594fe67fd78fe2956504f954` |
| AMS-002 summary | `threshold_screen/SUMMARY.json` | blob | `fc178baaa9b17123749a03f248aed2f71073841d` |
| AMS-002 evidence hashes | `threshold_screen/EVIDENCE_HASHES.json` | blob | `8aa68ca48a11d47b0142b33b97a01a6981dce434` |
| AMS-002 evidence zip | `threshold_screen/AMS_002_Evidence.zip` | blob | `9018414fa21fda4e691855791c778c92b5738dc8` |
| AMS-003 triage tree | `triage/` | tree | `50896d0e42c3bf77b50e14003c4975bcb5a14c81` |
| AMS-003 decisions | `triage/DECISIONS.md` | blob | `c7faade28ccd0bfd38e2df47f59a063338ccf3c4` |
| AMS-003 freeze | `triage/FREEZE.json` | blob | `4d9a11769c61b67ca4822a73a6e38533dc730341` |
| AMS-008 tree | `wide_threshold/` | tree | `397da0599dd656cb6be863e52f5f8479d69034ae` |
| AMS-008 results | `wide_threshold/RESULTS.md` | blob | `7307bc01c610ff3179c75e934e239b9b8a330309` |
| AMS-008 results json | `wide_threshold/RESULTS.json` | blob | `794584b09c9e3949eb5a7f2ed33af965f5c3f5bf` |
| AMS-008 freeze | `wide_threshold/FREEZE.json` | blob | `2cac328b6759b210d41f6bd7b907554d7cf866ff` |
| AMS-008 follow-up freeze | `wide_threshold/FOLLOWUP_FREEZE.json` | blob | `c02345e560c3a723dcbd404c9308ac929bd8a7bc` |
| AMS-008 follow-up results | `wide_threshold/FOLLOWUP_RESULTS.json` | blob | `d584bff7ee5c3c59e04c7806925bfc1c59f99803` |
| AMS-008 evidence hashes | `wide_threshold/EVIDENCE_HASHES.json` | blob | `4556808626837e2ce1962fcd80d8a5a76e55c5d8` |
| AMS-008 evidence zip | `wide_threshold/AMS_008_Evidence.zip` | blob | `3b3e4b0c0e18772049c0fa8fbb84f0c93b95c7bd` |
| Adversary packet | `lab/governance/astra/packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md` (flag "10 vs AMS static scan 0/180"; up-front item 2; card-10 row) | file | sha256 in PACKET_INDEX |

The retrieval form is the one the Adversary gives, `AMS:<path>`, which expands to `git -C /workspace/lab/astra-science show cba057e6:all_market_structure_20260924/<path>`.

**Note on the research-branch freeze:** the AMS freezes are branch-internal (`FREEZE.json` blobs above). They are not Archivist freeze packets. The Archivist indexes them here as **negative** evidence only; no positive result is indexed.

## Rules

- Frozen negative stays visible. Never delete or soften this entry.
- No resurrection without a **new freeze** that carries its own rule-equivalence/payoff proof per pair.
- No re-scan of the same retained data.
- Non-atomic fills and unmatched legs must be booked.
- The fee must carry the R1-P1 pin (Adversary binds).
- No live orders. No PnL invented.
