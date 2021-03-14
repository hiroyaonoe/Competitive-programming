n=int(input())
f = list(map(lambda x:int(x)-1,input().split()))
mod = 998244353
gs = 0
memo = [False for i in range(n)]

for i in range(n):
    if memo[i]:
        continue
    memo[i] = True
    group = [i]
    inmemo = [False for i in range(n)]
    inmemo[i]=True
    j = f[i]
    ok = True
    while i != j:
        if memo[j] or inmemo[j]:
            ok = False
            break
        inmemo[j] = True
        group.append(j)
        j = f[j]
    if ok:
        gs += 1
        for j in group:
            memo[j] = True


print((pow(2,gs,mod)-1)%mod)



# # UnionFind
# par=[i for i in range(n)]
# # roはグループの大きさ
# # ro=dict()
# #
# # for i in range(n):
# #     ro[i]=1
#
# def root(i):
#     if par[i]==i:
#         return i
#     else:
#         a=root(par[i])
#         par[i]=a
#         return a
#
# def unite(x,y):
#     rx=root(x)
#     ry=root(y)
#     if rx!=ry:
#         par[rx]=ry
#         # ro[ry]+=ro[rx]
#         # ro[rx]=0
#
# for i in range(n):
#     unite(i+1,f[i])
#
# for i in range(n):
#
