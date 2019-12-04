n=int(input())
s=list(map(int,list(input())))
ans=0
for i in range(10):
    try:
        ss=s[s.index(i)+1:]
        for j in range(10):
            try:
                sss=ss[ss.index(j)+1:]
                for k in range(10):
                    if k in sss:ans+=1
            except:pass
    except:pass

print(ans)