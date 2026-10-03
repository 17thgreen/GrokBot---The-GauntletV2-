# ARCHIVIST INDEX: KALSHI batch 2026-10-03 (items A–J)

- Archivist (registry seat). Written 2026-10-03 ~17:25 ET. Verify-and-record only: no scoring, no collectors or sims run, no orders, no PnL invented, no agent messaged. No packet owned by another seat was edited. The only in-place edits are the two Card 01 register repins in §3 (item I), each with `_prev` bytes saved first.
- Paths are relative to `/workspace/lab/` unless absolute. `P/` = `governance/astra/packets/`, `S/` = `governance/astra/steward/`, `W/` = `astra-capture/weather-nowcast/`, `E/` = `astra-capture/card01-nh002-house/`, `PRIV/` = `evidence_private/electindex/` (sha only; contents never read into governance).
- Tags: **[V]** = re-hashed on disk now and equal to the cited sha. **[I]** = cited or relayed only, no on-disk record. **MISSING** = bytes absent. **MISMATCH** = disk differs from cite.
- Rows marked "(reconfirmed)" were already in PACKET_INDEX and are not appended again.
- The sha256 of this receipt cannot appear inside it. See the PACKET_INDEX row appended with it and `registry/STATUS_2026-10-03.md`.
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.** Nothing in this batch is a score. EXT-K1/K2 verdict domains are DESCRIPTIVE/ITERATE/INCONCLUSIVE only, with counts_toward_keep false.

## 1. Master table

