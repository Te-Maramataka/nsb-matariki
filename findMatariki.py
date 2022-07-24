import numpy
import json
import urllib.request
from datetime import datetime, timedelta
from scipy.signal import argrelextrema


class Matariki(object):

    # This function takes the year and calls Nasa's API, returning STO values in a numpy array
    # Default settings: location = Auckland Observatory, timezone = GMT+12, frequency = 1 hour
    @staticmethod
    def getSTOS(year, center=500, timezone='+12:00', step_size='1h'):
        url = fr"https://ssd.jpl.nasa.gov/api/horizons.api?OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&format=json&COMMAND='301'&QUANTITIES='24'&CENTER='{center}@399'&START_TIME='{year}-05-26'&STOP_TIME='{year}-07-30'&TIME_ZONE='{timezone}'&STEP_SIZE='{step_size}'"
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        
        # Extract ephemeris from the results column
        data = result['result'].partition('$$SOE')[2].partition('$$EOE')[0]
        times = data.split('\n')[1:-1]
        stos = [times[i].split() for i in range(len(times))]
        return numpy.array(stos)

    # This function finds and returns indexes of local maximas after taking STO values in a numpy array
    @staticmethod
    def getNewMoons(stos):
        stos_cleaned = stos[:, 2].astype(float)
        return argrelextrema(stos_cleaned, numpy.greater)[0]

    # This function inputs the first day of the Tangaroa period, day 0, and returns the closest Friday,
    # assuming the Tangaroa period is four days long
    @staticmethod
    def getClosestFriday(d0):
        if (d0.weekday() < 4):
            friday = d0+timedelta(4-d0.weekday())
        else:
            friday = d0-timedelta(d0.weekday()-4)

        # Add correction for early Tangaroa (before 19th June)
        eighteen_june = datetime(d0.year, 6, 18)
        if friday < eighteen_june:
            friday += timedelta(days=7)

        return friday

    # This function takes input year (integer) and returns the Matariki date
    @staticmethod
    def getMatariki(year):
        eighteen_june = datetime(int(year), 6, 18)

        stos = Matariki.getSTOS(year)
        new_moons = Matariki.getNewMoons(stos)

        # Find the first day of the Tangaroa period (23rd day since new moon, first day included)
        for i in range(len(new_moons)):
            tangaroa = datetime.strptime(
                stos[new_moons[i]][0], '%Y-%b-%d') + timedelta(days=22)
            if tangaroa >= eighteen_june:
                return Matariki.getClosestFriday(tangaroa).strftime('%Y-%m-%d')

        


def main():
    validYear = False
    while not validYear:
        try:
            year = int(input("Year: "))
            if year < 1000 or year > 9999:
                print(
                    'This calculator only works for years between 1000 and 9999 inclusive.')
            else:
                validYear = True
        except:
            print('Year has to be a valid integer.')

    print(Matariki.getMatariki(year))


if __name__ == "__main__":
    main()
