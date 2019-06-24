#https://www.hackerrank.com/challenges/time-conversion/problem
from time import strptime, strftime
print strftime("%H:%M:%S", strptime(raw_input(), "%I:%M:%S%p"))
#Output
#07:05:45PM
#19:05:45