| item | path | cited sha | on-disk sha256 | embedded-pin check | _prev check | tag |
|---|---|---|---|---|---|---|
| A | `P/CONDUCTOR_ACCEPT_COLLECTOR_ADMIT1_POST_RUN_NOTE_2026-10-02.json` | `6e4922d6` | `6e4922d685e1d0ce6b0c6655f21cc2a9c586f0c5407db4ae23db752410293884` | note_sha256 9a2870db = disk; ruling ACCEPT; burst profile (2–3 workers, 1.5/s token bucket, no immediate retry after 429) is the spec for future ADMIT runs; run 19 (170 rows) ABORTED_SUPERSEDED; results/pnl/roi null | n/a (new file) | [V] |
| A | `astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md` (reconfirmed) | `9a2870db` | `9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362` | ACCEPTED status now [V] via 6e4922d6. **This closes the open [I] in receipt 0e479b7f §6.** | n/a | [V] |
| B | `S/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` (reconfirmed) | `133302a4` | `133302a440281647f7589f29dad54882928c3d43253e77cf9bef78dbb6f5d578` | resolution note §4 | 7e389f32 bytes unrestorable (unchanged) | [V]; resolution [I] |
| C | `W/KALSHI_429_STOP` (current) | `e55d6094` | `e55d6094a801131728399cefe08a1e23850f6d734c00030f625b817ccc1019ba` | = STOP_R2E marker_recreated.sha256; 429 at 2026-10-03 15:17:30 ET on KXHIGHLAX-26OCT03 | `_prev/e55d6094….KALSHI_429_STOP` self-hash OK | [V] |
| C | `W/_prev/a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399.KALSHI_429_STOP` | `a41d074e` | `a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399` | = STOP_R2D marker_clear.old_sha; cleared 09:20:25 ET | self-hash OK (r2d clear) | [V] |
| C | `W/_prev/abed68e79a21eab1ebf721c3ac41be99d95c61cb0676780ac0c240376ba5ba09.KALSHI_429_STOP` | `abed68e7` | `abed68e79a21eab1ebf721c3ac41be99d95c61cb0676780ac0c240376ba5ba09` | = STOP_R2D marker_recreated (429 at 09:20:46 ET, KXHIGHLAX-26OCT04) = STOP_R2E marker_clear.old_sha | self-hash OK (r2e clear) | [V] |
| C | `W/PROBE_R2C_2026-10-03.json` | `e69561d3` | `e69561d3718570aea642334c3874d4fa8e4f3f6baec8be0ae509217e42fda19d` | = STOP_R2D probe_record_sha256; embeds a41d074e, af0f4db3, 1a3166c4, 974ce4b5, c1fe39ac = disk | n/a | [V] |
| C | `W/STOP_R2D_AFTER_RELAUNCH_429_2026-10-03.json` | `c9341de0` | `c9341de0bc51f0a184c708b7f4bc3e040c8590ae0b727f9ed6ce6274f33d9306` | all external pins match. Its own `file_sha256` field says 4d889a24… and its `sha256` field says 12bcc402…; neither equals the disk bytes. A file cannot hold its own hash, so these are stale self-fields (pre-write values), not a cite mismatch | n/a | [V] (self-field note) |
| C | `W/archive_r2d_20261003.sqlite` (uncited) | — | `f58f421d8553fd9b13bd3a627dd906f934db17aa83c798b12c57d297562d5be8` | = STOP_R2E frozen_untouched; proof pre_since 0 in all tables; **ABORTED, EXCLUDED** | n/a | [V] (excluded) |
| C | `W/launch_r2d.sh` (reconfirmed) | `af0f4db3` | `af0f4db3f578e75db5f1b1336b14cc0a8453daf0d51fcee856567d0fc961acc0` | unchanged | n/a | [V] |
| C | `W/launch_r2e.sh` | `c168ca1d` | `c168ca1d9c3d14f7350263bf22514a1baf390a670ce1f276030ce9da0137f812` | = PROBE_R2E / STOP_R2E script_sha256 | n/a (new file) | [V] |
| C | `W/PROBE_R2E_2026-10-03.json` | `fe615c47` | `fe615c47fbe12694de7a20f7aafd106901378f05d5bb2af9fbe10fa1292ce813` | = STOP_R2E probe_record_sha256; cites ruling 8c90e657 + kick 18ed1592 = disk | n/a | [V] |
| C | `W/STOP_R2E_AFTER_RELAUNCH_429_2026-10-03.json` | `b33ada1c` | `b33ada1c68ba7572a0ff88c9cfb710cf56bb8cc12818bf1b5a1d18162ff4b1b0` | pins abed68e7 / c168ca1d / 1a3166c4 / 70912533 / 974ce4b5 / c1fe39ac / f58f421d / e55d6094 = disk; LAST box-IP attempt | n/a | [V] |
| C | `W/archive_r2e_20261003.sqlite` (post-run) | `181977c2` | `181977c23e658647f6610d1ce455c66634ef345bcbd1ff2a960ca077498bbb94` | proof pre_since 0; http_429=1; **ABORTED, EXCLUDED** (like r2b, r2d). -wal empty (e3b0c442); -shm mtime 15:57:43 ET (open by a reader, main DB unchanged) | n/a | [V] (excluded) |
| C | `W/archive.sqlite` (reconfirmed, frozen) | `974ce4b5` | `974ce4b5339b010ee28819f35f365693bfc55dd337ab0d7a192aff668714f60f` | unchanged; = PROBE_R2C / STOP_R2D / STOP_R2E frozen_untouched | n/a | [V] |
| D | `P/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.md` | `5c40fb9d…d6d3` | `5c40fb9d03a924e40577a81f262231701e331c98922f60f6dc7ab65a2dbed6d3` | in MANIFEST; = ACCEPT 02129007 / Adversary 676ba2fa / K2 json sister_freeze | n/a | [V] |
| D | `P/VARIANTS_EXT_K1_Q6000_LEGGING_RISK_AUDIT_FREEZE_2026-10-03.json` | `be3e8833…efaa` | `be3e88336389bc62c40413785e6ffb4a572e1dbd006d7cf3dfbc962f8184efaa` | freeze_md 5c40fb9d, ruling 870895a5, scout 13e44289 (prev bfb1b7f3), holdout 74507e1a, prereg ACCEPT 9a987a77 = disk; status FROZEN_FREEZE_ONLY_AWAITING_CONDUCTOR_ACCEPT_IMPLEMENT_GO; verdict domain DESCRIPTIVE/ITERATE/INCONCLUSIVE; effective_n_games 31 (dev-grade) | n/a | [V] |
| D | `P/EXT_K1_LEGGING_AUDIT/MANIFEST.sha256` | `5e8f7906` | `5e8f79063f132fe2db97ad3ecff5fea463d429f167abed09c58398a87fcadf01` | `sha256sum -c` 9/9 OK; SOURCE_PINS e58e6568 38/38 path pins = disk | n/a | [V] |
| D | `/workspace/EXT_K1_authentic_pins_2026-10-03.tgz` | `0f8f5297` | `0f8f529733bfd1ccb01b36f312cdc20865cc2811c04dcd3c812d50c67295db38` | 38 files; inner MANIFEST a041561e all OK; part-00 3fd70f7b + part-01 1f8b2ac1 concat = 0f8f5297; PARTS.sha256 a92df01d | n/a | [V] |
| D | `P/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` (governing ruling) | `870895a5` | `870895a58e80fd1442d0ce97e42df02426bf7e38f64dcd091efc6fbf26b74ebf` | inputs brief 13e44289 / freeze 15e2d2e4 = disk. **Clerical:** issued_et 2026-10-03T16:10:00-04:00, file mtime 16:06:39 ET; Conductor confirmed clerical (also on disk in ACCEPT 02129007 conditions) | n/a | [V] (clerical note) |
| D | `governance/astra/SCOUT_EXTERNAL_HUNT_2026-10-03.md` (scout brief) | `13e44289` | `13e442892d27466f3ee3082509a47ac9706c7f3448aa079de798bec8cb1a1dfb` | edited bfb1b7f3 → 13e44289 | `governance/astra/_prev/bfb1b7f3….SCOUT_EXTERNAL_HUNT_2026-10-03.md` self-hash OK | [V] |
| E | `P/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.md` | `d69a4f62…acbce` | `d69a4f627cb420b59bbc961b072d28242faeb9d21d5d29b9f90a77f6825acbce` | in MANIFEST; = json freeze_md | n/a | [V] |
| E | `P/VARIANTS_EXT_K2_OPTIMISM_TAX_DEPENDENCE_STRESS_FREEZE_2026-10-03.json` | `025a01a1` | `025a01a121e5b3a64a0b683a8030f9cbd1681f132365dadb419377d09d71ff6c` | 29 embedded full shas: K1 md/json/ACCEPT, Clock e7424a13/dc54e3da, bundles, Becker manifest, band registry 0860cbe2, holdout, prereg = disk; status FROZEN_FREEZE_ONLY_AWAITING_CONDUCTOR_ACCEPT_IMPLEMENT_GO | n/a | [V] |
| E | `P/EXT_K2_OPTIMISM_TAX/MANIFEST.sha256` | `3478b405` | `3478b4058681992109142bcde3ff87bd91c7e523092ba367d96d18afae693fe5` | `sha256sum -c` 11/11 OK; SOURCE_PINS 5133c826 50/50 path pins = disk | n/a | [V] |
| E | `/workspace/EXT_K2_authentic_pins_2026-10-03.tgz` (cloud bundle) | `963f7663` | `963f7663a74527db38479bbf4a253870bd5dc6f99c8f85b70750d3600c65907f` | 20 entries; inner MANIFEST 2e91d48f all OK; DEPENDS_ON 371597f1 → K1 0f8f5297; **no Becker bytes** (file list checked: governance packets + K1 PARTS only) | n/a | [V] |
| E | `astra-capture/external/ext_k2_becker_boxonly_2026-10-03/BECKER_BOXONLY_PIN_MANIFEST.json` | `fd5e1053` | `fd5e10531f488f30baf05e2dd6f17c8f8823603ecbae457170dbbde66126fb95` | 38/38 path pins = disk; **license [U], box-only, never bundled** | n/a | [V] |
| E | `P/CONDUCTOR_COMMISSION_EXT_K2_2026-10-03.json` | `1f2c7f68` | `1f2c7f68396131d65ef31e492355c2937a9a0a91fb6cdf67c7d66e220f0b51f5` | Clock e7424a13 / dc54e3da = disk; ruling_ref 870895a5; filed retro ("16:36 EDT, filed retro 16:5x") | n/a | [V] |
| E | `P/CLOCK_PROVENANCE_BECKER_ARCHIVE_2026-10-03.md` / `.json` (embedded support) | (embedded) | `e7424a130e95b72d288d567ef75b00804672b29b15bd93889aafb0722fd84d80` / `dc54e3dae4bbeeffc0e1c792bd769a2d63daee02a974dbff03d04da8780eebc3` | = K2 json clock_audit + commission | n/a | [V] (support) |
| F | `P/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md` | `676ba2fa…c130` | `676ba2faf0d877fa2f06dc4f2b247b9c7541188c0f9c7de17a622e6502eac130` | verdict **CLEAR** (advisory; DESCRIPTIVE/ITERATE/INCONCLUSIVE only); 7/7 embedded full shas = disk | n/a | [V] |
| F | `governance/astra/ADVERSARY_RISK_REGISTER_2026-09-22.md` | `1aecfd36` | `1aecfd366f8f9024be0f1393903812439a448ea5bf5585e4d21616874b1beab9` | chain 30eb735a → 537408cc → 1aecfd36 (mtime 17:08:57 ET) | `_prev/30eb735a….ADVERSARY_RISK_REGISTER_2026-09-22.md` self-hash OK; **no `_prev` of 537408cc anywhere** | [V] |
| F | (risk register intermediate bytes) | `537408cc` | — | not on disk (`find /workspace/lab -name '*ADVERSARY_RISK_REGISTER*'` → current + 30eb735a only) | none | **MISSING (register is not frozen; recorded, no rule breach)** |
| G | `P/ADVERSARY_CARD01_AMENDMENT_B_REVIEW_2026-10-03.md` | `271ec099…8f01` | `271ec099481ca35a57e4605b28abeff78d2660b6fd2657044666d45bcb728f01` | verdict ADVISORY_FLAGS; 7/7 embedded full shas = disk; = Amendment C lineage / Conductor ACCEPT 2225c3fa / gap record authority | n/a | [V] |
| G | `P/card01_hybrid_forecast/MANIFEST.md` | `f22df25b` | `f22df25bdebd300bfa51f557c940270212475edce6371b2ccaefb4204ce9e427` | = LEDGER "post-register re-hash"; prior 16f96d3d (LEDGER hash register + public extract) | **no copy of 16f96d3d anywhere**; `.pre-20260925T001140Z` = 4a757483 (an older version) | [V] (current) |
| G | (MANIFEST.md prior bytes, AF-9) | `16f96d3d` | — | per Conductor ruling: index file, low materiality | none | **UNVERIFIED_BYTES_MISSING** |
| H | `P/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_C.md` | `cc75f096…f0f0` | `cc75f09614ad285756fd7cb7f7a5c2ce4e711b5adb98102c2dd043ccfc1af0f0` | answers 271ec099; lineage base c3172446, A 4e36d0db, B ee6af37c, ACCEPT-B 74c5d49c, script 049368f9, decision pkt c0c1aa66 (at drafting) = disk; status AWAITING_CONDUCTOR_ACCEPT | n/a | [V]; **registered PENDING** (see §5) |
| H | `P/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_B.md` (reconfirmed, parent) | `ee6af37c` | `ee6af37cef95f1e468d28e5b06750caaca8b1706ec11ed5cf5cdce460524c2c6` | unchanged | n/a | [V] |
| I | `P/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` | `d66c9eaf…81ef` | `d66c9eaf2988bf081fea3096d7052c20def651e813ec29f13906a626effe81ef` | diff vs c0c1aa66 = docs-only (§2) | `P/_prev/c0c1aa66…` + `P/_prev/ebdaea01…` both self-hash OK | [V] |
| I | `P/_prev/c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c.CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` | `c0c1aa66…2c` | `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` | pre-edit bytes (19,633 B) | self-hash OK | [V] |
| I | `P/_prev/ebdaea019fc119d29f96bd04095d64eb60d99ade1a3206d441b94b422431ef25.CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` | `ebdaea01…25` | `ebdaea019fc119d29f96bd04095d64eb60d99ade1a3206d441b94b422431ef25` | transient (changelog timestamp 17:14 wrong; superseded) | self-hash OK | [V] |
| J | `E/ELECTINDEX_GAP_2026-09-27_to_2026-10-03_UNMONITORED.json` | `38d36b73` | `38d36b73336d2031204f79dae700f9f79d29eeb490863f491ea6b35dc215b221` | pins 271ec099, fb29ae5c, 336eca8f, 70e5aba3 = disk; never backfill | `E/_prev/38d36b73…` self-hash OK | [V] |
| J | `E/ELECTINDEX_CAPTURE_RESTORE_2026-10-03.md` | `9cdca130` | `9cdca1301f4dc40846834fea3a92dacfe389790b604b0a966a1e9ed82e8134d9` | page 255acb38, JS 82b09d7c, CSV 4713b5c4, diff efb53b1f, flag 3e585f84, gap 38d36b73, derived 11354fa1 = disk; cites runner 41d67d40 (now `_prev`, see next rows) | `E/_prev/9cdca130…` self-hash OK | [V] |
| J | `E/METHODOLOGY_CHANGED_2026-10-03.flag.json` | `3e585f84` | `3e585f84fa5ba2c56748af6a02f539f61a45cac865a33035a2afe63efcc4da6e` | new 82b09d7c / prev = R0 caaff53e; fetched 2026-10-03T21:13:06Z; label POSSIBLE_R0_REGIME_CHANGE (now resolved by the R1 ruling, §6) | `E/_prev/3e585f84…` self-hash OK | [V] |
| J | `E/_prev/41d67d400c75630f33f21c8e2b1810dc7a138f6d2be65e33d7e43dfb8aac86b3.run_daily.py` | `41d67d40` | `41d67d400c75630f33f21c8e2b1810dc7a138f6d2be65e33d7e43dfb8aac86b3` | = restore note + daily_runs runner_sha256 (the 2026-10-03 17:13 run used these bytes) | self-hash OK | [V] (as `_prev`) |
| J | `E/run_daily.py` (live) | `41d67d40` | `4f0854e56265e10b2505a9f371260caa6eaddb57726244a4435e1a424a54d5c8` | edited 17:15:37 ET after the restore note; **re-adds the README GET** (see §6) | old bytes at `E/_prev/41d67d40…` (rule satisfied) | **MISMATCH** |
| J | `PRIV/card01-nh002-house/2026-10-03/races_summary.csv` (sha only) | `4713b5c4` | `4713b5c44ca5f6db6080a55e0843210d953a45ba53e727408c9e4d93eb82fdf9` | = restore note / daily_runs | n/a | [V] |
| J | `PRIV/methodology/2026-10-03.html` (sha only) | `255acb38` | `255acb38163549a5ad0709e859f0f1e8a81b6ac506931241658c1e6e7fef0a31` | = restore note / daily_runs | n/a | [V] |
| J | `PRIV/methodology_asset/2026-09-26_to_2026-10-03_eifc-info.js.diff` (sha only) | `efb53b1f` | `efb53b1f07202c78589a95632e267d57b423c434f0dacf55ee8f1943c198ea3f` | = restore note | n/a | [V] |
| J | `PRIV/methodology_asset/2026-10-03_eifc-info.js` (sha only; regime R1) | `82b09d7c…66cd` | `82b09d7c845c9d04c23d30e2a27441aaaf66606c98558e618a34db7201ac66cd` | = flag new_sha256 / daily_runs. **R1 raw verified** | n/a | [V] |
| J | `PRIV/methodology_asset/2026-09-25_eifc-info.js`, `2026-09-26_eifc-info.js` (reconfirmed, R0) | `caaff53e` | `caaff53e739413a8340f0addbec7136ec1995195291cab61889a94c1286ea87f` | = Amendment 03 R0 | n/a | [V] |

