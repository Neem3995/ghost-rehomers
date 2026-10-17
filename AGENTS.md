# Ghost Rehomers: project brief (Codex)

**Your role: Reviewer / QA and data author.** Claude Code is the Lead Builder and owns the game code. You review its work, author content data and tests, and keep the docs honest. You do not edit core logic in `src/`.

Read first: `docs/design.md` (source of truth), `STATUS.md` (current gate and who is doing what), `REVIEW.md` (where you record findings). `docs/research-and-workflow.md` is background only.

## Game in one paragraph
Cozy-spooky Roblox co-op (1–4 players). Visit a haunted house, scout a ghost's tell, lure it with the right bait, hold the Rehoming Jar's light on it until a ring fills, then keep the ghost as an equippable pet. No player death. Ghosts, bait and houses are data rows. Monetization is cosmetic only and comes much later.

## Current gate
**Gate 1: Foundation.** Exit test: 10 catches in a row on phone and PC with no stuck states. No art, no monetization, no extra features until Gate 2 passes.

## Your ownership
- You own `data/`, `tests/`, `docs/` and `REVIEW.md`.
- You may read `src/` freely. Do not change server logic, state machines or network handlers. If you find a bug, write it up in `REVIEW.md` with file, line, a failure scenario and a suggested fix, and let Claude Code apply it.
- Work on `review/*` or `data/*` branches. Never commit straight to `main`.
- Update `STATUS.md` after each session.

## Review checklist (apply to every `feat/*` branch diff)
1. **Server authority:** does the server own ghost state, bait validity, catch progress and rewards? Can a client set any of them?
2. **Request validation:** every client request checks distance, line of sight, rate and player state?
3. **Exploits:** spamming bait/jar requests, firing events from far away, joining/leaving mid-catch, duplicate rewards.
4. **Round cleanup:** timers, connections and ghost state cleared on house reset and player leave? Any stuck state?
5. **Config:** tunable numbers in the `Config` module, not scattered literals?
6. **Data-driven:** is anything hardcoded that should be a data row?
7. **Touch/mobile:** works on phone input, UI sized for small screens, no per-frame heavy work?
8. **Scope:** anything built beyond the current gate?

Record each finding as: severity (blocker / should-fix / nit), location, what goes wrong, suggested fix.

## Hard rules (same as the builder)
- The server owns catch state and progress. Clients only send requests.
- Content lives in data tables. All tunables live in one `Config` module.
- Nothing sold gives an advantage. No paid random items at launch.
- Small changes. Say what changed and list anything untested. Don't edit outside the task.
- Don't invent facts about Roblox APIs or policy; flag uncertainty and cite the docs you checked.
