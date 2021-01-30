n,m= list(map(int,input().split()))
ab=[]
for i in range(m):
    ab.append(list(map(int,input().split())))

k=int(input())
cd=[]
for i in range(k):
    cd.append(list(map(int,input().split())))

ans=[0]
for i in range(1 << k):
    s=0
    l=[False for q in range(n+1)]
    for j in range(k):
        mask = (i & (1<<j)) > 0
        l[cd[j][mask]] = True

    for j in range(m):
        a,b=ab[j]
        if l[a] and l[b]:
            s += 1
    ans.append(s)


print(max(ans))
