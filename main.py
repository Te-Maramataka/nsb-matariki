from datetime import date, datetime, timedelta

d0 = datetime.fromisoformat('2022-06-21T02:18:00')


# 1 lunation = 29.530 588 235 days
# TODO: Convert this number down to the nearest millisecond\

dt = timedelta(days=29, hours=12, minutes=44, seconds=2, milliseconds=82.3504)

# TODO: find the number of lunations to be added
# NOTE: Every 3 years, an extra lunation is added (2023 is leap)

# Model doesn't work for: 2028,

n = 13+12+12+13+12+12+13+12

# Finding the next Tangaroa
d1 = n*dt + d0

# Find the closest Friday
print(getNextFriday(d1))
# TODO: add getNextFriday function

# print(d0)
# print(getClosestFriday(d1))