#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

def breakingRecords(score):
    high, low = score[0], score[0]
    lCount, hCount = 0, 0
    for s in scores:
        if(s > high):
            high = s
            hCount += 1
        if(s < low):
            low = s
            lCount += 1
    return hCount, lCount
    
n = int(input())
scores = input().split(' ')
scores = [int(x) for x in scores]
result = breakingRecords(scores)
print(result[0], result[1])
