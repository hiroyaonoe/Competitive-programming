from collections import deque

import sys
sys.setrecursionlimit(200000000)

k = int(input())
s = input()
mod = 10**9+7
def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y/2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def dele(s):
    l = len(s)
    ans = 1
    for i in range(1,l):
        if s[i] != s[i-1]:
            ans += 1
    return ans

p = dele(s)
l = len(s)

def search(n,p,k):
    if k == 0:
        return n
    aa = search(24*(n**2)%mod,p+1,k-1)
    aa += search(25*n%mod,p,k-1)
    return aa % mod



print(p)
n = power(25,l-p+2)*power(24,p-1)%mod
ans = search(n,p,k)
print(ans)

# def delete(s):
#     news = deque()
#     l = len(s)
#     for i in range(l):
#         old = s.popleft()
#         if i == l-1:
#             if old != news[-1]:
#                 news.append(old)
#         else:
#             if s[0] != old:
#                 news.append(old)
#     return news
# print(delete(deque("aabbaa")))






