##### In this case, there are gonna be teams ######

import functions as f

print("Datos del equipo 1: ")
print(" ")
print("Introduce el elo del jugador 1: ")
elo1 = float(input())
print("Introduce el elo del jugador 2: ")
elo2 = float(input())
print("Introduce el elo del jugador 3: ")
elo3 = float(input())

team1 = {'p1': elo1, 'p2': elo2, 'p3': elo3}

print("Datos del equipo 2: ")
print(" ")
print("Introduce el elo del jugador 4: ")
elo4 = float(input())
print("Introduce el elo del jugador 5: ")
elo5 = float(input())
print("Introduce el elo del jugador 6: ")
elo6 = float(input())

team2 = {'p4': elo4, 'p5': elo5, 'p6': elo6}

# The first thing I've got to do is to calculate the mean of every team

import statistics as s

mediaT1 = s.mean([team1['p1'], team1['p2'], team1['p3']])
mediaT2 = s.mean([team2['p4'], team2['p5'], team2['p6']])

e_score_p1 = mediaT1 / (mediaT1 + mediaT2)
e_score_p2 = mediaT2 / (mediaT1 + mediaT2)

# Now that the means are calculated, we have to introduce the results.

print("Introduzca el resultado (mirar la e_score y determinar): ")
result = float(input())
print("Introduzca el marcador (0.5 - 1): ")
marcador = float(input())

if e_score_p2 > 0.5:         # The second team has greater elo

    if result > e_score_p2:
        # T1 has won
        f.team1Won(team1, team2)
    if result == e_score_p2:
        f.draw(team1, team2)
    if result < e_score_p2:
        f.team2Won(team1, team2)

else:                        # The first team has greater elo

    if result > e_score_p1:
        # T2 has won
        f.team2Won(team1, team2)
    if result == e_score_p1:
        f.draw(team1, team2)
    if result < e_score_p1:
        f.team1Won(team1, team2)

