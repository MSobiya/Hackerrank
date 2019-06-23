#!/bin/python

import sys
from collections import defaultdict

def Occurrence(a):
    temp=a[0]
    c=defaultdict(lambda:0)
    i=0
    while(i<len(a)):
        if(a[i]==temp):
            c[a[i]]+=1
            i+=1
        else:
            temp=a[i]
    return c
            
def subsequenceAgain(s, k):
    t=[]
    c=Occurrence(s)
    for i in s:
        if c[i]>=k:
            t.append(i)
    t=''.join(t)
    return t
if __name__ == "__main__":
    s = raw_input().strip()
    k = int(raw_input().strip())
    result = subsequenceAgain(s, k)
    print result
