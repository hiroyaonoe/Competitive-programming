from collections import defaultdict

s=input().split()
sd=defaultdict(list)
for i,ss in enumerate(s):
    sd[len(ss)].append([ss,i])

n=int(input())
for i in range(n):
    t=input()
    l=len(t)
    star=[]
    for k in range(l):
        if t[k]=="*":
            star.append(k)

    for ii,[cc,j] in enumerate(sd[l]):
        if j==-1:continue
        for k in star:
            cc= cc[:k]+"*"+cc[k+1:]
        if cc==t:
            s[j]="*"*l
            sd[l][ii][1]=-1
print(" ".join(s))

