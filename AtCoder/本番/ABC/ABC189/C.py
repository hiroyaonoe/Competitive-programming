n=int(input())
a= list(map(int,input().split()))
ans=0
for l in range(n):
    mi=a[l]
    for r in range(l,n):
        mi=min(mi,a[r])
        tmp=mi*(r-l+1)
        ans=max(ans,tmp)
print(ans)