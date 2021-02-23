x=input()
m=int(input())
d=int(max(list(x)))
l=len(x)

if l==1:
    if int(x)<=m:
        print(1)
    else:
        print(0)
    exit()

def solve(n):
    t=1
    ret=0
    for i in reversed(range(l)):
        ret += int(x[i])*t
        t *= n
    return ret <= m

def binary_search(ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if solve(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans = binary_search(d, 1<<60) - d
print(ans)