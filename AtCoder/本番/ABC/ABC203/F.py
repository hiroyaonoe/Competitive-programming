import random

n = 10
k = 3
print(n, k)
m = 10**9 + 1
for i in range(n):
    l = []
    for j in range(n):
        l.append(str(random.randint(0, m)))

    print(" ".join(l))