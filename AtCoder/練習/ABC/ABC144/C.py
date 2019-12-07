from math import floor
from math import sqrt
n=int(input())
nn=floor(sqrt(n))
rest=n%nn
while rest!=0:
    nn-=1
    rest=n%nn
nnn=n/nn
print(int(nn+nnn-2))