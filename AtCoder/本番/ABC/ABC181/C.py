n=int(input())
x=[]
y=[]

for i in range(n):
    xx,yy=list(map(int,input().split()))
    x.append(xx)
    y.append(yy)

from itertools import combinations as cmb

comb=cmb(range(n),3)

for i,j,k in comb:
    x1,x2,x3=x[i],x[j],x[k]
    y1,y2,y3=y[i],y[j],y[k]
    if (y3-y1)*(x2-x1)==(x3-x1)*(y2-y1):
        print("Yes")
        exit()

print("No")