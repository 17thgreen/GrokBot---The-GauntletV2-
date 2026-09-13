# Coverage freeze — DATA-PROV-L3-001
**Clock CONDITIONAL** 2026-09-12T00:15:15Z · Conductor lock before F1 Examiner

## Join (binding)
knowable_bar = argmax { bar | close_time_ms <= decision_time_ms }
S_t = knowable_bar.close
On this PM-003 slice: open_time_ms = decision_time_ms - 60000.

## CLEARED
F1_price_at_t_completed_1m_close · F1_RV_sigma_trailing_completed_1m (completed bars only; W=60 as card)

## BLOCKED
Incomplete-bar close (lookahead) · Binance as oracle/F2/CF · holdout extension · F2

## Window
2026-09-04T00:00Z → 2026-09-11T23:59Z spot 1m only.
