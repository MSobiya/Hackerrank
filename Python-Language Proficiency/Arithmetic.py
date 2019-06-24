#https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
class Result:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def result(self):
        return (self.a + self.b, self.a - self.b, self.a * self.b)

a = int(input())
b = int(input())
res = Result(a, b)
add, sub, prod = res.result()
print(add)
print(sub)
print(prod)
