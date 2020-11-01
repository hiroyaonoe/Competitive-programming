from collections import Counter as cnt
sss=input()
ss=cnt(list(sss))

i=0

l=min(len(sss),3)
while i<10**l:
    if sss==i:
        print("Yes")
        exit()
    s=ss.copy()
    ok=True
    si=str(i).zfill(l)
    for j in range(l):
        lit=si[j]
        if s[lit]>0:
            s[lit]-=1
        else:
            ok=False
            break
    if ok:
        print("Yes")
        exit()
    i+=8

print("No")
