#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if(ar[i]+ar[j])%k == 0:
                res += 1
    return res

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
