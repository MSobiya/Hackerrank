#!/bin/python
#https://www.hackerrank.com/contests/codeagon/challenges/ugly-or-beautiful/submissions/code/1303034410/
import sys
def betweeen_n(a,b):
    for i in a:
        if i not in b:
            return True
    return False

def uglyOrBeautiful(a,b):
    if sorted(a)==a or len(set(a)) != len(a) or betweeen_n(a,b):
        return "Ugly"
    return "Beautiful"
if __name__ == "__main__":
    q = int(raw_input())
    for a0 in xrange(q):
        n = int(raw_input())
        a = map(int, raw_input().strip().split(' '))
        b=range(n+1)
        result = uglyOrBeautiful(a,b)
        print result

