n=int(input())
a=[]
a=list(map(int,input().split()))

mi=min(a)
ma=max(a)

ans=[]
for i in range(mi,ma+1):
    sum=0
    for aa in a:
        sum+=(i-aa)**2
    ans.append(sum)

print(min(ans))
