import numpy as np
import time
n,k=list(map(int,input().split()))
a=np.array(list(map(int,input().split())))

last = np.array([n]*n)

if n<=k:
    ans = list(map(str, last))
    print(" ".join(ans))
    exit()

s = time.time()
olda = np.zeros(n, dtype = int)
newa = a.copy()
for j in range(k):
    print(j)
    print(a)
    # newa = np.zeros(n, dtype = int)

    for i in range(n):
        num = a[i]
        di = olda[i]
        mi = max(i - num, 0)
        mii = max(i - di, 0)
        ma = min(i + num + 1, n)
        maa = min(i + di + 1, n)
        # newa[mi:ma] += 1
        newa[mi:mii] +=1
        newa[maa:ma] +=1
    olda = a.copy()
    a=newa.copy()
    mask = a == n
    if mask.all():
        break


a=list(map(str, a))
print(" ".join(a))




