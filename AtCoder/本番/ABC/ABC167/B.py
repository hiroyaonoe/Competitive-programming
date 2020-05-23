a,b,c,k=map(int,input().split())
ans=0
cc=k-a-b
bb=k-b
if cc>0:
    ans=a-cc
elif bb>0:
    ans=a
else:
    ans=k
print(ans)