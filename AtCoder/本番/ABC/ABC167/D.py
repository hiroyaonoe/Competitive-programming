

n,k=map(int,input().split())
a=list(map(int,input().split()))

ne=0
his=[None for i in range(n)]
l=False
for i in range(min(n,k)):
    if his[ne]!=None:
        back=his[ne]
        loop=i-back
        l=True
        break
    his[ne]=i
    #his.append(ne)
    ne=a[ne]-1

if l:
    ansidx=(k-back)%loop+back
    ans=his.index(ansidx)+1
else:
    ans=ne+1
print(ans)
