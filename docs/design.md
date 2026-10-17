# Ghost Rehomers: Design Doc

Oct 17, 2026 · Joseph Garcia

## Pitch

Ghost Rehomers is a cozy-spooky Roblox game for 1–4 players: you visit haunted houses, work out what each ghost likes, lure it with the right bait, catch it in a jar and keep it as a pet you can equip and show off, in a home you decorate.

- **One-line hook.** Don't fight the ghost. Find out what it likes, lure it, catch it, and rehome it.
- **Catching is the payoff of reading clues.** A correct guess about a ghost's quirk makes the catch easy; a wrong one sends it fleeing to another room.
- **No player death.** Failing costs time and a missed ghost, never a respawn wall, which keeps the game friendly, easy to code and playable on a phone.
- **Built to be updated.** Ghosts, bait and houses are data rows, so a new weekly haunting is mostly a data edit.
- **Monetization is cosmetic and collection-led,** matching what the 2026 research showed the earners use, with no gameplay advantage for sale.

## Core loop

One house visit: 5 steps, 1 decision, 1 retry loop. (Diagram omitted in this export: Enter house → Scout the tell → Choose and place bait → Hold the jar light to catch → Journal / pet / rewards, then next house.)

A wrong bait costs time, not a life: the ghost moves rooms and you try again. A caught ghost goes to the journal and can be equipped as a pet.

## The catching element

The catch is a two-step "lure, then jar" that rewards reading clues and works with a thumb on a phone, with no twitch aiming. Every number here is a starting value to tune in testing.

1. **Scout.** Each ghost has a tell: it hums near a music box, or flickers near candles. Watching it fills in a journal entry, which is the clue.
2. **Lure.** Place the matching bait in the ghost's room. The right bait makes it Curious: it drifts toward the bait and slows. The wrong bait Spooks it, so it flees to another room and the bait is used up.
3. **Catch.** Point the Rehoming Jar's light cone at a Curious ghost and hold. A ring fills while the ghost stays inside the light. Two or more players on the same ghost fill it faster. If the ghost leaves the light, progress drains.
4. **Grade.** A Perfect, Great or Good catch depends on how little the ghost wandered out of the light. The grade sets the ghost's starting affection, which unlocks its traits sooner, and never decides whether you keep it.

**States.** Each ghost is Drifting, Curious, Spooked or Caught, and the server owns that state, the bait check and the catch progress. Clients only send "placed bait" and "aimed jar" requests, which the server validates for distance, line of sight and rate.

**Failing.** If the house timer runs out, uncaught ghosts stay for the next visit. Nobody dies or respawns.

**Co-op without classes.** One player can scout and lure while another holds the jar, but any player can do either.

**Twists to test at Gate 2 (pick one, not all)**

- **Disguise.** Some ghosts hide inside ordinary objects until scouted, so finding them is a spot-the-odd-one-out puzzle.
- **Tough ghosts.** Rare ghosts need a short second timing ring after the first one fills.
- **Time of night.** The house's lighting changes which tells are visible.

## Content as data

Every ghost, bait item and house is a row in a data table, so a weekly update is mostly a data edit plus a model or two. That is what makes evening updates realistic.

| Table | Key fields | Notes |
| --- | --- | --- |
| Ghosts | id, name, rarity, tell, liked bait, disliked bait, base model, tint, accessories, one-line personality | One base model plus tint and accessories per ghost |
| Bait | id, name, effect tag, how it's earned | Each ghost's liked bait points to a row here |
| Houses | id, rooms, hiding spots, spawn table, timer | Built from reusable room modules |
| Haunting schedule | week, house, featured ghosts, limited-time variant | Drives the weekly rotation |
| Cosmetics | id, type (ghost outfit, jar skin, home theme), earned or Robux | Cosmetic only |

**Cheap variety.** Three base ghost shapes, six tints and eight accessories already give 144 combinations. Ship a curated subset so each ghost has a clear identity rather than every combination.

