import numpy as np
import json
import urllib.request
from datetime import datetime
from datetime import timedelta
from scipy.signal import argrelextrema


def getMatarikiFromAPI(year):
    TWENTYTHREEDAYS = timedelta(days=23)
    NINETEENJUNE = datetime(year, 6, 19)
    # month_start_index = -1

    # API Platfprm used - https://web.postman.co/
    url = fr"https://ssd.jpl.nasa.gov/api/horizons.api?format=json&COMMAND='301'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@399'&START_TIME='{year}-05-26'&STOP_TIME='{year}-07-30'&STEP_SIZE='1h'&QUANTITIES='24'&TIME_ZONE='-12:00'"

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    data = result['result'].partition('$$SOE')[2].partition('$$EOE')[0]
    times = data.split('\n')[1:-1]
    stos = np.array([times[i].split() for i in range(len(times))])

    stos_cleaned = stos[:, 2].astype(float)
    new_moon = argrelextrema(stos_cleaned, np.greater)[0]

    for i in range(len(new_moon)):
        tangaroa = datetime.strptime(
            stos[new_moon[i]][0], '%Y-%b-%d') + TWENTYTHREEDAYS
        if tangaroa >= NINETEENJUNE:
            # month_start_index = i
            break

    # for i in range(len(new_moon)):
    #     start = datetime.strptime(stos[new_moon[i]][0], '%Y-%b-%d')

    #     hours, mins = map(float, stos[new_moon[i]][1].split(':'))
    #     if timedelta(hours=hours, minutes=mins) <= timedelta(hours=6):
    #         start -= timedelta(days=1)

    #     tangaroa = start
    #     tangaroa += TWENTYTHREEDAYS
    #     if tangaroa >= NINETEENJUNE:
    #         # month_start_index = i
    #         break

    def getClosestFriday(d0):
        if (d0.weekday() < 4):
            matariki = d0+timedelta(4-d0.weekday())
        else:
            matariki = d0-timedelta(d0.weekday()-4)

        if matariki < NINETEENJUNE:
            matariki += timedelta(days=7)

        return matariki

    # print(f"date : {date}")
    return getClosestFriday(tangaroa).strftime('%Y-%m-%d')


print(getMatarikiFromAPI(2030))
