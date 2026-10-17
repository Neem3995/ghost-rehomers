# REVIEW: Codex findings on Claude Code's branches

Codex writes findings here; Claude Code marks each one fixed or disputed (with a reason).

## Template

### [branch] YYYY-MM-DD
| # | Severity | Location | What goes wrong | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | blocker / should-fix / nit | file:line | failure scenario | fix | open / fixed / disputed |

Checklist applied: server authority, request validation, exploits, round cleanup, Config, data-driven, touch/mobile, scope.
Verdict: approve / approve with fixes / request changes.

## Findings
### Independent desktop/multiplayer QA — 2026-10-17

Claude's source remains 5eec8bc, matching the 12-file timer manifest. No new source delta or actionable source defect found. Source approval stands. Independently executed local server/client checks are recorded in tests/evidence/2026-10-17-codex-multiclient.md; they are scripted/injected runtime evidence, not human PC/phone acceptance.

Confirmed connected Rojo, all 11 loaded scripts matching local checksums, and saved the current place (the earlier stale-place warning is superseded). Actual two-player sessions verified co-op fill consistent with the configured bonus, exactly-once eligible credit, exclusion of an observer, survivor completion after a disconnect requested at half fill, and no award/carry-over reset through the two-player expiry hook. Completed a genuine late-observer case in the resumed session and an automated OS-focus lifecycle check. The normal 480-second deadline was not independently established by the expiry-hook test; an ineffective shortened-config attempt is explicitly INVALID in the evidence.

Review of Claude's newest handoff: evidence types are accurately separated. The statement that Studio MCP is inherently solo-only was too broad: Studio UI can launch local clients, which then expose separate MCP sessions. Use the documented UI route for future multiplayer QA. No core implementation correction requested on that basis.

Gate 1 remains open: human PC/phone streaks and physical controller unplug cannot be completed by this desktop automation. Valid contributing late-joiner credit remains INCONCLUSIVE: the retry delivered zero joiner aims and therefore did not test that reward path. Keep unexecuted and interrupted cases explicit; no per-catch manual PASS rows invented. No src/ edits, feature push or merge by Codex.

### House timer and number-pad review — 2026-10-17

Reviewed committed feature snapshot **5eec8bc**, including 26c4b89 (previous fixes and number-pad bindings). Working tree was clean. Verdict: **approve in source; Gate 1 acceptance remains open**. No new actionable finding. F05 is corrected in Claude's local committed report: observers get no credit, contributors present at completion get one credit, no retroactive credit.

All eight review areas applied to the new delta:

- Authority/validation/exploits: timer deadlines, run state, carry-over and restart are server-owned. No new client request was added. DebugExpireRun and reset remain Studio-only BindableFunctions in ServerStorage. Number-pad bindings use the existing validated bait remote.
- Cleanup/timeout: Main calls HouseService.step before ghost/jar steps. Expiry captures uncaught rows, clears aims/catches/bait and invalidates respawn generation, then enters intermission. Restart clears again before spawning carry-over or the next cycle row. Expired progress does not award a catch in the inspected path.
- Config/data: duration resolves house.timerConfigKey through Config; intermission and warning thresholds are centralized. One physical room remains the Gate 1 exception; carry-over retains species and physical room, not previous catch progress.
- Touch/mobile/performance: clock renders existing server-owned attributes, with no new network request per frame. Number-pad bindings are scoped to the three bait items. Clock layout/touch usability and co-op remain device/runtime checks.
- Scope: timer now implements the design's timeout path; no art, pets, saves or monetization added. The user's timer choice is relayed in Claude's handoff; this review does not independently attest to another conversation.

Independent checks: Python validator PASS; timer commit diff whitespace PASS; Rojo 7.7.1 packaging PASS. New manifest docs/gate1-timer-review-hashes.json captures all 12 source/project files at this commit. The older fixes manifest is retained as historical evidence.

Claude reports scripted expiry at 0.54/0.92 progress without credit, carry-over at zero, pending-respawn cancellation after a catch, a natural 12-second run (Config restored to 480), and post-change injected catches 3/3. These were inspected as builder-reported results, not independently rerun. The local report relays Joseph's manual PC/focus/controller/phone passes without raw logs, device details or source identity; those cannot establish acceptance of the new timer build. Canonical test plan records the limited evidence and makes expiry tests runnable.

