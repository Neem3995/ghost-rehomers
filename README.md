# Ghost Rehomers

Cozy-spooky Roblox co-op game: scout a ghost's tell, lure it with the right bait, catch it in a jar, keep it as an equippable pet.

## Start here
1. `docs/design.md`: the design (source of truth).
2. `docs/research-and-workflow.md`: market research, earnings math, workflow (partly written for the earlier Hotel 13 idea; see its banner).
3. `docs/PROMPTS.md`: the first prompt for each agent.

## The two agents
| | Claude Code | Codex |
| --- | --- | --- |
| Role | Lead Builder | Reviewer / QA + data author |
| Brief | `CLAUDE.md` | `AGENTS.md` |
| Owns | `src/`, Rojo config, Git, `feat/*` branches | `data/`, `tests/`, `docs/`, `REVIEW.md`, `review/*` and `data/*` branches |
| Never touches | `data/`, `tests/`, `docs/` (requests via STATUS.md) | server logic in `src/` (writes findings in REVIEW.md) |

Shared coordination: `STATUS.md` (current gate, active work, requests) and `REVIEW.md` (findings).

Folder: `C:\\Users\\hoese\\Desktop\\Roblox\\ghost-rehomers`. When both agents finish, each leaves `REPORT-claude-code.md` / `REPORT-codex.md` (template: `docs/REPORT-TEMPLATE.md`) for review.

## Setup checklist

Only unfinished or unverified steps remain. Remove each item when verified complete; remove this section when none remain.

- [ ] Verify Roblox Studio is signed in as `LordNxtmen`.
- [ ] Verify Claude Code can connect to this project's Studio instance through MCP.
- [ ] Confirm Claude Code is working in this folder and has started its first prompt from `docs/PROMPTS.md`.

## Ground rules
Use the Roblox Studio account `LordNxtmen` for every Roblox game (user decision). Current Studio sign-in still needs verification.

Token budget: both agents read narrowly, stay in scope, write short replies, test narrowly and keep sessions small (full rule at the bottom of `CLAUDE.md` and `AGENTS.md`).
Server owns catch state. Content lives in data tables. All tunables in one Config module. Nothing sold gives an advantage. No monetization or extra features until the Gate 2 playtest passes.
