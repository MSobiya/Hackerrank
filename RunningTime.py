#https://www.hackerrank.com/challenges/runningtime/problem

def insertionSort(a):
    m=0
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while (j >= 0 and a[j] > key):
            a[j+1] = a[j]
            j = j-1
            m+=1
        a[j+1]=key
    print m

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
