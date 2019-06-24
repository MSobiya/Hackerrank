#https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while (j >= 0 and a[j] > key):
            a[j+1] = a[j]
            j = j-1
        a[j+1]=key
        print ' '.join(map(str, a))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
