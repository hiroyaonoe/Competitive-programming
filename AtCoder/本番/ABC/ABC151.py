# n=input()
# # print(chr(ord(n)+1))


# n,k,m=map(int,input().split())
# a=[]*(n-1)
# a=map(int,input().split())
# ans=m*n-sum(a)
# if ans<0:ans=0
# if ans>k:ans=-1
# print(ans)

# n,m=map(int,input().split())
# p=[[] for i in range(m)]
# s=[[] for i in range(m)]
# k=[True for i in range(n)]
# ac=0
# wa=[0 for i in range(n)]
#
# for i in range(m):
#     p[i],s[i]=input().split()
#
# p=list(map(int,p))
#
# for i in range(m):
#     if k[p[i]-1]:
#         if s[i]=="AC":
#             k[p[i]-1]=False
#             ac+=1
#         else:
#             wa[p[i]-1]+=1
#
# for i in range(n):
#     if k[i]:
#         wa[i]=0
#
# print(ac,sum(wa))

# import sys,copy
# sys.setrecursionlimit(100000000)
# h,w = map(int,input().split())
# ss=[[[] for i in range(w)] for j in range(h)]
# s=[[[] for i in range(w)] for j in range(h)]
# for i in range(h):
#     s[i]=list(input())
#
# dxdy=[[-1,0],[0,-1],[1,0],[0,1]]
#
# def search(x,y,qx,qy,cnt):
#     global aans
#     for dx,dy in dxdy:
#         if (0<=x+dx<=w-1)&(0<=y+dy<=h-1):
#             if (qx!=x+dx)|(qy!=y+dy):
#                 if s[y+dy][x+dx]==".":
#                     cnt+=1
#                     if cnt<=aans:
#                         if (x+dx == gx) & (y+dy == gy):
#                             aans = min(aans, cnt)
#                             cnt-=1
#                         else:
#                             search(x+dx,y+dy,x,y,cnt)
#
# ans=0
# for x in range(w):
#     for y in range(h):
#         for gx in range(w):
#             for gy in range(h):
#                 aans=1000
#                 if (x!=gx)|(y!=gy):
#                     if (s[y][x]==".")&(s[gy][gx]=="."):
#                         search(x,y,0,0,0)
#                         ans=max(aans,ans)
# print(ans)


# n,m=map(int,input().split())
# a=map(int,input().split())
# a.sort()
# dis=[a[i+1]-a[i] for i in range(n-1)]



