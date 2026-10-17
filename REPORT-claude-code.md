# Claude Code report — 2026-10-17

> Published to main at the user's request. The code it describes is on the local branch `feat/gate1-foundation` (ee37a82), not merged; Codex's review (REVIEW.md F01–F04) is still open.

## Role
Lead Builder: game code, Rojo config, Git branches.

## What I did
- Installed Rokit 1.2.0 (`~/.rokit`), Rojo 7.7.1 (pinned in `rokit.toml`) and the Rojo Studio plugin.
- Branch `feat/gate1-foundation` (2 commits on `main`): `default.project.json` (partially managed: `src/shared` -> ReplicatedStorage.Shared, `data/*.json` -> ReplicatedStorage.Data, `src/server` -> ServerScriptService.Server, `src/client` -> StarterPlayerScripts.Client).
- `src/shared`: `Config` (every tunable), `Content` (indexes Codex's JSON rows), `Net` (remote names), `Grade`.
- `src/server`: `GhostService` (state machine, spawn, reset), `BaitService` (bait requests), `JarService` (aim requests, fill/drain, grade), `RequestGuard` (rate limit, cooldown, alive check, line of sight, floor raycast), `Main` (wiring, `leaderstats.Catches`).
- `src/client/Main`: HUD with three bait buttons, a big hold-jar button, crosshair, ghost labels (name, tell, state, progress bar), a local light beam, and notices. Input: touch buttons; F / left mouse / R2 for the jar; 1–3 or X / Y / B for bait.
- Studio place (not in Git): `Workspace.House.Greybox` with a floor, 4 walls, 2 crates, Bounds, 6 GhostSpots and a SpawnLocation.
- Gate 1 rules and the JSON mapping are in STATUS.md under "Decisions made".

## What works (verified)
Studio solo playtest. A client-side script fired the real `PlaceBait` / `AimJar` remotes, so every request went through server validation. Results:
- **10 catches in a row, no stuck states** (catches 1–10 in two runs, plus 2 sanity catches): Hush 4.2–4.5 s, Wick 5.3 s, Mallow 6.9–7.0 s. Fill times match Config (Common 4 s, Uncommon 5 s, Rare 6.7 s).
- Wrong bait: Spooked, fled, then back to Drifting in about 3 s; the liked bait then caught it (2 runs).
- Light dropped at 50% for 1.0 s and 0.4 s: progress drained 0.50 -> 0.22 and 0.50 -> 0.38; both graded Great. Uninterrupted catches graded Perfect.
- Junk arguments (number, unknown id, nil, table, NaN vector, string, 100-length vector): nothing changed and no errors.
- 20 bait requests in one frame: 1 bait placed. 200 aim requests in one frame and then silence: no lasting progress.
- Aiming from 47 studs (range 30): progress stayed 0.
- Curious with nobody aiming: back to Drifting after the 25 s timeout and the bait was removed.
- Console: no script errors. Every transition is logged as `[Ghost]` / `[Catch]`.
- HUD screenshot: bait buttons in 1/2/3 order (a sort bug was found and fixed), jar button on the right.

## What needs work
1. Real phone run (touch hold plus camera drag aiming) has not been done. This is the main Gate 1 risk.
2. No Server & Clients run: MCP play is solo only, so co-op fill, two-player rewards and player-leave-mid-catch are untested.
3. The greybox room lives only in the local place file (`*.rbxl` is gitignored).
4. Liked and disliked bait ids are replicated to clients through Content. That's fine for Gate 1, but it's a spoiler/exploit surface once the journal exists.
5. In the very first scripted attempt, one liked-bait request was rejected for an uncaptured reason. I couldn't reproduce it in later runs, which logged every notice.

## Untested / assumptions
- Real input layer (button holds, keys, gamepad) and the beam visuals; the screenshot captured the HUD but not reliably the 3D view.
- Line of sight blocked by a crate.
- Assumed the `ButtonB` bait binding doesn't clash with Roblox defaults.

## Needs from Codex or Joseph
- Codex: review `main..feat/gate1-foundation` against AGENTS.md.
- Joseph: save the place; run Server & Clients (2 clients) and a real phone streak per `tests/gate1-test-plan.md`.

## Suggested next tasks
1. Codex review, then fix findings. Accept when REVIEW.md has no open blockers.
2. Manual 2-client Server & Clients test. Accept when co-op fill is faster, both players get credit, and one leaving mid-catch causes no stuck state.
3. Real phone streak of 10. Accept when 10 catches in a row work with touch only.
4. Decide on versioning a place snapshot (or a Rojo `.model.json` greybox).

## Rough effort
One session, inside the time box.
