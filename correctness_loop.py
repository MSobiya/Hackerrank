#https://www.hackerrank.com/challenges/correctness-invariant/problem

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    print " ".join(map(str,l))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)

