# Edit log with _prev bytes (RULE-FROZEN-EDIT-PREV-BYTES-001)

## Card 04 brief
| file | old sha256 | new sha256 | _prev path | note |
|---|---|---|---|---|
| SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md | 3f893cbfbc020fc6735b8557d3e7950745ea43c7c6564d59e3f79d3ac6d03fe0 | c15326583e96dcfa986e10e963ca1238320fa295a8c53cc13e248a9735adbafb | `_prev/3f893cbfbc020fc6735b8557d3e7950745ea43c7c6564d59e3f79d3ac6d03fe0.SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md` | Append AMENDMENT 01 (fees RT + FREEZE_GAP). Prev bytes reconstructed by truncating at amendment marker; hash matches pre-amend sha recorded at edit time. |
| SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md | c15326583e96dcfa986e10e963ca1238320fa295a8c53cc13e248a9735adbafb | 773e5abee36f6aae51dc49d0e8bab08f7e800a040b06754e47f5d02b3bda7e43 | `_prev/c15326583e96dcfa986e10e963ca1238320fa295a8c53cc13e248a9735adbafb.SCOUT_PERPS_STALE_QUOTE_SCREEN_2026-09-24.md` | Wording fix in amendment (threshold list not pre-specified). Prev reconstructed by reverse replace. |

## Card 06 packet
Freeze original **never edited**. Amendments are new files.
| file | old sha256 | new sha256 | _prev path | note |
|---|---|---|---|---|
| packets/scout_card06_census/AMENDMENT_01_2026-09-24.md | b8e263bf… (hashed) | transient 8a6811f6… then reverted to b8e263bf… | `packets/scout_card06_census/_prev/8a6811f664aba55f6ea2e2ab0dbb3e9f8a661d2625527db0412994275108a4b0.AMENDMENT_01_2026-09-24.md` | Transient DOL fetch-time wording edit; reverted. Final == hashed original. |
| packets/scout_card06_census/raw/official/bls_empsit_schedule_BROWSER.txt | d57d0e61df4a4feb79bac943631124d98f2ab4d448e0ae4cf15cd11e2b489f08 | 9946ff9e001627178ec53e5ceba155c543e69f9c7b6ff2bb99e788a6b74485f5 | `packets/scout_card06_census/raw/official/_prev/d57d0e61….bls_empsit_schedule_BROWSER.txt` | Fetch-time annotation aligned to `_fetch_log.tsv`. |
| packets/scout_card06_census/raw/official/bls_schedule_2025_BROWSER.txt | 20431e29ceeb7d24d5d048300f6ffa60b91e7362e11118486b05904de88d2c26 | 5b38427a080fb184aacd0868aae6e93626aabde3c4d9f6c2bced2f3f9060ec98 | `packets/scout_card06_census/raw/official/_prev/20431e29….bls_schedule_2025_BROWSER.txt` | same |
| packets/scout_card06_census/raw/official/tesla_ir_BROWSER_ERRORBODY_http403.txt | 385a6eceac7f31bce2a8223d04e436687631ee0d10cfe643c9e3291ece445df8 | 66ab3c58816d802681d4038c880f1aa59d84039b385e31ed3c3b2887a2d6ff40 | `packets/scout_card06_census/raw/official/_prev/385a6ece….tesla_ir_BROWSER_ERRORBODY_http403.txt` | same |
| packets/scout_card06_census/script/build_arrivals.py | d4948cca6913e6c1813c345f9b655888769d463bee71bc52f42d673126b4d657 | a2809637144614775d393a767bc0ec267c405e33664816ba62497d004f257579 | `packets/scout_card06_census/script/_prev/d4948cca….build_arrivals.py` | GDP mapping: rules quarter → BEA Advance Estimate (ticker date ≠ release). Helper script (not in freeze hash list). |

Card 04 packet files under `packets/scout_perps_screen_2026-09-24/` were **not** re-edited after this rule.

## SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md path clarify
- old: 6a9dc3d447d41e5b6a6902249cecc5e33c5134e5cd10135e710c480bfda6662d.SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md
- new: 02fb1de12c573c2330899562cd832b48bd024a1c9f0e3886f23e1be83751b8e8
- reason: label nonstandard JSON path as raw/docs/
EDIT 6a9dc3d447d41e5b6a6902249cecc5e33c5134e5cd10135e710c480bfda6662d.SCOUT_HOUSE_FEE_SOURCE_2026-09-24.md → 02fb1de12c573c2330899562cd832b48bd024a1c9f0e3886f23e1be83751b8e8 path label for nonstandard JSON
