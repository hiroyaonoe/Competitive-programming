n=int(input())

a=[]
b=[]
for i in range(n):
    aa,bb = list(map(int,input().split()))
    a.append(aa)
    b.append(bb)
ans=[]
for i in range(n):
    for j in range(n):
        if i==j:
            ans.append(a[i]+b[j])
        else:
            ans.append(max([a[i],b[j]]))
print(min(ans))