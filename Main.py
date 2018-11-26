# My personal implementation of an Elo System.

player1 = {'name': "Player One", 'elo': 2000}
player2 = {'name': "Player Two", 'elo': 2500}

# The players are gonna compete

match = [player1, player2]
e_score_p1 = match[0]['elo'] / (match[0]['elo'] + match[1]['elo'])
e_score_p2 = match[1]['elo'] / (match[1]['elo'] + match[0]['elo'])

# Now I am going to calculate a random result of the clash, and a random score

import random

result = random.uniform(0,1)


def calculateEloP1():

    # This means that the Player One has won against the player two

    score = random.uniform(0.5, 1)   # 0.5 winning very close, 1 means maximum difference

    lastEloP1 = match[0]['elo']
    newEloP1 = lastEloP1 + imp * (score - e_score_p1)

    lastEloP2 = match[0]['elo']
    newEloP2 = lastEloP2 + imp * ((1-score) - e_score_p2)

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


def calculateEloP2():

    # This means that the player 2 has won against the player one

    score = random.uniform(0.5, 1)

    lastEloP1 = match[0]['elo']
    newEloP1 = lastEloP1 + imp * ((1-score) - e_score_p1)

    lastEloP2 = match[0]['elo']
    newEloP2 = lastEloP2 + imp * (score - e_score_p2)

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


def draw():
    # In case there is a draw
    # There's no need of score, but, the draw affects differently to both players depending on their elo

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']

    newEloP1 = lastEloP1 + imp * (0.5 - e_score_p1)
    newEloP2 = lastEloP2 + imp * (0.5 - e_score_p2)

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


if e_score_p2 > 0.5:         # The second player has greater elo

    if result > e_score_p2:
        # P1 has won
        calculateEloP1()
    if result == e_score_p2:
        draw()
    if result < e_score_p2:
        calculateEloP2()

else:                        # The first player has greater elo

    if result > e_score_p1:
        # P2 has won
        calculateEloP2()
    if result == e_score_p1:
        draw()
    if result < e_score_p1:
        calculateEloP1()

# Now they have their new elo!



