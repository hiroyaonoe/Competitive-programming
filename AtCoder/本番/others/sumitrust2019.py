# m,d=map(int,input().split(" "))
# mm,dd=map(int,input().split(" "))
# if m==mm:print(0)
# else:print(1)

# import math
# n=int(input())
# ans=n/1.08
# ans=int(math.ceil(ans))
# if float(n)==math.floor(ans*1.08):print(ans)
# else:print(":(")

# x=int(input())
# num=x//100
# if x-num*100<=5*num:print(1)
# else:print(0)

import sys
input=sys.stdin.readline
from itertools import combinations as cmb
n=int(input())
s=list(input().rstrip())
# s.remove("\n")
combiset=set(cmb(s,3))
print(len(combiset))

