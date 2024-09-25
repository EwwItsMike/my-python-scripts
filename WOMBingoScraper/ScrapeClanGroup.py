import csv
import time

import requests

API_URL = "https://api.wiseoldman.net/v2/groups/2828/gained/"
METRICS = ['overall', 'attack', 'defence', 'strength', 'hitpoints', 'ranged', 'prayer', 'magic', 'cooking', 'woodcutting', 'fletching', 'fishing', 'firemaking', 'crafting', 'smithing', 'mining', 'herblore', 'agility', 'thieving', 'slayer', 'farming', 'runecrafting', 'hunter', 'construction', 'league_points', 'bounty_hunter_hunter', 'bounty_hunter_rogue', 'clue_scrolls_all', 'clue_scrolls_beginner', 'clue_scrolls_easy', 'clue_scrolls_medium', 'clue_scrolls_hard', 'clue_scrolls_elite', 'clue_scrolls_master', 'last_man_standing', 'pvp_arena', 'soul_wars_zeal', 'guardians_of_the_rift', 'colosseum_glory', 'abyssal_sire', 'alchemical_hydra', 'artio', 'barrows_chests', 'bryophyta', 'callisto', 'calvarion', 'cerberus', 'chambers_of_xeric', 'chambers_of_xeric_challenge_mode', 'chaos_elemental', 'chaos_fanatic', 'commander_zilyana', 'corporeal_beast', 'crazy_archaeologist', 'dagannoth_prime', 'dagannoth_rex', 'dagannoth_supreme', 'deranged_archaeologist', 'duke_sucellus', 'general_graardor', 'giant_mole', 'grotesque_guardians', 'hespori', 'kalphite_queen', 'king_black_dragon', 'kraken', 'kreearra', 'kril_tsutsaroth', 'lunar_chests', 'mimic', 'nex', 'nightmare', 'phosanis_nightmare', 'obor', 'phantom_muspah', 'sarachnis', 'scorpia', 'scurrius', 'skotizo', 'sol_heredit', 'spindel', 'tempoross', 'the_gauntlet', 'the_corrupted_gauntlet', 'the_leviathan', 'the_whisperer', 'theatre_of_blood', 'theatre_of_blood_hard_mode', 'thermonuclear_smoke_devil', 'tombs_of_amascut', 'tombs_of_amascut_expert', 'tzkal_zuk', 'tztok_jad', 'vardorvis', 'venenatis', 'vetion', 'vorkath', 'wintertodt', 'zalcano', 'zulrah', 'ehp', 'ehb']
# METRICS = ['alchemical_hydra']
player_data = {}

# dates used ISO8601 standards: example:"2020-04-26T21:38:35.779Z"
def request_data(startDate, endDate, metric):
    full_url = API_URL + "?startDate={}".format(startDate) + "&endDate={}".format(endDate) + "&metric={}".format(metric)
    j = requests.get(full_url)

    needed = {}

    if j.ok:
        for entry in j.json():
            name = entry['player']['displayName']
            gained = entry['data']['gained']
            needed[name] = gained

    return needed


def add_to_player_data(metric, entries):
    for entry in entries.keys():

        # player wasn't tracked yet
        if entry not in player_data.keys():
            player_data[entry] = {}
            for m in METRICS:
                player_data[entry][m] = 0

        # add metric data to player data
        player_data[entry][metric] = entries[entry]


def write_data_to_spreadsheet():
    with open('data.csv', 'w', encoding='UTF8', newline='') as f:
        fieldnames = ['player']
        for m in METRICS:
            fieldnames.append(m)

        writer = csv.writer(f)
        writer.writerow(fieldnames)

        for entry in player_data:
            to_add = [entry]
            for v in list(player_data[entry].values()):
                to_add.append(v)
            # print(to_add)
            writer.writerow(to_add)


def main():
    for metric in METRICS:
        add_to_player_data(metric, request_data("2024-04-12T16:00:00.000Z", "2024-04-27T02:30:00.000Z", metric))
    write_data_to_spreadsheet()
    print(player_data)


t0 = time.process_time()
main()
t1 = time.process_time()

print("Import completed in: {:.5f} seconds.".format(t1-t0))
