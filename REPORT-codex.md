# Codex report — 2026-10-17

## Latest session: F01–F04 re-review

Approved all four fixes in the uncommitted source on ee37a82; no new actionable finding in the seven changed source files. releaseJar covers input lifecycle, bait ingress and notices are independently throttled, house reset clears aims/catches, and requested tunables moved to Config. Studio-only ServerStorage reset hook acceptable in source. Exact reviewed file hashes are in docs/gate1-fix-review-hashes.json.

Independent checks: Python data validator PASS, diff whitespace PASS, Rojo 7.7.1 packaging PASS to temporary rbxlx. These do not certify execution, live sync, world geometry or gameplay. Claude's regression report was inspected, not independently rerun. Focus loss/controller disconnect, real PC/phone streaks, gamepad, two-client co-op/leave and obstacle LOS remain pending. House-timer deferral needs the user's decision.

No src/ edits, feature commit or merge by Codex. Only completed review documents published to main; Claude's source fixes remain uncommitted at review time. Gate 1 remains open.

## Previous session: initial Gate 1 source review

Reviewed all 13 changed files in `060fc76..ee37a82` against AGENTS.md. Verdict: **request changes**. REVIEW.md records three should-fix findings: stale held input after focus loss, unbounded bait rejection notices, and pre-reset aim surviving house reset. A fourth finding is a Config nit. No src/ edits, Studio mutations or feature merge.

Verified this session: `python tests/validate_data.py` passed; feature diff whitespace check passed. Read-only Studio console showed one Perfect Hush receipt for LordNxtmen followed by a Wick spawn, plus CorePackages warnings and asset-type mismatch messages. Source identity/input method were not established by that log. Findings are source-based, not live reproductions. Focus API semantics were checked against official Roblox documentation linked in REVIEW.md.

Claude must fix F01–F03, address F04 and provide a new commit with targeted evidence. Then re-review and run tests/gate1-test-plan.md. No new gameplay tests ran; real PC/phone streaks, gamepad, two-client co-op, disconnect and obstacle LOS remain unverified by Codex. Claude's reported scripted streak is separate evidence. Gate 1 stays open. One bounded review session; documentation published separately to main under user authorization, preserving the builder checkout.

The sections below describe the earlier support-data session.

## Role
Reviewer / QA and content data author for Gate 1.

## What I did
- Added docs/design-review.md with eight ranked, actionable design gaps.
- Added data/ghosts.json, bait.json, houses.json and README.md: three ghosts, three bait items and one house with three data-only rooms.
- Added tests/validate_data.py and tests/gate1-test-plan.md; updated STATUS.md.
- No src/ edits. Initial support session found no Git repository. User subsequently authorized public repository creation and committing completed support files to main; added .gitignore for credentials, generated files and local Studio places/locks.

## What works (verified)
- Python 3.13.2: `python tests/validate_data.py` exited 0 with `PASS: starter content schema and references`.
- In-memory mutations, independently copied from the valid JSON and passed to `validate`, each raised ValueError: deleted tell, unknown liked bait, duplicate bait ID, invalid rarity. Originals were not modified.

## What needs work
- Confirm transitions/reset/timeout, one-room flee behavior, bait semantics, co-op completion eligibility and grade formulas before gameplay acceptance.
- Builder must integrate the JSON authoring contract and verify asset/Config keys. No runtime loader exists in this snapshot.

## Where I got stuck
Initial session had no Git repository or implementation. User subsequently authorized Git setup/publication; source review remains pending until Claude provides an implementation.

## Untested / assumptions
No Studio, real PC/phone, gamepad, co-op or exploit tests ran. No code diff was available. Gate 1 remains open. Three-room content does not expand the one-room runtime scope. Validator does not prove assets, Config or runtime loading.

## Needs from Claude Code or Joseph
Claude: resolve docs/design-review.md, document runtime mapping, then provide the feature diff and actual test evidence. Joseph: real-phone acceptance testing when a runnable build exists.

## Suggested next tasks
1. Claude confirms the open rules and Config formulas so expected test results are explicit.
2. Claude integrates the content contract; verify IDs/asset keys against the loaded build.
3. Codex reviews the feature diff using AGENTS.md and records findings in REVIEW.md.
4. Execute device streaks and edge cases; retain logs identifying the build. Acceptance requires evidenced completion, not this report.

## Rough effort
One bounded support session; no gameplay acceptance claimed.
