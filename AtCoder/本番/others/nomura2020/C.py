n=int(input())
a=list(map(int,input().split()))
ok=True

v=[0 for i in range(n+2)]
import time

#start=time.time()
nextv=0

nec=2**n

for i in range(n,-1,-1):

    if nec>=v[i+1]+a[i]:
        v[i]=v[i+1]+a[i]
    else:
        v[i]=nec

    nec=nec >>1



#print(time.time()-start)

for i in range(1,n+1):
    if v[i-1]-a[i-1]<0:
        ok=False
        break
    if (v[i-1]-a[i-1])*2<v[i]:
        v[i]=(v[i-1]-a[i-1])*2


if n==0:
    if a[0]!=1:ok=False
else:
    if a[0] != 0:ok = False

if v[n]!=a[n]:ok=False

ans=sum(v)
if ans==0:ok=False

if ok:
    print(ans)
else:
    print(-1)

# print(time.time()-start)


