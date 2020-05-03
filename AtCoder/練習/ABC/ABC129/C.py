n,m=map(int,input().split())
a=[True for i in range(n)]
for i in range(m):
    a[int(input())-1]=False

num=[0 for i in range(n+2)]
num[0]=0
num[1]=1
mod=10**9+7
for i in range(n):
    if a[i]:
        num[i+2]=(num[i+1]+num[i])%mod

print(num[n+1])

