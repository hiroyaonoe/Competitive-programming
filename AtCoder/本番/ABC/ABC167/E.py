n,m,k=map(int,input().split())

dp=[m]
mod=998244353
for i in range(n):
    if i==0:continue

    if i<=k:
        ans=m**(i+1)%mod
        dp.append(ans)
    else:
        for kk in range(k):



