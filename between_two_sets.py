#https://www.hackerrank.com/challenges/between-two-sets?h_r=internal-search

def getX(a,b):
	res=0
	for i in range(max(a), min(b) +1):
		if all(i % arr == 0 for arr in a) and all(brr % i == 0 for brr in b):
			res += 1
	return res

n,m = raw_input().strip().split(' ')
n,m =int(n),int(m)
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
res=getX(a,b)
print res
