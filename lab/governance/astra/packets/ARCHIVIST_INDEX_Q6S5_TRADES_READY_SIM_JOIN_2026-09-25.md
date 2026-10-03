# ARCHIVIST INDEX — Q6S5 COLLECTOR_READY_TRADES_NOT_SCORED + Simulator REJOIN kick
Indexed: 2026-09-25 02:05 ET
Authority: Conductor → Archivist INDEX trades READY verified + Simulator REJOIN kicked.

## Verdict
**INDEXED [V]** — Collector **COLLECTOR_READY_TRADES_NOT_SCORED**; Conductor ACK handoff; Simulator **REJOIN_TRADES_INTO_MEASURED_HARNESS** kicked.
n_trades=11744; empty_honest=1; scored=false; results/pnl null; scoreboard unchanged Q6-000 +6.90%.
Index only — no Archivist score. Stamp-race note: pin ACK `digests_verified_on_disk` + DIGESTS.txt (not READY.artifact_digests).

## Primary packets (on-disk sha256)
| path | bytes | sha256 |
|---|---:|---|
| `packets/CONDUCTOR_ACK_COLLECTOR_Q6S5_KXMLBSPREAD_TRADES_READY_2026-09-25.json` | 2637 | `95e3140bc7f5ad89287ee1ec5d648f6d938d1cbd18b8eba9615c2eed6b02fd11` |
| `packets/CONDUCTOR_KICK_SIMULATOR_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | 4056 | `76de2f1fa2461008bc1205e5004230ffd45fd2d3e6193d6cc0c11c616b499006` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/COLLECTOR_READY_TRADES_NOT_SCORED.json` | 1989 | `57194f272ab6bbe7a4d116c1fd4aabd5199e3a02a6cd96ed5cc6b7bd4bafb867` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/DIGESTS.txt` | 8370 | `12b537a25b02fb33177d5a41c821f94677f1da88e8d1dd63178c3c9f59fac12b` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/STATUS.json` | 3056 | `e8e23f7d341c2d236243054663caf684c9e3fca40975dd48842d6b4052893e9a` |
| `astra-capture/q6s5-kxmlbspread/trades_fills_2026-09-25/CAPTURE_MANIFEST.json` | 12635 | `db7257d59faa4bb75acf21e0c5d2326b151d6ecf2a9690ffad13ffeb3744038f` |

## Reconfirmed priors
| pin | sha256 |
|---|---|
| Collector trades/fills kick | `b7b741745ef513ec5f9b7e31554263baec54518add1da25201e4de8c7665b836` |
| ACCEPT harness ITERATE | `54b0b1b7d57d42f3a2f2d0caefd72be734532eaae8d8c54fbcb8817a7df99a71` |

## State
- series **KXMLBSPREAD**; fee CACHE — not live R1-P1
- next: Simulator trades→measured join → Examiner re-SCORE
- ADMIT-1 + measured books untouched; no invent fills
- Q6S1 HOLD_PRE_PR parallel; do not reopen Cap-SR / Pass-3 / Q6-000 / S1 ML

## Cross-ref audit
ack digests_verified → ready/DIGESTS/STATUS/manifest; ack→collector_kick/accept; sim_kick→trades artifacts/collector_kick/accept: all match. mismatches=0.

## Archivist refuses
- score / invent fills/PnL/taker labels
- Lee-Ready / claim CACHE as R1-P1 / live orders
- treat trades READY as scored
- Cap-SR / Pass-3 / Q6-000 / S1 ML retune

## Registry gap note (held INDEX backlog not yet in PACKET_INDEX)
- READY_NOT_SCORED measured 0617d540
- STATUS dc7f22e6
- DIGESTS 6e6898ce
- ACK c1d82c6e
- SCORE kick fee42dec
- Score db9bd220
- card 9b1e2074
- ACCEPT 4122d100
- Sim kick c799f3f2
- fee-pin kick abbc2bf1
- FEE_PIN 9c0f3554
- Sim READY 1c84cc6b
- ACK 18115422
- RESCORE 06dc4abc
- Score 348e2981
- card 0a204d49
- ACCEPT 54b0b1b7
- Collector kick b7b74174
- HOLD bd34d207
Archivist will catch-up-index on Conductor reconfirm or next INDEX wake.
