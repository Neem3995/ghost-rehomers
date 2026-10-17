# STATUS: shared coordination board

Both agents read this at the start of a session and update it at the end. Keep it short.

## Current gate
Gate 1: Foundation (time box ~3 weeks at ~8 hrs/week; placeholder). Exit: 10 catches in a row on phone and PC, no stuck states.

## Decisions made
- Roblox Studio account for every Roblox game: LordNxtmen (user confirmed; current Studio sign-in unverified).
- Game: Ghost Rehomers (name not yet searched on Roblox).
- Catch style: setup-based (lure, then hold the jar light). Open for review at Gate 2.
- Gate 2 twist: not chosen yet (Disguise / Tough ghosts / Time of night).

## Active work
| Agent | Task | Branch | State |
| --- | --- | --- | --- |
| Claude Code | Repo + Rojo setup, then Gate 1 greybox | feat/gate1-foundation | started; user confirmed Claude Code is in |
| Codex | Doc QA, data schema + starter data, Gate 1 test plan | main (initial publication authorized by user) | support files complete; code review pending |

## Requests between agents
- Codex -> Claude Code: User authorized initial public GitHub publication on main. Continue builder work on feat/gate1-foundation; future Codex work uses data/* or review/* unless the user directs otherwise.
- Codex -> Claude Code: Read docs/design-review.md and data/README.md. Confirm reset/timeout rules, one-room wrong-bait exception, neutral bait/consumption, grade/co-op formulas and completion eligibility. Document JSON-to-runtime mapping and symbolic asset/Config references.
- Codex -> Claude Code: Report a reviewable source diff and build/Config identity when ready; execute tests/gate1-test-plan.md and retain real device/console evidence. No implementation is currently available for Codex review.

## Untested / known issues
- Studio, PC/phone streaks, gamepad, co-op and exploit tests: NOT RUN. Gate 1 remains open.
- JSON schema/references passed local validation; symbolic assets and Config references are not runtime-verified.
- Three-room data is starter content only; Gate 1 runtime remains one room/one ghost.

## Session log
- 2026-10-17, Codex: User confirmed Claude Code is in and Rojo is installed. Removed Claude folder/start checklist item; Studio account sign-in and Claude MCP verification remain pending. Builder feature checkout left untouched.
- 2026-10-17, Codex: Recorded LordNxtmen as the intended Studio account for all Roblox games; README sign-in verification remains pending.
- 2026-10-17, Codex: Removed verified README setup steps: Rojo 7.7.1/Git 2.53.0 installed, saved project place open in Studio, Codex Studio MCP connected, Codex folder/prompt complete. Remaining checklist covers intended Studio account and Claude folder/prompt/MCP verification; remove section after those are confirmed. Builder's untracked source/config left untouched.
- 2026-10-17, Codex: User authorized public repository creation and committing finished support files to main. Added ignore rules for credentials, generated files and local Studio place/lock files. Gameplay remains untested; initial publication does not close Gate 1.
- 2026-10-17, Codex: Added actionable design QA, three ghost/three bait/one three-room house data contract, Python validator and manual acceptance/exploit plan. Validator and four negative cases passed; see REPORT-codex.md. Await Claude's Git setup, rule confirmations and source diff; no src/ edits or commits.
