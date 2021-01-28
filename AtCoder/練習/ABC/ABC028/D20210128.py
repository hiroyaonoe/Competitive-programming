n,k= list(map(int,input().split()))
p = 1
p += 3 * (n-1)
p += 6 * (n-k) * (k-1)
print(p/(n**3))