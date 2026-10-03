# Archivist index: Examiner HOLD_PRE_PR Q6S5 — recorded 2026-09-25 00:16 ET

## Packet
| field | value |
|---|---|
| path | `packets/EXAMINER_HOLD_PRE_PR_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_2026-09-25.json` |
| sha256 | `4fff8de68d763138adce448b0138f87477a2a2bb96248c01f17caa2c05ef2329` (4135 B) |
| status/decision | `HOLD_PRE_PR` / `HOLD_PRE_PR` |
| series | `KXMLBSPREAD` |
| packet_id | `Q6S5-KXMLBSPREAD-FEEQUEUE-HARNESS` |
| scored / stub_ready | `False` / `False` |
| results / pnl | `None` / `None` |
| fee_cache | `{'fee_type': 'quadratic', 'multiplier': 0.5, 'label': 'CACHE-LABELED', 'not_live_R1_P1': True, 'note': 'CACHE-LABELED quadratic×0.5; not R1-P1 absolute fee-honest until live /series pin'}` |
| ack_status | `ACK_HOLD_PRE_PR` |
| stamped (if any) | `2026-09-25T00:15:05-04:00` |

## Pin verification (Conductor cites + on-disk)
| pin | on-disk sha256 | vs Conductor claim |
|---|---|---|
| ACCEPT | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` | MATCH `5adc42f9…` |
| Kick | `38375ffe1a554b406c6ea0e48be7cf9b71d3c1f0d0e1b6713cbc4ae76bff6c54` | MATCH `38375ffe…` |
| Freeze | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` | MATCH `4f65dcdf…` |
| Panel | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` | MATCH `c7f1f1f4…` |

## Embedded-hash audit (inside HOLD packet vs on-disk)
| field | cited | on-disk | result |
|---|---|---|---|
| `conductor_accept_sha256` | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` | `5adc42f9c9533238a2187aafe7593bdf1b8cdec6d12b8d3e9b12cb5ab29000fc` | MATCH |
| `conductor_kick_sha256` | `38375ffe1a554b406c6ea0e48be7cf9b71d3c1f0d0e1b6713cbc4ae76bff6c54` | `38375ffe1a554b406c6ea0e48be7cf9b71d3c1f0d0e1b6713cbc4ae76bff6c54` | MATCH |
| `freeze_sha256` | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` | `4f65dcdf536755b9f7dc2449c2dcd90b2df74cdf99a441b676f1a71c4d709c6e` | MATCH |
| `panel_stub_sha256` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` | MATCH |
| `panel_sha256` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` | `c7f1f1f4ca263838c4600ed46db8f525b68efc5399a567bd60929d18d76803cc` | MATCH |

## Prior related object (already indexed earlier)
| path | sha256 |
|---|---|
| `packets/EXAMINER_HOLD_Q6S5_KXMLBSPREAD_FEEQUEUE_HARNESS_PRE_PR_2026-09-25.json` | `57bbd3ddf8e99fe790eb827f3167f529528f0a30ae27ece1ff909617b2091aa8` |

## Rulings indexed
- Examiner **HOLD_PRE_PR** ACK for Q6S5-KXMLBSPREAD-FEEQUEUE-HARNESS.
- Do **not** score until merge + READY NOT_SCORED.
- Fee remains CACHE-LABELED quadratic×0.5 (not live R1-P1).
- results/pnl null; Q6-000 scoreboard unchanged.
- Variants sole-implement cloud informational only (Archivist does not launch/track clouds).
- Distinct from earlier HOLD stub `57bbd3dd…` — this packet is the Conductor-verified HOLD_PRE_PR index target.

**Status:** INDEXED. No scores / no orders from Archivist.
