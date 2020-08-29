n=int(input())
a=[]
b=[]
for i in range(n):
    aa,bb=list(map(int,input().split()))
    a.append(aa)
    b.append(bb)

ans=[]
for i in a:
    for o in b:
        cnt=0
        for nn in range(n):
            aa=a[nn]
            bb=b[nn]
            cnt+=abs(aa-i)+abs(bb-aa)+abs(o-bb)
        ans.append(cnt)

print(min(ans))