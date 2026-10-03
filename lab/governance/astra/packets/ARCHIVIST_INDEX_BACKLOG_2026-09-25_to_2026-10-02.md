# ARCHIVIST INDEX: KALSHI backlog 2026-09-25 → 2026-10-02 (items 1–14)

- Archivist (registry seat). Written 2026-10-02 19:24:00 ET. Verify-and-record only: no scoring, no collectors or sims run, no orders, no PnL invented, no frozen or existing packet edited, no agent messaged.
- Paths are relative to `/workspace/lab/` unless absolute. `P/` = `governance/astra/packets/`, `S/` = `governance/astra/steward/`.
- Tags: **[V]** = re-hashed on disk now and equal to the cited sha. **[I]** = cited or inferred only, bytes not re-hashable. **MISSING** = bytes absent. **MISMATCH** = disk differs from cite.
- The sha256 of this receipt cannot appear inside it. See the PACKET_INDEX row appended with it and `registry/STATUS_2026-10-02.md`.
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.** Verdicts in this window: one KILL (FL-band H1, KXMLBSPREAD only; cemetery below) and ITERATE for trades-join, PR62 game-phase, PR63 WX-FL and PR64 scorability. None counts toward KEEP.

## 1. Master table (items 1–13, plus the item 14 box-side files)

