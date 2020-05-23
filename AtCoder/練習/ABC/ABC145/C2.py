from itertools import permutations as per
from math import sqrt
n=int(input())
x=[]
y=[]
for _ in range(n):
    xx,yy=map(int,input().split())
    x.append(xx)
    y.append(yy)

sum=0
div=0
for jun in per(range(n)):
    div+=1
    for i in range(n-1):
        post=jun[i]
        pre=jun[i+1]

        sum+=sqrt((x[pre]-x[post])**2+(y[pre]-y[post])**2)

print(sum/div)