**Rarity.** Common, Uncommon, Rare and Legendary. Rarity sets how often a ghost appears in a house's spawn table and how hard it is to catch. Rarity is free and earned only; no paid random items at launch, since Roblox requires odds disclosure for those.

| Tier | Look | Starting spawn share | Catch |
| --- | --- | --- | --- |
| Common | White glow | about 60% | Easy |
| Uncommon | Soft blue glow | about 25% | Easy to medium |
| Rare | Purple glow with a sparkle trail | about 11% | Medium |
| Legendary | Gold aura, found only in certain houses | about 4% | Hard, may use the second timing ring |

Spawn shares are starting values to tune, not benchmarks. Limited-time ghosts from the weekly haunting carry a Limited tag on top of their tier, and any ghost has a small chance of a Shimmer recolor. Undiscovered ghosts show as silhouettes in the journal.

**Weekly rotation.** A "Haunting of the Week" features one house, a set of featured ghosts and one limited-time variant. The journal shows which ghosts you're missing, which is a reason to return.

**Saving.** The collection, journal and home layout need reliable saves. Test what happens when a save fails before any public release.

## Pets and showing off

Every caught ghost can become a pet that floats behind you, so the collection is something you wear, not just a list in a menu.

- **Equip.** You start with one pet slot, and more unlock with journal milestones. Equipped pets follow you in houses and in the hub.
- **Personality.** Pets react to emotes, idle with a short animation, and now and then say a line from their personality entry.
- **Nameplate and card.** A nameplate in the tier color sits over each pet. Tapping another player's pet shows its card: name, tier, catch grade, Limited tag and how long they've had it.
- **Affection.** Affection rises with the catch grade and with each day you play with the pet equipped, capped per day. Higher affection unlocks traits, outfits and a short bond animation. It rewards coming back without punishing a missed day.
- **Light assists, never power.** A trait can give a small hint, such as a faint glow toward a hiding spot. No pet is required to catch a ghost, and no pet is ever sold.
- **Display.** The hub has shelves and plinths for your ghosts and journal completion, plus a lobby area where players can see each other's equipped pets.
- **Mobile limits.** Cap how many pets render per player, and use a cheap tint and light before any particle aura.
- **Not in the MVP.** Trading. It brings scam and moderation risks, and Roblox has regional policy flags for trading paid items. Revisit after launch.

## Retention and monetization

The design maps directly onto the signals Roblox says drive recommendations, and it earns through cosmetics and collection, not power.

| Roblox signal | Design response |
| --- | --- |
| Play-through rate and first-play bounce | An honest thumbnail of a ghost in a lamp-lit room; a guided first lure and catch inside the first minute |
| Play days per user | A weekly haunting, journal gaps to fill, and pet affection that grows each day a pet is equipped |
| Playtime per user (counts up to 60 minutes a day) | 6–8 minute house visits chained by a "next house" button, with hub activities in between |
| Intentional co-play days | Faster catches with teammates, an invite button, private servers |
| Spend days and Robux per user | Small repeat cosmetic purchases rather than one big one |

