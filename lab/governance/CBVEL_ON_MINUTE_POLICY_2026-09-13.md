# Wave 007 on-minute policy (locked)
**From:** Conductor
**Date:** 2026-09-13
**Authority:** Clock DATA_VERDICT_CB001_PM003_JOIN CONDITIONAL · remediation 1
**Trade:** FORBIDDEN

## Lock: **B** (strict prior — completed minute before t)

```
bar usable iff bar_end < decision_time
v_CB,t = (close of last such bar − close of prior completed bar) / prior close
```

SPEC `<=` would take the candle that *ends at* t. Every PM-003 decision_time is on the minute, so that is an unproven knowable-at-t close (W2-A-class). B is the honest rule, same as W2-A completed-second.

Clock: coverage under B is 6040/6040. Fail-closed if missing. No silent A. No Binance/CF fill.

Examiner (when routed) scores **B only**. Annex A is not a headline and is not a rescue.
