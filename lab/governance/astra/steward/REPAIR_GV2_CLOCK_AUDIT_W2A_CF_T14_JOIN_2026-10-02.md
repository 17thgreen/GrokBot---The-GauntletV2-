# REPAIR — GV2 BAD_ON_MAIN CLOCK_AUDIT_W2A_CF_T14_JOIN.md (2026-10-02)
- Trigger: RUN_END sync-20261002-1840 bad_on_main=1 (commit aa9f0f0e, got blob 5229a5da) [V]
- Path: lab/data/DATA-PROV-CF-001/provenance/CLOCK_AUDIT_W2A_CF_T14_JOIN.md
- Source: box file, 10,018 B, sha256 8d412028835fb87df5045d45ed06d72002a7c9d94487e38521bfe711b45425b6, blob 32d5f03c80a2a7b6adc6c8352330faa658f05112 [V]
- Repair: cloud agent bc-a6536b02-ba38-5ddc-b11a-21968bbf4080, real checkout, byte-exact write, 1 file only, fast-forward push aa9f0f0..a6af242 [V]
- Commit: a6af24204cf2b64280f5c51cdee57f4dcbb1e30f (parent aa9f0f0e), 18:51 ET, signed/verified [V]
- Steward independent check via GitHub API: main head = a6af2420; commit files = 1; blob = 32d5f03c80a2a7b6adc6c8352330faa658f05112 [V]
- Diff vs bad blob: one heading line ("-- **Verdict recommendation**" -> "## Verdict recommendation") — consistent with a markdown-normalized push, not content loss [I]
- Leakage scan (agent): clean; no evidence_private / ElectIndex [V per agent report]
