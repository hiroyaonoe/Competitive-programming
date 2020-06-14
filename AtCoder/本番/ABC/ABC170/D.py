# n = int(input())
#
# import numpy as np
# a=np.array(map(int,input().split()))
# a.sort(reverse = True)
#
# idx = np.ones(n)
#
# for






n = int(input())

a=list(map(int,input().split()))
a.sort(reverse = True)
from collections import deque
from collections import Counter as cnt
from math import sqrt
aaa = dict(cnt(a))

maa = round(sqrt(a[0]))
ma = maa+2

ans = []
a = deque(a)
while True:
    if len(a) < 1 :
        break
    i = a.pop()
    ans.append(i)

    b = deque()
    while len(a)>0:
        j = a.pop()
        if j%i !=0:
            b.appendleft(j)
    a = b.copy()

    if i >= ma:
        ans += a
        break


mans = 0
for i,v in aaa.items():
    if (i in ans) & (v == 1) :
        mans+=1

print(mans)










