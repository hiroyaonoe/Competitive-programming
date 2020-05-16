n,a,b=list(map(int,input().split()))
x=list(map(int,input().split()))

cost=0
tp=n-1
for i in range(n-1):
    walk=(x[i+1]-x[i])*a
    if walk<b:
        cost+=walk
        tp-=1

cost+=tp*b
print(cost)