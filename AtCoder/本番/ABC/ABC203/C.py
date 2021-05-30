n, k = list(map(int,input().split()))
ab = []

for i in range(n):
    ab.append(list(map(int,input().split())))

ab.sort(key = lambda x:x[0])

now = 0
for (a,b) in ab:
    if k - a + now < 0:
        print(now + k)
        exit()

    k = k - a + now + b
    now = a

print(now + k)
