a,b,c=map(int,input().split())

from math import sqrt

if ((c-a-b)**2>4*a*b)&(c-a-b>=0):
    print("Yes")
else:
    print("No")