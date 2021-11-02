import math
import os
import random
import re
import sys

def gradingStudents(grades):
#creamos una nueva lista que almacena las notas finales ya redondeadas si fuese necesario
    new_grades=[]
    for grade in grades:
    #si la calificación es menos a 40 no se redondea por ser una nota suspensa
        if(grade<40):
            new_grades.append(grade)
        else:
            #si el resto es mayor de tres, entonces si se podra redondear
            if(grade%5 >=3):
                #para guardar la neuva nota, la ponemos en la lista nueva
                grade_redondeada=grade+(grade%5-1)
                new_grades.append(grade_redondeada)
            else:
                #si el resto no coincide con las indicaciones, entonces no redondeamos la nota
                #y la añadimos a la lista sin modificarla
                new_grades.append(grade)

    return new_grades




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):

    grades_item = int(input().strip())
    grades.append(grades_item)
result = gradingStudents(grades)
fptr.write('\n'.join(map(str, result)))
fptr.write('\n')
fptr.close()