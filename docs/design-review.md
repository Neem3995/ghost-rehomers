# Gate 1 design QA — 2026-10-17

These are open design/acceptance gaps, not code defects. No source implementation exists in this folder yet. Ranked by effect on Gate 1.

| Priority | Location | Gap / failure scenario | Proposed resolution for builder confirmation |
| --- | --- | --- | --- |
| 1 | design.md: catching / Gate 1 exit | “10 catches” lacks device, reset, failure and evidence definitions; a reset between catches could conceal a stuck state. | Use tests/gate1-test-plan.md: separate 10-catch streaks on real phone and PC, no manual recovery, recorded build/Config and per-catch evidence. |
| 2 | design.md: states / failing | No transition out of Caught, Curious or Spooked, no reset timing, and no rule for timeout during a catch. Repeat catches can stall. | Document transition conditions and Config timers, reset/rearm path, timeout precedence and progress clearing before testing. |
| 3 | design.md: lure vs PROMPTS.md: one room | Wrong bait must flee to another room, but Gate 1 explicitly builds one room. | Gate 1 uses another valid spot in the same room, as the builder prompt says; confirm this temporary exception. Three-room data does not authorize building three rooms. |
| 4 | design.md: catch / grade | Cone/range/LOS, drain/fill, co-op stacking and grade thresholds lack exact rules. Grades and faster co-op cannot be verified numerically. | Builder supplies Config values and formulas, server aim validation, stale-input expiry, progress bounds and grade behavior on uninterrupted versus interrupted catches. |
| 5 | design.md: lure / bait | The third bait is neither liked nor disliked; consumption for correct bait, repeated bait, bait ownership and replenishment are undefined. | Decide behavior for every bait category and state; free supplies must permit repeat testing without a soft lock. Reject invalid placement without consuming supplies. |
| 6 | design.md: co-op / rewards | Catch ownership, eligibility and departing contributors are undefined; simultaneous completion could grant duplicates. | Define eligible players, exactly-once completion per catch and cleanup on leave. Gate 1 may use a visible catch receipt; pets, collection and persistence wait for Gate 3. |
| 7 | design.md: content / prompt | JSON data needs a runtime mapping; room/asset keys and Config references cannot yet be checked against a build. | Claude documents importer/Rojo mapping and verifies symbolic references against actual assets/Config. Gate 1 selects one ghost deterministically. |
| 8 | design.md: next steps vs STATUS.md | Catch style is still listed as open in design, but STATUS records setup-based as chosen. | Treat STATUS choice as provisional through Gate 2; reconcile source text when approved. |

No Roblox API or policy claims were evaluated. Monetization/research claims are outside this Gate 1 review. Gate 2 twists, art, pets, saves and extra runtime rooms remain deferred.
