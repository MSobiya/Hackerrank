#!/bin/python3
N = int(input())

if((N % 2 != 0) or (N % 2 == 0 and 6 <= N <= 20)):
    print("Weird")
elif(N % 2 == 0 and (2 <= N <= 5 or N > 20)):
    print("Not Weird")

