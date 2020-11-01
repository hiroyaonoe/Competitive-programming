s=input()
l=len(s)
ans=0
for i in range(l-1):
    if s[i]!=s[i+1]:
        ans+=1
print(ans)