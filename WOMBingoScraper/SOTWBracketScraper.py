import time
import requests

API_URL = "https://api.wiseoldman.net/v2/competitions/{0}"
competition_id = 23686

bracket1 = []
bracket2 = []
bracket3 = []

def get_from_wom_and_put_in_brackets():
    response = requests.get(API_URL.format(competition_id))
    json = response.json()

    count = 0
    for participant in json['participations']:
        count += 1
        if count % 90 == 0:
            for i in range(31):
                print("Pausing until WOM API unblocks. Time remaining: {0} seconds.".format(str(310 - 10*i)))
                time.sleep(10)
            print("Resuming...")

        playerResponse = requests.get("https://api.wiseoldman.net/v2/players/{0}".format(participant['player']['username']))
        if not playerResponse.ok:
            print("Requesting player info failed. Try again in 5 minutes.")
            print("Fail reason: " + playerResponse.reason)
            return

        playerData = playerResponse.json()
        level = playerData['latestSnapshot']['data']['skills'][json['metric']]['level']

        if level <= 50:
            bracket1.append((participant['player']['username'], participant['progress']['gained']))
        elif level <= 80:
            bracket2.append((participant['player']['username'], participant['progress']['gained']))
        else:
            bracket3.append((participant['player']['username'], participant['progress']['gained']))


def get_winner(bracket):
    current_best = ('', 0)
    for participant in bracket:
        if participant[1] > current_best[1]:
            current_best = participant
    return current_best


get_from_wom_and_put_in_brackets()
print("Bracket 1: " + str(bracket1))
print("Bracket 2: " + str(bracket2))
print("Bracket 3: " + str(bracket3))

print("Bracket 1 winner:" + str(get_winner(bracket1)))
print("Bracket 2 winner:" + str(get_winner(bracket2)))
print("Bracket 3 winner:" + str(get_winner(bracket3)))