| item | path | cited sha | on-disk sha256 | embedded-pin check | _prev check | tag |
|---|---|---|---|---|---|---|
| 1 | `P/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.json` | `a18f2ad2` | `a18f2ad2f704d10ec526ccd2808edf8088f88de307ff8b3fe9845fa14ddde05a` | 13/13 path pins match; 4 trades-join lab files absent from clone, stream-verified inside preserve tar f91ecb68 (restorable) | n/a (new file) | [V] |
| 1 | `P/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_TRADES_JOIN_2026-09-25.md` | `e3eeb1a0` | `e3eeb1a07fddc08824a02a78a68b7f4aba69d77d8cbe5edb0b970bc61c69a9d1` | matches SCORE | n/a | [V] |
| 1 | `P/CONDUCTOR_ACCEPT_EXAMINER_Q6S5_KXMLBSPREAD_TRADES_JOIN_ITERATE_2026-09-25.json` | `ac713e5f` | `ac713e5fcbdda218d98e88bf4faab340204d8ad47dc9f0613d3762feca69b50d` | pins a18f2ad2 + e3eeb1a0 = match | n/a | [V] |
| 1 | `(queue packet bytes 08aa54de)` | `08aa54de` | — | n/a | none | **MISSING (known; superseded by 7472b8ac per ACCEPT a5398129; never recreated)** |
| 1 | `P/CONDUCTOR_QUEUE_Q6S5_STRATEGY_FILL_FREEZE_AFTER_Q6S1_2026-09-25.json` | `7472b8ac` | `7472b8ac01fd906577c49eb4d96b8fd5dbb2d7766c5a87fa86e47b3bffad2c61` | match | n/a | [V] |
| 1 | `P/MAXIMIZE_PIN_2026-09-25_0220ET.json` | `f23653fb` | `f23653fbf0ac82e6dc66dcf058553057ea7bcafae069d7b35d5f31e04321a6c5` | match | n/a | [V] |
| 2 | `P/CONDUCTOR_MERGE_Q6S1_KXATPMATCH_INVENTORY_REPROOF_PR59_2026-09-25.json` | `ef037c2c` | `ef037c2c628f98a4db87fc05ffefb6a985ab525fcdfcd5ec84e003ef46f8098f` | merge_commit cb8957d7 squash, parent f349ffa8 in git [V] | n/a | [V] |
| 2 | `P/CONDUCTOR_KICK_EXAMINER_Q6S1_KXATPMATCH_INVENTORY_REPROOF_PR59_READY_NOT_SCORED_2026-09-25.json` | `d2652887` | `d2652887e0aa187ada8af96e96d6b0586e9ad938b0ebc19d2ab4d93f2e183803` | match | n/a | [V] |
| 2 | `P/CONDUCTOR_KICK_VARIANTS_Q6S5_STRATEGY_FILL_FREEZE_2026-09-25.json` | `dc19794b` | `dc19794bdb8e26c3a3f4fe86eadc9bec1b02db97d508fca9426e3c3eddfb6bc8` | match | n/a | [V] |
| 3 | `astra-capture/prospective/ADMIT1_OUTAGE_GAP_2026-09-27_to_2026-09-29.json` | `4f2a5e26` | `4f2a5e2693f809e592238c0bf58ecac93f982fb8809c98ca81e51a41d8a65198` | window 13:31:52Z→20:39:41Z = cited | n/a | [V] |
| 3 | `P/CONDUCTOR_RULING_ADMIT1_OUTAGE_GAP_WEATHER_CARD03_RELAUNCH_2026-09-29.json` | `ac7cfe63` | `ac7cfe63623ca342ab5b4285ff58382a8138b58fb6cd8e95310a5d30d90304f2` | embeds 4f2a5e26 = match | n/a | [V] |
| 3 | `P/CONDUCTOR_ERRATUM_CARD03_GAP_WINDOW_2026-09-29.json` | `31da5974` | `31da5974867ee6230928b641e4a939171bce44260a4b87ee9161ffc8f30477d9` | amends ac7cfe63; card03 gap start 2026-09-25T19:37:33Z | n/a | [V] |
| 3 | `P/EXAMINER_NOTE_C1_PIT_CLE_ADMIT1_GAP_NOT_SCORED_2026-09-29.json` | `(uncited)` | `fe5ba611574253d7d6daf07b01bfd6051788775a8261ea82d4e6ae14d19bc1e3` | embedded pins match; supports item 3 | n/a | [V] (uncited support) |
| 4 | `P/Q6S5_KXMLBSPREAD_STRATEGY_FILL_FREEZE_2026-09-25.md` | `9f50ba19` | `9f50ba19694083c774bbe2a6cff491d1a2f81ed3a6f9cc21a3641a938c84955d` | match; twin in Q6S5_KXMLBSPREAD_STRATEGY_FILL/ same sha | n/a | [V] |
| 4 | `astra-science/kalshi_q6s5_kxmlbspread_strategy_fill_lab_20260925/Q6S5_KXMLBSPREAD_STRATEGY_FILL/Q6S5_KXMLBSPREAD_STRATEGY_FILL_authentic_pins_2026-09-25.tgz` | `6602e07e` | `6602e07ef9b444b8b242086d0cb338025507d117aa0874f24e99390cd9d01993` | 277 files | n/a | [V] |
| 4 | `P/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_STRATEGY_FILL_2026-09-25.json` | `3cb00d36` | `3cb00d3637ee8653a395e9547b1f4bfed3fbb11eff6abac60f2937d3d282849d` | only non-disk refs 08aa54de + manifest eea20e2e | n/a | [V] |
| 4 | `P/VARIANTS_ACCEPT_PING_Q6S5_KXMLBSPREAD_STRATEGY_FILL_2026-09-25.json` | `860b808e` | `860b808e868acfae265dda0a925679cca0a91f8c7d12b07dd6bed09062fc6ae6` | only non-disk refs 08aa54de + manifest eea20e2e | n/a | [V] |
| 4 | `P/Q6S1_KXATPMATCH_INVENTORY_REPROOF_V2_BUNDLE/Q6S1_KXATPMATCH_INVENTORY_REPROOF_authentic_pins_v2_2026-09-25.tgz` | `62de476e` | `62de476ec3d27b64183d1eba0d223c2c5ad61a6bc8abffde9873f6e76a5e633e` | 41 files; sidecar .sha256 match | n/a | [V] |
| 4 | `P/Q6S1_KXATPMATCH_INVENTORY_REPROOF_V2_BUNDLE/PROVENANCE_NOTE.md` | `160bb6df` | `160bb6df8efa729468224c452fa9ad7bbc7dc6960c6b9acb0b85e6d52680fb16` | match | n/a | [V] |
| 5 | `P/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_2026-09-29.json` | `3486a2fe` | `3486a2fe71da0be40a3cb6202abcc30e1783515180e20f594b3c25b034414bef` | commit 12e760f5 in git [V]; results null | n/a | [V] |
| 6 | `P/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_FREEZE_2026-09-29.md` | `fb6540f5` | `fb6540f52ed5f819ccf6e80bf0cf7eb6d951e065416b9d550fead0c6d06043fa` | match | n/a | [V] |
| 6 | `P/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE/MANIFEST.sha256` | `901285ed` | `901285ed3d559e1a121197c1ee36ead3d8b40498dfd2b4888694fb077fe3c043` | 8/8 OK | n/a | [V] |
| 6 | `astra-science/kalshi_q6s5_kxmlbspread_fl_band_settled_tape_lab_20260929/pins/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_authentic_pins_2026-09-29.tgz` | `63b5d981` | `63b5d981bc06f684eebb69a8ac29394534f8ae52c101f3018557544f14e29857` | 101 files; pins/MANIFEST OK | n/a | [V] |
| 6 | `P/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_2026-09-29.json` | `eba1260f` | `eba1260f1ab901a223f3f0b5feb1ff6f023d9f8870c1e69e16007e93e12b3a40` | match | n/a | [V] |
| 6 | `P/r3_p3_fl_maker_taker/bands_registry_10c.json` | `0860cbe2` | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` | match | n/a | [V] |
| 6 | `P/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_FL_BAND_SETTLED_TAPE_FREEZE_2026-10-01.json` | `8e4fbac7` | `8e4fbac7d0426bc67c1f53fb8057a382fe46da738bd701cb970a9812a6dc2a3b` | match | n/a | [V] |
| 6 | `P/CONDUCTOR_RULING_Q6S5_FL_BAND_IN_SAMPLE_DEV_LABEL_2026-10-01.json` | `09763030` | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` | match | n/a | [V] |
| 6 | `P/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `469de237` | `469de2376ae413f66684df26c08656e705a7fb5a0a1d128a4270d789c841df32` | merge d7558fc4 in git [V] | n/a | [V] |
| 6 | `P/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `2e74f17b` | `2e74f17b1307b8b57f33a6475cd7ce8af48c470099478cadfb07877b0d70745f` | verdict KILL, ceiling ITERATE; scratch out/ JSONs MISSING | n/a | [V] |
| 6 | `P/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.md` | `1bdb1d9c` | `1bdb1d9c1e6272a4b95a5080e4681858859e69a053f69e32b9b85b7d9e44c386` | cites bf9aafa3 = on disk | n/a | [V] |
| 6 | `P/CONDUCTOR_ACCEPT_EXAMINER_KILL_Q6S5_KXMLBSPREAD_FL_BAND_PR61_2026-10-01.json` | `be235777` | `be2357773ca7a842e6896676e3ba0291f40ef8e0b8f997d46f7124d4b2705229` | pins 2e74f17b + 1bdb1d9c = match; erratum_noted WRONG per 546f62c9 (not edited) | n/a | [V] |
| 6 | `P/SIMULATOR_READY_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `8e8a1756` | `8e8a17566747cb29077c2f7abccb49640739ae873d3d5c20fbfa819bbde36e1b` | match | n/a | [V] |
| 6 | `P/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `0f8de7cd` | `0f8de7cd6b2187076e2bd8f914c4de51b3d8bfecdd59e324a41a9f030f5f26b6` | match | n/a | [V] |
| 6/8 | `P/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_GAME_PHASE_PR62_AND_ANNOTATE_be235777_2026-10-01.json` | `546f62c9` | `546f62c99f1268b14ddb612fe9891c7741e5bee7e8397cae32c75d86fbff65ae` | annotation_of_be235777 (be235777 not edited) | n/a | [V] |
| 7 | `P/C4_KXCPI_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `bcd27e06` | `bcd27e06f57f0e6b617ce318fb6d42da8c9b0a526816fbc4e41cef07a875154c` | realigned 21df2532→bcd27e06 | _prev/21df2532… self-hash OK | [V] |
| 7 | `P/C4_KXCPI_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `968a46e3` | `968a46e3733bc17e58c223ccc71525e5090ff7a1204b7c2222de4353a3940191` | realigned b72465d8→968a46e3 | _prev/b72465d8… self-hash OK | [V] |
| 7 | `P/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/SOURCE_PINS.json` | `509e2cf2` | `509e2cf29c701de29a63b8c3cad06a3a405ac30b1677cc04c680c91d65ceddd9` | realigned 4de33473→509e2cf2 | _prev/4de33473… self-hash OK | [V] |
| 7 | `P/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/FROZEN_EXPERIMENT.json` | `382009b9` | `382009b93b561f21e5942cf0aa5cfbc8ee21821ad4b89db66468bfbe7ad094dc` | realigned 802b40b3→382009b9 | _prev/802b40b3… self-hash OK | [V] |
| 7 | `P/C4_KXCPI_SETTLED_JOIN_HARNESS/DIGESTS.txt` | `a2754a86` | `a2754a8673bde8a82acb64226877e4f4d4b2d1a135f0b16d18ed7fed409083a8` | UNCHANGED; pinned by SOURCE_PINS + C4 Examiner READY/ACK/scorecard | annotated 0404abf5 reverted 19:14:46 ET; _prev/a2754a86… present | [V] |
| 7 | `P/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/DIGESTS.txt` | `e72add78` | `e72add7818b65edd32ee0132104611d166934688092c23fce762db4f0a5f8745` | UNCHANGED; pinned by SOURCE_PINS | annotated fffe42ef reverted 19:14:46 ET; _prev/e72add78… present | [V] |
| 7 | `P/scout_c4_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` | `b72465d8` | `b72465d809ccd208588ce13baa8749b8f5d1eedfb82abef47d261d84939b067f` | intentionally NOT realigned | n/a | [V] |
| 7 | `P/scout_atp_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` | `802b40b3` | `802b40b308724ae0980da123843d6a0655d087af2f162b3cc3a0f66d25e1d690` | intentionally NOT realigned | n/a | [V] |
| 7 | `S/RULING2_REALIGN_RECORD_2026-10-01.json` | `3bb36969` | `3bb3696927b87eca53011bf69b335130351d585c740ecaaad90320086a57f02a` | 4/4 records match disk; LI lists RESTORED_UNVERIFIABLE | n/a | [V] |
| 7 | `/workspace/steward_astra_science_preserve_20261001/FROZEN_PREV_RECORD_astra_science.json` | `9b0d2e89` | `9b0d2e89aa6938ea3e71c66a7cb1533e98a3526c0749a29a53e2d7f76332761f` | 14/14: _prev = old, current = new | 14/14 OK | [V] |
| 7 | `S/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md` | `7e389f32` | `133302a440281647f7589f29dad54882928c3d43253e77cf9bef78dbb6f5d578` | cited 7e389f32 = pre-append (HYGIENE §11.2); disk 133302a4 = post-append (HYGIENE §11.3; LI-verified) | NO _prev of 7e389f32 bytes anywhere | **MISMATCH; 7e389f32 bytes UNVERIFIED_BYTES_MISSING (unrestorable)** |
| 7 | `S/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.json` | `433ba206` | `433ba206a2961d56801b95551ae67ed6403da7cb5c1f83e6df9cf32ba7a262ac` | JSON twin; LI-verified | n/a | [V] |
| 8 | `P/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_FREEZE_2026-10-01.md` | `5beba803` | `5beba803f3f6d33410409acc23ad3b782be62dc8829a0f54584e1da8ac18575a` | match | n/a | [V] |
| 8 | `P/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE/MANIFEST.sha256` | `88af3bd7` | `88af3bd79ad37c6fa09cfbe1bcd516c72b8a35d2928ce04eeaec994b5c1233a1` | 8/8 OK | n/a | [V] |
| 8 | `astra-science/kalshi_q6s5_kxmlbspread_game_phase_settled_tape_lab_20261001/pins/Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_authentic_pins_2026-10-01.tgz` | `6576ee6c` | `6576ee6cf9f023137e4357270f228dd9a5d29e3dc1d5e7ced85384681f2a7ecc` | 121 files; pins/MANIFEST 3/3 OK | n/a | [V] |
| 8 | `P/VARIANTS_ACCEPT_PING_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_2026-10-01.json` | `7af58fa9` | `7af58fa9253629c3defdcc52a2198b7d858a2a2a1b00544d10b65bcb7497fa7d` | match | n/a | [V] |
| 8 | `P/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_GAME_PHASE_SETTLED_TAPE_FREEZE_2026-10-01.json` | `08d23b36` | `08d23b363d72b8c8599772ee6fc6736cb90f13e8ed814b12c59b58fd5c7dc91e` | match | n/a | [V] |
| 8 | `P/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `fa361354` | `fa361354aa284b36482b0c4a67715ff6cda63fcf70f2d0c535bd1f7bdc465d5b` | merge 749bc146 in git [V] | n/a | [V] |
| 8 | `P/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `1626e2d0` | `1626e2d0e19f0e8cf35fc7b3a9e551f489957dab8e48be2f35216fd36ebda693` | verdict ITERATE; scratch out/ JSONs MISSING | n/a | [V] |
| 8 | `P/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.md` | `00c3da8d` | `00c3da8d20a74d8baad8236eb94c43ca6a7d7cc681ad4b308a89884613a2d5ca` | match | n/a | [V] |
| 8 | `P/EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `e6c9ac56` | `e6c9ac56be33af2ccc7757409b3bd918034fd2c48a438fd749827cbbd186e4e6` | match | n/a | [V] |
| 8 | `P/SIMULATOR_READY_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `98d0e625` | `98d0e62581ec54a3cbac60d6fb6d1cc538e765d0ea733360993b5d129082f661` | match | n/a | [V] |
| 8 | `P/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_GAME_PHASE_SETTLED_TAPE_PR62_2026-10-01.json` | `006d7d5d` | `006d7d5dc08babfb352d94cdde2460d8d49726d87d66d15d05c7cbd7acc2e90a` | match | n/a | [V] |
| 9 | `P/VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.md` | `370dc31d` | `370dc31df17191446013b6cebb52d44ee8346f47d2f5b543a1c73049ba52c063` | all embedded pins match | n/a | [V] |
| 9 | `P/VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.json` | `a76d2673` | `a76d2673f85a817af435deb2f70ec8b421ac3d8d2eb57f601eb4da39927d9865` | all embedded pins match | n/a | [V] |
| 9 | `P/CONDUCTOR_ACCEPT_VARIANTS_HOLDOUT_PREREG_ADDENDUM_Q6S5_KXMLBSPREAD_UNTOUCHED_CAPTURE_2026-10-01.json` | `9a987a77` | `9a987a77e6cd6293ddaeb14fadbf33a25c1a6cc392af25f46eaaaaae33ebb273` | pins 370dc31d/a76d2673 = match | n/a | [V] |
| 10 | `P/CONDUCTOR_RULING_VARIANTS_WX_FL_PREFREEZE_2026-10-01.json` | `0e37f91b` | `0e37f91b60289084f4e660b74bcb12a04f83f66fc93410add3a26baf0dd9f6af` | match | n/a | [V] |
| 10 | `P/WX_FL_KXHIGH_SETTLED_TAPE/WX_FL_KXHIGH_SETTLED_TAPE_FREEZE_2026-10-01.md` | `aec5b760` | `aec5b760f8539ea9f30aa1c3601534dccf78a62ee2026cb939842656e3c20e0f` | 2 explained drifts: collector.py 7bd1bddb→1a3166c4 (item 12, _prev OK); logs/kalshi_429.jsonl 9b9a2d5e→696b48a6 (live append log; 9b9a2d5e bytes kept in gap_log/) | n/a | [V] |
| 10 | `P/WX_FL_KXHIGH_SETTLED_TAPE/MANIFEST.sha256` | `21beb0b5` | `21beb0b51f33124e33541f36e36a1bde86c5a79100d8d1a4eea1a106a11af519` | 17/17 OK | n/a | [V] |
| 10 | `astra-science/wx_fl_kxhigh_settled_tape_lab_20261001/pins/WX_FL_KXHIGH_SETTLED_TAPE_authentic_pins_2026-10-01.tgz` | `febc74af` | `febc74af09b06db83fb686e904d6f3e305fe30414e4c4f67c05705f0de597807` | 56 files; = git blob; pins/MANIFEST 4/4 OK | n/a | [V] |
| 10 | `P/WX_FL_KXHIGH_SETTLED_TAPE/snapshot/archive.sqlite` | `d20d5e7d` | `d20d5e7d0cedc79ed77c92e905b2824f0ca1d79f8e524635bfd3a8f0e3c6eae2` | match | n/a | [V] |
| 10 | `P/WX_FL_KXHIGH_SETTLED_TAPE/SNAPSHOT_PROVENANCE.json` | `ed31cdf5` | `ed31cdf50ed9ae8fb4102272e2d511947309687b19a905e942dc02ef2981d36b` | discloses -shm rewrite, no _prev possible; live -wal df9765a5 / -shm 6af7afeb match it | n/a | [V] |
| 10 | `astra-capture/weather-nowcast/archive.sqlite` | `974ce4b5` | `974ce4b5339b010ee28819f35f365693bfc55dd337ab0d7a192aff668714f60f` | live DB; matches cite (LI: RESTORED_UNVERIFIABLE) | n/a | [V] |
| 10 | `P/VARIANTS_ACCEPT_PING_WX_FL_KXHIGH_SETTLED_TAPE_2026-10-01.json` | `2fbc2515` | `2fbc2515814f844caf7311b53406d81ae548ef90f5897dc862dbf11c48d13130` | match | n/a | [V] |
| 10 | `P/CONDUCTOR_ACCEPT_VARIANTS_WX_FL_KXHIGH_SETTLED_TAPE_FREEZE_2026-10-01.json` | `b5bd4f04` | `b5bd4f046b3a48cffc5617e5f8680a8b8d9d1688568a6fd723fd3b46a845045a` | match | n/a | [V] |
| 10 | `P/CONDUCTOR_MERGE_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `42967658` | `42967658ab2e4c5291790a3296d7323549bb203e6c9106a25281004a426614c2` | merge f233079d in git [V] | n/a | [V] |
| 10 | `P/CONDUCTOR_ACCEPT_ADDENDUM_WX_FL_KXHIGH_PR63_PRE_ROI_RULINGS_2026-10-01.json` | `68e1ff7a` | `68e1ff7a3f170a90b74a72448809558c3ce7364e32a8b5296a1d10c3b2590153` | match | n/a | [V] |
| 10 | `P/EXAMINER_SCORE_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `3ab89d3a` | `3ab89d3a8a9221461fb286610fc395f9b5bd49091b538011452fcc277b13015d` | verdict ITERATE (ceiling ITERATE); scratch out/ JSONs MISSING | n/a | [V] |
| 10 | `P/EXAMINER_SCORECARD_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.md` | `81f5a9b0` | `81f5a9b0169f866fa34e0faa84e4c8e0aa3df41a7cdbf70115c04188d6b6fdf2` | match | n/a | [V] |
| 10 | `P/EXAMINER_READY_NOT_SCORED_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `6ffae37a` | `6ffae37a9242c0a99dad138e0948c4e771fe69842d413c761b85c8e39bf55f42` | match | n/a | [V] |
| 10 | `P/SIMULATOR_READY_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `6256b698` | `6256b69867acfa8f35e94fb2d7289ffdca3d8eb378f6359587712dccf0856bd7` | match | n/a | [V] |
| 10 | `P/CONDUCTOR_SCORE_KICK_WX_FL_KXHIGH_SETTLED_TAPE_PR63_2026-10-01.json` | `e0c5203d` | `e0c5203da48854d397471973b35f8d99921e469594f6554876f95cb12c6d842f` | match | n/a | [V] |
| 10 | `P/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_WX_FL_KXHIGH_PR63_2026-10-01.json` | `50596785` | `5059678525d8b91c751e931ee45fecf7c4ee9f085528fc13c18ffafcb863cd39` | match | n/a | [V] |
| 11 | `S/LOSS_INVENTORY_2026-10-01.json` | `feb29c29` | `feb29c29a9d2b5e5f7c2ab85ac0a4785620f0e0df76a022a67ed40df54e6e2d1` | 3,431 RESTORED_SHA_VERIFIED; AMEND1; ADMIT-1 run 18 tail LOST | n/a | [V] |
| 11 | `/workspace/steward_astra_science_preserve_20261001/astra_science_dirty_133_20261001.tar` | `f91ecb68` | `f91ecb6840cd76b69d00354debd54499abd960c7ac724128bcc6e7e2faeec737` | LI-verified; holds trades-join lab files (item 1) | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/collector.py` | `1a3166c4` | `1a3166c4dad72aadf6600e17ef02d0c1b0d889eb9ecb8e84fa639f0eac2a9dff` | chain 7bd1bddb→9be001ba→1a3166c4 | _prev/7bd1bddb… + _prev/9be001ba… OK | [V] |
| 12 | `astra-capture/weather-nowcast/supervisor.sh` | `70912533` | `709125337c0b22fc57a237eaac464694841e41ac20caf9aebb753a2710ed2bd4` | chain 38ea356a→783cb184→70912533 | _prev/38ea356a… + _prev/783cb184… OK | [V] |
| 12 | `astra-capture/weather-nowcast/R2B_PREP_2026-10-02.md` | `ae3a9036` | `ae3a903609a4c5d7e331c2cdccf92d04be9760e07c31b2e5d9f650fae7c7a4e1` | match | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/archive_r2_20261002.sqlite` | `7ee088a6` | `7ee088a6f930362051fc65e0b61905833cfb7304391dda3e63974cb6909685a8` | ABORTED R2 (STOP_R2_ON_429) | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/STOP_R2_ON_429_2026-10-02.json` | `aed6c224` | `aed6c2243b8c989cc7dade273be8a3c222eea77ed78985827b83a9f390812815` | match | n/a | [V] |
| 12 | `astra-capture/q6s5-kxmlbspread/settlement_only_2026-10-02/COLLECTOR_READY_SETTLEMENT_ONLY.json` | `0dd61920` | `0dd61920f8e622c336cf9ab2ac88d0d78b04d4152c93cf98cecb14550b7d924c` | pinned by ACCEPT 9c6e19ca (settlement_pin_amendment); folder digest 65cfe9e4 recomputed | n/a | [V] |
| 12 | `incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json` | `52a6b8a1` | `52a6b8a1378b120a241ce9c6b302ca214b0a04b7360773269293d845b8623d3d` | supersedes v1 d943c13a (v1 kept on disk) | v1 retained | [V] |
| 12 | `incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02.json` | `d943c13a` | `d943c13a9d19668d870629fabd9fc0e765b7797889d379c049141e309d604163` | SUPERSEDED by 52a6b8a1 | n/a | [V] |
| 12 | `astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md` | `9a2870db` | `9a2870dba116645900809026be14303b61cf53913920688197f27d94cbd43362` | run 19 stopped_by_signal (ABORTED_SUPERSEDED); cited by fleet PR1 + primary PR65 README | n/a | [V] (bytes); ACCEPTED status per dispatcher only [I] |
| 12 | `astra-capture/weather-nowcast/PROBE_R2C_PM_2026-10-02.json` | `8695cf03` | `8695cf037abaa4753a9e2a1d1c76fef45eea2a4d0162f1c42ee532ffa5254820` | STOP_ON_429; silence until 2026-10-03 09:10 ET | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/KALSHI_429_STOP` | `a41d074e` | `a41d074e3c0792d7870cf4158936103e5d129bac3447c8c674a80f130b529399` | match | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/launch_r2c.sh` | `6ccf6dc6` | `6ccf6dc6271565849c1bb61f4647e5b9dc8b5e2360b4ec7c577cc1346c0b4806` | match | n/a | [V] |
| 12 | `astra-capture/weather-nowcast/launch_r2d.sh` | `af0f4db3` | `af0f4db3f578e75db5f1b1336b14cc0a8453daf0d51fcee856567d0fc961acc0` | match | n/a | [V] |
| 13 | `P/VARIANTS_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_SCORABILITY_FREEZE_2026-10-02.md` | `213ee6dd` | `213ee6dd33f292c8041977b0b8d7566da9412fd3debe0597643c500dc1e42db4` | parents 9f50ba19 / 4f65dcdf match | n/a | [V] |
| 13 | `P/VARIANTS_Q6S5_KXMLBSPREAD_STRATEGY_FILL_PR60_SCORABILITY_FREEZE_2026-10-02.json` | `6399ebe6` | `6399ebe6687c64972d2826df8cc36772582604e7a30b60e1b890a6d7e9cb0e55` | 26 non-file hashes are verbatim-text hashes | n/a | [V] |
| 13 | `P/Q6S5_PR60_SCORABILITY/MANIFEST.sha256` | `6e89b809` | `6e89b8098d29971070098e196347f9f75247ade83cc7ba4d79f694d55a790134` | 6/6 OK | n/a | [V] |
| 13 | `astra-science/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/pins/Q6S5_PR60_SCORABILITY_authentic_pins_2026-10-02.tgz` | `bd94757c` | `bd94757c4c5748fc3447cf596435ddee0af129c87599d4c48f002b2b61756308` | 157 files; pins/MANIFEST 159/159 OK | n/a | [V] |
| 13 | `P/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_PR60_SCORABILITY_2026-10-02.json` | `63530343` | `6353034311b5fdf26c982a6df7e8bb203a9c6554d0a6c79ba8e255543971a228` | match | n/a | [V] |
| 13 | `P/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_PR60_SCORABILITY_FREEZE_2026-10-02.json` | `9c6e19ca` | `9c6e19ca11a855015fb4e3e63cd65ae5e5c334875240e817e164e988426df9f5` | match | n/a | [V] |
| 13 | `P/CONDUCTOR_MERGE_PR64_Q6S5_PR60_SCORABILITY_2026-10-02.json` | `f1bab3b2` | `f1bab3b2e0cc19ccf64f25ea61c030532b4f5b89965a568624c910e012ccf154` | merge eb33f094 in git [V] | n/a | [V] |
| 13 | `P/SIMULATOR_READY_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_SETTLED_2026-10-02.json` | `5b9de869` | `5b9de869a4f2c8ee61e5af845c3cda2e0ebf4b9ca4b4352a6d7417023ad7a9a5` | match | n/a | [V] |
| 13 | `P/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.json` | `961f72fa` | `961f72fa76dd57867915b5321635becdc7a1f09d7d93e5147d66860fa0ea6e3e` | verdict ITERATE | n/a | [V] |
| 13 | `P/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_PR64_SCORABILITY_2026-10-02.md` | `1f418bf7` | `1f418bf73315c533cadebabfde939e0e4ea64fba01ddd7939b4185dfc49335fc` | match | n/a | [V] |
| 13 | `P/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_PR64_SCORABILITY_2026-10-02.json` | `57a9f5e6` | `57a9f5e68f41cf6df1428d2516ace34550267f264396d486f245977a571a871c` | pins 961f72fa/1f418bf7/5b9de869/f1bab3b2 = match; universe Sep-25 KXMLBSPREAD CONSUMED | n/a | [V] |
| 14A | `P/CONDUCTOR_MERGE_PR65_DOCLAG_2026-10-02.json` | `d8f4fb5c` | `d8f4fb5c1736a29d173a2b63a543658cdb45fcc99bf6b924b656cea2ca7a510d` | squash 761eaaed, head fa86a363, base eb33f094 = GitHub [V] | n/a | [V] |
| 14B | `P/CONDUCTOR_MERGE_FLEET_PR1_DOCLAG_2026-10-02.json` | `c732e73f` | `c732e73f33300af9cef2cecc0a1140760b34ceb2d644797510a3375165990d66` | squash 6db4d41a, head dc859604, base 1825ec8c = GitHub [V] | n/a | [V] |
| 14C | `S/DOCLAG_PR_REGISTRY_TEXT_2026-10-02.md` | `d0c872cd` | `d0c872cd65109a402ed2e5212a1a9b7e7fe9366af06ce77f60cdada5f3686a8b` | final rev3; rev1 3c290457 / rev2 c61231b5 superseded | no _prev of rev1/rev2 on disk | [V] (rev3); rev1/rev2 [I] |
| 14D | `S/DIGESTS_ANNOTATION_RECORD_2026-10-02.json` | `36f97e7e` | `36f97e7ec9593a2ceebd710296f9483d9935310ea433b648e64f162d0f079f6e` | v1 + REVERT revision; 2e9cf447→36f97e7e | no _prev of 2e9cf447 on disk | [V] (36f97e7e); 2e9cf447 [I] |
| 14D | `S/doclag_2026-10-02/digests_annotated_reverted/C4_KXCPI_SETTLED_JOIN_HARNESS.0404abf51bcdda1742de894d2fe6ed0ae91c4b1cfd73c9af9762c3fc0eed55ab.DIGESTS.txt` | `0404abf5` | `0404abf51bcdda1742de894d2fe6ed0ae91c4b1cfd73c9af9762c3fc0eed55ab` | audit copy of reverted annotation | n/a | [V] |
| 14D | `S/doclag_2026-10-02/digests_annotated_reverted/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS.fffe42ef7d9384bafa05c9dfebaf248b4ead40c82d091c7a7d131eadd331c2ea.DIGESTS.txt` | `fffe42ef` | `fffe42ef7d9384bafa05c9dfebaf248b4ead40c82d091c7a7d131eadd331c2ea` | audit copy of reverted annotation | n/a | [V] |

Git commits verified in the box clone (`git cat-file -t` = commit): cb8957d7… (PR59, parent f349ffa8), `12e760f5bd3b622d8f0d70a74c28655464e2b93c` (PR60), `d7558fc4b92256c68eaea66b9700021206de0a2d` (PR61), `749bc1464764fda03dcddd1162177ef062b2ece3` (PR62), `f233079d9e7d2a91e2100f2085bcf85d0006e28f` (PR63), `eb33f094f3341958746f83a8f2f8c1e2c37a7d0a` (PR64). 6/6 [V]. The astra-science clone HEAD is eb33f094. The Ruling-1 reset point was 12e760f5, and the clone was advanced after that.

## 2. Item 14: doc-lag PR65 (primary) + fleet PR1. Repo bytes vs box staged copies

- **PR65** `17thgreen/GPT-6-Astra-Deathmatch` #65: merged 2026-10-02 19:19:15 ET (GitHub merged_at 23:19:15Z). Squash `761eaaedc153dca9807d7630adcea1ae3387d9c1`, head `fa86a363ee071c493e86222264da626ade7c283d`, base `eb33f094`, 7 files, 2 commits [V via connector]. MERGE packet `P/CONDUCTOR_MERGE_PR65_DOCLAG_2026-10-02.json` `d8f4fb5c1736a29d173a2b63a543658cdb45fcc99bf6b924b656cea2ca7a510d` [V]; results/pnl/roi null.
- **Fleet PR1** `17thgreen/Grokbot-Deathmatch-Dedicated-Repo` #1: merged 2026-10-02 19:20:07 ET (23:20:07Z). Squash `6db4d41ad8eb7be94577f17f0b128d370e3116c5`, head `dc859604e561b4075b12fd92e39344c8c28a88d2`, base `1825ec8c`, 4 files, 2 commits [V via connector]. MERGE packet `P/CONDUCTOR_MERGE_FLEET_PR1_DOCLAG_2026-10-02.json` `c732e73f33300af9cef2cecc0a1140760b34ceb2d644797510a3375165990d66` [V]; results/pnl/roi null.
- Method: the GitHub connector `get_file_contents` / `get_git_tree` was read at the squash sha. Each repo blob id was compared with `git hash-object` of the box staged copy. Equal blob ids mean identical bytes, so the box sha256 is the repo sha256. Fleet `registry/STATUS.md` was also sha256-ed directly from the returned text (`efc3a8c3…`). The two 111 KB EXPERIMENT_REGISTRY blobs were compared by tree blob id rather than fetched in full. 11/11 repo files [V]. Nothing was left [I] on the repo side.

| PR | repo path @ squash | repo blob id | box staged copy | sha256 (box = repo) | note | tag |
|---|---|---|---|---|---|---|
| PR65 | `README.md` | `680b6413e6210593a120243fc50bdf5f93de1c47` | `S/doclag_2026-10-02/primary_new/README.md` | `a4e97325cc42d856b91cdaa618c6ea45f99668e94d7af5c55394e498cd519cc5` | old 8a40c212 (no repo _prev per Steward ruling; old bytes kept at governance/astra/steward/doclag_2026-10-02/primary_old/README.md) | [V] |
| PR65 | `docs/EXPERIMENT_REGISTRY.md` | `ecaa2a548b3ee6fd632b67b34e80a8b4b53d3fdf` | `S/doclag_2026-10-02/primary_new/docs/EXPERIMENT_REGISTRY.md` | `d1d01784ddb50629a6842f0f9055e22f087c48c28eb43ba537e135f5f47660a6` | old 8ee066c3 | [V] |
| PR65 | `docs/_prev/8ee066c3….EXPERIMENT_REGISTRY.md` | `0f5e8d801f3fead1866b3af6f96ba348ede1b915` | `S/doclag_2026-10-02/primary_new/docs/_prev/8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f.EXPERIMENT_REGISTRY.md` | `8ee066c3f13fe4677b9a4f7b753a57ada43d8aa81229f2ec3c83af16c1a1e30f` | _prev self-hash OK | [V] |
| PR65 | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json` | `6e7ea95c3719990eea1e4a9ae1c241ce77a88651` | `S/doclag_2026-10-02/primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json` | `cf9ce7ca7c8bc677f70388e63cde75c49aa9a5afcdd70cc459fef451214e4880` | old ffab465a; status "SUPERSEDED (PR64 merged eb33f094; Examiner SCORE 961f72fa ITERATE)" | [V] |
| PR65 | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a….EXAMINER_HOLD…json` | `47f10bcb1597053e914cda599edd12436f5404e2` | `S/doclag_2026-10-02/primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2.EXAMINER_HOLD_Q6S5_PR60_SCORABILITY_PRE_PR_2026-10-02.json` | `ffab465a62587587b8630a994414cb1d7cd74741d56c935a81e803c2037ef6a2` | _prev self-hash OK | [V] |
| PR65 | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md` | `580a110087f2ad8b7761bd41a2a494ac9f19116f` | `S/doclag_2026-10-02/r2_primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/README.md` | `c9cd9b68ec32b72692a4ed959f40cbdfff42a57e54457f74ff86534a2c6e545a` | old 9a8bc5c6 | [V] |
| PR65 | `kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/9a8bc5c6….README.md` | `8b625bf333c2d581f816789dbcbd0b2a8e13d845` | `S/doclag_2026-10-02/r2_primary_new/kalshi_q6s5_kxmlbspread_strategy_fill_scorability_lab_20261002/_prev/9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c.README.md` | `9a8bc5c6727c8abd30d83e4bfc1b9e6553aae6c449331d11b37b1bcd5ec5b83c` | _prev self-hash OK | [V] |
| fleet PR1 | `registry/STATUS.md` | `371702933afd67a7845138496360180fb664906c` | `S/doclag_2026-10-02/fleet_new/registry/STATUS.md` | `efc3a8c3a3e3e6aa434507f4b545dabba0318796c7c55807568ff05dd1a27017` | old 7e22d2a9; cites 52a6b8a1 + 9a2870db | [V] |
| fleet PR1 | `registry/_prev/7e22d2a9….STATUS.md` | `7e7b33202ef032ff722b4496b18363ed614e7d61` | `S/doclag_2026-10-02/fleet_new/registry/_prev/7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a.STATUS.md` | `7e22d2a95806e1797774cf0205a7b989fc671e4c3dd40ca2813d3a42efe0298a` | _prev self-hash OK | [V] |
| fleet PR1 | `registry/PACKET_INDEX.md` | `0800c2145b33076a6357fb68b7dd90a49db76659` | `S/doclag_2026-10-02/r2_fleet_new/registry/PACKET_INDEX.md` | `0b8aa0ca5bd927b47053e9ddfa3744af4ecfedff2e94888f8ced6ff91947331c` | old 92320112; cites 52a6b8a1 + 9a2870db | [V] |
| fleet PR1 | `registry/_prev/92320112….PACKET_INDEX.md` | `eaba7027cff5a86c3571fec709a381b5ee67662a` | `S/doclag_2026-10-02/r2_fleet_new/registry/_prev/92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0.PACKET_INDEX.md` | `92320112b06f48f60d4a8aac5e793462e70eddf52acbd58ad007b56968c880e0` | _prev self-hash OK | [V] |

