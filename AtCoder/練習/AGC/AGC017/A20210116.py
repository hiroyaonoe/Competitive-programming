# editional

n, p = list(map(int,input().split()))
a=list(map(int,input().split()))

one=0
for i in a:
    if i%2==1:
        one+=1


if one==0:
    if p==0:
        print(2**n)
    else:
        print(0)
else:
    print(2**(n-1))

