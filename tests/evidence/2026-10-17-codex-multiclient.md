# Codex local multiplayer QA — 2026-10-17

Build: feature commit 5eec8bc, source manifest docs/gate1-timer-review-hashes.json (12/12 matched before testing). Windows 11 x64; Studio 0.743.0.7431133; Rojo 7.7.1, one-way sync. This is executed Studio multiplayer evidence with scripted aiming/placement through real client remotes, not a human PC streak or a real-phone run.

## Before the interruption

These results were returned by Studio tools during this chat before the session closed. Transcribed from those tool outputs; temporary in-memory result storage did not survive the interruption. No raw JSON file was saved at that point.

- Rojo panel connected to ghost-rehomers at localhost:34872. All 11 loaded script lengths/Adler-32 matched normalized local source. Place saved with Ctrl+S; status bar confirmed path, disk size 92035 bytes and timestamp 2026-10-17 14:03:51 EDT. Prior place backed up under `%LOCALAPPDATA%\Codex\GhostRehomersQA\20261017-140350`.
- Studio UI: Server & Clients, count 2. Server confirmed real Player1 and Player2 instances, and separate client MCP sessions reported those identities. Runtime test setup positioned/anchored characters in clear floor space and initialized catch counters to zero. No source edits or mock players.

| Check | Observed output | Result / limits |
| --- | --- | --- |
| Solo control, Hush | Progress 0.32 -> 0.64 over 1.302 s (~0.246 ring/s); Player1 counter 0 -> 1, one receipt; Player2 counter 0 | PASS scripted control; observer was already present, not a late joiner |
| Two-player Hush fill | Progress 0.16 at 0.396 s -> 0.66 at 1.882 s (~0.337 ring/s across those samples); completion at 2.733 s after scheduled start | Consistent with configured 0.375 ring/s and ~1.5x solo, allowing sample quantization, client delivery and scheduling variation. Source formula also inspected. Not a precise benchmark. |
| Exactly-once credit | After solo baseline 1/0, co-op result counters 2/1. Both clients had two total receipts (including the solo broadcast). Co-op receipt named Player2 and Player1 once each | PASS; distinguish broadcasts from eligible reward counts |
| Invalid shortened-timer attempt | Tried changing Config through MCP require, reset and restore. Game console still logged 480 s; deadline remained ~480 s away; ordinary catch increased counters to 3/2 | INVALID timer test; excluded from expiry PASS. No source change or accepted shortened natural-expiry claim |
| Two-player expiry path | Studio DebugExpireRun invoked at progress 0.46 with both clients aiming. Immediate Intermission, zero ghosts. After 5.5 s: Hush Drifting, progress 0, Running. Counters unchanged at 3/2 | PASS expiry hook path; does not prove unshortened natural 480 s deadline |
| Leave at partial fill | Player2 disconnect requested using server Kick at progress 0.50. Removal processed later (sample at 1.582 s had one player and progress 0.92). Player1 continued, counter 3 -> 4; final receipt named only Player1 | PASS surviving-player completion and exclusion of departed player; disconnect request at half, actual removal near completion; no duplicate credit. Not a physical client-window close |
| Genuine late observer | Player3 joined while Hush Curious at 0.40, counter 0. Later attempted completion returned Player1 still at 4 and Player3 receipts 0/counter 0 | INCOMPLETE: catch completion not observed before interruption; no late-observer PASS inferred |

Server console contained `ContentId: rbxassetid://203785492 failed due to: Asset type does not match requested type`. No game script exception appeared in the captured server output. Console capture was not exhaustive across all clients; do not call the session error-free.

## Remaining at resume

Fresh test session required: complete late-observer and late-contributor cases, desktop focus-loss check. Human PC 10-streak, real phone/model, physical controller unplug remain manual tasks. Source approval is separate from runtime acceptance. Gate 1 stays open.

## Resumed session

Previous Studio sessions were closed when work resumed. Reopened the saved place, connected Rojo, confirmed all 11 loaded script checksums and all 12 manifest hashes again, and saved. Started Server & Clients with one initial client, then added actual late-joining clients through the Add Clients dropdown. No source edits.

- Automated focus check: injected F held through the actual input handler produced 10 aim requests in a one-second server window. Moving OS focus to the edit window increased the client's WindowFocusReleased counter from 1 to 2; subsequent 1.5-second window had zero aims. Sent injected key-up while away; after refocusing without a press, one-second window still had zero aims. Fresh F press produced 9 aims in one second; final key-up sent. This tests the lifecycle with tool input and OS window activation, not a human Alt-Tab run. Raw output is in 2026-10-17-codex-resume-tools.json.
- Late observer: server PlayerAdded log recorded Player3 joining with ghost Curious (progress 0 at that instant). Completed that same ghost after the join: Player1 counter 0 -> 1, Player3 0 -> 0, Caught/progress 1; receipt named only Player1. PASS for an observer joining during Curious before completion; it does not prove joining at exactly half fill.
- Late-contributor check: Player4 joined Curious at progress 0.14 (server PlayerAdded log). First attempt timed out to Drifting; polling never observed completion and counters stayed 1/0. Bounded re-lure retry of uncaught Hush: Player1's loop sent 56 aim requests and completed, increasing to 2; Player4's loop sent **zero** aim requests and stayed at 0. Therefore this did not exercise a valid contributing joiner and is INCONCLUSIVE, not a game failure or PASS. Later Player4 snapshot saw current Wick/Drifting correctly. Do not infer retroactive or missing credit from a zero-contribution fixture.

Do not turn these results into human PC/phone streaks. Physical controller unplug remains NOT RUN. The initial interrupted late-observer attempt remains excluded; the resumed completed case is separate.

Final console review: server captured normal state/house/catch logs plus the asset-type mismatch message above. Client4 output included Roblox CorePackages FoundationProvider warnings. No exception naming a game src/ script was found in those captured outputs. Client logs were not all captured, so this is not a blanket clean-console claim.

## Completion status

Resumed raw tool results and final server/Client4 consoles: `2026-10-17-codex-resume-final.json`. The smaller `2026-10-17-codex-resume-tools.json` contains the initial focus measurements only.

- DONE: verify connected Rojo, verify loaded source and save current place; source review remains approved with no new actionable code finding.
- EXECUTED supplementary runtime checks: two-player fill/credit, existing and genuine late observer exclusion, survivor completion after a disconnect, two-player expiry-hook cleanup, automated OS-focus lifecycle.
- INCONCLUSIVE: valid contributing late joiner (fixture did not deliver Player4 aim requests).
- NOT RUN by Codex: 10 catches by human keyboard/mouse, real-phone 10 catches/model, physically unplugging a controller, unshortened natural 480-second deadline with two clients. These require further device/manual evidence; no manual PASS rows created.
