n,k = list(map(int,input().split()))

a=n
for i in range(k):
    num=[0 for i in range(10)]
    p=a
    while p>0:
        num[p%10] += 1
        p=p//10
    g1=""
    g2=""
    for i in range(10):
        g1 = "".join([str(i) * num[i], g1])
        g2 = "".join([str(9-i) * num[9-i], g2])
    if g1 == "": g1 = 0
    if g2 == "": g2 = 0
    nec=int(g1)-int(g2)
    if a==nec:
        break
    a=nec

print(a)