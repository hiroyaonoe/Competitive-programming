h,w=list(map(int,input().split()))
ch,cw=list(map(int,input().split()))
dh,dw=list(map(int,input().split()))

s=[[] for j in range(h)]

for i in range(h):
    s[i]=list(input())

dhw=[(h,w) for h in (-2,-1,0,1,2) for w in (-2,-1,0,1,2)]
dhw-=(0,0)

from collections import deque

que=deque([(ch,cw)])
cost=[[-1 for i in range(w)] for j in range(h)]
cost[ch][cw]=0
while len(que)>0:
    h,w=que.pop()
    nc=cost[h][w]
    for dh,dw in ((0,1),(0,-1),(1,0),(-1,0)):
        nh=h+dh
        nw=w+dw
        if s[nh][nw]==".":
            if cost[nh][nw]==-1:
                cost[nh][nw] = nc
            else:
                cost[nh][nw] = min(nc,cost[nh][nw])



# def search(h,w,memo):
#     new=memo.copy()
#     ok=False
#     for dh,dw in dhw:
#         nh=h+dh
#         nw=w+dw
#         if s[nh][nw]==".":
#             ok=True
#             if (nh,nw) not in new:
#                 new.append((nh,nw))
#                 search(nh,nw,new)
#
# stack=[(ch,cw)]
#
# while len(stack)>0:
