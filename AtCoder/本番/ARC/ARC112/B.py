b,c = list(map(int,input().split()))

if c == 0:
    print(1)
    exit()
if c == 1:
    if b==0:
        print(1)
    else:
        print(2)
    exit()

k = c//2
x=b-k
y=b+k-1
if c % 2 == 0:
    z=-b-k+1
    w=-b+k-1
else:
    z=-b-k
    w=k-b

if x<=w and z<=y:
    mi = min(x,z)
    ma = max(y,w)
    ans=ma-mi+1
else:
    ans=y-x+w-z+2
print(ans)

