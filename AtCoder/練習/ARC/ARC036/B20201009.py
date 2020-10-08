n=int(input())

oh=int(input())

up=True
s=1
ans=[]
for i in range(1,n):
    nh=int(input())
    grad=nh-oh>0

    if up:
        if not grad:
            up=False
    else:
        if grad:
            ans.append(i-s+1)
            s=i
            up=True
    oh=nh

ans.append(n-s+1)
print(max(ans))




