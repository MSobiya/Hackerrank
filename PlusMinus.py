
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
neg=0.0
pos=0.0
zer=0.0
for i in arr:
    if i<0:
        neg+=1
    elif i>0:
        pos+=1
    else:
        zer+=1
print (pos/n)
print (neg/n)
print (zer/n)
