from copy import deepcopy
from collections import deque

h,w=map(int,input().split())
s=[]
for i in range(h):
    ssss=input().split()
    s.append(ss)

dxdy=[[-1,0],[0,-1],[1,0],[0,1]]

# mind=[[10**10 for j in range(w)] for i in range(h)]
ans=0

def search(x,y,map,d):
    global mind
    mind[x][y]=min(d,mind[x][y])
    map[x][y]="#"
    end=True
    for dx,dy in dxdy:
        nx=x+dx
        ny=y+dy
        if (0<=nx<h)&(0<=ny<w)&(map[nx][ny]=="."):
            end=False
            nd=d+1
            search(nx,ny,map,nd)
    if end:
        # mind[nx][ny]=min(mind[nx][ny],d)

anslist=[]
for i in range(h):
    for j in range(w):
        for ii in range(h):
            for jj in range(w):
                map=deepcopy(s)
                mind = [[10 ** 10 for j in range(w)] for i in range(h)]
                search(i,j,map,0)
                anslist.append(max(mind))

print(max(anslist))





