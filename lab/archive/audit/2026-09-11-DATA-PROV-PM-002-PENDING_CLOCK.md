# Audit — DATA-PROV-PM-002 registered PENDING_CLOCK

**Date (UTC):** 2026-09-11  
**Actor:** Conductor  
**DATA_ID:** DATA-PROV-PM-002  
**Parent:** DATA-PROV-PM-001 (Clock CONDITIONAL; labels only)

## What landed

Intra-window decision-time \(m_t\) reconstructed from public APIs (no keys) on a bounded stride sample:

- 120 Kalshi 15m BTC+ETH + 120 Polymarket Global 5m/15m BTC+ETH = 240 contracts
- 240/240 have ≥1 intra-window price
- 1140 checkpoint rows
- `derived/checkpoints.ndjson` SHA256 `affbbbd0b07c765d3f7c0af5e6b23564d3973ec82f27fe7d48b84bc4ded89dc0`
- CHECKSUMS.sha256 253/253 verify PASS

Not a terminal-only blocker. PM-001 terminal last/outcome prices were **not** used as \(m_t\).

## Status

- Dataset card: `archive/datasets/DATA-PROV-PM-002.md` — PENDING_CLOCK
- Clock DATA VERDICT: **requested, not issued**
- Examiner market-relative: **still BLOCKED**
- Independent oracle: still UNTESTED
- Historical books: still ABSENT
- Full 3824: not fetched

## INDEX / ledger

INDEX Track B PRIMARY updated. Dataset-use ledger: SLICE-PM002-BOUNDED-240 CAPTURED_PENDING_CLOCK (reconstruction only — not hypothesis tuning, not validation, not holdout).
