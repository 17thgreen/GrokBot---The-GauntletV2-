# Baseline Checklist — `gauntlet-v2.0-alpha`

| Field | Value |
|-------|-------|
| **Date** | 2026-09-11 |
| **Tag** | `gauntlet-v2.0-alpha` |
| **Status** | `MIRROR_COMPLETE_AWAITING_TAG` |
| **Mirror tip** | `5da5afcf9cb8f9f5316e2207d65ff52b136d850d` |
| **Canonical repo** | `17thgreen/GrokBot---The-GauntletV2-` |
| **Freeze record** | `governance/INSTITUTIONAL_LOCK_2026-09-11.md` |

## Purpose

Distinguish two learning tracks frozen at this baseline:

| Track | What we learn | Success looks like |
|-------|---------------|-------------------|
| **Market-learning** | Whether falsifiable BTC/ETH short-horizon edges survive measurement, costs, seals, cross-venue, and forward windows | Honest PASS/FAIL with cemetery when dead; capital only after chain clears |
| **Institution-learning** | Whether asymmetric authority, gated routing, evidence tags, dataset seals, and Archivist memory function as designed | Process integrity, non-waived vetoes, recoverable memory — even when alpha dies |

Gauntlet-OS remains a **future extraction** only after rules earn place under this baseline.

---

## What this baseline captures (pointers)

### Governance (operable rules)
- [x] `governance/INSTITUTIONAL_LOCK_2026-09-11.md` — full institutional freeze
- [x] `governance/DOCTRINE.md` — six lines + maxims
- [x] `governance/AUTHORITY.md` — asymmetric lattice + Conductor limits
- [x] `governance/ROUTING.md` — gated communication
- [x] `governance/EDGE_CARD.md` — universal competition unit
- [x] `governance/CONSTITUTIONAL_AMENDMENT_FORWARD_AND_CROSS_VENUE.md` — sealed holdout + forward + cross-venue
- [x] `governance/AMENDMENT_RULE.md` + `governance/templates/AMENDMENT.md` — change control (not retroactive by default)
- [x] Cycle research orders under `governance/CYCLE_*` (commission history; not rule substitutes)

### Archive (institutional memory)
- [x] `archive/SCHEMA.md`, `archive/INDEX.md`, `archive/FAILURE_CLASSES.md`
- [x] `archive/templates/` — EDGE, CEMETERY, DATASET, PRETEST_SEARCH, …
- [x] `archive/edges/`, `archive/cemetery/`, `archive/tests/` (MD + sha256 pointers), `archive/datasets/`, `archive/audit/`

### Data & seals (do not mutate under this checklist)
- [x] Registered provenance under `data/` (e.g. DATA-PROV-001, DATA-PROV-TRADES-001) — **local only; not in GitHub**
- [x] Clock audits / seal locks as filed — raw series immutable
- [x] Staged progression doctrine: OHLCV → trades → L2

### Harness & execution (measurement surface)
- [x] Examiner harness under `harness/` (outputs are evidence; do not rewrite for narrative)
- [x] Execution / verdict rubrics under `execution/`

### Out of scope for silent change
- Cycle 4 research data, Examiner harness outputs, and raw market data are **not** to be interrupted or modified to “fit” the tag.
- Material rule changes after tag → amendment, not quiet edit.

---

## Tag completion criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | GitHub mirror of this lab baseline complete on `17thgreen/GrokBot---The-GauntletV2-` | **MET** (2026-09-11; tip `5da5afcf`) |
| 2 | Annotated tag `gauntlet-v2.0-alpha` exists pointing at that freeze commit | **BLOCKED** — GitHub MCP has no create_tag; Cursor cloud agent usage exhausted |
| 3 | Human Governor confirms | **AWAITING** |

Until criterion 2+3 clear, treat `INSTITUTIONAL_LOCK_2026-09-11.md` as the binding freeze text. Status becomes `TAGGED` only after the annotated tag exists.
