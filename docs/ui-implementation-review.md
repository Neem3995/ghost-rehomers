# Claude UI implementation review — 2026-10-17

Reviewed local feature commit **069b2d8a4d1703b606772f68c48d7a024587b727**, based on approved gameplay build 5eec8bc. Claude Code implemented the requested spectral field kit and applied Codex's focused fixes. Only `src/client/Main.client.luau` and new `src/client/Theme.luau` changed in this commit. No server/shared/data/network/project changes. Source was fast-forwarded into the original local feature checkout and synced through the existing Rojo connection. No game-source push or main merge.

**Verdict: approve the presentation source with device/visual acceptance still open.** Existing Gate 1 gameplay acceptance remains open. This review does not certify all intended visual states on all screen sizes.

## Findings resolved before the source commit

| ID | Severity | Location in final source | Original failure / correction |
| --- | --- | --- | --- |
| UI01 | should-fix | Main.client.luau, CatchResult handler, sameName/mine | First pass inferred personal credit from DisplayName alone. Two players sharing that name could both see +1. Final code permits personal wording only when the matching name is unique among current players, otherwise uses generic wording. This conservative fallback omits personal celebration for legitimate contributors with duplicate names; actual server rewards are unchanged. |
| UI02 | should-fix | Main.client.luau, layout(), stacked/toastBase | First pass left a full-width receipt over the lower portrait touch-control area. Touch portrait now uses an upper receipt, hides optional bottom hint/portrait and shares one responsive base with entry animation. Source correction verified; real-phone fit not executed. |
| UI03 | should-fix | Main.client.luau, hideToast() | First pass did not immediately clear receipt effects on intermission/character removal. Final code invalidates the lifetime token, cancels receipt/border motion, destroys sparks and hides the card. Intermission rendering exercised; removal path reviewed in source. |

API checks: Roblox documents that [DisplayName is not unique](https://create.roblox.com/docs/reference/engine/classes/Player), [CoreUISafeInsets](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets), and [GuiService.ReducedMotionEnabled](https://create.roblox.com/docs/reference/engine/classes/GuiService). The name fallback avoids expanding the server protocol during a UI-only change.

## Independent checks executed

- Rojo 7.7.1 packaging PASS; existing Python content schema/reference validator PASS; whitespace check PASS. These do not prove gameplay or device fit.
- Original Studio Edit model received Main (32169 source bytes) and Theme (2103 bytes) through Rojo. Both compiled with Studio `loadstring` without execution errors. Subsequent Play mode loaded the HUD and theme successfully.
- Live desktop HUD query: GhostHUD and GhostReticle exist; safe GUI area 1251×415, bait tray 432×56, three 138×56 cards named Music Box / Unlit Candle / Cold Tea with 1/2/3 key labels. Jar 110×110. Clock counted down (7:49 observed). The full viewport differs from the safe area's height; this was the regular layout, not a compact-phone test.
- Inspected Studio screen capture of the clock, bait tray, centered reticle, amber jar/halo and hint. Captures showed a dark 3D backdrop, so they do **not** establish world/ghost-card composition. Client query confirmed the Hush billboard/card and Drifting state existed. No claim of full scene visual QA.
- Injected F through the real client input handler: held ring thickness 4, halo transparency ~0.70. After key release: thickness 3, halo ~0.88. This checks held/released presentation with tool input, not a human focus/controller test.
- Scripted actual catch through existing client remotes: temporarily placed/anchored the test character in clear space, invoked the existing reset hook, requested music-box bait and sent valid aim directions while polling. Catches 0 → 1; actual receipt displayed `You rehomed Hush`, grade Perfect, credit visible. This is supplementary runtime evidence, not a manual catch streak or a synthetic receipt.
- Later query: zero Spark objects and toast hidden. Invoked existing expiry hook: RunState Intermission, clock `Next visit in 5`, toast hidden. This does not prove interruption while the toast was still visible, physical controller behavior or natural countdown expiry.
- Console captured existing Roblox CorePackages FoundationProvider warnings and asset-type mismatch for 203785492. No game-script exception appeared in that captured output. Console was not exhaustively captured after every scenario; no blanket clean-console claim.
- Stopped Play mode, verified connected Rojo, saved original place. Disk file 97948 bytes, 2026-10-17 15:00:15 EDT. Transient runtime camera/character/test changes were discarded when Play stopped.

## Remaining limits

Real phone landscape/portrait and safe-control overlap; controller navigation and physical disconnect; focus/respawn regression on the UI build; observer/duplicate-name receipts in actual multiplayer; long text and lower-end performance; repeated-cycle object/connection counts; reduced-motion runtime switching; ghost-card readability in the actual scene; and every other unexecuted state in docs/ui-polish.md remain unverified. The portrait notice region reserves 72 px: an unusually long message can still overlap its receipt and should be checked in device QA. No paid assets or audio were added.

Claude's full local UI notes remain in the isolated build checkout's REPORT-claude-code.md. Original feature checkout's pre-existing dirty report/status were preserved. Claude CLI reported approximately $2.20 cumulative model cost for implementation and fixes; this is its reported cost estimate, not an account billing statement.
