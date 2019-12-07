n=int(input())
line=[[0,0] for _ in range(n-1)]
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    line[i][0]=a
    line[i][1]=b
dot=[]*n
color=[]
for i in range(n-1):
    used=set(dot[line[i][0]]+dot[line[i][1]])
    used.sort()
    end=False
    while end:

#途中でめんどくさくなってやめた