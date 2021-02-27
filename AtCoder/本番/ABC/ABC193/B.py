n=int(input())

ans=[]
for i in range(n):
    a,p,x = list(map(int,input().split()))
    if x-a>0:
        ans.append(p)

if ans:
    print(min(ans))
else:
    print(-1)