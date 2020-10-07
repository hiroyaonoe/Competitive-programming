n,k=list(map(int,input().split()))

a=[]
for i in range(n):
    aa=int(input())
    a.append(aa)

dp=[1 for i in range(n)]
ans=1
from collections import defaultdict
m=defaultdict(list)
m[1]=[0]
for i in range(1,n):
    aa=a[i]
    q=ans
    ok=True
    while q>0:
        for j in m[q]:
            if abs(a[j]-aa)<=k:
                dp[i]=q+1
                m[q+1].append(i)
                ans=q+1
                ok=False
                break
        if not ok:break
        q-=1
    if ok:
        m[1].append(i)

print(max(dp))