The signals come from [Roblox's discovery docs](https://create.roblox.com/docs/discovery).

**What to sell**

- Ghost outfits, jar skins, home themes and nameplate frames.
- A seasonal pass with a free track and a paid track. The paid track gives cosmetics only; every ghost stays earnable through play.
- A private-server subscription for friend groups.

**What never to sell:** catch advantages, ghosts themselves, or better odds. No paid random crates at launch.

**Expectation check.** Reaching $3,000 a month takes about 63,000 monthly players at a 3% paying rate and 600 Robux per payer at the standard DevEx rate. Treat that as a hit-game outcome and judge your own revenue per player once real data exists.

## MVP and gates

The MVP is one house, three ghost species, one catch and a small hub with a journal; everything else waits until the hook is proven.

(Gate roadmap diagram omitted in this export: Gate 1 Foundation → Gate 2 Prove the hook → Decision → Gate 3 collection/pets/saves → Gate 4 weekly haunt/affection → Gate 5 unguided playtest → Gate 6 limited release.)

Only Gates 1 and 2 get time boxes now; the later gates wait for the decision.

**In the MVP**

- One house with three rooms, built from simple placeholder shapes.
- Three ghost species (Common, Uncommon, Rare), each with a tell and a liked bait.
- Three bait items.
- The lure-and-jar catch with the four ghost states, all owned by the server.
- Solo play and co-op for up to four players.
- A small hub with the journal, one display shelf and one equipped pet.
- Saves for the collection and the equipped pet.

**Held back:** the weekly rotation, the Legendary tier, affection, the cosmetics store, trading and extra houses.

**Time boxes assume about 8 hours a week and are placeholders.** Gate 1 is about 3 weeks, Gate 2 about 3–4, Gate 3 about 4 and Gate 4 about 3–4. Replace them with your measured pace after Gate 1.

- **Gate 1, Foundation (~3 weeks).** Exit: 10 catches in a row on phone and PC with no stuck states.
- **Gate 2, Prove the hook (~3–4 weeks).** Exit: fresh testers can explain their bait choice and ask for another house. Then the Decision: go on, one fix cycle, or shelve.
- **Gate 3 (~4 weeks).** Collection, pets and saves.
- **Gate 4 (~3–4 weeks).** Weekly haunt and affection.
- **Gate 5.** Unguided playtest.
- **Gate 6.** Limited release.

**Stop rules**

- A gate that runs past 1.5 times its time box means cutting scope, not adding hours.
- A failed Gate 2 playtest gets one fix cycle of up to two weeks and one retest. A second failure shelves the idea and keeps the code as portfolio work.
- New game ideas go in a notes file until the Gate 2 decision.

**Workflow carries over.** Use the same Rojo, Git and Studio testing setup and the shared `CLAUDE.md` / `AGENTS.md` brief as before, with the rules swapped for this game: the server owns catch state, content lives in data tables, and nothing sold gives an advantage.

## Risks and first tests

The biggest risks are a crowded genre and a catch that feels bad on a phone, and both can be tested before you build much.

| Risk | Why it matters | Mitigation |
| --- | --- | --- |
| Crowded collection genre | Many pet games already exist | The difference is clue, lure, catch; check that players can explain it from a short clip |
| Catch feels bad on touch | Holding a light cone steady is awkward on a phone | Test a gray-box catch on a real phone at Gate 1 |
| Ghosts don't read at thumbnail size | A weak thumbnail lowers play-through | Test each design as a flat silhouette with a glow |
| Lost or corrupted saves | The collection is the product | Test failed saves and rejoining at Gate 3 |
| Content treadmill | Weekly drops are hard around a full schedule | Build rotations ahead; move to every two weeks if needed |
| Young audience | Cozy and no-death helps, but safety still matters | Describe content accurately in Roblox's maturity questionnaire |

**Cheapest tests, in order**

1. **Clip test.** Record a 30-second clip of one scouted, lured and caught ghost. Show it to five people and ask what the game is.
2. **Thumbnail test.** Make two thumbnail options and ask which one they'd click.
3. **Gray-box catch.** One room, one ghost, on your phone, before any art.

## Open questions and next steps

The key choice left is how the catch should feel, since everything else follows from it.

**Questions for you**

- Do you want the catch setup-based, as drafted (lure, then hold the light), or a more active chase?
- What art style do you picture: soft and cute, or more gothic-cute?
- How many hours a week can you protect for this?
- Is "Ghost Rehomers" the final name? Search Roblox for similar titles before commissioning or making any art.

**Next steps**

- [ ] Pick the catch style and the Gate 2 twist (Disguise, Tough ghosts or Time of night)
- [ ] Set up the Rojo + Git project and the shared brief files
- [ ] Gray-box one room and one ghost, and test the catch on your phone
- [ ] Record the 30-second clip and show it to five people
- [ ] Write the three starter ghosts as data rows: tell, liked bait, rarity