No src/ edits, gameplay mutations, feature push or merge by Codex. Feature source is committed locally; only review/support documentation is published on main. Next: logged manual evidence on the reviewed snapshot, two-client fill/reward/leave/join/timeout checks, and verify/save the current synced place.

### Acceptance-prep review — 2026-10-17

Independent source identity check: **11/11 approved hashes match** the current uncommitted working tree. No new code delta since the approved snapshot; source approval stands. Reviewed Claude's new acceptance-prep notes, not a new live playtest. Injected-keyboard streak (10/10) and crate/wall LOS results are builder-reported supplementary evidence, not real PC/phone or co-op acceptance. The interrupted earlier run is correctly marked void.

| # | Severity | Location | What goes wrong | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- |
| F05 | should-fix | REPORT-claude-code.md, Joseph-run checklist, join-mid-catch bullet (working-tree handoff) | It says a joiner gets no credit for that catch without distinguishing an observer from a contributing joiner. Current rules credit anyone who contributed during the attempt and remains present. Following the checklist could incorrectly fail valid co-op behavior. | Say observer gets no credit; a joiner who contributes before completion gets one credit; nobody gets retroactive credit for a completed catch. Canonical tests/gate1-test-plan.md now states this. | open (builder handoff correction) |

Documentation cleanup: Claude's older “Untested” section still lists crate LOS and the entire input layer as untested, despite newer injected-input/LOS results. Reconcile it with the latest evidence while retaining real-device/focus/gamepad limitations. Do not claim the saved rbxl contains current fixes until checked after saving.

Codex completed the requested per-device log template, split house reset and Curious timeout from house-timer expiry, and marked house-timer expiry BLOCKED pending Joseph's decision. No new gameplay tests needed for these documentation changes. Verdict: source approval unchanged; correct F05 before using the handoff checklist. Gate 1 remains open.

### Re-review: uncommitted F01–F04 fixes — 2026-10-17

Verdict: **approve the fixes in source; gameplay acceptance remains pending**. No new actionable defect found in the seven changed source files relative to ee37a82. No src/ edits or feature merge by Codex. Review identity is captured in docs/gate1-fix-review-hashes.json; Config SHA256 begins e7d657c6ba0d043a, matching Claude's report. This approval covers those bytes, not future edits or a claimed deployed build.

| Finding | Codex disposition | Evidence inspected |
| --- | --- | --- |
| F01 | Fixed in source; manual lifecycle tests pending | releaseJar clears all held sources and sends release; connected to focus loss, controller disconnect, character removal and death. Old key state is not re-added by Heartbeat. Claude reports injected-key death/respawn checks; actual focus loss/disconnect not run. |
| F02 | Fixed in source | Ingress rate gate precedes payload/placement work; every rejection uses an independently throttled notice helper. Claude reports 200 rejected requests yielding one notice and normal recovery; not independently rerun. |
| F03 | Fixed in source | GhostService reset invokes listeners before destroying/replacing ghosts; JarService's registered callback clears aims and catches. Registration occurs before startup reset. Claude reports comparative stale-aim tests with/without fix and normal-timeout regression; not independently rerun. |
| F04 | Fixed in source | Eye fallback, floor probe and notice/toast durations now reference Config; values preserved. |

