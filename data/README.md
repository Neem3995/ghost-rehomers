# Starter content contract

UTF-8 JSON arrays are the authoring source. Run `python tests/validate_data.py` from the project root (Python 3, standard library only). No Roblox importer exists yet; Claude must choose and document the Rojo/runtime mapping. Do not claim these files are loaded by the game.

All rows require a unique, nonempty `id`; IDs use lowercase letters, digits and hyphens. All listed fields are required. Unknown fields are rejected to catch misspellings. Text fields are nonempty strings. References are case-sensitive.

## Ghosts: ghosts.json

| Field | Valid value |
| --- | --- |
| id, name | Stable identifier; display name |
| rarity | Common, Uncommon, Rare, Legendary (starter set uses the first three) |
| tell | Observable clue text; builder must implement the matching behavior |
| likedBaitId, dislikedBaitId | Existing bait IDs; must differ |
| baseModel | Symbolic asset key; currently placeholder-ghost, not a verified Studio asset |
| tint | Three integer RGB channels, each 0–255 |
| accessories | List of unique nonempty symbolic asset keys; empty for Gate 1 |
| personality | One-line flavor text; no pet behavior implied |

## Bait: bait.json

`id`, `name`, `effectTag` (symbolic presentation/effect key), `earnedBy` (acquisition description). Effect tags are unique. These rows describe free test supplies; replenishment and consumption rules require builder confirmation. Ghost matching uses bait IDs, not effect tags.

## Houses: houses.json

`id`, `name`, `rooms`, `spawnTable`, `timerConfigKey`.

- `rooms`: nonempty list of `{id, name, hidingSpots}`. Room IDs are unique within the house; hiding spots are unique symbolic IDs within each room. These are content definitions, not constructed rooms.
- `spawnTable`: nonempty list of `{ghostId, roomId, weight}` referencing existing ghosts and this house's rooms. Each ghost/room pair is unique. Weight is a positive finite number; select proportionally to total weight. Starter weights total 96, intentionally excluding the held-back Legendary tier; they are not percentages.
- `timerConfigKey`: symbolic Config lookup, currently `HouseDurationSeconds`. The duration belongs in Claude's shared Config, not this table. Validator checks syntax only until Config exists.

Gate 1 runtime uses one room and one ghost with deterministic selection for repeatable tests. Three rooms/species here are the requested starter content only; building additional rooms, art, pets or spawning systems is outside this task. Grade thresholds, distances, rates, timers and progress tuning belong in Config. Unlisted bait behavior and wrong-bait consumption remain design decisions, not assumptions in these rows.
