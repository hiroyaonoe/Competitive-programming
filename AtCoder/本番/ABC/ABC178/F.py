n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from collections import defaultdict
b=reversed(b)
dic=defaultdict(list)
same=[]
ok=0
for i in range(n):
    aa=a[i]
    bb=b[i]
    if aa==bb:
        same.append(i,aa)
    else:
        ok+=1
        dic[aa].append(i)
        dic[bb].append(i)

for i in same:
    if len(dic[i])>=ok:
        print("No")
        exit()
    else:

