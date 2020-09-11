n,m=list(map(int,input().split()))
par=[i for i in range(n)]
ro=dict()

for i in range(n):
    ro[i]=1
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
        ro[ry]+=ro[rx]
        ro[rx]=0

for i in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    unite(a,b)

print(max(ro.values()))





