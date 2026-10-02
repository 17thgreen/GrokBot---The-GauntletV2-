# RESULTS-ONLY PR landing manifest — 2026-09-24

**Prepared by:** The Archivist (Registry) · 2026-09-24T19:49:49-04:00 (ET) · **Authority:** Conductor ruling (4).  
**Status:** MANIFEST ONLY. The Archivist does not open the PR. No source file was modified.  
**Machine-readable:** `registry/RESULTS_LANDING_MANIFEST_2026-09-24.json` · **Verify list:** `registry/RESULTS_LANDING_SHA256SUMS_2026-09-24.txt` (`sha256sum -c` from repo root; included files only).  
**Main checked:** tree @ `34a27202` (PR49) + directory re-read @ `37ad5b7b` (PR52, 19:46 ET): proposed paths unchanged.  
**Path rule:** `/workspace/lab/astra-science/<lab>/…` → `<lab>/…`; `/workspace/lab/governance/astra/…` → `lab/governance/astra/…`.

## Summary

- Entries: **171** · included in results PR: **159** · held/excluded: **12**
- Q7: included 79, excluded 1
- Q7-B-REHAB-P1: included 67, excluded 0
- R3-P2: included 13, excluded 11
- Included bytes: 2,278,467,945
- **Exceeds GitHub 100 MiB [I]:** 5 files, 1,772,203,495 bytes → LFS or archive-by-checksum
- Over 50 MiB warning: 8 files
- Already on main, byte-identical: 8 · exists on main with different bytes: 0

## Blocking flags

- Q7 verification.json: Examiner-scored bytes (sha256 eb1586bf…, VERIFIED) are NOT on the box. Box and main both hold the NOT_RUN_INPUTS_MISSING stub (sha256 9cde03dc…, blob 485a7149). UNVERIFIED — scored verification cannot be landed from the box.
- 5 files exceed 100 MiB (Q7 experiment_summary.json 272,427,327 B; four Q7-B P1 *_B1.json ~375 MB each) — LFS or archive-by-checksum required.
- R3-P2 trade-step retry outputs (2 files, written ~19:45 ET 2026-09-24) are Mechanic plumbing only, no Examiner stamp — HELD.

## Files

Legend: incl = include in results-only PR. main = exists on main (blob) / identical.

### Q7

