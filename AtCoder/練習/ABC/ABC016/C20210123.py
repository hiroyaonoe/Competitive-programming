n,m=list(map(int,input().split()))

e=[[] for i in range(n)]
for i in range(m):
    a,b=list(map(int,input().split()))
    e[a-1].append(b-1)
    e[b-1].append(a-1)


for i in range(n):
    ans=[i]
    ans+=e[i]

    for b in e[i]:
        ans += e[b]
    print(len(set(ans))-len(e[i])-1)