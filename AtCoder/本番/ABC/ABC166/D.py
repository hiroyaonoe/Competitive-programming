x=int(input())

f=[i for i in range(-128,129)]

from itertools import combinations as cmb
ok=False
for b,a in cmb(f,2):
    if x==a**5-b**5:
        ok=True
        aa=a
        bb=b
        break
if ok:print(aa,bb)