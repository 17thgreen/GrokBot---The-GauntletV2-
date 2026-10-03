# CEM-ASTRA-20260924-003 — Card 06 CPI sub-family: post-release CPI taking (CEMETERY_UP_FRONT)

- **CEM_ID:** CEM-ASTRA-20260924-003
- **DATE:** 2026-09-24 (ET) · The Archivist (Registry)
- **CARD:** Kalshi Edge Research card 06, "Official-source interpretation". This entry covers the **CPI post-release sub-family only**. The card's company-report KPI lane stays **PROCEED_WITH_DIFFERENTIATOR** (Adversary) and is **not** killed.
- **FAMILY:** KXCPI / KXCPIYOY. Buying after reading the scheduled BLS CPI release.
- **DECISION:** **CEMETERY_UP_FRONT (CPI sub-family)**. Per the Adversary, any other family whose market closes before its source arrives joins this list automatically.
- **CLASS of killing evidence:** historical replay (captured contract rules and close/settle times) [I] · CLASS_FIT_POOR, because this is a structural timing fact rather than a strategy run.

## Cause of death

The market closes before the source is published, so there is no post-release trading window.

**Kalshi close 8:25 AM ET, on disk [V]:**
- `packets/C4_KXCPI_PANEL_STUB_2026-09-23.json` (sha256 `b20b0cbee50c127d2e9bb2548b574b7d643cc708f54019d53bd91775f9762c13`), `rules_secondary`: "The market will always close at 8:25 AM ET on the scheduled day of the data release (November 10, 2026)."
- The same stub's `close_time` values are `2026-10-14T12:25:00Z` (08:25 EDT) and `2026-11-10T13:25:00Z`, `2026-12-10T13:25:00Z`, `2027-01-13T13:25:00Z` (08:25 EST).
- Settled example: `packets/scout_c4_settled_rejoin_2026-09-24/raw/event_KXCPI_26JUL.json` (sha256 `2bf1666cebede759434b61f486b512e0707a243c81e5cd437bf9f2ea60437b58`). It shows `close_time` `2026-08-12T12:25:00Z` = **08:25 ET** and `settlement_ts` `2026-08-12T12:56:49.124857Z` = 08:56:49 ET.

**KXCPIYOY close 8:29 AM ET, git object [V]:**
- `AMS:threshold_screen/RESULTS.md` (blob `fc476d21761baa2c14ad2850d8e45d5a53012c17` @ `cba057e62b3162bbf5cab17f4e2fee532a209ddc`), lines 37-38: "close trading at 8:29 AM ET on the scheduled release date. An ordinary strategy that reads the scheduled CPI release and then buys this contract has no post-release …"
- `AMS:triage/DECISIONS.md` (blob `c7faade28ccd0bfd38e2df47f59a063338ccf3c4`), line 11: "CPI post-release taking is excluded for the tested contract because trading closes first."

**Research report:** `research/KALSHI_EDGE_RESEARCH_2026-09-24.txt` line 437: "CPI contract closes before the release. That blocks the simple post-release CPI-sniping story." The report does not state the 8:25 or 8:30 clock times.

## Registry fact: BLS CPI release time (pinned 2026-09-24)

The Adversary packet noted: "the 8:30 ET BLS release time is not written in any lab file." It is pinned here from the official BLS schedule.

| Field | Value |
|---|---|
| URL 1 | https://www.bls.gov/schedule/news_release/cpi.htm |
| Fetch | WebFetch tool, ~19:39 ET 2026-09-24. The tool may return cached content. A direct `curl` at 2026-09-24T19:40:07-04:00 returned HTTP 403 (BLS blocks non-browser clients), so there are no raw bytes to hash. |
| Quoted text (verbatim rows) | "July 2026 \| Aug. 12, 2026 \| 08:30 AM" · "August 2026 \| Sep. 11, 2026 \| 08:30 AM" · "September 2026 \| Oct. 14, 2026 \| 08:30 AM" · "October 2026 \| Nov. 10, 2026 \| 08:30 AM" · "November 2026 \| Dec. 10, 2026 \| 08:30 AM" (table header "Reference Month \| Release Date \| Release Time") |
| URL 2 (time-zone basis) | https://www.bls.gov/schedule/2026/10_sched.htm (WebFetch, ~19:40 ET) |
| Quoted text | "14 Consumer Price Index September 2026 08:30 AM" and "NOTE: All times on calendar are Eastern Time." (page "Last Modified Date: February 18, 2026") |
| Registry fact | **BLS CPI release time = 08:30 AM Eastern Time** on scheduled release dates [V official BLS page via WebFetch; raw-byte hash UNAVAILABLE] |

**Cross-check [V dates line up]:**
- The Kalshi C4 stub rules name November 10, 2026 as a release day. BLS lists Nov. 10, 2026 08:30 AM.
- The KXCPI-26JUL close on 2026-08-12 at 08:25 ET falls on BLS "Aug. 12, 2026 | 08:30 AM".
- On both days the close comes before the release by the stated clock times. No new number is derived.

## Evidence IDs (Adversary packet, verbatim)

- Flag row "06 vs CPI closing before release".
- Up-front list item 3.
- Card-06 row.
- Source packet: `lab/governance/astra/packets/ADVERSARY_DEAD_CARD_OVERLAP_EDGE_RESEARCH_2026-09-24.md`
- Related closed harness (NOT_SCORED; not a kill): `packets/C4_KXCPI_FEEQUEUE_HARNESS_FREEZE_2026-09-23.md` (sha256 `949b255859196f02d73303a1019e51276c583f8d1e3ffb4f0a64d330467c6f93`)

## Rules

- Frozen negative stays visible. Never delete or soften this entry.
- No resurrection without a **new freeze** that proves, per contract, that the source arrives before the market closes.
- Data published after the market closes can never be traded (lookahead).
- Do not invent `occurrence_datetime`/SoT (CPI-FQ bind).
- No live orders. No PnL invented.
