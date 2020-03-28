n=int(input())
aa=[]
aa=list(map(int,input().split()))
# a=[[aa[i],i] for i in range(n)]

a=sorted(aa)
sum=0
mae=0
index=[0 for i in range(n)]
for i in range(n-1):
    if a[i]!=a[i+1]:
        index[a[i]-1]=i-mae+1
        sum+=(i-mae+1)*(i-mae)/2
        mae=i+1
index[a[n-1]-1]=n-mae
sum+=(n-mae)*(n-mae-1)/2

for ii in aa:
    ans=sum-index[ii-1]+1
    print(int(ans))

