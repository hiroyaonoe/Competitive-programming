n=int(input())
s=list(input())
ans=0
for i in range(10):
    if str(i) in s:
        first=s.index(str(i))
        for j in range(10):
            if str(j) in s[first+1:]:
                second=first+1+s[first+1:].index(str(j))
                for k in range(10):
                    if str(k) in s[second+1:]:
                        ans+=1
print(ans)