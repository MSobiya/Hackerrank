#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
#!/bin/python

import sys

n = int(raw_input().strip())
score = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))

distinct = sorted(set(score),reverse=True)
j = len(distinct)
for i in alice:
    while(j > 0 and i >= distinct[j-1]):
        j-=1
    print j+1