## 2. Item I: decision packet diff (`P/_prev/c0c1aa66…` vs current `d66c9eaf…`)

**Verdict: DOCS-ONLY, confirmed.** `diff` shows two pure additions (`11a12`, `204a206,209`), 5 added lines and 0 changed or removed lines. The added text carries only a path, shas, a timestamp and status words. No number, rule, threshold, universe, weight or knob changed. Verbatim:

```
11a12
> **Amendment C (pre-outcome, docs-only; pins Adversary AF-1/2/5/6/7/10/11; `AWAITING_CONDUCTOR_ACCEPT`):** `packets/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_C.md` (sha256 `cc75f09614ad285756fd7cb7f7a5c2ce4e711b5adb98102c2dd043ccfc1af0f0`)
204a206,209
> - **2026-10-03 17:12 ET (21:12Z): next version** (pre-edit bytes `c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c` saved byte-exact at `packets/_prev/c0c1aa66f104e3f102228a7a8e16f205977afbee63928f30a6954ec46707a82c.CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` under RULE-FROZEN-EDIT-PREV-BYTES-001; new sha256 is recorded outside this file, since a file cannot contain its own hash). Two changes:
>   - (1) Added the Amendment C pointer line under the Amendment B line (with Amendment C sha256 `cc75f096…f0f0`, status `AWAITING_CONDUCTOR_ACCEPT`).
>   - (2) Added this changelog entry. (A transient intermediate `ebdaea01…`, with a wrong timestamp in this entry, existed for under a minute; its bytes are kept at `packets/_prev/ebdaea01…` and it is superseded.)
>   - **No number, rule, threshold, universe, weight, knob, recommendation or result changed** in this file. The rule pins themselves live only in Amendment C.
```

- ebdaea01 → d66c9eaf differs only in the changelog entry: the timestamp "17:14 ET (21:14Z)" became "17:12 ET (21:12Z)", the hash-location wording changed, and the transient-intermediate sentence was added.
- The pointer line still reads `AWAITING_CONDUCTOR_ACCEPT` for Amendment C. That was accurate when written. The file is owned by Deep Research and was not edited by the Archivist.

## 3. Item I: repin of registers that listed c0c1aa66 (`rg -l c0c1aa66` over `governance/` and `astra-science/`, 21 files)

**Repinned (Card 01 registers):**

| register | type | action | old sha256 | new sha256 | `_prev` |
|---|---|---|---|---|---|
| `P/card01_hybrid_forecast/FROZEN_EXPERIMENT.json` | frozen register, edited in place | only `decision_packet_sha256_current` changed, c0c1aa66 → d66c9eaf (1-line diff, JSON valid). `decision_packet_lineage` was **not** edited, so c0c1aa66 remains there as the last historical entry | `44cb582fd6f4612574d1a0b58b2d4f24cdf421eddc61e32a681663bf1b16c910` | `8b716ef0ee2ed2daa5f533681ea6e4c77767094fd95e611b681f9f2807ef855c` | `P/card01_hybrid_forecast/_prev/44cb582f….FROZEN_EXPERIMENT.json` (saved first, self-hash OK) |
| `P/card01_hybrid_forecast/LEDGER_2026-09-24.md` | append-only ledger (MANIFEST status "Open") | appended section "Repin log", row RP1 (old c0c1aa66 → new d66c9eaf, reason, DR request, `_prev` path). The earlier hash-register and Key-pins rows are not rewritten; the first 13,171 bytes are byte-identical (`cmp`) | `d8ddfda72bdc6aaedd5627c78da99d6f360c48746b16c662d7ae3263a3d14fe1` | `ee9d12f75756cebd95e162bccc6ed50eecabff880bf40e7e555df4dcbbca1414` | `P/card01_hybrid_forecast/_prev/d8ddfda7….LEDGER_2026-09-24.md` (saved first, because the extract pins d8ddfda7; self-hash OK) |

