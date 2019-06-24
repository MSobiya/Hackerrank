#https://www.hackerrank.com/challenges/sock-merchant/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    tempar = list(set(ar))
    pair = 0
    for i in tempar:
        for j in range(n):
            if(ar.count(i) >= 2):
                temp = i
                pair += 1
                ar.remove(i)
                ar.remove(i)
            else:
                break
    return pair
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
