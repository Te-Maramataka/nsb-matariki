import numpy as np
import json
import urllib.request
from datetime import datetime
from datetime import timedelta
from scipy.signal import argrelextrema


def getMatarikiFromAPI(year):

    # API Platfprm used - https://web.postman.co/
    url = fr"https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='301'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@399'&START_TIME='{year}-05-26'&STOP_TIME='{year}-07-30'&STEP_SIZE='24h'&QUANTITIES='24"

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = result['result'].partition('$$SOE')[2].partition('$$EOE')[0]
    times = data.split('\n')[1:-1]
    stos = [times[i].split() for i in range(len(times))]

    for time in stos:
        del time[1]

    stos_cleaned = np.array(stos)[:, 1].astype(float)

    new_moon = argrelextrema(stos_cleaned, np.greater)
    TWENTYTHREEDAYS = timedelta(days=23)
    NINETEENJUNE = datetime(year, 6, 19)

    for new_month in new_moon[0]:
        tangaroa = datetime.strptime(
            stos[new_month][0], '%Y-%b-%d') + TWENTYTHREEDAYS
        if tangaroa >= NINETEENJUNE:
            break

    def getClosestFriday(d0):
        # If it's a Saturday, the previous Friday is chosen instead of the next
        if (d0.weekday() < 4):
            return d0+timedelta(4-d0.weekday())
        else:
            return d0-timedelta(d0.weekday()-4)

    # print(f"date : {date}")
    return getClosestFriday(tangaroa).strftime('%Y-%m-%d')


print(getMatarikiFromAPI(2022))
