#https://www.hackerrank.com/challenges/migratory-birds/problem

input()
res = [0]*6
for t in map(int,input().strip().split()):
    res[t] += 1
print(res.index(max(res)))
