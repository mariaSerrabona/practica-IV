#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#
def gameOfStones(n):
    if n==1:
        #ningún jugador puede realizar ningun movimiento:
        print('ningún jugador ha ganado')
    elif n==2:
        #p1 tira las dos piedras
        print('ganador: P1')
    elif n==3:
        #p1 tira las dos piedras y deja uno en el tablero, ganando el juego
        print('ganador: P1')
    elif n==4:
        #p1 tira las tres piedras y deja uno en el tablero, ganando el juego
        print('ganador: P1')
    elif n==5:
        #p1 tira todas las piedras del tablero
        print('ganador: P1')
    elif n==6:
        #p1 tira todas las piedras del tablero menos ujna, ganando así la partida
        print('ganador: P1')
    elif n==7:
        # en cualquiera de las tres posibilidades, el jugadoe que gana es el dos
        print('ganador: P2')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
result = gameOfStones(n)
    fptr.write(result + '\n')
fptr.close()