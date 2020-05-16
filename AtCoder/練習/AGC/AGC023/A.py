# 解説AC

from collections import Counter as cnt

n=int(input())
a=list(map(int,input().split()))

s=[0 for i in range(n+1)]

for i in range(n+1):
    if i>0:
        s[i]=s[i-1]+a[i-1]

s.sort()
dic=cnt(s)
ans=0
for n in dic.values():
    ans+=n*(n-1)/2

print(int(ans))

