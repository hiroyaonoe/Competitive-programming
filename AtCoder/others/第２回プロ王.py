# n=int(input())
# if n%2==0:n=n/2-1
# else:n=n//2
# print(int(n))

# from itertools import groupby
# n=int(input())
# a=[]*n
# a=list(map(int,input().split(" ")))
# num=1
# ans=True
# if a[0]!=0:ans=False
# a.sort()
# if a.count(0)!=1:ans=False
# for i in range(n-1):
#     if a[i+1]-a[i]!=0|a[i+1]-a[i]!=1:ans=False
# cash=1
# for key, group in groupby(a):
#     length=len(list(group))
#     num=num*((2**cash-1)**length)*(2**(length*(length-1)/2))
#
#     cash=length
# if ans:print(num%998244353)
# else:print("0")




n=int(input())
a=[]*n
b=[]*n
a=list(map(int,input().split(" ")))
b=list(map(int,input().split(" ")))
aso=sorted(a)
bso=sorted(b)
ans=True
for i in range(n):
    if aso[i]>bso[i]:ans=False
cnt=0
for i in range(n):
    if a[i]>b[i]:cnt+=1
if cnt>n-2:ans=False

if ans:print("Yes")
else:print("No")