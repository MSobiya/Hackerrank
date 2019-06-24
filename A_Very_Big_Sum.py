#Link of question
#https://www.hackerrank.com/challenges/a-very-big-sum/
def aVeryBigSum(ar):
    result=0
    for i in ar:
        result+=i
    return result

ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(ar)
print(result)