**Not repinned: these pin the pre-edit bytes, which are preserved in `_prev`.**
- `P/card01_hybrid_forecast/LEDGER_HASH_REGISTER_EXTRACT_2026-09-24.json` (03f9c193; Steward). This is a point-in-time public anchor of the 2026-09-24 hash set. It is git-tracked in the astra-science clone, with an identical copy at `astra-science/lab/governance/…` and a runner_tree copy inside the PR64 run dir. Repinning would falsify the anchor. It also pins LEDGER d8ddfda7 and FROZEN_EXPERIMENT 44cb582f, both now preserved in `card01_hybrid_forecast/_prev/`.
- Other-seat packets: `P/ADVERSARY_CARD01_AMENDMENT_B_REVIEW_2026-10-03.md`; `P/CARD01_HOUSE_ONLY_PROSPECTIVE_FREEZE_2026-09-24_AMENDMENT_C.md` ("at drafting"); `P/CARD01_EXP2_CENSUS_GATECOUNT_FREEZE_KERNEL_2026-09-24.md`; `governance/astra/briefs/EDGE_RESEARCH_CARDS_01_02_FREEZE_ACK_2026-09-24.md`.
- The decision packet itself and `P/_prev/ebdaea01…` cite c0c1aa66 only as the pre-edit reference.
- Archivist historical receipts, frozen and not edited: `P/ARCHIVIST_CARD01_02_LINEAGE_AND_AMENDMENT_B_2026-09-24.md`, `P/ARCHIVIST_CONDUCTOR_RULINGS_RECORD_2026-09-24.md`, `P/ARCHIVIST_FORWARD_AMENDMENT_B_2026-09-24.md`.
- Append-only registry files, history kept: `registry/PACKET_INDEX.md` (L337) gets an appended repin row; `registry/STATUS_2026-09-24.md` is left as is.
- Steward sync records: `S/GAUNTLET_OVERSIZE_LANDING_LIST_2026-10-02.json`, `S/GAUNTLET_SYNC_2026-10-02.log`, `S/GAUNTLET_SYNC_2026-10-03.log`, `S/MD_BYTE_EXACT_BACKLOG_2026-10-03.tsv`, `S/_prev/e37f80f2….MD_BYTE_EXACT_BACKLOG_2026-10-03.tsv`. The next Steward sync will see new shas for the decision packet, LEDGER and FROZEN_EXPERIMENT.

## 4. Resolution notes

- **B (resolution, per Conductor as relayed by the dispatcher; no Conductor packet on disk [I]):** `S/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` is **current at 133302a4** [V]. The cited 7e389f32 bytes are unrestorable, and the Conductor accepts that. The **7 lost Examiner scratch outputs** (PR61 5dd5ea93 / f4571074; PR62 7f412f32 / 1f5d28dd; PR63 70c58bcc / 7317bfb2 / 24e62b49) are **accepted as lost**. Their SCORE and scorecard bytes are intact, and they will not be regenerated. This closes the receipt 0e479b7f MISMATCH and MISSING-scratch exceptions as RESOLVED_ACCEPTED. The 0e479b7f rows themselves are not rewritten.
- **A:** the ACCEPTED status of 9a2870db moves from [I] to [V] (6e4922d6). Run 19's 170 rows stay ABORTED_SUPERSEDED and excluded downstream.
- **D (clerical):** ruling 870895a5 has `issued_et` 16:10:00 ET while its file mtime is 16:06:39 ET. The Conductor confirmed this is clerical with no content effect, and that is also recorded on disk in ACCEPT 02129007.
- **G / AF-9:** `card01_hybrid_forecast/MANIFEST.md` 16f96d3d → f22df25b is registered **UNVERIFIED_BYTES_MISSING** per the Conductor ruling (index file, low materiality). The current file is f22df25b [V]. The `.pre-20260925T001140Z` in-place copies are a format deviation the Archivist accepted earlier; they were not mirrored to `_prev/` (copy-only, optional).
- **F:** risk register 537408cc has no `_prev`. The register is not frozen, so this is recorded and is not a rule breach.

## 5. Status registrations (as instructed; see §7 for on-disk ACCEPTs)

- EXT-K1 freeze (5c40fb9d / be3e8833): **AWAITING Conductor ACCEPT** per brief. Measurement-only legging-risk audit of Q6-000; verdict domain DESCRIPTIVE/ITERATE/INCONCLUSIVE on the dev-grade 31-game cohort; no KEEP or KILL of 000 and no retune.
- EXT-K2 freeze (d69a4f62 / 025a01a1): **AWAITING Conductor ACCEPT** per brief. Becker inputs are box-only while the license is [U]; the cloud bundle contains 0 Becker bytes.
- Card 01 NH-002-H Amendment C (cc75f096): **PENDING, not accepted** per brief. Amendment B ee6af37c and ACCEPT-B 74c5d49c stand.

## 6. Item J: ElectIndex (replaces the ElectIndex part of item G)

- **Observed (read-only):** `ps -p 453207` returned no process (rc 1). `electindex_scheduler.pid` still holds 453207. The scheduler log's last line is "2026-09-26T20:17:10Z … next run: 2026-09-27T20:17:00Z". Before the restore, the latest capture in the log was 2026-09-26 (JS 20:17:03Z, CSV 20:17:10Z). The fresh snapshot is 2026-10-03 17:13:02–17:13:10 ET. No ElectIndex process is running now. The Adversary flag (no same-day R0 monitoring since 09-27) is confirmed and is now **resolved by the restore**.
- **Archivist ruling (recorded):**
  - Methodology regime **R1 = eifc-info.js `82b09d7c845c9d04c23d30e2a27441aaaf66606c98558e618a34db7201ac66cd`** (raw verified), first seen **2026-10-03T21:13:06Z**. **R0 was `caaff53e…`**.
  - The change time cannot be attributed within the UNMONITORED window: after the last R0 capture on 2026-09-26, and no later than 2026-10-03T21:13:06Z. The server Last-Modified (2026-10-02 13:36 ET) is **[U]** and is **not** the boundary.
  - **Card 01 stays frozen.** Sensitivity rows (i)/(ii) of Amendment B (b) apply at decision. Gap-window snapshots are regime **UNATTRIBUTED**.
  - The scheduler is now a **server-side daily routine at 20:17 UTC**. `electindex_scheduler.sh` (018a3009) is **retired, not restarted**.
  - The optional README fetch is **OPTIONAL_NOT_CAPTURED from 2026-10-03**. The Monday terms/robots check is kept.
  - `run_daily.py` endpoints stay within the pin (Amendment 03 70e5aba3 and the source gate).
- **Conflict flagged:** live `run_daily.py` 4f0854e5 (edited 17:15:37 ET) adds README_URL to ALL_URLS and makes one README GET per run ("Conductor 2026-10-03: re-added"). The README is inside the Amendment 03 pin as an optional GET, so the endpoint stays within the pin. But re-adding it contradicts **OPTIONAL_NOT_CAPTURED** in the ruling above. The edit also embeds the R1 regime constants (consistent with the ruling) and changed the flag trigger from "vs R0" to "vs current regime R1". 4f0854e5 is recorded as MISMATCH against the cited 41d67d40 and is **not** indexed as the conforming runner. A Conductor/Archivist decision is needed. The 41d67d40 bytes, which made today's capture, are kept at `E/_prev/`.

## 7. Seen but NOT indexed (ambiguous or out of scope)

