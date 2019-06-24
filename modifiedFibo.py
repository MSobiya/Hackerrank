#https://www.hackerrank.com/challenges/fibonacci-modified/problem
def modifiedFibo(a):
	t1=a[0]
	t2=a[1]
	t3=0
	for i in range(a[2]-2):
		t3=t1+(t2)*(t2)
		t1=t2
		t2=t3
	return t3


a = map(int, raw_input().strip().split(' '))
print(modifiedFibo(a))

