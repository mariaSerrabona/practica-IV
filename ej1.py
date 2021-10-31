import numpy as np
import os
import random
import re
import sys

def simpleArraySum(ar):

    np.array(ar)
    resultado=np.sum(ar)
    return resultado

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    array_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
fptr.write(str(result) + '\n')
fptr.close()

