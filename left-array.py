#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    dq=deque(arr)
    for i in range(1,d+1):
        from collections import deque

def rotateLeft(d, arr):
    dq = deque(arr)          # create deque once
    
    for i in range(d):
        x = dq.popleft()
        dq.append(x)

    return list(dq)          # return list (expected INTEGER_ARRAY)
        
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
