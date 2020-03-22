

n,m=map(int,input().split())

s=[]

for i in range(m):
    sss=list(map(int,input().split()))
    k=sss[0]
    b=0
    for ss in sss[1:]:
        b+=0b1<<(ss-1)
    s.append(b)


p=[]
p=list(map(int,input().split()))

def cntbin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count

ans=0

for i in range(2**n):
    ok=True
    for k in range(m):
        cnt=cntbin(i&s[k])
        if cnt%2==p[k]:
            pass
        else:ok=False

    if ok:ans+=1

print(ans)

