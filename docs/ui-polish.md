# HUD polish: the spectral field kit

Requested by Joseph on 2026-10-17. Design proposal for Claude Code to implement; **not installed in the game**. This small UI pass is requested before Gate 1 closes; gameplay acceptance remains open. Reference: `ui-polish.svg` (desktop and phone landscape). Illustration and example values are mockups, not runtime evidence.

## Direction

Cozy-spooky field kit: dark plum cards, warm cream text, amber jar light and mint catch progress. Leave the room and ghost visible. Use existing Roblox UI primitives and existing fonts; no purchased assets, new menus or new mechanics. Keep existing bait placement behavior: pressing a bait button immediately requests placement; do not turn it into a two-step select/place interaction.

| Token | Value | Use |
| --- | --- | --- |
| Panel | #211E30 | HUD surfaces |
| Raised panel | #302B42 | Bait/action cards |
| Border | #625871 | Subtle outlines |
| Text | #FFF4DC | Primary text |
| Muted text | #C6BED3 | Supporting text |
| Amber | #F5CB7A | Jar action, catch celebration |
| Mint | #ACE2C5 | Curious/progress |
| Coral | #F6A295 | Warning/error with text |
| Corners / spacing | 12 px / 8 px baseline | Consistent construction |

Visual tokens belong in one client presentation theme; gameplay tunables remain in Config. Ghost names, tells, rarity and bait names come from existing content data. Example Hush text in the reference is from the current data row.

## Components and behavior

1. **Clock:** compact top-center card with a small `HOUSE VISIT` caption and the existing authoritative countdown. Warning color supplements a `Time almost up` label. Intermission reads `Next visit in N`. Do not imply a countdown pause.
2. **Bait tray:** three equally sized cards below the clock, using existing data names. Show only the active device's bindings: 1/2/3 (number-pad equivalent remains functional), X/Y/B, or tap labels. Each card still places bait immediately. Feedback must say `Placement requested` until server confirmation; no persistent selected-bait styling that falsely implies an equipped item.
3. **Ghost card:** restyle the existing world-attached name, rarity, tell, state and progress bar. Use a dark backing, 18 px name and 14–16 px supporting text at desktop reference scale. Keep the current progress bar for this first pass; no new radial-rendering implementation. State always has a readable label in addition to color. Progress follows the replicated server value and can drain; do not animate it to completion locally.
4. **Jar:** warm amber circular hold button, clear `HOLD` / `JAR` labels. Show F on keyboard, R2 on controller, no keyboard hint on touch. Held styling follows existing held-source state. Preserve all existing focus-loss, input-end, disconnect and respawn release paths.
5. **Guidance:** replace the long all-device instruction sentence with one short hint for the active control type. Example PC: `Aim at the ghost · Hold F or left mouse`. Keep touch hints clear of the thumbstick and jump control. Preserve existing server rejection wording; display in a stable notice region without covering bait buttons.
6. **Catch receipt:** small amber-accented toast for the existing server result, with grade. Only say `You rehomed Hush` when this player is in the eligible receipt; observer broadcasts must not imply personal credit. No pet/collection claim yet.

## Responsive rules

- Reference sizes: desktop 1280×720, phone landscape 844×390 and 667×375; also inspect narrow 390×844. These are planned QA sizes, not tested-device claims.
- Place all HUD content inside platform-safe bounds. Verify Roblox menu/chat, leaderboard, notches, thumbstick and jump overlays in actual Studio/device runs; the SVG's simplified safe area cannot certify this.
- Bait tray width = available safe width minus 32 px, capped at 432 px. Three equal columns with 8 px gaps; each touch target at least 48 px high. Permit two lines for longer names without clipping or shrinking to unreadable text.
- At height below 450 px, compact the clock and tray, reduce decorative padding, and use a 76–88 px jar target above the actual jump control. Do not scale the entire HUD down uniformly.
- Keep the center crosshair and ghost visible. Notices and receipts use reserved regions and wrap within safe bounds. Supporting hints may collapse before action controls.
- Use text labels as well as colors. Avoid rapid flashing, full-screen effects, constant bounces and decorative per-frame work.

## Builder scope and acceptance

Claude owns changes to client source. Keep server requests, rates, eligibility, timing, world geometry and state transitions unchanged. No lighting/world-art pass included in this request. Existing greybox remains the scene behind the new HUD; the SVG room is only a composition backdrop.

