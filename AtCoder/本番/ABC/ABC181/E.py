import bisect

n,m=list(map(int,input().split()))

hh=list(map(int,input().split()))
w=list(map(int,input().split()))
hh.sort()
omt=[0 for i in range(n)]
ura=[0 for i in range(n)]
ukari=[]
for i in range(n-1):
    mns = hh[i+1] - hh[i]
    if i%2==0:
        oad=mns
        uad=0
    else:
        uad = mns
        oad = 0
    omt[i+1]=omt[i]+oad
    ukari.append(uad)
for i in reversed(range(n-1)):
    ura[i]=ura[i+1]+ukari[i]
ura.append(0)
ans=[]
for i in w:
    idx=bisect.bisect(hh,i)
    pls=0
    if idx%2==0:
        if idx<n:
            pls=abs(hh[idx]-i)
    else:
        pls=abs(i-hh[idx-1])
    o=omt[max(idx-1,0)]
    u=ura[max(idx,0)]
    ans.append(o+pls+u)

print(min(ans))