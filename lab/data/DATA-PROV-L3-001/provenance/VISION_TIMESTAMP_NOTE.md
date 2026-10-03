# Vision CSV timestamp note
Binance Vision spot daily 1m CSV uses **microseconds** for open_time/close_time
(e.g. open 1788480000000000, close 1788480059999999).
REST `/api/v3/klines` uses **milliseconds**.
DATA-PROV-L3-001 derived files truncate Vision times with integer `// 1000` (not round)
so close_time remains `…999` ms, matching API semantics.
Verified 2026-09-12: 11520 contiguous 1m bars/symbol, gaps=0.
