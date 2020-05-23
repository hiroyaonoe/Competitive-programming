
n,m=list(map(int,input().split()))

lis=[]
for i in range(m):
    a,b=list(map(int,input().split()))
    lis[a-1].append(b-1)
    lis[b-1].append(a-1)


