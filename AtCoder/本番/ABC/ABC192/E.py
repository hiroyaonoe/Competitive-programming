from heapq import *

n,m,x,y = list(map(int,input().split()))
x-=1
y-=1

ab=[[] for i in range(n)]

for i in range(m):
    a,b,t,k = list(map(int,input().split()))
    a -= 1
    b -= 1
    ab[a].append([b,t,k])
    ab[b].append([a,t,k])


INF=1<<60
d=[INF for i in range(n)]
d[x]=0
que=[]
for i in range(n):
    heappush(que, (d[i], i))

while que:
    time, place = heappop(que)
    if place==y:
        break
    for (i,t,k) in ab[place]:
        l=-(-time // k)*k+t
        if d[i]>l:
            d[i]=l
            heappush(que, (d[i], i))

if d[y]==INF:
    print(-1)
else:
    print(d[y])
