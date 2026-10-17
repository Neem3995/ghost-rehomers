# Gate 1 manual acceptance plan

Status: NOT RUN. This is a proposed acceptance protocol pending builder confirmation of the rules in docs/design-review.md. Data validation does not establish gameplay success.

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

Use this log header for 20 rows: `device | catch 1–10 | ghost | bait | grade | completion count | reset time | console evidence | pass/fail | notes`. Do not mark acceptance passed without all rows and evidence.

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
| Timeout / reset | Let timer expire at partial and near-full progress; reset repeatedly. | Agreed timeout precedence; old timers/aim/requests cannot affect next catch; no stale ring or completion. |
| Join mid-catch | Second client joins during Curious and during Caught. | Receives authoritative current state; cannot claim an already completed catch. |

## Exploit checklist

Ask Claude to provide a controlled request harness if needed. Never equate normal UI testing with malformed-request testing.

- Try requests from beyond range, behind a wall and with no valid character/jar/player state; verify server rejects them.
- Submit unknown ghost/bait IDs, another player's targets, wrong types, missing values, NaN/infinite vectors and oversized payloads; verify safe rejection without state mutation or handler errors.
- Attempt to supply progress, state, grade or reward values; confirm server ignores client authority claims.
- Replay stale requests after reset and near completion; flood from both clients and disconnect during the flood. Confirm rate limits and cleanup per player.
- Verify exactly-once completion at simultaneous finish and timeout boundaries; inspect server receipts, not only the ring animation.
- Review code for timer/connection cleanup and Config ownership. Runtime symptom checks alone cannot prove these properties.

Final report separates source review, local validator results, Studio solo/co-op tests, real PC streak and real phone streak. Gate 1 stays open until both device streaks and applicable edge cases pass, with unresolved cases explicitly listed.
