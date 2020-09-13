r,c,d=list(map(int,input().split()))
ans=[]
for i in range(r):
    a=list(map(int,input().split()))
    for j,aa in enumerate(a):
        q=d-i-j
        if (q%2==0)&(q>=0):
            ans.append(aa)

print(max(ans))

