n = int(input())

a=list(map(int,input().split()))

x = a[0]
for i in range(n-1):
    x = x^a[i+1]
ans = []
if n % 2 == 0:
    for i in range(n):
        pp = a[i]^x
        ans.append(pp)
else:
    ans = a
print(*ans)
# for i in range(n):
#     xx = 0
#     for j in range(n):
#         if i == j:
#             xx = xx^ans[j]
#     print(xx)
