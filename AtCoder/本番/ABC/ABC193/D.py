k=int(input())
s= list(map(int,list(input()[0:4])))
t= list(map(int,list(input()[0:4])))

cnt=[k for i in range(10)]
for i in range(4):
    cnt[int(s[i])] -= 1
    cnt[int(t[i])] -= 1
ans=0
for i in range(1,10):
    for j in range(1,10):
        if i==j:
            if cnt[i]<2:continue
        else:
            if cnt[i]<1 or cnt[j]<1:continue

        ci = [0 for i in range(10)]
        for q in range(4):
            ci[s[q]] += 1
        ci[i] += 1
        ss = 0
        for ii in range(1, 10):
            ss += ii * pow(10, ci[ii])

        ci = [0 for i in range(10)]
        for q in range(4):
            ci[t[q]] += 1
        ci[j] += 1
        tt = 0
        for ii in range(1, 10):
            tt += ii * pow(10, ci[ii])

        if ss>tt:
            add=0
            if i==j:
                add = (cnt[i]*(cnt[i]-1))/((k*9-8)*(k*9-9))
            else:
                add = (cnt[i]*cnt[j])/((k*9-8)*(k*9-9))
            ans += add

print(ans)