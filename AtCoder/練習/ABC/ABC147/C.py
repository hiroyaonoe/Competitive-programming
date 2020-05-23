n=int(input())

xy=[[] for i in range(n)]
for i in range(n):
    a=int(input())
    for j in range(a):
        xx,yy=list(map(int,input().split()))
        xy[i].append([xx-1,yy])


ans=[0]
for ii in range(2**n): #1 is honest

    i=bin(ii)[2:].zfill(n)
    ok=True
    for nin in range(n):
        if int(i[-nin])==1:
            for x,y in xy[nin]:
                if y!=int(i[-x]):
                    ok=False
                    break
            if not ok:break
    if ok:
        ans.append(i.count('1'))
print(max(ans))




# def cntbin(num):
#     bin_num = bin(num)[2:]
#     count = 0
#     for i in bin_num:
#             count += int(i)
#     return count
#
# ans=[0]
# for i in range(2**n): # 0 is honest
#     ok=True
#     for nin in range(n):
#         nin_is= (i>>nin) & 1
#         for x,y in xy[nin]:
#             x_is= nin_is ^ y
#             if ((i>>x) & 1)^x_is ==0:
#                 ok=False
#                 break
#         if not ok:break
#     if ok:
#         ans.append(n-cntbin(i))
#
# print(max(ans))