- **On-disk Conductor ACCEPTs that conflict with the brief's AWAITING/PENDING status:**
  - `P/CONDUCTOR_ACCEPT_EXT_K1_FREEZE_2026-10-03.json` `021290077cbbed277455145d2e56e1335f6ae331d56c2ad79d4d85b405559397` (issued 16:16:49 ET; verifies 5c40fb9d / be3e8833 / 5e8f7906 / 0f8f5297; it is pinned by the K2 freeze json and the Adversary review).
  - `P/CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` `d76779e1a309388e6bc7f401a2c992a3be2015ae81ba910b8f5655fb10472fc0` (16:50:38 ET; verifies d69a4f62 / 025a01a1 / 3478b405 / 963f7663 / fd5e1053).
  - `P/CONDUCTOR_ACCEPT_CARD01_AMENDMENT_C_2026-10-03.json` `2225c3fa0bea7c58cad59f52476f9fbe69e1d6fa813114a7557c748126dd2b1a` (17:14:08 ET; sha cc75f096).
  - All three re-hash, but they are held for confirmation and not indexed as acceptances.
- Related but uncited: `P/CONDUCTOR_MERGE_PR66_EXT_K1_2026-10-03.json` 9de0933b…, `P/CONDUCTOR_KICK_ADVERSARY_EXT_K1_PR66_DESCRIPTIVE_2026-10-03.json` 113c111a…, `P/CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` 0b68c4bf…, `P/CONDUCTOR_KICK_VARIANTS_CLOUD_EXT_K2_LAUNCH_2026-10-03.json` c8e4ff43…, the weather rulings and kicks 8c90e657… / 18ed1592… / dd1d7039…, `P/CONDUCTOR_KICK_SCOUT_EXTERNAL_HUNT_WHILE_BOX_IP_CLOSED_2026-10-03.json` 9c583e82…, scout freeze 15e2d2e4…, GV2 sync rulings, pins and merges, and MAXIMIZE_PIN files dated 10-02 20:50 → 10-03 16:55.
- `W/ROUTINE_CREATE_R2D_2026-10-03.json` 43d094ec… (with `_prev` d94a3815…) and `ROUTINE_PROMPT_R2D_2026-10-03.md`: these are r2d routine plumbing and were not in the brief.

## 8. Counts

- Master table: 49 rows. **[V] 46** (including 6 reconfirmed rows that are not re-appended: 9a2870db, 133302a4, launch_r2d af0f4db3, archive.sqlite 974ce4b5, Amendment B ee6af37c, R0 caaff53e; the item B row is [V] for bytes, while its resolution is [I]). **MISMATCH 1:** `E/run_daily.py`, cited 41d67d40 vs disk 4f0854e5; the 41d67d40 bytes are in `_prev`. **MISSING 2:** risk register 537408cc (no `_prev`, register not frozen) and MANIFEST.md 16f96d3d (UNVERIFIED_BYTES_MISSING per AF-9 ruling). **[I] 1:** item B resolution (no Conductor packet on disk).
- Embedded-pin checks: K1 SOURCE_PINS 38/38, K2 SOURCE_PINS 50/50, Becker manifest 38/38, K1 MANIFEST 9/9, K2 MANIFEST 11/11, K1 bundle inner manifest all OK, K2 bundle inner manifest all OK, Adversary reviews 14/14 full shas, Amendment C lineage 7/7. Self-field note on STOP_R2D (4d889a24 / 12bcc402).
- `_prev` rule checks: KALSHI_429_STOP a41d074e / abed68e7 / e55d6094 OK; decision packet c0c1aa66 / ebdaea01 OK; scout brief bfb1b7f3 OK; risk register 30eb735a OK and 537408cc absent; run_daily 41d67d40 OK; card01 MANIFEST 16f96d3d absent; repin `_prev` 44cb582f / d8ddfda7 written and OK.
- Repins: 2 (FROZEN_EXPERIMENT 44cb582f → 8b716ef0; LEDGER d8ddfda7 → ee9d12f7).
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.**

## Corrections (appended 2026-10-03 ~17:23 ET, Archivist rulings; §1–§8 above are unchanged)

- Pre-correction sha of this receipt: `dabc41ff55cdec5629dcc306769862b276e0e80d0d3fa3756c40181fbfb17b1a` (indexed in PACKET_INDEX). The post-correction sha cannot be written inside this file. It is recorded in PACKET_INDEX and STATUS_2026-10-03 as a new row.
- These corrections apply the Archivist's rulings on the round-1 ambiguities. Every check below was re-run on disk at the time of append.

### C1. Three on-disk Conductor ACCEPTs → ACCEPTED (supersedes §7 "held for confirmation")

The Archivist ruled that these are real Conductor stamps. They were issued before the FYIs reached the Archivist, and the brief was stale. Embedded pins were re-checked against the indexed shas:

| path | sha256 | issued (ET) | embedded pins | result |
|---|---|---|---|---|
| `P/CONDUCTOR_ACCEPT_EXT_K1_FREEZE_2026-10-03.json` | `021290077cbbed277455145d2e56e1335f6ae331d56c2ad79d4d85b405559397` | 16:16:49 | freeze_md 5c40fb9d (= indexed) OK; json be3e8833 OK; manifest 5e8f7906 OK; bundle_tgz and parts_concat 0f8f5297 OK | **ACCEPTED** [V], 0 mismatch |
| `P/CONDUCTOR_ACCEPT_EXT_K2_FREEZE_2026-10-03.json` | `d76779e1a309388e6bc7f401a2c992a3be2015ae81ba910b8f5655fb10472fc0` | 16:50:38 | freeze_md d69a4f62 (= indexed) OK; json 025a01a1 OK; manifest 3478b405 OK; cloud 963f7663 OK; becker fd5e1053 OK | **ACCEPTED** [V], 0 mismatch |
| `P/CONDUCTOR_ACCEPT_CARD01_AMENDMENT_C_2026-10-03.json` | `2225c3fa0bea7c58cad59f52476f9fbe69e1d6fa813114a7557c748126dd2b1a` | 17:14:08 | amendment cc75f096 (= indexed) OK; lineage Amendment B ee6af37c OK; adversary 271ec099 OK; script 049368f9 OK | **ACCEPTED** [V], 0 mismatch |

- File mtimes equal the issued times. EXT-K1 and EXT-K2 status AWAITING → ACCEPTED. Card01 Amendment C status PENDING → ACCEPTED.

### C2. run_daily.py: runner indexing corrected (supersedes the §4/§8 MISMATCH)

