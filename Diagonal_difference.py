#Digonal Differnce
#https://www.hackerrank.com/challenges/diagonal-difference

def Diagonal_Diff(a):
	sum1=0
	sum2=0
	for i in range(n):
		sum1+=a[i][i]
		sum2+=a[i][n-i-1]
		
	return abs(sum1-sum2)

n = int(raw_input().strip())
a=[]
for i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
diff=Diagonal_Diff(a)
print diff
