# This part calculates the importance of the match depending on the differences of levels.
# Besides, it has 4 ecuations that make the difference.

import math as m

def higherEloWins(diff):

    result = 50000/(0.00001*abs(diff) + 50)
    return result

def lowerEloWins(diff):

    result = (1/10)*abs(diff) + 3
    return result

def higherEloLoses(diff):

    result = (1/10)*abs(diff) + 3
    return result

def lowerEloLoses(diff):

    result = 50000/(0.00001*abs(diff) + 50)
    return result

def draw_both(diff):

    result = (1/10)*abs(diff) + 3
    return result