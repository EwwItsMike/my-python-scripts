import requests
import time

API_URL = "https://api.wiseoldman.net/v2"

def get_shitters():
    response = requests.get(API_URL + "/groups/2828")
    json = response.json()

    names = []
    shitters = []

    for member in json['memberships']:
        names.append(member['player']['username'])

    count = 0;

    for name in names:
        if count % 19 == 0:
            for i in range(6):
                print("Sleeping until API unblocks. Remaining: " + str(60 - 10*i))
                time.sleep(10)
            print("Resuming...")

        response = requests.get(API_URL + "/players/" + name)
        json = response.json()
        if json['latestSnapshot']['data']['skills']['overall']['level'] < 1500:
            shitters.append(json['username'])
        count += 1

    return shitters

print(get_shitters())
