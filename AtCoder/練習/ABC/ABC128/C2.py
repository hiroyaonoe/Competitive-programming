n,m=list(map(int,input().split()))
s=[]
k=[]
for i in range(m):
    ss=list(map(int,input().split()))
    k.append(ss[0])
    s.append(ss[1:])
p=list(map(int,input().split()))


ans=0

for bit in range(2**n):
    ok=True
    for mm in range(m):
        on=0
        for i in s[mm]:
            if bit & 2**(i-1)!=0:
                on+=1
        if on%2==p[mm]:
            pass
        else:
            ok=False

    if ok:ans+=1
print(ans)