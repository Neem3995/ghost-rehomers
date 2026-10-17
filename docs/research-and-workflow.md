# Research, Earnings & Workflow (reference)

> **Status: partly superseded.** This was written for the earlier Hotel 13 concept (Oct 16, 2026). The Hotel 13-specific sections (refined MVP scope, creature/art plan) were left out of this copy. The market research, earnings math, feasibility risks and workflow below still apply to **Ghost Rehomers**. The design source of truth is `docs/design.md`.

## Bottom line

A solo Roblox game is feasible if you build one small, finishable slice first inside a fixed time box. Aim it at your goal of replacing the pharmacy income, but plan around the low-earnings case so it still pays off as a portfolio piece if revenue stays small.

- Reaching $3,000 a month takes about 63,000 monthly players on medium assumptions, so the build plan should make sense at near-zero revenue.
- One decision point: after the "prove the hook" gate, fresh testers either explain the core mechanic and ask for another round, or you stop and keep the code as a portfolio project.
- The Accenture/apprenticeship track stays the primary path either way.

## Feasibility check

The hard part is reliable multiplayer logic built in limited hours, not the art or the idea. Hour figures are planning assumptions (about 8 hours a week), not measurements; replace them with your real pace after the first two weeks of Gate 1.

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| Limited hours | Evenings and weekends only; a stalled project is the most likely failure | Fixed weekly block, a time box per gate, a written stop rule |
| Multiplayer bugs | Duplicate completion, disconnect softlocks and stale round state are classic solo-dev traps | One server-owned state; clients only send requests; test with Studio's Server & Clients mode and Network Simulator |
| Small lobbies need players | 2–4 player co-op is empty if nobody joins | Solo test mode; recruit friends and coworkers for early playtests |
| Art workload | Many characters and skins are weeks of modeling | Blockout shapes and placeholders until the hook is proven |
| Mobile performance | Auras, chains and dark lighting are costly on phones | Budget effects early; check with Device Simulator, then real phones |
| Discoverability | A new experience gets little traffic with no audience | No ad spend until retention data exists; early players come from your network |
| Idea churn | Seven concepts is a trap if each steals a weekend | One project until the Gate 2 decision; park new ideas in a notes file |

## What the earning games offer

The biggest earners are update-driven collection, simulation and roleplay loops with many things to buy. Roblox doesn't publish per-game revenue, so every dollar figure is a third-party estimate.

**Highest estimated earners, Q1 2026 (per month)**

| Game | Category | Est. revenue | What it offers |
| --- | --- | --- | --- |
| Rivals | Competitive shooter | $8–15M | Weapon skins and battle passes |
| Blox Fruits | RPG | $8–14M | Gamepasses; rotating fruit availability drives update-led spending |
| Brookhaven RP | Roleplay | $6–12M | Gamepasses for premium houses and vehicles |
| Adopt Me! | Roleplay and pets | $5–10M | Pet trading economy; limited-time eggs |
| Pet Simulator 99 | Pet simulator | $4–8M | Gacha-style crates, gamepasses |
| Steal a Brainrot | Collection sim | $3–7M | Mobile-dominant; reported #1 mobile revenue in January 2026 |
| Fisch | Fishing sim | $3–6M | Gamepasses and cosmetics |
| Dress to Impress | Fashion dress-up | $2–5M | Cosmetics and seasonal passes |

