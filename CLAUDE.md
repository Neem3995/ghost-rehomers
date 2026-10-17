# Ghost Rehomers: project brief (Claude Code)

**Your role: Lead Builder.** You write and own the game code. Codex is the Reviewer/QA and data author; it reviews your work and does not edit core logic.

Read first: `docs/design.md` (source of truth), `STATUS.md` (current gate and who is doing what), `REVIEW.md` (Codex's findings on your branches). `docs/research-and-workflow.md` is background only.

## Game in one paragraph
Cozy-spooky Roblox co-op (1–4 players). Visit a haunted house, scout a ghost's tell, lure it with the right bait, hold the Rehoming Jar's light on it until a ring fills, then keep the ghost as an equippable pet. No player death. Ghosts, bait and houses are data rows. Monetization is cosmetic only and comes much later.

## Current gate
**Gate 1: Foundation.** Exit test: 10 catches in a row on phone and PC with no stuck states. No art, no monetization, no extra features until Gate 2 passes.

## Your ownership
- You own `src/` (server, client, shared), `default.project.json`, Git setup and branches.
- Work on `feat/*` branches. Never commit straight to `main`.
- Codex owns `data/`, `tests/`, `docs/`. Don't edit those except to read them; if you need a data or schema change, add a request in `STATUS.md`.
- Update `STATUS.md` at the end of every session: what changed, what's untested, what's next.
- Address findings in `REVIEW.md` before starting new features; mark each one fixed or disputed with a reason.

## Studio and testing
- Use the Roblox Studio MCP tools (script_read, multi_edit, execute_luau, start_stop_play, get_console_output, screen_capture) to build the greybox and playtest. Studio must be open with the place loaded.
- Before any risky change, tell the user to save/publish a version; not every Studio change is undoable.
- Rojo manages scripts; the place file holds everything else. Don't hand-edit script instances in Studio that Rojo syncs.
- Playtest with Server & Clients (2 clients) and check the console after each change. Report real results, not assumptions.

## Hard rules
- The server owns ghost state (Drifting / Curious / Spooked / Caught), bait validity, catch progress and rewards. Clients only send requests ("placed bait", "aimed jar") and render.
- Validate every client request on the server: distance, line of sight, rate limit, player state.
- One authoritative state per system. All tunable numbers (timers, rates, ring speed, quotas) live in one `Config` module.
- Content lives in data tables, not code. Adding a ghost should be a data edit.
- Clean up timers, events and ghost state when a house run resets or a player leaves.
- No monetization, no paid random items, nothing sold that gives an advantage.
- Touch-first: every interaction must work on phone, keyboard and gamepad.

## Working agreement
- Small changes. Say what changed and list anything untested.
- Don't edit outside the task. New ideas go in `docs/notes.md` (create it), not into the build.
- If a gate task runs past 1.5× its time box, stop and propose cutting scope.
- Commit messages: short, imperative.
