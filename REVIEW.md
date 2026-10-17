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
### feat/gate1-foundation — 2026-10-17

Reviewed `060fc76..ee37a821489ee8115eb2129e6815746538407b79` (13 changed files). Locations refer to that feature snapshot. Findings are source-based; no new gameplay reproduction was performed.

| # | Severity | Location | What goes wrong | Suggested fix | Status |
| --- | --- | --- | --- | --- | --- |
| F01 | should-fix | src/client/Main.client.luau:195–218, 237–250 | Hold F/mouse/R2, move focus away and release while unfocused. No focus-loss cleanup exists; if InputEnded is missed, jarSources stays set and Heartbeat keeps refreshing aim indefinitely. Server AimTimeout cannot clear continuously refreshed input. | Clear all held sources on WindowFocusReleased and send release; also clear on character removal/controller disconnect. Verify releasing while unfocused requires a fresh press on return. | open |
| F02 | should-fix | src/server/BaitService.luau:25–27 | Every valid-ID request rejected by cooldown fires a Notice. Hundreds of rejected requests still produce hundreds of outbound events and client flash timers. Placement is throttled but rejection feedback bypasses that protection. | Add an ingress rate limit before bait processing; silently discard excess traffic and independently throttle rejection notices. Verify bounded placements AND notices during flood, then recovery. | open |
| F03 | should-fix | src/server/GhostService.luau:192–204; src/server/JarService.luau:16, 66–86 | House reset drops ghost catch records through state listeners but never clears aims. A pre-reset aim remains eligible for up to AimTimeout (0.5 s). Immediately baiting the new ghost can advance it using input from the previous run. | Coordinate a JarService reset that clears aims and catches when the house resets. Reset/rebait without a new aim packet: progress must remain zero. | open |
| F04 | nit | src/server/RequestGuard.luau:61, 93; src/client/Main.client.luau:339, 346 | Fallback eye offset, floor raycast offsets/reach and notice durations remain literals despite the single-Config rule. | Move these tunables to Config; structural constants and decorative values need not move. | open |

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