- Old-side staged copies also re-hash: `S/doclag_2026-10-02/primary_old/README.md` 8a40c212…, `primary_old/docs/EXPERIMENT_REGISTRY.md` 8ee066c3…, `primary_old/…/EXAMINER_HOLD…json` ffab465a…, `r2_primary_old/…/README.md` 9a8bc5c6…, `fleet_old/registry/STATUS.md` 7e22d2a9…, `r2_fleet_old/registry/PACKET_INDEX.md` 92320112… [V]. The sha records `primary_sha_record.json` 77707f33…, `r2_primary_sha_record.json` 5405b8f8…, `fleet_sha_record.json` 999cfe6f… and `r2_fleet_sha_record.json` 36f3fec7… each match the files they list [V].
- README.md has no repo `_prev` (Steward ruling, prev_copy null). The 8a40c212 bytes survive only as the box staged copy above.
- Fleet citations: `incidents/ADMIT1_TRUNCATION_BOX_REBUILD_2026-10-02_v2_CORRECTED.json` 52a6b8a1… and `astra-capture/prospective/ADMIT1_POST_RUN_NOTE_2026-10-02.md` 9a2870db… re-hash on disk [V]. The PR65 README cites the same two shas.
- (C) `S/DOCLAG_PR_REGISTRY_TEXT_2026-10-02.md` final rev3 `d0c872cd65109a402ed2e5212a1a9b7e7fe9366af06ce77f60cdada5f3686a8b` [V]. rev1 3c290457 and rev2 c61231b5 are superseded and have no bytes on disk [I]. Per the dispatcher, Archivist ACKs were conditional at rev1, wording was applied at rev2, and the ACK was full at rev3.
- (D) DIGESTS annotate-then-revert. Annotated 0404abf5 (C4) and fffe42ef (ATP) were REVERTED at 19:14:46 ET by Archivist ruling. On disk now: `P/C4_KXCPI_SETTLED_JOIN_HARNESS/DIGESTS.txt` = a2754a86… and `P/ATP_KXATPMATCH_SETTLED_JOIN_HARNESS/DIGESTS.txt` = e72add78… [V]. `_prev` copies of those exact bytes have been in each `_prev/` since 19:13:35 ET. Audit copies 0404abf5 / fffe42ef are in `S/doclag_2026-10-02/digests_annotated_reverted/` [V]. Record `S/DIGESTS_ANNOTATION_RECORD_2026-10-02.json` 2e9cf447 → `36f97e7ec9593a2ceebd710296f9483d9935310ea433b648e64f162d0f079f6e` [V]; 2e9cf447 has no `_prev` [I]. Live pins match again: a2754a86 is in C4 SOURCE_PINS, EXAMINER_READY_C4…PR50, EXAMINER_ACK_C4_RJ_PR50 and EXAMINER_SCORECARD_STUB_C4 (top-level + harness copies); e72add78 is in ATP SOURCE_PINS [V].
- **DIGESTS is not indexed as changed.** It stays at a2754a86 / e72add78, pinned by SOURCE_PINS and the C4 Examiner packets. The scout copies `P/scout_c4_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` (b72465d8) and `P/scout_atp_settled_rejoin_2026-09-24/FROZEN_EXPERIMENT.json` (802b40b3) were intentionally not realigned [V].
- Also present in `S/doclag_2026-10-02/` and hashed, but working files and not record: CLOUDAGENT_PROMPT_primary 8bc489fb…, CLOUDAGENT_PROMPT_fleet b2fabf26…, CLOUDAGENT_FOLLOWUP_primary c5520f63…, CLOUDAGENT_FOLLOWUP_fleet 0e84488c…, apply_edits.py 0c339530…, apply_edits_2.py 6e73314b…, primary.diff 6a5667a6…, r2_primary.diff 4cc17c16…, fleet.diff 1efa7ea8…, r2_fleet.diff e40f9274….

