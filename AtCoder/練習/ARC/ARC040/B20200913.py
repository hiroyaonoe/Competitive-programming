n,r=list(map(int,input().split()))
s=input()

ink="o"*r
ok="o"*n
ans=0
i=0
while s!=ok:
    if s[i]==".":
        s=s[:i]+ink+s[i+r:]
    else:
        if "." not in s[i+r:]:
            ans+=1
            break
        i+=1
    ans+=1
print(ans)