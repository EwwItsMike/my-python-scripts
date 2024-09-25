import datetime

import pytz as pytz
import requests

API_URL = "https://api.wiseoldman.net/v2"

def get_inactives():
    max_inactive_timestamp = datetime.datetime.now(tz=pytz.UTC) - datetime.timedelta(weeks=8)
    response = requests.get(API_URL + "/groups/2828")
    json = response.json()

    inactives = []

    for member in json['memberships']:
        lastChangedAt = member['player']['lastChangedAt']
        lastUpdated = datetime.datetime.now(tz=pytz.UTC) - datetime.timedelta(weeks=25)
        if lastChangedAt is not None:
            lastUpdated = datetime.datetime.fromisoformat(member['player']['lastChangedAt'])
        if max_inactive_timestamp > lastUpdated:
            print("max: " + str(max_inactive_timestamp))
            print("lastUpdated: " + str(lastUpdated))
            inactives.append(member['player']['username'])

    write_to_file(inactives)


def write_to_file(names):
    with open("inactives.txt", 'w', encoding='UTF8') as f:
        for name in names:
            f.write(name + "\n")
    print("Added {} names to the inactives list".format(len(names)))


get_inactives()
