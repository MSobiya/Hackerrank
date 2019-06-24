# https://www.hackerrank.com/challenges/staircase

#!/bin/python
def staircase(n):
    for i in range(1, n + 1):
        print ' ' * (n - i) + '#' * i

n = int(raw_input().strip())
staircase(n)