## 3. Exceptions

- **MISSING (cited):** `08aa54de2b47314e9d27342c1bf3824400d3c434770d339f2e3c253ee90084f6` (Q6S5 queue, item 1). Known, superseded by 7472b8ac per ACCEPT a5398129, never recreated. Unrestorable.
- **MISMATCH (cited):** `S/STEWARD_CONDUCTOR_RULINGS_EXEC_2026-10-01.md`. Cited `7e389f326e05a85612200d0e37bc76c2f2db41878a2412ce57381ad7f380b571`; on disk `133302a440281647f7589f29dad54882928c3d43253e77cf9bef78dbb6f5d578`. Cause: the Conductor appended "Deletions done" after HYGIENE_2026-10-01 §11.2 recorded 7e389f32; §11.3 records 133302a4, and LOSS_INVENTORY verifies 133302a4. No `_prev` of the 7e389f32 bytes exists. **_prev gap:** UNVERIFIED_BYTES_MISSING for 7e389f32, unrestorable. The JSON twin 433ba206 is intact.
- **MISSING (uncited evidence, box rebuild):** Examiner scratch outputs. PR61: `/workspace/tmp/examiner_scratch_pr61_score/out/measure_pre_post.json` 5dd5ea93…, `out/independent_recompute.json` f4571074…. PR62: `…pr62_score/out/measure_pre_post.json` 7f412f32…, `out/independent_recompute.json` 1f5d28dd…. PR63: `…pr63_score/out/` runner_path_measure 70c58bcc…, independent 7317bfb2…, descriptive 24e62b49…. The scripts are present (pr61 d6f52f01 / 36fd44de; pr62 4a862b27 / f563856e; pr63 ffc91e4c / db9c5b31 / c58a6632). These files are not in LOSS_INVENTORY. They could be regenerated only by re-running scripts, which is outside the Archivist remit and was not done.
- **LOST (LOSS_INVENTORY):** ADMIT-1 run 18 after 2026-10-01 22:10:35 ET through 02:15 ET. Never backfill.
- **Restorable:** trades-join lab `astra-science/kalshi_q6s5_kxmlbspread_feequue_trades_join_20260925/` (results f707bcbd…, metrics 3dcdf2ab…, DIGESTS 02478c87…, runner 9a52bcb7…). These were removed from the clone by the Ruling-1 reset. All 4 were stream-verified inside the preserve tar `/workspace/steward_astra_science_preserve_20261001/astra_science_dirty_133_20261001.tar` (`f91ecb6840cd76b69d00354debd54499abd960c7ac724128bcc6e7e2faeec737`, re-hashed now [V]). Nothing was extracted.
- **Explained drift (not a mismatch):** the WX freeze aec5b760 embeds collector.py 7bd1bddb (now 1a3166c4 via item 12, `_prev` OK) and logs/kalshi_429.jsonl 9b9a2d5e (now 696b48a6, a live append-only log; the 9b9a2d5e bytes are in `P/WX_FL_KXHIGH_SETTLED_TAPE/gap_log/kalshi_429.jsonl`). The live weather `archive.sqlite-shm` rewrite is disclosed by SNAPSHOT_PROVENANCE ed31cdf5; no `_prev` is possible.
- **_prev gaps (steward working records, item 14):** DOCLAG text rev1 3c290457 / rev2 c61231b5 and DIGESTS record 2e9cf447 have no `_prev` [I]. They are superseded drafts, not frozen packets.

