import json
import urllib.request
from datetime import datetime
from datetime import timedelta


def getMatarikiFromAPI(year):

    # API Platfprm used - https://web.postman.co/
    url = fr"https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='301'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@399'&START_TIME='{year}-06-19'&STOP_TIME='{year}-07-15'&STEP_SIZE='60min'&QUANTITIES='24"

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = result['result'].partition('$$SOE')[2].partition('$$EOE')[0]
    times = data.split('\n')[1:-1]
    stos = [times[i].split() for i in range(len(times))]

    for time in stos:
        del time[1]

    for i in range(len(stos)-1):
        stos[i][1] = float(stos[i][1])
        stos[i].append(abs(stos[i][1]-90))

    stos = stos[:-1]

    for i in range(len(stos)-1):
        stos[i].append(True if (stos[i+1][1]-stos[i][1] > 0)else False)

    stos = stos[:-1]

    minimum = stos[0]

    for time in stos:
        if time[3]:
            if time[2] < minimum[2]:
                minimum = time

    tangaroa = minimum[0]

    def getClosestFriday(d0):
        # If it's a Saturday, the previous Friday is chosen instead of the next
        if (d0.weekday() < 4):
            return d0+timedelta(4-d0.weekday())
        else:
            return d0-timedelta(d0.weekday()-4)

    date = datetime.strptime(tangaroa, '%Y-%b-%d')

    # print(f"date : {date}")
    return getClosestFriday(date).strftime('%Y-%m-%d')


# print(getMatarikiFromAPI(2028))
