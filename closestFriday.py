from datetime import timedelta

# TODO: Add documentation.


def getClosestFriday(d0):
    # If it's a saturday, the previous Friday is chosen instead of the next
    if (d0.weekday() < 4):
        return d0+timedelta(4-d0.weekday())
    else:
        return d0-timedelta(d0.weekday()-4)
