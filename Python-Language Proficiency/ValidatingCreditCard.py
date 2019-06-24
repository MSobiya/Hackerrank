#https://www.hackerrank.com/challenges/validating-credit-card-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
def isOnlyDigit(c):
    for _ in c:
        if(not(_.isdigit()) and _ != '-'):
            return False
    return True


def group(c):
    if('-' in c):
        x = c.split('-')
        for _ in x:
            if(len(_) != 4):
                return False
    return True


def consecutive(c):
    c = c.replace("-", "")
    for n in range(len(c)-3):
        if(c[n] == c[n+1] == c[n+2] == c[n+3]):
            return False
            
    return True
            



def verify(c):
    if((c[0] == '4' or c[0] == '5' or c[0] == '6') and (len(c) == 16 or len(c) == 19) and (isOnlyDigit(c) and group(c)) and (consecutive(c))):
        print("Valid")
    else:
        print("Invalid")


n = int(input())
for i in range(n):
    verify(input())
