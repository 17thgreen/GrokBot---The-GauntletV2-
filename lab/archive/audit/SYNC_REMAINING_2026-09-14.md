# SYNC_REMAINING — 2026-09-14

Inventory only. No bodies invented. Remote = `origin/main` @ `f62bb11ea9d644968a954374640484c685fc423f`.
This environment has a partial `lab/` tree; authoritative Python / long markdown were not copied.

Method: GitHub + `git ls-tree` of `lab/harness/examiner/src`, `lab/archive/{features,tests,datasets,league}`, `lab/governance` (incl. `drafts/`, `proposals/`). Cited paths come from on-disk tests/README/orders, not guessed modules.

---

## 1) `lab/harness/examiner/src/*.py`

### Present on remote (do not redo)

| Path | bytes | blob |
|------|------:|------|
| `lab/harness/examiner/src/__init__.py` | 162 | `73822ad8` |
| `lab/harness/examiner/src/costs.py` | 1409 | `88530c7a` |
| `lab/harness/examiner/src/signal_edge001.py` | 3670 | `97c25efb` |
| `lab/harness/examiner/src/signal_edge_20260911_006.py` | 3573 | `5bd44b4a` |

Remote `src/` has **only these four files**. No other `*.py` exists on `origin/main`.

### Still missing (SAFE; cited; not inventable)

Count: **22**

| Path | Cited by |
|------|----------|
| `lab/harness/examiner/src/run_edge001.py` | README; `test_untested_without_data.py` |
| `lab/harness/examiner/src/run_edge003.py` | README; `test_edge003_primary_and_sealed.py` |
| `lab/harness/examiner/src/run_edge004.py` | `test_edge004_primary_and_sealed.py` |
| `lab/harness/examiner/src/run_edge_20260911_004.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/run_edge_20260911_005.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/run_edge_20260911_006.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/signal_edge003.py` | README; `test_signal_edge003_no_lookahead.py` |
| `lab/harness/examiner/src/signal_edge004.py` | `test_signal_edge004_no_lookahead.py`; `test_edge004_primary_and_sealed.py` |
| `lab/harness/examiner/src/signal_edge_20260911_001.py` | `test_trades_edges_no_lookahead.py` |
| `lab/harness/examiner/src/signal_edge_20260911_004.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/signal_edge_20260911_005.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/data_loader.py` | `test_edge003_*`; `test_edge004_*`; `test_sealed_never_opened.py` |
| `lab/harness/examiner/src/trades_loader.py` | `test_trades_edges_no_lookahead.py`; `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/funding_loader.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/oi_loader.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/catalyst_common.py` | `test_catalyst_c5_guards.py` |
| `lab/harness/examiner/src/splits.py` | `test_splits_frozen.py`; `test_sealed_never_opened.py` |
| `lab/harness/examiner/src/verdict.py` | `test_verdict_gates.py` |
| `lab/harness/examiner/src/verdict_edge004.py` | `test_edge004_primary_and_sealed.py` |
| `lab/harness/examiner/src/pm002_market_baseline.py` | `test_pm002_market_baseline.py`; `BINARY_EXAMINER_SPEC.md`; AMD-006 |
| `lab/harness/examiner/src/pm003_market_baseline.py` | `TEST-20260912-002-F1-INCREMENTAL.md` |
| `lab/harness/examiner/src/run_pm003_market_baseline.py` | `TEST-20260912-001-F3-INCREMENTAL.md` |

---

## 2) Archive FEAT / DRAFT / TEST / datasets / league

### Named items already on remote (do not redo unless noted)

| Path | bytes | note |
|------|------:|------|
| `lab/archive/features/DRAFT-ABST-20260914-008-F4-wick.md` | 6871 | full; tip commit `f62bb11` |
| `lab/archive/features/FEAT-20260914-008.md` | 7863 | full (earlier placeholder `099f2a7` overwritten) |
| `lab/archive/datasets/DATA-PROV-TRADES-001.md` | 1743 | present; not a PLACEHOLDER stub |
| `lab/archive/league/STRATEGY_LEAGUE.md` | 3041 | present; not a PLACEHOLDER stub |

### Still missing FEAT cards (referenced; no file)

Count: **6**

- `lab/archive/features/FEAT-20260912-002.md`
- `lab/archive/features/FEAT-20260912-003.md`
- `lab/archive/features/FEAT-20260912-004.md`
- `lab/archive/features/FEAT-20260912-006.md`
- `lab/archive/features/FEAT-20260913-001.md` (DRAFT-FEAT-001 points here)
- `lab/archive/features/FEAT-20260913-004.md`

### Still missing TEST incrementals / cards (referenced; no file)

Count: **8** md (plus cited json siblings; json not fetched — skip if >100KB)

