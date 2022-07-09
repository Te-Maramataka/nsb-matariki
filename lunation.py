from datetime import date, datetime, timedelta
import yearToLunation
import closestFriday

# TODO: REMOVE JULIAN DATE NAME
# getJulianDate(new Date('1923-01-17 02:41'))
BASE_LUNATION_JULIAN_DATE = datetime(1923, 1, 17, 2, 41)

# 1 Lunation Constant
dt = timedelta(days=29, hours=12, minutes=44, seconds=2, milliseconds=82.3504)

# Exceptions: 2028, 2031, 2033, 2034
# What is going on?


# def getMatariki(year):
#     lunation = yearToLunation.getLunation(year)

#     # d - date of the first tangaroa period
#     d = (lunation - 1)*dt + BASE_LUNATION_JULIAN_DATE + 0.75*dt

#     while (d.month == 6 and d.day <= 19) or (d.month < 6):
#         lunation += 1
#         d = (lunation - 1)*dt + BASE_LUNATION_JULIAN_DATE + 0.75*dt

#     return closestFriday.getClosestFriday(d)

year = 2540

lunation = yearToLunation.getLunation(year)

print(lunation)

# d - date of the first tangaroa period
d = (lunation - 1)*dt + BASE_LUNATION_JULIAN_DATE + 0.75*dt
print(d)
print(d.month)


while (d.month == 6 and d.day <= 19) or (d.month < 6):
    lunation += 1
    d = (lunation - 1)*dt + BASE_LUNATION_JULIAN_DATE + 0.75*dt

print(closestFriday.getClosestFriday(d))
