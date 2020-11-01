n,t=list(map(int,input().split()))
s=0
c=[]
for i in range(n):
    aa,bb=list(map(int, input().split()))
    c.append(aa-bb)
    s+=aa

c.sort()

ans=0
while s>t:
    if len(c)==0:
        print(-1)
        exit()
    ans+=1
    r=c.pop()
    s-=r

print(ans)