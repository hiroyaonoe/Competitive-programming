n,s=list(map(int,input().split()))

aa=list(map(int,input().split()))

aa.sort()

a=[]
for i in aa:
    if i<=s:
        a.append(i)
    else:
        break

mod=998244353

