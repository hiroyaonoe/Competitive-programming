# 解説AC

from collections import defaultdict

n=int(input())
if n==1:
    print(1)
    exit()
x=[]
y=[]
for i in range(n):
    xx,yy=list(map(int,input().split()))
    x.append(xx)
    y.append(yy)

dif=defaultdict(int)

for i in range(n):
    for j in range(n):
        if i==j:continue
        p=x[j]-x[i]
        q=y[j]-y[i]
        dif[(p,q)]+=1

dif=sorted(dif.items(),key=lambda x:x[1],reverse=True)
ans=n-dif[0][1]

print(ans)




