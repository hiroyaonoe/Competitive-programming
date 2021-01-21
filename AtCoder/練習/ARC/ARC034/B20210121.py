n=int(input())

ans=[]
for i in range(n-154,n+1):
    if i<=0:continue
    add=0
    s=i
    while s>0:
        add+=s%10
        s=s//10

    if n==i+add:
        ans.append(i)

print(len(ans))
for i in ans:
    print(i)