## 4. LOSS_INVENTORY cross-check (`S/LOSS_INVENTORY_2026-10-01.json` feb29c29…, 3,431 RESTORED_SHA_VERIFIED)

- LI-verified among cited items: 7472b8ac, dc19794b, ac7cfe63, 9f50ba19, 6602e07e, 62de476e, 63b5d981, 0860cbe2, bcd27e06, b72465d8, 968a46e3, 509e2cf2, 802b40b3, 382009b9, a2754a86, e72add78, 133302a4, 5beba803, 6576ee6c, aec5b760, febc74af, 4f65dcdf, 433ba206, f91ecb68 (tar).
- LI-listed RESTORED_UNVERIFIABLE: 974ce4b5 (live weather archive) and RULING2 record 3bb36969 (sha never recorded before the rebuild; 4/4 of its records match disk now).
- Hydrated, not in LI: the remaining pre-rebuild packets. Each is present and equals its cite; the integrity basis is the Conductor/Examiner cross-cites, not LI.
- Post-rebuild (created after 2026-10-01 23:13 ET, outside LI scope): item 12 and 13 files, item 14 files, and the 2026-10-02 MAXIMIZE pins.
- **Archivist receipts:** 21/21 `P/ARCHIVIST_INDEX_*` files re-hash to their authoritative PACKET_INDEX row. Corrections already on record: 895aca1c supersedes f2c10429 (no `_prev` of the stale mid-write bytes); 7d8ee73b supersedes ef1c1781 and 7629a4e0 supersedes 7595402e, with `_prev/` copies present and self-hashing. 0/21 appear in LI's verified list; they were hydrated by copy-in. No ARCHIVIST_INDEX receipt existed after 2026-09-25 before this one.

