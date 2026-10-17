# Gate 1 manual acceptance plan

Status: manual acceptance evidence INCOMPLETE. Claude relays manual PC/focus/controller/phone PASS reports without logs or source identity (see summary below). Two-client tests remain NOT RUN. House timer is implemented in feature commit 5eec8bc and expiry tests are now RUNNABLE; no timer waiver is assumed. Data validation and injected-input runs do not establish gameplay acceptance.

## Reported evidence (not completed per-device logs)

| Source | Reported result | Limits / remaining work |
| --- | --- | --- |
| Claude's committed report at 5eec8bc, relaying Joseph's 2026-10-17 feedback | PC streak, focus loss, controller and real phone reported PASS / working | No direct report in this Codex session, device details, per-catch rows, Output captures or precise source identity. Preserve as relayed results; do not fabricate 20 PASS rows. Record fresh logged runs on the timer build for acceptance. |
| Claude's Studio scripted timer report | Expiry at 0.54/0.92 progress: no catch/credit; zero-progress carry-over; respawn cancelled; shortened natural run/intermission restarted | Builder-reported, not independently rerun; default 480-second and real-device/two-client expiry checks remain pending. |
| Claude's injected number-pad and post-timer regression report | 3/3 catches for each reported regression | Supplementary tool input, not manual PC/phone acceptance. |
| Two-client fill, rewards, leave, join and expiry | NOT RUN | Use a real two-client session and retain separate client/server evidence. |

Gate 1 cannot close from these summaries alone: the existing protocol requires identifiable runs and per-catch evidence. Use the template below for fresh manual runs; record the exact tested commit/Config. Earlier passes are not discarded, but they do not certify later timer/input changes.

## Setup and evidence

Record date, tester, source commit (or exact source snapshot), Config values, Studio/client versions, device model/OS, control type, player count and console output. Test a real phone with touch and a PC with keyboard/mouse. Studio emulation is supplemental, not phone proof. Also smoke-test gamepad as required by the builder prompt; it does not replace either streak.

Use the one-room/one-ghost graybox, free replenishable bait and the normal supported next-catch/reset action. Builder must document state transitions, timer/reset expectations, aim expiry, co-op formula and grades first. Start with clean server state. Keep server-observed state/progress and catch receipts available through existing diagnostics; ask Claude for missing instrumentation rather than altering src/.

## Two acceptance streaks

Run this sequence **10 times consecutively on PC, then 10 on the real phone**. Use one continuous session per device; do not restart the server or manually change state between catches.

1. Observe Drifting and its tell; record ghost ID and expected liked bait.
2. Place correct bait through normal input. Confirm Curious and movement/slowdown according to the documented rules.
3. Aim and hold the jar. Confirm visible ring agrees with server progress, remains bounded and fills at the configured solo rate.
4. Keep the ghost in the light until Caught. Confirm one completion receipt, a valid documented grade and no further filling/reward on repeated input.
5. Release the input. Use the normal reset/rearm path; confirm progress clears and the next ghost returns to a catchable state within the configured limit.
6. Record console errors, unexpected state, elapsed time and result. A stuck state means normal actions cannot advance within the documented reset/transition limit. Any manual recovery, duplicate completion or unexpected error fails the streak; retain evidence, fix, and restart that device's streak at 1.

Copy the per-device evidence log below once for PC and once for phone. Do not mark acceptance passed without all 20 completed rows and evidence. Injected input, scripted camera/position, Studio emulation and interrupted runs are supplementary only. A void run cannot be stitched to a later run to create a streak.

## Per-device evidence log (copy for each device/session)

- Run ID / date / tester:
- Device model / OS / screen size / Studio or client version:
- Input method (human keyboard/mouse or real phone touch):
- Source commit (current review: 5eec8bc) OR all file hashes matching docs/gate1-timer-review-hashes.json:
- Config identity / relevant rates and reset timings:
- Place file/version / saved after approved Rojo sync / loaded-script identity:
- Player count / console-log or recording path:
- Session start/end / interruptions / overall PASS, FAIL, VOID or NOT RUN:

| Catch | Ghost / bait | Grade | Receipt count / Catches total | Next spawn time | Console or video reference | PASS / FAIL / NOT RUN | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | NOT RUN | |
| 2 | | | | | | NOT RUN | |
| 3 | | | | | | NOT RUN | |
| 4 | | | | | | NOT RUN | |
| 5 | | | | | | NOT RUN | |
| 6 | | | | | | NOT RUN | |
| 7 | | | | | | NOT RUN | |
| 8 | | | | | | NOT RUN | |
| 9 | | | | | | NOT RUN | |
| 10 | | | | | | NOT RUN | |

