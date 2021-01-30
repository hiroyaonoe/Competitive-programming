# editorial
from collections import deque

n,m= list(map(int,input().split()))
e=[[] for i in range(n)]

for i in range(m):
    a,b= list(map(int,input().split()))
    a-=1
    b-=1
    e[a].append(b)
    e[b].append(a)

k=int(input())
c= list(map(int,input().split()))
c=[i-1 for i in c]

dist=[]

for i in c:
    cost=[1<<30]*n
    que=deque([i])
    cost[i]=0
    while len(que) > 0:
        j = que.popleft()

        for nj in e[j]:
            if cost[nj]>cost[j]+1:
                cost[nj]=cost[j]+1
                que.append(nj)
    dist.append([cost[cc] for cc in c])


dp=[[1<<30] * k for i in range(1<<k)]

for i in range(k):
    dp[1<<i][i]=1

for si in range(1 << k):
    for i in range(k):
        if dp[si][i]==1<<30:continue

        for j in range(k):
            if si & 1 << j:continue
            if dp[si | 1 << j][j] > dp[si][i]+dist[i][j]:
                dp[si | 1 << j][j] = dp[si][i] + dist[i][j]


ans=min(dp[-1])
if ans == 1<<30:
    ans=-1
print(ans)


