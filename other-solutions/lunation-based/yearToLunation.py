from math import floor

CONST_LUNATION_2023 = 1243

# TODO: Add documentation.

# TODO: For years>2300. The lunation number this function returns is for the year previous. WHY??


def getLunation(year):
    mod = (year-2023) % 3  # remainder lunar months
    cycles = floor((year-2023)/3)  # a complete cycle = 12+12+13
    return mod*12 + cycles*37 + CONST_LUNATION_2023

# print(getLunation(2201))
