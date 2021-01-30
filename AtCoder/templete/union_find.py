

# UnionFind
par=[i for i in range(n)]
# roはグループの大きさ
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

