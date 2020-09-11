n=int(input())
a=list(map(int,input().split()))

from math import gcd
from itertools import combinations as cmb

par=[i for i in range(n)]

def root(i):
    if par[i]==i:
        return i
    else:
        r=root(par[i])
        par[i]=r
        return r

def unite(x,y):
    rx=root(x)
    ry=root(y)
    if rx!=ry:
        par[rx]=ry

co=False
set=a[0]
setok=False
for i,j in cmb(range(n),2):
    if i==0:
        set=gcd(set,a[j])
        if setok&set==1:
            print("setwise coprime")
            exit()
    if root(i)!=root(j):
        g=gcd(a[i],a[j])
        if g==1:
            co=True
            unite(i,j)
        else:
            setok=True
            if co:
                print("setwise coprime")
                exit()

if setok:print("not coprime")
else:print("pairwise coprime")