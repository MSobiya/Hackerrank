#https://www.hackerrank.com/challenges/python-division/problem

class Division:
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
    
    def divide(self):
        return (self.a // self.b, self.a / self.b)

res = Division()
integer, floating = res.divide()
print(integer)
print(floating)
