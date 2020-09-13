n=int(input())
p=[]
m=[]

for i in range(n):
    x,y=list(map(int,input().split()))
    p.append(x+y)
    m.append(x-y)

minp=min(p)
maxp=max(p)
minm=min(m)
maxm=max(m)

ans=[maxp-minp,maxm-minm,minm,maxm,minp-maxp]
print(max(ans))