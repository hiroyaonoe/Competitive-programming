
n=int(input())
x=[]
x=list(map(int,input().split()))
x.sort()
cost=[]
for i in range(x[0],x[-1]+1):
    aaa=[(xx-i)**2 for xx in x]
    cost.append(sum(aaa))
ans=min(cost)
print(ans)

