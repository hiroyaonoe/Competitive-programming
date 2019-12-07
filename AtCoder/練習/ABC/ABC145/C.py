from itertools import combinations as combi
from math import sqrt
n=int(input())
x=[]
y=[]
sum=0
for i in range(n):
    xx,yy=map(int,input().split())
    x.append(xx)
    y.append(yy)
for a,b in combi(range(n),2):
    dx=x[a]-x[b]
    dy=y[a]-y[b]
    d=sqrt(dx**2+dy**2)
    sum+=d
ans=sum*2/n
print(ans)