- **CURRENT runner:** `astra-capture/card01-nh002-house/run_daily.py` `4f0854e56265e10b2505a9f371260caa6eaddb57726244a4435e1a424a54d5c8`. The Archivist accepted the Conductor's README re-add. Authority is **[I]**: a Conductor message of 2026-10-03 17:09 ET with no packet on disk at the time of the ruling. Line 4 cites "Conductor msg 2026-10-03 17:09 ET"; that line was already present in 41d67d40 as the restore authority. Line 13 reads "Conductor 2026-10-03: re-added" with no time. README is the optional fetch inside the Amendment 03 pin.
- **Capture runner of 2026-10-03 17:13 ET:** `41d67d400c75630f33f21c8e2b1810dc7a138f6d2be65e33d7e43dfb8aac86b3`. `_prev/41d67d40….run_daily.py` exists and self-hashes OK. RULE-FROZEN-EDIT-PREV-BYTES-001 is satisfied.
- **OPTIONAL_NOT_CAPTURED is corrected:** it applies **only to the 2026-10-03 capture**. README capture resumes from the next daily run under its own `METHODOLOGY_CHANGED_README` change flag.
- **Endpoint check of 4f0854e5: PASS.** There are exactly 6 fetch() calls, all to pinned endpoints: METH_URL `https://electindex.com/forecasts/`; METH_ASSET_URL `https://electindex.com/wp-content/themes/electindex/assets/forecasts/eifc-info.js`; README_URL `https://raw.githubusercontent.com/ElectIndex/26_us_forecast_data/main/README.md` (same as the pinned README in the old `electindex_capture.sh` L32 and the capture-log header); CSV_URL `https://raw.githubusercontent.com/ElectIndex/26_us_forecast_data/main/output/races_summary.csv`; TERMS_URL `https://electindex.com/terms-of-service/` (Mondays); ROBOTS_URL `https://electindex.com/robots.txt` (Mondays). No other URL appears. curl runs without `-L`, so redirects are not followed. A README host guard limits it to raw.githubusercontent.com, and Kalshi hosts are refused.
- Seen after the ruling, not indexed here: `P/CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` `20605d1afbab593876a6d7114d8dbb23ba6b412561a9f6b06f5c7641995d9a22` (issued 17:20:33 ET). It states "runner_current: run_daily.py 4f0854e5 (10-03 capture by 41d67d40 in _prev)" and "RE-ADD one daily README GET, no redirect following, same host only; hashed with its own METHODOLOGY_CHANGED flag". It agrees with C2. The authority stays [I] as ruled; upgrading it to [V] against this packet is held for the Archivist.

### C3. FROZEN_EXPERIMENT lineage note (no further edit)

- `P/card01_hybrid_forecast/FROZEN_EXPERIMENT.json` `8b716ef0…`: the `decision_packet_lineage` list still ends at c0c1aa66 and is left as is. **The current pin is the `decision_packet_sha256_current` field = `d66c9eaf2988bf081fea3096d7052c20def651e813ec29f13906a626effe81ef`.** The file was not edited again.

### C4. Related packets indexed (read-only; packets not edited)

- Checks: sha256 on disk, then embedded-pin resolution, then `_prev` for any frozen edit, then a duplicate check against PACKET_INDEX (0 of 36 present before this append).
- `P/CONDUCTOR_RULING_SCOUT_EXTERNAL_HUNT_2026-10-03.json` `870895a5…` was **already indexed in round 1**. It is a duplicate and gets no new row.

| path | sha256 | mtime (ET) | embedded-pin check | `_prev` | tag |
|---|---|---|---|---|---|
| `P/CONDUCTOR_KICK_ADVERSARY_EXT_K1_PR66_DESCRIPTIVE_2026-10-03.json` | `113c111ad6e1bc02d0ff413945f5364038bf8cc4d4128be542a7ac3ed4beab7b` | 2026-10-03 16:56:01 | merge 09b56273 resolves (git object) | n/a | [V] |
| `P/CONDUCTOR_KICK_COLLECTOR_WEATHER_R2E_GATE_2026-10-03.json` | `18ed1592ff92d302d198bae25a962ca84ffd5c9bff3fe0dbaac586b5f414c046` | 2026-10-03 14:55:33 | abed68e7 OK; fe335ca9 OK; cd114dda = agent id (non-file) | n/a | [V] |
| `P/CONDUCTOR_KICK_SCOUT_EXTERNAL_HUNT_WHILE_BOX_IP_CLOSED_2026-10-03.json` | `9c583e82aec1c5d622f222875c19c1edc5f4c11de4908fe32f503494aa7f60c9` | 2026-10-03 15:53:59 | no sha pins; refs by filename resolve | n/a | [V] |
| `P/CONDUCTOR_KICK_VARIANTS_CLOUD_EXT_K2_LAUNCH_2026-10-03.json` | `c8e4ff43f86cdb0f04d08f0e89cbed68c657fc637ccae40ac6ad9a02773f4292` | 2026-10-03 16:56:01 | refs by filename (EXT-K2 freeze, k2_upload tgz) resolve | n/a | [V] |
| `P/CONDUCTOR_MERGE_PR66_EXT_K1_2026-10-03.json` | `9de0933b8ec8ade5cbb89d5372116fb76048e30007af1b8f0e09f17fbae28deb` | 2026-10-03 16:54:08 | merge 09b56273 (parent 761eaaed, committed 16:54:01 ET) verified in /workspace/v67/repo; head 7415447c verified in /workspace/v66/repo; a73a90e0 = constancy value, Adversary-reproduced (non-file); result DESCRIPTIVE, counts_toward_keep false | n/a | [V] |
| `P/CONDUCTOR_PIN_GV2_SYNC_V3_2_REV5_2026-10-03.json` | `c2bb096113a62cfb84c9574437b2a9d957921fd6266d8ea7f4b1f977298c6157` | 2026-10-03 11:06:13 | proposal 7d448ae3 OK; rev5 fce33b3b OK (now `steward/_prev/`); classifier d68e5591 recomputed from fce33b3b OK; 785c99ff verified; oversize v2 5cd0595c OK, supplement efe55738 OK; clerical skew issued 11:08 vs mtime 11:06:13 | rev4 4efc4caa `_prev` OK | [V] |
| `P/CONDUCTOR_PIN_GV2_SYNC_V3_2_REV6_2026-10-03.json` | `9f30783437172fd3c6ebeee9a535bd0c0089f07fbe54725f1b4024b1eaf9cb34` | 2026-10-03 15:09:31 | proposal 04d15c33 OK; rev6 5d1889f6 = current `steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.2.md`; classifier 21ed9577 recomputed OK; clerical skew issued 15:10 vs mtime 15:09:31 | rev5 fce33b3b `_prev` OK | [V] |
| `P/CONDUCTOR_RULING_EXT_K1_N6_UNDEFINED_DELTA_2026-10-03.json` | `0b68c4bf218e7f85fa8af760ebcf5424d4e77262e62a5d71c43e9a5d2b929291` | 2026-10-03 17:06:01 | Adversary 676ba2fa OK; prospective only, no effect on PR66 | n/a | [V] |
| `P/CONDUCTOR_RULING_GV2_SYNC_PAUSE_AFTER_1050_DRIFT_2026-10-03.json` | `f195d558e3e1aace911ac191f7ab778d761e1e174d575f4210e4b62cef474467` | 2026-10-03 10:58:37 | v3.1 df2f54a6 OK; classifier 7bda943b recomputed OK; PM-003 box blobs d61d950f / 2c8b5ab5 = git hash-object of `lab/data/DATA-PROV-PM-003/provenance/` files and = blobs on GV2 785c99ff; drifted main blobs 987bf95f / a1ea1c6c present at GV2 5cba80f8 / 76883e2c; clerical skew issued 10:59 vs mtime 10:58:37 | 4efc4caa `_prev` OK; 299c2ef5 `_prev` OK | [V] |
| `P/CONDUCTOR_RULING_WEATHER_BOX_IP_CLOSED_AFTER_R2E_429_2026-10-03.json` | `dd1d70396472a72fce2bad5233ba0190f5df4c14568d9b7746bf282ef892b2dc` | 2026-10-03 15:53:59 | b33ada1c OK; e55d6094 OK; BOX_IP_KALSHI_CLOSED | n/a | [V] |
| `P/CONDUCTOR_RULING_WEATHER_SILENCE_AFTER_R2D_429_2026-10-03.json` | `8c90e6577559001a9c7b41bf17f14a6fe2058bd9c93af02e10f2dc36d0a08414` | 2026-10-03 09:50:17 | fe335ca9 OK | n/a | [V] |
| `P/CONDUCTOR_SUPERSEDE_PAUSE_GV2_SYNC_2026-10-03.json` | `e69d1de87871ea58611122e87fb8f13bacd56bc7e191acff2e05b794984ac12b` | 2026-10-03 12:48:30 | f195d558 OK; c2bb0961 OK; fce33b3b OK | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-02_2050ET.json` | `465fcc79ff467251340f582c6fe48a02574dce327184fc950435e5643d251ee8` | 2026-10-02 20:51:46 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-02_2050ET.md` | `f155239046891b2e6435fa634efaefc979717357201057f2021a4578a894a14b` | 2026-10-02 20:51:46 | fe335ca9, 9a987a77 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-02_2150ET.json` | `6b9bfbbeabf73908d2fc9e8d4fe53a414d67a3f8811ff34f356cf3d5b9755a3e` | 2026-10-02 21:51:21 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-02_2150ET.md` | `bbfd929159e6e3dcab3f084f8e31b22790e5a59edfa9dbca7275b2241f604181` | 2026-10-02 21:51:21 | fe335ca9, 9a987a77 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_0848ET.json` | `064d6ca81b405ed6c8a46868ee0742ae235a128b113b0c43abdfa1f1501d438b` | 2026-10-03 08:49:10 | fe335ca9, a41d074e, af0f4db3 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_0848ET.md` | `89f709b0596ccfdfafc0d54a9d9ec9d6dd688467c72eaffec60f5d53786a417d` | 2026-10-03 08:49:10 | fe335ca9, af0f4db3 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_0946ET.json` | `fa96ef06463e11c55f8e0b5205f4f34159ae6cc6ae2a9293df34942909f679ce` | 2026-10-03 09:49:17 | fe335ca9, af0f4db3, abed68e7, c9341de0 OK; b361017c = GV2 commit (sync-20261003-0844 head) verified; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_0946ET.md` | `0d672912a81dbf72b2ea58b653720b824d99c2782987011f64dbd9672dac9432` | 2026-10-03 09:50:17 | fe335ca9, abed68e7 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1055ET.json` | `6db6b4eef15cb9326fe94b1d2299252d36f9bcabdc261220f9c422181e3777c5` | 2026-10-03 10:56:16 | fe335ca9, abed68e7 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1055ET.md` | `b0ea1c71c1dab72dd47308e95103a6ca4ddbda99135d4951b4f627187fe95074` | 2026-10-03 10:56:16 | no sha pins; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1145ET.json` | `8a4e2d0a5511e12416a2158a746112ba010f08a57d36e900e8a47978fa1f724c` | 2026-10-03 11:47:06 | fe335ca9, abed68e7 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1145ET.md` | `64fd51c04e153a3d0c6dcb73914acdb22d65ecafa53712c329ca434ba8f94163` | 2026-10-03 11:47:06 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1246ET.json` | `258a957efa10bcf53e4cbf0fb24a2088d3cbe2531259cc7fbcaac4de7a05e683` | 2026-10-03 12:47:42 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1246ET.md` | `71de4e3b27acc552c870da77460b18428e2473e979e68e87e40dc5d85b5f6f78` | 2026-10-03 12:47:42 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1351ET.json` | `49606cb4b436b1b842d603ab24b5fa23e31bc5431c5a57af6358abd5bce38097` | 2026-10-03 13:52:58 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1351ET.md` | `f90fafb8efaadbe5daa3a860b6390ce19756217f9436b5c7f3ec64d13828e4d6` | 2026-10-03 13:52:58 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1453ET.json` | `ef299576c93e439fcf5f224098a647f4d35d9847d56a6b3ba95ef262b18d0b7a` | 2026-10-03 14:55:33 | fe335ca9 OK; cd114dda = agent id (non-file); scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1453ET.md` | `a82d523bc364f892043753ae572eedcc2e3fe901e908c031c2b5d6c92db4307a` | 2026-10-03 14:55:33 | fe335ca9 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1551ET.json` | `ccf32b36ddb9487adcbe0b172d976abb5261b0c95a08fe516088e9138e8a25f7` | 2026-10-03 15:53:59 | fe335ca9, b33ada1c, e55d6094 OK; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1551ET.md` | `f48e1e77b4fa455eef36fdd6f5720545878207623ce37b73c01c5870ab9db632` | 2026-10-03 15:53:59 | no sha pins; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1655ET.json` | `079fb999af49f39bb2848678ab64aa465888a5e18065d3859edd780d3fb24176` | 2026-10-03 16:56:01 | merge 09b56273 resolves; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MAXIMIZE_PIN_2026-10-03_1655ET.md` | `7dba2e3c2cc7370849dd356ab0ef03492d9c1173bf8c39115ef3ee61c4e6cc91` | 2026-10-03 16:56:01 | no sha pins; scoreboard text "Q6-000 KEEP +6.90%"; KEEP/KILL only as forbidden terms | n/a | [V] |
| `P/MERGE_GV2_PR2_COMBINED_BYTE_EXACT_2026-10-03.json` | `10a3c5634f5980cda52614c63e42fbb5769fa2c93dfed195ff74594b8f8dbc21` | 2026-10-03 15:05:23 | merge c19b9232 (parent 785c99ff, committed 15:05:12 ET), head 1d89c195 verified in /workspace/tmp/gv2pr2; manifest 05f2b98a = `GV2_LANDING_MANIFEST_20261003T144419-0400.json`; 5cd0595c / efe55738 OK; clerical skew merged_et 15:08:00 vs commit 15:05:12 / mtime 15:05:23 | n/a | [V] |
| `P/MERGE_GV2_PR3_DELETE_STATUS_JSON_2026-10-03.json` | `62890c50f8add9dcd941e5374bb6778c49307024c0332f8f1e48f65c774f1324` | 2026-10-03 15:08:22 | merge 25f23a24 (parent c19b9232, committed 15:08:15 ET), head 90f3bf65 verified; clerical skew 15:09 vs mtime 15:08:22 | n/a | [V] |

