import numpy as np

n=int(input())
idx=np.arange(1,n+1)
a=np.array(list(map(int,input().split())))
ans=0
for i in range(n):
    minus=a[i]+i
    mask = np.arange(n-minus)==a[minus:]
    ans+=np.count_nonzero(mask)

print(ans)