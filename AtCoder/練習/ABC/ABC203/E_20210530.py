n, m = list(map(int,input().split()))

xy = []
for i in range(m):
    xy.append(list(map(int,input().split())))

xy.sort(key=lambda x: (x[0], x[1]))

s = set()
s.add(n)

xx = -1
a = set()
b = set()

for i in range(m):
    x, y = xy[i]
    if x != xx:
        xx = x
        for aa in a: s.add(aa)
        for bb in b: s.remove(bb)
        a = set()
        b = set()
    if (y - 1 in s or y + 1 in s) and y not in s:
        a.add(y)
    if (y - 1 not in s and y + 1 not in s) and y in s:
        b.add(y)

for aa in a: s.add(aa)
for bb in b: s.remove(bb)

print(len(s))
