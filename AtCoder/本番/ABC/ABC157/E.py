n=int(input())
s=input()
q=int(input())
ss=[]

for i in range(n):
    ss.append(ord(s[i]))
for qq in range(q):
    t,i,c=input().split()
    if t=="1":
        ss[int(i)-1]=ord(c)
    else:
        qs=ss[int(i)-1:int(c)]
        qs.sort()
        ans=1
        for j in range(len(qs)-1):
            if qs[j]!=qs[j+1]:ans+=1
        print(ans)