- Frozen-edit chain for `steward/GAUNTLET_SYNC_ROUTINE_PROMPT_v3.2.md`: rev4 4efc4caa → rev5 fce33b3b → rev6 5d1889f6 (current). Both prior versions are in `steward/_prev/`. OK.
- Clerical skews (issued/merged time later than mtime by ≤3 min) are recorded, not mismatches: GV2 PAUSE, REV5, PR2, PR3, REV6.
- Non-file refs: a73a90e0 is a constancy value reproduced by the Adversary; cd114dda is an agent id.

### C5. Seen after round 1, not indexed (outside ruling scope; shas only)

- `P/EXAMINER_READY_NOT_SCORED_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` `490112654a87699ea33bc60a60c05954428ecc41d0a31ac54556e89e3971b00f` (17:18:32 ET)
- `P/EXAMINER_SCORE_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` `0e5b10605798b45d69fde326e06fa1b9be52642dd4c64b28f79657b4d68edd5b` (17:19:13 ET): verdict **DESCRIPTIVE**, keep_available false, kill_of_q6000_available false. Gross Δ* −0.000205, 95% CI [−0.000577, 0.000188].
- `P/EXAMINER_SCORECARD_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.md` `b5e08bf8088a973c0f9919834b03593d8dc850cb9d875ba352fd9d9bec9a5958` (17:19:36 ET)
- `P/CONDUCTOR_ACCEPT_EXAMINER_SCORE_EXT_K1_2026-10-03.json` `530cca949ba4246602c853467bce5a7450be57e8e2815dba1590235d4e6a0fd5` (17:20:33 ET): its pins b5e08bf8 / 0e5b1060 / 49011265 match disk; verdict DESCRIPTIVE; "no change to Q6-000 KEEP; no gate adoption".
- `P/CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` `20605d1a…` (see C2).

### C6. Counts after corrections

- Round-1 MISMATCH (run_daily) is RESOLVED by ruling: 4f0854e5 is CURRENT [I], and 41d67d40 is the capture runner [V].
- Round-1 MISSING stays as before: 537408cc and 16f96d3d (AF-9).
- ACCEPT pin checks: 3 of 3 ACCEPTED; 14 embedded pins checked, 0 mismatch.
- C4: 36 indexed, **36 [V] / 0 MISMATCH / 0 MISSING**, plus 1 duplicate skipped (870895a5).
- KEEP/KILL/cemetery: no new KEEP, KILL or CEM. EXT-K1 PR66 is DESCRIPTIVE (Examiner score and Conductor accept on disk); it is not a KEEP. Box-IP Kalshi is CLOSED (dd1d7039), which is an operational state, not a cemetery event.
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%.**

