x=input()
m=int(input())
d=int(max(list(x)))
x=int(x)
low=d+1
mid=d+2

while mid-low>1:
    num=""
    p=m
    while p > 0:
        i=p%mid
        num=''.join([str(i),num])
        p=p//mid
    if x > int(num):
        mid=(mid+low)//2
    else:
        low=mid
        mid *= 2

mid += 1
while True:
    num=""
    p=m
    while p > 0:
        i=p%mid
        num=''.join([str(i),num])
        p=p//mid
    if x <= int(num):
        print(mid-d)
        exit()
    mid-=1
