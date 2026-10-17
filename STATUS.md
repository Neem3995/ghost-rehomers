# STATUS: shared coordination board

Both agents read this at the start of a session and update it at the end. Keep it short.

## Current gate
Gate 1: Foundation (time box ~3 weeks at ~8 hrs/week; placeholder). Exit: 10 catches in a row on phone and PC, no stuck states.

## Decisions made
- Roblox Studio account for every Roblox game: LordNxtmen (user confirmed account and active sign-in).
- Setup complete: user confirmed Claude's Studio MCP connection is running; README setup checklist removed.
- Game: Ghost Rehomers (name not yet searched on Roblox).
- Catch style: setup-based (lure, then hold the jar light). Open for review at Gate 2.
- Gate 2 twist: not chosen yet (Disguise / Tough ghosts / Time of night).

## Active work
| Agent | Task | Branch | State |
| --- | --- | --- | --- |
| Claude Code | Gate 1 greybox | feat/gate1-foundation | ee37a82 reviewed; fixes requested in REVIEW.md |
| Codex | Gate 1 source review | main (user authorized finished updates) | request changes: REVIEW.md F01–F03; F04 nit |

## Requests between agents
- Codex -> Claude Code: Reviewed feature snapshot ee37a82. Fix REVIEW.md F01 (stuck hold on focus loss), F02 (bait rejection notice flood), F03 (aims survive house reset); address F04 Config nit. Provide a new commit and targeted evidence. No src/ edits by Codex.
- Codex -> Claude Code: User authorized initial public GitHub publication on main. Continue builder work on feat/gate1-foundation; future Codex work uses data/* or review/* unless the user directs otherwise.
- Codex -> Claude Code: Read docs/design-review.md and data/README.md. Confirm reset/timeout rules, one-room wrong-bait exception, neutral bait/consumption, grade/co-op formulas and completion eligibility. Document JSON-to-runtime mapping and symbolic asset/Config references.
- Codex -> Claude Code: Feature source ee37a82 reviewed. After fixes, provide updated build/Config identity and execute tests/gate1-test-plan.md with real device/console evidence. Builder's existing scripted solo results are in REPORT-claude-code.md on the feature branch; manual acceptance remains pending.

## Untested / known issues
- Studio, PC/phone streaks, gamepad, co-op and exploit tests: NOT RUN. Gate 1 remains open.
- JSON schema/references passed local validation; symbolic assets and Config references are not runtime-verified.
- Three-room data is starter content only; Gate 1 runtime remains one room/one ghost.

## Session log
- 2026-10-17, Codex: Reviewed feature snapshot ee37a82 against all eight checklist areas; three should-fix findings and one nit in REVIEW.md. Data validator and diff whitespace checks passed. Read Studio console only; no gameplay tests rerun. Builder's scripted streak does not replace PC/phone input acceptance. See REPORT-codex.md.
- 2026-10-17, Codex: User confirmed Studio sign-in as LordNxtmen and Claude's Studio MCP connection are done and running. Removed the completed README setup checklist. This confirms setup only; Gate 1 gameplay acceptance remains open.
- 2026-10-17, Codex: User confirmed Claude Code is in and Rojo is installed. Removed Claude folder/start checklist item; Studio account sign-in and Claude MCP verification remain pending. Builder feature checkout left untouched.
- 2026-10-17, Codex: Recorded LordNxtmen as the intended Studio account for all Roblox games; README sign-in verification remains pending.
- 2026-10-17, Codex: Removed verified README setup steps: Rojo 7.7.1/Git 2.53.0 installed, saved project place open in Studio, Codex Studio MCP connected, Codex folder/prompt complete. Remaining checklist covers intended Studio account and Claude folder/prompt/MCP verification; remove section after those are confirmed. Builder's untracked source/config left untouched.
- 2026-10-17, Codex: User authorized public repository creation and committing finished support files to main. Added ignore rules for credentials, generated files and local Studio place/lock files. Gameplay remains untested; initial publication does not close Gate 1.
- 2026-10-17, Codex: Added actionable design QA, three ghost/three bait/one three-room house data contract, Python validator and manual acceptance/exploit plan. Validator and four negative cases passed; see REPORT-codex.md. Await Claude's Git setup, rule confirmations and source diff; no src/ edits or commits.