Ranges come from [RoWatcher](https://rowatcher.com/news/the-10-highest-earning-roblox-games-in-2026-and-what-they-mean-for-the-platform); its page dates are inconsistent, though the body covers Q1 2026. Category labels for the simulators are my own.

**How fast earnings fall off the chart** ([Statroblox](https://statroblox.com/guides/how-much-do-roblox-games-make), Oct 7, 2026 model, standard $0.0038 rate)

| Top-earning chart rank | Est. creator earnings per month |
| --- | --- |
| #1 | $16.2M |
| #10 | $1.5M |
| #50 | $250K |
| #100 | $115K |
| #200 | $52K |
| #475 | $19K |

The table stops at rank 475, so "a few thousand a month" sits below anything it publishes, and it gives no count of games reaching that level.

**Horror and co-op comparables**

| Game | Category | Players / estimates | What players do |
| --- | --- | --- | --- |
| Dandy's World | Mascot horror, team-based | ~165K playing now; peak 607K (Mar 2026); est. $839K/month (confidence 0.58) | Team up, collect Toons, complete machines |
| 99 Nights in the Forest | Survival crafting horror | ~201K playing now | Build a camp, manage hunger, rescue children |
| Forsaken | Asymmetric horror, 8 vs 1 | 82K concurrent (article figure) | Survivors vs one killer |
| Doors | Roguelite horror | 7.27B visits | Move through 100+ procedural rooms |
| Road-Side Shawarma | Night-shift horror | 70M visits | Use CCTV and a rulebook to spot anomalies |

Concurrent counts are one snapshot from [Live Counts](https://livecounts.nl/roblox-charts/) (October 2026).

**What the earners have in common**

- **Things to chase.** Collectible Toons, pets, fruits and crates give players a reason to return.
- **Rotating, limited-time content.** Seasonal passes, limited eggs and update-led drops keep spending going after launch.
- **Cosmetics and status over power** in the horror titles, though the big simulators lean on gamepasses and crates.
- **Cosmetic-led horror likely earns less per player.** Dandy's World works out to roughly $5/month per concurrent player vs roughly $11–27 for Brookhaven and Adopt Me! and $40+ for Blox Fruits and Rivals. Directional only; it mixes Q1 estimates with an October snapshot.
- **Short sessions with friends.** Co-op or trading appears in nearly every entry.

Treat these lists as survivors. They show the winners, not the many games that earn little.

## Earnings: what a few thousand a month takes

Medium case from your earnings brief: $1,436/month from 30,000 players. Reaching $3,000 needs about 63,000 unique players a month. Assumptions (illustrative, not Roblox averages): 3% of players pay, 600 Robux each, 70% creator share.

| Monthly cash target | Unique players needed, standard rate ($0.0038) | If all spend earns the higher rate ($0.0054) |
| --- | --- | --- |
| $1,000 | about 20,900 | about 14,700 |
| $2,000 | about 41,800 | about 29,400 |
| $3,000 | about 62,700 | about 44,100 |
| $5,000 | about 104,400 | about 73,500 |

The higher rate applies only to certain Earned Robux (passes, developer products, subscriptions, private servers) from US players verified 18+, so treat the right-hand column as a best case. Other [DevEx terms](https://create.roblox.com/docs/production/monetization/developer-exchange): 30,000 Earned Robux minimum, one request per calendar month, W-9/W-8 on file, age 13+.

- Cosmetic-only monetization tends to earn less per player than the 600-Robux assumption suggests.
- Revenue is taxable income, so plan to set part of it aside.
- The number to watch is revenue per unique player (the medium case implies about $0.048). Measure your own at the limited release before judging any plan.

**Suggested replacement test (adjust to your numbers).** Keep the pharmacy job until game income has covered your pharmacy take-home plus a cushion for several months in a row. I'm not a financial advisor; set the exact threshold with your own numbers. The Accenture track stays primary either way.

## Workflow

Work in weekly cycles that always end with a runnable game, and let each gate pass or fail on a test rather than a feeling.

**Tooling, kept light**

- **Roblox Studio** for the world, lighting and UI layout. Use the Test tab, **Server & Clients**, the **Network Simulator** for multiplayer and the **Device Simulator** for phone layouts, then check real phones ([Studio testing modes](https://create.roblox.com/docs/studio/testing-modes)).
- **VS Code + Rojo + Git** for scripts. Rojo's "partially managed" setup (it manages scripts; the place file holds everything else) is the lowest-friction start; its docs for that mode are still marked incomplete, so also save the place file regularly ([Rojo workflows](https://rojo.space/docs/v7/workflows/)).
- **Claude Code and Codex** for boilerplate, tests and review of the synced scripts. Review every network handler yourself against the server-owned rule before accepting it.
- Skip linters, package managers and fancier toolchains until Gate 1 works.

**Code layout.** Separate modules per system, plus one Config module for every tunable number (timers, quotas, rates). Content lives in data tables.

**Weekly loop (adjust to your real hours)**

- One or two short weeknight sessions for small, finishable tasks and bug fixes.
- One longer weekend block for the current gate's main feature.
- End every session with the game runnable and a Git commit; never leave it broken overnight.
- End every week with a playtest, even solo, and a three-line log: what works, what broke, what's next.

**Stop rules, decided now so you don't decide tired**

- A gate past 1.5× its time box means cut scope, not extend hours.
- A failed Gate 2 playtest gets one fix cycle of up to two weeks and one retest; a second failure shelves the idea.
- New game ideas go in a notes file until the Gate 2 decision.

**Two-agent workflow (Ghost Rehomers).** Claude Code is the lead builder on feature branches; Codex reviews each diff and authors data, tests and docs. See `README.md`, `CLAUDE.md`, `AGENTS.md` and `STATUS.md` in the project root.

**Reusing mechanics.** Borrowing a genre or loop is normal. Use your own names, art and audio. Keep a license list for any asset you buy, and don't reuse brainstorm images.

## Mini PC + OpenClaw idea (notes)

- Roblox Studio's official MCP server and the official `roblox-studio-agent-plugin` work on Windows and macOS only; Studio must be open, signed in, with a place open. Not every change is undoable, so save/publish a version first.
- OpenClaw can run Claude Code and Codex through ACP, but it carries real security risks (prompt injection, malicious skills, exposed instances), and subscription-login rules for third-party tools have been tightened; check current terms before relying on it.
- Simplest first test: link a session to your own computer and have the agents work there before buying hardware.
