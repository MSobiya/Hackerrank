#https://www.hackerrank.com/challenges/magic-square-forming/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    #n = [s[i][j] for i in range(3) for j in range(3)] 
    n = []
    for i in range(len(s)):
        n.extend(s[i])
    all_n = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

    allsum = []
    for l in all_n:
        allsum.append(sum([abs(n[i]-l[i]) for i in range(9)]))
    x = min(allsum)
    return(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
