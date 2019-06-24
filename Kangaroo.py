#https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):

    i = 1
    while(i<10000 and x1 < x2):
        x1 += v1
        x2 += v2
        if(x1==x2):
            return "YES"
        i+=1
    return "NO"


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
