n,k=map(int,input().split())
p=[]
p=list(map(int,input().split()))

ans=sum(p[0:k])
aa=sum(p[0:k])
for i in range(1,n-k+1):
    aa=aa-p[i-1]+p[i+k-1]
    ans=max(ans,aa)

aaaa=(ans+k)/2
print(aaaa)