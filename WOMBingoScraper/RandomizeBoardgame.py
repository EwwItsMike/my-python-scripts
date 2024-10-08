HARDTILES = [
"Dragon Warhammer",
"Lord of the Rings (all 4 DKS rings)",
"Lord of the Trash (mud bstaff, dragon axe, seercul, ring of life)",
"5 Unsired drops",
"Tanzanite fang",
"Magic fang",
"Uncut onyx (Zulrah)",
"Serpentine visage",
"Wilderness shield (all shards from same shield)",
"Dragon pickaxe",
"Any Wilderness ring (treasonous/tyrannical/gods)",
"Any voidwaker piece",
"Boss pet (no skotizo/chompy etc)",
"Skilling pet (skilling pet collog tab + herbi, zalcano. Maybe tempo/phoenix?)",
"Hydra leather OR Hydra’s claw",
"3 Brimstone ring pieces",
"Hydra tail",
"1 full barrows set in ANY combination (any helm, top, legs and weapon)",
"Primordial crystal",
"Eternal crystal",
"Pegasian crystal",
"Smouldering stone",
"Any Godwars Dungeon hilt (except Ancient)",
"Corporeal beast unique (any sigil OR holy elixir, NOT shield)",
"Any Boss jar",
"5 sub-40 Fire capes, or 2 sub-90 infernal capes",
"3 Gauntlet seeds (any combo of armour, weapon or enhanced)",
"Bandos GWD piece (Chestplate or Tassets)",
"Grotesque Guardians - Ring+Gloves+hammer OR core",
"Armadyl GWD unique (Chestplate or Chainskirt)",
"Zamorak GWD unique (spear or SotD)",
"Sara GWD unique (crossbow or sword)",
"Any Nex unique (hilt, horn, vambs, or torva piece)",
"Any Nightmare unique (mace, inq piece, staff or orb)",
"5 Venator shards (not from Frozen cache)",
"4 Sarachnis Cudgels",
"Vorkath unique (draconic/skeletal visage or dbone neck, must be from Vorkath)",
"CoX prayer scroll (Dex or Arcane, NOT torn)",
"Non-scroll CoX purple",
"ToA OR ToB purple (no lightbearer or osmumten’s fang)",
"Any 3 pieces of Elder Chaos druid robes",
"3 Zenyte shard",
"Heavy or Light ballista frame",
"Revenant weapon or avarice",
"1 of top 4 rev totems (relic, effigy, medallion or statuette)",
"Dust battlestaff AND Mist battlestaff (does not need to be from superior)",
"Leaf-bladed Battleaxe",
"Granite Longsword or Granite Boots",
"Dragon Sword or Dragon Harpoon",
"Blood shard (not from thieving)",
"Obsidian armour piece",
"Crystal Grail",
"Any Champion scroll",
"Occult necklace",
"Drakes unique (tooth or claw)",
"Dragon chainbody",
"Brine Saber",
"Dark bow",
"Dragon 2h sword",
"Tome of Fire or Tome of Water",
"Broken Dragon pickaxe",
"Pharaoh’s Sceptre",
"Mimic",
"Ranger boots",
"Dragon spear OR Shield left half",
"Any drop worth over 20m",
"Zalcano shard or Crystal tool seed",
"Hill giant club OR Bryophyta’s essence",
"Easy clue Team cape or Monk robe (g) piece",
"Any god d’hide boots",
"Any Elite clue unique (no Shared table)",
"Mask of Ranul",
"Strange old lockpick",
"Dragon Limbs",
"Full Ancient ceremonial set",
"Giant Shark",
"Giant Swordfish",
"Giant Bass",
"5 Gnome scarfs AND 5 Gnome Goggles",
"All 3 pieces of the Sandwich Lady outfit",
"Ornament kit from Master Clues",
"All 4 pages of a single God book (rightclick the page in screenshot)",
"Onyx from Tekton",
"5x Fedora",
"2500 total Onyx bolts (e)"
]

MIDTILES = [
"Lord of the rings",
"Any 5 Zulrah uniques",
"2 Unsired drops",
"Wilderness shield (all shards from same shield)",
"Dragon pickaxe",
"Any Wilderness ring",
"Any Voidwaker piece",
"Brimstone ring piece",
"Hydra unique (claw, tail, leather, knives or thrownaxes, from Alch hydra)",
"Full set of Barrows gear (any combination of helm, top, legs and weapon)",
"Any 4 Cerberus crystals",
"Any Bandos GWD unique (chestplate, tassets, boots, hilt)",
"Any Armadyl GWD unique (chestplate, chainskirt, helmet, hilt)",
"Any Zamorak GWD unique (spear, sotd, steam bstaff, hilt)",
"Any Saradomin GWD unique (crossbow, sword, light, hilt)",
"Corporeal Beast unique (any sigil, or holy elixir. NOT shield)",
"Any boss jar",
"5 Sub-40 Fire capes, or 2 Sub-90 Infernal capes",
"Any 2 Gauntlet seeds (weapon, armour, enhanced)",
"Any 2 Grotesque Guardian unique (ring, gloves, hammer, core)",
"Any Nex unique (hilt, horn, vambs, or torva piece)",
"3 Venator shards (not from Frozen chache)",
"2 Sarachnis cudgels",
"5 Vorkath heads",
"CoX prayer scroll (Dex or Arcane, NOT torn)",
"Non-scroll CoX unique",
"ToA purple",
"ToB purple",
"Any 3 pieces of Elder Chaos Druid robes",
"2 Zenyte shards",
"Any 5 pieces of a Ballista (limbs, spring, heavy frame, light frame, monkey tail)",
"Revenant unique (Not from Superior)",
"Dust battlestaff or Mist battlestaff (does not need to be from superior)",
"Leaf-bladed battleaxe",
"Granite longsword or Granite boots",
"Blood shard (not from thieving)",
"Obsidian armour piece",
"Crystal Grail",
"Any champion scroll",
"Any Revenant weapon attachment (vene fangs, callisto claws, vetion skull)",
"Pharaoh’s sceptre",
"Occult necklace",
"Dragon chainbody",
"Dragon 2h sword",
"Any drop worth over 15m",
"Full Ancient ceremonial set",
"Dragon sword or Dragon harpoon",
"Lord of the Trash (mud bstaff, dragon axe, seercul, ring of life)"
]

import random

TILES = MIDTILES

random.shuffle(TILES)

for i in range(len(TILES)):
    print(TILES[i])


