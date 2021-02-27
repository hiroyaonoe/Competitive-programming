from time import time
import math
n = int(input())
ans = n
two=math.floor(math.sqrt(n+1))
table = [0 for i in range(two + 1)]
for i in range(2, n + 1):
    k = i ** 2
    if k > n:
        break
    if table[i]:continue
    while k <= n:
        if k<=two:
            table[k] = True
        ans -= 1
        k *= i

print(ans)
