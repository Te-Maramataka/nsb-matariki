from datetime import date, timedelta, datetime

# TODO: Tangaroa is an interval. Need to find the closest Friday near that interval


def getClosestFriday(d0):
    if (d0.weekday() < 4):
        return d0+timedelta(4-d0.weekday())
    else:
        return d0-timedelta(d0.weekday()-4)
