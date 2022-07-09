from datetime import date, datetime, timedelta
from closestFriday import getClosestFriday

d0 = datetime.fromisoformat('2022-06-21T02:18:00')


# 1 lunation = 29.530 588 235 days
# TODO: Convert this number down to the nearest millisecond\

dt = timedelta(days=29, hours=12, minutes=44, seconds=2, milliseconds=82.3504)

# TODO: find the number of lunations to be added
# NOTE: Every 3 years, an extra lunation is added (2023 is leap)

# Model doesn't work for: 2028,

year = 2051

# TODO: make these work for years < 2022


def getThirteens(year):
    if (year == 2022):
        return 0
    else:
        return int((year-2022)/4) + 1


def getTwelves(year):
    thirteens = getThirteens(year)
    return year-2022-thirteens


thirteens = getThirteens(year)
twelves = getTwelves(year)

# Finding the next Tangaroa
d1 = (13*thirteens + 12 * twelves)*dt + d0

# Find the closest Friday
print(d1)
