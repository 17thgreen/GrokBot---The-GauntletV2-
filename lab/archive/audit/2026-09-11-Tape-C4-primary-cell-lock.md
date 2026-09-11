# Audit — Cycle 4 Tape primary cell lock

- **UTC:** 2026-09-11
- **Actor:** The Archivist
- **Source:** The Tape Reader (+ Conductor hold on TEST)
- **Event:** PRIMARY_CELL_LOCK + CARD_PATCH

## EDGE-20260911-001 (TR_FLOW_CNT_01)
- **Primary cell:** W_trade=1m, L=288, Q*=0.80, N_min=20, Δ_exec=500ms, h=1 (5m), residual=linear on {r_t,|r_t|,vol_t,range_t}
- PARAMETERS grid updated per Tape lock
- KNOWABLE/ENTRY/EXIT/ABSTENTION unchanged (confirmed correct)

## EDGE-20260911-002 (TR_FLOW_LRG_01)
- Truncation [A] cleared — ENTRY/EXIT/ABSTENTION/PARAMETERS originator-final
- **Primary cell:** p=0.95, W=1m, K=3, C*=0.50, P*=0.67, V_min=0, L_size=2000, L=288, α=0.50, Δ_exec=500ms, h=5m
- CONFIDENCE: 32/100 [H]; truncation caveat removed

## Gate
- **[V]** Both HYPOTHESIS CLEAR_TO_TEST
- **[V]** TEST route HELD until DATA-PROV-TRADES-001 Clock verdict + Conductor route
- **[V]** EDGE-005/006 still L2-blocked
