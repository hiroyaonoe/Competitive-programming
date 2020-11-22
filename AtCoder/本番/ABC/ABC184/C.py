a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
x=c-a
y=d-b

if x==0 and y==0:
    print(0)
    exit()

if (abs(x)+abs(y)<=3) or (abs(x)==abs(y)) :
    print(1)
    exit()

if abs(x)+abs(y)<=6 :
    print(2)
    exit()

l=(-3,-2,-1,0,1,2,3)
for i in l:
    for j in l:
        xx=x+i
        yy=y+j
        if abs(xx) + abs(yy) <= 3 or abs(xx) == abs(yy):
            print(2)
            exit()


if (x+y)%2==0:
    print(2)
else:
    print(3)
