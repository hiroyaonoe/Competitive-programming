n=int(input())

a=[]
b=[]

for i in range(n):
    aa,bb=list(map(int,input().split()))
    a.append(aa*2)
    b.append(bb*2)

a.sort()
b.sort()

if n%2==1:
    amed=a[(n-1)//2]
    bmed=b[(n-1)//2]

    ans=(bmed-amed)//2+1
else:
    amed=(a[n//2-1]+a[n//2])/2
    bmed = (b[n // 2 - 1] + b[n // 2]) / 2

    ans=bmed-amed+1

print(int(ans))