- `lab/archive/tests/TEST-20260913-003-W2E-INCREMENTAL.md` (pointer `TEST-20260913-003.md` → this)
- `lab/archive/tests/TEST-20260913-005-CBVEL-INCREMENTAL.md` (pointer `TEST-20260913-005.md` → this)
- `lab/archive/tests/TEST-20260913-006-W2D-IVRV-INCREMENTAL.md` (pointer `TEST-20260913-006.md` → this)
- `lab/archive/tests/TEST-20260913-007.md`
- `lab/archive/tests/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.md` (`FEAT-20260913-007.md` artifacts)
- `lab/archive/tests/TEST-20260914-001.md`
- `lab/archive/tests/TEST-20260914-001-F4-WICK-INCREMENTAL.md` (**named still-needed**)
- `lab/archive/tests/TEST-20260911-001.md` (id referenced; no card)

Cited json (absent; do not invent; do not commit if >100KB):

- `lab/archive/tests/TEST-20260913-003-W2E-INCREMENTAL.json`
- `lab/archive/tests/TEST-20260913-005-CBVEL-INCREMENTAL.json`
- `lab/archive/tests/TEST-20260913-006-W2D-IVRV-INCREMENTAL.json`
- `lab/archive/tests/TEST-20260913-007-W2B-LAST-AT-L-INCREMENTAL.json`
- `lab/archive/tests/TEST-20260914-001-F4-WICK-INCREMENTAL.json`

### Placeholder / short stubs on remote (note; do not invent replacements)

**Literal PLACEHOLDER token**

| Path | bytes | text |
|------|------:|------|
| `lab/archive/tests/TEST-20260913-002-W2C-INCREMENTAL.md` | 26 | `PLACEHOLDER_LOAD_FROM_FILE` only |
| `lab/archive/INDEX.md` | 453 | headline then `PLACEHOLDER_FULL_CONTENT_FROM_FILE` |

**Short SUPERSEDED DRAFT-FEAT pointers** (not `PLACEHOLDER` token; body is a 4–6 line promote note)

| Path | bytes |
|------|------:|
| `lab/archive/features/DRAFT-FEAT-20260913-001-W2C-sibling-mid.md` | 227 |
| `lab/archive/features/DRAFT-FEAT-20260913-002-W2E-strike-vs-mid.md` | 250 |
| `lab/archive/features/DRAFT-FEAT-20260913-003-W2A-cf-mid-basis.md` | 268 |
| `lab/archive/features/DRAFT-FEAT-20260913-005-CBVEL.md` | 255 |
| `lab/archive/features/DRAFT-FEAT-20260913-006-W2D-iv-rv.md` | 257 |
| `lab/archive/features/DRAFT-FEAT-20260914-008-F4-wick.md` | 273 |

**Short TEST pointer stubs** (verdict + `Full:` path; not PLACEHOLDER)

| Path | bytes | Full: target missing? |
|------|------:|------------------------|
| `lab/archive/tests/TEST-20260911-003.md` | 61 | no (EDGE-005 card present) |
| `lab/archive/tests/TEST-20260911-004.md` | 61 | no (EDGE-004 card present) |
| `lab/archive/tests/TEST-20260911-005.md` | 74 | no (EDGE-006 card present) |
| `lab/archive/tests/TEST-20260911-006.md` | 185 | no (PM002 card present) |
| `lab/archive/tests/TEST-20260911-007.md` | 185 | no (PM003 card present) |
| `lab/archive/tests/TEST-20260912-001.md` | 226 | no (F3 incremental present) |
| `lab/archive/tests/TEST-20260912-002.md` | 278 | no (F1 incremental present) |
| `lab/archive/tests/TEST-20260913-001.md` | 153 | no (F2 incremental present) |
| `lab/archive/tests/TEST-20260913-002.md` | 155 | **yes** — target is PLACEHOLDER |
| `lab/archive/tests/TEST-20260913-003.md` | 311 | **yes** — W2E incremental absent |
| `lab/archive/tests/TEST-20260913-004.md` | 331 | no (W2A incremental present) |
| `lab/archive/tests/TEST-20260913-005.md` | 307 | **yes** — CBVEL incremental absent |
| `lab/archive/tests/TEST-20260913-006.md` | 338 | **yes** — W2D incremental absent |

`TEST-20260911-002.md` pointer absent; `TEST-20260911-002-EDGE-20260911-002.md` (2450) is present.

On-remote FEAT-20260913-002/003/006/007 are short cards (~1.1–1.6KB) with verdict tables — not `PLACEHOLDER` only.

---

## 3) Governance (named bucket)

### Still missing (no matching path on remote)

Count: **8** (5 named stems + 3 drafts CHARTER/MEMO)