## 5. Cemetery entry (written this pass)

`governance/astra/cemetery/CEM-ASTRA-20261001-001_Q6S5_KXMLBSPREAD_FL_BAND_MAKER.md` sha256 `41ccd2825c98375135a81e0ae390ecc1e8ebfd9fb94a1e6c6a9f96efade11d0c` (new file; no existing CEM file edited). Its text follows verbatim:

> # CEM-ASTRA-20261001-001: Q6S5 KXMLBSPREAD FL-band maker thesis (H1: FL0 low band beats FL1 mid band)
>
> - **CEM_ID:** CEM-ASTRA-20261001-001
> - **DATE:** 2026-10-01 (ET). Examiner SCORE filed 2026-10-01T19:30:46-04:00; Conductor ACCEPT KILL stamped 2026-10-01T19:33:00-04:00. Indexed by the Archivist on 2026-10-02 (ET) in `packets/ARCHIVIST_INDEX_BACKLOG_2026-09-25_to_2026-10-02.md`.
> - **CARD-LINE:** Q6S5 KXMLBSPREAD. FL-band settled-tape measurement (PR61), on the parent R3-P3 10¢ favorite–longshot bands (`packets/r3_p3_fl_maker_taker/bands_registry_10c.json`).
> - **FAMILY:** FL-band maker thesis, KXMLBSPREAD only. family_size 4.
> - **DECISION:** **KILL** (verdict_ceiling ITERATE). Conductor ACCEPT `be235777` scope, verbatim: "FL-band maker thesis H1 (FL0 low-band beats FL1 mid-band), KXMLBSPREAD only, Sep-24 pinned universe".
> - **CLASS of killing evidence:** historical replay, IN_SAMPLE_DEV (Conductor addendum `09763030`), public_counterparty_realized. Effective n = 3 games. Fee view CACHE_NOT_R1P1 (not fee-honest). Astra fills/results/pnl null. counts_toward_keep false; promote false.
>
> ## Cause of death
>
> Examiner verdict_scope, verbatim (SCORE `2e74f17b`): "FL-band maker thesis (H1: maker_gross_roi_delta_FL0_minus_FL1 > 0) for KXMLBSPREAD only, per freeze. Not a kill of Q6S5, of the parent harness, of PR58/PR60, or of any other series."
>
> Pre-declared freeze rule, verbatim (freeze `fb6540f5` line 118): "`contradicts_H1` if the full-sample delta ≤ 0 **and** ≥2 of 3 LOEO deltas ≤ 0. … `contradicts_H1` supports a KILL of the FL-band maker thesis **for KXMLBSPREAD only**."
>
> Examiner reading, verbatim (scorecard `1bdb1d9c`): "Reading: **contradicts_H1**. The full-sample pre delta is -0.104764 (≤ 0). LOEO deltas are excl. HOUATH -0.240144, excl. LAASEA +0.031111, excl. SDLAD -0.122538, so 2/3 are ≤ 0."
>
> - "**Primary H1 delta FL0−FL1 = -0.104764**" (scorecard).
> - "All 6 LOMO H1 deltas are negative. H1 stays negative under both stresses." (scorecard)
> - Multiplicity, verbatim: "With 3 games, the minimum one-sided sign-test p is 0.125 … The KILL rests on the pre-declared directional rule, not on a significance test." (scorecard)
> - Conductor basis, verbatim (ACCEPT `be235777`): "pre-declared freeze rule contradicts_H1 -> KILL (full-sample delta <= 0 and >= 2 of 3 LOEO <= 0); directional, not significance-based"
> - scoreboard_effect, verbatim: "none (Q6-000 remains KEEP leader; nothing promoted)"
>
> ## Erratum (recorded as annotation; be235777 not edited)
>
> ACCEPT `be235777` field `erratum_noted` is WRONG. Conductor annotation in `546f62c9` (`annotation_of_be235777`), verbatim: "the erratum_noted field is WRONG. Per Examiner correction: finalized markets closed 04:30:17-20Z (HOUATH/LAASEA) and 05:06:42Z (SDLAD); 2026-09-28T01:40Z is latest_expiration / stale pre-close panel close. The original PR61 note was right." Effect, verbatim: "none on any PR61/PR62 number or verdict; 04:31Z prints were post-close and excluded".
>
> ## Evidence pins (sha256, re-hashed 2026-10-02 ET by the Archivist [V] unless marked)
>
> | Role | Path (relative to `lab/governance/astra/` unless noted) | sha256 |
> |---|---|---|
> | Freeze | `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_FREEZE_2026-09-29.md` | `fb6540f52ed5f819ccf6e80bf0cf7eb6d951e065416b9d550fead0c6d06043fa` |
> | Packet MANIFEST (8/8 OK) | `packets/Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE/MANIFEST.sha256` | `901285ed3d559e1a121197c1ee36ead3d8b40498dfd2b4888694fb077fe3c043` |
> | Pin bundle (101 files) | `lab/astra-science/kalshi_q6s5_kxmlbspread_fl_band_settled_tape_lab_20260929/pins/…FL_BAND…2026-09-29.tgz` | `63b5d981bc06f684eebb69a8ac29394534f8ae52c101f3018557544f14e29857` |
> | Variants registry ping | `packets/VARIANTS_ARCHIVIST_REGISTRY_PING_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_2026-09-29.json` | `eba1260f1ab901a223f3f0b5feb1ff6f023d9f8870c1e69e16007e93e12b3a40` |
> | Bands registry | `packets/r3_p3_fl_maker_taker/bands_registry_10c.json` | `0860cbe28d28ecc6142ddf6f1ebb67792084264ed82e0b4d868c3b3138ea5312` |
> | Conductor ACCEPT freeze | `packets/CONDUCTOR_ACCEPT_VARIANTS_Q6S5_FL_BAND_SETTLED_TAPE_FREEZE_2026-10-01.json` | `8e4fbac7d0426bc67c1f53fb8057a382fe46da738bd701cb970a9812a6dc2a3b` |
> | IN_SAMPLE_DEV addendum | `packets/CONDUCTOR_RULING_Q6S5_FL_BAND_IN_SAMPLE_DEV_LABEL_2026-10-01.json` | `09763030c67df066f2b59346200813e181777670cd46fcee6b8877a6dd74d754` |
> | PR61 merge commit (git) | 17thgreen/GPT-6-Astra-Deathmatch | `d7558fc4b92256c68eaea66b9700021206de0a2d` |
> | Conductor MERGE | `packets/CONDUCTOR_MERGE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `469de2376ae413f66684df26c08656e705a7fb5a0a1d128a4270d789c841df32` |
> | Simulator READY | `packets/SIMULATOR_READY_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `8e8a17566747cb29077c2f7abccb49640739ae873d3d5c20fbfa819bbde36e1b` |
> | Examiner READY_NOT_SCORED | `packets/EXAMINER_READY_NOT_SCORED_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `bf9aafa3363a45388aa8ebac2fffbaa0a556dba56d1cb59914119f6f78cfbffc` |
> | Conductor score kick | `packets/CONDUCTOR_SCORE_KICK_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `0f8de7cd6b2187076e2bd8f914c4de51b3d8bfecdd59e324a41a9f030f5f26b6` |
> | Examiner SCORE (KILL) | `packets/EXAMINER_SCORE_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.json` | `2e74f17b1307b8b57f33a6475cd7ce8af48c470099478cadfb07877b0d70745f` |
> | Examiner scorecard | `packets/EXAMINER_SCORECARD_Q6S5_KXMLBSPREAD_FL_BAND_SETTLED_TAPE_PR61_2026-10-01.md` | `1bdb1d9c1e6272a4b95a5080e4681858859e69a053f69e32b9b85b7d9e44c386` |
> | Conductor ACCEPT KILL | `packets/CONDUCTOR_ACCEPT_EXAMINER_KILL_Q6S5_KXMLBSPREAD_FL_BAND_PR61_2026-10-01.json` | `be2357773ca7a842e6896676e3ba0291f40ef8e0b8f997d46f7124d4b2705229` |
> | Annotation of be235777 | `packets/CONDUCTOR_ACCEPT_EXAMINER_ITERATE_Q6S5_GAME_PHASE_PR62_AND_ANNOTATE_be235777_2026-10-01.json` | `546f62c99f1268b14ddb612fe9891c7741e5bee7e8397cae32c75d86fbff65ae` |
>
> Flag: Examiner scratch outputs `/workspace/tmp/examiner_scratch_pr61_score/out/measure_pre_post.json` (`5dd5ea93…`) and `out/independent_recompute.json` (`f4571074…`) are **MISSING** on disk (box rebuild). Scripts `score_pr61.py` (`d6f52f01…`) and `independent_recompute.py` (`36fd44de…`) are present. The SCORE and scorecard bytes above are intact. The verdict does not depend on the scratch files being re-hashable.
>
> ## What this did NOT prove
>
> - Not a kill of Q6S5, of the parent harness, of PR58/PR60, or of any other series (verdict_scope).
> - Not evidence that FL1 or FL2 bands have edge. Conductor caveat, verbatim: "H2 (FL2 - FL1 = -0.4282) and the FL1 mid-band lead (+0.1443 gross) are hypothesis-generating only; carried to the untouched holdout as a pre-registered candidate, NOT a KEEP".
> - Not a significance result. Effective n = 3 games; min sign-test p 0.125 > Bonferroni 0.0125.
> - Not fee-honest (CACHE_NOT_R1P1). No Astra fills. No PnL.
>
> ## Rules
>
> - Frozen negative stays visible. Never delete or soften.
> - No resurrection without a **new freeze**. Scorecard, verbatim: "any re-test needs a new freeze with an untouched post-freeze settled set (p16 item 12)."
> - The Sep-24 pinned universe is consumed for this thesis.
> - No live orders. No invented PnL. Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%.

