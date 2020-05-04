n,m=map(int,input().split())
h=list(map(int,input().split()))
mi=[[] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    mi[a].append(h[b])
    mi[b].append(h[a])
ans=0
for i in range(n):
    if len(mi[i])==0:
        ans+=1
    else:
        if h[i]>max(mi[i]):ans+=1

print(ans)