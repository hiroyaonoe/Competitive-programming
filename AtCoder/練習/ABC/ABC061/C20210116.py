from collections import defaultdict

n,k=list(map(int,input().split()))
d=defaultdict(int)

for i in range(n):
    a,b=list(map(int,input().split()))
    d[a] += b

i=1
while True:
    k-=d[i]
    if k<=0:
        print(i)
        exit()
    i+=1