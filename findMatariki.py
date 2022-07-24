import numpy as np
import json
import urllib.request
from datetime import datetime, timedelta
from scipy.signal import argrelextrema


def getMatarikiFromAPI(year):
    TWENTYTHREEDAYS = timedelta(days=22)
    NINETEENJUNE = datetime(year, 6, 18)

    url = fr"https://ssd.jpl.nasa.gov/api/horizons.api?OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&format=json&COMMAND='301'&QUANTITIES='24'&CENTER='500@399'&START_TIME='{year}-05-26'&STOP_TIME='{year}-07-30'&TIME_ZONE='+12:00'&STEP_SIZE='1h'"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = result['result'].partition('$$SOE')[2].partition('$$EOE')[0]
    times = data.split('\n')[1:-1]
    stos = [times[i].split() for i in range(len(times))]
    stos = np.array(stos)
    stos_cleaned = stos[:, 2].astype(float)
    new_moon = argrelextrema(stos_cleaned, np.greater)[0]

    stos = stos[:-1]

    def getClosestFriday(d0):
        if (d0.weekday() < 4):
            matariki = d0+timedelta(4-d0.weekday())
        else:
            matariki = d0-timedelta(d0.weekday()-4)

        if matariki < NINETEENJUNE:
            matariki += timedelta(days=7)

        return matariki

    for i in range(len(new_moon)):
        tangaroa = datetime.strptime(
            stos[new_moon[i]][0], '%Y-%b-%d') + TWENTYTHREEDAYS
        if tangaroa >= NINETEENJUNE:
            break

    return getClosestFriday(tangaroa).strftime('%Y-%m-%d')


print(getMatarikiFromAPI(2021))
