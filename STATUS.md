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
- Gate 1 rules (Claude, answering docs/design-review.md; all numbers in `src/shared/Config.luau`):
  - States: Drifting -> Curious (liked bait) or Spooked (any other bait). Curious -> Caught (ring full) or Drifting (bait gone, or `CuriousTimeout` 25 s with no progress). Spooked -> Drifting once it reaches its flee spot and `SpookedMinDuration` has passed. Caught -> removed; next ghost spawns after `RespawnDelay`. `GhostService.reset()` clears ghosts, bait, progress and pending respawns.
  - One room: wrong bait sends the ghost to the farthest spot in the same room (temporary Gate 1 exception).
  - Bait: free, unlimited supply. Neutral and disliked bait both spook. Bait is used up on spook, catch or Curious timeout. Rejected placement uses nothing. Bait only works on a Drifting ghost; one bait per ghost.
  - Jar: server checks range (`JarRange`), cone (`JarConeHalfAngle`) and line of sight from the player's head every frame. Aims expire after `AimTimeout`. Fill = `JarFillRate` x rarity multiplier x (1 + `JarCoopBonus` x (holders - 1)), capped at 4 holders. Drains at `JarDrainRate` when nobody holds; a full drain resets the attempt and its grade.
  - Grade: outside-light time / total catch time; <= 5% Perfect, <= 20% Great, else Good.
  - Rewards: every player who held the light at any point during the attempt and is still in the server gets +1 `leaderstats.Catches` (Gate 1 receipt only). `GhostService.catch` runs once per ghost (state check), so no duplicates.
  - Runtime mapping: Rojo syncs `data/ghosts.json`, `bait.json`, `houses.json` to `ReplicatedStorage.Data.*` ModuleScripts; `src/shared/Content.luau` indexes them by id. `tint` becomes a Color3; `baseModel`, `accessories`, `effectTag`, `hidingSpots` and `personality` are not used in Gate 1. `timerConfigKey` resolves to `Config.HouseDurationSeconds`, but there is no house timer in Gate 1. Every data room maps to the one physical room `Workspace.House.Greybox`. `Config.SpawnSelection = "Cycle"` steps through the spawn table in order (deterministic).

## Active work
| Agent | Task | Branch | State |
| --- | --- | --- | --- |
| Claude Code | Gate 1 greybox | feat/gate1-foundation | REPORT-claude-code.md and Gate 1 rules published to main (user request); feature code stays on the local branch (ee37a82) until F01–F04 are fixed and reviewed |
| Codex | Design QA, starter data, validator, test plan and source review | main (user authorized finished updates) | COMPLETE and published; review verdict: request changes (F01–F03; F04 nit) |

## Publication audit (2026-10-17)
- GitHub main matched local main at 8d12e99 when checked; REVIEW.md's GitHub blob matched local main exactly. Codex report, starter data, validator and test plan are published.
- Claude's feature branch has three local commits after the shared base (82fa1ae, 1ac17bf, ee37a82). GitHub advertised only main; feature code and REPORT-claude-code.md were not published at audit time.
- The active feature checkout predates the review updates on main. Its old “code review pending” row and empty REVIEW.md are stale; read `git show main:REVIEW.md` for findings. No source merge, branch switch or feature push was performed by this audit.

## Requests between agents
- Codex -> Claude Code: Read the completed review on main, fix F01–F04 and update your report/status with evidence. Your feature code/report are local only as of this audit; publication remains outstanding. Do not treat the old feature-checkout REVIEW.md as current.
- Codex -> Claude Code: Reviewed feature snapshot ee37a82. Fix REVIEW.md F01 (stuck hold on focus loss), F02 (bait rejection notice flood), F03 (aims survive house reset); address F04 Config nit. Provide a new commit and targeted evidence. No src/ edits by Codex.
- Codex -> Claude Code: User authorized initial public GitHub publication on main. Continue builder work on feat/gate1-foundation; future Codex work uses data/* or review/* unless the user directs otherwise.
- Codex -> Claude Code: Read docs/design-review.md and data/README.md. Confirm reset/timeout rules, one-room wrong-bait exception, neutral bait/consumption, grade/co-op formulas and completion eligibility. Document JSON-to-runtime mapping and symbolic asset/Config references.
- Codex -> Claude Code: Feature source ee37a82 reviewed. After fixes, provide updated build/Config identity and execute tests/gate1-test-plan.md with real device/console evidence. Builder's existing scripted solo results are in REPORT-claude-code.md on the feature branch; manual acceptance remains pending.
- Claude Code -> Joseph: the greybox room exists only in the local place file (`*.rbxl` is gitignored). Save the place in Studio, and decide whether to version a place snapshot.

## Untested / known issues
- Codex has not run device streaks, gamepad, co-op or exploit tests. Claude reports scripted solo checks in local REPORT-claude-code.md; these are builder-reported, not real PC/phone input acceptance. Gate 1 remains open.
- JSON schema/references passed local validation; symbolic assets and Config references are not runtime-verified.
- Three-room data is starter content only; Gate 1 runtime remains one room/one ghost.

## Session log
- 2026-10-17, Claude Code: Published REPORT-claude-code.md and the Gate 1 rules/runtime mapping to main at the user's request. Feature code not merged; Codex verdict is request changes. Next: fix F01–F04 on feat/gate1-foundation with evidence.
- 2026-10-17, Claude Code: Installed Rokit 1.2.0 + Rojo 7.7.1 (+ Studio plugin). Built the Gate 1 greybox on feat/gate1-foundation and the greybox room in the place. 10-catch scripted solo run passed (real input, 2-client and phone runs not done).
- 2026-10-17, Codex: Audited GitHub refs and REVIEW.md blob against local Git. Confirmed Codex work published and marked COMPLETE; Claude's three feature commits/report remain local only. Recorded stale feature-checkout coordination files and outstanding fixes/publication. No game-code changes.
- 2026-10-17, Codex: Reviewed feature snapshot ee37a82 against all eight checklist areas; three should-fix findings and one nit in REVIEW.md. Data validator and diff whitespace checks passed. Read Studio console only; no gameplay tests rerun. Builder's scripted streak does not replace PC/phone input acceptance. See REPORT-codex.md.
- 2026-10-17, Codex: User confirmed Studio sign-in as LordNxtmen and Claude's Studio MCP connection are done and running. Removed the completed README setup checklist. This confirms setup only; Gate 1 gameplay acceptance remains open.
- 2026-10-17, Codex: User confirmed Claude Code is in and Rojo is installed. Removed Claude folder/start checklist item; Studio account sign-in and Claude MCP verification remain pending. Builder feature checkout left untouched.
- 2026-10-17, Codex: Recorded LordNxtmen as the intended Studio account for all Roblox games; README sign-in verification remains pending.
- 2026-10-17, Codex: Removed verified README setup steps: Rojo 7.7.1/Git 2.53.0 installed, saved project place open in Studio, Codex Studio MCP connected, Codex folder/prompt complete. Remaining checklist covers intended Studio account and Claude folder/prompt/MCP verification; remove section after those are confirmed. Builder's untracked source/config left untouched.
- 2026-10-17, Codex: User authorized public repository creation and committing finished support files to main. Added ignore rules for credentials, generated files and local Studio place/lock files. Gameplay remains untested; initial publication does not close Gate 1.
- 2026-10-17, Codex: Added actionable design QA, three ghost/three bait/one three-room house data contract, Python validator and manual acceptance/exploit plan. Validator and four negative cases passed; see REPORT-codex.md. Await Claude's Git setup, rule confirmations and source diff; no src/ edits or commits.
