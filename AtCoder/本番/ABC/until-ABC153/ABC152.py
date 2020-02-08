# n,m=map(int,input().split())
# if n==m:
#     print("Yes")
# else:
#     print("No")

# a,b=map(int,input().split())
# # ans=str(min(a,b))*max(a,b)
# # print(ans)

# n=int(input())
# p=[]*n
# p=list(map(int,input().split()))
# cnt=0
# com=p[0]
# for i in range(n):
#     if com>=p[i]:
#         cnt+=1
#     com=min(com,p[i])
# print(cnt)

# n=int(input())
# cnt=0
# data=[[0 for j in range(10)] for i in range(10)]
# for ii in range(1,n+1):
#     i=str(ii)
#     if i[-1]!=0:
#         data[int(i[-1])][int(i[0])]+=1
#
# for i in range(9):
#     for j in range(9):
#         cnt+=data[i+1][j+1]*data[j+1][i+1]
# print(cnt)

from random import randint

import sys
sys.setrecursionlimit(2000000)

from fractions import gcd
def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x


mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))



n=int(input())
aa=[]
aa=list(map(int,input().split()))
# for i in range(n):
#     aa.append(randint(1,10**6))

bb=lcm(aa)
mod=10**9+7
ans=0
for i in range(n):
    ccc=div(bb,aa[i])
    ans=int((ccc%mod+ans%mod)%mod)
print(int(ans))