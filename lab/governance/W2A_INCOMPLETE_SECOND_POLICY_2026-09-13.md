# W2-A incomplete-second policy (locked)

**From:** Conductor
**Date:** 2026-09-13
**Authority:** Clock DATA_VERDICT_W2A_CF_T14_JOIN CONDITIONAL · remediation 1
**Trade:** FORBIDDEN

## Lock: **B** (completed-second)

```
s     = floor(decision_time_ms / 1000)
cf_t  = last-in-second print on unix second (s − 1)
        from DATA-PROV-CF-001 hour tape (BRTI / ETHUSD_RTI)
        require print exists AND timestamp_ms <= decision_time_ms
        require (s − 1) is a completed second: (s) * 1000 <= decision_time_ms
```

All T-14m decision_times are on-second. Order-literal A would take the ms=0 print of the *current* second, which is not complete. The Clock order already forbade treating that second as complete. B is the honest rule.

Coverage under B: 604/604 BTC, 604/604 ETH (Clock). Fail-closed if missing. No silent A. No T−1. No close-minute CLEARED extractor.

Examiner TEST-20260913-004 scores **B only**. Annex A is not a headline and is not a rescue.
