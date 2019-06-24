#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthdayCakeCandles(n, a):
	m=max(a)
	return a.count(m)

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, a)
print(result)

#output:
#4
#3 2 1 3
#
#
#2
