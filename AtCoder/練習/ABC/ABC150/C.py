n=int(input())
p=input()
q=input()

from itertools import permutations as per

i=0
for nn in per(map(str,range(1,n+1))):
    i+=1
    st=' '.join(nn)
    if p==st:a=i
    if q==st:b=i

print(abs(b-a))