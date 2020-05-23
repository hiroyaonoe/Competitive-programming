n=int(input())

from math import sqrt,floor

nn=floor(sqrt(n))

for i in reversed(range(1,nn+1)):
    if n%i==0:
        f=max(len(str(i)),len(str(int(n/i))))
        print(f)
        exit()