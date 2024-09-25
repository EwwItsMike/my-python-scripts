import requests
import time

API_URL = "https://api.wiseoldman.net/v2/players/{0}"

def update_players():
    with open('names.txt') as f:
        lines = f.read().splitlines()
        over100players(lines)


def over100players(lines):
    bad_requests = []

    count = 0
    for line in lines:
        count += 1

        if count % 19 == 0:
            for i in range(6):
                print("Sleeping until API unblocks. Remaining: " + str(60 - 10*i))
                time.sleep(10)
            print("Resuming...")
        line.replace(" ", "%20")
        line.replace("-", "%20")
        line.replace("_", "%20")
        response = requests.post(API_URL.format(line))
        if not response.ok:
            print("Player not updated: {}".format(line) + "     Reason: {}".format(response.reason))
            if response.reason.casefold() == "bad request".casefold() or response.reason.casefold() == "internal server error":
                bad_requests.append(line)
            elif response.reason.casefold() == "too many requests".casefold() or response.reason.casefold() == 'gateway time-out':
                lines.append(line)

    print("Unable to update the following players:")
    for name in bad_requests:
        print(name)


update_players()
