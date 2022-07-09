from datetime import datetime, timedelta
import yearToLunation
import closestFriday

# Base Lunation Number 1 = '1923-01-17 02:41' (Brown Lunation Number)
BASE_LUNATION_BLN = datetime(1923, 1, 17, 2, 41)

# 1 Lunation Constant
dt = timedelta(days=29, hours=12, minutes=44, seconds=2, milliseconds=82.3504)
# Because above is an average of a lunation, that could explain why >2300 doesn't work


def getMatariki(year):
    lunation = yearToLunation.getLunation(year)

    # d - date of the first tangaroa period
    d = (lunation - 1)*dt + BASE_LUNATION_BLN + 0.75*dt

    # TODO: This algorithm which keeps on going to the next lunation until >19-06 is brute forcing. Find a better way.
    while (d.month == 6 and d.day <= 19) or (d.month < 6):
        lunation += 1
        d = (lunation - 1)*dt + BASE_LUNATION_BLN + 0.75*dt

    return closestFriday.getClosestFriday(d)

# TODO: Doesn't work for >2200 Investigate. yearToLunation() is not working.


print(getMatariki(2200))
