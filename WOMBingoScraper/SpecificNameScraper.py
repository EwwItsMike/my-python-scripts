import csv
import time

import requests

API_URL = "https://api.wiseoldman.net/v2/players/{0}/gained"

METRICS = ['overall', 'attack', 'defence', 'strength', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking', 'woodcutting', 'fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore', 'agility', 'thieving', 'slayer', 'farming', 'runecrafting', 'hunter', 'construction', 'league_points', 'bounty_hunter_hunter', 'bounty_hunter_rogue', 'clue_scrolls_all', 'clue_scrolls_beginner', 'clue_scrolls_easy', 'clue_scrolls_medium', 'clue_scrolls_hard', 'clue_scrolls_elite', 'clue_scrolls_master', 'last_man_standing', 'pvp_arena', 'soul_wars_zeal', 'guardians_of_the_rift', 'colosseum_glory', 'abyssal_sire', 'alchemical_hydra', 'artio', 'barrows_chests', 'bryophyta', 'callisto', 'calvarion', 'cerberus', 'chambers_of_xeric', 'chambers_of_xeric_challenge_mode', 'chaos_elemental', 'chaos_fanatic', 'commander_zilyana', 'corporeal_beast', 'crazy_archaeologist', 'dagannoth_prime', 'dagannoth_rex', 'dagannoth_supreme', 'deranged_archaeologist', 'duke_sucellus', 'general_graardor', 'giant_mole', 'grotesque_guardians', 'hespori', 'kalphite_queen', 'king_black_dragon', 'kraken', 'kreearra', 'kril_tsutsaroth', 'lunar_chests', 'mimic', 'nex', 'nightmare', 'phosanis_nightmare', 'obor', 'phantom_muspah', 'sarachnis', 'scorpia', 'scurrius', 'skotizo', 'sol_heredit', 'spindel', 'tempoross', 'the_gauntlet', 'the_corrupted_gauntlet', 'the_leviathan', 'the_whisperer', 'theatre_of_blood', 'theatre_of_blood_hard_mode', 'thermonuclear_smoke_devil', 'tombs_of_amascut', 'tombs_of_amascut_expert', 'tzkal_zuk', 'tztok_jad', 'vardorvis', 'venenatis', 'vetion', 'vorkath', 'wintertodt', 'zalcano', 'zulrah', 'ehp', 'ehb']
player_data = {}

# dates used ISO8601 standards: example:"2020-04-26T21:38:35.779Z"
def request_data(name, startDate, endDate):
    full_url = API_URL.format(name) + "?startDate={0}&endDate={1}".format(startDate, endDate)
    response = requests.get(full_url)
    js = response.json()

    if response.ok:
        print(js)
        for entry in js['data']['skills'].keys():
            if entry in METRICS:
                player_data[name][entry] = js['data']['skills'][entry]['experience']['gained']
        for entry in js['data']['bosses'].keys():
            if entry in METRICS:
                player_data[name][entry] = js['data']['bosses'][entry]['kills']['gained']
        for entry in js['data']['activities'].keys():
            if entry in METRICS:
                player_data[name][entry] = js['data']['activities'][entry]['score']['gained']
        for entry in js['data']['computed'].keys():
            if entry in METRICS:
                player_data[name][entry] = js['data']['computed'][entry]['value']['gained']
    else:
        print("Could not request player data for: {}    Reason: {}".format(name, response.reason))
        print(response.content)


def write_data_to_spreadsheet():
    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        fieldnames = ['player']
        for m in METRICS:
            fieldnames.append(m)

        writer = csv.writer(f)
        writer.writerow(fieldnames)

        for entry in player_data:
            name = entry.replace("%20", " ")
            to_add = [name]
            for v in list(player_data[entry].values()):
                to_add.append(v)
            # print(to_add)
            writer.writerow(to_add)


def get_names_from_file():
    with open('names.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            line.replace(" ", "%20")
            line.replace("-", "%20")
            line.replace("_", "%20")
            player_data[line] = {m:0 for m in METRICS}


get_names_from_file()

count = 0
for name in player_data.keys():
    count += 1

    if count % 19 == 0:
        for i in range(6):
            print("Sleeping until API unblocks. Remaining: {}".format(60-i*10))
            time.sleep(10)
        print("Resuming...")
    request_data(name, "2024-06-14T12:00:00.000Z", "2024-06-30T22:59:00.000Z")
write_data_to_spreadsheet()
