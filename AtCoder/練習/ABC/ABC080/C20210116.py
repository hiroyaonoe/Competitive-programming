n=int(input())
f=[]
p=[]

for i in range(n):
    ff=list(map(int,input().split()))
    f.append(ff)

for i in range(n):
    pp=list(map(int,input().split()))
    p.append(pp)

ans=[]
for i in range(1,1<<10):
    gain=0
    for k in range(n):
        open=0
        for j in range(10):
            mask = (i & (1<<j)) > 0
            if mask and f[k][j] > 0:
                open+=1
        gain += p[k][open]
    ans.append(gain)

print(max(ans))