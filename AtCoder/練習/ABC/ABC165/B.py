from math import floor
x=int(input())
a=100
i=0
while a<x:
    a*=1.01
    a=floor(a)
    i+=1
print(i)

