# My personal implementation of an Elo System.
import Imp_Calculator
from Imp_Calculator import higherEloLoses, higherEloWins, lowerEloLoses, lowerEloWins, draw_both

###### MAIN PROGRAM PART 1 ######

print("Introduce el elo del jugador 1: ")
player1Elo = float(input())
print("Introduce el elo del jugador 2: ")
player2Elo = float(input())

player1 = {'code': 1, 'name': "Player One", 'elo': player1Elo}
player2 = {'code': 2, 'name': "Player Two", 'elo': player2Elo}

# The players are gonna compete. I calculate the expected score

match = [player1, player2]
e_score_p1 = match[0]['elo'] / (match[0]['elo'] + match[1]['elo'])
e_score_p2 = match[1]['elo'] / (match[1]['elo'] + match[0]['elo'])

# More inputs

print("Introduce el resultado final: ")
result = float(input())

print("Introduce el marcador (0.5 - 1): ")
score = float(input())

##### FUNCTIONS #####

def player1Won():

    # This means that the Player One has won against the player two

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']

    diff1 = score - e_score_p1	     # Comparison to expected
    diff2 = -diff1

    if lastEloP1 > lastEloP2:   # The player with higher elo is P1
        K_P1 = higherEloWins(diff1)
        K_P2 = lowerEloLoses(diff2)
        newEloP1 = lastEloP1 + K_P1 * diff1
        newEloP2 = lastEloP2 + K_P2 * diff2
    else:                           # The player with higher elo is P2
        k1 = lowerEloWins(diff1)
        newEloP1 = lastEloP1 + k1 * diff1  
        k2 = higherEloLoses(diff2)    
        newEloP2 = lastEloP2 + k2 * diff2

    match[0]['elo'] = newEloP1
    match[1]['elo'] = newEloP2


def player2Won():

    # This means that the player 2 has won against the player one

    lastEloP1 = match[0]['elo']
    lastEloP2 = match[1]['elo']


    diff2 = (1-score) - e_score_p2
    diff1 = -diff2

    if lastEloP1 > lastEloP2:   # The player with higher elo is P1
        K_P1 = higherEloLoses(diff1)
        newEloP1 = lastEloP1 + K_P1 * diff1 
        K_P2 = lowerEloWins(diff2)     
        newEloP2 = lastEloP2 + K_P2 * diff2
    else:                           # The player with higher elo is P2
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

###### MAIN PROGRAM PART 2 ######

if e_score_p2 > 0.5:         # The second player has greater elo

    if result > e_score_p2:
        # P1 has won
        player1Won()
    if result == e_score_p2:
        draw()
    if result < e_score_p2:
        player2Won()

else:                        # The first player has greater elo

    if result > e_score_p1:
        # P2 has won
        player2Won()
    if result == e_score_p1:
        draw()
    if result < e_score_p1:
        player1Won()

# Now they have their new elo!

print(match[0]['elo'])
print(match[1]['elo'])