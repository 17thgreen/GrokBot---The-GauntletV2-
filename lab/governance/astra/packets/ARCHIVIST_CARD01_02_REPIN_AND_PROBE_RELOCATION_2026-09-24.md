# Archivist: card 01/02 re-pins + ElectIndex probe relocation (2026-09-24 ~20:12 ET)

Authority: Conductor rulings received 2026-09-24 ~20:08 ET (items 1–3 + card 02). Append-only; no frozen file edited by the Archivist.

## 1. ElectIndex pre-freeze probe files: RELOCATED (not deleted) [V]
- From: `packets/card01_hybrid_forecast/source_probe_electindex/`
- To (box only, never commit): `/workspace/lab/evidence_private/electindex/card01-nh002-house/PRE_FREEZE_2026-09-24/`
- sha256 round trip: `sha256sum -c` OK on all 4 before removal; `SHA256SUMS.txt` in the private dir = `e0b86d409830dc550ae561c948cdb188d1071169c2f3edac55d79aed93b707b8`.
- Gitignore: `/workspace/lab/evidence_private/.gitignore` = `*` (sha `fc47b400…`, unchanged). The dir is not inside any git work tree on the box.
- Stub left in place: `packets/card01_hybrid_forecast/source_probe_electindex/RELOCATED_TO_PRIVATE_STUB.json` = `996824ae797eb44abe5cfb95acf52996a6b9fff737937ecfd975f7d33b6c70d2`. Label **PRE_FREEZE_DESIGN_INPUT**.

| file | sha256 | bytes | fetched |
|---|---|---|---|
| `races_summary.csv` | `eb65e9aa71616843fb48832ca5bf4391f99ea76dcd8e087cae72a1f871fcdaf0` | 180322 | 2026-09-24T23:45:43Z |
| `cd_projections.csv` | `43abb7900855f37a3721a21726547698803e3229d9b3181bd9b37271f0947dd9` | 39289 | 2026-09-24T23:45:36Z |
| `README_electindex.md` | `16cf976af164d00b0f331eeca2ad85d885f7dfee19872a7bf54d38a5c2638df5` | 20663 | mtime 19:45:49 ET (no fetch record) |
| `received_at_utc.txt` | `688e5f7c96fcc5b58148563a11b244bcc0de21c2f790f79890a8de25449dba98` | 140 | mtime 19:45:43 ET |

Steward confirmed [V] none of these are staged in either PR and the 4 paths 404 on main.

## 2. Card 01 decision packet: HASH ORDER CORRECTED vs ruling text [V]/[U]
- File `packets/CARD01_NEGLECTED_HYBRID_DECISION_PACKET_2026-09-24.md` **current bytes hash `d59c26420713ef728a306efc0bb12761584125e96ba6a87e84fe0c3e57c69688`** (17539 B, mtime 2026-09-24 20:05:19 ET). It carries the v1.1 charter-reference bump text ("~20:05 ET, documentation-only").
- `58c44c4fb144968ba57e4c8b4a2018026a123d17a02e2e6c09fdfd38f465a353` is what the Archivist hashed earlier this evening, before the 20:05:19 write. It is therefore the **earlier** version.
- The ruling says "canonical = CURRENT bytes, 58c44c4f; superseded d59c2642". The two hashes are inverted relative to the file. Applying the ruling's stated principle (current bytes are canonical): **CANONICAL = `d59c2642…`; SUPERSEDED = `58c44c4f…`.** Flagged to Conductor for confirmation.
- The ACK brief (`briefs/EDGE_RESEARCH_CARDS_01_02_FREEZE_ACK_2026-09-24.md`) was rewritten at the same instant and now cites `d59c2642…`, consistent with this reading.
- **Superseded bytes `58c44c4f…` are not retained anywhere on the box and are not in any git history. UNVERIFIED_BYTES_MISSING.** The "docs only" claim cannot be byte-diffed; it rests on the Deep Research changelog line (requested).
- Card 01 freeze `c3172446…` and Amendment A `4e36d0db…` are separate files and are not affected by this.

## 3. Card 02 freeze kernel: re-pin registered [V]/[U]
- `packets/CARD02_STATION_WEATHER_NOWCAST_FREEZE_KERNEL_2026-09-24.md` current = `8412439f9a31211acbd66125275734afdf8e42e7a95ba7d9d5534003e587adfb` (19979 B, mtime 20:05:19 ET). **CANONICAL (post v1.1 charter bump).**
- At freeze (2026-09-24T23:47:00Z) = `9624ab2498e88896c46e8fd984211b4b8839e613567209841358d7cf5059e5d6`. **SUPERSEDED_AT_FREEZE_VERSION**, kept as the freeze-time pin.
- `packets/card02_station_weather/FROZEN_EXPERIMENT.json` records both (`packet_sha256_at_freeze`, `packet_sha256_after_v1_1_charter_bump`) and keeps `charter_sha256` = v1 `6a02cb46…` [V].
- Pre-bump bytes `9624ab24…` are **not retained** on the box or in git. UNVERIFIED_BYTES_MISSING, so "charter-reference lines only" cannot be byte-verified. Changelog line requested from Deep Research.

## 4. Rule going forward
Any edit to a frozen kernel or decision packet must keep a copy of the pre-edit bytes (e.g. `*.pre-<ts>`) so the Archivist can diff it. Two unrecoverable prior versions tonight.
