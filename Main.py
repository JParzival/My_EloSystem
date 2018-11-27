import Imp_Calculator
from Imp_Calculator import higherEloLoses, higherEloWins, lowerEloLoses, lowerEloWins, draw_both
# My personal implementation of an Elo System.

player1 = {'code':1, 'name': "Player One", 'elo': 2000.0}
player2 = {'code':2, 'name': "Player Two", 'elo': 2500.0}

# The players are gonna compete

match = [player1, player2]
e_score_p1 = match[0]['elo'] / (match[0]['elo'] + match[1]['elo'])
e_score_p2 = match[1]['elo'] / (match[1]['elo'] + match[0]['elo'])

# Now I am going to calculate a random result of the clash, and a random score

import random

result = random.uniform(0,1)


def calculateEloP1(player):

    # This means that the Player One has won against the player two

    score = random.uniform(0.5, 1)

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']

    diff1 = (1-score) - e_score_p1
    diff2 = score - e_score_p2

    if player['code'] == player1:   # The player with higher elo is P1
        newEloP1 = lastEloP1 + higherEloWins(diff1) * diff1
        newEloP2 = lastEloP2 + lowerEloLoses(diff2) * diff2
    else:
        k1 = lowerEloWins(diff1)
        newEloP1 = lastEloP1 + k1 * diff1  
        k2 = lowerEloLoses(diff2)    
        newEloP2 = lastEloP2 + k2 * diff2

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


def calculateEloP2(player):

    # This means that the player 2 has won against the player one

    score = random.uniform(0.5, 1)

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']

    diff1 = (1-score) - e_score_p1
    diff2 = score - e_score_p2

    if player['code'] == player1:   # The player with higher elo is P1
        newEloP1 = lastEloP1 + higherEloLoses(diff1) * diff1      
        newEloP2 = lastEloP2 + lowerEloWins(diff2) * diff2
    else:
        k1 = lowerEloLoses(diff1)
        newEloP1 = lastEloP1 + k1 * diff1
        k2 = higherEloWins(diff2)      
        newEloP2 = lastEloP2 + k2 * diff2

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


def draw():
    # In case there is a draw
    # There's no need of score, but, the draw affects differently to both players depending on their elo

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']

    newEloP1 = lastEloP1 + draw_both(0.5 - e_score_p1) * (0.5 - e_score_p1)
    newEloP2 = lastEloP2 + draw_both(0.5 - e_score_p2) * (0.5 - e_score_p2)

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


if e_score_p2 > 0.5:         # The second player has greater elo

    if result > e_score_p2:
        # P1 has won
        calculateEloP1(player2)
    if result == e_score_p2:
        draw()
    if result < e_score_p2:
        calculateEloP2(player2)

else:                        # The first player has greater elo

    if result > e_score_p1:
        # P2 has won
        calculateEloP2(player1)
    if result == e_score_p1:
        draw()
    if result < e_score_p1:
        calculateEloP1(player1)

# Now they have their new elo!