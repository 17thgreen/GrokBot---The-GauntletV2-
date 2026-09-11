# DATA-PROV-PM-001 — MANIFEST summary (counts + hashes + status)

Provisional sample metadata excerpt for git. Source: `lab/data/DATA-PROV-PM-001/MANIFEST.json` (not committed).

```json
{
  "DATA_ID": "DATA-PROV-PM-001",
  "NAME": "Provisional short-window BTC/ETH binary PM contracts (Kalshi 15m + Polymarket Global 5m/15m)",
  "STATUS": "PROVISIONAL_SAMPLE",
  "FETCHED_AT_UTC": "2026-09-11T20:45:58Z",
  "WINDOW_DAYS": 7,
  "CUTOFF_UTC": "2026-09-04T20:45:58Z",
  "COUNTS": {
    "kalshi_rows": 1328,
    "polymarket_rows": 2496,
    "combined": 3824,
    "kalshi_resolved_yes_no": 1328,
    "poly_resolved_yes_no": 2496
  },
  "SHA256": {
    "kalshi_ndjson": "c1a09fd7eb4e97ef4672f2d9d281299695125185bc6be0743ca6bb26c8e8186d",
    "poly_ndjson": "e199d2478b015a4210fa153883a020856f17c81169ca50558dbbf020601b8867",
    "combined_ndjson": "431f7bd1f3d5d7b96b1419c2cdd3f200c05a91086f0983a738897c7243e1f027",
    "kalshi_cutoff": "95b67f9c24ce0df86663710b671c64eb1165af3f891a9cefdebe4ba3e17f66a6"
  },
  "CLOCK_STATUS": "PENDING_CLOCK",
  "TOTAL_BYTES": 38528981,
  "CHECKSUMS_FILE": "CHECKSUMS.sha256",
  "NOTE": "Counts/hashes/status excerpt only \u2014 full MANIFEST.json and lab/data bulk NOT pushed to git."
}
```