| incl | category | role | proposed repo path | bytes | sha256 | on main (blob) | flags |
|---|---|---|---|---|---|---|---|
| Y | result | RUN_STATUS_STUB | `nfl_paircheck_lab_20260922/results/NOT_RUN.json` | 1,141 | `e9cb7084b71aa4cde64cdfd791ed6b3b138aadd425c925df3b35bdd60cf1c7b2` | yes `85d0675a4082d8866c47d3f20fb89a1c7ae89250` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED |
| Y | result | RUN_STATUS_STUB | `nfl_paircheck_lab_20260922/results/analysis_status.json` | 189 | `8acec3c77b86abce43b6eb01a941de317f1603a5a30c7ee4bc4582800c119ebb` | yes `24c7a72d8c15b9e2178efd63d92e701aea98b7fd` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED |
| Y | result | EXAMINER_CITED_SUMMARY_NO_SHA_PIN | `nfl_paircheck_lab_20260922/results/experiment_summary.json` | 272,427,327 | `8b6cf91485297ef1aa9f9dd16ddf6981423bf16417d14977f7c04aaf5cd300bb` | no | EXCEEDS_GITHUB_100MB_LIMIT |
| Y | result | EXAMINER_PINNED_SCORED_BYTES | `nfl_paircheck_lab_20260922/results/paircheck_effects.json` | 2,237 | `5d87ea610f22482c980868d8a31a228ca1931368d9eeab73add4256d2e117fdf` | no | MATCHES_EXAMINER_PIN |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_A.json` | 11,419 | `986e61c955f6695897cca67eca22076fda94cb1c9d7d4a8cb0c2d802134aa631` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_A_decisions.jsonl.gz` | 67 | `c0e5e2c39b2ba91b969e405d02fa8617f0c0e2891c874723ae80f2dd2f92b33e` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_A_fills.jsonl.gz` | 194,272 | `68a840077a46a4dc58a2a69a54e233c85e06fd8feb199cfaa37197e9236bfac4` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_A_orders.jsonl.gz` | 574,784 | `1f3fb173d589c347e822c12f65d7d963321012e3e4a822d50549c61479d90326` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_B.json` | 56,496,246 | `e79f367706849b3e4306cc541ac3993c90fbc5b69a7e41bee9b258f3f33ce590` | no | OVER_50MB_GITHUB_WARNING |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_B_decisions.jsonl.gz` | 67 | `034ec66d980a1e7e18159a40bd12746a3754d593429454c18ca968b31b7d068b` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_B_fills.jsonl.gz` | 183,864 | `5f020001eb359adbdfa4b3d8c6b8e87213ec38a61e84264c45cc44fa40fcaa8e` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_B_orders.jsonl.gz` | 561,341 | `4d8e741da6cc6b516577577536bca43e2c1a4850ceecb7856b9f5473012e2972` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_C.json` | 11,501 | `9aba9d6f38a7bc0ec1c9e0b26a34e67a242f5745463a116819d74eb2dcf24396` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_C_decisions.jsonl.gz` | 910,556 | `2c291ea93deb44b8160832d7136e214deb14657a6351b62c132ed74906fa2f90` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_C_fills.jsonl.gz` | 197,080 | `18637959030e341cf44d8ef6eb2a4cece2b09b84e7c5fb8d79d2e2c7b56a3815` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_C_orders.jsonl.gz` | 585,885 | `d012fa20e3fe5ca18b1e7309b583a5bfa38901919b9b5fa2d0452bf3b7d04ee8` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_D.json` | 2,342,036 | `283648c2b536c7c55222df486839b51c1bbeb030d361640075672732626eff19` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_D_decisions.jsonl.gz` | 827,009 | `27e164f61889d261b072aa5b49aed3675b4daa04dbccf93c6ff6b05568862687` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_D_fills.jsonl.gz` | 174,314 | `fa0633f1cb12659c3a2c384dad2b2e487046d8361aade1cc73762f34357175eb` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d0.25_D_orders.jsonl.gz` | 553,659 | `6ccb4d370e8e2707cd7e61ea5d5bc95f363909d0afca5a702b83650380b53e4b` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_A.json` | 11,405 | `89f9780b6f2aae1ad11a47e6100b7d9bc94aa20e09c8034f185dd83ceeb63946` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_A_decisions.jsonl.gz` | 64 | `ec052703e6e496e4973e1c5bf8806a8a69b3e62c2dfe2aabfeaf116a1c071cff` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_A_fills.jsonl.gz` | 187,383 | `3272ac30c67910ae09e3ee2e16f4ce86d1e0907c155115c6ed00e9b988c5d8e5` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_A_orders.jsonl.gz` | 570,960 | `aab1e8f11e7628219e3d3cc2dc00c2cb7f291a3e9b643722cd81bf0069ee2b22` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_B.json` | 56,496,255 | `5e7c2e5a48e0ed8815a05fdc9fcced103ebb669a169e12597248257d6df0c591` | no | OVER_50MB_GITHUB_WARNING |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_B_decisions.jsonl.gz` | 64 | `dbde156309f57b8a7735bfd7c1abd7d7f2d423ef51451f7e9b0fa74c06ef1260` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_B_fills.jsonl.gz` | 177,384 | `8281b8afe2c915f952e9225499cc8b95c1fcff51e862df935df6ab30b7207cad` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_B_orders.jsonl.gz` | 557,508 | `f04aa0aad767eb35a4a10c58af53de0fa29a1a8280f22f5fbec124463ba07447` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_C.json` | 11,504 | `11489eecb4fc343228bc379261224b5062782248b773f8a6a1428862bd17bbde` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_C_decisions.jsonl.gz` | 909,647 | `ffc2f1c929cdf272263e855f37a6ebf5ff03f506414e4501d94f18c6524c8b98` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_C_fills.jsonl.gz` | 190,447 | `fc58bd12ab1485e49597ca23fc3a21e6061e22e06988e8f2b76e7ec856d36e16` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_C_orders.jsonl.gz` | 582,225 | `127464e2c78567a4245dcf102b1df048230e0f3315f01d13cbbe58ef931d2109` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_D.json` | 2,342,066 | `9a6a600ddc7afd4bce16468d57bccf32a2b60875381ef8c4d3889e0a167dd87e` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_D_decisions.jsonl.gz` | 826,245 | `0c3c55742242d5a2cb13e569884d2eff3ff4c33de5e2aba10e84701f01f25ee2` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_D_fills.jsonl.gz` | 168,092 | `73195f1392d28007fbaee2e7141e0383f4193e4c0f5b13d32919786f9f368497` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q10000_d5_D_orders.jsonl.gz` | 550,396 | `df134386a3f3b985a1157bd60c4110bffc76e927da73aa15796f169e21f99cc9` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_A.json` | 11,409 | `50476534c2692ac3c54af86924c45bea5aea0b8311cb3e4465b0e1d3593262c4` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_A_decisions.jsonl.gz` | 66 | `3c4b3569fe317dd55e3e3ec78e6d8b2d0d7ed560a2ac019b0589bc3808d310e7` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_A_fills.jsonl.gz` | 598,114 | `50668e03b7e2577230974d032eb3a0d00019fa8dac1a4418f29299434378e2e1` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_A_orders.jsonl.gz` | 576,465 | `ae57baa132f363a48e18674c126a53d5e4a88dd4dd5327f857bf1ef1c55e26fd` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_B.json` | 56,907,767 | `370ccbcf342db59aa1697d448d3274791cf17c015d8e9eead17d788fbe79ffb5` | no | OVER_50MB_GITHUB_WARNING |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_B_decisions.jsonl.gz` | 66 | `c0bad55ee32de8ffcd51f6143cdec377c0e93c4730fc4a9297a83f8f8aa9eeea` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_B_fills.jsonl.gz` | 559,974 | `6c050d73f52e1cd8e4a2c582efdcfdb5f0933621611d09ad257a3f9bef2cddf4` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_B_orders.jsonl.gz` | 568,542 | `47fba8c5d188e8b048ab150d744ecb4e259d93079854faeea1610b082fccfe15` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_C.json` | 11,522 | `f381db01b02552542ab6382b23b7c57ac3b4101edf1fa3731d683881f8e6dc7c` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_C_decisions.jsonl.gz` | 920,024 | `c81ca0468698988c484e5ba00399169fc23b1e166891719d3ed91f13aa6ca761` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_C_fills.jsonl.gz` | 594,536 | `84f71618a2cae94f5760bdce5b1f1722eff0ee7a1043d359e1c5048776ca0e3a` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_C_orders.jsonl.gz` | 587,577 | `1b737f7089a972b074f79c5a8e17546c86c9538ef19a774cb5a5280025bf5513` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_D.json` | 2,356,708 | `fc38cfbc134ca313a6cd2b8763ef49c3a56f6b5cc763c50f82e2b4545cda898f` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_D_decisions.jsonl.gz` | 838,293 | `c26827d0dbe1d9426343deeecc0d8b3e389ccf60f9dd24b683ff1ca1839066e4` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_D_fills.jsonl.gz` | 534,943 | `52d27b67ef097b50171ef59acb8309fdf80f9c964fe7656d674d56000c927d23` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d0.25_D_orders.jsonl.gz` | 569,765 | `9f3417777cdffa17d5caaa2d14463976afd3c0a643e4eefd902f817842534bc7` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_A.json` | 11,427 | `02b445fcd7dccfce0e7ffd98a96bf29ae1107300a17bc50c61647b1baff53ace` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_A_decisions.jsonl.gz` | 63 | `3dea65fad9fbce444692ec4d7c511a10a822d018492d29aca48318ac75d35e04` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_A_fills.jsonl.gz` | 569,576 | `9fc1fdcd9e5299e72529b334d2c66e6a8579f0a4f908453d1d147576fd7277dc` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_A_orders.jsonl.gz` | 570,990 | `c96793d8361e400a8e49c6f9f5127ea6f986524ae594f227893ad348d8ee7e25` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_B.json` | 56,896,894 | `fa2ccdb8514191276ff0a3792fc12a9e1d2ffdd5b550f9a08510f7af806899ad` | no | OVER_50MB_GITHUB_WARNING |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_B_decisions.jsonl.gz` | 63 | `90a3afd9fd508a5d4f7ed548286aed64fbd1fa2d97e86f84581953a1ef882367` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_B_fills.jsonl.gz` | 532,691 | `13d871cc02692e7c9d080c4e80eb104244210479fcfce8722a817d84fdb628ce` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_B_orders.jsonl.gz` | 562,904 | `76ee281e81c57762c899276d7846541508f2ce8649a5679fdf9f93b7b8a32a8e` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_C.json` | 11,547 | `de3e0b73f2800ca94ee2cc5cff3b3dd77196247700b0b8b80089df7c790a757a` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_C_decisions.jsonl.gz` | 919,232 | `d63a3f1a622968c0fe92a405bf5cfa324287b47d1ac2c7584dbb79b9025e029d` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_C_fills.jsonl.gz` | 565,188 | `8c19b56e5bc82c239ea98a99a26e3ebf845dbd9cb37f557d074a17bc63015887` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_C_orders.jsonl.gz` | 582,782 | `05951c7e688b2607b4b9c5dc378a4923b576f67a1e230aa38d967eaad4a6651a` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_D.json` | 2,356,849 | `a0a638407edd78e1bf282cda1012a2cb8a6929c98c03ced799538cda1efe2d33` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_D_decisions.jsonl.gz` | 837,745 | `af14f73e241d6b7dfebf90fa6e7a15729632c2fd6956bed1f8f6d8e391570d6e` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_D_fills.jsonl.gz` | 509,313 | `fb07cdcab2ab36cf8229db77f962bd94e8952050e9365dd3b3fa472fcb1679dc` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q3300_d5_D_orders.jsonl.gz` | 565,589 | `d215a015c356c62c250b770a2ca0825bae44786daeb38384da59a469702a28f2` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q7_analyze.log` | 9 | `a4bccf5c13ef5ff8311e59b34d492bc7072a55298723601a6a9c127053aee8fc` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q7_pin_check.log` | 39 | `384da763781756f84a47539aa0be34af81425add70084e65e2d9a286f442ee7b` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q7_run_experiment.log` | 213 | `3418b01bcf43c2743f00b50c095cb78cdb2bd214f8e4be9354ab20c38335fdbc` | no |  |
| Y | result | RUN_OUTPUT | `nfl_paircheck_lab_20260922/results/q7_verify.log` | 9 | `8f5a1374b3eb9532a67c0de915a0810ea089fc304c33a44642a7f4878984803e` | no |  |
| N | result | EXAMINER_PINNED_BUT_BOX_BYTES_DO_NOT_MATCH_PIN | `nfl_paircheck_lab_20260922/results/verification.json` | 208 | `9cde03dc3d52eb3ab9d18024155c341451de9e1e8836356cdcf3cf1d0ac006e4` | yes `485a7149a13dff19b12e493a57ae36f40908ec62` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, EXAMINER_PIN_MISMATCH_SCORED_BYTES_MISSING |
| Y | scored_input_pin | EXAMINER_PINNED_INPUT | `nfl_paircheck_lab_20260922/FROZEN_EXPERIMENT.json` | 8,884 | `b0dd91699d2170e42c3a0ae9e27769a80f64f8121b116da030f253ac0d8a7f2b` | yes `1b1e160a786c64f535602f1d439ffec67f14b999` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, MATCHES_EXAMINER_PIN |
| Y | scored_input_pin | EXAMINER_PINNED_INPUT | `nfl_paircheck_lab_20260922/EXPERIMENT_SPEC.md` | 10,419 | `cdfba7817a4a13c51b3aec3dc2256e7de1cd61386d9e1b359d85b2b65a78344f` | yes `4d169acdad9a19731fffcd371e174ed1d0bd2614` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, MATCHES_EXAMINER_PIN |
| Y | stamp | EXAMINER_SCORECARD | `lab/governance/astra/packets/Q7_EXAMINER_SCORECARD_2026-09-22.md` | 6,554 | `65adfaf3f30f14545d12b81cba900b1990f019ea3d5c28753089c97e07590636` | no |  |
| Y | stamp | EXAMINER_REPORT | `lab/governance/astra/reports/RPT-Q7.md` | 2,093 | `05345c3e2c3a04f3c218c91d99e5ec0fe3b6204383fd9bc725e6ce1e4293a7c8` | no |  |
| Y | stamp | EXAMINER_REPORT | `lab/governance/astra/reports/RPT-Q7-PAIRCHECK.md` | 160 | `731beb835459073b756e0632edf9787caaad3f0c9602725e22eaed0d77d9e17b` | no |  |
| Y | stamp | PR_REVIEW | `lab/governance/astra/packets/Q7-PR2-REVIEW_2026-09-22.md` | 2,852 | `d47dd7b992eecc0e3bc8d80435a368d03fd3085e1f10a031ce4be6e42f7cedd6` | no |  |
| Y | stamp | CEMETERY_CARD | `lab/governance/astra/cemetery/CEM-ASTRA-20260922-001_Q7_ARM_B.md` | 2,040 | `1061864d8ef6a6bf44b8caafb42dd8e96562455c371a74bc75b2d1c0f27f65e8` | no |  |

Notes:
- `nfl_paircheck_lab_20260922/results/paircheck_effects.json`: Matches Examiner Q7 scorecard pin 5d87ea61… [V]. Also matches the PR38 body desk-verified hash.
- `nfl_paircheck_lab_20260922/results/verification.json`: Examiner Q7 scorecard (packets/Q7_EXAMINER_SCORECARD_2026-09-22.md) pins scored verification.json sha256 eb1586bf13b1631951a4f177293350cb89fc7948a50fbb7044f4f05313ebc06f (status VERIFIED). Box bytes are sha256 9cde03dc3d52eb3ab9d18024155c341451de9e1e8836356cdcf3cf1d0ac006e4 (status NOT_RUN_INPUTS_MISSING) and equal main blob 485a7149. The scored bytes were NOT found anywhere on the box (all 4 box copies of this path are the NOT_RUN stub). SCORED_BYTES_MISSING_FROM_BOX — UNVERIFIED; nothing to land.

Box source dirs: `/workspace/lab/astra-science/nfl_paircheck_lab_20260922/results/`; stamps under `/workspace/lab/governance/astra/{packets,reports,cemetery}/`

### Q7-B-REHAB-P1

| incl | category | role | proposed repo path | bytes | sha256 | on main (blob) | flags |
|---|---|---|---|---|---|---|---|
| Y | result | STAMP_COPY_IN_RESULTS_DIR | `nfl_q7_rehab_p1_cadence_20260923/results/EXAMINER_ACK_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.json` | 4,159 | `a91e399c213d566857142563d85ad46b4c4019a776d020236ac397938287054e` | no |  |
| Y | result | STAMP_COPY_IN_RESULTS_DIR | `nfl_q7_rehab_p1_cadence_20260923/results/EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` | 3,635 | `21d0813990727ec05f3633bc27c6e43c9e94758e73460773aa07f0b92fe00c5a` | no |  |
| Y | result | RUN_STATUS_STUB | `nfl_q7_rehab_p1_cadence_20260923/results/NOT_RUN.json` | 538 | `ff043ad08171e7d207507f44484bf2194eec3c476f4f94922bcc0fe9b26b1fd5` | yes `bb83bf37dfa9c5c92e63dcf7a239b58c5e5cb6c3` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | STAMP_COPY_IN_RESULTS_DIR | `nfl_q7_rehab_p1_cadence_20260923/results/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json` | 20,443 | `8edc708dc7727c7132578f221a79372b7f8c3622826759516509f7a14ca8e642` | no |  |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/TAPE_WALK_ARTIFACT_DIGEST.json` | 8,366 | `b4657e3aa0120ca4540693b90a899beb75c2011bee121627aa314f588bbd6714` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_STATUS_STUB | `nfl_q7_rehab_p1_cadence_20260923/results/UNIT_RESULTS.md` | 1,670 | `e04aec7f4deed276400c1f36f8e2cd66e3a1c5f960b5355830da1455bbef5d7f` | yes `bcbe9e244f9f0410dac24827a92043bba6495915` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/experiment_summary.json` | 13,965 | `8ca717cff8a138a5e045645a3ddb89bf84b9cf0f2815962936a8305f4b058886` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/parent_source_pins_reverify.json` | 583 | `11077c6d85dc73d73d929972208e54296faed291ca24a66cbe31fb41031485db` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/positive_control_compare.json` | 5,247 | `d334cb2efbca694c4224df11de6383af2afee1b5e1979907523c61b86a3fe049` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B0.json` | 56,496,276 | `029e45d592e1d310098d507574814b319500fdaab0f96adf6e92f4ed5c93fb7d` | no | OVER_50MB_GITHUB_WARNING, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B0_decisions.jsonl.gz` | 68 | `60b341e89468fd04e14ada298247d6213a10ce38e42731e02f13a82f49491676` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B0_fills.jsonl.gz` | 183,865 | `1db67bd179f17a90c72dbb26fe2a9f5a1cf1fd4d8b75cdf1fa301b2478b155d5` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B0_orders.jsonl.gz` | 561,342 | `bcdd495939eb616462c3b29eb6f9bec783a55b21426f381e7867e66c44a923f5` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B1.json` | 374,946,853 | `0e70397d54764e82629294d338582a9eccabdd598f5d0bc82b2a4b6c33cd8f4c` | no | EXCEEDS_GITHUB_100MB_LIMIT, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B1_decisions.jsonl.gz` | 68 | `54b04fb0820e0584cb665bcf9507e29547c52b92aee389ad101620e7320abb06` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B1_fills.jsonl.gz` | 92,997 | `e12fd1d49ac343e8b206d7347ab9186d9c42b60271221e4b62a34ae068d21587` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_B1_orders.jsonl.gz` | 23,157 | `06a5ce655aea55cbb36894f975c959b3853f27ee0fac8d70fd732ce73865266e` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_D.json` | 2,342,063 | `7903147db0ed6a0c908987115273293a363a5ebec6169853c7167a523fbbfdd5` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_D_decisions.jsonl.gz` | 827,009 | `aca82c5246f631b27d587c94aa736ea95889fb6a4625eaea8f2c2d6347f48615` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_D_fills.jsonl.gz` | 174,314 | `4db1a6ec477810e8b70e9b157a71ebf5e689052cdf126c30e061573cc79bf158` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d0.25_D_orders.jsonl.gz` | 553,659 | `ec6c59b5d78c0a6a0478d6cecd62eefc51745b8f996c1a256375fa7a0ef8331c` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B0.json` | 56,496,284 | `e611001dae9ea39b10506d48b4cfc90cbffbe5501669ea9d3a658f75bb2eec2a` | no | OVER_50MB_GITHUB_WARNING, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B0_decisions.jsonl.gz` | 65 | `826e1e838023d7cc15ef27f2963e3b5e328a28a400e06dc0903ab464ad51ff8b` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B0_fills.jsonl.gz` | 177,385 | `1f264c35bda2d86e449610a90787b734b368e808200808adf12b65237ffe1433` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B0_orders.jsonl.gz` | 557,509 | `d33bd72e6a9688f150e5fde1131654ceb901dd467459522b744520d697562cbe` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B1.json` | 374,931,398 | `6234227aacae28e1b9003da1a54e12205e493e0d870c549c776b53c4f5c76fea` | no | EXCEEDS_GITHUB_100MB_LIMIT, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B1_decisions.jsonl.gz` | 65 | `182733846b34d40275592f1b75b75c49b57fa49e37940d1272294bda163d535b` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B1_fills.jsonl.gz` | 89,280 | `c8ea3e923f6280e73f4f5fb9124b807cbde7cb0890a92f4c58b247a2883997ba` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_B1_orders.jsonl.gz` | 23,170 | `7415585a94a7cc4dfe6da943d68b90c078598b499ae42e7ec07259ca8dc4e3a2` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_D.json` | 2,342,094 | `0bc704dc8df4c1a8529182b7f7cf89a3abcdff58c508320030841bc58dd74c25` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_D_decisions.jsonl.gz` | 826,245 | `94d006c9bc650faa3cd3cbaf356fd63075e0b7236147c22404fc8d343018bbeb` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_D_fills.jsonl.gz` | 168,092 | `c42be0c49c03e5c57160104e9bde389106707115aa8f4f82fe15ca6322b46291` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q10000_d5_D_orders.jsonl.gz` | 550,396 | `f25a19bef1cd24752a42e6a7d7e73c682f7ef69875665357ad2a067ead56bbbf` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B0.json` | 56,907,796 | `9c0fb40a49a52c5cb1b5bfb3f0276f4406d938853c81b0d7b5cc05e720aff2c1` | no | OVER_50MB_GITHUB_WARNING, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B0_decisions.jsonl.gz` | 67 | `e34220273ce4a2622ab5458aed4be114569b813a682f7691cbe1c83d28268ca8` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B0_fills.jsonl.gz` | 559,975 | `5bf6f3d068f10fcd2ff078b7b8c4a1023e625fd6922f09ab68a6db00ed2603b6` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B0_orders.jsonl.gz` | 568,543 | `df41ddfd4f8019c3d34882ac442a35ec669f6cfe3f57b4afff431cf7b42bd12d` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B1.json` | 374,957,293 | `0c505fae29b579cf6dfe2ff5a3aa45b0fffa6d674ff1f9fef4ac71ffab3c2a8c` | no | EXCEEDS_GITHUB_100MB_LIMIT, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B1_decisions.jsonl.gz` | 67 | `76568b876905fe8ce408a3edfb7fc4caf7f99e088528e938c4fa8c1e103cee47` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B1_fills.jsonl.gz` | 208,808 | `1d0f2c9b0b0ed31d1a1709db0f02e2d72978fbfbf7938bfbd4801145debe0bf4` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_B1_orders.jsonl.gz` | 30,206 | `7afa7d5c88aed45a164f3ebe91713bd7028512224b0f8cd8a0f3791e249f2e83` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_D.json` | 2,356,736 | `21b433a9645914e589491fafa5109b3b1d6c7333c3f425cecd7dd22ef4c69e91` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_D_decisions.jsonl.gz` | 838,293 | `d9027386ef8bb9c16009516286781d87398698cf860f82a42f77d34368769a25` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_D_fills.jsonl.gz` | 534,943 | `43b0a2cda996875b5fc591c660853457c244f39a244c81250a69ec78afffb2ab` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d0.25_D_orders.jsonl.gz` | 569,765 | `28c9fe6eaf1fdc920ff44f7a3923b64f690860c9dd6d90e2bc04fc3484970fba` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B0.json` | 56,896,923 | `29c288889c7219d1531bc6ed9fb987da1b54695b13bd7d97c6f62ce450c2f30d` | no | OVER_50MB_GITHUB_WARNING, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B0_decisions.jsonl.gz` | 64 | `149ec5028974cfb0228852c11fbfe89adc259e869ccc15f816b13b403860e60c` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B0_fills.jsonl.gz` | 532,692 | `1a2ed482435ad674f5e6b36b8a283d46e035a2847292d3bdfa2e76d3ccbaeef5` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B0_orders.jsonl.gz` | 562,905 | `c370bd9b633a848bdedbea1ac1ee9b313c606896f3dfb351ed60495c11d74dcf` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B1.json` | 374,940,624 | `a67222c876aa51ae876d4004aa0f9630a630cae2defc06ab95fd3f4daaaa498e` | no | EXCEEDS_GITHUB_100MB_LIMIT, MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B1_decisions.jsonl.gz` | 64 | `a5d6fbaf1f137311322effd8689d57992c2aa2c00498f0de8bbbd0ec2a41d427` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B1_fills.jsonl.gz` | 201,545 | `12a92972f19660422b09407e279354aa1abeca6aa69fcbc283f2ceafb3fcef4f` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_B1_orders.jsonl.gz` | 30,103 | `08650c8774b43e2f6dd6692f2f758ab3b83072e8ccf087dd568a20931a2c66f2` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_D.json` | 2,356,877 | `9515226b12110bc2830750c8309b27e57f996ae0d29878fc21422de3e68f3acf` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_D_decisions.jsonl.gz` | 837,745 | `b2eecfcfb1adf9aee32829e263874e98422f02729164d90ad654cada55b21f20` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_D_fills.jsonl.gz` | 509,313 | `777c3f74a8742b5b2381c1028a2ae081a2526db9d4b676bf99157a663e3c3a58` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/q3300_d5_D_orders.jsonl.gz` | 565,589 | `b10620b641b1d466ceb5584d96e23f986d6421f0531de030bbd6696c92bf43aa` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | result | RUN_OUTPUT | `nfl_q7_rehab_p1_cadence_20260923/results/selection_status.json` | 701 | `94ea32f8a89fc90dee02af635c9f25e4f89b3a7d2ea932a6a9c292ede31877ce` | no | MATCHES_TAPE_WALK_ARTIFACT_DIGEST |
| Y | stamp | EXAMINER_SCORECARD | `lab/governance/astra/packets/EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` | 3,635 | `21d0813990727ec05f3633bc27c6e43c9e94758e73460773aa07f0b92fe00c5a` | no |  |
| Y | stamp | EXAMINER_ACK | `lab/governance/astra/packets/EXAMINER_ACK_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.json` | 4,159 | `a91e399c213d566857142563d85ad46b4c4019a776d020236ac397938287054e` | no |  |
| Y | stamp | CONDUCTOR_ACCEPT | `lab/governance/astra/packets/CONDUCTOR_ACCEPT_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.json` | 882 | `42304a30c9024605da8eabc68bf874a13f02681c8a5774d9d8b78267589e810c` | no |  |
| Y | stamp | CONDUCTOR_ROUTE | `lab/governance/astra/packets/CONDUCTOR_ROUTE_Q7_B_REHAB_P1_TAPE_WALK_EXAMINER_2026-09-23.json` | 770 | `2d12582e38f413f496e77e1f3f72121407585aa2909c832b21de37d26214da32` | no |  |
| Y | stamp | SIMULATOR_HANDOFF_OR_READY | `lab/governance/astra/packets/SIMULATOR_HANDOFF_EXAMINER_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json` | 2,811 | `0a99fc27570df6f8ff72ec5d1afedf482ef91fee1b74bfb84cf1a77b54d4c07c` | no |  |
| Y | stamp | SIMULATOR_HANDOFF_OR_READY | `lab/governance/astra/packets/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json` | 20,443 | `8edc708dc7727c7132578f221a79372b7f8c3622826759516509f7a14ca8e642` | no |  |
| Y | stamp | EXAMINER_SCORECARD | `lab/governance/astra/packets/Q7_B_REHAB_P1_CADENCE_600/EXAMINER_SCORECARD_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.md` | 3,635 | `21d0813990727ec05f3633bc27c6e43c9e94758e73460773aa07f0b92fe00c5a` | no |  |
| Y | stamp | EXAMINER_ACK | `lab/governance/astra/packets/Q7_B_REHAB_P1_CADENCE_600/EXAMINER_ACK_Q7_B_REHAB_P1_TAPE_WALK_KILL_2026-09-23.json` | 4,159 | `a91e399c213d566857142563d85ad46b4c4019a776d020236ac397938287054e` | no |  |
| Y | stamp | SIMULATOR_HANDOFF_OR_READY | `lab/governance/astra/packets/refiner/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json` | 20,443 | `8edc708dc7727c7132578f221a79372b7f8c3622826759516509f7a14ca8e642` | no |  |

Notes:
- `nfl_q7_rehab_p1_cadence_20260923/results/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json`: sha256 equals EXAMINER_ACK canonical_ready_sha256 8edc708d… [V]. (TAPE_WALK_ARTIFACT_DIGEST.json lists an earlier sha fcd93c92… for this name; digest was written before the final READY bytes [I].)
- `lab/governance/astra/packets/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json`: sha256 equals EXAMINER_ACK canonical_ready_sha256 8edc708d… [V]. (TAPE_WALK_ARTIFACT_DIGEST.json lists an earlier sha fcd93c92… for this name; digest was written before the final READY bytes [I].)
- `lab/governance/astra/packets/refiner/SIMULATOR_READY_Q7_B_REHAB_P1_TAPE_WALK_2026-09-23.json`: sha256 equals EXAMINER_ACK canonical_ready_sha256 8edc708d… [V]. (TAPE_WALK_ARTIFACT_DIGEST.json lists an earlier sha fcd93c92… for this name; digest was written before the final READY bytes [I].)

Box source dirs: `/workspace/lab/astra-science/nfl_q7_rehab_p1_cadence_20260923/results/`; stamps under `/workspace/lab/governance/astra/packets/`

### R3-P2

| incl | category | role | proposed repo path | bytes | sha256 | on main (blob) | flags |
|---|---|---|---|---|---|---|---|
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/EMPTY_RESULTS.json` | 60 | `649d09e14c5872d71b0d4247642b92cc470a4b037c6207940c29736159dce963` | no |  |
| Y | result | EXAMINER_PINNED_SCORED_BYTES | `lab/governance/astra/packets/r3_p2_queue_position/results/abs_err_signed_bias.json` | 52,006 | `f7e83a28abbf2f216fafe316a153aff27a94a27f231f5aa65bfd8310e6224141` | no | MATCHES_EXAMINER_PIN |
| N | result | MECHANIC_COMPUTED_NOT_EXAMINER_SCORED | `lab/governance/astra/packets/r3_p2_queue_position/results/abs_err_signed_bias_trade_step_retry.json` | 11,366 | `755244e25cb0cc387347896d88b708e10d58e001eed40024fc78396c3e384857` | no |  |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/archive/MECHANIC_DEMO_TRADE_STEP_SERIES_pass1_503block.md` | 3,668 | `09484574a734f252bc80ba8ef1d61229bad9228ebedb333f7365a7723dc9e466` | no |  |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/archive/demo_trade_step_sample_series_pass1_503block.json` | 43,128 | `8c8d34e6498449c7557366089301d001686d7779bcf418d2dec3a4f5ed9120e4` | no |  |
| Y | result | EXAMINER_PINNED_SERIES | `lab/governance/astra/packets/r3_p2_queue_position/results/demo_queue_sample_series.json` | 70,373 | `74ef9a9bb54054691e26b7b752568c8e833f51d21292034b1f40b9f3ca4ba8b4` | yes `288ae9626b564d042d7b08359e60578c9e41fd29` identical | ALREADY_ON_MAIN_IDENTICAL_NO_CHANGE_NEEDED, MATCHES_EXAMINER_PIN |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series.json` | 43,128 | `8c8d34e6498449c7557366089301d001686d7779bcf418d2dec3a4f5ed9120e4` | no |  |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series_503_blocked.json` | 43,128 | `8c8d34e6498449c7557366089301d001686d7779bcf418d2dec3a4f5ed9120e4` | no |  |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series_retry.json` | 57,909 | `6e2c82570e72efd19c4c77cac01c8727965938dfbceefec7a8a7d2f2db667db1` | no |  |
| Y | result | EXAMINER_PINNED_LABELS | `lab/governance/astra/packets/r3_p2_queue_position/results/estimate_ahead_labels.json` | 68,502 | `f89c06dc1639b194c9d026e157fbfbc2a8b527853afe698dd1f77389eb34c964` | no | MATCHES_EXAMINER_PIN |
| N | result | MECHANIC_COMPUTED_NOT_EXAMINER_SCORED | `lab/governance/astra/packets/r3_p2_queue_position/results/estimate_ahead_labels_trade_step_retry.json` | 21,091 | `e109ac02183abdf8b350e56b5e865250855a3caa55c474d76be32f7e4e1422b1` | no |  |
| N | result | RESULTS_DIR_UNSCORED_SUPPORTING | `lab/governance/astra/packets/r3_p2_queue_position/results/first_demo_queue_poll.json` | 4,319 | `b0212da2f0d03948f9c933bb08d6fc0f1bb292733553bcef7c01d6e75874258e` | no |  |
| Y | scored_input_pin | EXAMINER_PINNED_INPUT | `lab/governance/astra/packets/r3_p2_queue_position/harness/FROZEN_KNOBS.json` | 1,071 | `9a3534219b9be6cbfccb259b23e1245cec682dcee754b5f6a004c55d5354d2a6` | no | MATCHES_EXAMINER_PIN |
| N | result_duplicate | DUPLICATE_OF_PINNED_LABELS | `kalshi_r3p2_queue_position_lab_20260923/results/_test_labels.json` | 68,502 | `f89c06dc1639b194c9d026e157fbfbc2a8b527853afe698dd1f77389eb34c964` | no |  |
| N | result_duplicate | DUPLICATE_OF_PINNED_LABELS | `kalshi_r3p2_queue_position_lab_20260923/results/estimate_ahead_labels.json` | 68,502 | `f89c06dc1639b194c9d026e157fbfbc2a8b527853afe698dd1f77389eb34c964` | no |  |
| Y | stamp | EXAMINER_SCORECARD | `lab/governance/astra/packets/EXAMINER_SCORECARD_R3_P2_ABS_ERR_SIGNED_BIAS_2026-09-23.md` | 3,764 | `b21ed6f07f1646b84ef23b865ae2518ad29cc9e149a1071d00820133fdeae90a` | no |  |
| Y | stamp | EXAMINER_ACK | `lab/governance/astra/packets/EXAMINER_ACK_R3_P2_ABS_ERR_SIGNED_BIAS_SCORED_2026-09-23.json` | 3,281 | `c639f8d9b5f3295bdcbbc3d24708f97cc7a98ed394f9c29635c285295d6f1bb5` | no |  |
| Y | stamp | CONDUCTOR_ACCEPT | `lab/governance/astra/packets/CONDUCTOR_ACCEPT_R3_P2_ABS_ERR_SIGNED_BIAS_SCORED_2026-09-23.json` | 1,196 | `74eaa85cc20b6b41903551ccccb11dfebcde39eeb4864472410a475c6787e05a` | no |  |
| Y | stamp | CONDUCTOR_ROUTE | `lab/governance/astra/packets/CONDUCTOR_ROUTE_R3_P2_ABS_ERR_SIGNED_BIAS_EXAMINER_2026-09-23.json` | 1,733 | `d748c3ba32206fb91ef644db52931f6442945d62054cd4e41b331e8d0bbd1070` | no |  |
| Y | stamp | SIMULATOR_HANDOFF | `lab/governance/astra/packets/SIMULATOR_HANDOFF_EXAMINER_R3_P2_ABS_ERR_2026-09-23.json` | 3,566 | `8e71fc968d78db577537d38d6365d83960b4e4dba26128ca130ce380c2969608` | no |  |
| Y | stamp | EXAMINER_SCORECARD | `lab/governance/astra/packets/r3_p2_queue_position/EXAMINER_SCORECARD_R3_P2_ABS_ERR_SIGNED_BIAS_2026-09-23.md` | 3,764 | `b21ed6f07f1646b84ef23b865ae2518ad29cc9e149a1071d00820133fdeae90a` | no |  |
| Y | stamp | EXAMINER_ACK | `lab/governance/astra/packets/r3_p2_queue_position/EXAMINER_ACK_R3_P2_ABS_ERR_SIGNED_BIAS_SCORED_2026-09-23.json` | 3,281 | `c639f8d9b5f3295bdcbbc3d24708f97cc7a98ed394f9c29635c285295d6f1bb5` | no |  |
| Y | stamp | SIMULATOR_HANDOFF | `lab/governance/astra/packets/r3_p2_queue_position/SIMULATOR_HANDOFF_EXAMINER_R3_P2_ABS_ERR_2026-09-23.json` | 3,566 | `8e71fc968d78db577537d38d6365d83960b4e4dba26128ca130ce380c2969608` | no |  |
| Y | stamp | MECHANIC_COMPUTE_RECORD | `lab/governance/astra/packets/r3_p2_queue_position/MECHANIC_ABS_ERR_SIGNED_BIAS_2026-09-23.md` | 2,473 | `c316d4f2f8b091d3245ab3c12325b74e28eeca48bbc4305d3684c792653c30b2` | no |  |

Notes:
- `lab/governance/astra/packets/r3_p2_queue_position/results/EMPTY_RESULTS.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/abs_err_signed_bias_trade_step_retry.json`: Written 2026-09-24 ~19:45 ET by Mechanic trade-step retry (MECHANIC_TRADE_STEP_RETRY_ABS_ERR_SIGNED_BIAS_2026-09-24.md: "plumbing pass, not a calibration score"). No Examiner stamp located. HELD out of the results-only PR.
- `lab/governance/astra/packets/r3_p2_queue_position/results/archive/MECHANIC_DEMO_TRADE_STEP_SERIES_pass1_503block.md`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/archive/demo_trade_step_sample_series_pass1_503block.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series_503_blocked.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/demo_trade_step_sample_series_retry.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `lab/governance/astra/packets/r3_p2_queue_position/results/estimate_ahead_labels_trade_step_retry.json`: Written 2026-09-24 ~19:45 ET by Mechanic trade-step retry (MECHANIC_TRADE_STEP_RETRY_ABS_ERR_SIGNED_BIAS_2026-09-24.md: "plumbing pass, not a calibration score"). No Examiner stamp located. HELD out of the results-only PR.
- `lab/governance/astra/packets/r3_p2_queue_position/results/first_demo_queue_poll.json`: In R3-P2 results dir but not pinned by the Examiner abs_err/signed_bias scorecard or ACK. Listed for completeness; Conductor to decide landing.
- `kalshi_r3p2_queue_position_lab_20260923/results/_test_labels.json`: Box lab dir name kalshi_r3p2_... (no underscore) differs from main lab kalshi_r3_p2_...; byte-identical to pinned labels. Not needed for landing.
- `kalshi_r3p2_queue_position_lab_20260923/results/estimate_ahead_labels.json`: Box lab dir name kalshi_r3p2_... (no underscore) differs from main lab kalshi_r3_p2_...; byte-identical to pinned labels. Not needed for landing.

Box source dirs: `/workspace/lab/governance/astra/packets/r3_p2_queue_position/results/`, `/workspace/lab/astra-science/kalshi_r3p2_queue_position_lab_20260923/results/`; stamps under `/workspace/lab/governance/astra/packets/`. Alternative repo home noted per pinned file: main lab `kalshi_r3_p2_queue_position_lab_20260923/results/` (has EMPTY_RESULTS.json b15243a5, UNIT_RESULTS.md 07bbbb9b).

Absolute box path for every row = `/workspace/lab/astra-science/<repo path>` for top-level lab paths, or `/workspace/<repo path>` for `lab/governance/astra/…` paths (also listed verbatim in the JSON `box_path`).



---

## Note appended 2026-09-24T19:55:12-04:00 (ET): tier split, batch 3, duplicates, cold evidence (the JSON is not rewritten; see `RESULTS_LANDING_MANIFEST_2026-09-24_ADDENDUM_01.json`)

- **Tier A:** `registry/RESULTS_LANDING_TIER_A_SHA256SUMS_2026-09-24.txt`, sha256 `89662fa6bc939092fb68468c025ea136c213d6a7f3c037045126f7d03596d36b` [V]. 139 files ≤25 MB, handed to the Steward.
- **Tier B:** `registry/RESULTS_LANDING_TIER_B_CHECKSUM_ONLY_2026-09-24.txt`, sha256 `1c677347328d89dab52a19b7740c3b845e5904bc6d76bbfb10adbca73dd109ee` [V]. 13 files >25 MB, checksum-only pending a Conductor ruling.
- **139 + 13 = 152.** That is the 159 included here minus the 7 proposed paths already on main byte-identical [V set difference].
- **Tier A batch 3 (Conductor ruling c):** `registry/RESULTS_LANDING_TIER_A_BATCH3_SHA256SUMS_2026-09-24.txt`, 4 files, all ≤25 MB:
  - the two R3-P2 trade-step retry outputs: `abs_err_signed_bias_trade_step_retry.json` `755244e2…`, `estimate_ahead_labels_trade_step_retry.json` `e109ac02…`
  - the Examiner stamp `EXAMINER_SCORE_R3_P2_TRADE_STEP_RETRY_PLUMBING_2026-09-24.json` `e66d2636…` (MEASUREMENT_PLUMBING_PASS)
  - the Conductor ruling `CONDUCTOR_RULING_R3_P2_WARM_SHELF_2026-09-24.json` `7fa4455f…`
  - These rows above were marked HELD; they are now **added** by ruling. The rows above are not edited.
- **Dropped from the landing set:** the 2 duplicate label files `kalshi_r3p2_queue_position_lab_20260923/results/{_test_labels.json,estimate_ahead_labels.json}` (both `f89c06dc…`, byte-identical to the pinned labels). They stay on the box.
- **Still HELD pending a stamp:** the 7 unscored R3-P2 results-folder files. Note: `demo_trade_step_sample_series_retry.json` (`6e2c8257…`) is pinned by the new Examiner plumbing stamp (match=true). Flagged for the Conductor; still held.
- **Q7 `verification.json` pin `eb1586bf13b1…`:** **UNVERIFIED_BYTES_MISSING**. The Examiner verdict stands. The Simulator searches first. If it regenerates after the P2 walk and the result does not equal `eb1586bf…`, it goes back to the Examiner. The pin is not rewritten.
- **Tier B cold evidence:** gzip copies in `/workspace/lab/evidence_cold/2026-09-24/` (`MANIFEST.json`, `SHA256SUMS.txt`). All 13 round-trip to the source sha256. All are under 2 GiB (total 20,946,068 bytes). Nothing pushed. No LFS.

## Addendum 2026-09-24 ~19:59 ET — Conductor ruling: land demo_trade_step_sample_series_retry.json
- sha256 `6e2c82570e72efd19c4c77cac01c8727965938dfbceefec7a8a7d2f2db667db1` (57,909 bytes) moves from HELD to LANDING via `RESULTS_LANDING_TIER_A_BATCH3B_SHA256SUMS_2026-09-24.txt`.
- Label: **COLLECTED_POST_FREEZE** (not pre-declared). Pinned by Examiner stamp e66d2636; needed to reproduce.
- Remaining held R3-P2 unscored files: 6.
