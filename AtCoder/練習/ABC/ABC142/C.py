n=int(input())
a=list(map(int,input().split()))
x=[[a[i],i+1] for i in range(n)]
x.sort()
b=[str(x[j][1]) for j in range(n)]
ans=" ".join(b)
print(ans)