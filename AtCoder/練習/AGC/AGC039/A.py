s=input()
k=int(input())
l=len(s)
now=1
seq=[]
re=False
all=False
for i in range(l):
    if s[i%l]==s[(i+1)%l]:
        if i==l-1:
            re=True
            if len(seq)==0:
                all=True
            else:
                first=seq[0]//2
                end=now//2
                seq[0]=(seq[0]+now)
        now+=1
    else:
        seq.append(now)
        now=1
if all:
    ans=len(s)*k//2
else:
    seq=[i//2 for i in seq]
    if re:
        ans=sum(seq)*k-seq[0]+first+end
    else:
        ans=sum(seq)*k

print(ans)





