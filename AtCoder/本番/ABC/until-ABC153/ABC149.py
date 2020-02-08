# s,t = input().split()
# a=[t,s]
# ans="".join(a)
# print(ans)

# a,b,k=map(int,input().split())
#
# if a>=k:
#     aa=a-k
#     bb=b
# else:
#     aa=0
#     bb=max(a+b-k,0)
# print(aa,bb)

# x=int(input())
# conti=True
# if x==2:conti=False
# while conti:
#     for i in range(2,x):
#         if x%i==0:
#             x+=1
#             break
#         else:
#             if i==x-1:
#                 conti=False
# print(x)

# n,k=map(int,input().split())
# r,s,p=map(int,input().split())
# t=input()
# score=0
# free=[0]*n
# for i in range(n):
#     if i>=k:
#         if (t[i]==t[i-k])&(free[i-k]==0):
#             free[i]=1
#         else:
#             if t[i]=="r":
#                 score+=p
#             elif t[i]=="s":
#                 score+=r
#             elif t[i] == "p":
#                 score += s
#     else:
#         if t[i] == "r":
#             score += p
#         elif t[i] == "s":
#             score += r
#         elif t[i] == "p":
#             score += s
# print(score)

from itertools import combinations as combi

n,m=map(int,input().split())
a=[]*n
a=map(int,input().split())
a.sort()
ans=0
cnt=m//(n*2)
ans=sum(a)*sum(a[:cnt-1])*2-
for i in range(n):
    for j in