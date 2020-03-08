a,b,m=map(int,input().split())
a=[]
b=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=[]

for i in range(m):
    x,y,c=map(int,input().split())
    x-=1
    y-=1
    ans.append(a[x]+b[y]-c)
ans.append(min(a)+min(b))
print(min(ans))