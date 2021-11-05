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
    if n!=7:
        #en todos los casos en los que las piedras no son 7, simepre gana el primer jugador
        return print('ganador: P1')

    else:
        # en cualquiera de las tres posibilidades, el jugador que gana es el dos
        return print('ganador: P2')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    result = gameOfStones(n)
    fptr.write(result + '\n')
    fptr.close()