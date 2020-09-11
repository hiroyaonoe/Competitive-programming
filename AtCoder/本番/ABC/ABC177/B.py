s=input()
t=input()

ans=1<<30
for i in range(len(s)-len(t)+1):
    ss=s[i:i+len(t)]
    cnt=0
    for j in range(len(t)):
        if ss[j]!=t[j]:cnt+=1
    ans=min(ans,cnt)

print(ans)