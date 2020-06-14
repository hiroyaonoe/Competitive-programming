n = int(input())

a=list(map(int,input().split()))
a.sort()

from collections import Counter as cnt
aaa = dict(cnt(a))

ma = max(a)
dp = [True for i in range(ma+1)]

for i in a:
    if dp[i]:
        mul = i*2
        while mul<=ma:
            dp[mul] =False
            mul += i

mans = 0
for i,v in aaa.items():
    if dp[i] & (v == 1) :
        mans+=1

print(mans)