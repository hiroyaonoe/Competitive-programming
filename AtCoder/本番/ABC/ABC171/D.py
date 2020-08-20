n = int(input())

aa=list(map(int,input().split()))
q = int(input())
b=[]
c=[]
from collections import Counter as cnt
ans = sum(aa)

a = dict(cnt(aa))
for i in range(q):
    bb,cc=list(map(int,input().split()))
    b.append(bb)
    c.append(cc)
    if bb not in a:
        a[bb]=0
    if cc not in a:
        a[cc]=0



for i in range(q):
    ans += a[b[i]]*(c[i]-b[i])
    a[c[i]] += a[b[i]]

    a[b[i]] = 0
    print(ans)
