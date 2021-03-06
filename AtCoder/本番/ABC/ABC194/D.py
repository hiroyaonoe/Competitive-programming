n=int(input())

from math import factorial as fac
s=n*(n-1)//2
child=fac(n-1)*n
par=pow(s,n-2)*(n-s)**2
print(child/par)

