# This part calculates the importance of the match depending on the differences of levels.
# Besides, it has 4 ecuations that make the difference.

import math as m

def higherEloWins(diff):

    result = (1/10)*abs(diff) + 3
    return result

def lowerEloWins(diff):     # Al revés?

    result = 70/(0.0002*(abs(diff) + 700) ) - 50
    return result

def higherEloLoses(diff):    # Al revés?

    result = (1/10)*abs(diff) + 3
    return result

def lowerEloLoses(diff):

    result = 70/(0.0002*(abs(diff) + 700) ) -50
    return result

def draw_both(diff):        # Al revés?

    result = (1/10)*abs(diff) + 3
    return result