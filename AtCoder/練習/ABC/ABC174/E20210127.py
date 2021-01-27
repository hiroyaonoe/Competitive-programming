# editional
n,k= list(map(int,input().split()))
a= list(map(int,input().split()))
a.sort(reverse=True)

low = 0
high = a[0]
while True:
    s=0
    x=(low+high)//2
    if low==x or high==x:
        break

    for q in a:
        if q<=x:break
        s += q//x
        if q%x==0:
            s -= 1
        if s > k:break
    if s > k:
        low=x
    else:
        high=x

print(x+1)

