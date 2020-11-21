s,p=list(map(int,input().split()))

d=s**2-4*p

from math import sqrt

r=int(sqrt(d))

for i in range(3):
    rr=r+i-1
    if d==rr**2:
        print("Yes")
        exit()
print("No")

