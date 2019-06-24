#https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    result = 0
    shared = 5
    #half of five is always 2 therefor for multiplying we directly take 2
    for i in range(n):
        like = shared // 2
        shared = like * 3
        result += like
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
