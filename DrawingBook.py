#https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    near = min(p , abs(n-p))
    if(near == abs(n-p) and n%2 == 0 and abs(n-p) != p):
        near = near + 1
        
    return(near // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
