#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
def staircase(n):
    #generamos dos bucles for para hacer la escalera
    for tamaño in range (n):
        #incrementamos el rango en una unidad para poder dar forma a la escalera
        #y separamos por saltos de línea las distintas alturas de la escalera
        for altura in range (tamaño+1):
        print("#", end="")
    print("")

if __name__ == '__main__':
n = int(input().strip())
staircase(n)