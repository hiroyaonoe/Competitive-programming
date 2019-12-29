n,a,b=map(int,input().split())
aa=b-a
if aa%2==0:
    ans=aa/2
else:
    ans=min((a+b-1)/2,(n*2-a-b+1)/2)
print(int(ans))