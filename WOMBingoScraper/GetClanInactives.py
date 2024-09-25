import datetime
import time

import requests

API_URL = "https://api.wiseoldman.net/v2"

def update_clan_members():
    full_url = API_URL + "/groups/2828/update-all"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(full_url, json={"verificationCode": "669-466-576"}, headers=headers)
    time.sleep(60)
    print(response.content)


# dates used ISO8601 standards: example:"2020-04-26T21:38:35.779Z"
def get_inactives():
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(weeks=24)
    full_response = []

    for i in range(9):
        full_url = API_URL + "/groups/2828/gained?startDate={0}&endDate={1}&metric=overall&offset={2}&limit={3}".format(start_date.isoformat(), end_date.isoformat(), 450-(50*i), 50)
        response = requests.get(full_url)
        full_response.extend(response.json())

    names = []

    for entry in full_response:
        if entry['gained'] <= 50000:
            names.append(entry['player']['displayName'])
    write_to_file(names)


def write_to_file(names):
    with open("inactives.txt", 'w', encoding='UTF8') as f:
        for name in names:
            f.write(name + "\n")
    print("Added {} names to the inactives list".format(len(names)))


# update_clan_members()
get_inactives()