Debug hook review: Main creates DebugResetHouse only inside RunService:IsStudio(), as a BindableFunction under ServerStorage. No RemoteEvent or replicated access was added. Official [ServerStorage](https://create.roblox.com/docs/reference/engine/classes/ServerStorage) and [RunService](https://create.roblox.com/docs/reference/engine/classes/RunService) references checked. No client reset exposure found in source.

Independent local checks: Python content validator PASS; git diff --check PASS; Rojo 7.7.1 build PASS to a temporary rbxlx. Packaging does not establish Luau execution, place geometry, live sync or gameplay acceptance. No Studio mutations or new gameplay tests performed in this re-review.

Remaining acceptance: real PC/phone 10-catch streaks, actual focus-loss release, controller disconnect, gamepad/touch usability, two-client co-op/rewards/leave, obstacle LOS. House timer remains unimplemented; the proposed deferral requires the user's scope decision. Fixes remain uncommitted on the feature checkout at review time; source publication is not complete.

The initial findings and verdict below are historical; F01–F04 are superseded by this re-review.

### feat/gate1-foundation — 2026-10-17

Reviewed `060fc76..ee37a821489ee8115eb2129e6815746538407b79` (13 changed files). Locations refer to that feature snapshot. Findings are source-based; no new gameplay reproduction was performed.

| # | Severity | Location | What goes wrong | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- |
| F01 | should-fix | src/client/Main.client.luau:195–218, 237–250 | Hold F/mouse/R2, move focus away and release while unfocused. No focus-loss cleanup exists; if InputEnded is missed, jarSources stays set and Heartbeat keeps refreshing aim indefinitely. Server AimTimeout cannot clear continuously refreshed input. | Clear all held sources on WindowFocusReleased and send release; also clear on character removal/controller disconnect. Verify releasing while unfocused requires a fresh press on return. | fixed in source; see re-review |
| F02 | should-fix | src/server/BaitService.luau:25–27 | Every valid-ID request rejected by cooldown fires a Notice. Hundreds of rejected requests still produce hundreds of outbound events and client flash timers. Placement is throttled but rejection feedback bypasses that protection. | Add an ingress rate limit before bait processing; silently discard excess traffic and independently throttle rejection notices. Verify bounded placements AND notices during flood, then recovery. | fixed in source; see re-review |
| F03 | should-fix | src/server/GhostService.luau:192–204; src/server/JarService.luau:16, 66–86 | House reset drops ghost catch records through state listeners but never clears aims. A pre-reset aim remains eligible for up to AimTimeout (0.5 s). Immediately baiting the new ghost can advance it using input from the previous run. | Coordinate a JarService reset that clears aims and catches when the house resets. Reset/rebait without a new aim packet: progress must remain zero. | fixed in source; see re-review |
| F04 | nit | src/server/RequestGuard.luau:61, 93; src/client/Main.client.luau:339, 346 | Fallback eye offset, floor raycast offsets/reach and notice durations remain literals despite the single-Config rule. | Move these tunables to Config; structural constants and decorative values need not move. | fixed in source; see re-review |

Checklist applied:

- Server authority: state, bait matching, progress, grade and catch counter are server-owned; client inputs do not assign them directly.
- Validation/exploits: bait has room/floor/range/LOS/living-character checks; jar validates finite direction, rate, live character, range, cone and LOS during contribution. F02 concerns response amplification. Catch state check guards duplicate completion in source; simultaneous-client proof remains pending.
- Cleanup: player removal clears aims, participation and guard tables; ghost reset invalidates pending respawns and catch records. F01/F03 remain open.
- Config/data: JSON is wired through Rojo and Content; tunables mostly centralized, with F04 exceptions. Wiring is inspected, not independently runtime-tested.
- Touch/mobile: touch and gamepad handlers exist; actual device usability is unverified. Check fixed 352-pixel bait content at the smallest target viewport.
- Scope: one physical room, no pets/saves/monetization; one-room flee exception documented. Three species cycle one live ghost at a time. House timer is explicitly deferred; timeout acceptance needs implementation or an approved scope exception.

Verdict: **request changes** for F01–F03, then review fixes and run manual acceptance. No feature merge recommended yet.

API reference checked: [Roblox UserInputService](https://create.roblox.com/docs/reference/engine/classes/UserInputService) documents that InputEnded requires client focus and provides WindowFocusReleased. F01 is inferred from this contract and source, not a live reproduction.

Evidence: local content validator and feature diff whitespace check passed. Read-only Studio console showed one Hush Perfect catch credited to LordNxtmen and a Wick spawn, plus CorePackages warnings and asset-type mismatch messages. That log does not establish input method, a 10-catch streak, or reviewed source identity. Claude's scripted streak remains builder-reported evidence, separate from real input/device acceptance.
