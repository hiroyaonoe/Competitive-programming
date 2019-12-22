# a=int(input())
# b=int(input())
# print(6-a-b)

# n=int(input())
# s,t=input().split()
# ans=[]
# for i in range(n):
#     ans.append(s[i])
#     ans.append(t[i])
# aaa=''.join(ans)
# print(aaa)

# from fractions import gcd
# a,b=map(int,input().split())
# ans=a*b/gcd(a,b)
# print(int(ans))

# import sys
# sys.setrecursionlimit(2000000)
#
# n=int(input())
# a=[]*n
# a=list(map(int,input().split()))
# num=1
# bre=0
# no=True
# def search(pos):
#     spos=pos
#     global num,bre,no
#     end=True
#     while end:
#         if spos >= n:
#             break
#         if a[spos]==num:
#             no=False
#             num+=1
#             search(spos+1)
#             end=False
#         else:
#             spos+=1
#             bre+=1
#
# search(0)
# if no:
#     bre=-1
# print(bre)

n=int(input())
ans=0
if n%2==0:
    num=len(str(n))*2
    # n=int(n/2)
    ans=0
    for i in range(num):
        ans+=n//(10*(5**i))
print(int(ans))
# out=1
# def test(ss):
#     global out
#     if ss>0:
#         out*=ss
#         test(ss-2)
# test(n)
# str(out)
# sss=len(str(out))
# while sss>=0:
#     if out[sss]==0:
#         aaa+=1
#         sss-=1
#     else:sss=-1
# print(aaa)





