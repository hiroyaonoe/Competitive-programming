n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

num=sum(b)-sum(a)
if num<0:
    print("No")
    exit()

need=0
for i in range(n):
    aa=a[i]
    bb=b[i]
    if aa>bb:
        need+=aa-bb
    elif aa<bb:
        need-=(bb-aa)//2

if need<=0:print("Yes")
else:print("No")



