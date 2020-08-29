n,m=list(map(int,input().split()))
k=[]
s=[]

def cntbin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count

for i in range(m):
    kk,*ss=list(map(int,input().split()))
    k.append(kk)
    s.append(ss)

p=list(map(int,input().split()))

ans=0
for i in range(2**n):
    ok=True
    for mm in range(m):
        if not ok:break
        mask=0
        for ss in s[mm]:
            mask+=1 << ss-1
        on=cntbin(i&mask)
        if p[mm]!=on%2:
            ok=False

    if ok:ans+=1

print(ans)