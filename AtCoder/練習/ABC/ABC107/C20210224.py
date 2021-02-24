# editorial
n,k = list(map(int,input().split()))
x = list(map(int,input().split()))

ans=[]
for i in range(n-k+1):
    l=x[i]
    r=x[i+k-1]
    ans.append(abs(l) + abs(r - l))
    ans.append(abs(r) + abs(r - l))
print(min(ans))

# import bisect
#
# n,k = list(map(int,input().split()))
# x = list(map(int,input().split()))
#
# zero = bisect.bisect_left(x,0)
# ridx=zero+k-1
# lidx=zero
#
# ans=1<<60
#
# for i in range(k):
#     if lidx < 0: break
#     if ridx<=n-1:
#         left = -x[lidx]
#         if lidx==zero:
#             left=0
#         right = x[ridx]
#         ans=min([ans,left+right*2,left*2+right])
#     lidx-=1
#     ridx-=1
#
# print(ans)