Record edge-case runs separately: `run ID | device/clients | scenario | source/Config | expected | actual | evidence path | PASS/FAIL/BLOCKED/NOT RUN`. Save raw console output; distinguish engine/plugin warnings from game errors. Do not infer a test passed from the absence of errors alone.

## Edge cases (separate from the streaks)

Run on both input types where applicable, with a two-client server for co-op/leave cases. Record expected values from Config alongside actual results. Untestable tooling cases remain NOT RUN.

| Scenario | Action | Expected result |
| --- | --- | --- |
| Wrong bait | Use explicit disliked bait while Drifting; retry after Spooked resolves. | One consumption per accepted placement; flee to a valid alternate spot in the one-room exception, recover and allow a correct lure. |
| Unlisted bait | Use the third bait; place bait again while Curious/Spooked/Caught. | Matches the builder's agreed rules; no stuck state or repeated consumption from one accepted action. |
| Leave light | Part-fill, turn away/occlude/move out of range, then return. | Server progress drains at configured rate, clamps at zero, resumes correctly; grade follows documented interruption rule. |
| Release / input loss | Release touch, move finger off control, switch focus, unequip jar, respawn or stop updates. | Contribution ends or expires within configured limit; movement controls remain usable and no permanent hold persists. |
| Player leaves | Contributor leaves at partial fill and near completion; remaining player continues. Repeat with last player leaving. | Departing contribution/aim clears, remaining rate is correct, reset is possible, and no duplicate completion occurs. |
| Two players | Compare solo and two-player fill; release one, then finish simultaneously. | Rate matches formula, drops when one leaves light, one catch completion occurs; receipts follow agreed eligibility. |
| Rapid spam | Send bait/jar requests above configured rate using a controlled test client. | Server enforces limit, no extra progress/completions or bait placement; normal input recovers after limit window. |
| House timer expiry — RUNNABLE | On 5eec8bc, run to natural expiry (480 s); also use Studio-only DebugExpireRun at partial and near-full progress with aims arriving. | Expiry precedes catch progress: no new receipt or credit; bait/aim/progress cleared, uncaught species returns Drifting at zero after 5 s. Use Config values if changed and record them; a debug expiry alone does not verify the natural deadline. |
| Expiry after catch / intermission | Catch, then expire during RespawnDelay. Spam input during break; wait for restart, then lure/catch normally. | Pending old respawn cancelled, no ghosts/catches during break, exactly one next-cycle ghost after break; fresh input works. No duplicate credit or stale completion. |
| Clock / restart | Observe normal, warning and intermission display on PC/phone; reset via Studio hook. | Default run 480 s, warning threshold 30 s, break 5 s; server controls deadlines. Debug reset restarts clock and leaves one Drifting ghost. Distinguish reset cleanup logs from actual catch receipts. |
| House reset (separate from timer expiry) | Use the Studio-only server reset hook with partial/near-full progress; stop old aim delivery before reset, rebait and send no new aim. | Progress remains zero until fresh aim; pending respawns cannot create extra ghosts; no stale completion. Mark tooling unavailable as NOT RUN, not timer-blocked. |
| Curious timeout (separate from house timer) | Place liked bait, stop all aim and wait Config.CuriousTimeout with zero progress. | Bait removed, ghost returns to Drifting and correct bait works again. This test is available now. |
| Join mid-catch | Join during Curious: first observe without contributing, then separately join and contribute. Also join after Caught. | Observer receives no credit; a contributor still present at completion gets one credit under the current eligibility rule. Joining after completion never grants that catch retroactively. |

## Exploit checklist

Ask Claude to provide a controlled request harness if needed. Never equate normal UI testing with malformed-request testing.

- Try requests from beyond range, behind a wall and with no valid character/jar/player state; verify server rejects them.
- Submit unknown ghost/bait IDs, another player's targets, wrong types, missing values, NaN/infinite vectors and oversized payloads; verify safe rejection without state mutation or handler errors.
- Attempt to supply progress, state, grade or reward values; confirm server ignores client authority claims.
- Replay stale requests after reset and near completion; flood from both clients and disconnect during the flood. Confirm rate limits and cleanup per player.
- Verify exactly-once completion at simultaneous finish and timeout boundaries; inspect server receipts, not only the ring animation.
- Review code for timer/connection cleanup and Config ownership. Runtime symptom checks alone cannot prove these properties.

Final report separates source review, local validator results, Studio solo/co-op tests, real PC streak and real phone streak. Gate 1 stays open until both device streaks and applicable edge cases pass, with unresolved cases explicitly listed.
