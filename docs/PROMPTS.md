# First prompts

Paste each into its own agent, run from the `ghost-rehomers` folder. Start Claude Code first; Codex's data and test work doesn't depend on it, so the two can run in parallel. Review Claude Code's branch with Codex once it reports Gate 1 progress.

## Claude Code: Lead Builder

```
Read CLAUDE.md, STATUS.md and docs/design.md in full. You are the Lead Builder for Ghost Rehomers; Codex is the reviewer and data author.

Task: Gate 1 (Foundation) only.

1. Check whether Rojo and Git are installed. If either is missing, stop and tell me exactly what to install; don't work around it.
2. Create the repo structure: default.project.json (Rojo "partially managed": scripts managed, everything else in the place file), src/server, src/client, src/shared, data/, tests/, and a Git repo with a sensible .gitignore. Work on branch feat/gate1-foundation.
3. Build a gray-box prototype: one room, one ghost, placeholder shapes only.
   - A shared Config module for every tunable number.
   - A server-owned ghost state machine: Drifting, Curious, Spooked, Caught.
   - Bait placement: the server validates the request. The right bait makes the ghost Curious; the wrong bait Spooks it to a different spot and uses the bait.
   - Rehoming Jar: hold-to-fill ring while the ghost is inside the light cone; progress drains if it leaves; server owns progress; compute a Perfect/Great/Good grade.
   - Ghost and bait definitions read from a data table (placeholder rows are fine; Codex will supply the real schema in data/).
   - Input that works on touch, keyboard and gamepad.
4. Playtest through the Roblox Studio MCP tools (start_stop_play, get_console_output). Report real console output. Use Server & Clients with 2 clients if available.
5. Update STATUS.md.

Not allowed: art, monetization, pets, saves, extra rooms, or any feature beyond the above.
Acceptance: 10 catches in a row with no stuck states. If you can't verify something, say so; don't claim it works.
Ask me to save/publish a Studio version before any risky change.
Follow the Token budget rule in CLAUDE.md: read only what you need, stay in scope, keep replies short.
When done, summarize what changed, what's untested, and what you need from Codex.
```

## Codex: Reviewer / QA and data author

```
Read AGENTS.md, STATUS.md and docs/design.md in full. You are the Reviewer/QA and data author for Ghost Rehomers; Claude Code is the Lead Builder. Do NOT edit anything in src/.

Task: Gate 1 support. Work on branch data/starter-content.

1. QA the design doc: list gaps, contradictions, ambiguous rules and untestable exit criteria in docs/design-review.md, ranked by how much they would hurt Gate 1. Keep it to what's actionable.
2. Author the content data schema in data/: ghosts, bait, houses (one house, three rooms), with a short README describing each field and valid values. Include 3 starter ghosts (one Common, one Uncommon, one Rare) with tell, liked bait, disliked bait, base model, tint, accessories and a one-line personality, plus 3 bait items. Make sure every liked/disliked bait id points to a real bait row.
3. Write a simple validator script in tests/ that fails on a missing field, an unknown reference, a duplicate id or an invalid rarity. Note how to run it.
4. Write tests/gate1-test-plan.md: the manual test script for "10 catches in a row on phone and PC", including edge cases (wrong bait, leaving the light, player leaves mid-catch, two players on one ghost, rapid request spam) and an exploit checklist.
5. Update STATUS.md. When Claude Code reports a branch ready, review its diff using the checklist in AGENTS.md and record findings in REVIEW.md.

Follow the Token budget rule in AGENTS.md: read only what you need, stay in scope, keep replies short.
Don't invent Roblox API or policy facts; flag anything you aren't sure of. Summarize what you produced and what you need from Claude Code.
```
