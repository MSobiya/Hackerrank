#https://www.hackerrank.com/challenges/cut-the-sticks/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    result = []
    arr = sorted(arr)

    while(len(arr) > 0):
        i = 0
        print(i)
        print("i", arr[i])
        print("arr",arr)
        count = 0
        x = arr.count(arr[i])
        for j in range(len(arr)):
            arr[j] = arr[j] - arr[i]
            count += 1
        print("iii", x)
        
        for _ in range(x):
            arr.remove(arr[i])

        result.append(count)
    
    return result

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
