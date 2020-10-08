x,y,r=list(map(int,input().split()))
x1,y1,x2,y2=list(map(int,input().split()))


if (x1<=x-r)&(x+r<=x2)&(y1<=y-r)&(y+r<=y2):
    print("NO")
else:
    print("YES")


yes=False

for xx in (x1,x2):
    for yy in (y1,y2):
        if r**2<(xx-x)**2+(yy-y)**2:
            yes=True

if yes:
    print("YES")
else:
    print("NO")

