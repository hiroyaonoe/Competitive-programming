n,m=list(map(int,input().split()))

s=[]

for i in range(m):
    ks=list(map(int,input().split()))
    ss=[j-1 for j in ks[1:]]
    s.append(ss)
p=list(map(int,input().split()))

on=[0 for i in range(n)]
ans=0
for i in range(1<<n):
    lamp=True
    for j in range(n):
        on[j]=(i & (1<<j)) > 0

    for l in range(m):
        num=0
        for k in s[l]:
            num += on[k]
        if num%2!=p[l]:
            lamp=False
            break
    if lamp:
        ans+=1

print(ans)