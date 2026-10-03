# CEM-ASTRA-20260924-006 — Card 06 macro open-window families (close before official source)

- **CEM_ID:** CEM-ASTRA-20260924-006
- **DATE:** 2026-09-24 (ET) · Conductor (measurement ACCEPT) · Archivist to index
- **CARD:** Kalshi Edge Research card 06 (official-source interpretation), **non-CPI macro families** from the open-window census. CPI/CPIYOY already dead as CEM-ASTRA-20260924-003. Company-KPI lane (non-Tesla) stays open for a separate freeze.
- **DECISION:** **CEMETERY_UP_FRONT** for the five families below. Structural timing: market `close_time` is before (or equal to) official source arrival, so a post-release taking window does not exist on sourced rows.
- **CLASS of killing evidence:** historical + open contract panel vs official schedules [V] · CLASS_FIT_POOR (structural timing, not a scored strategy run).

## Families killed (sourced rows all NO)

| Family | Series | n / sourced / YES / NO / U | Pattern |
|---|---|---|---|
| Initial claims | KXJOBLESSCLAIMS | 20 / 20 / 0 / 20 / 0 | Close ~08:25 ET; DOL claims 08:30 Thu |
| Core PCE | KXPCECORE | 20 / 20 / 0 / 20 / 0 | Close ~08:25 ET; BEA PIO 08:30 |
| Fed decision | KXFEDDECISION | 13 / 2 / 0 / 2 / 11 | Sourced Jul/Sep 2026: close ~1:55–1:59 PM vs 2:00 PM statement (partial) |
| Fed funds level | KXFED | 17 / 6 / 0 / 6 / 11 | Same close-before-statement pattern (partial) |
| EIA crude | KXEIACRUDEW | 5 / 5 / 0 / 5 / 0 | Close 10:29 ET; EIA 10:30 Wed |

## Evidence pins

- Freeze: `packets/scout_card06_census/FREEZE_CARD06_CENSUS_2026-09-24.md` sha256 `db3b0a18fd96e2f56d309f1a1b40e46bfd84953699e76163c2ad62440f0044fe` · freeze_time_ET 2026-09-24 20:05:11 EDT
- Brief: `SCOUT_CARD06_OPEN_WINDOW_CENSUS_2026-09-24.md` sha256 `b79f4011849e7603dcbb6b1d452bd21d7cba3e3bd1c01f4d301f650294f53bfc`
- Machine table: `packets/scout_card06_census/out/census.json` sha256 `eefe61d9b664e87de1dc82b3019f85c77ca8b95e7ae843ca260305c1893c4fe5` · `out/census_rows.csv`
- Conductor ACCEPT: `packets/CONDUCTOR_ACCEPT_CARD06_OPEN_WINDOW_CENSUS_2026-09-24.json`
- Open-window rule (frozen): YES iff arrival_ET < close_ET; gap 0 = NO. Official arrivals only.

## Not killed by this entry

- **KXPAYROLLS / KXGDP (MIXED):** Conductor NO_BUILD. Lone YES rows are API `close_time` anomalies vs rules close language; not an OPEN-WINDOW family and not a build ticket.
- **KXTESLA (UNSOURCED):** PARK (IR 403). Not cemetery — no sourced proof either way.
- **Company-KPI open-window census (other tickers):** still the Card 06 differentiator path.

## What this did not prove

- No fee-honest P&L. No fills. No live edge. Only that these macro series close before the official print on sourced events in the frozen census.

## Rules

- Frozen negative stays visible. Never delete or soften.
- No resurrection without a **new freeze** proving, per contract, source arrival before market close on a sourced panel.
- Data published after close cannot be traded (lookahead).
- No live orders. No invented PnL.
