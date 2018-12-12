# This part calculates the importance of the match depending on the differences of levels.
# Besides, it has 4 ecuations that make the difference.

import math as m

def higherEloWins(diff):

    result = 1/(0.1*abs(diff))
    return result

def lowerEloWins(diff):

    result = abs((3/10)*abs(diff) + 2)
    return result

def higherEloLoses(diff):

    result = abs((4/10)*abs(diff) + 1)
    return result

def lowerEloLoses(diff):

    result = 1/(0.1*abs(diff))
    return result

def draw_both(diff):

    result = ((1/2)*diff)
    return result