a,v=list(map(int,input().split()))
b,w=list(map(int,input().split()))
t=int(input())

if v<=w:
    print("NO")
else:
    if abs(a-b)<=t*(v-w):
        print("YES")
    else:
        print("NO")

