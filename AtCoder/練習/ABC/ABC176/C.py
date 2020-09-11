n=int(input())

a=list(map(int,input().split()))

ans=0
max=a[0]
for i in range(1,n):
    if max>a[i]:
        ans+=max-a[i]
    else:
        max=a[i]

print(ans)