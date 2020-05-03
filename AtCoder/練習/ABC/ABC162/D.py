n=int(input())
s=input()
list(s)
r=s.count("R")
g=s.count("G")
b=s.count("B")
ans=r*g*b

for j in range(n):
    m=min(j,n-j-1)
    if m==0:
        continue
    for ik in range(m):
        ii=s[j-ik-1]
        jj=s[j]
        kk=s[j+ik+1]
        if (ii!=jj)&(jj!=kk)&(kk!=ii):ans-=1
print(ans)
