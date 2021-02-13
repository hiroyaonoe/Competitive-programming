import sys
sys.setrecursionlimit(2000000)
n = int(input())
par = list(map(int,("0 "+input()).split()))
par = [i-1 for i in par]

chi = [[] for i in range(n)]

for i,p in enumerate(par):
    if i == 0:continue
    chi[p].append(i)

memo=[[True,0,0] for i in range(n)]

def dfs(i):
    ps = True
    px = 0
    py = 1
    if chi[i]:
        mm=[]
        for c in chi[i]:
            dfs(c)
            mm.append(memo[c])


            cs,cx,cy=memo[c]
            ps = not (ps ^ cs)
            if cs:

            px += cx
            py += cy
        ps = not ps
    memo[i] = [ps, px, py]

dfs(0)
print(max(memo[0][1], memo[0][2]))

# que=deque()
# que.append(0)
# size=[0 for i in range(n)]
# def dfs(i):
#     ad=0
#     for c in chi[i]:
#         ad+=dfs[c]+1
#     size[i]=ad
#
# ans=0
# ta=True
# now=0
# coin=[True for i in range(n)]
# while True:
#     if coin[now]:
#         coin[now]=False
#         if ta:
#             ans+=1
#     else:
#         mi=INF
#         nex=-1
#         for i in chi[now]:
#             if coin[i] and size[i]<mi:
#                 nex=i
#         if nex==-1:
#             if par[now]==-1:
#                 print(ans)
#                 exit()
#             else:
#                 now=par[now]
#         else:
#             now=nex
#     ta = not ta
