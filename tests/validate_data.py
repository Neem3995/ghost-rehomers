"""Validate the JSON authoring contract; no Roblox runtime verification."""
import json
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "data"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def identifier(value):
    return text(value) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value) is not None


def fields(row, names, where):
    require(isinstance(row, dict), f"{where}: expected object")
    require(set(row) == set(names.split()), f"{where}: missing or unknown fields")


def rows(items, where):
    require(isinstance(items, list) and bool(items), f"{where}: expected nonempty array")
    seen = set()
    for row in items:
        require(isinstance(row, dict) and identifier(row.get("id")), f"{where}: invalid id")
        require(row["id"] not in seen, f"{where}: duplicate id {row['id']}")
        seen.add(row["id"])
    return seen


def validate(ghosts, bait, houses):
    ghost_ids = rows(ghosts, "ghosts")
    bait_ids = rows(bait, "bait")
    rows(houses, "houses")
    effects = set()
    for b in bait:
        fields(b, "id name effectTag earnedBy", b["id"])
        require(all(text(b[k]) for k in ("name", "effectTag", "earnedBy")), f"{b['id']}: invalid text")
        require(b["effectTag"] not in effects, "duplicate effectTag")
        effects.add(b["effectTag"])
    for g in ghosts:
        fields(g, "id name rarity tell likedBaitId dislikedBaitId baseModel tint accessories personality", g["id"])
        require(all(text(g[k]) for k in ("name", "tell", "baseModel", "personality")), f"{g['id']}: invalid text")
        require(g["rarity"] in ("Common", "Uncommon", "Rare", "Legendary"), f"{g['id']}: invalid rarity")
        require(g["likedBaitId"] in bait_ids and g["dislikedBaitId"] in bait_ids, f"{g['id']}: unknown bait reference")
        require(g["likedBaitId"] != g["dislikedBaitId"], f"{g['id']}: bait preferences overlap")
        tint = g["tint"]
        require(isinstance(tint, list) and len(tint) == 3 and all(type(v) is int and 0 <= v <= 255 for v in tint), f"{g['id']}: invalid tint")
        a = g["accessories"]
        require(isinstance(a, list) and all(text(v) for v in a) and len(a) == len(set(a)), f"{g['id']}: invalid accessories")
    for h in houses:
        fields(h, "id name rooms spawnTable timerConfigKey", h["id"])
        require(text(h["name"]) and text(h["timerConfigKey"]), f"{h['id']}: invalid text")
        room_ids = rows(h["rooms"], h["id"])
        for r in h["rooms"]:
            fields(r, "id name hidingSpots", r["id"])
            spots = r["hidingSpots"]
            require(text(r["name"]) and isinstance(spots, list) and bool(spots) and all(identifier(v) for v in spots) and len(spots) == len(set(spots)), f"{r['id']}: invalid room")
        require(isinstance(h["spawnTable"], list) and bool(h["spawnTable"]), "empty spawnTable")
        pairs = set()
        for s in h["spawnTable"]:
            fields(s, "ghostId roomId weight", "spawnTable")
            require(s["ghostId"] in ghost_ids and s["roomId"] in room_ids, "unknown spawn reference")
            pair = (s["ghostId"], s["roomId"])
            require(pair not in pairs, "duplicate spawn pair")
            pairs.add(pair)
            w = s["weight"]
            require(type(w) in (int, float) and math.isfinite(w) and w > 0, "invalid spawn weight")


def main():
    try:
        validate(*(json.loads((ROOT / name).read_text(encoding="utf-8")) for name in ("ghosts.json", "bait.json", "houses.json")))
    except (ValueError, TypeError, KeyError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: starter content schema and references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
