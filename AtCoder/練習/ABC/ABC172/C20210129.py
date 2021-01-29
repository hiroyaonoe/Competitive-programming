# editional

n,m,k= list(map(int,input().split()))
a= list(map(int,input().split()))
b= list(map(int,input().split()))

ra=[0]
for i in range(n):
    ra.append(ra[i]+a[i])

rb=[0]
for i in range(m):
    rb.append(rb[i]+b[i])

ans=[0]
best=m
for i in range(n+1):
    aa=ra[i]
    r=k-aa
    if r < 0:break
    while rb[best] > r and best >= 0:
        best -= 1
    ans.append(i+best)

print(max(ans))


# r=k
# ai=-1
# while ai < n-1:
#     ai += 1
#     use=a[ai]
#     if r >= use:
#         r -= use
#     else:
#         ai -= 1
#         break
#
# bi=-1
# while bi < n-1:
#     bi += 1
#     use=b[bi]
#     if r >= use:
#         r -= use
#     else:
#         bi -= 1
#         break
#
# while ai>=0 and bi<m-1:
#     while (r >= b[bi]) and (bi<m-1):
#         r -= b[bi]
#         bi += 1
#
#     if not(ai>=0 and bi<m-1):
#         break
#     mns=a[ai]
#     pls=b[bi+1]
#     if pls<=mns:
#         r = r + mns - pls
#         ai -= 1
#         bi += 1
#     else:
#         break
#
# print(ai+bi+2)