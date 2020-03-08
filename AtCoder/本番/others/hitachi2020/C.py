n=int(input())
d=[[set() for i in range(n)] for j in range(3)]
# two=[set() for i in range(n)]
# three=[set() for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    d[0][a].add(b)
    d[0][b].add(a)

p=[1 for i in range(n)]

for i in range(n):
    for one in d[0][i]:
        for two in d[0][one]:
            if two!=i:
                for three in d[0][two]:
                    if three!=one:
                        d[2][i].add(three)
                        d[2][three].add(i)

pair=[]
ans=[i for i in range(n)]

for a in range(n):
    for b in d[2][a]:
        if a<b:
            pair.append([a,b])

pair.sort(key=lambda x:x[1])
pair.sort(key=lambda x:x[0])

for a,b in pair:
    aa=ans[a]
    bb=ans[b]
    if (aa+bb)%3!=0:
        ama=(aa+bb)%3










