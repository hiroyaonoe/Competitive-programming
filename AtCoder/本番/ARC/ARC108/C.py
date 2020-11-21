n,m=list(map(int,input().split()))
g=[[] for i in range(n)]
# c=[]
l=[set() for i in range(n)]
ans=[-1 for i in range(n)]

for i in range(m):
    u,v,cc =list(map(int,input().split()))
    u-=1
    v-=1
    # c.append(cc)
    g[v].append([u,cc])
    g[u].append([v,cc])
    l[u].add(cc)
    l[v].add(cc)

s=[0]
while len(s)>0:
    v=s.popleft()
    for u,c in g[v]:
        if len()

