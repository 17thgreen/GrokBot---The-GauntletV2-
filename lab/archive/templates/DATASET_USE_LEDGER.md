# DATASET_USE_LEDGER (template)

**Purpose:** Append-only record of which dataset slices were opened, by whom, for what purpose, and under which role flags (research / validation / holdout / forward).  
**Active instance:** `archive/datasets/DATASET_USE_LEDGER.md`  
**Authority:** Archivist maintains rows; Clock / Conductor / Governor may require entries before slice open.

---

## Schema (one row per open / use event)

| Column | Meaning |
|--------|---------|
| `DATA_ID` | Registered dataset ID (e.g. `DATA-PROV-FUNDING-001`) |
| `SLICE_ID` | Named slice / partition within that dataset (e.g. `research`, `validation`, `holdout`, `forward`, or explicit calendar ID) |
| `START` | Slice window start (UTC) |
| `END` | Slice window end (UTC) |
| `USED_BY` | Agent / role / EDGE / TEST that consumed the slice |
| `PURPOSE` | Brief stated purpose (hypothesis tuning, RESEARCH TEST, seal check, Clock audit, etc.) |
| `RESEARCH?` | `Y` / `N` — opened as research / exploratory |
| `VALIDATION?` | `Y` / `N` — claimed as sealed validation |
| `HOLDOUT?` | `Y` / `N` — claimed as sealed historical holdout |
| `FORWARD?` | `Y` / `N` — forward / live-capture window |
| `FIRST_OPENED` | UTC timestamp of first open of this slice for this purpose/actor (immutable once set) |
| `WHO_OPENED` | Who performed the open |
| `STATUS` | `OPEN` \| `CLOSED` \| `CONTAMINATED` \| `SEALED` \| other explicit |

### Row table (copy into active ledger)

```
| DATA_ID | SLICE_ID | START | END | USED_BY | PURPOSE | RESEARCH? | VALIDATION? | HOLDOUT? | FORWARD? | FIRST_OPENED | WHO_OPENED | STATUS |
|---------|----------|-------|-----|---------|---------|-----------|-------------|----------|----------|--------------|------------|--------|
```

---

## Hard rule — no validation laundering

**Once a slice has been used for hypothesis tuning (or any exploratory / RESEARCH peek that informed SIGNAL, parameters, or cell choice), it MUST NOT later be labeled or treated as sealed validation.**

- Mark `RESEARCH?=Y` at first such use; do not flip to `VALIDATION?=Y` afterward.
- If contamination is discovered after the fact, set `STATUS=CONTAMINATED` and open a new, unused slice for true validation.
- Holdout and forward windows follow the same honesty: prior peek ⇒ not sealable as untouched.

**RETROACTIVE:** NO — this ledger governs going-forward opens; it does not rewrite prior TEST/CEM verdicts.
