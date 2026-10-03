# R2-P5 — Adverse-object field list (attach for Collector / Archivist)

**Packet:** R2-P5 (Kickoff SoT mismatch + R1-P3 adverse join)  
**Owner (schema):** Collector + Archivist (+ Clock provenance)  
**Contributor:** Deep Research (field list only — do not own schema)  
**Status:** ATTACHED 2026-09-22 ET  
**Cite:** Conductor R2 triage ADMIT; `briefs/R1-P3-ADVERSE_2026-09-22.md`; Scout kickoff SoT = Kalshi `occurrence_datetime`  
**Hard rules:** No live orders. No invented PnL. No Q6-`000` reopen. Schema owners implement; Deep Research does not admit panels.

---

## A. Kickoff / window SoT fields (process gate)

| Field | Type | Definition |
|---|---|---|
| `event_ticker` | string | Kalshi event id |
| `series_ticker` | string | e.g. `KXNFLGAME`, `KXMLBGAME` |
| `holdout_kickoff_utc` | string\|null | Schedule/holdout kickoff if any (ISO-8601) |
| `kalshi_occurrence_datetime` | string | **Source of truth** for windowing (ISO-8601) |
| `delta_kickoff_sec` | int\|null | `kalshi_occurrence_datetime − holdout_kickoff_utc` in seconds; null if no holdout |
| `window_clock_source` | enum | `kalshi_occurrence` \| `holdout_mixed` \| `unknown` — Collector must prefer `kalshi_occurrence` |
| `t_minus_7d_utc` | string | `occurrence − 7d` used for capture start |
| `panel_version` | string | Admit stamp (Archivist) |

**Refuse:** mixing holdout + occurrence clocks in one panel without labeling `window_clock_source=holdout_mixed`.

---

## B. R1-P3 demanded pre-settlement objects (when external odds path exists)

| Field | Type | Definition |
|---|---|---|
| `edge_at_quote` | float\|null | \(p_{fair}\) vs Kalshi touch at quote decision time |
| `edge_at_fill` | float\|null | Same at fill time (optional +`markout_dt_sec`) |
| `hedge_complete_flag` | bool\|null | Opposite-side hedge achieved YES+NO acquisition **< 1** after **R1-P1 fees**; null if no hedge attempt |
| `odds_age_sec` | float\|null | Age of external odds snapshot at quote (and at fill if refreshed) |
| `de_vig_method` | enum\|null | `proportional` \| `shin` \| `other` — freeze before fills; switching post-outcome = drift |
| `edge_lost_cancel` | bool\|null | Optional companion cancel reason present |

**Scorecard rule (Adversary):** without the four core channels (`edge_at_quote`, `edge_at_fill`, `hedge_complete_flag`, `odds_age_sec`), refuse Examiner-grade “edge” / paired-lock completed profit — label **measurement gap**, not strategy failure.

**Fee pin:** `hedge_complete_flag` must use **R1-P1 feebook** (not inherited Q7 literals). Until feebook Examiner tests closed, claims stay modeled under stated formula_id.

---

## C. Explicit non-owns

- Deep Research does **not** invent schema IDs, SQLite DDL, or panel admits.  
- Full Polymarket / polymm bot port remains **KILL**.  
- Do not touch Q6/Q7 arms.

## Attached-at

`2026-09-22T22:58:26+00:00` UTC · Desk 2026-09-22 ET
