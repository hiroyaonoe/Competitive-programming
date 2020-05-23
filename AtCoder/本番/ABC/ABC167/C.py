n,m,x=map(int,input().split())
c=[]
a=[]

for i in range(n):
    ca=list(map(int,input().split()))
    c.append(ca[0])
    a.append(ca[1:])
ok=False
money=[]

for cnt in range(2**n):
    aa=[0 for j in range(m)]
    mon=0
    for i in range(n):
        if 2**i & cnt !=0:
            mon+=c[i]
            for mm in range(m):
                aa[mm]+=a[i][mm]
    if min(aa) >= x:
        ok = True
        money.append(mon)

if ok:
    print(min(money))
else:
    print(-1)

