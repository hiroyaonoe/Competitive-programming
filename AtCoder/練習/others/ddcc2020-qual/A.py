x,y=list(map(int,input().split()))
awd=[300000,200000,100000]
ans=0
for xy in [x,y]:
    for ott in range(3):
        if xy==ott+1:
            ans+=awd[ott]

if x==1&y==1:
    ans+=400000

print(ans)
