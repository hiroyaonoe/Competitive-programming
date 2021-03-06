

# import random
# n=15*10**5
# m=1
# a=[random.randint(0,n) for i in range(n)]

n,m = list(map(int,input().split()))
a = list(map(int,input().split()))

memo=[0 for i in range(n+1)]

a.append(-1)
for i in range(m):
    memo[a[i]] += 1
j=0
while True:
    if memo[j] == 0:
        break
    j += 1
ans=[j]
outa=a[0]
ina=a[m]
memo[outa] -= 1
memo[ina] += 1
for i in range(1,n-m+1):
    if outa<=j and memo[outa]==0:
        j=outa
    elif ina == j:
        while True:
            if memo[j] == 0:
                break
            j += 1
    ans.append(j)
    outa = a[i]
    ina = a[i+m]
    memo[outa] -= 1
    memo[ina] += 1

print(min(ans))