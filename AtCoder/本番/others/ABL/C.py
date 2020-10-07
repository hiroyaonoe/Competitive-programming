n,m=list(map(int,input().split()))

par=[i for i in range(n)]
# ro=dict()
#
# for i in range(n):
#     ro[i]=1

def root(i):
    if par[i]==i:
        return i
    else:
        a=root(par[i])
        par[i]=a
        return a

def unite(x,y):
    rx=root(x)
    ry=root(y)
    if rx!=ry:
        par[rx]=ry
        # ro[ry]+=ro[rx]
        # ro[rx]=0

for i in range(m):
    a,b=list(map(int,input().split()))
    unite(a-1,b-1)

ans=set()

for i in range(n):
    rt=root(i)
    ans.add(rt)

# from collections import Counter as cnt
#
# bb=ro.values()
# ans=dict(cnt(ro.values()))

print(len(ans)-1)