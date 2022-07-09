from datetime import date, datetime, timedelta

from closestFriday import getClosestFriday

# Constants
d0 = datetime.fromisoformat('2022-06-21T02:18:00')
yearTime = timedelta(days=354)
leapMonthTime = timedelta(days=33)

# Input goes here

year = 2023

# NOTE: Every 3 years, an extra month with 33 days is added (2023 is leap)


d1 = d0 + 2*yearTime + 1*leapMonthTime

# Find the closest Friday
print(d1)

# print(d0)
# print(getClosestFriday(d1))