- Capture before/after screenshots on desktop and the phone sizes above, including maximum-length bait names, long notices, catch receipt, low timer and intermission.
- Check touch movement + jar hold together, release outside button, focus loss, controller disconnect, device-switch hints and respawn. Preserve number-pad bindings.
- Verify each bait action still sends one placement request and existing rejection throttling still works. Ensure HUD overlays do not consume camera input outside interactive controls.
- Inspect live progress drain, expiry mid-catch and observer receipt wording. The HUD must not promise credit before server confirmation.
- Report which checks were executed. Real-phone acceptance still requires actual hardware; a mockup or Studio preview is insufficient.

## Added flair pass — requested 2026-10-17

The updated SVG replaces the flat jar face with an amber gradient, a restrained halo and an engraved outer ring; adds mint-to-lavender progress accents and ghost-card corner marks; and shows a separate catch-celebration state with a ghost portrait, grade and a short friendly line. The toast and active catch shown on one sheet are state examples, not simultaneous gameplay. All particles, portraits and icons in this reference are editable vectors. Claude should use simple UI shapes or approved bundled assets, not a runtime SVG loader.

### Interaction choreography

| Trigger | Presentation | Duration / limit |
| --- | --- | --- |
| Bait hover / controller focus | Raise border brightness; show clear focus outline | 100 ms; desktop hover is supplementary |
| Bait press | Compress card to 97%, then return; label request pending without claiming success | 80 ms out / 120 ms back; animation must not block input |
| Jar held | Illuminate outer ring and warm inner gradient; restore released styling on every existing release path | 120 ms transition; no continuous pulse |
| Replicated progress changes | Update the existing bar; bright leading edge for progress, dimmer edge on drain | Never predict a catch; avoid smoothing that hides drainage |
| Confirmed eligible catch | Portrait toast enters 8 px upward, brief amber border bloom, grade and +1 catch | 180 ms entry, existing Config toast lifetime; at most 6 tiny spark shapes for 450 ms |
| Observer catch broadcast | Same restrained toast with `Hush was rehomed`; no personal +1 | Same lifetime; reuse receipt eligibility |
| Server rejection | Existing text in a coral-accented notice; no screen shake | Existing Config notice lifetime/throttle |
| Low clock | Amber then coral text with `Time almost up`; one transition | No flashing, ticking pulse or new urgency sound |
| Intermission | Muted lavender clock card; `Next visit in N` | Follow authoritative run state |

Use short, event-driven UI transitions and cancel superseded animations. Remove transient spark shapes after expiry, reset or GUI teardown; never accumulate connections or animated objects. No camera shake, gameplay zoom, full-screen blur or movement of the aiming reticle. Prefer a static halo built from a small number of layers; the SVG gradient is visual intent, not a required rendering technique.

### Small details that give it personality

- A small jar/ghost mark in the clock card and simple music-box, candle and teacup silhouettes on bait cards; keep text names visible. If an icon is unavailable, ship the text card instead of an unrelated emoji.
- Grade badge and ghost portrait reuse the ghost's data tint. Portrait here is decorative; it must not imply a saved pet, new species unlock or collection reward.
- Flavor line such as `A little less haunted.` belongs in presentation copy, never replaces the actual result. Do not expose the liked bait as a new automatic hint or invent teammate counts unavailable to the client.
- Keep sparks inside the toast region and away from camera aim. Mobile uses a compact toast, with optional decoration omitted before reducing text or touch target size.
- This pass adds no audio assets. A later sound pass can use approved/licensed assets after review; no arbitrary asset IDs in the UI patch.

### Reduced-motion and performance acceptance

Provide a presentation-only reduced-motion preference if no shared motion setting exists: replace scale/slide/sparks with instant state changes and a static border. Keep this local to presentation; do not create an account/settings service. Controls and information remain identical. No idle spark emitters or decorative frame loops. Check repeated catch/rejection/reset cycles for growing object or connection counts and verify the low-end phone profile. Visual/runtime/performance checks remain NOT RUN until Claude implements the pass.

### Review additions

Capture idle, focused, pressed, held, draining, eligible receipt, observer receipt, rejection and intermission. Verify rapid bait presses do not queue animation locks; overlapping results replace the toast cleanly; hold loss always clears illumination; reduced motion removes all optional movement. Keep touch controls usable under the new halo/portrait layers (decorative layers must not intercept input).

## Implementation handoff

Current source reviewed for layout: `src/client/Main.client.luau` at feature 5eec8bc. Current bait tray is 360 px wide, jar target 110 px, and bottom hint combines touch/keyboard/controller instructions. Implement the above as a small presentation-only change, then request Codex review of the source diff and screenshots. No new mechanics are authorized by this brief.
