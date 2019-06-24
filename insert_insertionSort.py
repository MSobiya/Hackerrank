#https://www.hackerrank.com/challenges/insertionsort1/problem
def insertionSort(a,m):    
    x=a[m-1]
    flag=0
    for i in range(m-2,-1,-1):
        if(a[i]>x):
            if(i==0):
                a[i+1]=a[i]
                a[i]=x
            else:
                a[i+1]=a[i]
        elif(a[i]<=x):
            a[i+1]=x
            flag=1
            break
        print ' '.join(map(str, a))
    if(flag==1):
        print ' '.join(map(str, a))

m = input()
a = [int(i) for i in raw_input().strip().split()]
insertionSort(a,m)


#Input:
#5
#2 4 6 8 3

#Output:
#2 4 6 8 8 
#2 4 6 6 8 
#2 4 4 6 8 
#2 3 4 6 8 
