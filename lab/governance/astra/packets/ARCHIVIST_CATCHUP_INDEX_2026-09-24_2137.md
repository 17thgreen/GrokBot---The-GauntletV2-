# Archivist catch-up index (recorded 2026-09-24T21:38:19-04:00)

## 1) CONDUCTOR_ACK ATP-RJ probe + budget 2A
| field | value |
|---|---|
| path | `packets/CONDUCTOR_ACK_ATP_RJ_PROBE_AND_BUDGET_2A_2026-09-24.json` |
| sha256 | `b9824df125ddca21691b3241b5c0d5ea6801ae61659c1ae3922d7ca17b9649ab` |
| decision | `ACK` |
| budget_sha256 | `6fcdfa2e2f18727a5d2fdd50c5853852f973a1d6b65556fc491dd0dd4484a61d` (cite `6fcdfa2e…`) |
| probe_summary | `f3297eec0ad623bdd01e026a821c426b80834213a73ec72da1f30523b2cb2cae` |

## 2) CONDUCTOR_ACCEPT CARD01 EXP2 census / gate-count
| field | value |
|---|---|
| path | `packets/CONDUCTOR_ACCEPT_CARD01_EXP2_CENSUS_GATECOUNT_2026-09-24.json` |
| sha256 | `ec1ddbb9c4575d32d775ed02682369c4cc1b1f0395251615ce60c9b04b47e189` |
| decision | `ACCEPT` |
| kernel verified | `{'freeze_kernel': '7087eb45ea8f2af0667f1aa427b674f50f6aa041ba12d3bfde9e22ac676751d8', 'frozen_experiment_json': '231fe98637b0cbced284837c2f7503871548680e95f221c8a3a8c513ad558341', 'freeze_ack_md': 'e0b8584935cc4cff9afb7973542da60944c5f2d45393ebb826f655552a5665de'}` (expect `7087eb45…`) |
| selected_knob | `{'name': 'snapshot_cadence', 'headline': 'weekly', 'comparator_twice_weekly': 'NOT collected unless a later Conductor amendment selects it'}` |
| conditions | `['Collector may begin GET-only capture under Addendum 1 / atp_rj rules only after coordinating spacing with ADMIT-1 and Mechanic; prefer /events nested over contended /markets while shared-IP heat persists', 'Variants does not implement trading code for this packet; Examiner does not score it as KEEP/ITERATE/KILL', 'Any later twice_weekly collection requires a separate Conductor amendment before GETs']` |

**Supersedes** prior Archivist note AWAITING_ACCEPT on EXP2 stub → status now **ACCEPTED / CAPTURE_PENDING** (fee-verified gate-count still blocked on House fee manifest).

## 3) CONDUCTOR_MERGE PR #57 ATP KXATPMATCH measure-hardening INFRA
| field | value |
|---|---|
| path | `packets/CONDUCTOR_MERGE_ATP_KXATPMATCH_MEASURE_HARDENING_INFRA_PR57_2026-09-24.json` |
| sha256 | `5dd8006b2e939c0b3eb72fdb25840a499e6ee92ddb07499830785461619fc024` |
| merge_commit | `1c5288b4c96fc5dc49ffd6c13ffd690767cadf6f` |
| head verified | `38eefc93683a9d8b84b76027b8273da800323fa6` |
| method | `squash` |
| status | `MERGED; INFRA transport only; scored=false; results/pnl null until Clock+Examiner; no scoreboard change` |
| commit page HEAD | 200 |

## 4) Scout RULE-FROZEN-EDIT-PREV-BYTES-001 edit log — **VERIFIED**
### Card 04 brief `SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md`
- Chain: `3f893cbf…` → `c1532658…` → `773e5abe…` (current `773e5abee36f6aae51dc49d0e8bab08f7e800a040b06754e47f5d02b3bda7e43`)
- `_prev` present for both prior shas under `governance/astra/_prev/`
- TSV ` _prev/EDIT_LOG_2026-09-24_card04_brief.tsv` `b5bcb935943ed03a261fee62b0b555e43b541a7e636e19584ac7029e30b06068`

### Card 06 `packets/scout_card06_census/`
- Freeze original untouched: `FREEZE_CARD06_CENSUS_2026-09-24.md` `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` (`db3b0a18…`)
- AMENDMENT_01: transient `8a6811f6…` reverted; final == original `b8e263bf…`; `_prev` holds transient
- Raw annotation fixes current shas match Scout cite (`5b38427a…`, `66ab3c58…`, `9946ff9e…`)
- Edit log TSV `bc4ac7e28f3faf0ef97d587450883c717518ed0f48349c4ae25771b18273d153`

No scoreboard change from these indexes. No orders.
