n=int(input())
lx=[]
ly=[]
for i in range(n):
    xx,yy= list(map(int,input().split()))
    lx.append(xx)
    ly.append(yy)
m=int(input())
p=[((0,0,0),(1,0,0))]
x,y=[(0,0,0),(1,0,0)]

def rev(l):
    new =(l[0], not l[1],-l[2])
    return new

for i in range(m):
    op=list(map(int,input().split()))
    if op[0]==1:
        tmp=rev(x)
        x=y
        y=tmp
        op.append((x,y))
    elif op[0]==2:
        tmp=rev(y)
        y=x
        x=tmp
    elif op[0]==3:
        x=rev(x)
        x=(x[0],x[1],x[2]+2*op[1])
    else:
        y=rev(y)
        y=(y[0],y[1],y[2]+2*op[1])
    p.append((x, y))

q=int(input())
for i in range(q):
    a,b= list(map(int,input().split()))
    xy = [lx[b-1],ly[b-1]]
    op=p[a]
    ans=[0,0]
    for i in range(2):
        ans[i]=xy[op[i][0]]
        if op[i][1]:
            ans[i]=-ans[i]
        ans[i]+=op[i][2]
    print(ans[0],ans[1])


