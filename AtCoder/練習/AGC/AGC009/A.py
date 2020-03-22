n=int(input())
a=[]
b=[]
for i in range(n):
    aa,bb=map(int,input().split())
    a.append(aa)
    b.append(bb)

ans=0

for ii in range(n):
    i=n-ii-1
    aa=a[i]
    bb=b[i]
    ama=(bb-(aa+ans)%bb)%bb
    ans+=ama

print(ans)