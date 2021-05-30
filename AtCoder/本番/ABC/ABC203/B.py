n, k = list(map(int,input().split()))

j = (k * (k+1) * n) // 2
i = (n * (n+1) * k) // 2

print(i*100+j)
