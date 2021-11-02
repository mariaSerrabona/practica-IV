#!/bin/python3
import math
import os
import random
import re
import sys
 #
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #creamos una lista que guarda la distancia a la que han caido las manzanas respecto del árbol
    fallenApples=[]
    applesDistance=0
    #creamos un bucle para guardar todas las distancias
    for apple in apples:
        applesDistance=apple+a
        fallenApples.append(applesDistance)
    #ahora con otra lista, guardamos las manzanas que están dentro del intervalo de la casa
    houseApples=[]
    for apple in fallenApples:
        if apple<15 and apple>5:
            houseApples.append(apple)

    #por último imprimimos por pantalla el tamaño de la lista de las manzanas que caen en la casa
    total_apples=len(houseApples)


    #ahora realizamos el mismo procedimiento pero para las naranjas que estarán a otra distancia de al casa
    fallenOranges=[]
    orangeDistance=0
    for orange in oranges:
        orangeDistance=orange+b
        fallenOranges.append(orangeDistance)

    houseOranges=[]
    for orange in fallenOranges:
        if (orange<30 and orange>15):
            houseOranges.append(orange)

    total_oranges=len(houseOranges)

    return total_oranges , total_apples

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)