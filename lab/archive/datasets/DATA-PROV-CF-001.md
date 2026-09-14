# DATA-PROV-CF-001

- **DATA_ID:** DATA-PROV-CF-001
- **NAME:** Entitled CF BRTI / ETHUSD_RTI close-minute ticks for PM-003 Kalshi 15m
- **STATUS:** CLEARED
- **Registered:** 2026-09-13 UTC
- **Path:** `/workspace/lab/data/DATA-PROV-CF-001/`
- **Role:** L2 official settlement-index tape (close minute only). F2 / FEAT-005.
- **NOT:** Binance · public unauth Kalshi candles · EXPIRATION_VALUE feature
- **Auth:** Kalshi Trade API CF passthrough (entitled). Keys not stored in this tree.
- **Parent arena:** DATA-PROV-PM-003 1208
- **Trading:** Forbidden

## Access gates

| Path | Access |
|------|--------|
| raw/ | hour payloads (no secrets) |
| derived/ | 1Hz close-minute ticks + pre_close_last |
| Examiner | after Clock DATA VERDICT |
| Trading | Forbidden |


## Clock
- **DATA VERDICT:** CLEARED (2026-09-13T17:53:52Z)
- Path: `data/DATA-PROV-CF-001/provenance/DATA_VERDICT_DATA-PROV-CF-001.md`
- 1208/1208 contracts 60/60 close-minute 1Hz; pre_close_last 1208/1208
- Missing-sec rate BTC/ETH: 0.0 / 0.0 on close minutes
