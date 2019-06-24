#https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import sys

def solve(n, s, d, m):
    if m > d:
        return 0
    if m == 1:
        if(s[0] == d):
            return 1
        return 0
    
    res = 0
    for i in range(n):
        add = 0
        if m+i > n:
            return res
        
        for j in range(i,m+i):
            if s[j] > d or add > d:
                break
            add = add+s[j]
        if (add == d):
                res += 1
    return res

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