## D. Authority upgrade + EXT-K1 score chain (appended 2026-10-03 ~17:25 ET, Archivist yes-to-both; §1–§8 and Corrections C1–C6 unchanged)

- Receipt sha before this section: `e19d217888499cebbbed0c6a9075f890e3edf85bf8815efbf6a9768d02ded468`. The post-D sha is recorded in PACKET_INDEX and STATUS_2026-10-03.

### D1. run_daily.py authority [I] → [V]

- `P/CONDUCTOR_RULING_ELECTINDEX_README_READD_2026-10-03.json` `20605d1afbab593876a6d7114d8dbb23ba6b412561a9f6b06f5c7641995d9a22`. Issued 17:20:33 EDT (mtime 17:20:33). `ruling_message_et` reads "2026-10-03 17:1x EDT (Conductor -> Collector)". It is indexed now.
- Its embedded refs resolve:
  - `runner_current` "run_daily.py 4f0854e5 (10-03 capture by 41d67d40 in _prev)" = live `4f0854e5…` and `_prev/41d67d40…` (both re-hashed OK).
  - R0 `caaff53e…` and R1 `82b09d7c…` are both already indexed.
- Rulings recorded: README "RE-ADD one daily README GET, no redirect following, same host only; hashed with its own METHODOLOGY_CHANGED flag". terms/robots "KEEP Monday check (one GET each)". Other scope "unchanged; no Kalshi hosts; refuse dates after 11-03".
- **Authority of `run_daily.py` 4f0854e5 is now [V]** via 20605d1a, superseding C2's [I].
- Adversary R1 ruling, quoted verbatim from the file:
  > "r1_assessment":"Adversary: R0 caaff53e -> R1 82b09d7c display-only; named seats outside 92-race universe; Card01 stays frozen; gap labeled CHANGED_IN_GAP"
- Note: the "17:1x" message time is vaguer than the "17:09 ET" cited by run_daily line 4. The two are consistent, but the exact minute isn't fixed by the packet.

### D2. EXT-K1 score chain (read-only; sha256 on disk + embedded pins)

| path | sha256 | mtime (ET) | embedded-pin check | tag |
|---|---|---|---|---|
| `P/EXAMINER_READY_NOT_SCORED_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` | `490112654a87699ea33bc60a60c05954428ecc41d0a31ac54556e89e3971b00f` | 17:18:32 | ACCEPT 02129007, merge pkt 9de0933b, Adversary 676ba2fa, fee ruling 870895a5, N6 0b68c4bf, Adversary kick 113c111a, freeze md 5c40fb9d / json be3e8833, EXT_K1 MANIFEST 5e8f7906, SOURCE_PINS e58e6568, bundle tgz 0f8f5297, inner MANIFEST a041561e, template 56bcf626 / ad1dd283, REPORT f3552b58 all OK. Git: merge 09b56273 (parent 761eaaed, tree 622e4c93 = head 7415447c tree, lab tree 0d82000a, chain 7415447c←32e10492←3ab5cd59←761eaaed) verified in /workspace/v67/repo. EXAMINER_HOLD in repo 51e36811 (blob e5519d97) and orchestrator.py 1c629274 verified at 09b56273. Replay pins 5aba1bf3 / 641d0df3 / c1a0fd2d / 78b94ae5 / 9d56f5d3 / c390801b and UNIT_RESULTS c6825269 resolve. a73a90e0 is a constancy value (non-file). | [V] |
| `P/EXAMINER_SCORE_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.json` | `0e5b10605798b45d69fde326e06fa1b9be52642dd4c64b28f79657b4d68edd5b` | 17:19:13 | READY 49011265, template 56bcf626 / ad1dd283, merge 09b56273, N6 0b68c4bf, 870895a5, 5c40fb9d, 02129007, 5e8f7906, a041561e, f3552b58, fee manifest aa765876 / ADDENDUM_02 44a69092 all OK. Examiner scratch recompute_out e931e02f, recompute.py bde8cf13, sens_direct.py 270190cc re-hash OK in /workspace/tmp/examiner_scratch_ext_k1/. **Verdict DESCRIPTIVE**; keep_available false; kill_of_q6000_available false. | [V] |
| `P/EXAMINER_SCORECARD_EXT_K1_Q6000_LEGGING_AUDIT_PR66_2026-10-03.md` | `b5e08bf8088a973c0f9919834b03593d8dc850cb9d875ba352fd9d9bec9a5958` | 17:19:36 | READY 49011265 and SCORE 0e5b1060 (full) OK. Short refs 02129007, 5c40fb9d, be3e8833, 5e8f7906, 0f8f5297, a041561e, 676ba2fa, 9de0933b, 0b68c4bf, 870895a5, f3552b58, 56bcf626 / ad1dd283, aa765876 / 44a69092, 51e36811, 761eaaed / 7415447c / 622e4c93 all resolve. | [V] |
| `P/CONDUCTOR_ACCEPT_EXAMINER_SCORE_EXT_K1_2026-10-03.json` | `530cca949ba4246602c853467bce5a7450be57e8e2815dba1590235d4e6a0fd5` | 17:20:33 | verified.scorecard b5e08bf8 / score 0e5b1060 / ready 49011265 (full) = disk. Run record f3552b58 and Adversary 676ba2fa OK. bc-cc5ab6e2 is a cloud agent id (non-file). Verdict DESCRIPTIVE: "no change to Q6-000 KEEP; no gate adoption". | [V] |
| `/workspace/v66/REPORT.md` (EXT-K1 run record per ACCEPT_SCORE `anomaly_fix`; Variants box verify, PASS-with-notes) | `f3552b58d571be2147024e94e666831e036cb11f199214c53d0c6750b978c4d0` | 16:53:07 | head 7415447c and base 761eaaed verified. 5c40fb9d, be3e8833, 02129007, 0f8f5297, a041561e, 9d56f5d3, 5e8f7906 OK. Holdout 74507e1a and prereg 9a987a77 / 370dc31d resolve in the repo pins at 09b56273. Artifact shas 1594860c / 6fb24d90 / 947970df / c0d4d2a2 and constancy a73a90e0 are computed values, not files. Clerical: the text says "verified … about 16:47–17:10 ET", but the mtime is 16:53:07. | [V] |

- Cross-ref (already indexed, no new row): `P/ADVERSARY_EXT_K1_PRESCORE_REVIEW_2026-10-03.md` `676ba2faf0d877fa2f06dc4f2b247b9c7541188c0f9c7de17a622e6502eac130` (verdict CLEAR). Re-hashed OK. It is cited by READY, SCORECARD and ACCEPT_SCORE.
- No `_prev` applies to these files: no frozen edits and no `_prev` copies under `packets/_prev/`.
- Labelling note carried from READY: ACCEPT.verified.manifest 5e8f7906 is the packet-dir MANIFEST, and a041561e is the inner bundle MANIFEST. Both verify; this is not a digest mismatch.

### D3. Counts and scoreboard

- D: 6 new rows (1 ruling + 4 score-chain + 1 run record), **6 [V] / 0 MISMATCH / 0 MISSING**. 1 cross-ref (676ba2fa) is already indexed and gets no new row. About 50 embedded refs were checked; all resolve or are explicitly non-file.
- EXT-K1 PR66 = **DESCRIPTIVE** (Examiner-scored, Conductor-accepted). It is not a KEEP or a KILL, and there is no cemetery event.
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%.**
