from itertools import combinations as cmb

n=int(input())

idx=[0,0,0,0,0]

for i in range(n):
    s=input()
    ss=s[0]
    if ss=="M":
        idx[0]+=1
    elif ss=="A":
        idx[1]+=1
    elif ss=="R":
        idx[2]+=1
    elif ss=="C":
        idx[3]+=1
    elif ss=="H":
        idx[4]+=1

ans=0
for a,b,c in cmb(idx,3):
    ans+=a*b*c

print(ans)