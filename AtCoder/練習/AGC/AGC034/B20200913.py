s=input()
l=len(s)
ans=0
i=0
while i<l-2:
    if s[i:i+3]=="ABC":
        s=s[:i]+"BCA"+s[i+3:]
        if i!=0:i-=1
        ans+=1
    else:i+=1
print(ans)