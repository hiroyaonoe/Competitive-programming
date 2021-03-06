from itertools import combinations as cmb

n=int(input())
a = list(map(int,input().split()))
ans=0
s=sum(a)
ss=sum([i**2 for i in a])
print(n*ss-s**2)