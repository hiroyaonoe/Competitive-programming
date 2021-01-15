from collections import deque

n,m=list(map(int,input().split()))

path=[[] for i in range(n)]

for i in range(m):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    path[a].append(b)
    path[b].append(a)

prev=[-1 for i in range(n)]
prev[0]=0
que=deque()
que.append(0)

while len(que)>0:
    pos=que.popleft()
    for i in path[pos]:
        if prev[i]<0:
            que.append(i)
            prev[i]=pos

print("Yes")
for i in prev[1:]:
    print(i+1)