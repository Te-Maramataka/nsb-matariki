from math import floor

CONST_LUNATION_2023 = 1243

# TODO: Add documentation


def getLunation(year):
    mod = (year-2023) % 3  # remainder
    cycles = floor((year-2023)/3)  # 12+12+13
    return mod*12 + cycles*37 + CONST_LUNATION_2023


print(getLunation(2500))
# hello world
