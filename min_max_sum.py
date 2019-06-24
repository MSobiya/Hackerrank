#https://www.hackerrank.com/challenges/mini-max-sum/problem
def maxMinSum(a):
	x=sum(a)
	print (x-max(a)),(x-min(a))
		
a = map(int, raw_input().strip().split(' '))
maxMinSum(a)

#Output:
#1 2 3 4 5                   
#10 14
