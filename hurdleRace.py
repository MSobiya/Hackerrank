#https://www.hackerrank.com/challenges/the-hurdle-race/problem

#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))

m = max(height)
if(m < k):
    print 0
else:
    print m-k
