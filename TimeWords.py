#https://www.hackerrank.com/challenges/the-time-in-words/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    hours = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]

    minutes = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if(m == 0):
        return (hours[h-1] + " o' clock")
    elif(m == 1):
        return ("one minute past " + hours[h-1])
    elif(m == 15):
        return ("quarter past " + hours[h-1])
    elif(m > 1 and m < 30):
        return (minutes[m-1] + " minutes past " + hours[h-1])
    elif(m == 30):
        return ("half past " + hours[h-1])
    elif(m == 45):
        return ("quarter to " + hours[h])
    elif(m > 30 and m <= 59):
        return (minutes[60-m-1] + " minutes to " + hours[h])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
