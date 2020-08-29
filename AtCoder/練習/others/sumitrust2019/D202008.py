n=int(input())
s=list(input())

ans=0
for i in range(10):
    if str(i) in s:
        first=s.index(str(i))
        ss=s[first+1:]
        for j in range(10):
            if str(j) in ss:
                sec=ss.index(str(j))

                for k in range(10):
                    if str(k) in ss[sec+1:]:
                        ans+=1

print(ans)
