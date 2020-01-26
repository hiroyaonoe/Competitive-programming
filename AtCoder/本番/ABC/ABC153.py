# h,a=map(int,input().split())
# ans=h//a
# if h%a!=0:
#     ans+=1
# print(ans)


# h,n=map(int,input().split())
# a=[]
# a=map(int,input().split())
#
# if h<=sum(a):
#     print("Yes")
# else:
#     print("No")


# n,k=map(int,input().split())
# h=[]
# h=list(map(int,input().split()))
#
# h.sort()
# ans=0
# if n-k>0:
#     ans=sum(h[:n-k])
# print(ans)


# h=int(input())
# mos=1
# ans=0
# while h>0:
#     ans+=mos
#     h=h//2
#     mos*=2
# print(ans)


# h,n=map(int,input().split())
# a=[]
# ab=[]
#
# for i in range(n):
#     aabb=list(map(int,input().split()))
#     ab.append(aabb)
#     a.append(aabb[0])
#
# loop=h+max(a)
# cost=[-1 for i in range(loop)]
# cost[0]=0
# i=0
# costlist=[]
# while i<loop:
#     costlist=[]
#     for j in range(n):
#         ii=i-ab[j][0]
#         if (0<=ii<h)&(cost[ii]>=0):
#             costlist.append(cost[ii]+ab[j][1])
#     if len(costlist)!=0:
#         cost[i]=min(costlist)
#     i+=1
# acost=[i for i in cost[h:] if i!=-1]
# ans=min(acost)
# print(ans)


