n,q=map(int,input().split())
s=input()
idx=[0 for i in range(n+1)]

for i in range(n-1):
    if s[i:i+2]=="AC":idx[i+1]=idx[i]+1
    else:idx[i+1]=idx[i]

ans=[]
for i in range(q):
    l,r=map(int,input().split())
    print(idx[r-1]-idx[l-1])