| Expected SAFE path | Evidence |
|--------------------|----------|
| `lab/governance/LIQ_VENDOR_RECON.md` (or `LIQ_VENDOR_RECON_*.md`) | stem not in tree; no hits |
| `lab/governance/DATA_PROV_CATALYST_SOURCES_2026-09-11.md` | cited by `CYCLE_5_EXECUTION_ORDER`, `DATA-PROV-FUNDING-001`, `DATA-PROV-OI-001`, `US_LAWFUL_VENUE_CONSTRAINT` |
| `lab/governance/GROK_POINTER_FETCH.md` (or `GROK_POINTER_FETCH_*.md`) | stem not in tree; no hits |
| `lab/governance/GITHUB_BOOK_HUNT.md` (or `GITHUB_BOOK_HUNT_*.md`) | stem not in tree; `CONDUCTOR_MO_GITHUB_DATA_HUNT_2026-09-13.md` is a different file |
| `lab/governance/FOLLOW_VS_FADE_NEEDS_DATA.md` (or `FOLLOW_VS_FADE_NEEDS_DATA_*.md`) | stem not in tree; `JOIN_SPEC_FOLLOW_VS_FADE_2026-09-14.md` is a different file |
| `lab/governance/drafts/CHARTER_INTAKE_AUDITOR.md` | `drafts/` has only `CHARTER_REFINER.md` |
| `lab/governance/drafts/MEMO_CONSTITUTION_AMENDMENTS_2026-09-13.md` | absent under `drafts/` |
| `lab/governance/drafts/MEMO_FLEET_RECOMMENDED_CHANGES_2026-09-13.md` | absent under `drafts/` |

### Present (named / sha-diff)

| Path | bytes | blob | note |
|------|------:|------|------|
| `lab/governance/BINARY_EXAMINER_SPEC.md` | 11998 | `8e03a7cf054e6e2367122aa60446b585fb72b864` | local HEAD (pre-ff) == `origin/main`. **No second authoritative tree in this environment to sha-diff against.** History includes `affe5ec` / `a9bfeeb` “byte-exact” fixes. Deferred: off-repo sha-diff. |
| `lab/governance/POST_KILL_ATTENTION_2026-09-13.md` | 5042 | `b17ed148` | present; `POST_KILL.md` basename absent |
| `lab/governance/PREDICTION_MARKET_MISSION_2026-09-11.md` | 19280 | `25e0c01a` | present |
| `lab/governance/CHARTER_INTAKE_AUDITOR.md` | 5950 | `bbef8fe6` | root seat (not drafts/) |
| `lab/governance/CHARTER_REFINER.md` | 4677 | `01a26e5b` | same blob as `drafts/CHARTER_REFINER.md` |
| `lab/governance/drafts/CHARTER_REFINER.md` | 4677 | `01a26e5b` | present |
| `lab/governance/proposals/2026-09-13/CHARTER_INTAKE_AUDITOR.md` | 4417 | `88defcb2` | **≠** root charter sha |
| `lab/governance/proposals/2026-09-13/CHARTER_REFINER.md` | 3736 | `30aa8601` | **≠** root/drafts sha |
| `lab/governance/proposals/2026-09-13/MEMO_CONSTITUTION_AMENDMENTS_2026-09-13.md` | 13578 | `97ba7eb1` | present |
| `lab/governance/proposals/2026-09-13/MEMO_FLEET_RECOMMENDED_CHANGES_2026-09-13.md` | 11572 | `bbf49977` | present |
| `lab/governance/proposals/2026-09-13/README.md` | 1291 | `616e1168` | present |

---

## Deferred categories / counts

| Category | Missing | Present-on-remote (this bucket) | Placeholder / short stub notes |
|----------|--------:|--------------------------------:|--------------------------------|
| Examiner `src/*.py` (excl. 4 already synced) | **22** | 4 | none |
| FEAT cards | **6** | 8 FEAT files | 0 PLACEHOLDER |
| DRAFT-ABST F4 | **0** | 1 | — |
| DRAFT-FEAT short SUPERSEDED | 0 (files exist) | 6 short + 3 long | 6 short promote notes |
| TEST incrementals / missing cards | **8** md | many pointers + some full cards | 1 literal PLACEHOLDER (`TEST-20260913-002-W2C-INCREMENTAL.md`); 4 pointers whose Full: target is missing |
| TEST json incrementals | **5** cited-absent | skip if >100KB | not inventoried by size |
| DATA-PROV-TRADES-001 / STRATEGY_LEAGUE | **0** | 2 | not placeholders |
| Governance named stems | **5** | BINARY_EXAMINER / POST_KILL / PREDICTION_MARKET present | BINARY_EXAMINER sha-diff **deferred** (no 2nd tree) |
| drafts CHARTER/MEMO | **3** | 1 (`drafts/CHARTER_REFINER.md`) | — |
| proposals CHARTER/MEMO | **0** | 4 + README | proposal charters sha-differ from stamped root |

**Still-missing SAFE paths total (authoritative-body required): 22 + 6 + 8 + 5 + 3 = 44**  
(+ 5 TEST json cited-absent, gated by 100KB rule)

Do not invent the 22 examiner modules or the long markdown cards. Next sync must copy from an authoritative lab tree.
