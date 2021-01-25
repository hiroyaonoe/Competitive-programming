# editorial
n=int(input())
s=[]
ans=0
ba=0
ca=0
bc=0
for i in range(n):
    s=input()
    for l in range(len(s)-1):
        if s[l:l+2]=="AB":
            ans+=1

    if s[-1] == "A":
        if s[0] == "B":
            ba+=1
        else:
            ca+=1
    else:
        if s[0] == "B":
            bc+=1

if ba==0:
    ans+=min(ca,bc)
else:
    if ca+bc>0:
        ans+=ba+min(ca,bc)
    else:
        ans+=ba-1

print(ans)

