h=list(map(int,input().split()))

a=max(h)
b=min(h)
ans=0
if a%2==0:
    ans=a*b/2
else:
    ans+=(a-1)*b/2
    ans+=(b+1)//2

if b==1:ans=1
print(int(ans))