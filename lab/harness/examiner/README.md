# Examiner harness — PROV-MEAS-20260910-001 / EDGE-20260910-001

Deterministic short-horizon BTC/ETH backtest harness for Logan's alpha lab.

**Default measurement without approved data: `UNTESTED`.**  
This harness invents **zero** Sharpes, returns, or trade counts.

## Quick start

```bash
cd /workspace/lab/harness/examiner
pip install -r requirements.txt

# No data → UNTESTED (exit 0)
python -m src.run_edge001 --package PROV-MEAS-20260910-001

# Unit tests
python -m pytest /workspace/lab/harness/examiner/tests -q
```

## When DATA-PROV arrives

```bash
python -m src.run_edge001 \
  --package PROV-MEAS-20260910-001 \
  --data /workspace/lab/data/DATA-PROV-YYYYMMDD-NNN
```

Requirements for the data directory:

- `MANIFEST.json` with `clock_verdict` ∈ {`APPROVED`, `CONDITIONAL`} (else UNTESTED)
- `btc_5m.csv` / `eth_5m.csv` (or paths listed in manifest)
- Columns: `timestamp, open, high, low, close, volume` (UTC exchange event time)

`CONDITIONAL` with research-only scope → VALIDATION/HOLDOUT not used for promotion gates.

### Opening sealed holdout (rare)

Holdout (final 20% post-warmup) is **SEALED by default**. Evaluation requires **both**:

1. CLI flag `--open-holdout`
2. Conductor order file (default: `config/CONDUCTOR_OPEN_HOLDOUT.order`)

```bash
python -m src.run_edge001 \
  --package PROV-MEAS-20260910-001 \
  --data /workspace/lab/data/DATA-PROV-... \
  --open-holdout \
  --conductor-order /path/to/CONDUCTOR_OPEN_HOLDOUT.order
```

## Signal (EDGE-001)

- 5m bars; `r_t` = close-to-close return
- `RV_t` = sum of squared returns over `W` completed bars ending at `t`
- `Q_lo` = trailing empirical quantile of RV over `L` completed bars ending at `t` (no future)
- Signal when `RV_t ≤ Q_lo` and `|r_t| > ε`
- Position = `Sign(r_t)`; flat at close `t+h`
- Gross bps (sign-aligned): `Sign(r_t) * (close[t+h]/close[t]-1)*1e4`
- Net = gross − `C` (bps round-trip)

**Primary cell (pre-registered):** `W=24, Q_lo=0.33, L=288, h=1, ε=small`

## Assumptions **[A]**

| Item | Value | Tag |
|------|-------|-----|
| `C_base` | 7.0 bps (fees 4 + spread 2 + slip 1) | [A] |
| Stress | 1×=7, 2×=14, 3×=21; gross C=0 diagnostic only | [A] |
| Latency stress | +1 / +3 bp on 1× C — `LATENCY_STRESS_[A]` | [A] |
| `ε` small | `0.00005` (0.5 bps absolute return) | [A] |
| `ε` 2×small | `0.0001` | [A] |
| Warmup | `max(W)+max(L)=624` bars | locked |
| Splits | RESEARCH 60% / VALIDATION 20% / HOLDOUT 20% post-warmup | [A] until frozen per DATA_ID |

Frozen machine-readable copy: `config/PROV-MEAS-20260910-001.json`.

## Non-claims

- **OF mechanism is NOT validated** by this OHLCV conditional-return test.
- Provisional net ≠ executable / venue-live alpha.
- Assumed 7 bps ≠ any venue’s true cost stack.
- BTC and ETH are **separate** pipelines; no pooled-only claims.

## Layout

See package tree under `src/`, `tests/`, `fixtures/` (synthetic mechanics only), `out/`.

Authoritative specs:

- `/workspace/lab/harness/provisional/PROVISIONAL_MEASUREMENT_PACKAGE_EDGE-20260910-001.md`
- `/workspace/lab/harness/provisional/DATA_ATTACHMENT_REQUIREMENTS.md`
- `/workspace/lab/archive/edges/EDGE-20260910-001.md`


## EDGE-20260910-003 — Range-expansion snapback (Cycle 2)

**Status:** Primary cell LOCKED [V]. Harness ready. Cite **CEM-20260910-001** — NOT a rescue of EDGE-001.

| Item | Value |
|------|-------|
| Package | `PROV-MEAS-EDGE-003` |
| Signal module | `range_expansion_snapback` (`src/signal_edge003.py`) |
| Primary cell | p=0.95, L=288, h=1, ε=small(5e-05 [A]) |
| range_t | (high−low)/close [A] |
| r_t | close-to-close **log** return (Edge Card) |
| Position | −Sign(r_t) fade; exit close t+h |
| Economics | C_base=7bps [A], stress 1×/2×/3×, latency +1/+3 — reused from PROV-MEAS-001 |
| Splits | SEAL_LOCK 60/20/20; sealed/ NEVER without Conductor order |
| CLI | `python -m src.run_edge003 --package PROV-MEAS-EDGE-003 --data ...` |

Without locked `primary_cell` the CLI exits `BLOCKED_PENDING_PRIMARY_CELL` / `UNTESTED` and invents **zero** metrics.

VALIDATION is evaluated only if RESEARCH does not FAIL (per instrument).

```bash
python -m src.run_edge003 \
  --package PROV-MEAS-EDGE-003 \
  --data /workspace/lab/data/DATA-PROV-001 \
  --test-id TEST-20260910-002
```

Edge Card: `/workspace/lab/archive/edges/EDGE-20260910-003.md`
