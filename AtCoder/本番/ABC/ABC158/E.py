n,p=map(int,input().split())
s=input()

genL=[set() for i in range(n+1)]
ans=0


def ser(l,gL):
    global kari

    for gR in genL[l+len(str(gL))]:
        new=str(gL)+str(gR)
        if new not in genL[l]:
            kari.add(new)
            ser(l,new)





if p==2:
    for i in range(n):
        if int(s[i])%2==0:
            ans+=i+1
elif p==5:
    for i in range(n):
        if int(s[i])%5==0:
            ans+=i+1
else:
    pke=len(str(p))
    for i in range(pke+1):
        for l in range(n-i):
            num=s[l:l+i+1]
            if int(num)%p==0:

                genL[l].add(num)


    for i in range(n):
        kari=set()
        for l in genL[i]:
            ser(i,l)

        for k in kari:
            genL[i].add(k)

    for i in genL:
        ans+=len(i)

print(ans)




