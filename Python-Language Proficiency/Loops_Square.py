#https://www.hackerrank.com/challenges/python-loops/problem
class Square:
    def squares(self, n):
        for i in range(n):
            print(i ** 2)

sq = Square()
sq.squares(int(input()))