## 6. Seen but NOT indexed (ambiguous or out of scope)

- `S/SYNC_PROMPT_V3_2_PROPOSAL_2026-10-03.md` (written 19:19 ET; a proposal, not in the backlog).
- Uncited related packets: CONDUCTOR_ACCEPT_*_STRATEGY_FILL_FREEZE_2026-09-29, CONDUCTOR_ACCEPT_VARIANTS_Q6S5_STRATEGY_FILL_FREEZE_2026-09-29, CONDUCTOR_RECONCILE_*_DUAL_ACCEPT_SOLE_CLOUD_2026-09-29, EXAMINER_VERIFY_Q6S1_BUNDLE_V2_2026-09-29, EXAMINER_ACK_*_PR60_SETTLED_NOT_SCORABLE_2026-10-01, SIMULATOR_READY_*_STRATEGY_FILL_PR60_SETTLED_2026-10-02, the 2026-10-02 holdout maker-null feasibility kick/ACCEPT/note, EXAMINER_ACK_SIMULATOR_READY FL-band 26684451, VARIANTS_ACCEPT_PING FL-band 32b1d5f2, and MAXIMIZE_PIN files 09-29 to 10-02.
- `astra-capture/prospective/ADMIT1_RUN18_TRUNCATION_GAP_2026-10-02_to_RUN19.json` b44b4793… treats run 19 as a continuation and is superseded by v2 52a6b8a1.
- The "ACCEPTED" status of the post-run note 9a2870db rests on the dispatcher only. No Conductor ACCEPT citing 9a2870db was found on disk. The bytes are [V], the status is [I].

## 7. Counts

- Master table rows: 109 (103 plain [V]). Item 14 repo files: 11/11 [V] by blob id. Git commits: 6/6 [V] in the box clone, plus PR65/PR1 squash and head shas [V] via connector.
- MISMATCH: 1 (rulings md 7e389f32 → 133302a4). MISSING cited: 1 (08aa54de). MISSING uncited evidence: 7 Examiner scratch outputs (PR61 ×2, PR62 ×2, PR63 ×3). LOST: ADMIT-1 run 18 tail. Restorable: 4 trades-join lab files.
- [I] only: 3c290457, c61231b5, 2e9cf447 (superseded steward drafts) and the ACCEPTED status of 9a2870db.
- **Scoreboard unchanged: Q6-000 / Arm D KEEP +$345.24 / +6.90%; no new KEEP.**
