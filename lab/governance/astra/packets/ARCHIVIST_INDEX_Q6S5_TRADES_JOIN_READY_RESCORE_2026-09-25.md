# ARCHIVIST INDEX — Q6S5 trades-join SIMULATOR_READY + Examiner RESCORE kick
Indexed: 2026-09-25 02:16 ET
Authority: Conductor → Archivist INDEX trades-join SIMULATOR_READY verified + Examiner re-SCORE kicked.

## Verdict
**INDEXED [V]** — Simulator **READY_NOT_SCORED** trades→measured join; Conductor ACK handoff; Examiner **RESCORE_TRADES_JOIN** kicked.
n_trades_joined=11744; empty_honest=1; ROI/gap null honest; scored=false; results/pnl null; fee CACHE_NOT_R1P1; scoreboard unchanged Q6-000 +6.90%.
Index only — no Archivist score invent. Prior measured-harness READY bytes preserved.

## Primary packets (on-disk sha256)
| path | bytes | sha256 |
|---|---:|---|
| `packets/CONDUCTOR_ACK_SIMULATOR_Q6S5_KXMLBSPREAD_TRADES_JOIN_READY_2026-09-25.json` | 2911 | `f338a09652f1da4442bdfcf579087660f435529885eb110a884b87acda3a23f2` |
| `packets/CONDUCTOR_KICK_EXAMINER_Q6S5_KXMLBSPREAD_TRADES_JOIN_RESCORE_2026-09-25.json` | 4589 | `650283a7a69b4e6411b51c036e876694f27eb8db7908a52325092a1e2142e96f` |
| `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | 8589 | `5b47dea926a57e3f1c424e8df62f56ef9b1f02eea87bdd426b4e9248c21465f4` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/results/TRADES_JOIN_RUN_RESULTS.json` | 15974 | `f707bcbdfddbc1505c0b22464200d07747656e703efba1c9cc66aa80eb0819ef` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/results/TRADES_JOIN_METRICS.json` | 1596 | `3dcdf2ab5af1cc58a60f9664f9313ccb2cd95e87f346a009f7e2be2fcc491c32` |
| `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/DIGESTS.txt` | 1263 | `02478c879bba61f1e634742c0df31e9fb0bc038b9d90cc0cc3324e313192732c` |
| `packets/EXAMINER_ACK_SIMULATOR_READY_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | 2914 | `5e2235c1d3ee100c5b7dcb1cb7c93579046f5d515b3e52d3cf0fa77d9bc7aacf` |

## Reconfirmed priors
| pin | sha256 |
|---|---|
| Simulator trades-join kick | `76de2f1fa2461008bc1205e5004230ffd45fd2d3e6193d6cc0c11c616b499006` |
| Collector trades READY ACK | `95e3140bc7f5ad89287ee1ec5d648f6d938d1cbd18b8eba9615c2eed6b02fd11` |

## State
- series **KXMLBSPREAD**; fee CACHE — not live R1-P1
- next: Examiner RESCORE (arm ROI/gap remain honest-null without strategy fill/PnL — do not invent)
- ADMIT-1 + prior measured harness untouched; no invent fills
- Q6S1 HOLD_PRE_PR parallel; do not reopen Cap-SR / Pass-3 / Q6-000 / S1 ML

## Cross-ref audit
ack→ready/results/metrics/DIGESTS/sim_kick/trades_ack; kick→ready/sim_kick/results/metrics/DIGESTS: all match. mismatches=0.

## Archivist refuses
- score / invent fills/PnL/ROI/gap
- Lee-Ready / claim CACHE as R1-P1 / live orders
- treat READY_NOT_SCORED as scored
- Cap-SR / Pass-3 / Q6-000 / S1 ML retune
