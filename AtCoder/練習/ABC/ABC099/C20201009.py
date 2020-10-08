import sys
sys.setrecursionlimit(2000000000)

n=int(input())

memo=[-1 for i in range(n+1)]

def search(n):
    if n==0:
        return 0
    if memo[n]!=-1:
        return memo[n]

    res=n

    p=1
    while p<=n:
        res=min(res,search(n-p)+1)
        p*=6

    p = 1
    while p <= n:
        res = min(res, search(n - p) + 1)
        p *= 9

    memo[n]=res
    return res

ans=search(n)
print(ans)

# https://qiita.com/drken/items/ace3142967c4f01d42e9





# l=[1]
# i=6
# while i<n:
#     l.append(i)
#     i*=6
# i=9
# while i<n:
#     l.append(i)
#     i*=9
#
# l.sort(reverse=True)
# cnt=0
# while n>0:
#     for i in l:
#         if i<=n:
#             n-=i
#             cnt+=1
#             print(i)
#             break
#
# print(cnt)
