n,m=list(map(int,input().split()))
x=[set([i]) for i in range(n)]

def cntbin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count

ans=1
for i in range(m):
    xx,yy=list(map(int,input().split()))
    x[xx-1].add(yy-1)
    x[yy-1].add(xx-1)

for mask in range(1,2**n):
    g=set()
    ok=True
    for i in range(n):
        if (mask >> i) & 1:
            g.add(i)
    for p in g:
        if not g <= x[p]:
            ok=False
            break
    if ok:
        ans=max(ans,len(g))

print(ans)
