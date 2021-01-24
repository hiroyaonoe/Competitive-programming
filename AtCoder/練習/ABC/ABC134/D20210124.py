n=int(input())

a= list(map(int,("0 "+input()).split()))
b=[0 for i in range(0,n+1)]
for i in reversed(range(1,n+1)):
    k=i*2
    s=0
    while k<=n:
        s=s ^ b[k]
        k += i
    b[i]= s ^ a[i]

ans=[str(i) for i,v in enumerate(b) if v ]
print(len(ans))
print(" ".join(ans))