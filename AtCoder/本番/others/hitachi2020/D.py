n,tt=map(int,input().split())
a=[]
b=[]
for i in range(n):
    aa,bb=map(int,input().split())
    a.append(aa)
    b.append(bb)

d=[a[i]+b[i] for i in range(n)]
t=[1 for i in range(n)]
for i in range(n):
    idx,md=min(enumerate(d),key=lambda x:x[1])
    dd=a[i]*(t[idx]+1)+b[i]+md
    d[i]=min(d[i],dd)
